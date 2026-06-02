# Resume PM Rewriter

AI 产品经理 / B 端产品经理 / 大模型应用产品经理简历项目经历重构 skill。

## What It Optimizes

把执行动作型项目经历改写为可信的产品叙事：

> 业务问题 -> 产品判断 -> 机制设计 -> 价值闭环

适用于简历优化、项目经历改写、工作经历重写、resume rewrite、JD 匹配、AI 产品经理 / B 端产品经理岗位简历打磨。

## Default Output

默认一次性交付可用稿，而不是逐段等待确认：

```markdown
## 诊断
## 改写版
## 为什么这样改
## 面试追问
## 待确认补充
```

当用户明确说“逐条改 / 精修 / 一条条来”时，才进入逐条确认模式。

## Truth Boundary

改写必须区分：

- 原文已有事实
- 合理产品抽象
- 需确认补充

不得编造百分比、用户量、营收影响、上线状态或负责人级 ownership。缺失指标应放入“待确认补充”。

## Sharpness Pass

每次输出前会检查文案是否“正确但平淡”。如果只有痛点词、没有业务冲突、产品取舍、机制命名、状态跃迁或角色信号，就二次改写；但不通过编造指标或夸大 ownership 来制造锋利感。

## References

- `references/ai_pm_glossary.md`: AI PM 术语、机制表达、易混概念。
- `references/resume_patterns.md`: before/after 示例、平淡文案二次增强、常见劣化案例、项目类型模板。

## Optional Scripts

### JD Analyzer

用于用户提供目标 JD 时做关键词匹配，不是默认必跑流程。

```bash
python scripts/jd_analyzer.py --file jd.txt --resume resume.txt
```

### Market Scanner

保留为辅助脚本，但不作为默认流程依赖。需要市场趋势时，应优先使用当前来源或实时搜索，并说明依据。

```bash
python scripts/market_scanner.py --role "AI产品经理"
```

## Dependencies

```bash
pip install -r requirements.txt
```
