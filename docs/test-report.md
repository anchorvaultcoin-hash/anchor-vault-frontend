# AnchorVaultV45 — Test Report

**Date:** 2026-06-03
**Compiler:** solc 0.8.26, viaIR: true, optimizer 200 runs
**OpenZeppelin:** 5.6.1

## Unit Tests (Foundry)

| Test | Status | Gas |
|------|--------|-----|
| test_OpenVault_Valid | ✅ PASS | 324455 |
| test_OpenVault_InvalidAmount | ✅ PASS | 166967 |
| test_OpenVault_NoEmergency | ✅ PASS | 281764 |
| test_DepositToVault_Valid | ✅ PASS | 179049 |
| test_DepositToVault_InvalidAmount | ✅ PASS | 166719 |
| test_Withdraw_ValidSignature | ✅ PASS | 425438 |
| test_Withdraw_InvalidSignature | ✅ PASS | 340592 |
| test_Withdraw_ReplayBlocked | ✅ PASS | 447102 |
| test_TransferVault_Valid | ✅ PASS | 523418 |
| test_TransferVault_InvalidRecipient | ✅ PASS | 355182 |
| test_EarlyClose_Valid | ✅ PASS | 378633 |
| test_RecoverToSafe_Valid | ✅ PASS | 342381 |
| test_EmergencyWithdraw_Valid | ✅ PASS | 301085 |
| test_PanicWithdraw_Valid | ✅ PASS | 199040 |
| test_RotateAuthKeys_Valid | ✅ PASS | 481310 |
| test_SetTimelock_Valid | ✅ PASS | 369264 |

## Invariant Tests

| Test | Status | Runs |
|------|--------|------|
| invariant_Solvency | ✅ PASS | 256 |

## Tokenomics (non-ANCR 50/50)

| Test | Status | Gas |
|------|--------|-----|
| test_AccrueFees_NonANCR_50_50 | ✅ PASS | 76842 |

**Total:** 17 tests passed.
**All green. No failures.**
