---
id: DOC-OTHER-PVO-BookSummaryExtractPVO
doc_type: system-doc
title: "BookSummaryExtractPVO — PVO Cross-Module"
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
  - BookSummaryExtractPVO
  - booksummaryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BookSummaryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Book Summary Extract. Acessa as tabelas: FA_BOOKS_SUMMARY.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.BookSummaryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 1 | 3 | 108 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[fa_books_summary|FA_BOOKS_SUMMARY]] — 127 atributos (3 PKs, 108 BICC)

---

## ⚙️ Atributos

### [[fa_books_summary|FA_BOOKS_SUMMARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookSummaryAccDeprnAdjustmentAmount | ACC_DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | BookSummaryAcceleratedAdjustedCost | ACCELERATED_ADJUSTED_COST | — | ✅ |
| 3 | BookSummaryAcceleratedDeprnAmount | ACCELERATED_DEPRN_AMOUNT | — | ✅ |
| 4 | BookSummaryAcceleratedDeprnReserve | ACCELERATED_DEPRN_RESERVE | — | ✅ |
| 5 | BookSummaryAcceleratedYtdDeprn | ACCELERATED_YTD_DEPRN | — | ✅ |
| 6 | BookSummaryAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 7 | BookSummaryAdjustedCost | ADJUSTED_COST | — | ✅ |
| 8 | BookSummaryAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | ✅ |
| 9 | BookSummaryAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 10 | BookSummaryAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 11 | BookSummaryAmortizeFlag | AMORTIZE_FLAG | — | ✅ |
| 12 | BookSummaryAssetId | ASSET_ID | 🔑 | ✅ |
| 13 | BookSummaryAssetType | ASSET_TYPE | — | ✅ |
| 14 | BookSummaryBonusAdjustedCost | BONUS_ADJUSTED_COST | — | ✅ |
| 15 | BookSummaryBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | ✅ |
| 16 | BookSummaryBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | ✅ |
| 17 | BookSummaryBonusExpenseAdjAmount | BONUS_EXPENSE_ADJ_AMOUNT | — | ✅ |
| 18 | BookSummaryBonusRate | BONUS_RATE | — | ✅ |
| 19 | BookSummaryBonusReserveAdjAmount | BONUS_RESERVE_ADJ_AMOUNT | — | ✅ |
| 20 | BookSummaryBonusReserveRetAdjAmount | BONUS_RESERVE_RET_ADJ_AMOUNT | — | ✅ |
| 21 | BookSummaryBonusRuleId | BONUS_RULE_ID | — | ✅ |
| 22 | BookSummaryBookSummaryBonusYtdDeprn | BONUS_YTD_DEPRN | — | ✅ |
| 23 | BookSummaryBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 24 | BookSummaryCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | ✅ |
| 25 | BookSummaryCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | ✅ |
| 26 | BookSummaryCapitalAdjustment | CAPITAL_ADJUSTMENT | — | ✅ |
| 27 | BookSummaryCapitalizedFlag | CAPITALIZED_FLAG | — | ✅ |
| 28 | BookSummaryCeilingTypeId | CEILING_TYPE_ID | — | ✅ |
| 29 | BookSummaryChangeInAdditionsCost | CHANGE_IN_ADDITIONS_COST | — | — |
| 30 | BookSummaryChangeInAdjustmentsCost | CHANGE_IN_ADJUSTMENTS_COST | — | — |
| 31 | BookSummaryChangeInCipCost | CHANGE_IN_CIP_COST | — | ✅ |
| 32 | BookSummaryChangeInCost | CHANGE_IN_COST | — | ✅ |
| 33 | BookSummaryChangeInEofyReserve | CHANGE_IN_EOFY_RESERVE | — | ✅ |
| 34 | BookSummaryChangeInGroupRecCost | CHANGE_IN_GROUP_REC_COST | — | — |
| 35 | BookSummaryChangeInRetirementsCost | CHANGE_IN_RETIREMENTS_COST | — | — |
| 36 | BookSummaryCipCost | CIP_COST | — | ✅ |
| 37 | BookSummaryCost | COST | — | ✅ |
| 38 | BookSummaryCreatedBy | CREATED_BY | — | ✅ |
| 39 | BookSummaryCreationDate | CREATION_DATE | — | ✅ |
| 40 | BookSummaryDatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 41 | BookSummaryDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 42 | BookSummaryDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 43 | BookSummaryDeprnAdjustmentFactor | DEPRN_ADJUSTMENT_FACTOR | — | ✅ |
| 44 | BookSummaryDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 45 | BookSummaryDeprnLimitType | DEPRN_LIMIT_TYPE | — | ✅ |
| 46 | BookSummaryDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 47 | BookSummaryDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 48 | BookSummaryDisabledFlag | DISABLED_FLAG | — | ✅ |
| 49 | BookSummaryEofyAdjCost | EOFY_ADJ_COST | — | ✅ |
| 50 | BookSummaryEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | ✅ |
| 51 | BookSummaryEofyReserve | EOFY_RESERVE | — | ✅ |
| 52 | BookSummaryEopAdjCost | EOP_ADJ_COST | — | ✅ |
| 53 | BookSummaryEopFormulaFactor | EOP_FORMULA_FACTOR | — | ✅ |
| 54 | BookSummaryExpenseAdjustmentAmount | EXPENSE_ADJUSTMENT_AMOUNT | — | ✅ |
| 55 | BookSummaryExtendedDeprnFlag | EXTENDED_DEPRN_FLAG | — | ✅ |
| 56 | BookSummaryFiscalYear | FISCAL_YEAR | — | ✅ |
| 57 | BookSummaryFlatRateId | FLAT_RATE_ID | — | ✅ |
| 58 | BookSummaryFormulaFactor | FORMULA_FACTOR | — | ✅ |
| 59 | BookSummaryFullyReserveOnAddFlag | FULLY_RESERVE_ON_ADD_FLAG | — | ✅ |
| 60 | BookSummaryFullyReservedFlag | FULLY_RESERVED_FLAG | — | ✅ |
| 61 | BookSummaryFullyRetiredFlag | FULLY_RETIRED_FLAG | — | ✅ |
| 62 | BookSummaryFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 63 | BookSummaryGeneralFund | GENERAL_FUND | — | ✅ |
| 64 | BookSummaryGroupAssetId | GROUP_ASSET_ID | — | ✅ |
| 65 | BookSummaryImpReserveRetAdjAmount | IMP_RESERVE_RET_ADJ_AMOUNT | — | ✅ |
| 66 | BookSummaryImpairLossBalance | IMPAIR_LOSS_BALANCE | — | ✅ |
| 67 | BookSummaryImpairmentAmount | IMPAIRMENT_AMOUNT | — | ✅ |
| 68 | BookSummaryImpairmentReserve | IMPAIRMENT_RESERVE | — | ✅ |
| 69 | BookSummaryImpairmentReserveAdjAmount | IMPAIRMENT_RESERVE_ADJ_AMOUNT | — | ✅ |
| 70 | BookSummaryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | BookSummaryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 72 | BookSummaryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 73 | BookSummaryLeaseAdjustmentFactor | LEASE_ADJUSTMENT_FACTOR | — | ✅ |
| 74 | BookSummaryLeaseExpenseBasis | LEASE_EXPENSE_BASIS | — | ✅ |
| 75 | BookSummaryLeaseId | LEASE_ID | — | ✅ |
| 76 | BookSummaryLeaseScheduleId | LEASE_SCHEDULE_ID | — | ✅ |
| 77 | BookSummaryLifeCompleteFlag | LIFE_COMPLETE_FLAG | — | ✅ |
| 78 | BookSummaryLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | ✅ |
| 79 | BookSummaryLtdProceedsOfSale | LTD_PROCEEDS_OF_SALE | — | ✅ |
| 80 | BookSummaryLtdProduction | LTD_PRODUCTION | — | — |
| 81 | BookSummaryMemberDeprnLimitAmount | MEMBER_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 82 | BookSummaryMemberSalvageValue | MEMBER_SALVAGE_VALUE | — | ✅ |
| 83 | BookSummaryMethodId | METHOD_ID | — | ✅ |
| 84 | BookSummaryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 85 | BookSummaryOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | ✅ |
| 86 | BookSummaryPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 87 | BookSummaryPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 88 | BookSummaryPeriodNum | PERIOD_NUM | — | ✅ |
| 89 | BookSummaryPolishAdjRecCost | POLISH_ADJ_REC_COST | — | ✅ |
| 90 | BookSummaryPolishDeprnBasis | POLISH_DEPRN_BASIS | — | ✅ |
| 91 | BookSummaryProduction | PRODUCTION | — | — |
| 92 | BookSummaryProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 93 | BookSummaryRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | ✅ |
| 94 | BookSummaryRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 95 | BookSummaryRemainingLife1 | REMAINING_LIFE1 | — | ✅ |
| 96 | BookSummaryRemainingLife2 | REMAINING_LIFE2 | — | ✅ |
| 97 | BookSummaryReserveAdjustmentAmount | RESERVE_ADJUSTMENT_AMOUNT | — | ✅ |
| 98 | BookSummaryReserveRetAdjAmount | RESERVE_RET_ADJ_AMOUNT | — | ✅ |
| 99 | BookSummaryResetAdjustedCostFlag | RESET_ADJUSTED_COST_FLAG | — | ✅ |
| 100 | BookSummaryRevalAmortBalance | REVAL_AMORT_BALANCE | — | ✅ |
| 101 | BookSummaryRevalAmortization | REVAL_AMORTIZATION | — | — |
| 102 | BookSummaryRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 103 | BookSummaryRevalCeiling | REVAL_CEILING | — | — |
| 104 | BookSummaryRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | — |
| 105 | BookSummaryRevalLossBalance | REVAL_LOSS_BALANCE | — | ✅ |
| 106 | BookSummaryRevalReserve | REVAL_RESERVE | — | — |
| 107 | BookSummaryRevalReserveAdjAmount | REVAL_RESERVE_ADJ_AMOUNT | — | ✅ |
| 108 | BookSummaryRevalReserveRetAdjAmount | REVAL_RESERVE_RET_ADJ_AMOUNT | — | ✅ |
| 109 | BookSummarySalvageType | SALVAGE_TYPE | — | ✅ |
| 110 | BookSummarySalvageValue | SALVAGE_VALUE | — | ✅ |
| 111 | BookSummaryShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | ✅ |
| 112 | BookSummarySwitchCode | SWITCH_CODE | — | ✅ |
| 113 | BookSummarySystemBonusDeprnAmount | SYSTEM_BONUS_DEPRN_AMOUNT | — | ✅ |
| 114 | BookSummarySystemDeprnAmount | SYSTEM_DEPRN_AMOUNT | — | ✅ |
| 115 | BookSummaryTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | ✅ |
| 116 | BookSummaryTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | ✅ |
| 117 | BookSummaryTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 118 | BookSummaryTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 119 | BookSummaryUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 120 | BookSummaryUnplannedAmount | UNPLANNED_AMOUNT | — | — |
| 121 | BookSummaryUnrevaluedCost | UNREVALUED_COST | — | — |
| 122 | BookSummaryYtdCostOfRemoval | YTD_COST_OF_REMOVAL | — | ✅ |
| 123 | BookSummaryYtdDeprn | YTD_DEPRN | — | ✅ |
| 124 | BookSummaryYtdImpairment | YTD_IMPAIRMENT | — | ✅ |
| 125 | BookSummaryYtdProceedsOfSale | YTD_PROCEEDS_OF_SALE | — | ✅ |
| 126 | BookSummaryYtdProduction | YTD_PRODUCTION | — | — |
| 127 | BookSummaryYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
