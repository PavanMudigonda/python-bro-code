#!/usr/bin/env python3
"""
Enhance README files with content extracted from video transcripts.
"""

import re
from pathlib import Path


def clean_transcript_text(text):
    """Clean transcript text by removing extra spaces."""
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_key_points(transcript_text):
    """Extract key teaching points from the transcript."""
    # Clean the text first
    text = clean_transcript_text(transcript_text)
    
    # Split into sentences (roughly)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    key_points = []
    
    # Keywords that indicate important teaching moments
    teaching_keywords = [
        'print', 'function', 'variable', 'type', 'syntax', 'create', 'define',
        'important', 'remember', 'note', 'use', 'understand', 'learn',
        'method', 'example', 'basic', 'simple', 'first', 'write', 'code'
    ]
    
    code_indicators = ['print(', 'def ', 'class ', 'import ', '=', '()', 'return']
    
    for sentence in sentences:
        # Skip very short or very long sentences
        if len(sentence) < 30 or len(sentence) > 200:
            continue
        
        sentence_lower = sentence.lower()
        
        # Check if sentence contains teaching keywords
        has_teaching_keyword = any(keyword in sentence_lower for keyword in teaching_keywords)
        
        # Check if it mentions code concepts
        mentions_code = any(indicator in sentence for indicator in code_indicators)
        
        # Prioritize sentences about code or teaching
        if (has_teaching_keyword or mentions_code) and len(key_points) < 5:
            # Clean up the sentence
            cleaned = sentence.strip()
            
            # Remove filler words from start
            cleaned = re.sub(r'^(?:so|now|then|okay|alright|well|um|uh)\s+', '', cleaned, flags=re.IGNORECASE)
            
            # Ensure it starts with capital letter
            if cleaned:
                cleaned = cleaned[0].upper() + cleaned[1:]
                
                # Add if not duplicate and meaningful
                if cleaned not in key_points and not cleaned.startswith('I '):
                    key_points.append(cleaned)
    
    return key_points


def extract_code_explanations(transcript_text):
    """Extract code-related explanations from transcript."""
    text = clean_transcript_text(transcript_text)
    
    code_patterns = [
        r"(?:type|write|add|create)\s+([a-zA-Z_][a-zA-Z0-9_().,\s]{10,80})(?:and|then|now|this|to)",
        r"(?:syntax|format|structure)\s+(?:is|would be)\s+(.{15,100})(?:\.|,|and)",
    ]
    
    explanations = []
    for pattern in code_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            exp = match.group(1).strip()
            if len(explanations) < 3:
                explanations.append(exp)
    
    return explanations


def read_transcript(transcript_path):
    """Read and return transcript content."""
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Skip the header (first 4 lines)
            lines = content.split('\n')
            if len(lines) > 4:
                return '\n'.join(lines[4:])
            return content
    except Exception as e:
        print(f"Error reading {transcript_path}: {e}")
        return ""


def enhance_readme(readme_path, transcript_path):
    """Enhance README with insights from transcript."""
    if not transcript_path.exists():
        print(f"⏭️  No transcript for {readme_path.parent.name}")
        return False
    
    # Read current README
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except Exception as e:
        print(f"Error reading README {readme_path}: {e}")
        return False
    
    # Check if already enhanced
    if '## 🎓 Key Takeaways' in readme_content:
        print(f"⏭️  {readme_path.parent.name} already enhanced")
        return False
    
    # Read transcript
    transcript_text = read_transcript(transcript_path)
    if not transcript_text:
        return False
    
    # Extract key points
    key_points = extract_key_points(transcript_text)
    
    if not key_points:
        print(f"⚠️  No key points extracted for {readme_path.parent.name}")
        return False
    
    # Create enhancement section
    enhancement = "\n\n## 🎓 Key Takeaways from Video\n\n"
    for i, point in enumerate(key_points, 1):
        enhancement += f"{i}. {point}\n"
    
    # Add note about transcript
    enhancement += "\n> 💡 *These points are extracted from the video transcript to enhance your learning experience.*\n"
    
    # Find where to insert (before "Coming Soon" section or at the end)
    if '## 📖 Coming Soon' in readme_content:
        readme_content = readme_content.replace(
            '## 📖 Coming Soon',
            enhancement + '\n## 📖 Coming Soon'
        )
    else:
        readme_content += enhancement
    
    # Write enhanced README
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        return True
    except Exception as e:
        print(f"Error writing README {readme_path}: {e}")
        return False


def main():
    """Main function to enhance all READMEs."""
    repo_root = Path(__file__).parent.parent
    transcripts_dir = repo_root / "transcripts"
    
    if not transcripts_dir.exists():
        print(f"❌ Transcripts directory not found: {transcripts_dir}")
        return
    
    # Process chapters 1-49
    enhanced = 0
    skipped = 0
    failed = 0
    
    for i in range(1, 50):
        # Find chapter folder (handles both "1-name" and "01-name" formats)
        chapter_folders = list(repo_root.glob(f"{i}-*"))
        if not chapter_folders:
            chapter_folders = list(repo_root.glob(f"{i:02d}-*"))
        
        if not chapter_folders:
            print(f"⚠️  Chapter {i} folder not found")
            failed += 1
            continue
        
        chapter_folder = chapter_folders[0]
        readme_path = chapter_folder / "README.md"
        transcript_path = transcripts_dir / f"{i:02d}-transcript.txt"
        
        if not readme_path.exists():
            print(f"⚠️  README not found for {chapter_folder.name}")
            failed += 1
            continue
        
        print(f"Processing {chapter_folder.name}...", end=' ')
        
        if enhance_readme(readme_path, transcript_path):
            print("✅ Enhanced")
            enhanced += 1
        else:
            skipped += 1
    
    print("\n" + "=" * 80)
    print(f"Summary: {enhanced} enhanced, {skipped} skipped, {failed} failed")
    print(f"Total: {enhanced}/{49} README files enhanced")


if __name__ == "__main__":
    main()
