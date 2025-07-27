
# proxy config 
$env:HTTP_PROXY = "http://127.0.0.1:10808"
$env:HTTPS_PROXY = "http://127.0.0.1:10808"

# run python
python ./groq_telegram_bot.py
