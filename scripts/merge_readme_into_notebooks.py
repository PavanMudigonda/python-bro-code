#!/usr/bin/env python3
"""Merge README.md content into chapter Jupyter notebooks, then delete the README.

For each chapter folder that has both a README.md and a .ipynb:
  1. Replace the first markdown cell(s) with the full README content
     (split into badge cell + content cell).
  2. Preserve all existing code cells.
  3. Delete the README.md.
"""

import json
import glob
import os
import re
import sys

GITHUB_REPO = "PavanMudigonda/python-bro-code"
GITHUB_BRANCH = "main"

# Matches old Colab/Kaggle badge lines at the top of READMEs
OLD_BADGE_RE = re.compile(
    r'^\s*\[!\[.*?\]\(https?://(?:colab\.research\.google\.com|kaggle\.com|img\.shields\.io).*?\)\]\(.*?\)\s*'
    r'(?:\[!\[.*?\]\(https?://(?:colab\.research\.google\.com|kaggle\.com|img\.shields\.io).*?\)\]\(.*?\)\s*)*$',
    re.MULTILINE,
)


def make_badge_cell(folder, nb_name):
    """Create a markdown cell with Colab + Kaggle badges for the correct repo."""
    colab_url = (
        f"https://colab.research.google.com/github/{GITHUB_REPO}"
        f"/blob/{GITHUB_BRANCH}/{folder}/{nb_name}"
    )
    kaggle_url = (
        f"https://kaggle.com/kernels/welcome?src="
        f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{folder}/{nb_name}"
    )
    badge_md = (
        f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url}) "
        f"[![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)]({kaggle_url})"
    )
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [badge_md],
    }


def make_markdown_cell(text):
    """Create a markdown cell from a string."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.splitlines(True),  # preserve line endings
    }


def strip_old_badges(content):
    """Remove pre-existing Colab/Kaggle badge lines."""
    return OLD_BADGE_RE.sub('', content).lstrip('\n')


def merge_readme_into_notebook(folder, nb_path, readme_path):
    """Merge README into notebook, replacing old markdown cells."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme = f.read()

    # Strip old badges from README
    readme = strip_old_badges(readme)

    nb_name = os.path.basename(nb_path)

    # Separate code cells (preserve) from old markdown cells (replace)
    code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']

    # Build new cell list: badge + full README + all code cells
    new_cells = [
        make_badge_cell(folder, nb_name),
        make_markdown_cell(readme),
    ] + code_cells

    nb['cells'] = new_cells

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write('\n')

    return True


def main():
    base_dir = "."
    merged = 0
    skipped = 0

    folders = sorted(
        [f for f in os.listdir(base_dir) if os.path.isdir(f) and re.match(r'^\d+-', f)],
        key=lambda x: int(x.split('-')[0]),
    )

    for folder in folders:
        readme_path = os.path.join(folder, "README.md")
        notebooks = sorted(glob.glob(os.path.join(folder, "*.ipynb")))

        if not os.path.exists(readme_path) or not notebooks:
            continue

        nb_path = notebooks[0]  # use the first notebook
        print(f"Merging: {readme_path} -> {nb_path}")
        merge_readme_into_notebook(folder, nb_path, readme_path)

        # Delete the README
        os.remove(readme_path)
        print(f"  Deleted: {readme_path}")
        merged += 1

    print(f"\nDone. Merged {merged} READMEs into notebooks.")


if __name__ == '__main__':
    main()
