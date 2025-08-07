import yt_dlp
import os

def download_audio(youtube_url, output_path="audio.wav"):
    output_base = output_path.replace(".wav", "")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{output_base}.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    return f"{output_base}.wav"