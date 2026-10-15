# ai-research-writing-skill 静态审查

- 来源：[jin-s13/ai-research-writing-skill](https://github.com/jin-s13/ai-research-writing-skill)；[本地](../../third_party/jin-s13/ai-research-writing-skill/)。
- 日期：2026-10-15；原状态：已接收、未审查，没有有效删除或排除记录。
- 结论：**部分保留为接口、证据契约与实现设计参考**：研究到写作的交接、来源数值重算，以及区分既有 PDF 与实际构建的记录设计。不将整套 Skill 或质量门禁通过。
- 比较基准：决定前已入库的 CCFA 与 Master-cai 的明确保留范围。
- 静态分析，不运行候选脚本、测试、示例或 Skill，也不建立候选要求的项目状态文件。

## 已读范围与依赖

完整阅读 `SKILL.md`、`references/numeric-evidence.md` 及其 schema、`references/research-handoff.md` 及其 schema、`references/artifacts.md`、`scripts/README.md`、`scripts/check_numeric_evidence.py`、`scripts/check_research_handoff.py`、`scripts/record_build.py`；阅读 README 的定位及来源关系，`paper_contract.py` 的文本读取、TeX／图像收集和构建输入记录函数，抽读质量门禁的构建状态检查及相关测试片段。

三个已读工具直接依赖 `paper_contract.py`；交接检查还调用数值登记校验。这些关系影响判断，因此一并追读。引用锁、在线文献核验、图表生成、模板获取及整套质量门禁未完整审查，不随本次通过。示例结果和测试文件的存在不算本次验证结果。

## 自身质量及边界

| 源码事实与位置 | 价值判断／限制 |
| --- | --- |
| [research-handoff](../../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.md) 定义问题、论文类型、目标及证据文件；[schema](../../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.schema.json) 与 [validate_handoff](../../third_party/jin-s13/ai-research-writing-skill/scripts/check_research_handoff.py) 区分定量必需材料和 blockers，并检查路径、非空及数值来源 | 提供从上游研究到论文写作的具体接口示例；路径存在、非空和 blockers 为空不能证明科研事实真实、实验完整或上游没有漏报问题 |
| [numeric-evidence](../../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.md)、[schema](../../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.schema.json) 和 [load_registry / _selected_values / _aggregate](../../third_party/jin-s13/ai-research-writing-skill/scripts/check_numeric_evidence.py) 将来源、选择条件、聚合方法与表示形式分开；源码包含均值、标准差等重算逻辑 | 比“填写来源路径”更具体，可作为数值溯源与重算设计参考；不能由此推断稿件主张成立 |
| 同一脚本的 `find_unverified_numbers` 只要任一 `EvidenceValue.matches` 命中数值便放行，没有绑定稿件位置、方法、指标或实验条件 | **关键限制：**它验证的是数值集合匹配，不是逐项语义归属；不保留为能证明正文／表格用对数值的自动检查器 |
| 数值覆盖由英文 `STRICT_SECTION_TERMS` 和表格正则选择；共享 `collect_tex_text` 按收集文件顺序拼接文本 | 覆盖不是整稿语义解析，中文章节、宏、复杂 LaTeX 结构与跨文件节结构需另外判断；没有结果错误率数据 |
| [record_build](../../third_party/jin-s13/ai-research-writing-skill/scripts/record_build.py) 区分 `artifact-only` 与 `executed`，记录实际命令、日志、返回码与输入／输出状态；[artifacts](../../third_party/jin-s13/ai-research-writing-skill/references/artifacts.md) 要求最终提交状态有实际构建 | 区分“文件存在”和“构建确实发生”有具体实现价值。`build.status` 单字段不足以判定，必须连同 attestation 等信息理解 |
| `paper_contract.paper_input_files` 自动收集范围是 TeX 引入、图像和 bibliography；`record_build` 用默认 `shlex.split` 解析命令 | 并非完整 LaTeX 依赖图，本地样式文件等不由该收集函数自动发现；Windows 命令路径及引号兼容性未验证。仅保留记录设计，不能认定构建工具已适配本环境 |
| [SKILL 的 Execution Contract / Gates](../../third_party/jin-s13/ai-research-writing-skill/SKILL.md) 对整稿要求状态文件、任务包和多类产物，示意图默认偏图像生成 | 有明确但较重的生产流程；不作为本资源库维护流程，也不把这些默认要求整体引入团队写作 |

数值归属限制可由源码推导一个反例：已登记 A、B 两方法的数值，稿件将两者对调时，两处数字仍可能各自匹配证据集合。这里是未执行的静态反例，不是一次失败测试；来源重算正确也无法消除该限制。

## 与已入库范围的重合及增量

| 已入库内容 | 相同点 | 本候选的保留增量 |
| --- | --- | --- |
| [CCFA integrity auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) | 都要求数字有来源、口径一致，且不编造结果 | 候选有具体 selector／aggregate 契约与重算源码，补充实现设计；不替代 CCFA 所要求的语义和上下文核对 |
| [CCFA submission checker](../../third_party/mikubaka88/CCFA-Skills/ccf-submission-checker/SKILL.md) | 都区分实际构建和既有文件 | 候选给出命令、日志、返回码及构建记录的数据设计；不因此认定其依赖覆盖或 Windows 执行正确 |
| CCFA 的证据与交接约束 | 都要求携带材料、范围和未解决项 | 候选给出研究到写作的字段、条件必需项和校验代码，可供接口设计参考；不强制团队采用其文件格式 |
| [Master-cai 已保留的段落与 Method 参考](research-paper-writing-skills.md) | 都涉及论文组织 | 不再登记其通用写作模板作为增量。候选 README 明示受到 Master-cai 启发；共同建议不当成独立来源验证 |

以上增量指相对于本次核对范围的具体化程度，不证明整个 CCFA 仓库都没有同类实现，更不构成运行效果排名。

## 决定与复查条件

[模块表](../MODULES.md#ai-research-writing-skill) 只登记三组参考内容。数值脚本的稿件扫描门禁、全局质量门禁、引用工具、生成图策略及整份 Skill 的执行合同均未作为可原样采用的方案通过；未读部分保持未审状态。

若后续准备采用数值检查器，需先解决数值与稿件位置／方法／指标的归属问题，并明确覆盖范围。若准备采用构建工具，需检查实际依赖和 Windows 命令处理。当前均不运行；这些是扩大保留或使用范围时需处理的问题，不是此次维护任务。

修改所保留契约、校验逻辑或共享解析依赖时复查受影响部分。保留理由是具体接口和实现设计的参考价值，不能用“仅供参考”掩盖对完整自动核验能力的否定；该能力本次没有通过。
