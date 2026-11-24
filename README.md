# AnchorVaultCoin-UTXO — настольный пульт 1.3.1 (Linux) · 1.3.0 (Windows, macOS)

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
| **Ubuntu / Debian** | [anchorvaultcoin-utxo_1.3.1_amd64.deb](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/anchorvaultcoin-utxo_1.3.1_amd64.deb) | 66 МБ |
| **Другой Linux** | [AnchorVaultCoin-UTXO-1.3.1.AppImage](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.1.AppImage) | 97 МБ |

Какой у Mac процессор: меню  → «Об этом Mac» → строка «Чип» или «Процессор» (Apple M… — первый файл, Intel — второй).

Контрольные суммы: [SHA256SUMS](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS),
подпись Creator: [SHA256SUMS.sig](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS.sig).

## Подлинность: ключ выпуска

Список SHA256SUMS подписан ключом выпуска Creator (Ed25519). Открытый ключ:

```
f881f543afc1644374f15460045400ca9ce9fb3f58861c6ad0212449295b4782
```

Тот же ключ — на [anchorvaultcoin.com](https://anchorvaultcoin.com), в
[docs/RELEASE_PUBKEY.txt](https://github.com/anchorvaultcoin-hash/anchorvaultcoin-utxo/blob/main/docs/RELEASE_PUBKEY.txt)
и в официальных каналах проекта. Сверьте хотя бы в двух местах. Проверка скачанных файлов
(в отдельной пустой папке): `node scripts/release_verify.js --dir <папка>` из репозитория
[anchorvaultcoin-utxo](https://github.com/anchorvaultcoin-hash/anchorvaultcoin-utxo).

## Обновление по кнопке (Linux .deb, с версии 1.3.1)

Приложение раз в 6 часов проверяет подписанный список выпуска. Если подпись верна и версия новее —
предлагает «Обновить»: скачивает файл, сверяет SHA-256 из подписанного списка, ставит через системный
apt (пароль спрашивает окно системы) и перезапускается. Без подписи Creator, с подменённым файлом или
со старой версией обновление не предлагается и не ставится. Ключи и фразы не затрагиваются.
Версию 1.3.1 один раз нужно поставить вручную: в 1.3.0 кнопки нет. Windows и macOS — следующим шагом.

## Установка

Платной подписи Microsoft и Apple у проекта пока нет — при первом запуске система предупредит. Это ожидаемо.

**Windows.** Установщик `.exe` — запустить и пройти шаги. Или переносная версия `.zip` — правый щелчок →
«Извлечь всё» → в распакованной папке запустить **AnchorVaultCoin-UTXO.exe**. Если появится «Windows защитила ваш
компьютер» — «Подробнее» → «Выполнить в любом случае». Ключи хранятся там же, где у версии 1.1.0:
если она стоит, новая её ключи увидит.

**Ubuntu / Debian.** `sudo apt install ./anchorvaultcoin-utxo_1.3.1_amd64.deb`, затем запуск из меню
приложений. Нужна связка ключей: `sudo apt install gnome-keyring libsecret-1-0`.

**Другой Linux.** `chmod +x AnchorVaultCoin-UTXO-1.3.1.AppImage` и запустить.

**macOS.** Открыть `.dmg`, перетащить AnchorVaultCoin-UTXO в «Программы». Первый запуск: если macOS
пишет «не удаётся проверить разработчика» — Системные настройки → Конфиденциальность и безопасность →
«Всё равно открыть».
