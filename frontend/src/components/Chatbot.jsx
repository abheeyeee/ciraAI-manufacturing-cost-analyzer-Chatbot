import { useState } from 'react';

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { from: 'bot', text: 'Hi! I can help calculate your manufacturing costs. Ready?' }
  ]);
  const [userInput, setUserInput] = useState('');

  const handleSend = async () => {
    if (!userInput.trim()) return;

    const newMessages = [...messages, { from: 'user', text: userInput }];
    setMessages(newMessages);
    setUserInput('');

    try {
      const res = await fetch("https://chatbot-backend-7ij7.onrender.com/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
      });

      const data = await res.json();
      const botReply = data.reply || "Sorry, I couldn't process that.";

      setMessages([...newMessages, { from: 'bot', text: botReply }]);
    } catch (error) {
      setMessages([...newMessages, { from: 'bot', text: "Sorry, there was an error." }]);
    }
  };

  return (
    <div className="max-w-xl w-full mx-auto bg-white shadow-xl rounded-xl p-4 border border-indigo-100 animate-fade-in">
      <div className="text-2xl font-bold mb-3 text-center text-indigo-600">ciraAI🤖</div>
      
      <div className="h-80 overflow-y-auto mb-4 space-y-2 bg-gray-100 p-2 rounded">
        {messages.map((msg, i) => (
          <div key={i} className={`text-sm ${msg.from === 'bot' ? 'text-left' : 'text-right'}`}>
            <span className={`inline-block px-3 py-2 rounded-lg ${msg.from === 'bot' ? 'bg-blue-100' : 'bg-green-100'}`}>
              {msg.text}
            </span>
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          className="flex-1 border rounded px-3 py-2"
          value={userInput}
          onChange={e => setUserInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && handleSend()}
          placeholder="Type your question..."
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
