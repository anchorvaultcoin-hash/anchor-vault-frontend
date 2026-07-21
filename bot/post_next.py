"""
Публикует следующий пост из очереди bot/posts.json в Telegram-канал.
Ничего не сочиняет сам — только берёт готовый текст и отправляет.

Нужны переменные окружения (задаются как GitHub Secrets):
  TELEGRAM_BOT_TOKEN — токен от @BotFather
  TELEGRAM_CHAT      — юзернейм канала вида "@anchorvaultcoin" (или числовой chat_id)
"""

import json
import os
import sys
import urllib.request
import urllib.parse

POSTS_FILE = os.path.join(os.path.dirname(__file__), "posts.json")


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT")

    if not token or not chat:
        print("Нет TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT в secrets — проверь настройки репозитория.")
        sys.exit(1)

    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        posts = json.load(f)

    next_post = next((p for p in posts if not p.get("posted")), None)

    if next_post is None:
        print("Очередь пуста — постить нечего. Добавь новые посты в bot/posts.json.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat,
        "text": next_post["text"],
        "disable_web_page_preview": "true",
    }).encode()

    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = resp.read().decode()
            print("Ответ Telegram:", result)
    except Exception as e:
        print("Ошибка отправки в Telegram:", e)
        sys.exit(1)

    next_post["posted"] = True
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Опубликован пост id={next_post['id']}")


if __name__ == "__main__":
    main()
