import requests
import time

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
        # new messages
        response = requests.get(f'{TELEGRAM_API}/getUpdates?offset={last_update_id + 1}')
        data = response.json()

        for update in data['result']:
            if 'message' not in update:
                continue

            chat_id = update['message']['chat']['id']
            user_text = update['message'].get('text', '')
            last_update_id = update['update_id']

            print(f'📨 Message from {chat_id}: {user_text}')

            # skipe if message is null
            if not user_text.strip():
                continue

            # request ro groq
            groq_response = requests.post(
                GROQ_API_URL,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {GROQ_API_KEY}"
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": [{"role": "user", "content": user_text}]
                }
            )

            result = groq_response.json()
            reply = result['choices'][0]['message']['content']

            # send message to telegram
            requests.post(f'{TELEGRAM_API}/sendMessage', data={
                'chat_id': chat_id,
                'text': reply
            })

    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(1)
