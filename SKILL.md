---
name: resume-pm-rewriter
description: Use when revising resumes, rewriting project experience, improving resume bullets, aligning AI product manager or B2B product manager experience with a JD, or turning execution-heavy descriptions into product-impact language. Trigger on 简历优化, 简历润色, 项目经历改写, 工作经历重写, resume rewrite, CV rewrite, JD匹配, AI产品经理简历, B端产品经理简历. Do not use for non-resume writing such as articles, reports, or marketing copy.
---

# AI Product Resume Rewriter

Use this skill to rewrite AI product manager, B2B product manager, and large-model application product manager resume experience. The goal is not prettier wording; it is a credible shift from execution notes to a product story: business problem, product judgment, mechanism design, and value loop.

## Operating Modes

Default to **one-pass delivery** unless the user explicitly asks for iterative refinement.

- **One-pass delivery**: output a complete usable draft in one response: `诊断`, `改写版`, `为什么这样改`, `面试追问`, `待确认补充`.
- **Refinement mode**: if the user says `逐条改`, `精修`, `一条条来`, `先别整合`, or similar, work one section or bullet at a time and wait for confirmation before continuing.
- **File output**: do not create or update an interview-question file by default. Only write a file when the user explicitly asks to save one and provides or confirms a path.

## Inputs To Recognize

Support these common input shapes:

- Project experience only.
- Project experience plus target role or JD.
- Multiple projects plus a resume target.
- A rough bullet list that needs rewriting into resume-ready language.

If key information is missing, still produce a draft, but mark assumptions and missing facts in `待确认补充`. Do not block unless the project cannot be understood at all.

## Rewrite Lens

For each project, infer and express:

1. Business object and scenario.
2. Original pain points.
3. Product mechanism, architecture method, or strategy design.
4. State change from old process/system to new process/system.
5. Business value, system capability, or quality-control outcome.

Every final bullet should carry this structure implicitly: **problem -> method -> mechanism -> value**.

## Sharpness Pass

After the first draft, run a sharpness pass before responding. This is the main guard against bland output.

A bullet is bland if it only contains pain-point words but lacks at least one of these signals:

- **Business tension**: the concrete contradiction behind the work, such as accuracy vs coverage, automation vs compliance, scale vs control, speed vs quality.
- **Product judgment**: why this mechanism was chosen instead of a simpler workflow, manual rule, or pure model call.
- **Mechanism identity**: a named capability that sounds like a product module, not a task label.
- **State transition**: what changed from old state to new state.
- **Role signal**: what product judgment, coordination, or ownership the candidate actually demonstrated.

Repair bland bullets with one or two of these levers, not all of them:

1. Put the business contradiction earlier.
2. Replace generic verbs (`优化`, `支持`, `建设`, `打通`) with a mechanism verb (`治理`, `重构`, `编排`, `收敛`, `配置化`, `归因`, `回归`).
3. Name the product mechanism before describing details.
4. Add an old-state -> new-state transition.
5. Make the role signal explicit without exaggerating ownership.
6. Remove decorative jargon that does not create an interview follow-up.

If the source material is thin, produce a solid restrained draft and list the missing facts needed to make it sharper. Do not create false sharpness by inventing scope, metrics, or decision authority.

## Truth Boundary

Separate facts from interpretation.

- **原文已有事实**: details explicitly present in the user's material.
- **合理产品抽象**: higher-level wording that faithfully summarizes the facts.
- **需确认补充**: numbers, scope, ownership, production status, business impact, or causal claims not proven by the source text.

Never invent percentages, user counts, revenue impact, model scores, release status, or ownership level. If the source says only `参与`, do not rewrite it as `主导` unless the context proves ownership. If a metric is missing, write a metric placeholder or ask for the real number in `待确认补充`.

## Output Format

For one-pass delivery, use this structure:

```markdown
## 诊断
- 核心问题:
- 可强化信号:
- 风险提醒:

## 改写版
### 项目总述
[for bland or high-stakes material, provide both 稳健版 and 锋利版, then recommend one]

### 项目 Bullet
- [bullet 1]
- [bullet 2]
- [bullet 3]

### 成果段
- 效果提升:
- 能力沉淀:
- 后续扩展:

## 为什么这样改
| 原始表达 | 改写策略 | 传递的产品能力 |
|---|---|---|

## 面试追问
- [question] - 考察点: [point]

## 待确认补充
- [missing fact or metric]
```

Keep the final resume copy concise enough to paste into a resume. Put explanation outside the resume copy.

## Granularity Rules

- **Project summary**: explain business contradiction, architecture direction, and value combination. Do not put detailed metrics or field lists here.
- **Bullets**: explain capability modules and mechanism design. Keep key process steps if removing them would make the mechanism vague.
- **Results section**: carry metrics, capability assets, reuse value, and follow-up expansion. If metrics are absent, mark the exact missing metric.

## Language Rules

- Prefer dense product language: `治理`, `重构`, `分层`, `路由`, `编排`, `配置化`, `闭环`, `可观测`, `可归因`, `可回归`, `可追溯`.
- Pain-point wording should include cause plus compressed result: `人工创作依赖经验（慢）`, `缺乏场景与渠道区分（同质）`.
- Avoid semantic repetition: `无差异化（同质）` is weak because the cause and result say the same thing.
- Vary sentence structure across projects. Do not make every summary start with `面向`.
- Avoid empty claims such as `提升用户体验`, `优化流程`, `提高效率` unless the mechanism and object are clear.
- Avoid jargon stacking. AI terms must explain what business or quality problem they solved.

## Quality Rubric

Before finalizing, check the draft against this rubric:

| Dimension | Pass Criteria |
|---|---|
| 岗位匹配度 | Uses role-relevant terms naturally, especially from a provided JD. |
| 业务抽象 | Names the business object, scenario, and contradiction. |
| 机制清晰度 | Shows the product mechanism or architecture method, not just actions. |
| 面试可追问性 | Each bullet can support concrete follow-up questions. |
| 语言密度 | Concise, resume-ready, not essay-like. |
| 表达锋利度 | Contains business tension, product judgment, state transition, or a clear role signal. |
| 可信度 | No fabricated metrics, ownership, or release status. |
| 过度包装风险 | Does not turn support work into strategic leadership without evidence. |

If any dimension is weak, fix the draft or call out the risk in `待确认补充`.

## Optional References And Tools

- Read `references/ai_pm_glossary.md` when terminology, AI product concepts, or mechanism names need precision.
- Read `references/resume_patterns.md` when examples, anti-patterns, or project-type templates would help.
- Use `scripts/jd_analyzer.py --file jd.txt --resume resume.txt` only when the user provides a JD or asks for JD matching. Treat its output as keyword guidance, not as a mandatory scoring gate.
- Do not rely on `scripts/market_scanner.py` for the default workflow. If market trend alignment is requested, use current sources/search results and cite or summarize the source basis.
