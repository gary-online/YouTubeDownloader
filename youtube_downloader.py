import yt_dlp as youtube_dl  # Use yt-dlp in place of youtube_dl


def download_from_youtube():
    # URL Source Selection
    url = input("Enter the YouTube or YouTube Music URL: ")
    if "music.youtube.com" in url:
        print("Detected YouTube Music URL.")
    else:
        print("Detected standard YouTube URL.")

    # Format Selection using Numerical Choices
    print("Choose desired format:\n1. Video\n2. Audio")
    format_choice = input("Enter your choice (1/2): ")

    # youtube_dl Configuration
    if format_choice == "2":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': './%(title)s.%(ext)s',
        }
    elif format_choice == "1":
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': './%(title)s.%(ext)s',
        }
    else:
        print("Invalid format choice. Exiting.")
        return

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    download_from_youtube()
