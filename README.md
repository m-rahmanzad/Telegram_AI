# 🤖 Telegram AI Assistant using Groq API

A simple Telegram bot that connects your Telegram account to a powerful AI model (such as LLaMA 3 or Gemma) via the [Groq API](https://groq.com). The bot receives messages from users, sends them to the AI, and replies back with the response.

---

## ✨ Features

- ✅ Telegram bot integration
- ✅ Supports Groq API with models like LLaMA 3, Gemma, and more
- ✅ Lightweight and easy to deploy
- ✅ Optional proxy support (e.g. for users behind a firewall)

---

## 📦 Requirements

- Python 3.8+
- A Telegram Bot Token (create via [@BotFather](https://t.me/BotFather))
- A Groq API key (get one at [console.groq.com](https://console.groq.com/))
- Python dependencies:
  ```bash
  pip install requests



🧠 Supported Models on Groq
You can view all available models and their identifiers here:
🔗 Groq Model List

Example model names:

meta-llama/llama-3-8b-instruct

meta-llama/llama-3-70b-instruct

google/gemma-7b-it

gemini

🔧 Installation & Setup
Clone this repo:

bash
Copy
Edit
git clone https://github.com/yourusername/groq-telegram-bot.git
cd groq-telegram-bot
Create a .env file or set your secrets manually:

Open the Python file and replace the following placeholders:

TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"

GROQ_API_KEY = "your-groq-api-key"

MODEL = "your-desired-model" (e.g., meta-llama/llama-3-70b-instruct)

Run the bot:

bash
Copy
Edit
python groq_telegram_bot.py
💡 Optional: Use with Proxy on Windows PowerShell
If you're behind a proxy (e.g., using Clash or V2Ray), and want to run the bot via proxy:

Open PowerShell and allow script execution (first time only):

powershell
Copy
Edit
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Run the helper script:

powershell
Copy
Edit
.\run_via_proxy.ps1
This sets the environment proxy and runs the bot automatically.

📸 Example
Send a message to your Telegram bot like:

What is the difference between GPT and LLaMA?

And get a smart, AI-generated response powered by Groq!

📁 File Structure
bash
Copy
Edit
groq-telegram-bot/
│
├── groq_telegram_bot.py       # Main bot logic
├── run_via_proxy.ps1          # Windows script to run behind proxy
└── README.md                  # Project info


🔐 Security Notice
Do not hardcode or expose your API keys in public repositories.
Use .env or a secure secrets manager if you're deploying this in production.

🧠 Future Ideas
 Support conversation history (chat memory)

 Add logging and admin commands

 Multi-user rate limiting

📬 Contact
Made with ❤️ by Mostafa
Feel free to fork, use, and contribute.

🏷️ License
MIT License

📢 Hashtags (for social sharing)
#TelegramBot #Python #AI #Groq #LLaMA #Gemma #OpenSource #Chatbot #LLM #NLP
