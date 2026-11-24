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

### SHA-256 каждого файла

| Файл | SHA-256 |
|---|---|
| AnchorVaultCoin-UTXO-1.3.0-win-x64.exe | `5d95365090e421392ff0c97f2b2b2800e39d50a1b7dadbf46ade07918836ad86` |
| AnchorVaultCoin-UTXO-1.3.0-win-x64.zip | `0d8a8c6510c0d45c06da8df65f649cba3bf4b98a41d9356151d85c1aac35e88c` |
| AnchorVaultCoin-UTXO-1.3.0-mac-arm64.dmg | `384b993783d42f2353e6b1aada951c8110f05b62294bfafce2177b0859d86859` |
| AnchorVaultCoin-UTXO-1.3.0-mac-x64.dmg | `aa34a9799a7e0a3d848c0cdafcee9cb8f2b7f48a78f59bdd14704ec6c28628c0` |
| AnchorVaultCoin-UTXO-1.3.1.AppImage | `86137c9f6633566670b73985eff44dfcfbf1ad41a7f0074c9abf2ad8bd914a84` |
| anchorvaultcoin-utxo_1.3.1_amd64.deb | `fdc94ba16075fc14433b20fe5e7bad22ef03c6cdd578d0b832cd3ef778cf7d1e` |

Те же суммы — в подписанном списке SHA256SUMS. Проверка в Linux/macOS: `sha256sum <файл>`, в Windows: `certutil -hashfile <файл> SHA256`.

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
