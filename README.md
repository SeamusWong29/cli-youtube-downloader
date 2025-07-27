# CLI YouTube Downloader

A simple Python-based command-line tool to download Youtube videos in the highest resolution using 'pytube'.

---

## Example CLI Command
```bash
# Download to default folder
python main.py --url "https://youtu.be/dQw4w9WgXcQ"
```

```bash
# Download to custom folder
python main.py --url "https://youtu.be/dQw4w9WgXcQ" --output "~/videos"
```

```bash
# Dry run (test first)
python main.py --url "https://youtu.be/dQw4w9WgXcQ" --dry-run
```

## Feature
- Download videos from Youtube by url
- Saves to a custom output directory (default './downloads')
- Progress feedback during download.

---

## Installation & Usage
1. **Clone and install**:
```bash
git clone https://github.com/SeamusWong29/cli-youtube-downloader.git
cd cli-youtube-downloader
pip install -r requirements.txt
```
2. **Download Video**:
```bash
# Usage
python main.py --url"<YouTube Video URL>" --output"<Directory>"
```
