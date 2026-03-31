---
id: DOC-OTHER-PVO-ReportingRevaluationsExtractPVO
doc_type: system-doc
title: "ReportingRevaluationsExtractPVO — PVO Cross-Module"
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
  - ReportingRevaluationsExtractPVO
  - reportingrevaluationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingRevaluationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Revaluations Extract. Acessa as tabelas: FA_MC_REVALUATIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingRevaluationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 1 | 2 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_revaluations|FA_MC_REVALUATIONS]] — 48 atributos (2 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[fa_mc_revaluations|FA_MC_REVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingRevaluationsAllowFundAccountingFlag | ALLOW_FUND_ACCOUNTING_FLAG | — | ✅ |
| 2 | ReportingRevaluationsAmortizeRevalReserveFlag | AMORTIZE_REVAL_RESERVE_FLAG | — | ✅ |
| 3 | ReportingRevaluationsAssetId | ASSET_ID | — | ✅ |
| 4 | ReportingRevaluationsBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 5 | ReportingRevaluationsBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 6 | ReportingRevaluationsCost | COST | — | ✅ |
| 7 | ReportingRevaluationsCreatedBy | CREATED_BY | — | ✅ |
| 8 | ReportingRevaluationsCreationDate | CREATION_DATE | — | ✅ |
| 9 | ReportingRevaluationsDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 10 | ReportingRevaluationsFairMarketValue | FAIR_MARKET_VALUE | — | ✅ |
| 11 | ReportingRevaluationsImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 12 | ReportingRevaluationsImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 13 | ReportingRevaluationsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ReportingRevaluationsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ReportingRevaluationsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ReportingRevaluationsLifeExtensionCeiling | LIFE_EXTENSION_CEILING | — | ✅ |
| 17 | ReportingRevaluationsLifeExtensionFactor | LIFE_EXTENSION_FACTOR | — | ✅ |
| 18 | ReportingRevaluationsLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 19 | ReportingRevaluationsLinkedFlag | LINKED_FLAG | — | ✅ |
| 20 | ReportingRevaluationsMassRevalId | MASS_REVAL_ID | — | ✅ |
| 21 | ReportingRevaluationsMaxFullyRsvdRevals | MAX_FULLY_RSVD_REVALS | — | ✅ |
| 22 | ReportingRevaluationsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ReportingRevaluationsPeriodEndRevalFlag | PERIOD_END_REVAL_FLAG | — | ✅ |
| 24 | ReportingRevaluationsPriceIndexId | PRICE_INDEX_ID | — | ✅ |
| 25 | ReportingRevaluationsPriceIndexValue | PRICE_INDEX_VALUE | — | ✅ |
| 26 | ReportingRevaluationsPriorBonusDeprnReserve | PRIOR_BONUS_DEPRN_RESERVE | — | ✅ |
| 27 | ReportingRevaluationsPriorCost | PRIOR_COST | — | ✅ |
| 28 | ReportingRevaluationsPriorDeprnReserve | PRIOR_DEPRN_RESERVE | — | ✅ |
| 29 | ReportingRevaluationsPriorFairMarketValue | PRIOR_FAIR_MARKET_VALUE | — | ✅ |
| 30 | ReportingRevaluationsPriorImpairLossBalance | PRIOR_IMPAIR_LOSS_BALANCE | — | ✅ |
| 31 | ReportingRevaluationsPriorImpairmentReserve | PRIOR_IMPAIRMENT_RESERVE | — | ✅ |
| 32 | ReportingRevaluationsPriorLifeInMonths | PRIOR_LIFE_IN_MONTHS | — | ✅ |
| 33 | ReportingRevaluationsPriorRevalAmortBasis | PRIOR_REVAL_AMORT_BASIS | — | ✅ |
| 34 | ReportingRevaluationsPriorRevalLossBalance | PRIOR_REVAL_LOSS_BALANCE | — | ✅ |
| 35 | ReportingRevaluationsPriorRevalReserve | PRIOR_REVAL_RESERVE | — | ✅ |
| 36 | ReportingRevaluationsRevalAmortBasis | REVAL_AMORT_BASIS | — | ✅ |
| 37 | ReportingRevaluationsRevalAmount | REVAL_AMOUNT | — | ✅ |
| 38 | ReportingRevaluationsRevalDeprnReserveFlag | REVAL_DEPRN_RESERVE_FLAG | — | ✅ |
| 39 | ReportingRevaluationsRevalFullyRsvdFlag | REVAL_FULLY_RSVD_FLAG | — | ✅ |
| 40 | ReportingRevaluationsRevalGainLoss | REVAL_GAIN_LOSS | — | ✅ |
| 41 | ReportingRevaluationsRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 42 | ReportingRevaluationsRevalMethod | REVAL_METHOD | — | ✅ |
| 43 | ReportingRevaluationsRevalPercentage | REVAL_PERCENTAGE | — | ✅ |
| 44 | ReportingRevaluationsRevalReserve | REVAL_RESERVE | — | ✅ |
| 45 | ReportingRevaluationsRevalValueType | REVAL_VALUE_TYPE | — | ✅ |
| 46 | ReportingRevaluationsRevalYtdDeprnFlag | REVAL_YTD_DEPRN_FLAG | — | ✅ |
| 47 | ReportingRevaluationsSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 48 | ReportingRevaluationsTransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
