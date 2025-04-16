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
    try:
        data = request.get_json(force=True)  # force=True ensures it parses JSON even if content-type is off
    except Exception as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    target_lang = data.get("target_lang", "en")

    try:
        summary = summarizer.summarize_text(text, target_lang)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": f"Summarization failed: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
