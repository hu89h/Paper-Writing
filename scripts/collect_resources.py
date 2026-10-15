"""Maintain repositories listed in resources/repositories.json.

Run from any directory with Python 3.9+. Standard library only.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import os
import re
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'resources/repositories.json'


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def request(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Paper-Writing-Resource-Collector/1.0', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read(), response.geturl(), dict(response.headers)


def git(*args, cwd=ROOT, timeout=600):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_LFS_SKIP_SMUDGE='1')
    return subprocess.run(['git', '-c', 'core.longpaths=true', *args], cwd=cwd,
                          env=env, encoding='utf-8', errors='replace', capture_output=True, timeout=timeout)


def discover():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))['repositories']


def collect(item, offline=False):
    item = dict(item)
    name = item['name']
    if not offline:
        try:
            raw, final, _ = request('https://api.github.com/repos/' + name)
            meta = json.loads(raw)
            name = meta['full_name']
            item.update(name=name, url=meta['html_url'], clone_url=meta['clone_url'],
                        description=meta['description'], default_branch=meta['default_branch'],
                        archived=meta['archived'], upstream_updated_at=meta['pushed_at'],
                        github_size_kib=meta['size'], metadata_url=final)
            item.pop('metadata_error', None)
        except Exception as exc:
            item.update(metadata_error=str(exc))
    item.setdefault('url', 'https://github.com/' + name)
    item.setdefault('clone_url', 'https://github.com/' + name + '.git')
    item['path'] = 'third_party/' + name
    dest = ROOT / item['path']
    try:
        if not (dest / '.git').exists():
            if offline:
                raise RuntimeError('Repository is missing; initialize its submodule or rerun without --offline')
            dest.parent.mkdir(parents=True, exist_ok=True)
            result = git('clone', '--depth', '1', '--', item['clone_url'], str(dest))
            (ROOT / 'resources/logs').mkdir(parents=True, exist_ok=True)
            (ROOT / 'resources/logs' / (name.replace('/', '--') + '.log')).write_text(result.stdout + result.stderr, encoding='utf-8')
            if result.returncode:
                raise RuntimeError(result.stderr[-1600:])
        result = git('rev-parse', 'HEAD', cwd=dest)
        if result.returncode:
            raise RuntimeError(result.stderr)
        item.update(status='cloned', commit=result.stdout.strip())
        item.pop('error', None)
        tracked = git('ls-files', '-z', cwd=dest).stdout.split('\0')
        item['tracked_files'] = sum(bool(p) for p in tracked)
        item['skill_files'] = [p for p in tracked if Path(p).name == 'SKILL.md']
        item['lfs_pointers_may_be_unfetched'] = True
        item['nested_submodules_initialized'] = False
    except Exception as exc:
        item.update(status='failed', error=str(exc))
    item['checked_at_utc'] = datetime.now(timezone.utc).isoformat()
    print(json.dumps({k: item.get(k) for k in ('name', 'status', 'commit', 'metadata_error', 'error')}, ensure_ascii=False), flush=True)
    return item


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--register-submodules', action='store_true', help='Register fetched repositories in the parent Git index; does not commit.')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--offline', action='store_true', help='Inspect local repositories without network access or cloning.')
    args = parser.parse_args()
    items = discover()
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(collect, item, args.offline) for item in items]):
            results.append(future.result())
    if args.register_submodules:
        # The parent Git index is shared: registrations must be sequential.
        for item in results:
            if item['status'] != 'cloned':
                continue
            query = git('config', '-f', '.gitmodules', '--get', 'submodule.' + item['path'] + '.url')
            if query.returncode:
                result = git('submodule', 'add', '--', item['clone_url'], item['path'])
                item['submodule_registered'] = result.returncode == 0
                if result.returncode:
                    item['registration_error'] = result.stderr
            else:
                item['submodule_registered'] = True
            if item.get('submodule_registered'):
                git('config', '-f', '.gitmodules', 'submodule.' + item['path'] + '.shallow', 'true')
    write_json(MANIFEST, {'schema_version': 1,
                         'repositories': sorted(results, key=lambda item: item['name'].lower())})
    return int(any(item['status'] == 'failed' or item.get('submodule_registered') is False for item in results))


if __name__ == '__main__':
    raise SystemExit(main())
