"""Generate received-material indexes; admission records are maintained in Markdown."""
from pathlib import Path
import json
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    '正文写作与审校': {
        'Master-cai/Research-Paper-Writing-Skills': '论文结构、段落逻辑与改写',
        'K-Dense-AI/claude-scientific-writer': '跨学科科学写作工具及规则',
        'WenyuChiou/academic-writing-skills': '学术写作、稿件修订与审稿',
        'Hiro-Inagawa/paper-audit-skill': '论文审校规则',
        'Odinary-AI/research-writing-skill': '通用学术写作流程',
        'PoseZhaoyutao/research-paper-writer-skill': '论文写作与多角色工作流参考',
        'Norman-bury/research-writing-skill': '模块化写作流程参考',
        'zLanqing/codex-claude-academic-skills': '学术写作与配套工具参考',
    },
    'LaTeX、证据与稿件交付': {
        'appautomaton/latex-arxiv-SKILL': 'LaTeX 论文工作流，实际适用范围需按任务确认',
        'yunshenwuchuxun/latex-paper-skills': 'LaTeX 写作与实验结果回填参考',
        'jin-s13/ai-research-writing-skill': '数值证据、引用锁与构建记录',
        'ShaishavMaisuria/research-paper-lifecycle-skills': '引用、结果、主张核验与稿件预检',
    },
    '审稿、文献与图表专项': {
        'Rezenders/scientific_writing_agent': '增量审稿、技术段落与实现对照',
        'Yuan1z0825/nature-skills': '论文精读、文献核验、写作与数据工具',
        'Haojae/scipilot-figure-skill': '科研数据图制作与检查',
        'serenakeyitan/citation-check-skill': '引用核查提示词与 schema 参考',
    },
    '完整科研框架与工具库（按模块参考）': {
        'mikubaka88/CCFA-Skills': '科研全流程与写作／审查模块',
        'K-Dense-AI/scientific-agent-skills': '跨学科科学工具库',
        'wanshuiyin/Auto-claude-code-research-in-sleep': '自主科研与实验／论文审计参考',
        'Orchestra-Research/AI-Research-SKILLs': 'AI 研究工具与论文写作模块',
        'Galaxy-Dawn/claude-scholar': '文献管理、知识库与科研工作流',
        'WUBING2023/PaperSpine': '完整论文生产工作台',
        'brycewang-stanford/Auto-Empirical-Research-Skills': '大型实证研究方法与工具汇编',
    },
}


def relative_link(path):
    return urllib.parse.quote('../' + path, safe='/.-_')


def main():
    data = json.loads((ROOT / 'resources/repositories.json').read_text(encoding='utf-8'))
    repos = {item['name']: item for item in data['repositories']}
    groups = {title: {name: purpose for name, purpose in entries.items() if name in repos}
              for title, entries in GROUPS.items()}
    classified = {name for entries in groups.values() for name in entries}
    if set(repos) - classified:
        groups['未分类'] = {name: '待整理说明' for name in sorted(set(repos) - classified)}
    lines = ['# 已接收仓库清单', '',
             f'收集范围：{len(repos)} 个上游仓库。文件列表来自本地源码；来源链接已通过 GitHub API 和实际克隆核对。', '',
             '分类和用途是导航摘要，不构成功能效果排名。`SKILL.md` 数量是跟踪文件数，可能包含重复打包的同一 Skill，不等于独立能力数量。', '',
             '上游链接与完整文件清单见 [repositories.json](repositories.json)。', '',
             '此页由脚本生成，只记录已接收材料；正式保留范围见 [已入库资源](CATALOG.md)，处理历史见 [资源变更记录](CHANGELOG.md)。未入库材料的当前状态以变更记录中最新有效结论为准；没有有效结论的资源为待审候选。', '']
    for title, entries in groups.items():
        if not entries:
            continue
        lines += ['## ' + title, '', '| 仓库／本地入口 | 导航用途 | SKILL.md 文件数 |', '| --- | --- | ---: |']
        for name, purpose in entries.items():
            item = repos[name]
            lines.append(f'| [{name}]({item["url"]}) · [本地]({relative_link(item["path"])}) | {purpose} | {len(item.get("skill_files", []))} |')
        lines.append('')
    lines += ['## 获取与使用状态', '',
              '- 所有仓库均已下载并注册为 Git submodule；未安装依赖、未启用 Skill、未执行上游代码。',
              '- 采用浅克隆；未递归初始化上游子模块，Git LFS 内容可能仍是指针文件。',
              '- 资源尚未经过统一写作任务、核验准确率或运行效果测试。',
              '- 两个不同 owner 的 `research-writing-skill` 均在接收清单中，未因同名而合并。', '']
    (ROOT / 'resources/RECEIVED.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    modules = json.loads((ROOT / 'resources/modules.json').read_text(encoding='utf-8'))
    lines = ['# 已接收材料的模块线索', '',
             '以下入口仅核对本地文件存在，供定位待审内容，不表示已入库。通过审查的内容与边界见 [已入库模块](MODULES.md)，处理历史见 [资源变更记录](CHANGELOG.md)。', '',
             '脚本入口只提供定位；运行前阅读其输入约定、依赖与副作用。引用元数据核验与“原文是否支持当前主张”是不同任务，需分别验证。', '']
    for module in modules:
        item = repos[module['repo']]
        lines += ['## ' + module['task'], '', f'上游：[{module["repo"]}]({item["url"]})。', '']
        for path in module['paths']:
            full = item['path'] + '/' + path
            assert (ROOT / full).is_file(), full
            lines.append(f'- [{path}]({relative_link(full)})')
        lines.append('')
    (ROOT / 'resources/RECEIVED_MODULES.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print(f'Generated RECEIVED.md and RECEIVED_MODULES.md: {len(repos)} repositories, {len(modules)} module groups.')


if __name__ == '__main__':
    main()
