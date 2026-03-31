---
id: DOC-OTHER-PVO-FaItfImpairmentsPVO
doc_type: system-doc
title: "FaItfImpairmentsPVO — PVO Cross-Module"
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
  - FaItfImpairmentsPVO
  - faitfimpairmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaItfImpairmentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Itf Impairments. Acessa as tabelas: FA_CASH_GEN_UNITS, FA_DEPRN_PERIODS, FA_ITF_IMPAIRMENTS.

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.FaItfImpairmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 3 | 2 | 43 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[fa_cash_gen_units|FA_CASH_GEN_UNITS]] — 11 atributos (2 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 16 atributos (1 BICC)
- [[fa_itf_impairments|FA_ITF_IMPAIRMENTS]] — 98 atributos (2 PKs, 40 BICC)

---

## ⚙️ Atributos

### [[fa_cash_gen_units|FA_CASH_GEN_UNITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashGenUnitBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | CashGenUnitCashGeneratingUnit | CASH_GENERATING_UNIT | — | ✅ |
| 3 | CashGenUnitCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | — |
| 4 | CashGenUnitCreatedBy | CREATED_BY | — | — |
| 5 | CashGenUnitCreationDate | CREATION_DATE | — | — |
| 6 | CashGenUnitDescription | DESCRIPTION | — | — |
| 7 | CashGenUnitDisabledFlag | DISABLED_FLAG | — | — |
| 8 | CashGenUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CashGenUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | CashGenUnitLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | CashGenUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DepreciationPeriodCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 3 | DepreciationPeriodCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 4 | DepreciationPeriodCreatedBy | CREATED_BY | — | — |
| 5 | DepreciationPeriodCreationDate | CREATION_DATE | — | — |
| 6 | DepreciationPeriodDeprnRun | DEPRN_RUN | — | — |
| 7 | DepreciationPeriodFiscalYear | FISCAL_YEAR | — | — |
| 8 | DepreciationPeriodLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | DepreciationPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | DepreciationPeriodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | DepreciationPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | DepreciationPeriodPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 13 | DepreciationPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 14 | DepreciationPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 15 | DepreciationPeriodPeriodNum | PERIOD_NUM | — | — |
| 16 | DepreciationPeriodPeriodOpenDate | PERIOD_OPEN_DATE | — | — |

### [[fa_itf_impairments|FA_ITF_IMPAIRMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | 🔑 | ✅ |
| 2 | FaItfImpairmentsAdjustedCost | ADJUSTED_COST | — | ✅ |
| 3 | FaItfImpairmentsAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 4 | FaItfImpairmentsBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | — |
| 5 | FaItfImpairmentsBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 6 | FaItfImpairmentsBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 7 | FaItfImpairmentsBonusRate | BONUS_RATE | — | ✅ |
| 8 | FaItfImpairmentsBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 9 | FaItfImpairmentsBookTypeCode | BOOK_TYPE_CODE | — | — |
| 10 | FaItfImpairmentsCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 11 | FaItfImpairmentsCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | — |
| 12 | FaItfImpairmentsCategoryId | CATEGORY_ID | — | — |
| 13 | FaItfImpairmentsCost | COST | — | ✅ |
| 14 | FaItfImpairmentsCreatedBy | CREATED_BY | — | — |
| 15 | FaItfImpairmentsCreationDate | CREATION_DATE | — | — |
| 16 | FaItfImpairmentsCurrentUnits | CURRENT_UNITS | — | ✅ |
| 17 | FaItfImpairmentsDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | — |
| 18 | FaItfImpairmentsDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 19 | FaItfImpairmentsDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 20 | FaItfImpairmentsDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 21 | FaItfImpairmentsDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 22 | FaItfImpairmentsEofyReserve | EOFY_RESERVE | — | — |
| 23 | FaItfImpairmentsFormulaFactor | FORMULA_FACTOR | — | — |
| 24 | FaItfImpairmentsGeneralFund | GENERAL_FUND | — | ✅ |
| 25 | FaItfImpairmentsGoodwillAssetFlag | GOODWILL_ASSET_FLAG | — | ✅ |
| 26 | FaItfImpairmentsHistoricalNetBookValue | HISTORICAL_NET_BOOK_VALUE | — | ✅ |
| 27 | FaItfImpairmentsImpairClass | IMPAIR_CLASS | — | — |
| 28 | FaItfImpairmentsImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 29 | FaItfImpairmentsImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 30 | FaItfImpairmentsImpairmentDate | IMPAIRMENT_DATE | — | ✅ |
| 31 | FaItfImpairmentsImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 32 | FaItfImpairmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | FaItfImpairmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | FaItfImpairmentsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | FaItfImpairmentsLtdProduction | LTD_PRODUCTION | — | ✅ |
| 36 | FaItfImpairmentsNetBookValue | NET_BOOK_VALUE | — | ✅ |
| 37 | FaItfImpairmentsNetSellingPrice | NET_SELLING_PRICE | — | ✅ |
| 38 | FaItfImpairmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 39 | FaItfImpairmentsPeriodCounter | PERIOD_COUNTER | — | — |
| 40 | FaItfImpairmentsPeriodOfAdditionFlag | PERIOD_OF_ADDITION_FLAG | — | — |
| 41 | FaItfImpairmentsPriorFyBonusExpense | PRIOR_FY_BONUS_EXPENSE | — | ✅ |
| 42 | FaItfImpairmentsPriorFyExpense | PRIOR_FY_EXPENSE | — | ✅ |
| 43 | FaItfImpairmentsProcessOrder | PROCESS_ORDER | — | — |
| 44 | FaItfImpairmentsProduction | PRODUCTION | — | ✅ |
| 45 | FaItfImpairmentsRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 46 | FaItfImpairmentsReason | REASON | — | — |
| 47 | FaItfImpairmentsRequestId | REQUEST_ID | — | — |
| 48 | FaItfImpairmentsRevalAmortBalance | REVAL_AMORT_BALANCE | — | ✅ |
| 49 | FaItfImpairmentsRevalAmortization | REVAL_AMORTIZATION | — | ✅ |
| 50 | FaItfImpairmentsRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 51 | FaItfImpairmentsRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | ✅ |
| 52 | FaItfImpairmentsRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 53 | FaItfImpairmentsRevalReserve | REVAL_RESERVE | — | ✅ |
| 54 | FaItfImpairmentsRevalReserveAdjAmount | REVAL_RESERVE_ADJ_AMOUNT | — | — |
| 55 | FaItfImpairmentsReversedDeprnImpact | REVERSED_DEPRN_IMPACT | — | — |
| 56 | FaItfImpairmentsReversedDeprnImpactS1 | REVERSED_DEPRN_IMPACT_S1 | — | — |
| 57 | FaItfImpairmentsReversedDeprnImpactS2 | REVERSED_DEPRN_IMPACT_S2 | — | — |
| 58 | FaItfImpairmentsReversedDeprnImpactS3 | REVERSED_DEPRN_IMPACT_S3 | — | — |
| 59 | FaItfImpairmentsReversedImpAmt | REVERSED_IMP_AMT | — | — |
| 60 | FaItfImpairmentsReversedImpAmtS1 | REVERSED_IMP_AMT_S1 | — | — |
| 61 | FaItfImpairmentsReversedImpAmtS2 | REVERSED_IMP_AMT_S2 | — | — |
| 62 | FaItfImpairmentsReversedImpAmtS3 | REVERSED_IMP_AMT_S3 | — | — |
| 63 | FaItfImpairmentsReversedRevalAmt | REVERSED_REVAL_AMT | — | — |
| 64 | FaItfImpairmentsReversedRevalAmtS1 | REVERSED_REVAL_AMT_S1 | — | — |
| 65 | FaItfImpairmentsReversedRevalAmtS2 | REVERSED_REVAL_AMT_S2 | — | — |
| 66 | FaItfImpairmentsReversedRevalAmtS3 | REVERSED_REVAL_AMT_S3 | — | — |
| 67 | FaItfImpairmentsReversedRevalImpact | REVERSED_REVAL_IMPACT | — | — |
| 68 | FaItfImpairmentsReversedRevalImpactS1 | REVERSED_REVAL_IMPACT_S1 | — | — |
| 69 | FaItfImpairmentsReversedRevalImpactS2 | REVERSED_REVAL_IMPACT_S2 | — | — |
| 70 | FaItfImpairmentsReversedRevalImpactS3 | REVERSED_REVAL_IMPACT_S3 | — | — |
| 71 | FaItfImpairmentsSplit1ImpairClass | SPLIT1_IMPAIR_CLASS | — | — |
| 72 | FaItfImpairmentsSplit1LossAmount | SPLIT1_LOSS_AMOUNT | — | — |
| 73 | FaItfImpairmentsSplit1Percent | SPLIT1_PERCENT | — | — |
| 74 | FaItfImpairmentsSplit1ProcessOrder | SPLIT1_PROCESS_ORDER | — | — |
| 75 | FaItfImpairmentsSplit1Reason | SPLIT1_REASON | — | — |
| 76 | FaItfImpairmentsSplit1RevalReserve | SPLIT1_REVAL_RESERVE | — | — |
| 77 | FaItfImpairmentsSplit2ImpairClass | SPLIT2_IMPAIR_CLASS | — | — |
| 78 | FaItfImpairmentsSplit2LossAmount | SPLIT2_LOSS_AMOUNT | — | — |
| 79 | FaItfImpairmentsSplit2Percent | SPLIT2_PERCENT | — | — |
| 80 | FaItfImpairmentsSplit2ProcessOrder | SPLIT2_PROCESS_ORDER | — | — |
| 81 | FaItfImpairmentsSplit2Reason | SPLIT2_REASON | — | — |
| 82 | FaItfImpairmentsSplit2RevalReserve | SPLIT2_REVAL_RESERVE | — | — |
| 83 | FaItfImpairmentsSplit3ImpairClass | SPLIT3_IMPAIR_CLASS | — | — |
| 84 | FaItfImpairmentsSplit3LossAmount | SPLIT3_LOSS_AMOUNT | — | — |
| 85 | FaItfImpairmentsSplit3Percent | SPLIT3_PERCENT | — | — |
| 86 | FaItfImpairmentsSplit3ProcessOrder | SPLIT3_PROCESS_ORDER | — | — |
| 87 | FaItfImpairmentsSplit3Reason | SPLIT3_REASON | — | — |
| 88 | FaItfImpairmentsSplit3RevalReserve | SPLIT3_REVAL_RESERVE | — | — |
| 89 | FaItfImpairmentsSplitImpairFlag | SPLIT_IMPAIR_FLAG | — | — |
| 90 | FaItfImpairmentsSystemBonusDeprnAmount | SYSTEM_BONUS_DEPRN_AMOUNT | — | — |
| 91 | FaItfImpairmentsSystemDeprnAmount | SYSTEM_DEPRN_AMOUNT | — | — |
| 92 | FaItfImpairmentsValueInUse | VALUE_IN_USE | — | ✅ |
| 93 | FaItfImpairmentsWorkerId | WORKER_ID | — | — |
| 94 | FaItfImpairmentsYtdDeprn | YTD_DEPRN | — | ✅ |
| 95 | FaItfImpairmentsYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 96 | FaItfImpairmentsYtdProduction | YTD_PRODUCTION | — | ✅ |
| 97 | FaItfImpairmentsYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | ✅ |
| 98 | ImpairmentId | IMPAIRMENT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
