#!/usr/bin/env python3
"""
Enhanced README updater with better content extraction from transcripts.
Uses a more intelligent approach to extract meaningful insights.
"""

import os
import re
from pathlib import Path


def clean_transcript(text):
    """Clean transcript by normalizing spaces and removing metadata."""
    # Skip header lines
    lines = text.split('\n')
    if len(lines) > 4:
        text = '\n'.join(lines[4:])
    
    # Normalize excessive spaces (transcript has double spaces between words)
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def extract_meaningful_insights(transcript_text, chapter_name):
    """Extract meaningful insights based on chapter context."""
    text = clean_transcript(transcript_text)
    
    insights = []
    
    # Pattern 1: Installation/Setup instructions (for early chapters)
    if any(word in chapter_name.lower() for word in ['print', 'variable', 'setup', 'start']):
        # Look for installation steps
        setup_patterns = [
            (r'download.*?python.*?interpreter', 'Download Python interpreter from python.org'),
            (r'install.*?(?:pycharm|vs code|ide)', f'Install an IDE (PyCharm or VS Code) for writing Python code'),
            (r'add python.*?to path', 'Add Python to PATH during installation (Windows)'),
            (r'create.*?new.*?(?:project|file)', 'Create a new Python project and file'),
            (r'print\(["\'].*?["\']\)', 'Use print() function to display output'),
        ]
        
        for pattern, insight in setup_patterns:
            if re.search(pattern, text, re.IGNORECASE) and insight not in insights:
                insights.append(insight)
    
    # Pattern 2: Core concept explanations
    concept_keywords = {
        'variable': 'Variables store data values that can be reused',
        'string': 'Strings are text data enclosed in quotes',
        'integer': 'Integers are whole numbers without decimals',
        'float': 'Floats are numbers with decimal points',
        'boolean': 'Booleans are True/False values',
        'list': 'Lists store multiple items in a single variable',
        'dictionary': 'Dictionaries store data in key-value pairs',
        'function': 'Functions are reusable blocks of code',
        'loop': 'Loops repeat code multiple times',
        'conditional': 'Conditionals execute code based on conditions',
        'class': 'Classes are blueprints for creating objects',
    }
    
    for keyword, concept in concept_keywords.items():
        if keyword in chapter_name.lower() or keyword in text.lower()[:500]:
            if concept not in insights:
                insights.append(concept)
                break  # Only add one concept
    
    # Pattern 3: Key syntax/usage from transcript
    syntax_patterns = [
        (r'syntax.*?(?:is|would be|looks like)', 'Understanding the proper syntax is important'),
        (r'(?:type|write).*?print\(', 'Use print() to output text to the console'),
        (r'(?:def|define).*?function', 'Define functions using the def keyword'),
        (r'(?:import|from).*?(?:module|package)', 'Import modules to use external code'),
        (r'(?:for|while).*?loop', 'Use loops to repeat actions'),
        (r'if.*?(?:elif|else)', 'Use if-elif-else for conditional logic'),
    ]
    
    for pattern, insight in syntax_patterns:
        if re.search(pattern, text, re.IGNORECASE) and insight not in insights and len(insights) < 5:
            insights.append(insight)
    
    # Pattern 4: Best practices mentioned
    practice_patterns = [
        (r'(?:important|remember|note).*?(?:comment|documentation)', 'Use comments to document your code'),
        (r'(?:always|make sure|don\'t forget).*?(?:save|backup)', 'Save your work regularly'),
        (r'test.*?code', 'Test your code to ensure it works correctly'),
        (r'(?:error|exception).*?handling', 'Handle errors gracefully in your code'),
    ]
    
    for pattern, insight in practice_patterns:
        if re.search(pattern, text, re.IGNORECASE) and insight not in insights and len(insights) < 5:
            insights.append(insight)
    
    # If still no insights, extract first meaningful teaching sentence
    if not insights:
        # Look for sentences about "what" something is
        what_patterns = [
            r'(?:what is|what are)\s+[a-z]+\s+(?:is|are)\s+([^.!?]{20,100})[.!?]',
            r'([A-Z][^.!?]*?(?:is|are)\s+(?:used|needed|required|important)[^.!?]{10,80})[.!?]',
        ]
        
        for pattern in what_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches[:2]:
                cleaned = match.strip()
                if len(cleaned) > 20 and cleaned not in insights:
                    insights.append(cleaned)
    
    # Ensure we have at least 3 insights
    default_insights = [
        f'Follow along with the video for hands-on practice',
        f'Experiment with the code examples to deepen understanding',
        f'Take notes on key concepts as you learn',
    ]
    
    while len(insights) < 3:
        for default in default_insights:
            if default not in insights:
                insights.append(default)
                break
    
    return insights[:5]


