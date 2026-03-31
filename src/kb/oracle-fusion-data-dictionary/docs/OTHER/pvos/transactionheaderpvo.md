---
id: DOC-OTHER-PVO-TransactionHeaderPVO
doc_type: system-doc
title: "TransactionHeaderPVO — PVO Cross-Module"
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
  - TransactionHeaderPVO
  - transactionheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Header. Acessa as tabelas: FA_ADDITIONS_B, FA_ASSET_HISTORY, FA_BOOKS (+9).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.TransactionHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 579 | 12 | 1 | 37 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 82 atributos (5 BICC)
- [[fa_asset_history|FA_ASSET_HISTORY]] — 28 atributos (2 BICC)
- [[fa_books|FA_BOOKS]] — 174 atributos (4 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (3 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 12 atributos (1 BICC)
- [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]] — 8 atributos (1 BICC)
- [[fa_methods|FA_METHODS]] — 19 atributos
- [[fa_retirements|FA_RETIREMENTS]] — 39 atributos (1 BICC)
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 90 atributos (1 PKs, 17 BICC)
- [[fa_trx_references|FA_TRX_REFERENCES]] — 26 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddBaseAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AddBaseAssetId | ASSET_ID | — | — |
| 3 | AddBaseAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | AddBaseAssetNumber | ASSET_NUMBER | — | — |
| 5 | AddBaseAssetType | ASSET_TYPE | — | — |
| 6 | AddBaseCommitment | COMMITMENT | — | — |
| 7 | AddBaseContext | CONTEXT | — | — |
| 8 | AddBaseCreatedBy | CREATED_BY | — | — |
| 9 | AddBaseCreationDate | CREATION_DATE | — | — |
| 10 | AddBaseCurrentUnits | CURRENT_UNITS | — | — |
| 11 | AddBaseDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 12 | AddBaseInUseFlag | IN_USE_FLAG | — | — |
| 13 | AddBaseInventorial | INVENTORIAL | — | — |
| 14 | AddBaseInvestmentLaw | INVESTMENT_LAW | — | — |
| 15 | AddBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | AddBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AddBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AddBaseLeaseId | LEASE_ID | — | — |
| 19 | AddBaseManufacturerName | MANUFACTURER_NAME | — | — |
| 20 | AddBaseModelNumber | MODEL_NUMBER | — | — |
| 21 | AddBaseNewUsed | NEW_USED | — | — |
| 22 | AddBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AddBaseOwnedLeased | OWNED_LEASED | — | — |
| 24 | AddBaseParentAssetId | PARENT_ASSET_ID | — | — |
| 25 | AddBaseProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 26 | AddBasePropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 27 | AddBaseSerialNumber | SERIAL_NUMBER | — | — |
| 28 | AddBaseTagNumber | TAG_NUMBER | — | — |
| 29 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 30 | AdditionAssetId | ASSET_ID | — | — |
| 31 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 32 | AdditionAssetNumber | ASSET_NUMBER | — | ✅ |
| 33 | AdditionAssetType | ASSET_TYPE | — | — |
| 34 | AdditionCommitment | COMMITMENT | — | — |
| 35 | AdditionContext | CONTEXT | — | — |
| 36 | AdditionCreatedBy | CREATED_BY | — | — |
| 37 | AdditionCreationDate | CREATION_DATE | — | — |
| 38 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 39 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 40 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 41 | AdditionInventorial | INVENTORIAL | — | — |
| 42 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 43 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | AdditionLeaseId | LEASE_ID | — | — |
| 47 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 48 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 49 | AdditionNewUsed | NEW_USED | — | — |
| 50 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 52 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 53 | AdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 54 | AdditionPrntAssetId | ASSET_ID | — | — |
| 55 | AdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 56 | AdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 57 | AdditionPrntAssetType | ASSET_TYPE | — | — |
| 58 | AdditionPrntCommitment | COMMITMENT | — | — |
| 59 | AdditionPrntContext | CONTEXT | — | — |
| 60 | AdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 61 | AdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 62 | AdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 63 | AdditionPrntInventorial | INVENTORIAL | — | — |
| 64 | AdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 65 | AdditionPrntLeaseId | LEASE_ID | — | — |
| 66 | AdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 67 | AdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 68 | AdditionPrntNewUsed | NEW_USED | — | — |
| 69 | AdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 70 | AdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 71 | AdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 72 | AdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 73 | AdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 74 | AdditionPrntTagNumber | TAG_NUMBER | — | — |
| 75 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 76 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 77 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 78 | AdditionTagNumber | TAG_NUMBER | — | — |
| 79 | TrxRefDestAdditionAssetId | ASSET_ID | — | — |
| 80 | TrxRefDestAdditionAssetNumber | ASSET_NUMBER | — | ✅ |
| 81 | TrxRefSrcAdditionAssetId | ASSET_ID | — | — |
| 82 | TrxRefSrcAdditionAssetNumber | ASSET_NUMBER | — | ✅ |

### [[fa_asset_history|FA_ASSET_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NewFaHisAssetId | ASSET_ID | — | — |
| 2 | NewFaHisAssetType | ASSET_TYPE | — | — |
| 3 | NewFaHisCategoryId | CATEGORY_ID | — | — |
| 4 | NewFaHisCreatedBy | CREATED_BY | — | — |
| 5 | NewFaHisCreationDate | CREATION_DATE | — | — |
| 6 | NewFaHisDateEffective | DATE_EFFECTIVE | — | — |
| 7 | NewFaHisDateIneffective | DATE_INEFFECTIVE | — | — |
| 8 | NewFaHisLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | NewFaHisLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | NewFaHisLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | NewFaHisObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | NewFaHisTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 13 | NewFaHisTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 14 | NewFaHisUnits | UNITS | — | — |
| 15 | OldFaHisAssetId | ASSET_ID | — | — |
| 16 | OldFaHisAssetType | ASSET_TYPE | — | — |
| 17 | OldFaHisCategoryId | CATEGORY_ID | — | — |
| 18 | OldFaHisCreatedBy | CREATED_BY | — | — |
| 19 | OldFaHisCreationDate | CREATION_DATE | — | — |
| 20 | OldFaHisDateEffective | DATE_EFFECTIVE | — | — |
| 21 | OldFaHisDateIneffective | DATE_INEFFECTIVE | — | — |
| 22 | OldFaHisLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | OldFaHisLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | OldFaHisLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | OldFaHisObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | OldFaHisTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 27 | OldFaHisTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 28 | OldFaHisUnits | UNITS | — | — |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NewFaBookAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 2 | NewFaBookAdjustedCost | ADJUSTED_COST | — | — |
| 3 | NewFaBookAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 4 | NewFaBookAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 5 | NewFaBookAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 6 | NewFaBookAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 7 | NewFaBookAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | — |
| 8 | NewFaBookAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 9 | NewFaBookAssetId | ASSET_ID | — | — |
| 10 | NewFaBookBonusRuleId | BONUS_RULE_ID | — | — |
| 11 | NewFaBookBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | NewFaBookCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 13 | NewFaBookCeilingTypeId | CEILING_TYPE_ID | — | — |
| 14 | NewFaBookCipCost | CIP_COST | — | — |
| 15 | NewFaBookConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 16 | NewFaBookConversionDate | CONVERSION_DATE | — | — |
| 17 | NewFaBookCost | COST | — | ✅ |
| 18 | NewFaBookCreatedBy | CREATED_BY | — | — |
| 19 | NewFaBookCreationDate | CREATION_DATE | — | — |
| 20 | NewFaBookDateEffective | DATE_EFFECTIVE | — | — |
| 21 | NewFaBookDateIneffective | DATE_INEFFECTIVE | — | — |
| 22 | NewFaBookDatePlacedInService | DATE_PLACED_IN_SERVICE | — | — |
| 23 | NewFaBookDepreciateFlag | DEPRECIATE_FLAG | — | — |
| 24 | NewFaBookDepreciationOption | DEPRECIATION_OPTION | — | — |
| 25 | NewFaBookDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 26 | NewFaBookDeprnStartDate | DEPRN_START_DATE | — | — |
| 27 | NewFaBookDisabledFlag | DISABLED_FLAG | — | — |
| 28 | NewFaBookEofyAdjCost | EOFY_ADJ_COST | — | — |
| 29 | NewFaBookEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 30 | NewFaBookEofyReserve | EOFY_RESERVE | — | — |
| 31 | NewFaBookEopAdjCost | EOP_ADJ_COST | — | — |
| 32 | NewFaBookEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 33 | NewFaBookExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 34 | NewFaBookExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 35 | NewFaBookExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 36 | NewFaBookFlatRateId | FLAT_RATE_ID | — | — |
| 37 | NewFaBookFormulaFactor | FORMULA_FACTOR | — | — |
| 38 | NewFaBookFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 39 | NewFaBookGroupAssetId | GROUP_ASSET_ID | — | — |
| 40 | NewFaBookLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | NewFaBookLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | NewFaBookLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | NewFaBookLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 44 | NewFaBookLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 45 | NewFaBookLtdProceeds | LTD_PROCEEDS | — | — |
| 46 | NewFaBookMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 47 | NewFaBookMethodId | METHOD_ID | — | — |
| 48 | NewFaBookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | NewFaBookOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 50 | NewFaBookOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 51 | NewFaBookOriginalCost | ORIGINAL_COST | — | — |
| 52 | NewFaBookOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 53 | NewFaBookOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 54 | NewFaBookPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | — |
| 55 | NewFaBookPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 56 | NewFaBookPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 57 | NewFaBookPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 58 | NewFaBookPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 59 | NewFaBookPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 60 | NewFaBookProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 61 | NewFaBookProrateDate | PRORATE_DATE | — | — |
| 62 | NewFaBookRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 63 | NewFaBookRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 64 | NewFaBookRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 65 | NewFaBookRecoverableCost | RECOVERABLE_COST | — | — |
| 66 | NewFaBookReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 67 | NewFaBookReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 68 | NewFaBookReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 69 | NewFaBookReductionRate | REDUCTION_RATE | — | — |
| 70 | NewFaBookRemainingLife1 | REMAINING_LIFE1 | — | — |
| 71 | NewFaBookRemainingLife2 | REMAINING_LIFE2 | — | — |
| 72 | NewFaBookRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 73 | NewFaBookRetirementId | RETIREMENT_ID | — | — |
| 74 | NewFaBookRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 75 | NewFaBookRevalCeiling | REVAL_CEILING | — | — |
| 76 | NewFaBookSalvageType | SALVAGE_TYPE | — | — |
| 77 | NewFaBookSalvageValue | SALVAGE_VALUE | — | — |
| 78 | NewFaBookShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |
| 79 | NewFaBookTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 80 | NewFaBookTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 81 | NewFaBookTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 82 | NewFaBookTrackingMethod | TRACKING_METHOD | — | — |
| 83 | NewFaBookTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 84 | NewFaBookTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 85 | NewFaBookUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 86 | NewFaBookUnrevaluedCost | UNREVALUED_COST | — | — |
| 87 | NewFaBookYtdProceeds | YTD_PROCEEDS | — | — |
| 88 | OldFaBookAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 89 | OldFaBookAdjustedCost | ADJUSTED_COST | — | — |
| 90 | OldFaBookAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 91 | OldFaBookAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 92 | OldFaBookAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 93 | OldFaBookAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 94 | OldFaBookAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | — |
| 95 | OldFaBookAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 96 | OldFaBookAssetId | ASSET_ID | — | — |
| 97 | OldFaBookBonusRuleId | BONUS_RULE_ID | — | — |
| 98 | OldFaBookBookTypeCode | BOOK_TYPE_CODE | — | — |
| 99 | OldFaBookCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 100 | OldFaBookCeilingTypeId | CEILING_TYPE_ID | — | — |
| 101 | OldFaBookCipCost | CIP_COST | — | — |
| 102 | OldFaBookConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 103 | OldFaBookConversionDate | CONVERSION_DATE | — | — |
| 104 | OldFaBookCost | COST | — | ✅ |
| 105 | OldFaBookCreatedBy | CREATED_BY | — | — |
| 106 | OldFaBookCreationDate | CREATION_DATE | — | — |
| 107 | OldFaBookDateEffective | DATE_EFFECTIVE | — | — |
| 108 | OldFaBookDateIneffective | DATE_INEFFECTIVE | — | — |
| 109 | OldFaBookDatePlacedInService | DATE_PLACED_IN_SERVICE | — | — |
| 110 | OldFaBookDepreciateFlag | DEPRECIATE_FLAG | — | — |
| 111 | OldFaBookDepreciationOption | DEPRECIATION_OPTION | — | — |
| 112 | OldFaBookDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 113 | OldFaBookDeprnStartDate | DEPRN_START_DATE | — | — |
| 114 | OldFaBookDisabledFlag | DISABLED_FLAG | — | — |
| 115 | OldFaBookEofyAdjCost | EOFY_ADJ_COST | — | — |
| 116 | OldFaBookEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 117 | OldFaBookEofyReserve | EOFY_RESERVE | — | — |
| 118 | OldFaBookEopAdjCost | EOP_ADJ_COST | — | — |
| 119 | OldFaBookEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 120 | OldFaBookExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 121 | OldFaBookExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 122 | OldFaBookExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 123 | OldFaBookFlatRateId | FLAT_RATE_ID | — | — |
| 124 | OldFaBookFormulaFactor | FORMULA_FACTOR | — | — |
| 125 | OldFaBookFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 126 | OldFaBookGroupAssetId | GROUP_ASSET_ID | — | — |
| 127 | OldFaBookLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 128 | OldFaBookLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 129 | OldFaBookLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 130 | OldFaBookLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 131 | OldFaBookLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 132 | OldFaBookLtdProceeds | LTD_PROCEEDS | — | — |
| 133 | OldFaBookMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 134 | OldFaBookMethodId | METHOD_ID | — | — |
| 135 | OldFaBookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 136 | OldFaBookOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 137 | OldFaBookOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 138 | OldFaBookOriginalCost | ORIGINAL_COST | — | — |
| 139 | OldFaBookOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 140 | OldFaBookOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 141 | OldFaBookPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | — |
| 142 | OldFaBookPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 143 | OldFaBookPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 144 | OldFaBookPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 145 | OldFaBookPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 146 | OldFaBookPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 147 | OldFaBookProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 148 | OldFaBookProrateDate | PRORATE_DATE | — | — |
| 149 | OldFaBookRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 150 | OldFaBookRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 151 | OldFaBookRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 152 | OldFaBookRecoverableCost | RECOVERABLE_COST | — | — |
| 153 | OldFaBookReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 154 | OldFaBookReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 155 | OldFaBookReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 156 | OldFaBookReductionRate | REDUCTION_RATE | — | — |
| 157 | OldFaBookRemainingLife1 | REMAINING_LIFE1 | — | — |
| 158 | OldFaBookRemainingLife2 | REMAINING_LIFE2 | — | — |
| 159 | OldFaBookRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 160 | OldFaBookRetirementId | RETIREMENT_ID | — | — |
| 161 | OldFaBookRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 162 | OldFaBookRevalCeiling | REVAL_CEILING | — | — |
| 163 | OldFaBookSalvageType | SALVAGE_TYPE | — | — |
| 164 | OldFaBookSalvageValue | SALVAGE_VALUE | — | — |
| 165 | OldFaBookShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |
| 166 | OldFaBookTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 167 | OldFaBookTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 168 | OldFaBookTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 169 | OldFaBookTrackingMethod | TRACKING_METHOD | — | — |
| 170 | OldFaBookTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 171 | OldFaBookTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 172 | OldFaBookUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 173 | OldFaBookUnrevaluedCost | UNREVALUED_COST | — | — |
| 174 | OldFaBookYtdProceeds | YTD_PROCEEDS | — | — |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BkCtrlAccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | BkCtrlAllowBackdatedTransfersFlag | ALLOW_BACKDATED_TRANSFERS_FLAG | — | — |
| 3 | BkCtrlAllowCipAssetsFlag | ALLOW_CIP_ASSETS_FLAG | — | — |
| 4 | BkCtrlAllowCipDepGroupFlag | ALLOW_CIP_DEP_GROUP_FLAG | — | — |
| 5 | BkCtrlAllowCipMemberFlag | ALLOW_CIP_MEMBER_FLAG | — | — |
| 6 | BkCtrlAllowCostCeiling | ALLOW_COST_CEILING | — | — |
| 7 | BkCtrlAllowCostSignChangeFlag | ALLOW_COST_SIGN_CHANGE_FLAG | — | — |
| 8 | BkCtrlAllowDeprnExpCeiling | ALLOW_DEPRN_EXP_CEILING | — | — |
| 9 | BkCtrlAllowGroupDeprnFlag | ALLOW_GROUP_DEPRN_FLAG | — | — |
| 10 | BkCtrlAllowIntercoGroupFlag | ALLOW_INTERCO_GROUP_FLAG | — | — |
| 11 | BkCtrlAllowMassChanges | ALLOW_MASS_CHANGES | — | — |
| 12 | BkCtrlAllowMassCopy | ALLOW_MASS_COPY | — | — |
| 13 | BkCtrlAllowMemberTrackingFlag | ALLOW_MEMBER_TRACKING_FLAG | — | — |
| 14 | BkCtrlAllowPurgeFlag | ALLOW_PURGE_FLAG | — | — |
| 15 | BkCtrlAllowRevalFlag | ALLOW_REVAL_FLAG | — | — |
| 16 | BkCtrlAmortizeFlag | AMORTIZE_FLAG | — | — |
| 17 | BkCtrlAmortizeRevalReserveFlag | AMORTIZE_REVAL_RESERVE_FLAG | — | — |
| 18 | BkCtrlBookClass | BOOK_CLASS | — | — |
| 19 | BkCtrlBookControlId | BOOK_CONTROL_ID | — | — |
| 20 | BkCtrlBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 21 | BkCtrlBookTypeName | BOOK_TYPE_NAME | — | ✅ |
| 22 | BkCtrlCapitalGainThreshold | CAPITAL_GAIN_THRESHOLD | — | — |
| 23 | BkCtrlCopyAdditionsFlag | COPY_ADDITIONS_FLAG | — | — |
| 24 | BkCtrlCopyAdjustmentsFlag | COPY_ADJUSTMENTS_FLAG | — | — |
| 25 | BkCtrlCopyGroupAdditionFlag | COPY_GROUP_ADDITION_FLAG | — | — |
| 26 | BkCtrlCopyGroupAssignmentFlag | COPY_GROUP_ASSIGNMENT_FLAG | — | — |
| 27 | BkCtrlCopyRetirementsFlag | COPY_RETIREMENTS_FLAG | — | — |
| 28 | BkCtrlCopySalvageValueFlag | COPY_SALVAGE_VALUE_FLAG | — | — |
| 29 | BkCtrlCostOfRemovalClearingAcct | COST_OF_REMOVAL_CLEARING_ACCT | — | — |
| 30 | BkCtrlCostOfRemovalGainAcct | COST_OF_REMOVAL_GAIN_ACCT | — | — |
| 31 | BkCtrlCostOfRemovalLossAcct | COST_OF_REMOVAL_LOSS_ACCT | — | — |
| 32 | BkCtrlCreateAccountingRequestId | CREATE_ACCOUNTING_REQUEST_ID | — | — |
| 33 | BkCtrlCreatedBy | CREATED_BY | — | — |
| 34 | BkCtrlCreationDate | CREATION_DATE | — | — |
| 35 | BkCtrlCurrentFiscalYear | CURRENT_FISCAL_YEAR | — | — |
| 36 | BkCtrlDateIneffective | DATE_INEFFECTIVE | — | — |
| 37 | BkCtrlDefaultLifeExtensionCeiling | DEFAULT_LIFE_EXTENSION_CEILING | — | — |
| 38 | BkCtrlDefaultLifeExtensionFactor | DEFAULT_LIFE_EXTENSION_FACTOR | — | — |
| 39 | BkCtrlDefaultMaxFullyRsvdRevals | DEFAULT_MAX_FULLY_RSVD_REVALS | — | — |
| 40 | BkCtrlDefaultRevalFullyRsvdFlag | DEFAULT_REVAL_FULLY_RSVD_FLAG | — | — |
| 41 | BkCtrlDeferredDeprnExpenseAcct | DEFERRED_DEPRN_EXPENSE_ACCT | — | — |
| 42 | BkCtrlDeferredDeprnReserveAcct | DEFERRED_DEPRN_RESERVE_ACCT | — | — |
| 43 | BkCtrlDeprFirstYearRetFlag | DEPR_FIRST_YEAR_RET_FLAG | — | — |
| 44 | BkCtrlDeprnAllocationCode | DEPRN_ALLOCATION_CODE | — | — |
| 45 | BkCtrlDeprnCalendar | DEPRN_CALENDAR | — | — |
| 46 | BkCtrlDeprnRequestId | DEPRN_REQUEST_ID | — | — |
| 47 | BkCtrlDeprnStatus | DEPRN_STATUS | — | — |
| 48 | BkCtrlDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 49 | BkCtrlFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 50 | BkCtrlFlexbuilderDefaultsCcid | FLEXBUILDER_DEFAULTS_CCID | — | — |
| 51 | BkCtrlFullyReservedFlag | FULLY_RESERVED_FLAG | — | — |
| 52 | BkCtrlGlPostingAllowedFlag | GL_POSTING_ALLOWED_FLAG | — | — |
| 53 | BkCtrlImmediateCopyFlag | IMMEDIATE_COPY_FLAG | — | — |
| 54 | BkCtrlInitialDate | INITIAL_DATE | — | — |
| 55 | BkCtrlInitialPeriodCounter | INITIAL_PERIOD_COUNTER | — | — |
| 56 | BkCtrlLastDeprnRunDate | LAST_DEPRN_RUN_DATE | — | — |
| 57 | BkCtrlLastMassCopyPeriodCounter | LAST_MASS_COPY_PERIOD_COUNTER | — | — |
| 58 | BkCtrlLastPeriodCounter | LAST_PERIOD_COUNTER | — | — |
| 59 | BkCtrlLastPurgePeriodCounter | LAST_PURGE_PERIOD_COUNTER | — | — |
| 60 | BkCtrlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | BkCtrlLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | BkCtrlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | BkCtrlMassCopySourceBook | MASS_COPY_SOURCE_BOOK | — | — |
| 64 | BkCtrlMassRequestId | MASS_REQUEST_ID | — | — |
| 65 | BkCtrlMcSourceFlag | MC_SOURCE_FLAG | — | — |
| 66 | BkCtrlNbvAmountThreshold | NBV_AMOUNT_THRESHOLD | — | — |
| 67 | BkCtrlNbvFractionThreshold | NBV_FRACTION_THRESHOLD | — | — |
| 68 | BkCtrlNbvRetiredGainAcct | NBV_RETIRED_GAIN_ACCT | — | — |
| 69 | BkCtrlNbvRetiredLossAcct | NBV_RETIRED_LOSS_ACCT | — | — |
| 70 | BkCtrlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | BkCtrlProceedsOfSaleClearingAcct | PROCEEDS_OF_SALE_CLEARING_ACCT | — | — |
| 72 | BkCtrlProceedsOfSaleGainAcct | PROCEEDS_OF_SALE_GAIN_ACCT | — | — |
| 73 | BkCtrlProceedsOfSaleLossAcct | PROCEEDS_OF_SALE_LOSS_ACCT | — | — |
| 74 | BkCtrlProrateCalendar | PRORATE_CALENDAR | — | — |
| 75 | BkCtrlRetireRevalReserveFlag | RETIRE_REVAL_RESERVE_FLAG | — | — |
| 76 | BkCtrlRevalDeprnReserveFlag | REVAL_DEPRN_RESERVE_FLAG | — | — |
| 77 | BkCtrlRevalRsvRetiredGainAcct | REVAL_RSV_RETIRED_GAIN_ACCT | — | — |
| 78 | BkCtrlRevalRsvRetiredLossAcct | REVAL_RSV_RETIRED_LOSS_ACCT | — | — |
| 79 | BkCtrlRevalYtdDeprnFlag | REVAL_YTD_DEPRN_FLAG | — | — |
| 80 | BkCtrlSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 81 | BkCtrlUsePercentSalvageValueFlag | USE_PERCENT_SALVAGE_VALUE_FLAG | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProrateConTypeConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateConTypeCreatedBy | CREATED_BY | — | — |
| 3 | ProrateConTypeCreationDate | CREATION_DATE | — | — |
| 4 | ProrateConTypeDeprWhenAcquiredFlag | DEPR_WHEN_ACQUIRED_FLAG | — | — |
| 5 | ProrateConTypeDescription | DESCRIPTION | — | — |
| 6 | ProrateConTypeFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 7 | ProrateConTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProrateConTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProrateConTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProrateConTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProrateConTypeProrateConventionCode | PRORATE_CONVENTION_CODE | — | — |
| 12 | ProrateConTypeSetId | SET_ID | — | — |

### [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTrxnBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | InvTrxnCreatedBy | CREATED_BY | — | — |
| 3 | InvTrxnDateEffective | DATE_EFFECTIVE | — | — |
| 4 | InvTrxnInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 5 | InvTrxnLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | InvTrxnLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | InvTrxnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | InvTrxnTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnMthdCreatedBy | CREATED_BY | — | — |
| 2 | DeprnMthdCreationDate | CREATION_DATE | — | — |
| 3 | DeprnMthdDepreciateLastyearFlag | DEPRECIATE_LASTYEAR_FLAG | — | — |
| 4 | DeprnMthdDeprnBasisRule | DEPRN_BASIS_RULE | — | — |
| 5 | DeprnMthdDeprnBasisRuleId | DEPRN_BASIS_RULE_ID | — | — |
| 6 | DeprnMthdExcludeSalvageValueFlag | EXCLUDE_SALVAGE_VALUE_FLAG | — | — |
| 7 | DeprnMthdLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | DeprnMthdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DeprnMthdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DeprnMthdLifeInMonths | LIFE_IN_MONTHS | — | — |
| 11 | DeprnMthdMethodCode | METHOD_CODE | — | — |
| 12 | DeprnMthdMethodId | METHOD_ID | — | — |
| 13 | DeprnMthdName | NAME | — | — |
| 14 | DeprnMthdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DeprnMthdPolishAdjCalcBasisFlag | POLISH_ADJ_CALC_BASIS_FLAG | — | — |
| 16 | DeprnMthdProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 17 | DeprnMthdRateSourceRule | RATE_SOURCE_RULE | — | — |
| 18 | DeprnMthdSetId | SET_ID | — | — |
| 19 | DeprnMthdStlMethodFlag | STL_METHOD_FLAG | — | — |

### [[fa_retirements|FA_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RetirementAssetId | ASSET_ID | — | — |
| 2 | RetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 3 | RetirementBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | RetirementCostOfRemoval | COST_OF_REMOVAL | — | — |
| 5 | RetirementCostRetired | COST_RETIRED | — | — |
| 6 | RetirementCreatedBy | CREATED_BY | — | — |
| 7 | RetirementCreationDate | CREATION_DATE | — | — |
| 8 | RetirementDateEffective | DATE_EFFECTIVE | — | — |
| 9 | RetirementDateRetired | DATE_RETIRED | — | — |
| 10 | RetirementEofyReserve | EOFY_RESERVE | — | — |
| 11 | RetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 12 | RetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 13 | RetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | RetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | RetirementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 17 | RetirementNbvRetired | NBV_RETIRED | — | — |
| 18 | RetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 20 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 21 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 22 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 23 | RetirementReductionRate | REDUCTION_RATE | — | — |
| 24 | RetirementReferenceNum | REFERENCE_NUM | — | — |
| 25 | RetirementReserveRetired | RESERVE_RETIRED | — | — |
| 26 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 27 | RetirementRetirementId | RETIREMENT_ID | — | — |
| 28 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 29 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 30 | RetirementSoldTo | SOLD_TO | — | — |
| 31 | RetirementStatus | STATUS | — | — |
| 32 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 33 | RetirementStlMethodId | STL_METHOD_ID | — | — |
| 34 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 35 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 36 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 37 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 38 | RetirementUnits | UNITS | — | — |
| 39 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemTrxnHeaderAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | MemTrxnHeaderAssetId | ASSET_ID | — | — |
| 3 | MemTrxnHeaderBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | MemTrxnHeaderCallingInterface | CALLING_INTERFACE | — | — |
| 5 | MemTrxnHeaderCreatedBy | CREATED_BY | — | — |
| 6 | MemTrxnHeaderCreationDate | CREATION_DATE | — | — |
| 7 | MemTrxnHeaderDateEffective | DATE_EFFECTIVE | — | — |
| 8 | MemTrxnHeaderEventId | EVENT_ID | — | — |
| 9 | MemTrxnHeaderInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 10 | MemTrxnHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | MemTrxnHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | MemTrxnHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | MemTrxnHeaderMassReferenceId | MASS_REFERENCE_ID | — | — |
| 14 | MemTrxnHeaderMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 15 | MemTrxnHeaderMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 16 | MemTrxnHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | MemTrxnHeaderSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 18 | MemTrxnHeaderTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 19 | MemTrxnHeaderTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 20 | MemTrxnHeaderTransactionKey | TRANSACTION_KEY | — | — |
| 21 | MemTrxnHeaderTransactionName | TRANSACTION_NAME | — | — |
| 22 | MemTrxnHeaderTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 23 | MemTrxnHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 24 | MemTrxnHeaderTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 25 | RetTrxHdrOutAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 26 | RetTrxHdrOutAssetId | ASSET_ID | — | — |
| 27 | RetTrxHdrOutBookTypeCode | BOOK_TYPE_CODE | — | — |
| 28 | RetTrxHdrOutCallingInterface | CALLING_INTERFACE | — | — |
| 29 | RetTrxHdrOutDateEffective | DATE_EFFECTIVE | — | — |
| 30 | RetTrxHdrOutEventId | EVENT_ID | — | — |
| 31 | RetTrxHdrOutInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 32 | RetTrxHdrOutMassReferenceId | MASS_REFERENCE_ID | — | — |
| 33 | RetTrxHdrOutMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 34 | RetTrxHdrOutMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 35 | RetTrxHdrOutSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 36 | RetTrxHdrOutTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 37 | RetTrxHdrOutTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 38 | RetTrxHdrOutTransactionKey | TRANSACTION_KEY | — | — |
| 39 | RetTrxHdrOutTransactionName | TRANSACTION_NAME | — | — |
| 40 | RetTrxHdrOutTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 41 | RetTrxHdrOutTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 42 | RetTrxHdrOutTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 43 | SrcTrxnHeaderAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 44 | SrcTrxnHeaderAssetId | ASSET_ID | — | — |
| 45 | SrcTrxnHeaderBookTypeCode | BOOK_TYPE_CODE | — | — |
| 46 | SrcTrxnHeaderCallingInterface | CALLING_INTERFACE | — | — |
| 47 | SrcTrxnHeaderCreatedBy | CREATED_BY | — | — |
| 48 | SrcTrxnHeaderCreationDate | CREATION_DATE | — | — |
| 49 | SrcTrxnHeaderDateEffective | DATE_EFFECTIVE | — | — |
| 50 | SrcTrxnHeaderEventId | EVENT_ID | — | — |
| 51 | SrcTrxnHeaderInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 52 | SrcTrxnHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | SrcTrxnHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | SrcTrxnHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | SrcTrxnHeaderMassReferenceId | MASS_REFERENCE_ID | — | — |
| 56 | SrcTrxnHeaderMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 57 | SrcTrxnHeaderMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 58 | SrcTrxnHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | SrcTrxnHeaderSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 60 | SrcTrxnHeaderTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 61 | SrcTrxnHeaderTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |
| 62 | SrcTrxnHeaderTransactionKey | TRANSACTION_KEY | — | — |
| 63 | SrcTrxnHeaderTransactionName | TRANSACTION_NAME | — | — |
| 64 | SrcTrxnHeaderTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 65 | SrcTrxnHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 66 | SrcTrxnHeaderTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 67 | TransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |
| 68 | TrxnHeaderAmortizationStartDate | AMORTIZATION_START_DATE | — | ✅ |
| 69 | TrxnHeaderAssetId | ASSET_ID | — | — |
| 70 | TrxnHeaderBookTypeCode | BOOK_TYPE_CODE | — | — |
| 71 | TrxnHeaderCallingInterface | CALLING_INTERFACE | — | — |
| 72 | TrxnHeaderCreatedBy | CREATED_BY | — | ✅ |
| 73 | TrxnHeaderCreationDate | CREATION_DATE | — | ✅ |
| 74 | TrxnHeaderDateEffective | DATE_EFFECTIVE | — | — |
| 75 | TrxnHeaderEventId | EVENT_ID | — | — |
| 76 | TrxnHeaderInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 77 | TrxnHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 78 | TrxnHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 79 | TrxnHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 80 | TrxnHeaderMassReferenceId | MASS_REFERENCE_ID | — | — |
| 81 | TrxnHeaderMassTransactionId | MASS_TRANSACTION_ID | — | ✅ |
| 82 | TrxnHeaderMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 83 | TrxnHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 84 | TrxnHeaderSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | ✅ |
| 85 | TrxnHeaderTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | ✅ |
| 86 | TrxnHeaderTransactionKey | TRANSACTION_KEY | — | ✅ |
| 87 | TrxnHeaderTransactionName | TRANSACTION_NAME | — | ✅ |
| 88 | TrxnHeaderTransactionSubtype | TRANSACTION_SUBTYPE | — | ✅ |
| 89 | TrxnHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 90 | TrxnHeaderTrxReferenceId | TRX_REFERENCE_ID | — | — |

### [[fa_trx_references|FA_TRX_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxRefBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | TrxRefCreatedBy | CREATED_BY | — | — |
| 3 | TrxRefCreationDate | CREATION_DATE | — | — |
| 4 | TrxRefDestAmortizationStartDate | DEST_AMORTIZATION_START_DATE | — | — |
| 5 | TrxRefDestAssetId | DEST_ASSET_ID | — | — |
| 6 | TrxRefDestEofyReserve | DEST_EOFY_RESERVE | — | — |
| 7 | TrxRefDestExpenseAmount | DEST_EXPENSE_AMOUNT | — | — |
| 8 | TrxRefDestTransactionHeaderId | DEST_TRANSACTION_HEADER_ID | — | — |
| 9 | TrxRefDestTransactionSubtype | DEST_TRANSACTION_SUBTYPE | — | — |
| 10 | TrxRefEventId | EVENT_ID | — | — |
| 11 | TrxRefInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 12 | TrxRefLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | TrxRefLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | TrxRefLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | TrxRefMemberAssetId | MEMBER_ASSET_ID | — | — |
| 16 | TrxRefMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 17 | TrxRefObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | TrxRefReserveTransferAmount | RESERVE_TRANSFER_AMOUNT | — | — |
| 19 | TrxRefSrcAmortizationStartDate | SRC_AMORTIZATION_START_DATE | — | — |
| 20 | TrxRefSrcAssetId | SRC_ASSET_ID | — | — |
| 21 | TrxRefSrcEofyReserve | SRC_EOFY_RESERVE | — | — |
| 22 | TrxRefSrcExpenseAmount | SRC_EXPENSE_AMOUNT | — | — |
| 23 | TrxRefSrcTransactionHeaderId | SRC_TRANSACTION_HEADER_ID | — | — |
| 24 | TrxRefSrcTransactionSubtype | SRC_TRANSACTION_SUBTYPE | — | — |
| 25 | TrxRefTransactionType | TRANSACTION_TYPE | — | — |
| 26 | TrxRefTrxReferenceId | TRX_REFERENCE_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
