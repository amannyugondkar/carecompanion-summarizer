from flask import Flask, request, jsonify
from summarizer.summarizer import Summarizer
import os

app = Flask(__name__)
summarizer = Summarizer()

@app.route("/")
def home():
    return "CareCompanion Summarizer API is running."

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Missing 'text' field"}), 400

    summary = summarizer.summarize_text(text, target_lang)
    return jsonify({"summary": summary})
