import os
import re

def fix_markdown_links(content):
    # This regex catches:
    # 1. `../1-print/`
    # 2. `../1-print/README.md`
    # 3. `./1-print`
    # 4. `1-print/`
    # Replaces with: `1-print.md`
    # It ensures that cross-chapter links work properly inside MkDocs!
    # Wait, the regex `\]\((?:\.\/|\.\.\/)?(\d+-[^/\)]+)(?:\/README\.md|\/|\.md)?\)`
    # is safer.
    content = re.sub(r'\]\((?:\.\/|\.\.\/)?(\d+-[a-zA-Z0-9-]+)(?:\/README\.md|\/|\.md)?\)', r'](\1.md)', content)
    return content

def main():
    base_dir = "."
    docs_dir = "docs"
    mkdocs_file = "mkdocs.yml"
    
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
    
    nav_entries = []
    
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
            
            # Apply link fixing
            content = fix_markdown_links(content)
            
            # Prepend a title if it's not present
            if not content.startswith('# '):
                content = f"# {display_name}\n\n{content}"
            
            with open(doc_path, 'w', encoding='utf-8') as wf:
                wf.write(content)
                
            nav_entries.append(f"  - '{display_name}': {doc_filename}")
            
    # 3. Update mkdocs.yml navigation
    if os.path.exists(mkdocs_file):
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            mkdocs_content = f.read()
            
        nav_index = mkdocs_content.find("nav:")
        if nav_index != -1:
            new_mkdocs = mkdocs_content[:nav_index] + "nav:\n  - Home: index.md\n" + "\n".join(nav_entries) + "\n"
        else:
            new_mkdocs = mkdocs_content + "\nnav:\n  - Home: index.md\n" + "\n".join(nav_entries) + "\n"
            
        with open(mkdocs_file, 'w', encoding='utf-8') as f:
            f.write(new_mkdocs)
            
        print(f"Generated docs for Home + {len(nav_entries)} chapters.")

if __name__ == '__main__':
    main()
