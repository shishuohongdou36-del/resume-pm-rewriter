# Resume Rewrite Patterns

Use this reference when a resume rewrite needs examples, anti-patterns, or project-type templates. Keep final resume text shorter than these examples; this file teaches the pattern, not the exact wording.

## High-Quality Before / After

### Example 1: RAG Knowledge Base

**Before**

> 负责保险知识库建设，整理产品条款，优化检索效果，支持客服问答系统上线。

**After**

> RAG 知识边界重构：针对保险产品条款相似度高、人工口径维护分散（乱）、检索依据易漂移（偏）的问题，设计产品级元数据标签与分层检索策略，将原始文档检索升级为可过滤、可约束、可追溯的知识调用机制，降低跨产品误召回与无依据生成风险。

**Why it works**

- Names the business object: insurance product clauses.
- Explains the pain: similar clauses, scattered manual maintenance, drifting evidence.
- Shows product mechanism: metadata tags and layered retrieval.
- Keeps the value credible without inventing a metric.

### Example 2: Agent Workflow

**Before**

> 参与 AI Agent 系统设计，配置多个工具和流程，提升用户处理效率。

**After**

> Agent 任务编排升级：针对多步骤业务咨询依赖人工判断、任务流转断点多（断）、处理口径不可复用（散）的问题，设计意图识别、工具调用与状态续接机制，将固定问答流程升级为可路由、可编排、可复用的 Agent 服务链路，支撑复杂咨询任务的连续承接。

**Why it works**

- Does not say `提升效率` alone.
- Turns tool configuration into a product mechanism.
- Avoids claiming full ownership if the source only says `参与`.

### Example 3: Quality Evaluation

**Before**

> 优化大模型回答质量，整理 bad case，做了一些测试集。

**After**

> 质量评测闭环建设：针对大模型回答问题难归因、修正后难回归（黑盒）的问题，建立 `模型预判 -> 人工复核 -> 差异归因 -> 修正 -> 回归验证` 的评测链路，将单次问题修复升级为可度量、可归因、可回归的质量治理机制。

**Why it works**

- Keeps the concrete workflow steps because they prove the mechanism exists.
- Uses `bad case` as evidence for quality governance, not as a loose buzzword.
- Leaves dataset size for the result section if the user provides it.

## Common Degradation Patterns

| Weak Pattern | Why It Fails | Better Move |
|---|---|---|
| `负责/参与/协助` stacked at the start of every bullet | Sounds like a task list, not product ownership. | Start with capability module or business mechanism. |
| `使用 RAG/Agent/Prompt` without explaining the problem | AI jargon does not prove product judgment. | Tie every AI term to a pain point and quality boundary. |
| `提升效率/体验/准确率` without object or mechanism | Empty value claim. | Name what became faster, clearer, more stable, or more controllable. |
| Invented metrics like `提升 30%` | Creates credibility risk. | Use `待确认补充` for metrics not in source material. |
| Every bullet uses the same formula | Looks generated and stiff. | Vary openings: scenario, mechanism, state change, quality loop. |
| Over-abstracted language | Interviewer cannot ask concrete follow-ups. | Preserve enough workflow detail to defend the claim. |

## Bland-To-Strong Upgrade

Use this section when a draft is technically correct but still feels plain.

### Upgrade Levers

| Lever | Bland Draft Usually Says | Stronger Draft Adds |
|---|---|---|
| Business tension | `优化流程` | Why the old flow could not balance speed, accuracy, compliance, scale, or control. |
| Product judgment | `设计方案` | Why this mechanism was chosen and what trade-off it handled. |
| Mechanism identity | `负责某功能` | A product-module name such as `策略配置化`, `意图路由`, `质量回归闭环`. |
| State transition | `提升效果` | `from old state -> to new state`, with the object being changed. |
| Role signal | `参与项目` | The candidate's actual judgment: abstraction, coordination, validation, boundary definition. |
| Interview hook | `完成建设` | A specific mechanism that can be challenged in an interview. |

### Example: Too Plain

**Source**

> 负责内容生成工具优化，支持运营人员生成不同渠道的营销文案。

**Plain but weak**

> 内容生成效率优化：针对运营文案生成慢、质量不稳定的问题，优化内容生成流程，提升多渠道营销文案产出效率。

Why it is weak:

- `优化流程` does not show the product mechanism.
- `提升效率` has no object or boundary.
- There is no product judgment or old/new state transition.

**Sharper**

> 多渠道生成策略重构：针对运营文案依赖人工经验、渠道语气难区分（同质）、复核成本高（慢）的问题，设计场景标签、渠道模板与审核约束机制，将单次提示词生成升级为可配置、可复用、可复核的内容生产链路，支撑不同渠道营销素材的稳定产出。

Why it works:

- Adds business tension: speed vs channel differentiation vs review control.
- Names mechanism: scenario tags, channel templates, review constraints.
- Shows state transition: one-off prompt generation -> configurable production chain.

### Example: Product Judgment

**Source**

> 做了客服机器人意图识别和知识库问答，减少人工客服压力。

**Plain but weak**

> 智能客服能力建设：通过意图识别和知识库问答能力，提升客服机器人服务效率，减少人工客服压力。

**Sharper**