def re_enhance_readme(readme_path, transcript_path):
    """Re-enhance README with better extracted insights."""
    if not transcript_path.exists():
        return False, "no_transcript"
    
    # Read README
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except Exception as e:
        return False, f"read_error: {e}"
    
    # Read transcript
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
    except Exception as e:
        return False, f"transcript_error: {e}"
    
    # Extract insights
    chapter_name = readme_path.parent.name
    insights = extract_meaningful_insights(transcript_text, chapter_name)
    
    if not insights:
        return False, "no_insights"
    
    # Create new section
    enhancement = "## 🎓 Key Takeaways from Video\n\n"
    for i, insight in enumerate(insights, 1):
        enhancement += f"{i}. {insight}\n"
    enhancement += "\n> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*\n"
    
    # Remove existing section if present
    if '## 🎓 Key Takeaways' in readme_content:
        pattern = r'## 🎓 Key Takeaways from Video.*?(?=\n## |\Z)'
        readme_content = re.sub(pattern, '', readme_content, flags=re.DOTALL)
    
    # Insert before "Coming Soon" or at end
    if '## 📖 Coming Soon' in readme_content:
        readme_content = readme_content.replace(
            '## 📖 Coming Soon',
            enhancement + '\n## 📖 Coming Soon'
        )
    elif '## 🔗 Next Chapter' in readme_content:
        readme_content = readme_content.replace(
            '## 🔗 Next Chapter',
            '\n' + enhancement + '\n## 🔗 Next Chapter'
        )
    else:
        readme_content += '\n' + enhancement
    
    # Clean up extra newlines
    readme_content = re.sub(r'\n{3,}', '\n\n', readme_content)
    
    # Write back
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        return True, "enhanced"
    except Exception as e:
        return False, f"write_error: {e}"


def main():
    base_path = Path('/Users/nagapavankumar.mudigonda/code/python-bro-code')
    transcripts_path = base_path / 'transcripts'
    
    enhanced_count = 0
    skipped_count = 0
    failed_count = 0
    
    print("Re-enhancing README files with improved insights extraction...\n")
    
    for i in range(1, 50):
        # Find chapter folder
        folders = list(base_path.glob(f'{i}-*'))
        if not folders:
            folders = list(base_path.glob(f'{i:02d}-*'))
        
        if not folders:
            print(f"⚠️  Chapter {i} folder not found")
            failed_count += 1
            continue
        
        chapter_folder = folders[0]
        chapter_name = chapter_folder.name
        
        readme_path = chapter_folder / 'README.md'
        if not readme_path.exists():
            print(f"⚠️  README not found in {chapter_name}")
            failed_count += 1
            continue
        
        # Find transcript
        transcript_files = list(transcripts_path.glob(f'{i:02d}-transcript.txt'))
        if not transcript_files:
            transcript_files = list(transcripts_path.glob(f'{i}-transcript.txt'))
        
        if not transcript_files:
            print(f"{chapter_name:40} ⏭️  No transcript")
            skipped_count += 1
            continue
        
        # Enhance
        print(f"{chapter_name:40} ", end='')
        success, status = re_enhance_readme(readme_path, transcript_files[0])
        
        if success:
            print("✅")
            enhanced_count += 1
        else:
            print(f"❌ ({status})")
            failed_count += 1
    
    print("\n" + "="*80)
    print(f"Summary: {enhanced_count} enhanced, {skipped_count} skipped, {failed_count} failed")
    print(f"Total: {enhanced_count}/{49} README files successfully enhanced")


if __name__ == '__main__':
    main()
