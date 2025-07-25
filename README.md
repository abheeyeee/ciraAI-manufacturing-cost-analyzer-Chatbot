
---

## 🔧 Tech Stack

- 🧠 **Frontend**: React + Vite + Tailwind CSS  
- ⚙️ **Backend**: Python + Flask  
- 🌐 **Deployment**: [Render.com](https://render.com)  
 

---

## 🚀 Live Demo

- **Frontend**: [https://chatbot-frontend-f8pa.onrender.com](https://chatbot-frontend-f8pa.onrender.com)  
- **Backend**: [https://chatbot-backend-7ij7.onrender.com](https://chatbot-backend-7ij7.onrender.com)

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/manufacturing-cost-analyzer-Chatbot.git
cd manufacturing-cost-analyzer-Chatbot

2. ## Backend Setup (/backend)
cd backend
pip install -r requirements.txt

#🔑 Create a .env file
OPENROUTER_API_KEY=your_openrouter_api_key
Be sure to keep your .env file secret!
.env            # should be in .gitignore

#Run Locally:
python main.py


3. ## Frontend Setup (/frontend)
cd frontend
npm install
npm run dev    # For development
npm run build  # For production

🧠 How It Works
User chats via the frontend chatbot.

The message is sent to the Flask API.

The backend calls OpenAI/OpenRouter with the prompt.

The chatbot returns step-by-step help or a cost summary.

