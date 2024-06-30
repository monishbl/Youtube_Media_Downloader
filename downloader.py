import sys
import os
import yt_dlp
from pytube import Search

sys.stderr = open('stderr.log', 'w')

Result_found = False
video_url = ""

def download_audio(video_url):
    global Result_found
    if Result_found:
        print(f"Downloading video from: {video_url}")
        output_folder = 'downloads/audio'
        os.makedirs(output_folder, exist_ok=True)
        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'noplaylist': False,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])
        print("Downloaded successfully.")
    else:
        print("No results found.")

def download_video(video_url):
    global Result_found
    if Result_found:
        output_folder = 'downloads/videos'
        os.makedirs(output_folder, exist_ok=True)
        options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'noplaylist': False,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])
        print("Downloaded successfully.")
    else:
        print("No results found.")

def get_url(query):
    global Result_found
    global video_url
    if query.startswith("https://"):
        video_url = query
        Result_found = True
    else:
        search = Search(query)
        results = search.results
        if not results:
            print("No results found.")
            return
        Result_found = True
        video_url = results[0].watch_url

query = input("Enter YouTube Video link or Video name: ")
get_url(query)

if Result_found:
    print("1. Download as Audio(MP3)")
    print("2. Download as Video(MP4)")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        download_audio(video_url)
    elif choice == 2:
        download_video(video_url)
    else:
        print("Invalid choice.")

sys.stderr.close()

if os.path.exists('stderr.log'):
    os.remove('stderr.log')