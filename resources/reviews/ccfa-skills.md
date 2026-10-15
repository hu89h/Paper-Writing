# CCFA-Skills 静态审查

- 来源：[mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills)；[本地材料](../../third_party/mikubaka88/CCFA-Skills/)。
- 日期：2026-10-15。
- 结论：**部分保留，作为首个入库资源**。保留六个写作相关模块的流程规范，以及两个共享依赖的适用规则，具体范围见[入库模块表](../MODULES.md)。不整体采用完整科研框架。
- 本次开始时已入库资源为空。其他已下载仓库均为待审材料；重合与替代检查记为**不适用**，不能据此宣称 CCFA 独特、最优或覆盖其他候选。
- 方法：只阅读本地源码和文档；未启用 Skill、未执行上游脚本、未安装依赖、未开展论文写作或实验。

## 接收与阅读范围

接收清单、上游来源及本地路径一致，材料可读；历史变更表没有对 CCFA 的有效入库或排除决定。仓库提供 17 个 `ccf-*` Skill 入口，另有模板与参考资料。

完整阅读 `ccf-common`、`ccf-humanization`、`ccf-paper-writer`、`ccf-paper-reviewer`、`ccf-integrity-auditor`、`ccf-paper-to-exemplar`、`ccf-rebuttal-writer`、`ccf-submission-checker` 的 `SKILL.md`。阅读写作的 `prose-quality-guardrails.md`、`citation-workflow.md`，Humanization 的 `humanization-policy.md`，审稿的 `fixed-output-format.md`，返修的 `revision-ledger.md`，以及共享的 `privacy-and-evidence.md`；抽读 `routing.md`、`section-modules.md`、会议指南索引和转换脚本 `convert.py`。

README 用于理解作者定位，决定依据以下列规则和代码为主。未逐份审查全部参考资料、模板、示例、脚本或测试；目录数量不构成质量证明。

## 自身质量与价值判断

下表“原文事实”描述材料中实际存在的要求；价值判断是基于这些规则的分析，不是执行效果结论。

| 内容 | 原文事实及定位 | 价值判断 |
| --- | --- | --- |
| 写作 | [writer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/SKILL.md) 的 `Modes`、`Workflow`：区分局部修改与整稿；保留事实、数值及引用键，未知事实留待补；[引用流程](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/references/citation-workflow.md)要求检查原文支持，而非只确认书目存在 | 不只是润色口号，有可复用的任务边界和证据约束；适合作为正文写作流程参考 |
| 审稿 | [reviewer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/SKILL.md) 区分写作／科学／完整／版本比较；[报告规范](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/references/fixed-output-format.md) 的 `Finding Record` 要求位置、证据、反证复核、判定和解决条件 | 可帮助把意见转成可核对的问题记录；没有据此证明模拟评审接近真实审稿结果 |
| 完整性核验 | [auditor](../../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) 的 `Core Rule`、`Workflow`：主张映射证据，检查数值及单位，区分不可比较与不一致，分开书目身份与上下文支持 | 核验对象和判定边界具体，能为写作提供证据检查框架；属于 Agent 规范，不能视为自动事实核验器 |
| 写作范例 | [exemplar](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/SKILL.md) 的 `Workflow`：基于全文与页码提炼写作动作，卡片保留来源及不得复制内容的边界，不能以摘要替代全文 | 有明确提炼结构及复用边界；可保留为范例整理方法 |
| 返修 | [rebuttal](../../third_party/mikubaka88/CCFA-Skills/ccf-rebuttal-writer/SKILL.md) 与 [revision-ledger](../../third_party/mikubaka88/CCFA-Skills/ccf-rebuttal-writer/references/revision-ledger.md) 将意见、承诺、实际修改位置、状态和证据关联；未发生的修改不得标完成 | 可支持回复与稿件一致性检查，减少仅在回复中声称完成的修改 |
| 投稿检查 | [submission-checker](../../third_party/mikubaka88/CCFA-Skills/ccf-submission-checker/SKILL.md) 的 `Check Scope`：区分通过、失败、不适用、未核验；要求当前官方规则及实际构建证据，缺工具不能推断通过或失败 | 检查方法有参考价值；具体政策和模板仍需单独核验 |
| 共享依赖 | [common](../../third_party/mikubaka88/CCFA-Skills/ccf-common/SKILL.md) 控制范围、产物及交接；[humanization-policy](../../third_party/mikubaka88/CCFA-Skills/ccf-humanization/references/humanization-policy.md) 要求保留真实限制、负面结果及不确定性，不机械删除限定词 | 有助于避免改写超出事实；这些共享入口也是理解上面六个模块的依赖，不能把业务入口当完全独立资源 |

综合判断：上述内容与论文写作直接相关，规则有实质且能定位到材料，值得按范围保留。理解和维护成本较高：业务模块依赖共享规则，并可能路由到未审模块；后续改版需同时检查受影响的共享文件。

