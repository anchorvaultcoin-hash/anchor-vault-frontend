"""
Публикует следующий пост из очереди bot/posts.json в Telegram-канал.
Ничего не сочиняет сам — только берёт готовый текст и отправляет.

Поддерживает трёхъязычные посты: если у поста есть поля ru/en/zh,
они склеиваются в одно сообщение через разделитель. Если есть только
поле text — отправляется как есть (старый формат, обратная совместимость).

Когда очередь заканчивается, все посты помечаются непрочитанными заново,
и цикл начинается с начала. Канал не замолкает никогда.

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
SEPARATOR = "\n\n— — —\n\n"
TELEGRAM_LIMIT = 4096


def build_text(post):
    """Собирает сообщение из языковых версий поста."""
    if post.get("text"):
        return post["text"]

    parts = [post[lang] for lang in ("ru", "en", "zh") if post.get(lang)]
    if not parts:
        return ""

    text = SEPARATOR.join(parts)
    if len(text) > TELEGRAM_LIMIT:
        print(f"ВНИМАНИЕ: пост id={post.get('id')} длиннее лимита, отправляю только ru.")
        text = post.get("ru", parts[0])
    return text


def save(posts):
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT")
    if not token or not chat:
        print("Нет TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT в secrets — проверь настройки репозитория.")
        sys.exit(1)

    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        posts = json.load(f)

    if not posts:
        print("Файл posts.json пуст — добавь посты.")
        return

    next_post = next((p for p in posts if not p.get("posted")), None)

    if next_post is None:
        print("Очередь пройдена до конца, начинаю цикл заново.")
        for p in posts:
            p["posted"] = False
        next_post = posts[0]

    text = build_text(next_post)
    if not text:
        print(f"У поста id={next_post.get('id')} нет текста — пропускаю и помечаю выполненным.")
        next_post["posted"] = True
        save(posts)
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat,
        "text": text,
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
    save(posts)

    left = sum(1 for p in posts if not p.get("posted"))
    print(f"Опубликован пост id={next_post['id']}. Осталось в очереди: {left}")


if __name__ == "__main__":
    main()
