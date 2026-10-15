# Repository Guidelines

## 项目范围

本仓库是团队论文写作工作区。具体学科、投稿目标和写作流程以对应论文项目的要求为准，不预设统一期刊或模板。

## 共享资料

- README、资源索引、脚本和配置面向所有协作者，只记录项目用途、公开资源和可复用的操作说明。
- 沟通记录、个人资料及临时来源笔记放在 `.local/`；该目录不纳入 Git。
- 共享文件不引用 `.local/` 中的材料，运行脚本不依赖该目录。

## 资源维护

- 搭建或修改资源调研工作流时，只调整流程规范与模板，不默认开始评审资源。
- 执行资源搜集、整理、汇总、筛选或价值判定前，先读 [资源调研工作流](workflows/resource-curation/WORKFLOW.md)，按任务单、阶段规范和交接条件推进。
- `third_party/` 使用 Git submodule 管理上游资源；不要在资源整理任务中直接修改上游源码。
- `resources/repositories.json` 是资源维护脚本的输入。变更后重新生成索引并运行 `scripts/verify_resources.py`。
- 下载资源不等于启用 Skill。根据实际任务选择模块，再阅读其规则和依赖。
- Windows 环境使用 PowerShell；文本使用 UTF-8 编码。
