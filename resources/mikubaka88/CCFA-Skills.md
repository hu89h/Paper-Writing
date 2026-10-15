# CCFA-Skills

[上游](https://github.com/mikubaka88/CCFA-Skills) · [本地源码](../../third_party/mikubaka88/CCFA-Skills/)

部分保留，作为论文写作与检查的流程参考。它将写作、审稿、证据核验和返修分别组织，适合从已有研究材料推进稿件；完整科研框架未整体采用。

## 保留内容

| 内容 | 作用及保留边界 |
| --- | --- |
| [paper-writer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/SKILL.md) | 分节写作、局部修改和压缩，保留事实、数字、引用键及用户格式；缺失证据明确待补。不采用未知投稿目标时回退 NeurIPS 的默认策略 |
| [paper-reviewer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/SKILL.md) | 分开写作检查、科学审查与版本比较；问题带位置、依据、反证复核及解决条件。模拟视角和分数不代表真实独立评审或接收概率 |
| [integrity-auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) | 主张—证据映射，检查数字、单位和口径，分开书目身份与引用上下文支持；保留审计方法，实际核验准确率未验证 |
| [paper-to-exemplar](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/SKILL.md) | 从全文提炼写作动作，保留页码、来源和不得复制科研内容的边界；[convert.py](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/scripts/convert.py) 的 `make_card` 生成含 `[ANALYZE]` 的骨架，不是自动完成范例分析 |
| [rebuttal-writer](../../third_party/mikubaka88/CCFA-Skills/ccf-rebuttal-writer/SKILL.md) | 将意见、回复承诺、修改位置、状态和证据关联；只有实际修改才可标完成，具体结构见 [revision-ledger](../../third_party/mikubaka88/CCFA-Skills/ccf-rebuttal-writer/references/revision-ledger.md) |
| [submission-checker](../../third_party/mikubaka88/CCFA-Skills/ccf-submission-checker/SKILL.md) | 区分格式、构建与交付检查，分别报告通过、失败、不适用及未核验；仅保留检查方法，具体会议政策和模板未获认可 |
| [common](../../third_party/mikubaka88/CCFA-Skills/ccf-common/SKILL.md) 与 [humanization](../../third_party/mikubaka88/CCFA-Skills/ccf-humanization/SKILL.md) | 上述模块的共享依赖，保留范围、证据、交接和事实忠实等适用规则；跨模块路由不自动使未审模块通过 |

## 保留理由与限制

规则具体到主张支持、审稿问题记录和返修闭环，而不止要求“写得更好”。[引用流程](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/references/citation-workflow.md) 明确书目存在不等于支持句子；[审稿格式](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/references/fixed-output-format.md) 要求反证复核，并声明格式检查不能验证科学真伪。这些是静态内容价值，不是效果证明。

下列默认策略不作为团队标准：[humanization-policy](../../third_party/mikubaka88/CCFA-Skills/ccf-humanization/references/humanization-policy.md) 的机械标点和措辞偏好，[privacy-and-evidence](../../third_party/mikubaka88/CCFA-Skills/ccf-common/references/privacy-and-evidence.md) 对 literature-searcher 的固定出版来源排除，以及整稿写作的 NeurIPS 回退策略。

其余九个 Skill、具体会议指南、LaTeX 模板和未读参考资料仍未审查。依赖共享规则使维护成本较高；共享规则或保留模块发生实质变化时，应复查受影响范围。未运行、未启用 Skill，也未验证写作效果或跨 Agent 适配。
