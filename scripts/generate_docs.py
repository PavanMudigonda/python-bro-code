import os
import re
import glob

GITHUB_REPO = "PavanMudigonda/python-bro-code"
GITHUB_BRANCH = "main"

# Pattern to match old badge lines (Colab/Kaggle image-links at the top of READMEs)
OLD_BADGE_RE = re.compile(
    r'^\s*\[!\[.*?\]\(https?://(?:colab\.research\.google\.com|kaggle\.com|img\.shields\.io).*?\)\]\(.*?\)\s*'
    r'(?:\[!\[.*?\]\(https?://(?:colab\.research\.google\.com|kaggle\.com|img\.shields\.io).*?\)\]\(.*?\)\s*)*$',
    re.MULTILINE,
)

def strip_old_badges(content):
    """Remove pre-existing Colab/Kaggle badge lines from README content."""
    return OLD_BADGE_RE.sub('', content).lstrip('\n')

def fix_markdown_links(content):
    # This regex catches:
    # 1. `../1-print/`
    # 2. `../1-print/README.md`
    # 3. `./1-print`
    # 4. `1-print/`
    # Replaces with: `1-print.md`
    # It ensures that cross-chapter links work properly in generated docs!
    # Wait, the regex `\]\((?:\.\/|\.\.\/)?(\d+-[^/\)]+)(?:\/README\.md|\/|\.md)?\)`
    # is safer.
    content = re.sub(r'\]\((?:\.\/|\.\.\/)?(\d+-[a-zA-Z0-9-]+)(?:\/README\.md|\/|\.md)?\)', r'](\1.md)', content)
    return content

def generate_notebook_badges(folder):
    """Generate Colab and Kaggle badges for any .ipynb files in the folder."""
    notebooks = sorted(glob.glob(os.path.join(folder, "*.ipynb")))
    if not notebooks:
        return ""

    badges_lines = ["\n## 🚀 Open Notebook\n"]
    for nb_path in notebooks:
        nb_name = os.path.basename(nb_path)
        colab_url = (
            f"https://colab.research.google.com/github/{GITHUB_REPO}"
            f"/blob/{GITHUB_BRANCH}/{folder}/{nb_name}"
        )
        kaggle_url = (
            f"https://kaggle.com/kernels/welcome?src="
            f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{folder}/{nb_name}"
        )
        badges_lines.append(
            f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url}) "
            f"[![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)]({kaggle_url})"
        )
    badges_lines.append("")
    return "\n".join(badges_lines)

def main():
    base_dir = "."
    docs_dir = "docs"
    
    # Ensure docs directory exists
    os.makedirs(docs_dir, exist_ok=True)
    
    # 1. Update the Main Index
    root_readme = os.path.join(base_dir, "README.md")
    if os.path.exists(root_readme):
        with open(root_readme, 'r', encoding='utf-8') as f:
            root_content = f.read()
        
        root_content = fix_markdown_links(root_content)
        
        with open(os.path.join(docs_dir, "index.md"), 'w', encoding='utf-8') as f:
            f.write(root_content)
            
    # 2. Parse Chapter Folders
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(f) and re.match(r'^\d+-', f)]
    folders.sort(key=lambda x: int(x.split('-')[0]))
    
    chapter_count = 0
    generated_chapters = []
    
    for folder in folders:
        readme_path = os.path.join(folder, "README.md")
        if os.path.exists(readme_path):
            chapter_name = ' '.join(word.capitalize() for word in folder.split('-')[1:])
            chapter_prefix = folder.split('-')[0]
            display_name = f"Chapter {chapter_prefix}: {chapter_name}"
            
            doc_filename = f"{folder}.md"
            doc_path = os.path.join(docs_dir, doc_filename)
            
            with open(readme_path, 'r', encoding='utf-8') as rf:
                content = rf.read()
            
            # Remove old/stale Colab/Kaggle badges from README
            content = strip_old_badges(content)
            
            # Apply link fixing
            content = fix_markdown_links(content)
            
            # Prepend a title if it's not present
            if not content.startswith('# '):
                content = f"# {display_name}\n\n{content}"

            # Inject Colab / Kaggle notebook badges after the first heading
            notebook_badges = generate_notebook_badges(folder)
            if notebook_badges:
                first_newline = content.find('\n')
                if first_newline != -1:
                    content = content[:first_newline] + "\n" + notebook_badges + content[first_newline:]
                else:
                    content += "\n" + notebook_badges
            
            with open(doc_path, 'w', encoding='utf-8') as wf:
                wf.write(content)
                
            generated_chapters.append(folder)
            chapter_count += 1

    # 3. Append MyST toctree to index.md for Sphinx navigation
    toctree_entries = "\n".join(generated_chapters)
    toctree_block = f"""

```{{toctree}}
:maxdepth: 1
:caption: Chapters
:hidden:

{toctree_entries}
```
"""
    index_path = os.path.join(docs_dir, "index.md")
    with open(index_path, 'a', encoding='utf-8') as f:
        f.write(toctree_block)

    print(f"Generated docs for Home + {chapter_count} chapters.")

if __name__ == '__main__':
    main()
