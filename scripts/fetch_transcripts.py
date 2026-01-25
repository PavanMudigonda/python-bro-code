#!/usr/bin/env python3
"""
Fetch YouTube transcripts for all video chapters in the python-bro-code repository.
"""

import re
import os
import json
import subprocess
import time
from pathlib import Path

# You'll need to install: pip install yt-dlp
try:
    import yt_dlp
except ImportError:
    print("Please install yt-dlp: pip install yt-dlp")
    exit(1)


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def fetch_transcript(video_id):
    """Fetch transcript for a given video ID using yt-dlp."""
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,  # Disable SSL verification (for corporate networks)
        }
        
        url = f'https://www.youtube.com/watch?v={video_id}'
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Try to get subtitles
            subtitles = info.get('subtitles', {})
            automatic_captions = info.get('automatic_captions', {})
            
            # Prefer manual subtitles, fallback to automatic
            captions = subtitles.get('en') or automatic_captions.get('en')
            
            if not captions:
                return "No English subtitles available"
            
            # Download the subtitle file (usually JSON format)
            subtitle_url = None
            for caption in captions:
                if caption.get('ext') == 'json3':
                    subtitle_url = caption.get('url')
                    break
            
            if not subtitle_url:
                # Try any format
                subtitle_url = captions[0].get('url')
            
            if not subtitle_url:
                return "Could not find subtitle URL"
            
            # Fetch subtitle content
            import urllib.request
            with urllib.request.urlopen(subtitle_url) as response:
                subtitle_data = json.loads(response.read().decode())
            
            # Extract text from JSON3 format
            if 'events' in subtitle_data:
                texts = []
                for event in subtitle_data['events']:
                    if 'segs' in event:
                        for seg in event['segs']:
                            if 'utf8' in seg:
                                texts.append(seg['utf8'])
                return ' '.join(texts).replace('\n', ' ')
            else:
                return "Unknown subtitle format"
                
    except Exception as e:
        return f"Error: {str(e)[:200]}"


def parse_readme_for_videos():
    """Parse main README.md for video URLs."""
    readme_path = Path(__file__).parent.parent / "README.md"
    
    if not readme_path.exists():
        print(f"README.md not found at {readme_path}")
        return []
    
    videos = []
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Pattern to match video entries
    # Example: - [x] 1. Start coding with PYTHON in 5 minutes! 🐍 (5:13) - https://youtu.be/Sg4GMVMdOPo
    pattern = r'- \[x\] (\d+)\. (.+?) - (https://youtu\.be/[^\s]+)'
    
    matches = re.findall(pattern, content)
    for num, title, url in matches:
        video_id = extract_video_id(url)
        if video_id:
            videos.append({
                'number': int(num),
                'title': title.strip(),
                'url': url,
                'video_id': video_id
            })
    
    return videos


def save_transcript(video_info, transcript, output_dir):
    """Save transcript to a file."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    filename = f"{video_info['number']:02d}-transcript.txt"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Video {video_info['number']}: {video_info['title']}\n")
        f.write(f"URL: {video_info['url']}\n")
        f.write("=" * 80 + "\n\n")
        f.write(transcript)
    
    return filepath


def main():
    """Main function to fetch all transcripts."""
    print("Parsing README.md for video links...")
    videos = parse_readme_for_videos()
    
    if not videos:
        print("No videos found in README.md")
        return
    
    print(f"Found {len(videos)} videos")
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / "transcripts"
    output_dir.mkdir(exist_ok=True)
    
    # Check which transcripts already exist
    existing_files = set(f.name for f in output_dir.glob("*-transcript.txt"))
    videos_to_fetch = []
    skipped = 0
    
    for video in videos:
        filename = f"{video['number']:02d}-transcript.txt"
        if filename in existing_files:
            print(f"⏭️  Skipping Video {video['number']}: {video['title'][:50]} (already exists)")
            skipped += 1
        else:
            videos_to_fetch.append(video)
    
    if not videos_to_fetch:
        print(f"\n✅ All {len(videos)} transcripts already downloaded!")
        return
    
    print(f"\nFetching {len(videos_to_fetch)} missing transcripts ({skipped} already exist)...\n")
    
    successful = 0
    failed = 0
    
    for video in videos_to_fetch:
        print(f"Fetching transcript for Video {video['number']}: {video['title'][:50]}...", end=' ')
        
        transcript = fetch_transcript(video['video_id'])
        
        if transcript.startswith("Error"):
            print(f"❌ {transcript}")
            failed += 1
            # If rate limited, wait longer before next attempt
            if "429" in transcript or "Too Many Requests" in transcript:
                print("   Rate limited - waiting 5 seconds before continuing...")
                time.sleep(5)
        else:
            filepath = save_transcript(video, transcript, output_dir)
            print(f"✅ Saved to {filepath.name}")
            successful += 1
            # Small delay between successful requests to avoid rate limiting
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print(f"Summary: {successful} successful, {failed} failed, {skipped} skipped")
    print(f"Total: {successful + skipped}/{len(videos)} transcripts downloaded")
    print(f"Transcripts saved to: {output_dir}")


if __name__ == "__main__":
    main()
