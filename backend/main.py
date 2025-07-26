from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
 
load_dotenv()
 
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)
 
app = Flask(__name__)
CORS(app, origins=["https://chatbot-frontend-f8pa.onrender.com"])  
 
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        messages = data.get("messages", [])

        if not messages or not isinstance(messages, list):
            return jsonify({"error": "Messages list is required"}), 400

        print("Received chat history:")
        for m in messages:
            print(f"{m['role']}: {m['content']}")

        completion = client.chat.completions.create(
            model="google/gemini-2.5-flash-lite",
            messages=messages,
            extra_headers={
                "HTTP-Referer": "https://chatbot-frontend-f8pa.onrender.com",
                "X-Title": "CiraAI"
            }
        )

        reply = completion.choices[0].message.content
        print(f"Reply: {reply}")
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong."}), 500
