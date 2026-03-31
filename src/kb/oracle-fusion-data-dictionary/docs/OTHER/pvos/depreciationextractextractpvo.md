---
id: DOC-OTHER-PVO-DepreciationExtractExtractPVO
doc_type: system-doc
title: "DepreciationExtractExtractPVO — PVO Cross-Module"
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
  - DepreciationExtractExtractPVO
  - depreciationextractextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationExtractExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Extract Extract. Acessa as tabelas: FA_DEPRN_EXTRACT.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DepreciationExtractExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 1 | 1 | 73 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deprn_extract|FA_DEPRN_EXTRACT]] — 73 atributos (1 PKs, 73 BICC)

---

## ⚙️ Atributos

### [[fa_deprn_extract|FA_DEPRN_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaDeprnExtractAHTransactionHeaderId | AH_TRANSACTION_HEADER_ID | — | ✅ |
| 2 | FaDeprnExtractAccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 3 | FaDeprnExtractAcceleratedAdjustedCost | ACCELERATED_ADJUSTED_COST | — | ✅ |
| 4 | FaDeprnExtractAcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 5 | FaDeprnExtractAcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 6 | FaDeprnExtractAcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 7 | FaDeprnExtractAdjustedCost | ADJUSTED_COST | — | ✅ |
| 8 | FaDeprnExtractAssetId | ASSET_ID | — | ✅ |
| 9 | FaDeprnExtractAssetType | ASSET_TYPE | — | ✅ |
| 10 | FaDeprnExtractBonusAdjustedCost | BONUS_ADJUSTED_COST | — | ✅ |
| 11 | FaDeprnExtractBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 12 | FaDeprnExtractBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 13 | FaDeprnExtractBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 14 | FaDeprnExtractBonusRuleId | BONUS_RULE_ID | — | ✅ |
| 15 | FaDeprnExtractBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 16 | FaDeprnExtractBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 17 | FaDeprnExtractBooksTransactionHeaderId | BOOKS_TRANSACTION_HEADER_ID | — | ✅ |
| 18 | FaDeprnExtractCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 19 | FaDeprnExtractCategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | — | ✅ |
| 20 | FaDeprnExtractCategoryId | CATEGORY_ID | — | ✅ |
| 21 | FaDeprnExtractCeilingTypeId | CEILING_TYPE_ID | — | ✅ |
| 22 | FaDeprnExtractCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 23 | FaDeprnExtractConventionTypeId | CONVENTION_TYPE_ID | — | ✅ |
| 24 | FaDeprnExtractCost | COST | — | ✅ |
| 25 | FaDeprnExtractCreatedBy | CREATED_BY | — | ✅ |
| 26 | FaDeprnExtractCreationDate | CREATION_DATE | — | ✅ |
| 27 | FaDeprnExtractCurrencyCode | CURRENCY_CODE | — | ✅ |
| 28 | FaDeprnExtractDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 29 | FaDeprnExtractDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 30 | FaDeprnExtractDeprnExtractId | DEPRN_EXTRACT_ID | 🔑 | ✅ |
| 31 | FaDeprnExtractDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 32 | FaDeprnExtractDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 33 | FaDeprnExtractDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 34 | FaDeprnExtractDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 35 | FaDeprnExtractDistributionId | DISTRIBUTION_ID | — | ✅ |
| 36 | FaDeprnExtractEmployeeId | EMPLOYEE_ID | — | ✅ |
| 37 | FaDeprnExtractFlatRateId | FLAT_RATE_ID | — | ✅ |
| 38 | FaDeprnExtractGeneralFund | GENERAL_FUND | — | ✅ |
| 39 | FaDeprnExtractGroupAssetId | GROUP_ASSET_ID | — | ✅ |
| 40 | FaDeprnExtractImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 41 | FaDeprnExtractImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 42 | FaDeprnExtractLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | FaDeprnExtractLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 44 | FaDeprnExtractLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 45 | FaDeprnExtractLatestFlag | LATEST_FLAG | — | ✅ |
| 46 | FaDeprnExtractLedgerId | LEDGER_ID | — | ✅ |
| 47 | FaDeprnExtractLedgerSetId | LEDGER_SET_ID | — | ✅ |
| 48 | FaDeprnExtractLocationId | LOCATION_ID | — | ✅ |
| 49 | FaDeprnExtractLtdProduction | LTD_PRODUCTION | — | ✅ |
| 50 | FaDeprnExtractMethodId | METHOD_ID | — | ✅ |
| 51 | FaDeprnExtractNetBookValue | NET_BOOK_VALUE | — | ✅ |
| 52 | FaDeprnExtractOriginalCost | ORIGINAL_COST | — | ✅ |
| 53 | FaDeprnExtractPeriodCounter | PERIOD_COUNTER | — | ✅ |
| 54 | FaDeprnExtractPeriodName | PERIOD_NAME | — | ✅ |
| 55 | FaDeprnExtractProduction | PRODUCTION | — | ✅ |
| 56 | FaDeprnExtractRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 57 | FaDeprnExtractRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 58 | FaDeprnExtractRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 59 | FaDeprnExtractRevalReserve | REVAL_RESERVE | — | ✅ |
| 60 | FaDeprnExtractSalvageValue | SALVAGE_VALUE | — | ✅ |
| 61 | FaDeprnExtractSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 62 | FaDeprnExtractSourceTable | SOURCE_TABLE | — | ✅ |
| 63 | FaDeprnExtractTotalAccDeprnReserve | TOTAL_ACC_DEPRN_RESERVE | — | ✅ |
| 64 | FaDeprnExtractTotalBonusDeprnReserve | TOTAL_BONUS_DEPRN_RESERVE | — | ✅ |
| 65 | FaDeprnExtractTotalDeprnReserve | TOTAL_DEPRN_RESERVE | — | ✅ |
| 66 | FaDeprnExtractTotalUnits | TOTAL_UNITS | — | ✅ |
| 67 | FaDeprnExtractTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |
| 68 | FaDeprnExtractUnitRatio | UNIT_RATIO | — | ✅ |
| 69 | FaDeprnExtractUnitsAssigned | UNITS_ASSIGNED | — | ✅ |
| 70 | FaDeprnExtractYtdDeprn | YTD_DEPRN | — | ✅ |
| 71 | FaDeprnExtractYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 72 | FaDeprnExtractYtdProduction | YTD_PRODUCTION | — | ✅ |
| 73 | FaDeprnExtractYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
