---
id: DOC-OTHER-PVO-DepreciationDetailExtractPVO
doc_type: system-doc
title: "DepreciationDetailExtractPVO — PVO Cross-Module"
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
  - DepreciationDetailExtractPVO
  - depreciationdetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Detail Extract. Acessa as tabelas: FA_DEPRN_DETAIL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DepreciationDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 1 | 4 | 37 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deprn_detail|FA_DEPRN_DETAIL]] — 42 atributos (4 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[fa_deprn_detail|FA_DEPRN_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationDetailAccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | DepreciationDetailAcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 3 | DepreciationDetailAcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 4 | DepreciationDetailAcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 5 | DepreciationDetailAdditionCostToClear | ADDITION_COST_TO_CLEAR | — | ✅ |
| 6 | DepreciationDetailAssetId | ASSET_ID | 🔑 | ✅ |
| 7 | DepreciationDetailBacklogDeprnReserve | BACKLOG_DEPRN_RESERVE | — | — |
| 8 | DepreciationDetailBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 9 | DepreciationDetailBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 10 | DepreciationDetailBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 11 | DepreciationDetailBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 12 | DepreciationDetailBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 13 | DepreciationDetailCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 14 | DepreciationDetailCost | COST | — | ✅ |
| 15 | DepreciationDetailCreatedBy | CREATED_BY | — | ✅ |
| 16 | DepreciationDetailCreationDate | CREATION_DATE | — | ✅ |
| 17 | DepreciationDetailDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 18 | DepreciationDetailDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 19 | DepreciationDetailDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 20 | DepreciationDetailDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 21 | DepreciationDetailDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 22 | DepreciationDetailDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 23 | DepreciationDetailDistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 24 | DepreciationDetailEventId | EVENT_ID | — | ✅ |
| 25 | DepreciationDetailGeneralFund | GENERAL_FUND | — | ✅ |
| 26 | DepreciationDetailImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 27 | DepreciationDetailImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 28 | DepreciationDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | DepreciationDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | DepreciationDetailLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | DepreciationDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | DepreciationDetailPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 33 | DepreciationDetailRevalAmortBalance | REVAL_AMORT_BALANCE | — | — |
| 34 | DepreciationDetailRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 35 | DepreciationDetailRevalAmortizationAdjustment | REVAL_AMORTIZATION_ADJUSTMENT | — | — |
| 36 | DepreciationDetailRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 37 | DepreciationDetailRevalReserve | REVAL_RESERVE | — | ✅ |
| 38 | DepreciationDetailYtdBacklogDeprn | YTD_BACKLOG_DEPRN | — | — |
| 39 | DepreciationDetailYtdDeprn | YTD_DEPRN | — | ✅ |
| 40 | DepreciationDetailYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 41 | DepreciationDetailYtdRevalAmortization | YTD_REVAL_AMORTIZATION | — | — |
| 42 | DepreciationDetailYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
