from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API key Render Environment se aayegi
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("text")

    if not user_text:
        return jsonify({"reply": "कुछ बोला नहीं गया"})

    prompt = f"""
    तुम एक smart AI assistant हो।
    सवाल को समझो, नया जवाब दो।
    repeat मत करना।
    इंसान की तरह बात करो।

    सवाल: {user_text}
    """

    response = model.generate_content(prompt)

    return jsonify({
        "reply": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
