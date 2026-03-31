---
id: DOC-OTHER-PVO-ReportingDepreciationDetailExtractPVO
doc_type: system-doc
title: "ReportingDepreciationDetailExtractPVO — PVO Cross-Module"
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
  - ReportingDepreciationDetailExtractPVO
  - reportingdepreciationdetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingDepreciationDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Depreciation Detail Extract. Acessa as tabelas: FA_MC_DEPRN_DETAIL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingDepreciationDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 1 | 5 | 53 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_deprn_detail|FA_MC_DEPRN_DETAIL]] — 53 atributos (5 PKs, 53 BICC)

---

## ⚙️ Atributos

### [[fa_mc_deprn_detail|FA_MC_DEPRN_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingDepreciationDetailAccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | ReportingDepreciationDetailAcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 3 | ReportingDepreciationDetailAcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 4 | ReportingDepreciationDetailAcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 5 | ReportingDepreciationDetailAdditionCostToClear | ADDITION_COST_TO_CLEAR | — | ✅ |
| 6 | ReportingDepreciationDetailAssetId | ASSET_ID | 🔑 | ✅ |
| 7 | ReportingDepreciationDetailBacklogDeprnReserve | BACKLOG_DEPRN_RESERVE | — | ✅ |
| 8 | ReportingDepreciationDetailBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 9 | ReportingDepreciationDetailBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 10 | ReportingDepreciationDetailBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 11 | ReportingDepreciationDetailBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 12 | ReportingDepreciationDetailBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 13 | ReportingDepreciationDetailCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 14 | ReportingDepreciationDetailConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 15 | ReportingDepreciationDetailCost | COST | — | ✅ |
| 16 | ReportingDepreciationDetailCreatedBy | CREATED_BY | — | ✅ |
| 17 | ReportingDepreciationDetailCreationDate | CREATION_DATE | — | ✅ |
| 18 | ReportingDepreciationDetailDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 19 | ReportingDepreciationDetailDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 20 | ReportingDepreciationDetailDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 21 | ReportingDepreciationDetailDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 22 | ReportingDepreciationDetailDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 23 | ReportingDepreciationDetailDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 24 | ReportingDepreciationDetailDistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 25 | ReportingDepreciationDetailEventId | EVENT_ID | — | ✅ |
| 26 | ReportingDepreciationDetailGeneralFund | GENERAL_FUND | — | ✅ |
| 27 | ReportingDepreciationDetailImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 28 | ReportingDepreciationDetailImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 29 | ReportingDepreciationDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | ReportingDepreciationDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | ReportingDepreciationDetailLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | ReportingDepreciationDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | ReportingDepreciationDetailPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 34 | ReportingDepreciationDetailRevalAmortBalance | REVAL_AMORT_BALANCE | — | ✅ |
| 35 | ReportingDepreciationDetailRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 36 | ReportingDepreciationDetailRevalAmortizationAdjustment | REVAL_AMORTIZATION_ADJUSTMENT | — | ✅ |
| 37 | ReportingDepreciationDetailRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 38 | ReportingDepreciationDetailRevalReserve | REVAL_RESERVE | — | ✅ |
| 39 | ReportingDepreciationDetailSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 40 | ReportingDepreciationDetailSourceAdditionCostToClear | SOURCE_ADDITION_COST_TO_CLEAR | — | ✅ |
| 41 | ReportingDepreciationDetailSourceDeprnAdjustmentAmount | SOURCE_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 42 | ReportingDepreciationDetailSourceDeprnAmount | SOURCE_DEPRN_AMOUNT | — | ✅ |
| 43 | ReportingDepreciationDetailSourceDeprnReserve | SOURCE_DEPRN_RESERVE | — | ✅ |
| 44 | ReportingDepreciationDetailSourceRevalAmortization | SOURCE_REVAL_AMORTIZATION | — | ✅ |
| 45 | ReportingDepreciationDetailSourceRevalDeprnExpense | SOURCE_REVAL_DEPRN_EXPENSE | — | ✅ |
| 46 | ReportingDepreciationDetailSourceRevalReserve | SOURCE_REVAL_RESERVE | — | ✅ |
| 47 | ReportingDepreciationDetailSourceYtdDeprn | SOURCE_YTD_DEPRN | — | ✅ |
| 48 | ReportingDepreciationDetailSourceYtdRevalDeprnExpense | SOURCE_YTD_REVAL_DEPRN_EXPENSE | — | ✅ |
| 49 | ReportingDepreciationDetailYtdBacklogDeprn | YTD_BACKLOG_DEPRN | — | ✅ |
| 50 | ReportingDepreciationDetailYtdDeprn | YTD_DEPRN | — | ✅ |
| 51 | ReportingDepreciationDetailYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 52 | ReportingDepreciationDetailYtdRevalAmortization | YTD_REVAL_AMORTIZATION | — | ✅ |
| 53 | ReportingDepreciationDetailYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
