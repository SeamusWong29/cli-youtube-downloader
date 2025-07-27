from pytube import YouTube
import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context
# OR safer version:
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

def download_video_py(video_url: str, output_dir: str, dry_run: bool = False):
    """
    Download a Youtube video in the highest resolution.

    Parameters:
        video_url (str): Youtube video URL 
        output_dir (str): Video output folder
        dry_run (bool): if true, ony print the planned actions, without downloading video to the given path
    """
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        print(f"Video Title: {yt.title}")

        if dry_run:
            print(f"[Dry-Run] Would download to: {output_dir}")
        else:
            stream.download(output_path=output_dir)
            print(f"Saved to {output_dir}")
    except Exception as e:
        print(f"Error: {e}")

        
import os
import subprocess

def download_video(url, output_dir, dry_run=False):
    command = [
        "yt-dlp",
        "-f", "best",
        "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
        url
    ]

    if dry_run:
        print("[DRY-RUN] Would run:", " ".join(command))
    else:
        print("[INFO] Downloading video...")
        subprocess.run(command)

        
    