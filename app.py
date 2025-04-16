from flask import Flask, request, jsonify
from summarizer.summarizer import Summarizer
import os

app = Flask(__name__)
summarizer = Summarizer()

@app.route("/", methods=["GET"])
def home():
    return "CareCompanion Summarizer API is running."

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(force-True)
    text = data.get("text")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Missing 'text' field"}), 400

    summary = summarizer.summarize_text(text, target_lang)
    return jsonify({"summary": summary})

# Ensure the app listens on the correct port assigned by Render
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
