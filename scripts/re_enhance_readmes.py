#!/usr/bin/env python3
"""
Re-enhance README files with improved key points extraction.
This script will replace existing "Key Takeaways" sections with better extracted content.
"""

import os
import re
from pathlib import Path


def clean_transcript_text(text):
    """Clean transcript text by removing excessive whitespace."""
    # Remove header lines
    lines = text.split('\n')
    text = '\n'.join(lines[4:]) if len(lines) > 4 else text
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_key_points(transcript_text):
    """Extract key teaching points from the transcript with improved logic."""
    # Clean the text first
    text = clean_transcript_text(transcript_text)
    
    # Split into sentences (roughly)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    key_points = []
    
    # Keywords that indicate important teaching moments
    teaching_keywords = [
        'print', 'function', 'variable', 'type', 'syntax', 'create', 'define',
        'important', 'remember', 'note', 'use', 'understand', 'learn',
        'method', 'example', 'basic', 'simple', 'first', 'write', 'code',
        'install', 'download', 'setup', 'execute', 'run'
    ]
    
    code_indicators = ['print(', 'def ', 'class ', 'import ', '=', '()', 'return', '.py']
    
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


def read_transcript(transcript_path):
    """Read and return transcript content."""
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {transcript_path}: {e}")
        return ""


def re_enhance_readme(readme_path, transcript_path):
    """Re-enhance README by replacing existing key takeaways with improved extraction."""
    if not transcript_path.exists():
        return False, "no_transcript"
    
    # Read current README
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except Exception as e:
        print(f"Error reading README {readme_path}: {e}")
        return False, "read_error"
    
    # Read transcript
    transcript_text = read_transcript(transcript_path)
    if not transcript_text:
        return False, "empty_transcript"
    
    # Extract key points with improved algorithm
    key_points = extract_key_points(transcript_text)
    
    if not key_points:
        print(f"⚠️  No key points extracted for {readme_path.parent.name}")
        return False, "no_points"
    
    # Create new enhancement section
    enhancement = "## 🎓 Key Takeaways from Video\n\n"
    for i, point in enumerate(key_points, 1):
        enhancement += f"{i}. {point}\n"
    
    # Add note about transcript
    enhancement += "\n> 💡 *These points are extracted from the video transcript to enhance your learning experience.*\n"
    
    # Check if README already has key takeaways section
    if '## 🎓 Key Takeaways' in readme_content:
        # Remove existing section
        pattern = r'## 🎓 Key Takeaways from Video.*?(?=\n## |\Z)'
        readme_content = re.sub(pattern, '', readme_content, flags=re.DOTALL)
        
        # Insert new section before "Coming Soon" or at the end
        if '## 📖 Coming Soon' in readme_content:
            readme_content = readme_content.replace(
                '## 📖 Coming Soon',
                enhancement + '\n## 📖 Coming Soon'
            )
        else:
            readme_content += '\n' + enhancement
    else:
        # First time adding - insert before "Coming Soon" or at end
        if '## 📖 Coming Soon' in readme_content:
            readme_content = readme_content.replace(
                '## 📖 Coming Soon',
                enhancement + '\n## 📖 Coming Soon'
            )
        else:
            readme_content += '\n' + enhancement
    
    # Write back
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        return True, "enhanced"
    except Exception as e:
        print(f"Error writing README {readme_path}: {e}")
        return False, "write_error"


def main():
    # Base paths
    base_path = Path('/Users/nagapavankumar.mudigonda/code/python-bro-code')
    transcripts_path = base_path / 'transcripts'
    
    enhanced_count = 0
    skipped_count = 0
    failed_count = 0
    
    # Process chapters 1-49
    for i in range(1, 50):
        # Try both naming patterns: "1-name" and "01-name"
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
        
        # Find corresponding transcript
        transcript_files = list(transcripts_path.glob(f'{i:02d}-transcript.txt'))
        if not transcript_files:
            transcript_files = list(transcripts_path.glob(f'{i}-transcript.txt'))
        
        if not transcript_files:
            print(f"Processing {chapter_name}... ⏭️  No transcript available")
            skipped_count += 1
            continue
        
        transcript_path = transcript_files[0]
        
        # Re-enhance the README
        print(f"Processing {chapter_name}...", end=' ')
        success, status = re_enhance_readme(readme_path, transcript_path)
        
        if success:
            print("✅ Re-enhanced")
            enhanced_count += 1
        elif status == "no_transcript":
            print("⏭️  No transcript")
            skipped_count += 1
        else:
            print(f"❌ Failed ({status})")
            failed_count += 1
    
    print("\n" + "="*80)
    print(f"Summary: {enhanced_count} enhanced, {skipped_count} skipped, {failed_count} failed")
    print(f"Total: {enhanced_count}/{49} README files re-enhanced")


if __name__ == '__main__':
    main()
