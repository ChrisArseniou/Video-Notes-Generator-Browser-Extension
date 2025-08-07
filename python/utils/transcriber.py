from google.cloud import speech
import time

def transcribe_audio_chunks(chunk_paths):
    client = speech.SpeechClient()
    full_transcript = ""

    for path in chunk_paths:
        with open(path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code="en-US"
        )

        print(f"Transcribing chunk: {path} (async)...")
        operation = client.long_running_recognize(config=config, audio=audio)

        # Wait for operation to complete
        response = operation.result(timeout=180)

        for result in response.results:
            full_transcript += result.alternatives[0].transcript + " "

    return full_transcript
