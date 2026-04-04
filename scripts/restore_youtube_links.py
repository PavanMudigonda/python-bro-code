#!/usr/bin/env python3
"""Restore YouTube video badge links in notebook markdown cells.

The YouTube badges were accidentally stripped by the old badge regex.
This script inserts them back into the '📺 Video Tutorial' section
of each chapter's notebook.
"""

import json
import os
import re

# Mapping of chapter folder -> YouTube video URL (extracted from git history)
YOUTUBE_LINKS = {
    "1-print": "https://youtu.be/Sg4GMVMdOPo",
    "2-variables": "https://youtu.be/7IoQ5BGkTJo",
    "3-type-casting": "https://youtu.be/Qtq83lAoogM",
    "4-user-input": "https://youtu.be/nMCOB8KElwo",
    "5-madlibs-game": "https://youtu.be/jc7TBgMS_kw",
    "6-if-statements": "https://youtu.be/FvMPfrgGeKs",
    "7-calculator": "https://youtu.be/yUrYouDQZL8",
    "8-weight-conversion": "https://youtu.be/80kjCBRjkmU",
    "9-temp-conversion": "https://youtu.be/fy5QsDJmctQ",
    "10-logical-operators": "https://youtu.be/W7luvtXeQTA",
    "11-conditional-expressions": "https://youtu.be/TYyKQBC4bwE",
    "12-string-methods": "https://youtu.be/tb6EYiHtcXU",
    "13-string-indexing": "https://youtu.be/7pXf1DUuaIo",
    "14-email-slicer": "https://youtu.be/6MAufQ6vGtI",
    "15-format": "https://youtu.be/FrvBwdAU2dQ",
    "16-while": "https://youtu.be/rRTjPnVooxE",
    "17-interest-calculator": "https://youtu.be/aM5dttidg4Q",
    "18-for": "https://youtu.be/KWgYha0clzw",
    "19-nested-loops": "https://youtu.be/APWy6Pc83gE",
    "20-timer": "https://youtu.be/KseiSR0MCTI",
    "21-lists-sets-tuples": "https://youtu.be/gOMW_n2-2Mw",
    "22-shopping-cart": "https://youtu.be/kbyHLU9JqjE",
    "23-2d-collections": "https://youtu.be/Xy6qeQWQwwFw",
    "24-quiz-game": "https://youtu.be/zehwgTB0vV8",
    "25-dictionaries": "https://youtu.be/MZZSMaEAC2g",
    "26-concession-stand-program": "https://youtu.be/PbkIzW_70EI",
    "27-random-numbers": "https://youtu.be/piJc18hcH0Y",
    "28-number-guessing-game": "https://youtu.be/jcKe13D6bao",
    "29-rock-paper-scissors-game": "https://youtu.be/fn68QNcatfo",
    "30-dice-roller-program": "https://youtu.be/x-Ag2_bJ40Y",
    "31-encryption-program": "https://youtu.be/vsLBErLWBhA",
    "32-functions": "https://youtu.be/89cGQjB5R4M",
    "33-default-arguments": "https://youtu.be/m2uURZxex3c",
    "34-keyword-arguments": "https://youtu.be/7QCHpAtlSMo",
    "35-args-kwargs": "https://youtu.be/Vh__2V2tXUM",
    "36-iterables": "https://youtu.be/VL_g3LjsFqs",
    "37-membership-operators": "https://youtu.be/OJ5E7VLsZQM",
    "38-list-comprehensions": "https://youtu.be/YlY2g2xrl6Q",
    "39-match-case-statements": "https://youtu.be/L7tT0NZF-Ag",
    "40-modules": "https://youtu.be/XcfxkHrHTVE",
    "41-scope-resolution": "https://youtu.be/XN83IECAscM",
    "42-if-name-main": "https://youtu.be/8A0E1dSyjFM",
    "43-credit-card-validator": "https://youtu.be/LqXIJjcRmGI",
    "44-banking-program": "https://youtu.be/8aW3tkIul-8",
    "45-slot-machine": "https://youtu.be/f5J3YiZ3XX8",
    "46-hangman-game": "https://youtu.be/ag8NtD1e0Kc",
    "47-python-oop": "https://youtu.be/1XE-_s4ZBT8",
    "48-class-variables": "https://youtu.be/bytvWg4fPB0",
    "49-inheritance": "https://youtu.be/u1be7Vele5o",
    "50-multiple-inheritance": "https://youtu.be/Q8YlYHjksLo",
    "51-abstract-classes": "https://youtu.be/97V7ICVeTJc",
    "55-aggregation": "https://youtu.be/caXOUnQkD1o",
    "56-composition": "https://youtu.be/TPUdUkFHD5I",
    "57-nested-classes": "https://youtu.be/zxPODCF4KEw",
    "63-lambda": "https://youtu.be/IljPHDyBRog",
    "64-sorting": "https://youtu.be/cd-vtiO5chk",
    "65-zip": "https://youtu.be/5WK3j2erJW4",
    "66-recursion": "https://youtu.be/ivl5-snqul8",
    "71-execution-time": "https://youtu.be/FblABqaKz_U",
    "74-iterators": "https://youtu.be/k0D3MQwLn7A",
    "75-generators": "https://youtu.be/Gsfsq2epdr8",
    "76-generator-expressions": "https://youtu.be/ZBlxaXMN_hU",
    "77-data-classes": "https://youtu.be/G1lJeEIl05o",
    "92-qr-codes": "https://youtu.be/pJdTyvufOdg",
    "93-music-player": "https://youtu.be/xf71dRBRP6o",
}

