---
id: DOC-OTHER-PVO-DepreciationExtractPVO
doc_type: system-doc
title: "DepreciationExtractPVO — PVO Cross-Module"
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
  - DepreciationExtractPVO
  - depreciationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Extract. Acessa as tabelas: FA_BOOK_CONTROLS, FA_DEPRN_EXTRACT, GL_LEDGERS (+1).

**Caminho:** `FscmTopModelAM.FinFaDeprDepreciationAM.DepreciationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 90 | 4 | 1 | 43 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[fa_book_controls|FA_BOOK_CONTROLS]] — 4 atributos
- [[fa_deprn_extract|FA_DEPRN_EXTRACT]] — 75 atributos (1 PKs, 43 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 8 atributos

---

## ⚙️ Atributos

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlPEOBookControlId | BOOK_CONTROL_ID | — | — |
| 2 | BookControlPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | BookControlPEOBookTypeName | BOOK_TYPE_NAME | — | — |
| 4 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[fa_deprn_extract|FA_DEPRN_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AHTransactionHeaderId | AH_TRANSACTION_HEADER_ID | — | — |
| 2 | AccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 3 | AcceleratedAdjustedCost | ACCELERATED_ADJUSTED_COST | — | ✅ |
| 4 | AcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 5 | AcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 6 | AcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 7 | AdjustedCost | ADJUSTED_COST | — | ✅ |
| 8 | AssetId | ASSET_ID | — | ✅ |
| 9 | AssetType | ASSET_TYPE | — | — |
| 10 | BonusAdjustedCost | BONUS_ADJUSTED_COST | — | ✅ |
| 11 | BonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 12 | BonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 13 | BonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 14 | BonusRuleId | BONUS_RULE_ID | — | — |
| 15 | BonusYtdDeprn | BONUS_YTD_DEPRN | — | — |
| 16 | BookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 17 | BooksTransactionHeaderId | BOOKS_TRANSACTION_HEADER_ID | — | — |
| 18 | CapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 19 | CategoryBookDefaultId | CATEGORY_BOOK_DEFAULT_ID | — | — |
| 20 | CategoryId | CATEGORY_ID | — | — |
| 21 | CeilingTypeId | CEILING_TYPE_ID | — | — |
| 22 | CodeCombinationId | CODE_COMBINATION_ID | — | — |
| 23 | ConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 24 | Cost | COST | — | ✅ |
| 25 | CreatedBy | CREATED_BY | — | — |
| 26 | CreationDate | CREATION_DATE | — | — |
| 27 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 28 | DeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 29 | DeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 30 | DeprnExtractId | DEPRN_EXTRACT_ID | 🔑 | ✅ |
| 31 | DeprnReserve | DEPRN_RESERVE | — | — |
| 32 | DeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 33 | DeprnRunId | DEPRN_RUN_ID | — | — |
| 34 | DeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 35 | DistributionId | DISTRIBUTION_ID | — | ✅ |
| 36 | EmployeeId | EMPLOYEE_ID | — | — |
| 37 | FlatRateId | FLAT_RATE_ID | — | — |
| 38 | GeneralFund | GENERAL_FUND | — | ✅ |
| 39 | GroupAssetId | GROUP_ASSET_ID | — | — |
| 40 | ImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 41 | ImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 42 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | LatestFlag | LATEST_FLAG | — | — |
| 46 | LedgerId | LEDGER_ID | — | — |
| 47 | LedgerSetId | LEDGER_SET_ID | — | — |
| 48 | LocationId | LOCATION_ID | — | — |
| 49 | LtdProduction | LTD_PRODUCTION | — | ✅ |
| 50 | MethodId | METHOD_ID | — | — |
| 51 | NetBookValue | NET_BOOK_VALUE | — | ✅ |
| 52 | OriginalCost | ORIGINAL_COST | — | ✅ |
| 53 | PeriodCounter | PERIOD_COUNTER | — | ✅ |
| 54 | PeriodName | PERIOD_NAME | — | ✅ |
| 55 | Production | PRODUCTION | — | ✅ |
| 56 | RecoverableCost | RECOVERABLE_COST | — | ✅ |
| 57 | RevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 58 | RevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 59 | RevalReserve | REVAL_RESERVE | — | ✅ |
| 60 | SalvageValue | SALVAGE_VALUE | — | ✅ |
| 61 | SourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 62 | SourceTable | SOURCE_TABLE | — | — |
| 63 | TotalAccDeprnReserve | TOTAL_ACC_DEPRN_RESERVE | — | — |
| 64 | TotalBonusDeprnReserve | TOTAL_BONUS_DEPRN_RESERVE | — | ✅ |
| 65 | TotalDeprnReserve | TOTAL_DEPRN_RESERVE | — | ✅ |
| 66 | TotalUnits | TOTAL_UNITS | — | — |
| 67 | TransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 68 | UnitRatio | UNIT_RATIO | — | — |
| 69 | UnitsAssigned | UNITS_ASSIGNED | — | — |
| 70 | YtdBonusDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 71 | YtdDeprn | YTD_DEPRN | — | ✅ |
| 72 | YtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 73 | YtdLatestFlag | YTD_LATEST_FLAG | — | — |
| 74 | YtdProduction | YTD_PRODUCTION | — | ✅ |
| 75 | YtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerId1 | LEDGER_ID | — | — |
| 2 | LedgerPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentName | ASSIGNMENT_NAME | — | — |
| 3 | AssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 6 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | LocationId1 | LOCATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
