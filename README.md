# Paper Writing Resources

科研论文写作工作区，用于维护写作、证据核验、审稿、图表和稿件交付相关的工具与参考资源。

## 资料入口

- [仓库接收、审查与维护工作流](workflows/resource-curation/WORKFLOW.md)：接收已提供的仓库，检查自身质量和现有重合，决定是否保留并登记作用。
- [资源变更记录](resources/CHANGELOG.md)：入库、修改、删除、排除和恢复的原因与依据。
- [已入库资源](resources/CATALOG.md)：通过静态审查的资源、保留理由及范围。
- [已入库模块](resources/MODULES.md)：通过审查的具体内容及适用边界。
- [已接收仓库](resources/RECEIVED.md)与[模块线索](resources/RECEIVED_MODULES.md)：下载材料的导航，不代表入库。
- [机器可读接收清单](resources/repositories.json)：上游 URL、获取状态及全部 `SKILL.md` 路径。
- `third_party/<owner>/<repo>`：以 Git submodule 管理的上游源码。

入库表示指定范围具有静态内容参考价值，不表示运行效果已验证或 Skill 已启用。已接收但未入库的材料继续作为候选保留。

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

上游更新后，按维护工作流复查受影响的内容，必要时修改入库范围及原因记录，再提交实际 diff。收集脚本以公开资源清单为输入，补齐缺少的仓库并记录现有 checkout，不自动升级已有资源。`--offline` 只检查本地资源；省略该选项可刷新 GitHub 元数据并获取缺少的仓库。

`build_catalog.py` 只生成 `RECEIVED.md` 和 `RECEIVED_MODULES.md`。`CATALOG.md`、`MODULES.md` 及 `CHANGELOG.md` 由维护者直接更新；两个 JSON 文件记录已接收材料，不承担入库状态管理。

```powershell
python -X utf8 scripts/verify_resources.py
```

该检查核对 Git submodule、工作区状态和模块入口存在性，不运行第三方代码。

## 资源使用

资源质量与重合度通过静态阅读检查，不实际运行候选资源。

本地材料放在 `.local/`，该目录由 Git 忽略，不参与共享。
