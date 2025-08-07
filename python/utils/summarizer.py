import google.generativeai as genai
import os

def summarize_text(text):

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"Summarize the following YouTube transcript into concise, structured notes:\n\n{text}"

    response = model.generate_content(prompt)

    return response.text.strip()
