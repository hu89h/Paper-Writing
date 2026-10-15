# Paper Writing Resources

科研论文写作工作区，用于维护写作、证据核验、审稿、图表和稿件交付相关的工具与参考资源。

## 资料入口

- [仓库接收、审查与维护工作流](workflows/resource-curation/WORKFLOW.md)：接收已提供的仓库，检查自身质量和现有重合，决定是否保留并登记作用。
- [资源变更记录](resources/CHANGELOG.md)：入库、修改、删除、排除和恢复的原因与依据。
- [资源分类索引](resources/CATALOG.md)：23 个仓库的用途与入口。
- [重点模块索引](resources/MODULES.md)：写作、数值证据、引用核验、增量审稿、绘图等具体文件位置。
- [机器可读清单](resources/repositories.json)：上游 URL、获取状态及全部 `SKILL.md` 路径。
- `third_party/<owner>/<repo>`：以 Git submodule 管理的上游源码。

分类用于导航，不代表工具效果排名。使用具体模块前，阅读其说明并配置所需依赖。部分仓库覆盖完整科研流程，可按任务选择其中的写作与审查模块。

## 获取与维护

Windows PowerShell，文本文件使用 UTF-8。

克隆团队仓库后，获取资源：

```powershell
$env:GIT_LFS_SKIP_SMUDGE = '1'
git submodule update --init --depth 1
```

只获取一个资源时，可以指定路径：

```powershell
git submodule update --init --depth 1 -- third_party/Master-cai/Research-Paper-Writing-Skills
```

以上命令不递归初始化上游子模块，并跳过 Git LFS 大文件下载。模型、数据集、API 凭证和运行依赖按模块说明单独配置。

需要主动检查并升级某个上游时：

```powershell
git -C third_party/Master-cai/Research-Paper-Writing-Skills fetch --depth 1 origin main
git -C third_party/Master-cai/Research-Paper-Writing-Skills checkout --detach FETCH_HEAD
python -X utf8 scripts/collect_resources.py --offline --register-submodules
python -X utf8 scripts/build_catalog.py
git add -- .gitmodules third_party/Master-cai/Research-Paper-Writing-Skills resources
```

提交前检查实际 diff。收集脚本以公开资源清单为输入，补齐缺少的仓库并记录现有 checkout，不自动升级已有资源。`--offline` 只检查本地资源；省略该选项可刷新 GitHub 元数据并获取缺少的仓库。

```powershell
python -X utf8 scripts/verify_resources.py
```

该检查核对 Git submodule、工作区状态和模块入口存在性，不运行第三方代码。

## 资源使用

资源质量与重合度通过静态阅读检查，不实际运行候选资源。

本地材料放在 `.local/`，该目录由 Git 忽略，不参与共享。
