---
id: DOC-OTHER-PVO-ReportingDepreciationSummaryExtractPVO
doc_type: system-doc
title: "ReportingDepreciationSummaryExtractPVO — PVO Cross-Module"
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
  - ReportingDepreciationSummaryExtractPVO
  - reportingdepreciationsummaryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingDepreciationSummaryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Depreciation Summary Extract. Acessa as tabelas: FA_MC_DEPRN_SUMMARY.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingDepreciationSummaryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 4 | 57 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_deprn_summary|FA_MC_DEPRN_SUMMARY]] — 57 atributos (4 PKs, 57 BICC)

---

## ⚙️ Atributos

### [[fa_mc_deprn_summary|FA_MC_DEPRN_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingDepreciationSummaryAccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | ReportingDepreciationSummaryAcceleratedAdjustedCost | ACCELERATED_ADJUSTED_COST | — | ✅ |
| 3 | ReportingDepreciationSummaryAcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 4 | ReportingDepreciationSummaryAcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 5 | ReportingDepreciationSummaryAcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 6 | ReportingDepreciationSummaryAdjustedCost | ADJUSTED_COST | — | ✅ |
| 7 | ReportingDepreciationSummaryAssetId | ASSET_ID | 🔑 | ✅ |
| 8 | ReportingDepreciationSummaryBacklogDeprnReserve | BACKLOG_DEPRN_RESERVE | — | ✅ |
| 9 | ReportingDepreciationSummaryBonusAdjustedCost | BONUS_ADJUSTED_COST | — | ✅ |
| 10 | ReportingDepreciationSummaryBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 11 | ReportingDepreciationSummaryBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 12 | ReportingDepreciationSummaryBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 13 | ReportingDepreciationSummaryBonusRate | BONUS_RATE | — | ✅ |
| 14 | ReportingDepreciationSummaryBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 15 | ReportingDepreciationSummaryBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 16 | ReportingDepreciationSummaryCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 17 | ReportingDepreciationSummaryConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 18 | ReportingDepreciationSummaryCreatedBy | CREATED_BY | — | ✅ |
| 19 | ReportingDepreciationSummaryCreationDate | CREATION_DATE | — | ✅ |
| 20 | ReportingDepreciationSummaryDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 21 | ReportingDepreciationSummaryDeprnAdjustmentFactor | DEPRN_ADJUSTMENT_FACTOR | — | ✅ |
| 22 | ReportingDepreciationSummaryDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 23 | ReportingDepreciationSummaryDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 24 | ReportingDepreciationSummaryDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 25 | ReportingDepreciationSummaryDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 26 | ReportingDepreciationSummaryDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 27 | ReportingDepreciationSummaryDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 28 | ReportingDepreciationSummaryEventId | EVENT_ID | — | ✅ |
| 29 | ReportingDepreciationSummaryGeneralFund | GENERAL_FUND | — | ✅ |
| 30 | ReportingDepreciationSummaryImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 31 | ReportingDepreciationSummaryImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 32 | ReportingDepreciationSummaryImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 33 | ReportingDepreciationSummaryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ReportingDepreciationSummaryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | ReportingDepreciationSummaryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | ReportingDepreciationSummaryLtdProduction | LTD_PRODUCTION | — | ✅ |
| 37 | ReportingDepreciationSummaryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 38 | ReportingDepreciationSummaryPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 39 | ReportingDepreciationSummaryPriorFyBonusExpense | PRIOR_FY_BONUS_EXPENSE | — | ✅ |
| 40 | ReportingDepreciationSummaryPriorFyExpense | PRIOR_FY_EXPENSE | — | ✅ |
| 41 | ReportingDepreciationSummaryProduction | PRODUCTION | — | ✅ |
| 42 | ReportingDepreciationSummaryRevalAmortBalance | REVAL_AMORT_BALANCE | — | ✅ |
| 43 | ReportingDepreciationSummaryRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 44 | ReportingDepreciationSummaryRevalAmortizationAdjustment | REVAL_AMORTIZATION_ADJUSTMENT | — | ✅ |
| 45 | ReportingDepreciationSummaryRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 46 | ReportingDepreciationSummaryRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 47 | ReportingDepreciationSummaryRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 48 | ReportingDepreciationSummaryRevalReserve | REVAL_RESERVE | — | ✅ |
| 49 | ReportingDepreciationSummarySetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 50 | ReportingDepreciationSummarySystemBonusDeprnAmount | SYSTEM_BONUS_DEPRN_AMOUNT | — | ✅ |
| 51 | ReportingDepreciationSummarySystemDeprnAmount | SYSTEM_DEPRN_AMOUNT | — | ✅ |
| 52 | ReportingDepreciationSummaryYtdBacklogDeprn | YTD_BACKLOG_DEPRN | — | ✅ |
| 53 | ReportingDepreciationSummaryYtdDeprn | YTD_DEPRN | — | ✅ |
| 54 | ReportingDepreciationSummaryYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 55 | ReportingDepreciationSummaryYtdProduction | YTD_PRODUCTION | — | ✅ |
| 56 | ReportingDepreciationSummaryYtdRevalAmortization | YTD_REVAL_AMORTIZATION | — | ✅ |
| 57 | ReportingDepreciationSummaryYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
