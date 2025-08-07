YouTube to Notes 📄🎧

A tool that converts YouTube videos into structured, summarized text notes — perfect for learning, research, and content review. Powered by Python, Google Cloud Speech-to-Text, and Gemini, and accessible via a handy browser extension.
🔧 Features

    🎥 Download audio directly from YouTube videos

    🔊 Automatically split audio for optimized processing

    🧠 Transcribe audio using Google Cloud Speech-to-Text

    ✍️ Summarize transcripts using Gemini AI (via Google Generative AI)

    🌐 JavaScript browser extension for easy API access

🧩 Project Structure

youtube-to-notes/
│
├── main.py                  # Orchestrates the process
├── downloader.py            # Downloads YouTube audio
├── splitter.py              # Splits audio into chunks
├── transcriber.py           # Converts audio to text
├── summarizer.py            # Uses Gemini to summarize text
├── extension/               # Browser extension JS code
└── README.md                # This file

🐍 Python Backend
1. Download Audio from YouTube

download_audio(youtube_url, output_path="audio.wav")

Uses yt_dlp to extract and convert YouTube audio into a .wav file.
2. Split Audio into Chunks

split_audio("audio.wav")

Uses pydub to split audio into 60-second mono chunks, which is required by Google Cloud Speech-to-Text.
3. Transcribe Audio

transcribe_audio_chunks(chunk_paths)

Uses Google Cloud's speech API to transcribe each chunk asynchronously and stitch together the full transcript.
4. Summarize Transcript

summarize_text(full_transcript)

Sends the transcript to Google's Gemini model for summarization into concise, structured notes.
🌐 Browser Extension (JS)

The extension allows users to click a button while on YouTube and send the current video URL to your Python backend. The backend processes the video and returns summarized notes.
Example Flow:

    User visits a YouTube video

    Clicks the extension button

    The extension sends the video URL to the backend API

    The backend:

        Downloads and processes the audio

        Transcribes the content

        Summarizes the transcript

    Summary is returned to the extension and displayed to the user

🛠️ Requirements
Python:

    yt_dlp

    pydub

    google-cloud-speech

    google-generativeai

Install dependencies:

pip install yt_dlp pydub google-cloud-speech google-generativeai

Make sure FFmpeg is installed for audio processing:

# Ubuntu
sudo apt install ffmpeg

# Mac (brew)
brew install ffmpeg

Also, configure your environment for Google Cloud access:

    Set up authentication for google-cloud-speech

    Authenticate and initialize Gemini with API access for google-generativeai

🚀 Usage

Python:

url = "https://www.youtube.com/watch?v=example"
audio_file = download_audio(url)
chunks = split_audio(audio_file)
transcript = transcribe_audio_chunks(chunks)
summary = summarize_text(transcript)
print(summary)

Browser Extension:
Make sure your extension is set up to call the API route on your server with the current YouTube URL.
🧠 Future Enhancements

    Multilingual support for transcription

    UI for editing and saving summaries

    Option to export summaries to Markdown or PDF

    Caching/transcript reuse for already-processed videos

📄 License

MIT License — free to use and modify for personal and commercial projects.
