import os
import argparse
from utils import download_video

def main():
    ap = argparse.ArgumentParser(description="YouTube Vidoe Downloader CLI")
    ap.add_argument("--url", required=True, help="YouTube video URL")
    ap.add_argument("--output", default="downloads", help='Outut directory')
    ap.add_argument("--dry-run", default=False, help="Print planned actions without making changes") 
    args = ap.parse_args()

    if not os.path.exists(args.output):
        os.mkdir("downloads")

    download_video(args.url, args.output)
                    
if __name__ == '__main__':
    main()

