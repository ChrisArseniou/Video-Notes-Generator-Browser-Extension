from flask import Flask, request, jsonify
from utils.downloader import download_audio
from utils.splitter import split_audio
from utils.transcriber import transcribe_audio_chunks
from utils.summarizer import summarize_text
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"/summarize": {"origins": "*"}},
    methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
    supports_credentials=False
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-crentials.json"

# Example bodies to hit the endpoint
# {
#   "url": "https://www.youtube.com/watch?v=3olUrSOHts0"
# }


@app.route("/summarize", methods=["POST"])
def summarize():
        
    try:
        print("Raw request data:", request.data)
        
        if not request.is_json:
            return jsonify({"error": "Missing JSON in request"}), 400
        
        data = request.json
        print("Parsed JSON:", data)

        url = data.get("url")

        rl = data.get("url")
        if not url or url.strip() == "":
            return jsonify({"error": "URL is empty or missing"}), 400

        try:
            print("Step 1: Downloading audio...")
            audio_path = download_audio(url)

            print("Step 2: Splitting audio...")
            chunks = split_audio(audio_path)

            print("Step 3: Transcribing audio...")
            transcript = transcribe_audio_chunks(chunks)

            print("Step 4: Summarizing...")
            summary = summarize_text(transcript)

            return jsonify({"summary": summary})

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
