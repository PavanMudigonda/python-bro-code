"""Remove duplicate Video Tutorial sections from docs/*.md files."""
import re

files = [
    "docs/6-if-statements.md",
    "docs/7-calculator.md",
    "docs/8-weight-conversion.md",
    "docs/10-logical-operators.md",
    "docs/11-conditional-expressions.md",
    "docs/12-string-methods.md",
    "docs/13-string-indexing.md",
    "docs/19-nested-loops.md",
    "docs/20-timer.md",
]

for f in files:
    with open(f) as fh:
        lines = fh.readlines()

    # Find all line indices with the Video Tutorial heading
    vt_indices = [i for i, line in enumerate(lines) if line.strip() == "## 📺 Video Tutorial"]

    if len(vt_indices) < 2:
        print(f"  {f}: only {len(vt_indices)} heading(s), skipping")
        continue

    # Remove the second occurrence: heading + blank + badge line + trailing blank
    idx = vt_indices[1]
    to_remove = []

    # blank line before heading (if present)
    if idx > 0 and lines[idx - 1].strip() == "":
        to_remove.append(idx - 1)

    to_remove.append(idx)  # heading line

    # blank line after heading
    if idx + 1 < len(lines) and lines[idx + 1].strip() == "":
        to_remove.append(idx + 1)

    # badge line
    if idx + 2 < len(lines) and "Watch on YouTube" in lines[idx + 2]:
        to_remove.append(idx + 2)

    for li in sorted(to_remove, reverse=True):
        lines.pop(li)

    with open(f, "w") as fh:
        fh.writelines(lines)

    print(f"  {f}: removed {len(to_remove)} duplicate lines")
