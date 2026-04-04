"""Add myst-nb YAML frontmatter to docs/*.md files that contain {code-cell} blocks."""
import glob

FRONTMATTER = """\
---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

"""

for md in sorted(glob.glob("docs/*.md")):
    with open(md) as f:
        content = f.read()

    if "{code-cell}" not in content:
        continue
    if content.startswith("---"):
        continue  # already has frontmatter

    with open(md, "w") as f:
        f.write(FRONTMATTER + content)

    print(f"  {md}: added frontmatter")
