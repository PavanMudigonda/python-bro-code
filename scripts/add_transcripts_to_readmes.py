#!/usr/bin/env python3
"""
Add transcripts to individual chapter README files.
"""

import re
import json
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Please install yt-dlp: pip install yt-dlp")
    exit(1)


def extract_video_id_from_readme(readme_path):
    """Extract video ID from a chapter README."""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for YouTube URL
    pattern = r'https://youtu\.be/([^\)]+)'
    match = re.search(pattern, content)
    if match:
        return match.group(1)
    return None


def fetch_transcript(video_id):
    """Fetch and format transcript using yt-dlp."""
    try:
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,  # Disable SSL verification
        }
        
        url = f'https://www.youtube.com/watch?v={video_id}'
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            subtitles = info.get('subtitles', {})
            automatic_captions = info.get('automatic_captions', {})
            captions = subtitles.get('en') or automatic_captions.get('en')
            
            if not captions:
                return "Transcript not available: No English subtitles"
            
            # Find JSON3 format subtitle
            subtitle_url = None
            for caption in captions:
                if caption.get('ext') == 'json3':
                    subtitle_url = caption.get('url')
                    break
            
            if not subtitle_url:
                subtitle_url = captions[0].get('url')
            
            if not subtitle_url:
                return "Transcript not available: Could not find subtitle URL"
            
            # Fetch subtitle content
            import urllib.request
            with urllib.request.urlopen(subtitle_url) as response:
                subtitle_data = json.loads(response.read().decode())
            
            # Format with timestamps
            formatted = []
            if 'events' in subtitle_data:
                for event in subtitle_data['events']:
                    if 'tStartMs' in event and 'segs' in event:
                        timestamp = int(event['tStartMs']) // 1000
                        minutes = timestamp // 60
                        seconds = timestamp % 60
                        
                        text_parts = []
                        for seg in event['segs']:
                            if 'utf8' in seg:
                                text_parts.append(seg['utf8'])
                        
                        if text_parts:
                            text = ''.join(text_parts).replace('\n', ' ').strip()
                            if text:
                                formatted.append(f"[{minutes:02d}:{seconds:02d}] {text}")
            
            return '\n'.join(formatted) if formatted else "Transcript not available: Could not parse subtitles"
                
    except Exception as e:
        return f"Transcript not available: {str(e)[:200]
            text = item['text'].replace('\n', ' ')
            formatted.append(f"[{minutes:02d}:{seconds:02d}] {text}")
        
        return '\n'.join(formatted)
    except Exception as e:
        return f"Transcript not available: {str(e)}"


def add_transcript_to_readme(readme_path):
    """Add transcript section to README if not already present."""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if transcript section already exists
    if '## 📝 Transcript' in content or '## Transcript' in content:
        print(f"Transcript already exists in {readme_path.name}")
        return False
    
    # Extract video ID
    video_id = extract_video_id_from_readme(readme_path)
    if not video_id:
        print(f"No video ID found in {readme_path.name}")
        return False
    
    # Fetch transcript
    print(f"Fetching transcript for {readme_path.parent.name}...", end=' ')
    transcript = fetch_transcript(video_id)
    
    if transcript.startswith("Transcript not available"):
        print(f"❌ {transcript}")
        return False
    
    # Add transcript section before "Coming Soon" or at the end
    transcript_section = f"\n\n## 📝 Video Transcript\n\n<details>\n<summary>Click to expand full transcript</summary>\n\n```\n{transcript}\n```\n\n</details>\n"
    
    # Insert before "Coming Soon" section or at the end
    if '## 📖 Coming Soon' in content:
        content = content.replace('## 📖 Coming Soon', transcript_section + '\n## 📖 Coming Soon')
    else:
        content += transcript_section
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Added")
    return True


def main():
    """Process all chapter READMEs."""
    repo_root = Path(__file__).parent.parent
    
    # Find all chapter folders
    chapter_folders = sorted([d for d in repo_root.iterdir() 
                             if d.is_dir() and re.match(r'^\d+-.+', d.name)])
    
    print(f"Found {len(chapter_folders)} chapter folders")
    
    successful = 0
    failed = 0
    
    for folder in chapter_folders:
        readme_path = folder / "README.md"
        if readme_path.exists():
            if add_transcript_to_readme(readme_path):
                successful += 1
            else:
                failed += 1
        else:
            print(f"No README.md in {folder.name}")
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"Summary: {successful} transcripts added, {failed} skipped/failed")


if __name__ == "__main__":
    main()
