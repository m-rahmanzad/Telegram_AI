import requests
import time
from datetime import datetime

# ==== API&Token ====
TELEGRAM_TOKEN = '22222222222222:AAErgb48aBadasdadadadadpk'
GROQ_API_KEY = 'gsk_asdasdasdasdadadasdasdasasdsaJ'
GROQ_MODEL = 'gemma2-9b-it'

# ==== URLs ====
TELEGRAM_API = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}'
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

# ==== new message ====
last_update_id = 0

# ==== main loop ====
print("🤖 Bot is running...")

while True:
    try:
        # Try to get new updates from Telegram
        response = requests.get(f'{TELEGRAM_API}/getUpdates?offset={last_update_id + 1}', timeout=10)
        data = response.json()

        for update in data['result']:
            if 'message' not in update:
                continue

            message = update['message']
            user_info = message.get("from", {})
            username = user_info.get("username") or f'{user_info.get("first_name", "")} {user_info.get("last_name", "")}'.strip()
            chat_id = message['chat']['id']
            user_text = message.get('text', '')
            last_update_id = update['update_id']

            # Print message with timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'[{timestamp}] 📨 Message from {chat_id} ({username}): {user_text}')

            if not user_text.strip():
                continue

            # Send user input to GROQ
            groq_response = requests.post(
                GROQ_API_URL,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {GROQ_API_KEY}"
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": [{"role": "user", "content": user_text}]
                },
                timeout=15
            )

            result = groq_response.json()
            reply = result['choices'][0]['message']['content']

            # Send reply to Telegram
            requests.post(f'{TELEGRAM_API}/sendMessage', data={
                'chat_id': chat_id,
                'text': reply
            }, timeout=10)

    except requests.exceptions.RequestException as net_err:
        print("🌐 Network error:", net_err)
        print("⏳ Waiting 10 seconds before retrying...")
        time.sleep(10)

    except Exception as e:
        print("⚠️ General error:", e)
        time.sleep(2)  # Shorter delay for other errors

    time.sleep(1)  # Normal loop delay
