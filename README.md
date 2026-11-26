# AnchorVaultCoin-UTXO — настольный пульт 1.3.2 · Android 1.1.0

Пульт сейфов AnchorVaultCoin для компьютера: контракт Ethereum (сейфы, аварийные операции,
передача сейфов), кошелёк BTC/LTC по своей фразе и сейфы Bitcoin / Litecoin кнопками.
Переключатель 🌐 Основная сеть / 🧪 Тренировка (тестовые сети) — в шапке.

## Скачать — под свою систему

| Система | Файл | Размер |
|---|---|---|
| **Windows 10/11** (x64) — установщик | [AnchorVaultCoin-UTXO-1.3.2-win-x64.exe](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.2-win-x64.exe) | 70 МБ |
| **Windows 10/11** (x64) — без установки | [AnchorVaultCoin-UTXO-1.3.2-win-x64.zip](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.2-win-x64.zip) | 96 МБ |
| **macOS, процессор Apple** (M1–M4) | [AnchorVaultCoin-UTXO-1.3.2-mac-arm64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.2-mac-arm64.dmg) | 86 МБ |
| **macOS, процессор Intel** | [AnchorVaultCoin-UTXO-1.3.2-mac-x64.dmg](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.2-mac-x64.dmg) | 93 МБ |
| **Ubuntu / Debian** | [anchorvaultcoin-utxo_1.3.2_amd64.deb](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/anchorvaultcoin-utxo_1.3.2_amd64.deb) | 66 МБ |
| **Другой Linux** | [AnchorVaultCoin-UTXO-1.3.2.AppImage](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-UTXO-1.3.2.AppImage) | 97 МБ |
| **Android** 5.1+ (телефон) | [AnchorVaultCoin-Android-1.1.0.apk](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/AnchorVaultCoin-Android-1.1.0.apk) | 12 МБ |

Какой у Mac процессор: меню  → «Об этом Mac» → строка «Чип» или «Процессор» (Apple M… — первый файл, Intel — второй).

Контрольные суммы: [SHA256SUMS](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS),
подпись Creator: [SHA256SUMS.sig](https://github.com/anchorvaultcoin-hash/anchor-vault-frontend/raw/desktop-downloads/SHA256SUMS.sig).

### SHA-256 каждого файла

| Файл | SHA-256 |
|---|---|
| AnchorVaultCoin-UTXO-1.3.2-win-x64.exe | `8c4bc3dbcf91ee679fb968d0c655672a6f65e1170f36eb64586dcb89e2aac950` |
| AnchorVaultCoin-UTXO-1.3.2-win-x64.zip | `e961621a36b29c5156903fffb6e59d49b524cb0ef8cea93cd6e3aa7fff792640` |
| AnchorVaultCoin-UTXO-1.3.2-mac-arm64.dmg | `a9bb364325de184419967cef54ac64ad1ca12038b2bbcb9979ca02375ca09696` |
| AnchorVaultCoin-UTXO-1.3.2-mac-x64.dmg | `8ca0ba0b0d7606e14f0f87fd359baa7f9084e03b6643eefd03d484acecaae702` |
| AnchorVaultCoin-UTXO-1.3.2.AppImage | `f6f54221dd65effcd55a776fe58fc89a0acf8ee23a1c511af13af3221635269f` |
| anchorvaultcoin-utxo_1.3.2_amd64.deb | `9f5d230cee10ac3d5b834c9955356a1d2f54da918bfbc28a29180c06cbbeea20` |
| AnchorVaultCoin-Android-1.1.0.apk | `871a2b60277e592c033b1765f0644ce071f1ecd4b06479dfa9ff97cde96f35ae` |

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

## Обновление по кнопке (с версии 1.3.2; Linux .deb — с 1.3.1; Android — с 1.1.0)

Приложение раз в 6 часов проверяет подписанный список выпуска. Если подпись Creator верна и версия
новее — в пульте появляется плашка «Доступна версия…» и уведомление системы. Нажали — окно
«Обновить / Позже». Можно и вручную: кнопка ⟳ «Проверить обновления» в шапке пульта.

После «Обновить» файл скачивается, сверяется по SHA-256 из подписанного списка и ставится:

- **Ubuntu / Debian (.deb)** — через системный apt, пароль спрашивает окно системы;
- **AppImage** — новый файл встаёт на место старого;
- **Windows, установщик «для себя»** — приложение закрывается, установщик обновляет его без вопросов и запускает снова;
- **macOS** — новая версия заменяет приложение в той же папке (если приложение не перемещено в «Программы» — подскажет);
- **Android** — системный установщик Android; он сам проверяет, что новая версия подписана тем же ключом.

Переносная версия Windows (.zip) и установка «для всех пользователей» обновляются вручную: приложение
сообщит о новой версии и откроет эту страницу. Без подписи Creator, с подменённым файлом или со старой
версией обновление не предлагается и не ставится. Ключи и фразы не затрагиваются.

**Один раз вручную:** у кого стоит Windows/macOS 1.3.0 или Android 1.0 — поставьте новую версию со
страницы (в старых версиях кнопки нет). Linux 1.3.1 обновится до 1.3.2 по кнопке сам.

## Установка

Платной подписи Microsoft и Apple у проекта пока нет — при первом запуске система предупредит. Это ожидаемо.

**Windows.** Установщик `.exe` — запустить и пройти шаги. Или переносная версия `.zip` — правый щелчок →
«Извлечь всё» → в распакованной папке запустить **AnchorVaultCoin-UTXO.exe**. Если появится «Windows защитила ваш
компьютер» — «Подробнее» → «Выполнить в любом случае». Ключи хранятся там же, где у версии 1.1.0:
если она стоит, новая её ключи увидит.

**Ubuntu / Debian.** `sudo apt install ./anchorvaultcoin-utxo_1.3.2_amd64.deb`, затем запуск из меню
приложений. Нужна связка ключей: `sudo apt install gnome-keyring libsecret-1-0`.

**Другой Linux.** `chmod +x AnchorVaultCoin-UTXO-1.3.2.AppImage` и запустить.

**Android.** Открыть скачанный `.apk` на телефоне; если Android спросит — разрешить установку из этого источника.

**macOS.** Открыть `.dmg`, перетащить AnchorVaultCoin-UTXO в «Программы». Первый запуск: если macOS
пишет «не удаётся проверить разработчика» — Системные настройки → Конфиденциальность и безопасность →
«Всё равно открыть».
