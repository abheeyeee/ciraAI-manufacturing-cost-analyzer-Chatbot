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
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "Message is required"}), 400

        print(f"Received message: {message}")

        
        completion = client.chat.completions.create(
            model="google/gemini-2.5-flash-lite",   
            messages=[{"role": "user", "content": message}],
            extra_headers={
                "HTTP-Referer": "http://localhost:5173",
                "X-Title": "CiraAI"
            }
        )

        reply = completion.choices[0].message.content
        print(f"Reply: {reply}")
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong."}), 500

 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
