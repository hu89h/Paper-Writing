# ai-research-writing-skill

[上游](https://github.com/jin-s13/ai-research-writing-skill) · [本地源码](../../third_party/jin-s13/ai-research-writing-skill/)

部分保留为研究交接、数值溯源与构建记录的契约和实现设计参考。完整 Skill 与稿件自动质量门禁未整体通过。

## 保留内容

| 内容 | 作用及保留边界 |
| --- | --- |
| [research-handoff](../../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.md)、[schema](../../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.schema.json)、[check_research_handoff](../../third_party/jin-s13/ai-research-writing-skill/scripts/check_research_handoff.py) | 问题、证据文件、定量必需项和未解决项的交接接口及结构校验；路径存在、非空和 blockers 为空不证明科研事实真实或材料完整，不强制采用其 JSON 格式 |
| [numeric-evidence](../../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.md)、[schema](../../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.schema.json)、[来源重算代码](../../third_party/jin-s13/ai-research-writing-skill/scripts/check_numeric_evidence.py) | 来源选择、聚合和表示形式的契约，以及 `load_registry`、`_selected_values`、`_aggregate` 的重算设计；不通过 `find_unverified_numbers` 的完整稿件核验能力 |
| [artifacts 的构建部分](../../third_party/jin-s13/ai-research-writing-skill/references/artifacts.md) 与 [record_build](../../third_party/jin-s13/ai-research-writing-skill/scripts/record_build.py) | 区分既有 PDF 和实际执行构建，关联命令、日志、返回码及输入输出状态；仅保留记录设计，依赖完整性和 Windows 兼容性未验证 |

代码直接依赖 [paper_contract.py](../../third_party/jin-s13/ai-research-writing-skill/scripts/paper_contract.py)；交接检查还调用数值登记校验。这些关系影响所保留设计，修改时需连同相关依赖核对。

## 保留理由与已知问题

相对 [CCFA](../mikubaka88/CCFA-Skills.md) 的证据核对与投稿检查规范，这里提供了具体字段、来源选择与聚合逻辑，以及构建记录代码，补充实现粒度。README 明示受 [Master-cai](../Master-cai/Research-Paper-Writing-Skills.md) 启发，通用写作建议不另当独立依据或新能力保留。

数值检查器在 `find_unverified_numbers` 中只要任一证据值匹配就放行，未绑定稿件位置、方法、指标和实验条件。由代码可推断：两个已登记方法的数字在稿件中互换，仍可能匹配证据集合。因此，来源重算不等于语义归属正确；这是静态反例，不是已运行测试。覆盖还受到英文章节名和表格正则的限制。

`paper_contract.paper_input_files` 自动收集 TeX 引入、图像和 bibliography，并非完整 LaTeX 依赖图；`record_build` 使用默认 `shlex.split` 分词，Windows 路径及引号处理需另核对。不能仅凭构建状态字段宣称整个稿件已正确构建。

## 不采用与未审范围

数值集合匹配门禁、整份 Skill 的状态文件和任务包要求不作为团队默认方案。引用锁、在线文献核验、图表生成、模板获取及完整质量门禁未完整审查，不随这些局部设计通过。

未运行脚本、测试、示例或 Skill。若准备扩大保留范围，应先解决数值语义归属、扫描覆盖、构建依赖及 Windows 命令处理等相关问题。
