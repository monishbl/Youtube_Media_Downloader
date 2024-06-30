# YouTube Video and Audio Downloader

## Description
This script allows users to download YouTube videos and audio at maximum available resolution using URL or by searching for a video based on a keyword. It utilizes the `yt_dlp` library for downloading videos and audio, and the `pytube` library for searching YouTube.

## How to Use
1. **Installation**:
   - Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
   - Install required libraries by running:
     ```
     pip install yt-dlp pytube
     ```
   - Install ffmpeg for merging audio and video. You can refer to ```ffmpeg_installation.md``` for detailed instructions.

2. **Running the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script `Downloader.py`.
   - Run the script using the command:
     ```
     python Downloader.py
     ```

3. **Using the Script**:
   - When prompted, enter either a YouTube video link (URL) or the name of the video you want to download.
   - If you enter a video link, the script will directly download it.
   - If you enter a video name, the script will search YouTube for that video and download the first result.
   - If the video link/title is valid, it will ask for format to download it

4. **Format Selection**:
   - By default, the script will download the best available quality for the video and audio.
   - If you want to select a specific quality, modify the `ydl_opts` dictionary in the script to include the desired format. For example, you can add `format: '137'` for 1080p videos and `format: '140'` for m4a audio.

5. **Note**:
   - Some videos may have restricted download permissions or may not be available in certain formats. In such cases, the script may not be able to download the video or audio.