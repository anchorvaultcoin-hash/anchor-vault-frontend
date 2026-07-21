# AnchorVaultCoin

Non-custodial, multi-asset ERC-20 vault with dual-key EIP-712 authorization.

> Technical contract identifier: `AnchorVaultV45`. Product/brand name: **AnchorVaultCoin**.

## Status

| | |
|---|---|
| Network | Sepolia testnet (chainId `11155111`) |
| Contract | [`0x8E1F46fC913c4928303BbCEB92ccb7c54cD95BA4`](https://sepolia.etherscan.io/address/0x8E1F46fC913c4928303BbCEB92ccb7c54cD95BA4) |
| Mainnet | Not deployed |
| Security audit | In progress (independent, external) — mainnet is blocked until the final report |

This repository holds the **frontend and web interface only**. The Solidity contract source is maintained in a separate, private repository under a BUSL-1.1 license.

## What it is

AnchorVaultCoin is a non-custodial vault for ERC-20 assets. Instead of a single private key controlling everything, each vault is authorized by two separate EIP-712 keys:

- **mainAuthKey** — day-to-day operations (withdraw, transfer)
- **recoveryAuthKey** — a separate key used only for emergency recovery

Neither key has to match the vault owner's wallet address — losing or leaking one key alone does not mean losing the funds.

Other mechanics:
- **panicWithdraw** — unsigned emergency withdrawal path (20% fee, intentionally costly to discourage misuse)
- Standard withdrawal — 0.5% fee
- Multi-asset support, including fee-on-transfer and rebasing tokens
- A solvency invariant (`balance >= locked principal + fees + reserves`), checked via fuzz testing (10M+ calls, 0 violations)

## Applications

- **pulse.html** — browser-based dashboard for managing existing vaults (connect wallet, deposit/withdraw, view status). Does not generate keys.
- **Offline key generator** (`AnchorVaultCoin.apk`, `AnchorVaultCoin-Linux.deb`, `AnchorVaultCoin-Setup-Windows.exe`, `AnchorVaultCoin-Mac.dmg`) — native apps for generating wallet keys, one build per platform. Verify against `docs/CHECKSUMS.txt` before running. For sensitive roles, generate keys on an offline / air-gapped machine.

## Live links

- Site: https://anchorvaultcoin-hash.github.io/anchor-vault-frontend/
- Vault dashboard (pulse): https://anchorvaultcoin-hash.github.io/anchor-vault-frontend/pulse.html
- Telegram: https://t.me/AnchorVaultCoin
- X: https://x.com/Anchorvaultcoin
- Contract (Sepolia Etherscan): https://sepolia.etherscan.io/address/0x8E1F46fC913c4928303BbCEB92ccb7c54cD95BA4
- Custom domain: `anchorvault.site` (if already configured)

## Repository structure

```
docs/
  landing.html                        Main site
  pulse.html                          Browser vault dashboard (no key generation)
  AnchorVaultCoin.apk                 Offline key generator - Android
  AnchorVaultCoin-Linux.deb           Offline key generator - Linux
  AnchorVaultCoin-Setup-Windows.exe   Offline key generator - Windows
  AnchorVaultCoin-Mac.dmg             Offline key generator - macOS
  CHECKSUMS.txt                       Checksums for the four apps above
bot/                    Telegram announcement bot (posts a pre-written queue on schedule)
.github/workflows/      CI - runs the Telegram bot on schedule
LICENSE                 MIT (this repo - frontend/site code only)
```

## Tech stack

- HTML5 / CSS3 / JavaScript (ES6)
- ethers.js v6
- EIP-712 typed-data signing
- Python (Telegram automation in `bot/`)

## Local development

Static site, no build step required.

```bash
git clone https://github.com/anchorvaultcoin-hash/anchor-vault-frontend.git
cd anchor-vault-frontend/docs
python3 -m http.server 8000
# open http://localhost:8000/landing.html
```

## Telegram automation

`bot/post_next.py` publishes the next unpublished entry from `bot/posts.json` to the project's Telegram channel, on a GitHub Actions schedule (`.github/workflows/telegram-post.yml`). It does not generate content - every post is written in advance and reviewed before it's added to the queue.

## Security

This is pre-audit, testnet-only software. Do not send real funds. The contract has not been deployed to mainnet and will not be until an independent external audit is complete. When generating keys with the offline generator apps, verify checksums first and prefer an air-gapped machine.

## License

MIT - this repository (frontend/site).
The vault contract itself is BUSL-1.1 and lives in a separate, private repository.
