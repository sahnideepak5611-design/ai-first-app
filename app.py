from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Gemini API key from Render Environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("text")

    try:
        response = model.generate_content(user_text)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "मुझे समझ नहीं आया, फिर से बोलो"})


if __name__ == "__main__":
    app.run()
