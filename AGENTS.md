# Repository Guidelines

## 项目范围

本仓库是团队论文写作工作区。具体学科、投稿目标和写作流程以对应论文项目的要求为准，不预设统一期刊或模板。

## 共享资料

- README、资源索引、脚本和配置面向所有协作者，只记录项目用途、公开资源和可复用的操作说明。
- 沟通记录、个人资料及临时来源笔记放在 `.local/`；该目录不纳入 Git。
- 共享文件不引用 `.local/` 中的材料，运行脚本不依赖该目录。

## 资源维护

- 搭建或修改仓库审查工作流时，只调整流程规范与模板，不默认开始评审资源。
- 本工作流从已经提供的仓库开始。审查、入库或删改前，先读 [仓库接收、审查与维护工作流](workflows/resource-curation/WORKFLOW.md)。按任务选择所需环节，简单维护不必填写全套模板。
- 新增前查看 [资源变更记录](resources/CHANGELOG.md)；删改时记录具体原因，避免重复引入曾排除的资源。恢复时追加新依据，保留旧记录。
- 质量检查只做静态分析，不实际运行候选资源。完成一次完整维护后，将相关修改和记录一并提交到本地 Git，不捎带无关改动。
- `third_party/` 使用 Git submodule 管理上游资源；不要在资源整理任务中直接修改上游源码。
- `resources/CATALOG.md` 和 `resources/MODULES.md` 手工记录已入库范围；待审候选不作为已有入库资源参与重合判断。
- `resources/repositories.json` 和 `resources/modules.json` 是已接收材料的脚本输入。变更后重新生成 `resources/RECEIVED.md` 与 `resources/RECEIVED_MODULES.md`，并运行 `scripts/verify_resources.py`；生成脚本不改写入库记录。
- 下载资源不等于启用 Skill。根据实际任务选择模块，再阅读其规则和依赖。
- Windows 环境使用 PowerShell；文本使用 UTF-8 编码。
