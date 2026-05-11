"""
JD Analyzer — 解析目标岗位 JD，提取关键词与能力要求，指导简历用词。

用法:
    python jd_analyzer.py --url "https://example.com/job/12345"
    python jd_analyzer.py --file jd.txt
    python jd_analyzer.py --file jd.txt --resume resume.txt
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装依赖: pip install requests beautifulsoup4 lxml")
    sys.exit(1)


# AI 产品经理岗位高频关键词库（按类别）
KEYWORD_CATEGORIES = {
    "AI能力": [
        "大模型", "LLM", "RAG", "Agent", "Workflow", "Prompt",
        "NLP", "知识图谱", "向量检索", "语义理解", "意图识别",
        "多轮对话", "Fine-tune", "RLHF", "GPT", "Claude",
        "embedding", "token", "上下文窗口", "幻觉", "对齐",
    ],
    "产品能力": [
        "产品设计", "需求分析", "用户体验", "产品规划", "产品策略",
        "竞品分析", "数据分析", "A/B测试", "MVP", "PRD",
        "产品迭代", "产品生命周期", "商业化", "增长",
    ],
    "架构与机制": [
        "架构设计", "系统设计", "流程设计", "策略设计",
        "可配置", "可扩展", "可复用", "模块化",
        "评测体系", "质量闭环", "归因", "回归",
    ],
    "业务场景": [
        "B端", "企业级", "SaaS", "PaaS", "中台",
        "客服", "营销", "风控", "审核", "核保",
        "保险", "金融", "医疗", "教育", "电商",
    ],
    "协作与管理": [
        "跨部门", "项目管理", "技术沟通", "推动落地",
        "0到1", "从0到1", "全流程", "端到端",
    ],
}

ALL_KEYWORDS = []
KEYWORD_TO_CATEGORY = {}
for cat, words in KEYWORD_CATEGORIES.items():
    for w in words:
        ALL_KEYWORDS.append(w.lower())
        KEYWORD_TO_CATEGORY[w.lower()] = cat


def fetch_url(url: str) -> str:
    """从 URL 抓取页面文本内容"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "lxml")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    return soup.get_text(separator="\n", strip=True)


def extract_keywords(text: str) -> dict:
    """从文本中提取关键词并分类统计"""
    text_lower = text.lower()
    found = Counter()

    for kw in ALL_KEYWORDS:
        count = text_lower.count(kw)
        if count > 0:
            found[kw] = count

    categorized = {}
    for kw, count in found.most_common():
        cat = KEYWORD_TO_CATEGORY[kw]
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append({"keyword": kw, "count": count})

    return categorized


def extract_requirements(text: str) -> list:
    """提取 JD 中的能力要求条目"""
    lines = text.split("\n")
    requirements = []

    requirement_patterns = [
        r"^\d+[\.\、\)]",
        r"^[-•·▪]",
        r"^（?\d+）",
        r"^[a-zA-Z][\.\)]",
    ]

    in_requirement_section = False
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if any(kw in line for kw in ["任职要求", "岗位要求", "职位要求", "要求", "资格", "Requirement", "Qualification"]):
            in_requirement_section = True
            continue

        if any(kw in line for kw in ["岗位职责", "工作职责", "职责描述", "Responsibility"]):
            in_requirement_section = False
            continue

        if in_requirement_section or any(re.match(p, line) for p in requirement_patterns):
            cleaned = re.sub(r"^[\d\.\、\)\-•·▪（）a-zA-Z]+\s*", "", line)
            if len(cleaned) > 5:
                requirements.append(cleaned)

    return requirements


def match_resume(jd_keywords: dict, resume_text: str) -> dict:
    """将 JD 关键词与简历内容匹配，输出覆盖率"""
    resume_lower = resume_text.lower()
    matched = {}
    missed = {}

    for cat, keywords in jd_keywords.items():
        matched[cat] = []
        missed[cat] = []
        for item in keywords:
            if item["keyword"] in resume_lower:
                matched[cat].append(item["keyword"])
            else:
                missed[cat].append(item["keyword"])

    total_kw = sum(len(v) for v in jd_keywords.values())
    matched_kw = sum(len(v) for v in matched.values())
    coverage = matched_kw / total_kw * 100 if total_kw > 0 else 0

    return {
        "coverage": round(coverage, 1),
        "matched": matched,
        "missed": missed,
        "total": total_kw,
        "matched_count": matched_kw,
    }


def format_report(keywords: dict, requirements: list, match_result: dict = None) -> str:
    """格式化输出分析报告"""
    lines = ["# JD 分析报告\n"]

    lines.append("## 关键词提取\n")
    for cat, items in keywords.items():
        lines.append(f"### {cat}")
        for item in items:
            lines.append(f"- **{item['keyword']}** (出现 {item['count']} 次)")
        lines.append("")

    if requirements:
        lines.append("## 能力要求提取\n")
        for i, req in enumerate(requirements, 1):
            lines.append(f"{i}. {req}")
        lines.append("")

    if match_result:
        lines.append("## 简历匹配度\n")
        lines.append(f"**总体覆盖率: {match_result['coverage']}%** ({match_result['matched_count']}/{match_result['total']})\n")

        if any(v for v in match_result["missed"].values()):
            lines.append("### 简历中缺失的关键词（建议补充）\n")
            for cat, missed in match_result["missed"].items():
                if missed:
                    lines.append(f"- **{cat}**: {', '.join(missed)}")
            lines.append("")

        if any(v for v in match_result["matched"].values()):
            lines.append("### 已覆盖的关键词\n")
            for cat, matched in match_result["matched"].items():
                if matched:
                    lines.append(f"- **{cat}**: {', '.join(matched)}")
            lines.append("")

    lines.append("## 简历优化建议\n")
    lines.append("基于 JD 分析，建议在简历中：\n")

    if match_result and any(v for v in match_result["missed"].values()):
        lines.append("1. **补充缺失关键词**：将上述缺失词自然融入项目经历描述中")
    lines.append("2. **对齐能力要求**：确保每条 JD 要求都能在简历中找到对应的项目经历支撑")
    lines.append("3. **使用 JD 原词**：在不失真的前提下，优先使用 JD 中出现的原始表述")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="JD 解析与关键词提取")
    parser.add_argument("--url", help="JD 页面 URL")
    parser.add_argument("--file", help="JD 本地文件路径")
    parser.add_argument("--resume", help="简历文件路径（用于匹配度分析）")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    args = parser.parse_args()

    if not args.url and not args.file:
        parser.print_help()
        sys.exit(1)

    if args.url:
        print(f"正在抓取: {args.url}")
        jd_text = fetch_url(args.url)
    else:
        jd_text = Path(args.file).read_text(encoding="utf-8")

    keywords = extract_keywords(jd_text)
    requirements = extract_requirements(jd_text)

    match_result = None
    if args.resume:
        resume_text = Path(args.resume).read_text(encoding="utf-8")
        match_result = match_resume(keywords, resume_text)

    if args.json:
        output = {
            "keywords": keywords,
            "requirements": requirements,
        }
        if match_result:
            output["match"] = match_result
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(format_report(keywords, requirements, match_result))


if __name__ == "__main__":
    main()
