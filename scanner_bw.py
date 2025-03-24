import requests
from bs4 import BeautifulSoup
from utils import hash_text, keyword_match, ticker_match, send_discord_alert
import config

seen = set()

def scan():
    url = "https://www.businesswire.com/portal/site/home/news/industry/?vnsId=31452"
    headers = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, "lxml")
    articles = soup.select("li.bwNewsItem")

    for article in articles:
        link_elem = article.find("a")
        if not link_elem: continue
        title = link_elem.get_text(strip=True)
        link = "https://www.businesswire.com" + link_elem.get("href")
        hash_id = hash_text(link)

        if hash_id not in seen and keyword_match(title, config.KEYWORDS) and ticker_match(title, config.TICKERS):
            seen.add(hash_id)
            send_discord_alert(title, link)