import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
from flask_cors import CORS


# Load .env variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

app = Flask(__name__)
CORS(app)
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "Message is required"}), 400

        print(f"Received message: {message}")

        # Build the OpenRouter API payload
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",  # Update when deployed
            "X-Title": "Manufacturing Cost Analyzer"
        }

        payload = {
            "model": "google/gemini-pro",  
            "messages": [
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            print(f"OpenRouter Error: {response.text}")
            return jsonify({"error": "Failed to get response from OpenRouter."}), 500

        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print(f"OpenRouter Response: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

