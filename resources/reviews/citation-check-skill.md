# citation-check-skill 静态审查

- 资源：[serenakeyitan/citation-check-skill](https://github.com/serenakeyitan/citation-check-skill)
- 日期：2026-10-15
- 处理结果：**不保留为通用论文引文核验资源**，从重点模块入口移除。
- 阅读范围：完整阅读当前工作区的 README、`SKILL.md` 和 `references/citation_schema.json`；未运行候选资源，未调用其核验流程。
- 历史检查：审查前的变更表中没有该资源的排除、删除或恢复记录。

## 内容与可取之处

该仓库提供引文和事实核查提示词，以及以幻灯片为中心的输出 schema。流程包括先提取主张再逐条核验、联网核查和限定文档核查两种模式、来源定位和报告格式。

先提取主张再核查、区分来源存在与来源支持主张、在报告中保留出处，均有参考价值。依据为 [SKILL.md](../../third_party/serenakeyitan/citation-check-skill/SKILL.md) 的 `Two-Pass Architecture`、`Status Decision Tree` 和 `Output Format`。

在当前仓库的跟踪文件列表中，未发现配套核验执行脚本或测试文件。因此，其“相同输入得到相同输出”的表述属于设计目标，不能仅凭这些提示词认定已经实现确定性验证。

## 自身质量检查

以下行号对应当前工作区文件，用于定位原文。

| 发现 | 原文位置 | 对本项目的影响 |
| --- | --- | --- |
| 数值规则把任意舍入和有效位数变化判为错误，后面的近似值规则又接受一定偏差 | `SKILL.md` L159–194、L318 | 没有按具体指标和表达精度确定容差，规则优先级也不清楚，不宜作为通用论文核验标准 |
| 主张提取排除方法描述，示例是所用软件版本 | `SKILL.md` L75–85 | 论文的方法、软件版本和实验设置本身也可能是需要核对的事实；不能把该排除表直接用于整篇论文审计 |
| 仅有二手来源时，一处要求未核验，另一处允许两个独立二手来源通过；来源冲突时也同时存在“未核验”和“采用最新来源”的要求 | `SKILL.md` L278–318 | 对相同情形存在不同处理指示，与其减少判断分歧的目标不一致 |
| 正文定义多种结果，但 JSON schema 的 claim status 仅允许四种 | `SKILL.md` L115–121、L155、L402–404；[citation_schema.json](../../third_party/serenakeyitan/citation-check-skill/references/citation_schema.json) L62–65 | `Numerical Error`、`Citation Not Found`、`Misquoted`、`Not in Source` 等没有对应枚举或明确映射，结构化输出约定不完整 |
| schema 主要围绕 slides，而资源描述同时覆盖论文、PDF 和报告 | `citation_schema.json` L6、L39–47 | 对通用论文场景需要另外适配；不能把该 schema 直接视为通用稿件核验格式 |

这些是静态规则与接口层面的发现，不是运行失败率或写作效果测试结果。

## 与现有内容的重合及差异

比较范围限定为以下已有内容，并非对全部资源做完整审查。对照内容本身也未因此自动获得入库通过结论。

| 能力 | 已有对照内容 | 对比结论 |
| --- | --- | --- |
| 主张、数字、引文身份及上下文支持核验 | [CCFA integrity auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md)，`Core Rule`、`Modes`、`Workflow` | 已提供主张—证据矩阵和多类一致性检查；还明确区分不可比较与不一致，核心问题范围重合 |
| 提取候选主张并整理证据矩阵 | [lifecycle verify-claims](../../third_party/ShaishavMaisuria/research-paper-lifecycle-skills/skills/verify-claims/SKILL.md)，`Process`、`Hard rules` | 已有候选提取、定位、证据映射与状态区分，并明确脚本提取不等于判定真伪；查阅了脚本头部说明和函数位置，未运行或完整验证脚本 |
| 引用记录是否真实、元数据是否匹配 | [lifecycle verify-citations](../../third_party/ShaishavMaisuria/research-paper-lifecycle-skills/skills/verify-citations/SKILL.md)，`Inputs`、`Process`、`Hard rules` | 存在专门的书目核验规范和配套脚本，但这只说明已有同类材料，不代表该工具已经验证可用，也不等于核验句子支持关系 |

候选资源的限定文档页码索引、幻灯片视觉检查提示和报告布局具有不同侧重。本次没有证明这些内容在所有现有资源中都被覆盖；但其独立增量不足以抵消上述通用核验规则和输出约定的问题。

## 处理决定及边界

- 从重点模块入口中移除，避免被误当作已筛选的通用核验资源。
- 原始仓库继续作为已接收材料留在本地收集清单中，记录排除原因；不修改上游文件。
- 现有对照项只作为后续审查的相关对象，不将它们宣称为实测更好的替代工具。
- 若上游协调数值与来源判定规则、补齐状态 schema，并体现明确的独立价值，可以重新审查；恢复时保留本次原因。

关键问题在完整读完候选文件后重新核对了一遍，属于单个 Agent 的静态复核，不是独立评审或运行验证。
