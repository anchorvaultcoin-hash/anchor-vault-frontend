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
TELEGRAM_LIMIT = 4096


def esc(text):
    """Экранирует символы, ломающие HTML-разметку Telegram."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_text(post):
    """Собирает сообщение: русский открыто, переводы под сворачиваемыми блоками."""
    if post.get("text"):
        return esc(post["text"]), False

    ru = post.get("ru", "")
    if not ru:
        parts = [post[l] for l in ("en", "zh") if post.get(l)]
        return (esc(parts[0]) if parts else ""), False

    emoji = post.get("emoji", "\U0001F510")

    # Эмодзи приклеиваем к заголовку — это первая строка текста
    lines = ru.split("\n")
    lines[0] = f"{emoji} {lines[0]}"
    body = esc("\n".join(lines))

    blocks = [f"<b>{esc(lines[0])}</b>" + body[len(esc(lines[0])):]]

    if post.get("en"):
        blocks.append(
            "<blockquote expandable>\U0001F1EC\U0001F1E7 <b>English</b>\n\n"
            + esc(post["en"]) + "</blockquote>"
        )
    if post.get("zh"):
        blocks.append(
            "<blockquote expandable>\U0001F1E8\U0001F1F3 <b>\u4e2d\u6587</b>\n\n"
            + esc(post["zh"]) + "</blockquote>"
        )

    text = "\n\n".join(blocks)
    if len(text) > TELEGRAM_LIMIT:
        print(f"ВНИМАНИЕ: пост id={post.get('id')} длиннее лимита, отправляю только ru.")
        text = body
    return text, True


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

    text, use_html = build_text(next_post)
    if not text:
        print(f"У поста id={next_post.get('id')} нет текста — пропускаю и помечаю выполненным.")
        next_post["posted"] = True
        save(posts)
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat,
        "text": text,
        "disable_web_page_preview": "true",
    }
    if use_html:
        payload["parse_mode"] = "HTML"
    data = urllib.parse.urlencode(payload).encode()
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
