"""Check actual Git state, resource origins, and indexed entry points."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import configparser
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args, cwd=ROOT):
    return subprocess.run(['git', *args], cwd=cwd, capture_output=True, encoding='utf-8', errors='replace', check=True).stdout.strip()


def verify(item):
    errors = []
    path = ROOT / item['path']
    try:
        actual = git('rev-parse', 'HEAD', cwd=path)
        if actual != item['commit']:
            errors.append(item['path'] + ': checkout differs from manifest')
        if git('status', '--porcelain', cwd=path):
            errors.append(item['path'] + ': upstream working tree has modifications')
        if git('remote', 'get-url', 'origin', cwd=path) != item['clone_url']:
            errors.append(item['path'] + ': origin differs from manifest')
        for skill in item['skill_files']:
            if not (path / skill).is_file():
                errors.append(item['path'] + ': missing ' + skill)
    except Exception as exc:
        errors.append(item['path'] + ': ' + str(exc))
    return errors


def main():
    records = json.loads((ROOT / 'resources/repositories.json').read_text(encoding='utf-8'))['repositories']
    modules = json.loads((ROOT / 'resources/modules.json').read_text(encoding='utf-8'))
    paths = {item['path'] for item in records}
    by_name = {item['name']: item for item in records}
    errors = []
    config = configparser.ConfigParser(interpolation=None)
    config.read(ROOT / '.gitmodules', encoding='utf-8')
    registered = {config[section]['path'] for section in config.sections()}
    if registered != paths:
        errors.append('Manifest and .gitmodules differ: ' + str(registered.symmetric_difference(paths)))
    index = {}
    for row in git('ls-files', '--stage').splitlines():
        mode, sha, stage, path = re.split(r'\s+', row, maxsplit=3)
        if path.startswith('.local/'):
            errors.append('Local-only material is tracked: ' + path)
        if mode == '160000':
            index[path] = sha
    if set(index) != paths:
        errors.append('Git index submodules differ from manifest')
    for item in records:
        if item['status'] != 'cloned' or not item.get('submodule_registered'):
            errors.append(item['name'] + ': collection incomplete')
        if index.get(item['path']) != item['commit']:
            errors.append(item['path'] + ': staged gitlink differs from manifest')
    for module in modules:
        for path in module['paths']:
            if not (ROOT / by_name[module['repo']]['path'] / path).is_file():
                errors.append('Module entry missing: ' + module['repo'] + '/' + path)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(verify, records):
            errors.extend(result)
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(records)} repositories, fixed commits, origins, Git index, clean upstream checkouts, local-only material isolation and {sum(len(x["paths"]) for x in modules)} module entry points.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
