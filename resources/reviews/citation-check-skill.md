# citation-check-skill 静态审查

- 来源：[serenakeyitan/citation-check-skill](https://github.com/serenakeyitan/citation-check-skill)；[本地](../../third_party/serenakeyitan/citation-check-skill/)。
- 日期：2026-10-15；当前结论：**不保留为团队论文核验资源**。
- 历史：先前排除决定曾因误将待审候选当作已有覆盖而撤销，恢复待审。此次重新核对自身质量，以现已入库的范围比较，形成新的正式决定；不覆盖历史变更记录。
- 本次比较基准：CCFA、Master-cai 和 jin-s13 已明确入库的范围；没有把其他待审候选用作现成替代。
- 完整阅读当前本地 README、`SKILL.md` 与 `references/citation_schema.json`，核对跟踪文件列表；只做静态分析，没有执行资源或联网核验其示例。

## 内容与自身质量

该仓库提供两阶段的主张提取／核查提示词、联网与限定文档两种模式、图表核查提示及面向幻灯片的 JSON schema。先定位主张再核查、区分书目真实与句子支持关系、保留来源位置，均有参考价值。

以下位置按章节定位，避免将易随上游更新漂移的行号作为唯一依据。

| 源码事实 | 原文位置 | 判断及后果 |
| --- | --- | --- |
| 只提取规定的主张类型，明确不提取方法描述，例子是所用 PyTorch 版本 | [SKILL](../../third_party/serenakeyitan/citation-check-skill/SKILL.md) 的 `Claim Extraction Rules` | 方法、软件版本及设置也可能是应核对事实，不能将该提取范围作为完整论文审计范围 |
| 任意舍入、截断、有效位数变化均判错；百分数与等价小数被列为单位不匹配；近似表达又允许来源值的 ±10% | 同文件 `Numerical Precision Rules`、`Tie-Breaker Rules` | 没有结合指标、单位换算及报告精度给出可用的通用判定规则，近似例外与严格规则的优先级不清楚 |
| 只有 Rank 5–6 二手来源时要求未核验；另一表允许至少两个独立二手来源一致即通过 | `Source Authority Hierarchy` 对照 `Multi-Source Verification` | 同类输入存在互不一致的操作指示，与确定性判定的设计目标不符 |
| 来源冲突时一处要求未核验，另一处要求采用最新权威来源 | `Multi-Source Verification` 对照 `Tie-Breaker Rules` | 缺少冲突时的优先级和可比性判据，不能仅按年份推定哪个结论适用于原主张 |
| 正文判定包括 Numerical Error、Citation Not Found、Misquoted、Not in Source，schema 的 status 只有 verified、unverified、hallucination、misleading | [SKILL](../../third_party/serenakeyitan/citation-check-skill/SKILL.md) 的 `Status Decision Tree`、`Output Format Options`；[schema](../../third_party/serenakeyitan/citation-check-skill/references/citation_schema.json) 的 `slides.items.properties.claims.items.properties.status` | JSON 模式缺少明确映射，输出接口与规则不闭合；这是可由静态材料直接核对的缺陷 |
| schema 围绕 slides、slide_number 和 presentation_title，README 同时宣称覆盖研究论文、报告及 PDF | 同一 schema 与 README 的 `What it does` | 论文适配需要额外设计，不能把现成 schema 视为通用稿件核验格式 |
| 跟踪文件仅有 README、SKILL、schema 等文档，没有配套核验执行脚本或测试 | 跟踪文件列表；SKILL 的 `Design principle` | “相同输入相同输出”是作者目标，未由实现或结果证明；也不能由缺少代码反推出提示词一定无效 |

这些问题涉及核心提取范围、判定规则和输出接口，足以独立支持此次不保留决定，不依赖“其他库已经做过”这一理由。

## 与当前已入库内容的对照

| 比较点 | 已入库依据 | 共同内容、区别及处理 |
| --- | --- | --- |
| 重要主张、数值与引文上下文核对 | [CCFA integrity auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) 的 `Core Rule`、`Modes`、`Workflow` | 已有证据矩阵、数值口径及身份／支持关系分离的检查方法。候选的逐页文档索引和视觉检查更具体，但没有证明这些细节已被全部覆盖，不用“完全重复”作为排除理由 |
| 数字来源及聚合重算 | [jin-s13 保留范围](ai-research-writing-skill.md) | jin-s13 提供来源重算设计，同时本库已明确否定其数字集合匹配能证明语义正确；该已知缺陷不被隐藏，也不因两者同属核验就判定可直接替代 |
| 局部写作检查 | [Master-cai 保留范围](research-paper-writing-skills.md) | 不承担 citation-check 的完整核验功能，不作为其替代依据 |

候选中有益的普通核查思路与现有规范重合，其文档索引、两阶段提取和报告布局仍有不同侧重。本次没有选择拆出这些局部建议新增专项条目：其增量不足以支持承担核心规则和格式修订的维护成本。这是范围与价值判断，不是断言其没有任何独特内容。

## 决定与后续处理

- 不在已入库资源和模块表登记；原始仓库继续在接收材料清单中，避免为了记录排除而删除源码。
- 在[变更记录](../CHANGELOG.md)追加正式排除原因，并保留先前决定及撤销记录；日后再次收到此来源先查最新有效记录。
- 重新考虑的条件：协调来源和数值判定规则，明确适合论文的提取范围，补齐状态映射与输出契约；或提供可独立保留的专项内容及其价值依据。届时只复核受影响部分，不要求重新搜集资源。
- 这是同一 Agent 的静态复核，没有运行准确率、确定性或跨模型效果验证。
