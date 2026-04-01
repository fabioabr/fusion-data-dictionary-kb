---
id: DOC-OTHER-PVO-RevaluationsPVO
doc_type: system-doc
title: "RevaluationsPVO — PVO Cross-Module"
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
  - RevaluationsPVO
  - revaluationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevaluationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Revaluations. Acessa as tabelas: FA_PRICE_INDEXES, FA_REVALUATIONS.

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.RevaluationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 2 | 1 | 24 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[fa_price_indexes|FA_PRICE_INDEXES]] — 10 atributos (2 BICC)
- [[fa_revaluations|FA_REVALUATIONS]] — 47 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[fa_price_indexes|FA_PRICE_INDEXES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceIndexCalendarType | CALENDAR_TYPE | — | — |
| 2 | PriceIndexCreatedBy | CREATED_BY | — | — |
| 3 | PriceIndexCreationDate | CREATION_DATE | — | — |
| 4 | PriceIndexDescription | DESCRIPTION | — | — |
| 5 | PriceIndexLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PriceIndexLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PriceIndexLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PriceIndexObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PriceIndexPriceIndexId | PRICE_INDEX_ID | — | — |
| 10 | PriceIndexPriceIndexName | PRICE_INDEX_NAME | — | ✅ |

### [[fa_revaluations|FA_REVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevaluationsAllowFundAccountingFlag | ALLOW_FUND_ACCOUNTING_FLAG | — | — |
| 2 | RevaluationsAmortizeRevalReserveFlag | AMORTIZE_REVAL_RESERVE_FLAG | — | — |
| 3 | RevaluationsAssetId | ASSET_ID | — | — |
| 4 | RevaluationsBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 5 | RevaluationsBookTypeCode | BOOK_TYPE_CODE | — | — |
| 6 | RevaluationsCost | COST | — | ✅ |
| 7 | RevaluationsCreatedBy | CREATED_BY | — | — |
| 8 | RevaluationsCreationDate | CREATION_DATE | — | — |
| 9 | RevaluationsDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 10 | RevaluationsFairMarketValue | FAIR_MARKET_VALUE | — | — |
| 11 | RevaluationsImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 12 | RevaluationsImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 13 | RevaluationsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | RevaluationsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | RevaluationsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | RevaluationsLifeExtensionCeiling | LIFE_EXTENSION_CEILING | — | — |
| 17 | RevaluationsLifeExtensionFactor | LIFE_EXTENSION_FACTOR | — | — |
| 18 | RevaluationsLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 19 | RevaluationsLinkedFlag | LINKED_FLAG | — | — |
| 20 | RevaluationsMassRevalId | MASS_REVAL_ID | — | — |
| 21 | RevaluationsMaxFullyRsvdRevals | MAX_FULLY_RSVD_REVALS | — | — |
| 22 | RevaluationsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | RevaluationsPeriodEndRevalFlag | PERIOD_END_REVAL_FLAG | — | — |
| 24 | RevaluationsPriceIndexId | PRICE_INDEX_ID | — | — |
| 25 | RevaluationsPriceIndexValue | PRICE_INDEX_VALUE | — | ✅ |
| 26 | RevaluationsPriorBonusDeprnReserve | PRIOR_BONUS_DEPRN_RESERVE | — | ✅ |
| 27 | RevaluationsPriorCost | PRIOR_COST | — | ✅ |
| 28 | RevaluationsPriorDeprnReserve | PRIOR_DEPRN_RESERVE | — | ✅ |
| 29 | RevaluationsPriorFairMarketValue | PRIOR_FAIR_MARKET_VALUE | — | ✅ |
| 30 | RevaluationsPriorImpairLossBalance | PRIOR_IMPAIR_LOSS_BALANCE | — | ✅ |
| 31 | RevaluationsPriorImpairmentReserve | PRIOR_IMPAIRMENT_RESERVE | — | ✅ |
| 32 | RevaluationsPriorLifeInMonths | PRIOR_LIFE_IN_MONTHS | — | ✅ |
| 33 | RevaluationsPriorRevalAmortBasis | PRIOR_REVAL_AMORT_BASIS | — | ✅ |
| 34 | RevaluationsPriorRevalLossBalance | PRIOR_REVAL_LOSS_BALANCE | — | ✅ |
| 35 | RevaluationsPriorRevalReserve | PRIOR_REVAL_RESERVE | — | ✅ |
| 36 | RevaluationsRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 37 | RevaluationsRevalAmount | REVAL_AMOUNT | — | — |
| 38 | RevaluationsRevalDeprnReserveFlag | REVAL_DEPRN_RESERVE_FLAG | — | — |
| 39 | RevaluationsRevalFullyRsvdFlag | REVAL_FULLY_RSVD_FLAG | — | — |
| 40 | RevaluationsRevalGainLoss | REVAL_GAIN_LOSS | — | — |
| 41 | RevaluationsRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 42 | RevaluationsRevalMethod | REVAL_METHOD | — | — |
| 43 | RevaluationsRevalPercentage | REVAL_PERCENTAGE | — | — |
| 44 | RevaluationsRevalReserve | REVAL_RESERVE | — | ✅ |
| 45 | RevaluationsRevalValueType | REVAL_VALUE_TYPE | — | — |
| 46 | RevaluationsRevalYtdDeprnFlag | REVAL_YTD_DEPRN_FLAG | — | — |
| 47 | TransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