## 缺点、默认策略与保留边界

| 事实／问题 | 依据 | 处理 |
| --- | --- | --- |
| 没有投稿目标及匹配指南时，整稿写作允许将 NeurIPS 指南／模板作为披露的起草假设 | [writer](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/SKILL.md) 的 `Workflow`；章节篇幅示例也偏 AI/ML | 不作为团队默认策略；保留写作方法不等于采用统一会议、学科或模板 |
| 对破折号有“优先零个、整篇最多三个”等偏好，写作规范偏向特定叙述方式 | [humanization-policy](../../third_party/mikubaka88/CCFA-Skills/ccf-humanization/references/humanization-policy.md) 的 `Consolidated Writing Constraints`；[prose-quality-guardrails](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/references/prose-quality-guardrails.md) 的 `Default voice` | 这些是风格偏好，静态材料没有证明其为普适质量标准；不作为硬门槛，保留事实与论证约束 |
| 共享文献政策要求 literature-searcher 排除 MDPI 来源 | [privacy-and-evidence](../../third_party/mikubaka88/CCFA-Skills/ccf-common/references/privacy-and-evidence.md) 的 `Literature Source Policy` | 固定出版来源排除不作为团队文献评价标准；检索模块未纳入本次通过范围 |
| 完整审稿默认十四节、写作审稿九节；格式校验不核验科学真伪 | [fixed-output-format](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/references/fixed-output-format.md) 的各报告 profile 与 `Deterministic Report Check` | 保留问题记录设计；固定报告有阅读与维护成本，不把结构合规或分数当作质量证明 |
| `convert.py` 的 `make_card()` 写入多个 `[ANALYZE]` 占位符，主流程打印 `Card skeleton`；Skill 另外要求完成实际分析 | [转换脚本](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/scripts/convert.py) 的 `make_card`、`main`；[Skill](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/SKILL.md) 的 `Workflow` | 脚本是提取与骨架辅助，不是自动写作分析实现；保留 Agent 分析流程，不声称脚本自动产出完整范例 |
| 会议指南索引中有 legacy、TBD 及需重新核验标记；本次未逐项验证指南和模板 | [venue-guides/index](../../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/references/venue-guides/index.md) | 具体投稿政策、会议归类、链接和模板不随本次通过；投稿检查仅保留方法层面 |
| 六个业务入口要求先加载 humanization、common，并有跨模块协作路由 | 各入口的 `Collaboration Contract`、[routing](../../third_party/mikubaka88/CCFA-Skills/ccf-common/references/routing.md) | 记录依赖，不把路由到的其他模块自动视为已审、已启用或质量合格；上游默认规则不会因本次入库而改写 |

没有发现足以否定上述受限流程参考价值的问题；这不等于证明整个仓库没有规则冲突。若要求原样启用全部默认行为，本次结论不足以支持。

## 未通过本次审查的范围

- **未审查／暂不入库：**`ccf-visual-composer`、`ccf-idea-reviewer`、`ccf-idea-optimizer`、`ccf-literature-searcher`、`ccf-literature-monitor`、`ccf-experiment-designer`、`ccf-pipeline-orchestrator`、`ccf-project-scaffolder`、`ccf-skill-forger`。前六类需要各自专项质量审查，后三类主要涉及完整科研组织、项目搭建和上游 Skill 维护；均不由本次写作流程审查推定质量。
- **未核验／不随本次入库：**具体会议指南、LaTeX 模板、未读参考材料及脚本的运行正确性。相关文件仍随完整上游原件保留。
- **明确不采用为团队统一规则：**未知目标时回退 NeurIPS、固定出版来源排除、机械标点与措辞门槛。

## 全流程结果与后续维护

接收材料可读 → 对写作相关范围完成静态检查 → 入库基准为空，重合检查不适用 → 决定部分保留 → 在入库目录、模块表和变更表登记 → 核对入口与记录并随本次修改提交本地 Git。

维护检查：接收导航重新生成；`scripts/verify_resources.py` 通过，核对 23 个上游仓库和 32 个接收入口；共享 Markdown 的 131 个本地链接存在；`git diff --check` 通过。以上检查针对本仓库的记录与链接，未执行候选代码。

判断限制：未验证实际写作效果、核验准确率、运行正确性、跨 Agent 适配或全部政策时效性。后续收到同类候选时，应与本次明确保留的具体内容比较，不与 CCFA 全仓库的宣传覆盖面比较。

重新检查的触发条件：共享规则或上述六个模块发生影响结论的变化；准备扩大保留范围；发现规则冲突、依赖缺失或同类已入库内容能够替代。修改、删除和恢复均在[变更记录](../CHANGELOG.md)追加原因，保留历史结论。
