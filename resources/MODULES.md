# 已入库模块

只列通过静态审查的具体内容，作为写作流程与检查规范参考。这里记录内容价值和边界，接入与实际使用另按任务处理。

## CCFA-Skills

| 内容入口 | 保留作用 | 保留边界 |
| --- | --- | --- |
| [ccf-paper-writer](../third_party/mikubaka88/CCFA-Skills/ccf-paper-writer/SKILL.md) | 分节写作、局部修改与压缩；保留原有事实、数值、引用键和用户格式，缺证据处明确待补 | 保留论证组织与证据约束；不采用未知投稿目标时回退 NeurIPS 的默认策略，不将章节篇幅或措辞偏好作为通用标准 |
| [ccf-paper-reviewer](../third_party/mikubaka88/CCFA-Skills/ccf-paper-reviewer/SKILL.md) | 将写作检查与科学审查分开；问题带位置、依据、反证复核与解决条件 | 固定报告结构是可参考的输出设计；模拟视角与分数不代表真实独立评审或接收概率 |
| [ccf-integrity-auditor](../third_party/mikubaka88/CCFA-Skills/ccf-integrity-auditor/SKILL.md) | 主张—证据映射，数值及口径一致性，书目身份与引用上下文支持分别核对 | 保留审计流程；实际覆盖率、检索准确率及判定可靠性未验证 |
| [ccf-paper-to-exemplar](../third_party/mikubaka88/CCFA-Skills/ccf-paper-to-exemplar/SKILL.md) | 从完整来源提炼写作动作，保留页码定位和禁止复制科研内容的边界 | 保留 Agent 分析流程和卡片结构；转换脚本只提供提取和含占位符的卡片骨架，不能视为自动完成写作分析 |
| [ccf-rebuttal-writer](../third_party/mikubaka88/CCFA-Skills/ccf-rebuttal-writer/SKILL.md) | 将审稿意见、回复承诺、修改位置及证据放入同一返修记录 | 只有实际修改可标完成；不由回复文字推定实验或修改已发生 |
| [ccf-submission-checker](../third_party/mikubaka88/CCFA-Skills/ccf-submission-checker/SKILL.md) | 区分格式、构建、材料交付；用通过／失败／不适用／未核验表述检查结果 | 仅保留检查方法，不认可随附模板及具体投稿政策的正确性或时效性 |
| [ccf-common](../third_party/mikubaka88/CCFA-Skills/ccf-common/SKILL.md) | 上述模块的共享依赖：范围、证据、产物位置及交接责任 | 保留适用的通用约束；跨模块路由不意味着未审模块也已入库；固定出版来源排除策略不作为团队文献标准 |
| [ccf-humanization](../third_party/mikubaka88/CCFA-Skills/ccf-humanization/SKILL.md) | 上述模块的共享依赖：保持事实与不确定性，减少空泛表达，避免机械删掉限定语 | 保留证据忠实和上下文判断；破折号数量、句式和作者主语偏好不作为通用质量门槛 |

其余九个 Skill、具体会议指南、LaTeX 模板和未读参考材料不随本次审查通过。未审内容与明确不采用的默认策略分别见[审查记录](reviews/ccfa-skills.md)。上游文件保持原样；保留范围由本表和审查记录限定。

## Research-Paper-Writing-Skills

来源：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)。[审查与对比依据](reviews/research-paper-writing-skills.md)。

| 内容入口 | 保留作用 | 保留边界 |
| --- | --- | --- |
| [Paragraph Clarity Check](../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/SKILL.md#paragraph-clarity-check-important) 与 [flow 参考](../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/does-my-writing-flow-source.md) | 读者视角检查术语和衔接；反向列出全文论点、段落主旨与支撑证据，检查对应关系 | 仅保留这一小节及参考方法；第一句主旨等是修订建议，不将全份 Skill 的输出规则一起采用 |
| [Method 指南](../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/method.md) 与 [overview 模板](../third_party/Master-cai/Research-Paper-Writing-Skills/research-paper-writing/references/examples/method/overview-template.md) | 模块化方法的分步起草、动机／设计／优势检查，overview 的设置与章节导航示例 | 与 CCFA 有覆盖重合，保留操作粒度与示例；适用 ML/CV 等模块化方法，示例科研事实和引用不可直接复用 |

其余分节指南和未读例库仍未审查；默认附加整套报告、通用实证接收判断和 novelty 叙述规则明确不采用为团队标准。

## ai-research-writing-skill

来源：[jin-s13/ai-research-writing-skill](https://github.com/jin-s13/ai-research-writing-skill)。[审查与对比依据](reviews/ai-research-writing-skill.md)。

| 内容入口 | 保留作用 | 保留边界 |
| --- | --- | --- |
| [研究交接契约](../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.md)、[schema](../third_party/jin-s13/ai-research-writing-skill/references/research-handoff.schema.json)、[check_research_handoff](../third_party/jin-s13/ai-research-writing-skill/scripts/check_research_handoff.py) | 研究问题、证据文件、定量必需项和未解决项的交接接口与结构检查设计 | 文件非空与 blockers 为空不证明科学正确；不强制采用该 JSON 格式 |
| [数值来源契约](../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.md)、[schema](../third_party/jin-s13/ai-research-writing-skill/references/numeric-evidence.schema.json)、[重算源码](../third_party/jin-s13/ai-research-writing-skill/scripts/check_numeric_evidence.py) | 来源选择、聚合和表示形式，以及 `load_registry` 等来源重算逻辑的设计参考 | 不通过 `find_unverified_numbers` 的完整稿件核验能力：数值未绑定具体指标／方法／稿件位置，扫描覆盖有限 |
| [产物契约](../third_party/jin-s13/ai-research-writing-skill/references/artifacts.md) 的构建部分与 [record_build](../third_party/jin-s13/ai-research-writing-skill/scripts/record_build.py) | 区分既有 PDF 与实际执行构建，记录命令、日志、返回码及来源状态 | 只保留构建记录设计；依赖收集不完整，Windows 命令兼容性及运行正确性未验证 |

上述脚本共享 [paper_contract.py](../third_party/jin-s13/ai-research-writing-skill/scripts/paper_contract.py)，交接检查还依赖数值登记检查；这些是参考源码的依赖，不是已经启用的工具链。整套写作合同、引用锁、模板与完整质量门禁不随本次通过。

全部已接收材料的定位线索见[接收模块线索](RECEIVED_MODULES.md)，处理历史见[变更记录](CHANGELOG.md)。本表由维护者直接更新。
