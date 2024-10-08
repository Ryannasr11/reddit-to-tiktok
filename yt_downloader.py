import sys
import yt_dlp

def download_video(youtube_url, output_file):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_file,
        'merge_output_format': 'mp4',  # Merge video and audio into an MP4 file
        'verbose': True  # Enable verbose output for debugging
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from URL: {youtube_url}")
            ydl.download([youtube_url])
            print(f"Video successfully downloaded and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python scripty.py <youtube_url> <output_file>")
        print("Example: python3 youtube_download/yt_downloader.py https://www.youtube.com/watch?v=9bZkp7q19f0 output.mp4")
        sys.exit(1)

    youtube_url = sys.argv[1]
    output_file = sys.argv[2]

    print(f"URL: {youtube_url}")
    print(f"Output file: {output_file}")

    download_video(youtube_url, output_file)

if __name__ == "__main__":
    main()
