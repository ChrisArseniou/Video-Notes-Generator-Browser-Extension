# π§ YouTube to Notes

Transform any YouTube video into **summarized, structured notes** using speech recognition and AI summarization.  
This project combines a Python backend with a browser extension frontend to make learning from videos easier and faster.

---

## π“ Overview

- **Extracts audio** from YouTube videos  
- **Splits** long audio files into short chunks  
- **Transcribes** speech to text using Google Cloud Speech-to-Text  
- **Summarizes** transcripts using Gemini (Google Generative AI)  
- **Browser extension** to trigger summarization from any YouTube video  

---

## π—‚οΈ Project Structure

```
youtube-to-notes/
β”‚
β”β”€β”€ downloader.py       # Downloads and extracts audio from YouTube
β”β”€β”€ splitter.py         # Splits audio into smaller chunks
β”β”€β”€ transcriber.py      # Converts audio chunks to text
β”β”€β”€ summarizer.py       # Summarizes full transcript using Gemini AI
β”β”€β”€ main.py             # Orchestrates the entire pipeline
β”β”€β”€ extension/          # Browser extension files (popup, scripts)
β””β”€β”€ README.md           # Project documentation
```

---

## π§  How It Works

### 1. **Download YouTube Audio**
Downloads the best-quality audio stream using `yt_dlp`, and converts it to WAV.

```python
download_audio(youtube_url)
```

---

### 2. **Split Audio Into Chunks**
To comply with speech recognition limits, the audio is split into 60-second mono chunks.

```python
split_audio("audio.wav")
```

---

### 3. **Transcribe Audio Chunks**
Uses Google Cloud's asynchronous `Speech-to-Text` API to convert each chunk to text.

```python
transcribe_audio_chunks(chunk_paths)
```

---

### 4. **Summarize the Transcript**
Sends the full transcript to Gemini for a clean, structured summary.

```python
summarize_text(full_transcript)
```

---

## π Browser Extension

A simple browser extension allows you to summarize YouTube videos directly from your browser.

### β… Features:
- Detects current video URL
- Sends it to your Python backend
- Receives the summarized notes
- Displays results in the popup UI

**Directory:** `/extension/`

> Want help generating the manifest or popup UI code? Just ask.

---

## π› οΈ Requirements

### Python Packages
- `yt_dlp`
- `pydub`
- `google-cloud-speech`
- `google-generativeai`

### System Dependencies
- **FFmpeg** (used by `pydub` and `yt_dlp`)

---

## π” Authentication

### Google Cloud Speech-to-Text
- Requires a valid Google Cloud project
- Set up a service account and download the JSON key file
- Set environment variable:

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/key.json"
```

### Google Generative AI (Gemini)
- Requires API key
- Initialize your client using the `google-generativeai` library

---

## π€ Example Usage

```python
from downloader import download_audio
from splitter import split_audio
from transcriber import transcribe_audio_chunks
from summarizer import summarize_text

url = "https://www.youtube.com/watch?v=your_video_id"
audio_path = download_audio(url)
chunks = split_audio(audio_path)
transcript = transcribe_audio_chunks(chunks)
summary = summarize_text(transcript)

print(summary)
```

---

## π“¦ Installation

### Python Environment
Use your preferred environment manager (e.g., `venv`, `poetry`, or `conda`), then install:

```python
pip install yt_dlp pydub google-cloud-speech google-generativeai
```

### FFmpeg
Ensure FFmpeg is installed and accessible on your system path.

---

## π“ To Do / Roadmap

- [ ] Add support for multilingual transcription
- [ ] Provide export options (Markdown, PDF)
- [ ] Cache transcripts to avoid reprocessing
- [ ] UI improvements in browser extension
- [ ] Deployable API service (Flask/FastAPI)

---

## π“„ License

MIT License  
Feel free to use, modify, and distribute.
