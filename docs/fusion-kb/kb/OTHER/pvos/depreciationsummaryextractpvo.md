---
id: DOC-OTHER-PVO-DepreciationSummaryExtractPVO
doc_type: system-doc
title: "DepreciationSummaryExtractPVO — PVO Cross-Module"
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
  - DepreciationSummaryExtractPVO
  - depreciationsummaryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationSummaryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Summary Extract. Acessa as tabelas: FA_DEPRN_SUMMARY.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DepreciationSummaryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 1 | 3 | 36 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deprn_summary|FA_DEPRN_SUMMARY]] — 49 atributos (3 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[fa_deprn_summary|FA_DEPRN_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationSummaryAdjustedCost | ADJUSTED_COST | — | ✅ |
| 2 | DepreciationSummaryAssetId | ASSET_ID | 🔑 | ✅ |
| 3 | DepreciationSummaryBacklogDeprnReserve | BACKLOG_DEPRN_RESERVE | — | — |
| 4 | DepreciationSummaryBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 5 | DepreciationSummaryBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 6 | DepreciationSummaryBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 7 | DepreciationSummaryBonusRate | BONUS_RATE | — | ✅ |
| 8 | DepreciationSummaryBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 9 | DepreciationSummaryBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 10 | DepreciationSummaryCapitalAdjustment | CAPITAL_ADJUSTMENT | — | — |
| 11 | DepreciationSummaryCreatedBy | CREATED_BY | — | ✅ |
| 12 | DepreciationSummaryCreationDate | CREATION_DATE | — | ✅ |
| 13 | DepreciationSummaryDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 14 | DepreciationSummaryDeprnAdjustmentFactor | DEPRN_ADJUSTMENT_FACTOR | — | — |
| 15 | DepreciationSummaryDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 16 | DepreciationSummaryDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 17 | DepreciationSummaryDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 18 | DepreciationSummaryDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 19 | DepreciationSummaryDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 20 | DepreciationSummaryDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 21 | DepreciationSummaryEventId | EVENT_ID | — | ✅ |
| 22 | DepreciationSummaryGeneralFund | GENERAL_FUND | — | — |
| 23 | DepreciationSummaryImpairLossBalance | IMPAIR_LOSS_BALANCE | — | — |
| 24 | DepreciationSummaryImpairmentAmount | IMPAIRMENT_AMOUNT | — | — |
| 25 | DepreciationSummaryImpairmentReserve | IMPAIRMENT_RESERVE | — | — |
| 26 | DepreciationSummaryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | DepreciationSummaryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | DepreciationSummaryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | DepreciationSummaryLtdProduction | LTD_PRODUCTION | — | ✅ |
| 30 | DepreciationSummaryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 31 | DepreciationSummaryPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 32 | DepreciationSummaryPriorFyBonusExpense | PRIOR_FY_BONUS_EXPENSE | — | ✅ |
| 33 | DepreciationSummaryPriorFyExpense | PRIOR_FY_EXPENSE | — | ✅ |
| 34 | DepreciationSummaryProduction | PRODUCTION | — | ✅ |
| 35 | DepreciationSummaryRevalAmortBalance | REVAL_AMORT_BALANCE | — | — |
| 36 | DepreciationSummaryRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 37 | DepreciationSummaryRevalAmortizationAdjustment | REVAL_AMORTIZATION_ADJUSTMENT | — | — |
| 38 | DepreciationSummaryRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 39 | DepreciationSummaryRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 40 | DepreciationSummaryRevalLossBalance | REVAL_LOSS_BALANCE | — | — |
| 41 | DepreciationSummaryRevalReserve | REVAL_RESERVE | — | ✅ |
| 42 | DepreciationSummarySystemBonusDeprnAmount | SYSTEM_BONUS_DEPRN_AMOUNT | — | ✅ |
| 43 | DepreciationSummarySystemDeprnAmount | SYSTEM_DEPRN_AMOUNT | — | ✅ |
| 44 | DepreciationSummaryYtdBacklogDeprn | YTD_BACKLOG_DEPRN | — | — |
| 45 | DepreciationSummaryYtdDeprn | YTD_DEPRN | — | ✅ |
| 46 | DepreciationSummaryYtdImpairment | YTD_IMPAIRMENT | — | — |
| 47 | DepreciationSummaryYtdProduction | YTD_PRODUCTION | — | ✅ |
| 48 | DepreciationSummaryYtdRevalAmortization | YTD_REVAL_AMORTIZATION | — | — |
| 49 | DepreciationSummaryYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