YOUTUBE_BADGE = (
    '[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red'
    '?style=for-the-badge&logo=youtube)]({url})'
)

VIDEO_HEADING_RE = re.compile(r'^## 📺 Video Tutorial', re.MULTILINE)


def restore_in_notebook(nb_path, folder):
    url = YOUTUBE_LINKS.get(folder)
    if not url:
        return False

    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    badge_line = YOUTUBE_BADGE.format(url=url)
    modified = False

    for cell in nb['cells']:
        if cell['cell_type'] != 'markdown':
            continue
        source = ''.join(cell['source'])
        if '📺 Video Tutorial' not in source:
            continue
        # Already has YouTube link?
        if 'youtu' in source:
            break

        # Insert the badge right after the heading line
        lines = source.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if VIDEO_HEADING_RE.match(line):
                new_lines.append('')
                new_lines.append(badge_line)
        cell['source'] = [l + '\n' for l in new_lines[:-1]] + [new_lines[-1]]
        modified = True
        break

    if modified:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write('\n')
        return True
    return False


def restore_in_readme(readme_path, folder):
    """Restore YouTube badge in README.md for chapters that still have READMEs."""
    url = YOUTUBE_LINKS.get(folder)
    if not url:
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '📺 Video Tutorial' not in content:
        return False
    if 'youtu' in content:
        return False  # already has it

    badge_line = YOUTUBE_BADGE.format(url=url)
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if VIDEO_HEADING_RE.match(line):
            new_lines.append('')
            new_lines.append(badge_line)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    return True


def main():
    base_dir = '.'
    restored = 0

    for folder in sorted(os.listdir(base_dir)):
        if not os.path.isdir(folder) or not re.match(r'^\d+-', folder):
            continue

        # Try notebook first
        import glob
        notebooks = sorted(glob.glob(os.path.join(folder, '*.ipynb')))
        if notebooks:
            if restore_in_notebook(notebooks[0], folder):
                print(f"  Restored YouTube link in {notebooks[0]}")
                restored += 1
                continue

        # Fall back to README
        readme_path = os.path.join(folder, 'README.md')
        if os.path.exists(readme_path):
            if restore_in_readme(readme_path, folder):
                print(f"  Restored YouTube link in {readme_path}")
                restored += 1

    print(f"\nDone. Restored YouTube links in {restored} chapters.")


if __name__ == '__main__':
    main()
