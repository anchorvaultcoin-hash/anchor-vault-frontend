# AnchorVaultCoin-UTXO — настольный пульт, тестовая сборка 1.1.0

Пульт сейфов AnchorVaultCoin для компьютера: ETH-контракт (сейфы, аварийные
операции, передача сейфов) и UTXO-сейфы BTC/LTC. Собрано на GitHub из исходника
`129c09a` (17.11.2026).

> **Тестовая сборка.** Пульт работает с контрактом в **основной сети Ethereum**:
> каждая операция — настоящий газ и настоящие токены. Для показа берите
> минимальные суммы. Аварийный вывод — штраф 15 %, паника — 20 %, передача
> сейфа — 0,5 %.

## Скачать — под свою систему

| Система | Файл | Размер |
|---|---|---|
| **Windows 10/11** (x64) | [AnchorVaultCoin-UTXO-1.1.0-win-x64.exe](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.1.0-win-x64.exe) | 73 МБ |
| **macOS, процессор Apple** (M1, M2, M3, M4) | [AnchorVaultCoin-UTXO-1.1.0-mac-arm64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.1.0-mac-arm64.dmg) | 90 МБ |
| **macOS, процессор Intel** | [AnchorVaultCoin-UTXO-1.1.0-mac-x64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.1.0-mac-x64.dmg) | 97 МБ |
| **Ubuntu / Debian** | [anchorvaultcoin-utxo_1.1.0_amd64.deb](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/anchorvaultcoin-utxo_1.1.0_amd64.deb) | 69 МБ |
| **Другой Linux** | [AnchorVaultCoin-UTXO-1.1.0.AppImage](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.1.0.AppImage) | 101 МБ |

Какой у Mac процессор: меню  → «Об этом Mac» → строка «Процессор» или «Чип»
(Apple M… — первый файл, Intel — второй).

Контрольные суммы: [SHA256SUMS](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS).

## Установка

Платной подписи Microsoft и Apple у проекта пока нет, поэтому система при
первом запуске предупредит. Это ожидаемо.

**Windows.** Запустить `.exe`. Если появится «Windows защитила ваш компьютер»
— «Подробнее» → «Выполнить в любом случае». Дальше — как обычный установщик.

**macOS.** Открыть `.dmg`, перетащить AnchorVaultCoin-UTXO в «Программы».
Первый запуск: если macOS пишет «не удаётся проверить разработчика» —
**Системные настройки → Конфиденциальность и безопасность**, внизу кнопка
«Всё равно открыть». (На macOS 14 и старше можно: правый щелчок по программе →
«Открыть» → «Открыть».)

**Ubuntu / Debian.**
```bash
sudo apt install ./anchorvaultcoin-utxo_1.1.0_amd64.deb
```

**Другой Linux.**
```bash
chmod +x AnchorVaultCoin-UTXO-1.1.0.AppImage && ./AnchorVaultCoin-UTXO-1.1.0.AppImage
```

## Первый запуск

1. Значок 🔑 в шапке → вкладка **Ethereum**. Нужны три ключа, по очереди:
   **Кошелёк владельца** (с него уходят транзакции — на нём нужен ETH на газ и
   токены), **Рабочий ключ**, **Запасной ключ**. Рабочий и запасной обязаны
   отличаться от кошелька владельца — так устроена защита контракта.
2. Каждая секретная фраза показывается **один раз** в отдельном защищённом окне.
   Записать на бумаге, затем приложение попросит ввести три слова по номерам.
   Неверное слово подсвечивается красным.
3. Уже есть фраза — «Восстановить по фразе», ввод тоже в защищённом окне.
4. Кнопка 🛡 в шапке — свой **код защиты** (как anti-phishing code на Binance):
   он показывается в каждом окне подтверждения настоящего пульта.
5. Каждую подпись и транзакцию приложение показывает в своём окне
   подтверждения — с расшифровкой: что за операция, куда, сколько.

UTXO-сейфы BTC и LTC — в списке токенов в шапке (раздел «UTXO-сейфы»).
