"""
Собирает кандидатов для постов из открытых RSS-лент.

НИЧЕГО НЕ ПУБЛИКУЕТ. Только складывает найденное в bot/drafts.json,
чтобы человек просмотрел и решил, о чём писать. Копировать чужой текст
в канал нельзя — берём только заголовок, дату и ссылку на источник
как повод написать своё.

Запуск: python3 bot/fetch_news.py
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from xml.etree import ElementTree

DRAFTS_FILE = os.path.join(os.path.dirname(__file__), "drafts.json")

# Ленты. Проверь каждую в браузере перед первым запуском — адреса меняются.
FEEDS = [
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("CoinDesk", "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("Cointelegraph", "https://cointelegraph.com/rss"),
    ("Decrypt", "https://decrypt.co/feed"),
    ("The Defiant", "https://thedefiant.io/api/feed"),
]

# Что нас интересует: кражи, фишинг, социнженерия, кошельки
# Заголовок проходит, только если в нём есть И криптослово, И слово про кражу.
# Иначе лента забивается корпоративной безопасностью: серверы, роутеры, больницы.
CRYPTO_WORDS = [
    "crypto", "bitcoin", "ethereum", "wallet", "seed phrase", "seed-phrase",
    "private key", "defi", "web3", "nft", "token", "blockchain", "onchain",
    "on-chain", "metamask", "ledger", "trezor", "cold storage", "self-custody",
    "crypto exchange", "stablecoin", "usdt", "usdc", "solana", "binance",
]

THEFT_WORDS = [
    "drain", "drained", "drainer", "stolen", "steal", "stole", "theft",
    "phishing", "phished", "scam", "scammer", "social engineering",
    "impersonat", "hacked", "hack", "heist", "exploit", "compromised",
    "rug pull", "lost", "siphon", "fraud", "attacker",
]

STOP_WORDS = [
    "price prediction", "market cap", "rally", "bull run", "bearish",
    "etf approval", "stock", "earnings", "forecast", "surge", "all-time high",
]

MAX_PER_FEED = 15


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (news collector)"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def strip_tags(text):
    return re.sub(r"<[^>]+>", "", text or "").strip()


def parse_feed(raw):
    """Достаёт записи и из RSS, и из Atom."""
    root = ElementTree.fromstring(raw)
    items = []

    for item in root.iter():
        tag = item.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue

        title = link = date = ""
        for child in item:
            ctag = child.tag.split("}")[-1]
            if ctag == "title":
                title = strip_tags(child.text)
            elif ctag == "link":
                link = (child.text or child.attrib.get("href", "")).strip()
            elif ctag in ("pubDate", "published", "updated"):
                date = (child.text or "").strip()
        if title and link:
            items.append({"title": title, "link": link, "date": date})
        if len(items) >= MAX_PER_FEED:
            break
    return items


def is_relevant(title):
    low = title.lower()
    if any(stop in low for stop in STOP_WORDS):
        return False
    has_crypto = any(w in low for w in CRYPTO_WORDS)
    has_theft = any(w in low for w in THEFT_WORDS)
    return has_crypto and has_theft


def main():
    if os.path.exists(DRAFTS_FILE):
        with open(DRAFTS_FILE, "r", encoding="utf-8") as f:
            drafts = json.load(f)
    else:
        drafts = []

    seen = {d["link"] for d in drafts}
    added = 0

    for source, url in FEEDS:
        try:
            raw = fetch(url)
            items = parse_feed(raw)
        except Exception as e:
            print(f"[{source}] не удалось получить: {e}")
            continue

        found = 0
        for it in items:
            if it["link"] in seen or not is_relevant(it["title"]):
                continue
            drafts.append({
                "source": source,
                "title": it["title"],
                "link": it["link"],
                "date": it["date"],
                "collected": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "used": False,
            })
            seen.add(it["link"])
            found += 1
            added += 1
        print(f"[{source}] подходящих новых: {found}")

    # Держим файл небольшим: только неиспользованные и последние 200
    drafts = [d for d in drafts if not d.get("used")][-200:]

    with open(DRAFTS_FILE, "w", encoding="utf-8") as f:
        json.dump(drafts, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"\nВсего добавлено: {added}. В файле кандидатов: {len(drafts)}")
    if added:
        print("Просмотри bot/drafts.json и перенеси интересное в bot/posts.json со своим текстом.")


if __name__ == "__main__":
    main()
