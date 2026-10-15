# Research-Paper-Writing-Skills 静态审查

- 来源：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)；[本地](../../third_party/Master-cai/Research-Paper-Writing-Skills/)。
- 日期：2026-10-15；原状态：已接收、未审查，没有有效删除或排除记录。
- 结论：**部分保留为写作参考材料**，保留段落检查、反向提纲、Method 分步组织方法及一个 overview 模板；不将整份 Skill 的执行规则整体通过。
- 比较基准：本次决定前已入库的 CCFA 写作、审稿范围。后续候选不作为现成替代。
- 只做静态阅读，未激活 Skill 或运行候选内容。

## 阅读范围与自身质量

完整阅读 README、`research-paper-writing/SKILL.md`、`references/does-my-writing-flow-source.md`、`references/method.md`、`references/paper-review.md` 和 `references/examples/method/overview-template.md`；抽读 Introduction 的任务开场、technical challenge 与增量叙述提示。其他分节指南、例库及引用原论文未逐项核验。

| 事实与原文 | 判断及影响 |
| --- | --- |
| [SKILL 的 Paragraph Clarity Check](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/SKILL.md#paragraph-clarity-check-important) 明确检查读者是否理解术语与句间关系；反向列出全文论点、段落主旨及证据，再核对两层对应关系 | 提供可直接理解的修订步骤，有局部写作参考价值；不能证明能提高实际投稿表现 |
| [flow 参考](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/does-my-writing-flow-source.md) 解释读者视角、反向提纲、临时标题与过渡关系 | 反向提纲有实际内容支撑；该文件自称 PDF 提取，但没有在文件中给出可直接核对的原 PDF 来源，不能将其作为独立权威证据 |
| [method 指南](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/method.md) 将结构与执行步骤、模块动机及优势分开，并给出先写设计再补动机的起草顺序；[overview 模板](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/examples/method/overview-template.md) 将设置、贡献及章节导航对应到示例 | 适合 ML/CV 等模块化方法稿件的结构参考；示例里的方法事实、引用编号及句子不能直接移入新稿 |
| [SKILL 的 Execution Rules / Output Contract](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/SKILL.md) 默认附提纲、段落角色、自审表和逐条主张证据映射 | 对局部改写有额外输出负担，不作为团队默认交付要求 |
| [paper-review](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/paper-review.md) 把实验支持作为所有主要主张的强制条件，并强调超过已有方法的实证表现和消融 | 主要适合实证 ML/CV 稿件；不适用于所有论文类型，也不能当作通用接收标准。本次不保留这套整稿判定规则 |
| [introduction](../../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/introduction.md) 的 `Part B` 提醒即使研究是增量工作，也避免以朴素基线的补丁方式叙述 | 可理解为呈现建议，但不能据此淡化真实研究关系、夸大创新；相关 novelty 叙述规则不随本次通过 |

README 明示主要方法来自公开研究笔记，贡献在整理和 Skill 包装。这里保留的是组织后的操作参考，不声称其是独立研究证据。

## 与已入库范围的比较

| 比较点 | 已入库原文 | 候选增量与处理 |
| --- | --- | --- |
| 段落主旨、衔接、术语与证据 | [CCFA section-modules 的 Small Paragraph Edit Mode](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/references/section-modules.md#small-paragraph-edit-mode) 已包含这些检查 | 大部分目的相同；候选明确给出“全文论点—段落主旨—证据”的反向提纲步骤，可作为简洁的检查参考。未证明这一方法在 CCFA 全仓中独有或缺失 |
| Method 的动机、设计与优势 | 同一 CCFA 文件的 `Method` 已有三者组织要求 | 不登记为新能力；只保留候选的分步起草顺序及 overview 示例，补充操作粒度 |
| 整稿审查与主张核对 | 已入库 [CCFA reviewer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/SKILL.md) 和 [integrity auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) 已分别覆盖 | 候选的实证偏向与整稿自审默认不值得再作为通用标准并列入库；这不代表 CCFA 运行效果更好 |

## 决定与维护边界

保留位置以[模块表](../MODULES.md)为准，层级为具体小节和参考文件；上游完整原件保持原样。其余分节指南及未读例库未审查，整份执行／输出合同、通用接收判断和 novelty 叙述默认不随本次通过。

本决定的依据是内容具体性、与目标的关联及补充粒度，不是仓库数量、声望或“独特能力”数量。后续同类候选出现时，应比较反向提纲步骤或范例组织本身；若同等内容已被更清晰的已入库材料覆盖，可缩小或删除本条，并记录原因。

静态检查不能判断真实写作改善、完整例库准确性或全部规则自洽性。没有引入新的机器状态或安装要求；登记、记录与本次 Git 提交共同构成此次维护。
