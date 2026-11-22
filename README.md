# AnchorVaultCoin-UTXO — настольный пульт 1.3.0

Пульт сейфов AnchorVaultCoin для компьютера: контракт Ethereum (сейфы, аварийные операции,
передача сейфов), кошелёк BTC/LTC по своей фразе и сейфы Bitcoin / Litecoin кнопками.
Переключатель 🌐 Основная сеть / 🧪 Тренировка (тестовые сети) — в шапке.

## Скачать — под свою систему

| Система | Файл | Размер |
|---|---|---|
| **Windows 10/11** (x64) — установщик | [AnchorVaultCoin-UTXO-1.3.0-win-x64.exe](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.0-win-x64.exe) | 70 МБ |
| **Windows 10/11** (x64) — без установки | [AnchorVaultCoin-UTXO-1.3.0-win-x64.zip](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.0-win-x64.zip) | 97 МБ |
| **macOS, процессор Apple** (M1–M4) | [AnchorVaultCoin-UTXO-1.3.0-mac-arm64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.0-mac-arm64.dmg) | 86 МБ |
| **macOS, процессор Intel** | [AnchorVaultCoin-UTXO-1.3.0-mac-x64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.0-mac-x64.dmg) | 93 МБ |
| **Ubuntu / Debian** | [anchorvaultcoin-utxo_1.3.0_amd64.deb](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/anchorvaultcoin-utxo_1.3.0_amd64.deb) | 66 МБ |
| **Другой Linux** | [AnchorVaultCoin-UTXO-1.3.0.AppImage](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.0.AppImage) | 97 МБ |

Какой у Mac процессор: меню  → «Об этом Mac» → строка «Чип» или «Процессор» (Apple M… — первый файл, Intel — второй).

Контрольные суммы: [SHA256SUMS](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS).

## Установка

Платной подписи Microsoft и Apple у проекта пока нет — при первом запуске система предупредит. Это ожидаемо.

**Windows.** Установщик `.exe` — запустить и пройти шаги. Или переносная версия `.zip` — правый щелчок →
«Извлечь всё» → в распакованной папке запустить **AnchorVaultCoin-UTXO.exe**. Если появится «Windows защитила ваш
компьютер» — «Подробнее» → «Выполнить в любом случае». Ключи хранятся там же, где у версии 1.1.0:
если она стоит, новая её ключи увидит.

**Ubuntu / Debian.** `sudo apt install ./anchorvaultcoin-utxo_1.3.0_amd64.deb`, затем запуск из меню
приложений. Нужна связка ключей: `sudo apt install gnome-keyring libsecret-1-0`.

**Другой Linux.** `chmod +x AnchorVaultCoin-UTXO-1.3.0.AppImage` и запустить.

**macOS.** Открыть `.dmg`, перетащить AnchorVaultCoin-UTXO в «Программы». Первый запуск: если macOS
пишет «не удаётся проверить разработчика» — Системные настройки → Конфиденциальность и безопасность →
«Всё равно открыть».
