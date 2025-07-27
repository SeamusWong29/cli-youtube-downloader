import os
import argparse
from utils import download_video

def main():
    ap = argparse.ArgumentParser(description="YouTube Vidoe Downloader CLI")
    ap.add_argument("--url", required=True, help="YouTube video URL")
    ap.add_argument("--output", default="downloads", help='Outut directory') 
    ap.add_argument("--dry-run", action="store_true", help="Print planned actions without making changes") 
    args = ap.parse_args()

    if args.dry_run and not os.path.exists(args.output):
        print(f"[DRY-RUN] Would create folder at {args.output}")
    elif not os.path.exists(args.output):
        os.mkdir(args.output)

    download_video(args.url, args.output, args.dry_run)
                    
if __name__ == '__main__':
    main()

read