#!/usr/bin/env python3
"""expert-wiki 知识库体检与统计工具。

用法:
  python3 wiki_tool.py doctor <wiki根目录>   # 检查断链、孤儿条目、缺失元数据
  python3 wiki_tool.py stats  <wiki根目录>   # 输出领域/条目/案例统计
"""
import re
import sys
from pathlib import Path

FRONT = re.compile(r"^---\n(.*?)\n---", re.S)
LINK = re.compile(r"\[\[([^\]|#]+?)\]\]")


def collect(root: Path):
    docs = {}  # title -> path
    raw = []   # (path, text)
    for sub in ("entries", "cases", "methods", "moc"):
        for p in (root / sub).rglob("*.md"):
            t = p.read_text(encoding="utf-8")
            raw.append((p, t))
            m = FRONT.search(t)
            title = None
            if m and re.search(r"^title:\s*(.+)$", m.group(1), re.M):
                title = re.search(r"^title:\s*(.+)$", m.group(1), re.M).group(1).strip()
            docs[norm(title or p.stem)] = p
    if (root / "HOME.md").exists():
        docs["HOME"] = root / "HOME.md"
    return docs, raw


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


def doctor(root: Path):
    docs, raw = collect(root)
    issues = 0
    for p, text in raw:
        for m in LINK.finditer(text):
            target = norm(m.group(1))
            if target not in docs:
                print(f"✗ 断链: {p.relative_to(root)} -> [[{m.group(1)}]]")
                issues += 1
        fm = FRONT.search(text)
        if not fm and "moc" not in p.parts and p.name != "HOME.md":
            print(f"✗ 缺少 frontmatter: {p.relative_to(root)}")
            issues += 1
    # 孤儿条目：没有出链也没有入链
    inbound = {norm(m.group(1)) for _, text in raw for m in LINK.finditer(text)}
    for title, p in docs.items():
        if not p:
            continue
        if p.name == "HOME.md":
            continue  # HOME 是入口，允许无链接
        text = p.read_text(encoding="utf-8")
        if norm(title) not in inbound and not LINK.search(text):
            print(f"⚠ 孤儿条目(无链接关系): {p.relative_to(root)}")
            issues += 1
    print(f"\n体检完成，发现问题 {issues} 处。")
    return issues


def stats(root: Path):
    total = 0
    for sub in ("entries", "cases", "methods", "moc"):
        files = list((root / sub).rglob("*.md"))
        print(f"{sub:8s}: {len(files)} 个文件")
        total += len(files)
    print(f"合计 {total} 个文档")


if __name__ == "__main__":
    cmd, root = sys.argv[1], Path(sys.argv[2])
    doctor(root) if cmd == "doctor" else stats(root)
