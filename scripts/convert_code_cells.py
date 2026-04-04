"""Convert ```python blocks in docs/*.md to ```{code-cell} python blocks.

Rules:
- Only converts fenced code blocks that start with ```python
- Blocks containing input() get :tags: [skip-execution]
- Blocks that look like pseudocode (contain '# ...' or '...' on its own line,
  or are inside a non-runnable context) are left as plain ```python
"""
import glob
import re

SKIP_MARKERS = [
    "# ...",
    "# calculator code here",
    "# Create calculator",
    "# Parse and calculate",
    "# Allow user",
    "# your code here",
    "# TODO",
    "pass  #",
]

def should_convert(code_lines):
    """Return True if the block looks like runnable Python code."""
    code = "\n".join(code_lines)
    # Skip very short blocks (1 line) that are just illustrations
    stripped = [l for l in code_lines if l.strip()]
    if not stripped:
        return False
    # Skip blocks with obvious pseudocode markers
    for marker in SKIP_MARKERS:
        if marker in code:
            return False
    # Skip blocks that are just comments
    if all(l.strip().startswith("#") or not l.strip() for l in code_lines):
        return False
    return True

def uses_input(code_lines):
    """Return True if the block calls input()."""
    return any("input(" in line for line in code_lines)

def convert_file(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    i = 0
    converted = 0

    while i < len(lines):
        line = lines[i]

        # Match opening of a python code fence
        if re.match(r"^```python\s*$", line):
            # Collect the code block
            code_lines = []
            i += 1
            while i < len(lines) and not re.match(r"^```\s*$", lines[i]):
                code_lines.append(lines[i])
                i += 1
            closing = lines[i] if i < len(lines) else "```"

            if should_convert(code_lines):
                if uses_input(code_lines):
                    new_lines.append("```{code-cell} python")
                    new_lines.append(":tags: [skip-execution]")
                    new_lines.append("")
                else:
                    new_lines.append("```{code-cell} python")
                new_lines.extend(code_lines)
                new_lines.append(closing)
                converted += 1
            else:
                # Keep as-is
                new_lines.append("```python")
                new_lines.extend(code_lines)
                new_lines.append(closing)
            i += 1
        else:
            new_lines.append(line)
            i += 1

    if converted > 0:
        with open(filepath, "w") as f:
            f.write("\n".join(new_lines))

    return converted

total = 0
for md in sorted(glob.glob("docs/*.md")):
    if md == "docs/index.md":
        continue
    count = convert_file(md)
    if count > 0:
        print(f"  {md}: converted {count} block(s)")
        total += count

print(f"\nTotal: {total} code blocks converted across all docs")
