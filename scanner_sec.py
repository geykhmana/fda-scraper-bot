import requests
from bs4 import BeautifulSoup
from utils import hash_text, keyword_match, ticker_match, send_discord_alert
import config

seen = set()

def scan():
    feed_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent"
    soup = BeautifulSoup(requests.get(feed_url).content, "lxml")
    entries = soup.select("item")

    for entry in entries:
        title = entry.find("title").get_text()
        link = entry.find("link").get_text()
        hash_id = hash_text(link)

        if hash_id not in seen and keyword_match(title, config.KEYWORDS) and ticker_match(title, config.TICKERS):
            seen.add(hash_id)
            send_discord_alert(title, link)