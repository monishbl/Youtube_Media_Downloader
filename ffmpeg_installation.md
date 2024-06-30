## FFmpeg Installation

FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams.

### Windows

1. Download the latest version of FFmpeg from the [official website](https://ffmpeg.org/download.html).
2. Extract the downloaded zip file. This should result in a folder named something like `ffmpeg-4.4-essentials_build`.
3. Move this folder to `C:\` and rename it to `ffmpeg`.
4. Add `ffmpeg` to your system's PATH:
   - Search for `Environment Variables` in your computer's search bar and select `Edit the system environment variables`.
   - In the System Properties window that appears, click `Environment Variables`.
   - In the Environment Variables window, under `System variables`, find `Path` and click `Edit`.
   - In the Edit Environment Variable window, click `New` and add `C:\ffmpeg\bin`.
   - Click `OK` in all windows.

### Linux

1. Update the packages list:
   ```bash
   sudo apt update
   ```
2. Install FFmpeg by typing:
   ```bash
   sudo apt install ffmpeg
   ```
3. Verify the installation by checking the version:
   ```bash
   ffmpeg -version
   ```

### macOS

1. Update Homebrew's package database:
   ```bash
   brew update
   ```
2. Install FFmpeg:
   ```bash
   brew install ffmpeg
   ```
3. Verify the installation by checking the version:
   ```bash
   ffmpeg -version
   ```