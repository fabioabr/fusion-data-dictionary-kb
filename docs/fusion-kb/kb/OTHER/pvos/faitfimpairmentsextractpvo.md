---
id: DOC-OTHER-PVO-FaItfImpairmentsExtractPVO
doc_type: system-doc
title: "FaItfImpairmentsExtractPVO — PVO Cross-Module"
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
  - FaItfImpairmentsExtractPVO
  - faitfimpairmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaItfImpairmentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Itf Impairments Extract. Acessa as tabelas: FA_ITF_IMPAIRMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.FaItfImpairmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 97 | 1 | 2 | 97 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_itf_impairments|FA_ITF_IMPAIRMENTS]] — 97 atributos (2 PKs, 97 BICC)

---

## ⚙️ Atributos

### [[fa_itf_impairments|FA_ITF_IMPAIRMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaItfImpairmentsAdjustedCost | ADJUSTED_COST | — | ✅ |
| 2 | FaItfImpairmentsAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 3 | FaItfImpairmentsAssetId | ASSET_ID | 🔑 | ✅ |
| 4 | FaItfImpairmentsBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 5 | FaItfImpairmentsBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 6 | FaItfImpairmentsBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 7 | FaItfImpairmentsBonusRate | BONUS_RATE | — | ✅ |
| 8 | FaItfImpairmentsBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 9 | FaItfImpairmentsBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 10 | FaItfImpairmentsCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 11 | FaItfImpairmentsCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | ✅ |
| 12 | FaItfImpairmentsCategoryId | CATEGORY_ID | — | ✅ |
| 13 | FaItfImpairmentsCost | COST | — | ✅ |
| 14 | FaItfImpairmentsCreatedBy | CREATED_BY | — | ✅ |
| 15 | FaItfImpairmentsCreationDate | CREATION_DATE | — | ✅ |
| 16 | FaItfImpairmentsCurrentUnits | CURRENT_UNITS | — | ✅ |
| 17 | FaItfImpairmentsDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 18 | FaItfImpairmentsDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 19 | FaItfImpairmentsDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 20 | FaItfImpairmentsDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 21 | FaItfImpairmentsDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 22 | FaItfImpairmentsEofyReserve | EOFY_RESERVE | — | ✅ |
| 23 | FaItfImpairmentsFormulaFactor | FORMULA_FACTOR | — | ✅ |
| 24 | FaItfImpairmentsGeneralFund | GENERAL_FUND | — | ✅ |
| 25 | FaItfImpairmentsGoodwillAssetFlag | GOODWILL_ASSET_FLAG | — | ✅ |
| 26 | FaItfImpairmentsHistoricalNetBookValue | HISTORICAL_NET_BOOK_VALUE | — | ✅ |
| 27 | FaItfImpairmentsImpairClass | IMPAIR_CLASS | — | ✅ |
| 28 | FaItfImpairmentsImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 29 | FaItfImpairmentsImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 30 | FaItfImpairmentsImpairmentDate | IMPAIRMENT_DATE | — | ✅ |
| 31 | FaItfImpairmentsImpairmentId | IMPAIRMENT_ID | 🔑 | ✅ |
| 32 | FaItfImpairmentsImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 33 | FaItfImpairmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | FaItfImpairmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | FaItfImpairmentsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | FaItfImpairmentsLtdProduction | LTD_PRODUCTION | — | ✅ |
| 37 | FaItfImpairmentsNetBookValue | NET_BOOK_VALUE | — | ✅ |
| 38 | FaItfImpairmentsNetSellingPrice | NET_SELLING_PRICE | — | ✅ |
| 39 | FaItfImpairmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | FaItfImpairmentsPeriodCounter | PERIOD_COUNTER | — | ✅ |
| 41 | FaItfImpairmentsPeriodOfAdditionFlag | PERIOD_OF_ADDITION_FLAG | — | ✅ |
| 42 | FaItfImpairmentsPriorFyBonusExpense | PRIOR_FY_BONUS_EXPENSE | — | ✅ |
| 43 | FaItfImpairmentsPriorFyExpense | PRIOR_FY_EXPENSE | — | ✅ |
| 44 | FaItfImpairmentsProcessOrder | PROCESS_ORDER | — | ✅ |
| 45 | FaItfImpairmentsProduction | PRODUCTION | — | ✅ |
| 46 | FaItfImpairmentsRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | ✅ |
| 47 | FaItfImpairmentsReason | REASON | — | ✅ |
| 48 | FaItfImpairmentsRequestId | REQUEST_ID | — | ✅ |
| 49 | FaItfImpairmentsRevalAmortBalance | REVAL_AMORT_BALANCE | — | ✅ |
| 50 | FaItfImpairmentsRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 51 | FaItfImpairmentsRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 52 | FaItfImpairmentsRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 53 | FaItfImpairmentsRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 54 | FaItfImpairmentsRevalReserve | REVAL_RESERVE | — | ✅ |
| 55 | FaItfImpairmentsRevalReserveAdjAmount | REVAL_RESERVE_ADJ_AMOUNT | — | ✅ |
| 56 | FaItfImpairmentsReversedDeprnImpact | REVERSED_DEPRN_IMPACT | — | ✅ |
| 57 | FaItfImpairmentsReversedDeprnImpactS1 | REVERSED_DEPRN_IMPACT_S1 | — | ✅ |
| 58 | FaItfImpairmentsReversedDeprnImpactS2 | REVERSED_DEPRN_IMPACT_S2 | — | ✅ |
| 59 | FaItfImpairmentsReversedDeprnImpactS3 | REVERSED_DEPRN_IMPACT_S3 | — | ✅ |
| 60 | FaItfImpairmentsReversedImpAmt | REVERSED_IMP_AMT | — | ✅ |
| 61 | FaItfImpairmentsReversedImpAmtS1 | REVERSED_IMP_AMT_S1 | — | ✅ |
| 62 | FaItfImpairmentsReversedImpAmtS2 | REVERSED_IMP_AMT_S2 | — | ✅ |
| 63 | FaItfImpairmentsReversedImpAmtS3 | REVERSED_IMP_AMT_S3 | — | ✅ |
| 64 | FaItfImpairmentsReversedRevalAmt | REVERSED_REVAL_AMT | — | ✅ |
| 65 | FaItfImpairmentsReversedRevalAmtS1 | REVERSED_REVAL_AMT_S1 | — | ✅ |
| 66 | FaItfImpairmentsReversedRevalAmtS2 | REVERSED_REVAL_AMT_S2 | — | ✅ |
| 67 | FaItfImpairmentsReversedRevalAmtS3 | REVERSED_REVAL_AMT_S3 | — | ✅ |
| 68 | FaItfImpairmentsReversedRevalImpact | REVERSED_REVAL_IMPACT | — | ✅ |
| 69 | FaItfImpairmentsReversedRevalImpactS1 | REVERSED_REVAL_IMPACT_S1 | — | ✅ |
| 70 | FaItfImpairmentsReversedRevalImpactS2 | REVERSED_REVAL_IMPACT_S2 | — | ✅ |
| 71 | FaItfImpairmentsReversedRevalImpactS3 | REVERSED_REVAL_IMPACT_S3 | — | ✅ |
| 72 | FaItfImpairmentsSplit1ImpairClass | SPLIT1_IMPAIR_CLASS | — | ✅ |
| 73 | FaItfImpairmentsSplit1LossAmount | SPLIT1_LOSS_AMOUNT | — | ✅ |
| 74 | FaItfImpairmentsSplit1Percent | SPLIT1_PERCENT | — | ✅ |
| 75 | FaItfImpairmentsSplit1ProcessOrder | SPLIT1_PROCESS_ORDER | — | ✅ |
| 76 | FaItfImpairmentsSplit1Reason | SPLIT1_REASON | — | ✅ |
| 77 | FaItfImpairmentsSplit1RevalReserve | SPLIT1_REVAL_RESERVE | — | ✅ |
| 78 | FaItfImpairmentsSplit2ImpairClass | SPLIT2_IMPAIR_CLASS | — | ✅ |
| 79 | FaItfImpairmentsSplit2LossAmount | SPLIT2_LOSS_AMOUNT | — | ✅ |
| 80 | FaItfImpairmentsSplit2Percent | SPLIT2_PERCENT | — | ✅ |
| 81 | FaItfImpairmentsSplit2ProcessOrder | SPLIT2_PROCESS_ORDER | — | ✅ |
| 82 | FaItfImpairmentsSplit2Reason | SPLIT2_REASON | — | ✅ |
| 83 | FaItfImpairmentsSplit2RevalReserve | SPLIT2_REVAL_RESERVE | — | ✅ |
| 84 | FaItfImpairmentsSplit3ImpairClass | SPLIT3_IMPAIR_CLASS | — | ✅ |
| 85 | FaItfImpairmentsSplit3LossAmount | SPLIT3_LOSS_AMOUNT | — | ✅ |
| 86 | FaItfImpairmentsSplit3Percent | SPLIT3_PERCENT | — | ✅ |
| 87 | FaItfImpairmentsSplit3ProcessOrder | SPLIT3_PROCESS_ORDER | — | ✅ |
| 88 | FaItfImpairmentsSplit3Reason | SPLIT3_REASON | — | ✅ |
| 89 | FaItfImpairmentsSplit3RevalReserve | SPLIT3_REVAL_RESERVE | — | ✅ |
| 90 | FaItfImpairmentsSplitImpairFlag | SPLIT_IMPAIR_FLAG | — | ✅ |
| 91 | FaItfImpairmentsSystemBonusDeprnAmount | SYSTEM_BONUS_DEPRN_AMOUNT | — | ✅ |
| 92 | FaItfImpairmentsSystemDeprnAmount | SYSTEM_DEPRN_AMOUNT | — | ✅ |
| 93 | FaItfImpairmentsValueInUse | VALUE_IN_USE | — | ✅ |
| 94 | FaItfImpairmentsYtdDeprn | YTD_DEPRN | — | ✅ |
| 95 | FaItfImpairmentsYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 96 | FaItfImpairmentsYtdProduction | YTD_PRODUCTION | — | ✅ |
| 97 | FaItfImpairmentsYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
