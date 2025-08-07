from pydub import AudioSegment
import os

def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(file_path)
    
    # Convert to mono (required by Google STT)
    audio = audio.set_channels(1)
    
    chunks = []
    base = os.path.splitext(file_path)[0]
    
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_name = f"{base}_chunk_{i//chunk_length_ms}.wav"
        chunk.export(chunk_name, format="wav")
        chunks.append(chunk_name)
    
    return chunks
