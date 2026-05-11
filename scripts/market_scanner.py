"""
Market Scanner — 扫描 AI 产品经理市场趋势、热词与能力要求。

通过搜索主流招聘平台，聚合当前市场对 AI PM 的核心要求，
帮助简历用词与市场对齐。

用法:
    python market_scanner.py --role "AI产品经理"
    python market_scanner.py --role "大模型产品经理" --platform boss
    python market_scanner.py --role "AI产品经理" --output report.md
"""

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装依赖: pip install requests beautifulsoup4 lxml")
    sys.exit(1)


SEARCH_ENGINES = {
    "bing": "https://www.bing.com/search?q={query}",
    "sogou": "https://www.sogou.com/web?query={query}",
}

PLATFORM_QUERIES = {
    "boss": "site:zhipin.com {role} 岗位职责 任职要求",
    "lagou": "site:lagou.com {role} 岗位描述",
    "liepin": "site:liepin.com {role} 职位要求",
    "general": "{role} 岗位职责 任职要求 JD 2025",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# 能力维度关键词（用于从搜索结果中提取趋势）
CAPABILITY_DIMENSIONS = {
    "AI技术理解": [
        "大模型", "LLM", "RAG", "Agent", "Prompt Engineering",
        "NLP", "知识图谱", "向量数据库", "Fine-tuning", "RLHF",
        "多模态", "Embedding", "Function Calling", "MCP",
        "AI Agent", "Workflow", "Copilot", "AI应用",
    ],
    "产品核心能力": [
        "需求分析", "产品设计", "产品规划", "用户研究",
        "数据分析", "竞品分析", "商业化", "产品策略",
        "PRD", "原型设计", "用户体验", "增长策略",
    ],
    "B端/企业级": [
        "B端", "企业级", "SaaS", "PaaS", "中台",
        "平台化", "API", "SDK", "开放平台",
        "多租户", "权限管理", "配置化",
    ],
    "行业场景": [
        "金融", "保险", "医疗", "教育", "电商",
        "客服", "营销", "风控", "审核", "搜索",
        "内容生成", "智能问答", "对话系统",
    ],
    "协作与软实力": [
        "跨部门", "技术沟通", "项目管理", "推动落地",
        "从0到1", "全流程", "端到端", "方法论",
        "抗压", "自驱", "创新",
    ],
    "质量与工程": [
        "评测", "评估", "Bad Case", "质量体系",
        "可观测", "归因", "回归测试", "AB测试",
        "数据标注", "模型评估", "效果验证",
    ],
}


def search_web(query: str, engine: str = "bing", max_results: int = 10) -> list:
    """执行搜索并返回结果摘要"""
    url = SEARCH_ENGINES.get(engine, SEARCH_ENGINES["bing"]).format(query=query)

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, "lxml")

        results = []
        for item in soup.select(".b_algo, .vrso, .b_ans"):
            title = item.select_one("h2")
            snippet = item.select_one(".b_caption p, .b_paractl")
            if title:
                results.append({
                    "title": title.get_text(strip=True),
                    "snippet": snippet.get_text(strip=True) if snippet else "",
                })
            if len(results) >= max_results:
                break

        return results
    except Exception as e:
        print(f"搜索失败 ({engine}): {e}", file=sys.stderr)
        return []


def extract_trends(search_results: list) -> dict:
    """从搜索结果中提取能力趋势"""
    all_text = " ".join(
        f"{r['title']} {r['snippet']}" for r in search_results
    ).lower()

    trends = {}
    for dimension, keywords in CAPABILITY_DIMENSIONS.items():
        found = []
        for kw in keywords:
            count = all_text.count(kw.lower())
            if count > 0:
                found.append({"keyword": kw, "frequency": count})
        if found:
            found.sort(key=lambda x: x["frequency"], reverse=True)
            trends[dimension] = found

    return trends


def extract_salary_signals(search_results: list) -> list:
    """从搜索结果中提取薪资信号"""
    salary_patterns = [
        r"(\d+)[kK]-(\d+)[kK]",
        r"(\d+)-(\d+)[万]",
        r"月薪\s*(\d+)-(\d+)",
        r"年薪\s*(\d+)-(\d+)",
    ]

    signals = []
    for r in search_results:
        text = f"{r['title']} {r['snippet']}"
        for pattern in salary_patterns:
            matches = re.findall(pattern, text)
            for m in matches:
                signals.append(f"{m[0]}-{m[1]}")

    return list(set(signals))[:5]


def format_report(role: str, trends: dict, salary_signals: list, search_results: list) -> str:
    """格式化输出市场扫描报告"""
    lines = [
        f"# {role} 市场趋势扫描报告",
        f"\n> 扫描时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    lines.append("## 能力维度热度\n")
    for dimension, keywords in trends.items():
        total_freq = sum(k["frequency"] for k in keywords)
        top_3 = ", ".join(k["keyword"] for k in keywords[:3])
        lines.append(f"### {dimension} (热度: {total_freq})")
        lines.append(f"Top 关键词: **{top_3}**\n")
        for kw in keywords[:5]:
            bar = "█" * min(kw["frequency"], 20)
            lines.append(f"- {kw['keyword']}: {bar} ({kw['frequency']})")
        lines.append("")

    if salary_signals:
        lines.append("## 薪资信号\n")
        for s in salary_signals:
            lines.append(f"- {s}")
        lines.append("")

    lines.append("## 简历优化建议\n")
    lines.append("基于市场扫描结果，建议简历重点突出：\n")

    all_hot = []
    for keywords in trends.values():
        all_hot.extend(keywords[:2])
    all_hot.sort(key=lambda x: x["frequency"], reverse=True)

    for i, kw in enumerate(all_hot[:8], 1):
        lines.append(f"{i}. **{kw['keyword']}** — 当前市场高频要求，确保简历中有对应项目经历支撑")

    lines.append("\n## 原始搜索结果摘要\n")
    for i, r in enumerate(search_results[:8], 1):
        lines.append(f"{i}. **{r['title']}**")
        if r["snippet"]:
            lines.append(f"   {r['snippet'][:100]}...")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="AI PM 市场趋势扫描")
    parser.add_argument("--role", default="AI产品经理", help="目标岗位名称")
    parser.add_argument("--platform", default="general",
                        choices=list(PLATFORM_QUERIES.keys()),
                        help="搜索平台 (boss/lagou/liepin/general)")
    parser.add_argument("--output", help="输出文件路径 (.md)")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    args = parser.parse_args()

    query_template = PLATFORM_QUERIES[args.platform]
    query = query_template.format(role=args.role)

    print(f"正在扫描: {args.role} ({args.platform})...")
    results = search_web(query)

    if not results:
        print("未获取到搜索结果，请检查网络或尝试其他搜索引擎。")
        sys.exit(1)

    trends = extract_trends(results)
    salary_signals = extract_salary_signals(results)

    if args.json:
        output = {
            "role": args.role,
            "platform": args.platform,
            "scan_time": datetime.now().isoformat(),
            "trends": trends,
            "salary_signals": salary_signals,
        }
        content = json.dumps(output, ensure_ascii=False, indent=2)
    else:
        content = format_report(args.role, trends, salary_signals, results)

    if args.output:
        Path(args.output).write_text(content, encoding="utf-8")
        print(f"报告已保存至: {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()
