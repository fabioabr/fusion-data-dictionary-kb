---
id: DOC-OTHER-PVO-TrxExtractExtractPVO
doc_type: system-doc
title: "TrxExtractExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TrxExtractExtractPVO
  - trxextractextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TrxExtractExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Trx Extract Extract. Acessa as tabelas: FA_TRX_EXTRACT.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.TrxExtractExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_trx_extract|FA_TRX_EXTRACT]] — 64 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[fa_trx_extract|FA_TRX_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtractAHTransactionHeaderId | AH_TRANSACTION_HEADER_ID | — | ✅ |
| 2 | TrxExtractAdjustmentLineId | ADJUSTMENT_LINE_ID | — | ✅ |
| 3 | TrxExtractAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 4 | TrxExtractAssetId | ASSET_ID | — | ✅ |
| 5 | TrxExtractAssetType | ASSET_TYPE | — | ✅ |
| 6 | TrxExtractBonusExpense | BONUS_EXPENSE | — | ✅ |
| 7 | TrxExtractBonusReserve | BONUS_RESERVE | — | ✅ |
| 8 | TrxExtractBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 9 | TrxExtractBooksTransactionHeaderId | BOOKS_TRANSACTION_HEADER_ID | — | ✅ |
| 10 | TrxExtractCapitalizationFlag | CAPITALIZATION_FLAG | — | ✅ |
| 11 | TrxExtractCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | — | ✅ |
| 12 | TrxExtractCategoryId | CATEGORY_ID | — | ✅ |
| 13 | TrxExtractCipCost | CIP_COST | — | ✅ |
| 14 | TrxExtractCipCostClearing | CIP_COST_CLEARING | — | ✅ |
| 15 | TrxExtractCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 16 | TrxExtractCost | COST | — | ✅ |
| 17 | TrxExtractCostClearing | COST_CLEARING | — | ✅ |
| 18 | TrxExtractCostOfRemoval | COST_OF_REMOVAL | — | ✅ |
| 19 | TrxExtractCreatedBy | CREATED_BY | — | ✅ |
| 20 | TrxExtractCreationDate | CREATION_DATE | — | ✅ |
| 21 | TrxExtractCurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | TrxExtractDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 23 | TrxExtractDistributionId | DISTRIBUTION_ID | — | ✅ |
| 24 | TrxExtractEmployeeId | EMPLOYEE_ID | — | ✅ |
| 25 | TrxExtractExpense | EXPENSE | — | ✅ |
| 26 | TrxExtractImpairmentExpense | IMPAIRMENT_EXPENSE | — | ✅ |
| 27 | TrxExtractImpairmentId | IMPAIRMENT_ID | — | ✅ |
| 28 | TrxExtractImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 29 | TrxExtractInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | ✅ |
| 30 | TrxExtractInvoiceTransactionType | INVOICE_TRANSACTION_TYPE | — | ✅ |
| 31 | TrxExtractLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | TrxExtractLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | TrxExtractLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | TrxExtractLedgerId | LEDGER_ID | — | ✅ |
| 35 | TrxExtractLedgerSetId | LEDGER_SET_ID | — | ✅ |
| 36 | TrxExtractLocationId | LOCATION_ID | — | ✅ |
| 37 | TrxExtractMassTransactionId | MASS_TRANSACTION_ID | — | ✅ |
| 38 | TrxExtractNbvRetired | NBV_RETIRED | — | ✅ |
| 39 | TrxExtractNewBooksTrxIdIn | NEW_BOOKS_TRX_ID_IN | — | ✅ |
| 40 | TrxExtractOldBooksTrxIdIn | OLD_BOOKS_TRX_ID_IN | — | ✅ |
| 41 | TrxExtractOriginalCost | ORIGINAL_COST | — | ✅ |
| 42 | TrxExtractPeriodCounter | PERIOD_COUNTER | — | ✅ |
| 43 | TrxExtractPeriodName | PERIOD_NAME | — | ✅ |
| 44 | TrxExtractProceedsOfSale | PROCEEDS_OF_SALE | — | ✅ |
| 45 | TrxExtractRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 46 | TrxExtractReserve | RESERVE | — | ✅ |
| 47 | TrxExtractRetirementId | RETIREMENT_ID | — | ✅ |
| 48 | TrxExtractRetirementTrxId | RETIREMENT_TRX_ID | — | ✅ |
| 49 | TrxExtractRevalReserve | REVAL_RESERVE | — | ✅ |
| 50 | TrxExtractSalvageValue | SALVAGE_VALUE | — | ✅ |
| 51 | TrxExtractSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 52 | TrxExtractSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 53 | TrxExtractSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 54 | TrxExtractSourceTable | SOURCE_TABLE | — | ✅ |
| 55 | TrxExtractSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 56 | TrxExtractTotalUnits | TOTAL_UNITS | — | ✅ |
| 57 | TrxExtractTrackMemberFlag | TRACK_MEMBER_FLAG | — | ✅ |
| 58 | TrxExtractTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |
| 59 | TrxExtractTransactionKey | TRANSACTION_KEY | — | ✅ |
| 60 | TrxExtractTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 61 | TrxExtractTrxExtractId | TRX_EXTRACT_ID | 🔑 | ✅ |
| 62 | TrxExtractUnitRatio | UNIT_RATIO | — | ✅ |
| 63 | TrxExtractUnitsAssigned | UNITS_ASSIGNED | — | ✅ |
| 64 | TrxExtractUnplannedTrxId | UNPLANNED_TRX_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