> 智能客服路由机制设计：针对咨询入口混杂、业务问题与知识问答边界不清（乱）、复杂问题易被单轮问答误承接（错）的问题，设计意图分层、知识问答与人工转接边界，将统一问答入口拆解为可路由、可拒答、可升级的服务分发机制，降低机器人越权回答与人工重复分流成本。

Why it works:

- The mechanism is not just `意图识别`; it explains routing and escalation boundaries.
- The value is sharper because it names avoided risk.
- It creates interview follow-ups: how to define transfer boundary, how to handle refusal.

### Example: Quality Loop

**Source**

> 负责模型效果评估，整理测试数据，推动问题修复。

**Plain but weak**

> 模型评估体系建设：整理测试数据并推动问题修复，提升模型输出质量。

**Sharper**

> 模型质量回归闭环：针对模型问题修复依赖人工经验、错误原因难定位（黑盒）、版本迭代后难验证（难回归）的问题，建立测试集分层、Bad Case 归因与回归验证机制，将经验式调优升级为可复测、可归因、可沉淀的质量治理流程。

Why it works:

- It turns evaluation from a task into a repeatable quality mechanism.
- It avoids fake metrics while still showing maturity.
- It makes the candidate look like someone who understands AI product quality operations.

### Too Much: Over-Packaging Warning

**Overdone**

> 主导企业级大模型战略转型，构建全链路智能化质量治理平台，全面提升公司 AI 能力。

Why it fails:

- Claims strategy, platform scope, and company-level impact without evidence.
- Sounds impressive but fragile under interview questioning.

**Safer**

> 质量评测闭环建设：围绕[具体模型/业务场景]建立测试集分层、Bad Case 归因与回归验证机制，支撑模型迭代后的问题复测与质量沉淀。

## Sharpness Checklist

Before finalizing a resume draft, ask:

- Can the interviewer see the business contradiction in the first half of the bullet?
- Does the bullet show a product mechanism rather than only a task?
- Is there a clear old-state -> new-state transition?
- Does the wording reveal product judgment or only execution effort?
- If every adjective were removed, would the claim still stand?
- Is the sharpest claim supported by the source facts?

## Project-Type Templates

Adapt these templates only when the source facts support them.

### RAG / Knowledge Governance

> [能力模块]：针对[业务知识对象]存在[相似/分散/漂移/不可追溯]等问题，通过[元数据治理/分层检索/权限或边界约束/引用强绑定]，将[原检索或维护方式]升级为[可过滤/可约束/可追溯]的知识调用机制，降低[误召回/错答/合规]风险。

Good module names:

- RAG 知识边界重构
- 检索策略分层治理
- 知识元数据标签体系
- 检索强绑定与拒答机制

### Agent / Workflow Orchestration

> [能力模块]：针对[业务任务]在[多步骤/跨系统/多角色]场景下[断点多/口径散/人工判断重]的问题，设计[意图路由/工具调用/状态续接/Skill 编排]机制，将[固定流程或人工承接]升级为[可路由/可编排/可复用]的服务链路。

Good module names:

- Agent 服务路由设计
- Skill 标准化沉淀
- 多轮状态续接机制
- 复杂流程任务编排

### Quality Evaluation / Bad Case Governance

> [能力模块]：针对[模型或系统输出]存在[难归因/难复现/难回归/不可观测]的问题，建立[评测集/人工复核/差异归因/回归验证]机制，将[单点修复]升级为[可度量/可归因/可回归]的质量治理闭环。

Good module names:

- 质量评测闭环
- Bad Case 归因体系
- LLM Judge 与人工抽检机制
- 质量回归验证链路

### B2B Platform / Configuration

> [能力模块]：针对[业务规则/流程策略]依赖人工维护、变更成本高（慢）、复用性弱（散）的问题，设计[策略配置化/权限分层/规则引擎/流程模板]能力，将[硬编码或线下流转]升级为[可配置/可复用/可审计]的平台机制。

Good module names:

- 策略配置化能力建设
- 业务规则产品化
- 权限与流程边界治理
- 平台能力复用机制

### Data / Monitoring / Observability

> [能力模块]：针对[关键业务过程]缺乏过程指标与异常定位能力（黑盒），设计[指标口径/埋点链路/看板/告警/归因维度]，将[结果后验判断]升级为[过程可观测/异常可定位/问题可追溯]的运营或质量监控机制。

Good module names:

- 过程可观测体系
- 指标口径治理
- 异常归因看板
- 质量监控闭环

## Result Section Patterns

Use results only when facts are available. If numbers are missing, keep placeholders explicit.

- **效果提升**：将[对象]从[原状态]提升至[新状态]；如有真实数据，补充[指标口径 + 时间范围 + 数值]。
- **能力沉淀**：沉淀[模板/规则/评测集/标签体系/配置能力]，支撑后续复用。
- **后续扩展**：为[渠道/业务线/场景]扩展提供[接口/流程/方法论/质量基线]。

## Interview Follow-Up Patterns

For each final bullet, generate at least one follow-up question:

- Why was this mechanism chosen instead of a simpler workflow?
- Which part was deterministic rule handling, and which part needed model reasoning?
- What was the boundary condition or failure case?
- How did you know the result improved?
- What would you change if this scaled to more business lines?
