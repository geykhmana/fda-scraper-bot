import requests
import datetime
import hashlib
import config

def hash_text(text):
    return hashlib.md5(text.encode()).hexdigest()

def keyword_match(text, keywords):
    return any(k.lower() in text.lower() for k in keywords)

def ticker_match(text, tickers):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today_tickers = tickers.get(today, [])
    return any(t.lower() in text.lower() for t in today_tickers)

def send_discord_alert(title, link):
    message = f"🚨 **FDA News Detected!**\n**Title:** {title}\n**Link:** {link}\n⏰ {datetime.datetime.now()}"
    requests.post(config.DISCORD_WEBHOOK_URL, json={"content": message})