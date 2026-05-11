# Resume PM Rewriter

AI产品经理 / B端产品经理 / 大模型应用产品经理简历项目经历重构 Skill。

## 核心能力

将项目经历从"执行动作堆砌"重构为"**业务痛点抽象—产品判断—机制设计—价值闭环**"的高级简历表达。

## 工作流程

```
输入项目经历
    ↓
核心矛盾提炼 → 痛点词提炼 → 解法机制提炼 → 可突出能力判断
    ↓
项目总述（稳健版/锋利版）→ 用户确认
    ↓
逐条 Bullet 改写（每条含逐词能力映射）→ 用户逐条确认
    ↓
成果段 → 最终整合版
    ↓
同步输出面试追问题文件
```

## 核心机制

| 机制 | 说明 |
|------|------|
| **颗粒度三层控制** | 总述讲矛盾、Bullet讲机制、成果段讲数据，严格分层 |
| **痛点词规范** | "原因（结果词）"格式，原因与结果语义不重复 |
| **逐词能力映射** | 每条 Bullet 的模块名逐词解释体现什么PM能力 |
| **面试题联动** | 每条 Bullet 确认后同步写入面试追问题文件 |
| **总述差异化** | 同一简历多个项目不同句式结构，避免同质化 |
| **JD 关键词匹配** | 通过脚本解析目标 JD，提取关键词指导简历用词 |
| **市场趋势扫描** | 搜索当前 AI PM 市场热词与能力要求，保持简历竞争力 |

## 目录结构

```
resume-pm-rewriter/
├── SKILL.md                 # Skill 主文件
├── README.md                # 说明文档
├── scripts/
│   ├── jd_analyzer.py       # JD 解析与关键词提取
│   └── market_scanner.py    # AI PM 市场趋势扫描
└── references/
    └── ai_pm_glossary.md    # AI 产品经理术语表与用法参考
```

## 脚本使用

### JD 解析

```bash
# 从 URL 解析 JD
python scripts/jd_analyzer.py --url "https://example.com/job/12345"

# 从本地文件解析
python scripts/jd_analyzer.py --file jd.txt

# 与简历内容对比，输出匹配度
python scripts/jd_analyzer.py --file jd.txt --resume resume.txt
```

### 市场趋势扫描

```bash
# 扫描 AI 产品经理岗位热词
python scripts/market_scanner.py --role "AI产品经理"

# 指定平台
python scripts/market_scanner.py --role "AI产品经理" --platform boss

# 输出 markdown 报告
python scripts/market_scanner.py --role "AI产品经理" --output report.md
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 触发方式

在 Windsurf / Claude 中使用以下触发词：

> 简历优化、简历润色、项目经历改写、帮我改简历、写简历、简历重构、resume rewrite、项目描述优化

## License

MIT
