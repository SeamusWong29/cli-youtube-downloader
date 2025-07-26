from pytube import YouTube

def download_video(video_url: str, output_dir: str, dry_run: bool = False):
    """
    Download video in the given from the Youtube video url provided

    Parameters:
        video_url: Youtube video URL 
        output_dir: Video output folder
        dry_run: if true, ony print the planned actions, without downloading video to the given path
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
        
    