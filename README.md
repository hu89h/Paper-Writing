# Paper Writing Resources

科研论文写作工作区，用于维护写作、证据核验、审稿、图表和稿件交付相关的工具与参考资源。

## 资料入口

- [仓库接收、审查与维护工作流](workflows/resource-curation/WORKFLOW.md)：接收已提供的仓库，检查自身质量和现有重合，决定是否保留并登记作用。
- [已入库资源](resources/CATALOG.md)：资源导航，链接各库的内容说明。
- `resources/<作者>/<库名>.md`：对应资源的作用、保留内容、判断依据与限制。
- [资源删改与排除原因](resources/CHANGELOG.md)：影响资源选择的有效原因及重新考虑条件。
- [已接收仓库](resources/RECEIVED.md)与[模块线索](resources/RECEIVED_MODULES.md)：下载材料的导航，不代表入库。
- `third_party/<owner>/<repo>`：以 Git submodule 管理的上游源码。

入库范围以对应资源说明为准，不表示运行效果已验证或 Skill 已启用。未入库且没有处理结论的材料为待审候选。

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
git add -- third_party/Master-cai/Research-Paper-Writing-Skills resources
```

上游更新后，按维护工作流复查受影响的内容，必要时修改入库范围及原因记录，再提交实际 diff。

接收目录、各资源说明和删改原因直接维护，修改过程由 Git 记录。Agent 使用 Git 和文件工具核对 submodule、来源、工作区状态及链接。

## 资源使用

资源质量与重合度通过静态阅读检查，不实际运行候选资源。

本地材料放在 `.local/`，该目录由 Git 忽略，不参与共享。
