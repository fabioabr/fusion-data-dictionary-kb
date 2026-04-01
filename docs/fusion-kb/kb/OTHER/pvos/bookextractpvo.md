---
id: DOC-OTHER-PVO-BookExtractPVO
doc_type: system-doc
title: "BookExtractPVO — PVO Cross-Module"
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
  - BookExtractPVO
  - bookextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BookExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Book Extract. Acessa as tabelas: FA_BOOKS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.BookExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 144 | 1 | 1 | 112 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[fa_books|FA_BOOKS]] — 144 atributos (1 PKs, 112 BICC)

---

## ⚙️ Atributos

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookAdjustedCapacity | ADJUSTED_CAPACITY | — | ✅ |
| 2 | BookAdjustedCost | ADJUSTED_COST | — | ✅ |
| 3 | BookAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | ✅ |
| 4 | BookAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | ✅ |
| 5 | BookAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | ✅ |
| 6 | BookAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 7 | BookAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 8 | BookAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | ✅ |
| 9 | BookAssetId | ASSET_ID | — | ✅ |
| 10 | BookBonusRuleId | BONUS_RULE_ID | — | ✅ |
| 11 | BookBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 12 | BookCapitalizeFlag | CAPITALIZE_FLAG | — | ✅ |
| 13 | BookCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | ✅ |
| 14 | BookCeilingTypeId | CEILING_TYPE_ID | — | ✅ |
| 15 | BookCipCost | CIP_COST | — | ✅ |
| 16 | BookContractId | CONTRACT_ID | — | ✅ |
| 17 | BookConventionTypeId | CONVENTION_TYPE_ID | — | ✅ |
| 18 | BookConversionDate | CONVERSION_DATE | — | ✅ |
| 19 | BookCost | COST | — | ✅ |
| 20 | BookCreatedBy | CREATED_BY | — | ✅ |
| 21 | BookCreationDate | CREATION_DATE | — | ✅ |
| 22 | BookDateEffective | DATE_EFFECTIVE | — | ✅ |
| 23 | BookDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 24 | BookDatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 25 | BookDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 26 | BookDepreciationOption | DEPRECIATION_OPTION | — | ✅ |
| 27 | BookDeprnAdjustmentFactor | DEPRN_ADJUSTMENT_FACTOR | — | ✅ |
| 28 | BookDeprnLimitType | DEPRN_LIMIT_TYPE | — | ✅ |
| 29 | BookDeprnStartDate | DEPRN_START_DATE | — | ✅ |
| 30 | BookDisabledFlag | DISABLED_FLAG | — | ✅ |
| 31 | BookDryHoleFlag | DRY_HOLE_FLAG | — | ✅ |
| 32 | BookEofyAdjCost | EOFY_ADJ_COST | — | ✅ |
| 33 | BookEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | ✅ |
| 34 | BookEofyReserve | EOFY_RESERVE | — | ✅ |
| 35 | BookEofyRevalReserve | EOFY_REVAL_RESERVE | — | — |
| 36 | BookEopAdjCost | EOP_ADJ_COST | — | ✅ |
| 37 | BookEopFormulaFactor | EOP_FORMULA_FACTOR | — | ✅ |
| 38 | BookExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | ✅ |
| 39 | BookExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | ✅ |
| 40 | BookExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | ✅ |
| 41 | BookExtendedDepreciationPeriod | EXTENDED_DEPRECIATION_PERIOD | — | ✅ |
| 42 | BookExtendedDeprnFlag | EXTENDED_DEPRN_FLAG | — | ✅ |
| 43 | BookFairMarketValue | FAIR_MARKET_VALUE | — | ✅ |
| 44 | BookFlatRateId | FLAT_RATE_ID | — | ✅ |
| 45 | BookFormulaFactor | FORMULA_FACTOR | — | ✅ |
| 46 | BookFullyReserveOnAddFlag | FULLY_RESERVE_ON_ADD_FLAG | — | ✅ |
| 47 | BookFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | ✅ |
| 48 | BookGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 49 | BookGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 50 | BookGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 51 | BookGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 52 | BookGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 53 | BookGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 54 | BookGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 55 | BookGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 56 | BookGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 57 | BookGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 58 | BookGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 59 | BookGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 60 | BookGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 61 | BookGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 62 | BookGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 63 | BookGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 64 | BookGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 65 | BookGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 66 | BookGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 67 | BookGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 68 | BookGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 69 | BookGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 70 | BookGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 71 | BookGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 72 | BookGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 73 | BookGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 74 | BookGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 75 | BookGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 76 | BookGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 77 | BookGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 78 | BookGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 79 | BookGroupAssetId | GROUP_ASSET_ID | — | ✅ |
| 80 | BookItcAmount | ITC_AMOUNT | — | ✅ |
| 81 | BookItcAmountId | ITC_AMOUNT_ID | — | ✅ |
| 82 | BookItcBasis | ITC_BASIS | — | ✅ |
| 83 | BookLastPriceIndexValue | LAST_PRICE_INDEX_VALUE | — | ✅ |
| 84 | BookLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | BookLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 86 | BookLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 87 | BookLeaseId | LEASE_ID | — | ✅ |
| 88 | BookLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | ✅ |
| 89 | BookLowValueAssetFlag | LOW_VALUE_ASSET_FLAG | — | ✅ |
| 90 | BookLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | ✅ |
| 91 | BookLtdProceeds | LTD_PROCEEDS | — | ✅ |
| 92 | BookMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | ✅ |
| 93 | BookMethodId | METHOD_ID | — | ✅ |
| 94 | BookNbvAtSwitch | NBV_AT_SWITCH | — | ✅ |
| 95 | BookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 96 | BookOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | ✅ |
| 97 | BookOldAdjustedCost | OLD_ADJUSTED_COST | — | ✅ |
| 98 | BookOriginalCost | ORIGINAL_COST | — | ✅ |
| 99 | BookOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | ✅ |
| 100 | BookOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | ✅ |
| 101 | BookPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 102 | BookPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | ✅ |
| 103 | BookPeriodCounterExtended | PERIOD_COUNTER_EXTENDED | — | ✅ |
| 104 | BookPeriodCounterFullyExtended | PERIOD_COUNTER_FULLY_EXTENDED | — | ✅ |
| 105 | BookPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | ✅ |
| 106 | BookPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | ✅ |
| 107 | BookPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | ✅ |
| 108 | BookPriorDeprnLimit | PRIOR_DEPRN_LIMIT | — | ✅ |
| 109 | BookPriorDeprnLimitAmount | PRIOR_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 110 | BookPriorDeprnLimitType | PRIOR_DEPRN_LIMIT_TYPE | — | ✅ |
| 111 | BookPriorEofyReserve | PRIOR_EOFY_RESERVE | — | ✅ |
| 112 | BookPriorFlatRateId | PRIOR_FLAT_RATE_ID | — | ✅ |
| 113 | BookPriorMethodId | PRIOR_METHOD_ID | — | ✅ |
| 114 | BookProductionCapacity | PRODUCTION_CAPACITY | — | ✅ |
| 115 | BookProrateDate | PRORATE_DATE | — | ✅ |
| 116 | BookRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | ✅ |
| 117 | BookRateInUse | RATE_IN_USE | — | ✅ |
| 118 | BookRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | ✅ |
| 119 | BookRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 120 | BookRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 121 | BookReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | ✅ |
| 122 | BookReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | ✅ |
| 123 | BookReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | ✅ |
| 124 | BookReductionRate | REDUCTION_RATE | — | ✅ |
| 125 | BookRemainingLife1 | REMAINING_LIFE1 | — | ✅ |
| 126 | BookRemainingLife2 | REMAINING_LIFE2 | — | ✅ |
| 127 | BookRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | ✅ |
| 128 | BookRetirementId | RETIREMENT_ID | — | ✅ |
| 129 | BookRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 130 | BookRevalCeiling | REVAL_CEILING | — | ✅ |
| 131 | BookRevaluedCost | REVALUED_COST | — | ✅ |
| 132 | BookSalvageType | SALVAGE_TYPE | — | ✅ |
| 133 | BookSalvageValue | SALVAGE_VALUE | — | ✅ |
| 134 | BookShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | ✅ |
| 135 | BookTerminalGainLoss | TERMINAL_GAIN_LOSS | — | ✅ |
| 136 | BookTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | ✅ |
| 137 | BookTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | ✅ |
| 138 | BookTrackingMethod | TRACKING_METHOD | — | ✅ |
| 139 | BookTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |
| 140 | BookTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 141 | BookUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 142 | BookUnrevaluedCost | UNREVALUED_COST | — | ✅ |
| 143 | BookUseBooksSummaryFlag | USE_BOOKS_SUMMARY_FLAG | — | ✅ |
| 144 | BookYtdProceeds | YTD_PROCEEDS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
