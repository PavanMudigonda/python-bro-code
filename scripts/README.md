# Transcript Fetching Scripts

This directory contains scripts to programmatically fetch YouTube video transcripts for all chapters using **yt-dlp**.

## Prerequisites

Install the required Python package:

```bash
pip install yt-dlp
```

## Scripts

### 1. `fetch_transcripts.py`

Fetches transcripts for all 93 videos and saves them as individual text files in the `transcripts/` directory.

**Usage:**
```bash
python scripts/fetch_transcripts.py
```

**Output:**
- Creates `transcripts/` folder in the repository root
- Saves each transcript as `01-transcript.txt`, `02-transcript.txt`, etc.
- Each file includes video title, URL, and full transcript

### 2. `add_transcripts_to_readmes.py`

Automatically adds transcript sections to each chapter's README.md file.

**Usage:**
```bash
python scripts/add_transcripts_to_readmes.py
```

**What it does:**
- Scans all chapter folders for README.md files
- Extracts video ID from each README
- Fetches the transcript from YouTube
- Adds a collapsible transcript section to the README
- Includes timestamps for easy navigation

**Example Output:**
The script adds a section like this to each README:

```markdown
## 📝 Video Transcript

<details>
<summary>Click to expand full transcript</summary>

\```
[00:00] Welcome to this Python tutorial...
[00:15] In this video we're going to learn...
[01:30] Let's start by creating...
\```

</details>
```

## Notes

- Uses **yt-dlp** which is more robust than youtube-transcript-api
- Works better with SSL certificates and corporate networks
- Supports both manual and auto-generated captions
- Auto-generated transcripts may contain errors
- Transcripts include timestamps in [MM:SS] format
- yt-dlp handles age-restricted and region-locked videos better

## Benefits

1. **Enhanced Learning**: Read along with videos
2. **Quick Reference**: Find specific topics without watching entire video
3. **Searchability**: Search transcript text for specific concepts
4. **Accessibility**: Better experience for deaf/hard-of-hearing learners
5. **Translation**: Can be translated to other languages

## Troubleshooting

**Import Error:**
```basht-dlp
```

**No transcripts found:**
- Video may not have captions enabled
- Auto-generated captions may be disabled
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

**SSL/Network issues:**
yt-dlp handles SSL certificates and proxies better than other tools. If you still have issues, try:
```bash
pip install --upgrade yt-dlp certifi
```
If fetching many transcripts, YouTube may rate limit. Add delays between requests if needed.
