---
id: DOC-OTHER-PVO-AdjustmentPVO
doc_type: system-doc
title: "AdjustmentPVO — PVO Cross-Module"
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
  - AdjustmentPVO
  - adjustmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment. Acessa as tabelas: FA_ADDITIONS_B, FA_ADJUSTMENTS, FA_ASSET_HISTORY (+10).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.AdjustmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 599 | 13 | 3 | 34 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 132 atributos
- [[fa_adjustments|FA_ADJUSTMENTS]] — 25 atributos (2 PKs, 13 BICC)
- [[fa_asset_history|FA_ASSET_HISTORY]] — 14 atributos (1 PKs, 4 BICC)
- [[fa_books|FA_BOOKS]] — 81 atributos
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (2 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 16 atributos (4 BICC)
- [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]] — 19 atributos (6 BICC)
- [[fa_flat_rates|FA_FLAT_RATES]] — 5 atributos
- [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]] — 4 atributos
- [[fa_methods|FA_METHODS]] — 13 atributos
- [[fa_retirements|FA_RETIREMENTS]] — 111 atributos (2 BICC)
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 78 atributos (3 BICC)
- [[fa_trx_references|FA_TRX_REFERENCES]] — 20 atributos

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetId | ASSET_ID | — | — |
| 3 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | AdditionAssetNumber | ASSET_NUMBER | — | — |
| 5 | AdditionAssetType | ASSET_TYPE | — | — |
| 6 | AdditionCommitment | COMMITMENT | — | — |
| 7 | AdditionContext | CONTEXT | — | — |
| 8 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 9 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 10 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 11 | AdditionInventorial | INVENTORIAL | — | — |
| 12 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 13 | AdditionLeaseId | LEASE_ID | — | — |
| 14 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 15 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 16 | AdditionNewUsed | NEW_USED | — | — |
| 17 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 18 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 19 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 20 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 21 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 22 | AdditionTagNumber | TAG_NUMBER | — | — |
| 23 | AssetAdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 24 | AssetAdditionAssetId | ASSET_ID | — | — |
| 25 | AssetAdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 26 | AssetAdditionAssetNumber | ASSET_NUMBER | — | — |
| 27 | AssetAdditionAssetType | ASSET_TYPE | — | — |
| 28 | AssetAdditionCommitment | COMMITMENT | — | — |
| 29 | AssetAdditionContext | CONTEXT | — | — |
| 30 | AssetAdditionCurrentUnits | CURRENT_UNITS | — | — |
| 31 | AssetAdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 32 | AssetAdditionInUseFlag | IN_USE_FLAG | — | — |
| 33 | AssetAdditionInventorial | INVENTORIAL | — | — |
| 34 | AssetAdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 35 | AssetAdditionLeaseId | LEASE_ID | — | — |
| 36 | AssetAdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 37 | AssetAdditionModelNumber | MODEL_NUMBER | — | — |
| 38 | AssetAdditionNewUsed | NEW_USED | — | — |
| 39 | AssetAdditionOwnedLeased | OWNED_LEASED | — | — |
| 40 | AssetAdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 41 | AssetAdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 42 | AssetAdditionPrntAssetId | ASSET_ID | — | — |
| 43 | AssetAdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 44 | AssetAdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 45 | AssetAdditionPrntAssetType | ASSET_TYPE | — | — |
| 46 | AssetAdditionPrntCommitment | COMMITMENT | — | — |
| 47 | AssetAdditionPrntContext | CONTEXT | — | — |
| 48 | AssetAdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 49 | AssetAdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 50 | AssetAdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 51 | AssetAdditionPrntInventorial | INVENTORIAL | — | — |
| 52 | AssetAdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 53 | AssetAdditionPrntLeaseId | LEASE_ID | — | — |
| 54 | AssetAdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 55 | AssetAdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 56 | AssetAdditionPrntNewUsed | NEW_USED | — | — |
| 57 | AssetAdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 58 | AssetAdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 59 | AssetAdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 60 | AssetAdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 61 | AssetAdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 62 | AssetAdditionPrntTagNumber | TAG_NUMBER | — | — |
| 63 | AssetAdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 64 | AssetAdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 65 | AssetAdditionSerialNumber | SERIAL_NUMBER | — | — |
| 66 | AssetAdditionTagNumber | TAG_NUMBER | — | — |
| 67 | DistAdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 68 | DistAdditionPrntAssetId | ASSET_ID | — | — |
| 69 | DistAdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 70 | DistAdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 71 | DistAdditionPrntAssetType | ASSET_TYPE | — | — |
| 72 | DistAdditionPrntCommitment | COMMITMENT | — | — |
| 73 | DistAdditionPrntContext | CONTEXT | — | — |
| 74 | DistAdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 75 | DistAdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 76 | DistAdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 77 | DistAdditionPrntInventorial | INVENTORIAL | — | — |
| 78 | DistAdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 79 | DistAdditionPrntLeaseId | LEASE_ID | — | — |
| 80 | DistAdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 81 | DistAdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 82 | DistAdditionPrntNewUsed | NEW_USED | — | — |
| 83 | DistAdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 84 | DistAdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 85 | DistAdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 86 | DistAdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 87 | DistAdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 88 | DistAdditionPrntTagNumber | TAG_NUMBER | — | — |
| 89 | TrxnAdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 90 | TrxnAdditionAssetId | ASSET_ID | — | — |
| 91 | TrxnAdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 92 | TrxnAdditionAssetNumber | ASSET_NUMBER | — | — |
| 93 | TrxnAdditionAssetType | ASSET_TYPE | — | — |
| 94 | TrxnAdditionCommitment | COMMITMENT | — | — |
| 95 | TrxnAdditionContext | CONTEXT | — | — |
| 96 | TrxnAdditionCurrentUnits | CURRENT_UNITS | — | — |
| 97 | TrxnAdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 98 | TrxnAdditionInUseFlag | IN_USE_FLAG | — | — |
| 99 | TrxnAdditionInventorial | INVENTORIAL | — | — |
| 100 | TrxnAdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 101 | TrxnAdditionLeaseId | LEASE_ID | — | — |
| 102 | TrxnAdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 103 | TrxnAdditionModelNumber | MODEL_NUMBER | — | — |
| 104 | TrxnAdditionNewUsed | NEW_USED | — | — |
| 105 | TrxnAdditionOwnedLeased | OWNED_LEASED | — | — |
| 106 | TrxnAdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 107 | TrxnAdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 108 | TrxnAdditionPrntAssetId | ASSET_ID | — | — |
| 109 | TrxnAdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 110 | TrxnAdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 111 | TrxnAdditionPrntAssetType | ASSET_TYPE | — | — |
| 112 | TrxnAdditionPrntCommitment | COMMITMENT | — | — |
| 113 | TrxnAdditionPrntContext | CONTEXT | — | — |
| 114 | TrxnAdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 115 | TrxnAdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 116 | TrxnAdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 117 | TrxnAdditionPrntInventorial | INVENTORIAL | — | — |
| 118 | TrxnAdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 119 | TrxnAdditionPrntLeaseId | LEASE_ID | — | — |
| 120 | TrxnAdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 121 | TrxnAdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 122 | TrxnAdditionPrntNewUsed | NEW_USED | — | — |
| 123 | TrxnAdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 124 | TrxnAdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 125 | TrxnAdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 126 | TrxnAdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 127 | TrxnAdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 128 | TrxnAdditionPrntTagNumber | TAG_NUMBER | — | — |
| 129 | TrxnAdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 130 | TrxnAdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 131 | TrxnAdditionSerialNumber | SERIAL_NUMBER | — | — |
| 132 | TrxnAdditionTagNumber | TAG_NUMBER | — | — |

### [[fa_adjustments|FA_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 3 | AdjustmentAnnualizedAdjustment | ANNUALIZED_ADJUSTMENT | — | — |
| 4 | AdjustmentAssetId | ASSET_ID | — | ✅ |
| 5 | AdjustmentAssetInvoiceId | ASSET_INVOICE_ID | — | — |
| 6 | AdjustmentBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 7 | AdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 8 | AdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 9 | AdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 10 | AdjustmentDebitCreditFlag | DEBIT_CREDIT_FLAG | — | ✅ |
| 11 | AdjustmentDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | — |
| 12 | AdjustmentDistributionId | DISTRIBUTION_ID | — | — |
| 13 | AdjustmentInsertionOrder | INSERTION_ORDER | — | — |
| 14 | AdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | AdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | AdjustmentLineId | ADJUSTMENT_LINE_ID | 🔑 | ✅ |
| 18 | AdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | AdjustmentPeriodCounterAdjusted | PERIOD_COUNTER_ADJUSTED | — | ✅ |
| 20 | AdjustmentPeriodCounterCreated | PERIOD_COUNTER_CREATED | — | — |
| 21 | AdjustmentSourceDestCode | SOURCE_DEST_CODE | — | — |
| 22 | AdjustmentSourceLineId | SOURCE_LINE_ID | — | — |
| 23 | AdjustmentSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 24 | AdjustmentTrackMemberFlag | TRACK_MEMBER_FLAG | — | — |
| 25 | TransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

### [[fa_asset_history|FA_ASSET_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaAstHistAssetId | ASSET_ID | — | — |
| 2 | FaAstHistAssetType | ASSET_TYPE | — | — |
| 3 | FaAstHistCategoryId | CATEGORY_ID | — | ✅ |
| 4 | FaAstHistCreatedBy | CREATED_BY | — | — |
| 5 | FaAstHistCreationDate | CREATION_DATE | — | — |
| 6 | FaAstHistDateEffective | DATE_EFFECTIVE | — | — |
| 7 | FaAstHistDateIneffective | DATE_INEFFECTIVE | — | — |
| 8 | FaAstHistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | FaAstHistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | FaAstHistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | FaAstHistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | FaAstHistTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |
| 13 | FaAstHistTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 14 | FaAstHistUnits | UNITS | — | — |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaBooksAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 2 | FaBooksAdjustedCost | ADJUSTED_COST | — | — |
| 3 | FaBooksAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 4 | FaBooksAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 5 | FaBooksAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 6 | FaBooksAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 7 | FaBooksAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | — |
| 8 | FaBooksAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 9 | FaBooksAssetId | ASSET_ID | — | — |
| 10 | FaBooksBonusRuleId | BONUS_RULE_ID | — | — |
| 11 | FaBooksBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | FaBooksCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 13 | FaBooksCeilingTypeId | CEILING_TYPE_ID | — | — |
| 14 | FaBooksCipCost | CIP_COST | — | — |
| 15 | FaBooksConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 16 | FaBooksConversionDate | CONVERSION_DATE | — | — |
| 17 | FaBooksCost | COST | — | — |
| 18 | FaBooksDateEffective | DATE_EFFECTIVE | — | — |
| 19 | FaBooksDateIneffective | DATE_INEFFECTIVE | — | — |
| 20 | FaBooksDatePlacedInService | DATE_PLACED_IN_SERVICE | — | — |
| 21 | FaBooksDepreciateFlag | DEPRECIATE_FLAG | — | — |
| 22 | FaBooksDepreciationOption | DEPRECIATION_OPTION | — | — |
| 23 | FaBooksDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 24 | FaBooksDeprnStartDate | DEPRN_START_DATE | — | — |
| 25 | FaBooksDisabledFlag | DISABLED_FLAG | — | — |
| 26 | FaBooksEofyAdjCost | EOFY_ADJ_COST | — | — |
| 27 | FaBooksEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 28 | FaBooksEofyReserve | EOFY_RESERVE | — | — |
| 29 | FaBooksEopAdjCost | EOP_ADJ_COST | — | — |
| 30 | FaBooksEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 31 | FaBooksExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 32 | FaBooksExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 33 | FaBooksExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 34 | FaBooksFlatRateId | FLAT_RATE_ID | — | — |
| 35 | FaBooksFormulaFactor | FORMULA_FACTOR | — | — |
| 36 | FaBooksFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 37 | FaBooksGroupAssetId | GROUP_ASSET_ID | — | — |
| 38 | FaBooksLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 39 | FaBooksLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 40 | FaBooksLtdProceeds | LTD_PROCEEDS | — | — |
| 41 | FaBooksMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 42 | FaBooksMethodId | METHOD_ID | — | — |
| 43 | FaBooksOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 44 | FaBooksOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 45 | FaBooksOriginalCost | ORIGINAL_COST | — | — |
| 46 | FaBooksOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 47 | FaBooksOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 48 | FaBooksPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | — |
| 49 | FaBooksPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 50 | FaBooksPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 51 | FaBooksPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 52 | FaBooksPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 53 | FaBooksPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 54 | FaBooksProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 55 | FaBooksProrateDate | PRORATE_DATE | — | — |
| 56 | FaBooksRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 57 | FaBooksRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 58 | FaBooksRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 59 | FaBooksRecoverableCost | RECOVERABLE_COST | — | — |
| 60 | FaBooksReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 61 | FaBooksReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 62 | FaBooksReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 63 | FaBooksReductionRate | REDUCTION_RATE | — | — |
| 64 | FaBooksRemainingLife1 | REMAINING_LIFE1 | — | — |
| 65 | FaBooksRemainingLife2 | REMAINING_LIFE2 | — | — |
| 66 | FaBooksRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 67 | FaBooksRetirementId | RETIREMENT_ID | — | — |
| 68 | FaBooksRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 69 | FaBooksRevalCeiling | REVAL_CEILING | — | — |
| 70 | FaBooksSalvageType | SALVAGE_TYPE | — | — |
| 71 | FaBooksSalvageValue | SALVAGE_VALUE | — | — |
| 72 | FaBooksShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |
| 73 | FaBooksTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 74 | FaBooksTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 75 | FaBooksTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 76 | FaBooksTrackingMethod | TRACKING_METHOD | — | — |
| 77 | FaBooksTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 78 | FaBooksTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 79 | FaBooksUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 80 | FaBooksUnrevaluedCost | UNREVALUED_COST | — | — |
| 81 | FaBooksYtdProceeds | YTD_PROCEEDS | — | — |

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
| 20 | BkCtrlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 21 | BkCtrlBookTypeName | BOOK_TYPE_NAME | — | — |
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
| 80 | BkCtrlSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 81 | BkCtrlUsePercentSalvageValueFlag | USE_PERCENT_SALVAGE_VALUE_FLAG | — | — |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPeriodCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | ✅ |
| 3 | DeprnPeriodCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 4 | DeprnPeriodCreatedBy | CREATED_BY | — | — |
| 5 | DeprnPeriodCreationDate | CREATION_DATE | — | — |
| 6 | DeprnPeriodDeprnRun | DEPRN_RUN | — | — |
| 7 | DeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 8 | DeprnPeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DeprnPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | DeprnPeriodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | DeprnPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | DeprnPeriodPeriodCloseDate | PERIOD_CLOSE_DATE | — | ✅ |
| 13 | DeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 14 | DeprnPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 15 | DeprnPeriodPeriodNum | PERIOD_NUM | — | — |
| 16 | DeprnPeriodPeriodOpenDate | PERIOD_OPEN_DATE | — | — |

### [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistHistAssetId | ASSET_ID | — | — |
| 2 | DistHistAssignedTo | ASSIGNED_TO | — | ✅ |
| 3 | DistHistBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | DistHistCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 5 | DistHistCreatedBy | CREATED_BY | — | — |
| 6 | DistHistCreationDate | CREATION_DATE | — | — |
| 7 | DistHistDateEffective | DATE_EFFECTIVE | — | — |
| 8 | DistHistDateIneffective | DATE_INEFFECTIVE | — | — |
| 9 | DistHistDistributionId | DISTRIBUTION_ID | — | — |
| 10 | DistHistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DistHistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DistHistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | DistHistLocationId | LOCATION_ID | — | ✅ |
| 14 | DistHistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DistHistRetirementId | RETIREMENT_ID | — | — |
| 16 | DistHistTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 17 | DistHistTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 18 | DistHistTransactionUnits | TRANSACTION_UNITS | — | — |
| 19 | DistHistUnitsAssigned | UNITS_ASSIGNED | — | ✅ |

### [[fa_flat_rates|FA_FLAT_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlatRateAdjustedRate | ADJUSTED_RATE | — | — |
| 2 | FlatRateAdjustingRate | ADJUSTING_RATE | — | — |
| 3 | FlatRateBasicRate | BASIC_RATE | — | — |
| 4 | FlatRateFlatRateId | FLAT_RATE_ID | — | — |
| 5 | FlatRateMethodId | METHOD_ID | — | — |

### [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTrxnBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | InvTrxnDateEffective | DATE_EFFECTIVE | — | — |
| 3 | InvTrxnInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 4 | InvTrxnTransactionType | TRANSACTION_TYPE | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationMethodDepreciateLastyearFlag | DEPRECIATE_LASTYEAR_FLAG | — | — |
| 2 | DepreciationMethodDeprnBasisRule | DEPRN_BASIS_RULE | — | — |
| 3 | DepreciationMethodDeprnBasisRuleId | DEPRN_BASIS_RULE_ID | — | — |
| 4 | DepreciationMethodExcludeSalvageValueFlag | EXCLUDE_SALVAGE_VALUE_FLAG | — | — |
| 5 | DepreciationMethodLifeInMonths | LIFE_IN_MONTHS | — | — |
| 6 | DepreciationMethodMethodCode | METHOD_CODE | — | — |
| 7 | DepreciationMethodMethodId | METHOD_ID | — | — |
| 8 | DepreciationMethodName | NAME | — | — |
| 9 | DepreciationMethodPolishAdjCalcBasisFlag | POLISH_ADJ_CALC_BASIS_FLAG | — | — |
| 10 | DepreciationMethodProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 11 | DepreciationMethodRateSourceRule | RATE_SOURCE_RULE | — | — |
| 12 | DepreciationMethodSetId | SET_ID | — | — |
| 13 | DepreciationMethodStlMethodFlag | STL_METHOD_FLAG | — | — |

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
| 13 | RetirementInAssetId | ASSET_ID | — | — |
| 14 | RetirementInBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 15 | RetirementInBookTypeCode | BOOK_TYPE_CODE | — | — |
| 16 | RetirementInCostOfRemoval | COST_OF_REMOVAL | — | — |
| 17 | RetirementInCostRetired | COST_RETIRED | — | — |
| 18 | RetirementInCreatedBy | CREATED_BY | — | — |
| 19 | RetirementInCreationDate | CREATION_DATE | — | — |
| 20 | RetirementInDateEffective | DATE_EFFECTIVE | — | — |
| 21 | RetirementInDateRetired | DATE_RETIRED | — | — |
| 22 | RetirementInEofyReserve | EOFY_RESERVE | — | — |
| 23 | RetirementInGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 24 | RetirementInGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 25 | RetirementInLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | RetirementInLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | RetirementInLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | RetirementInLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 29 | RetirementInNbvRetired | NBV_RETIRED | — | — |
| 30 | RetirementInObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | RetirementInProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 32 | RetirementInRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 33 | RetirementInRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 34 | RetirementInRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 35 | RetirementInReductionRate | REDUCTION_RATE | — | — |
| 36 | RetirementInReferenceNum | REFERENCE_NUM | — | — |
| 37 | RetirementInReserveRetired | RESERVE_RETIRED | — | — |
| 38 | RetirementInRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 39 | RetirementInRetirementId | RETIREMENT_ID | — | — |
| 40 | RetirementInRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 41 | RetirementInRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 42 | RetirementInSoldTo | SOLD_TO | — | — |
| 43 | RetirementInStatus | STATUS | — | — |
| 44 | RetirementInStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 45 | RetirementInStlMethodId | STL_METHOD_ID | — | — |
| 46 | RetirementInTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 47 | RetirementInTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 48 | RetirementInTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 49 | RetirementInTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 50 | RetirementInUnits | UNITS | — | — |
| 51 | RetirementInUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |
| 52 | RetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | RetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | RetirementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 56 | RetirementNbvRetired | NBV_RETIRED | — | — |
| 57 | RetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 59 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 60 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 61 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 62 | RetirementReductionRate | REDUCTION_RATE | — | — |
| 63 | RetirementReferenceNum | REFERENCE_NUM | — | — |
| 64 | RetirementReserveRetired | RESERVE_RETIRED | — | — |
| 65 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 66 | RetirementRetirementId | RETIREMENT_ID | — | — |
| 67 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 68 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 69 | RetirementSoldTo | SOLD_TO | — | — |
| 70 | RetirementStatus | STATUS | — | — |
| 71 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 72 | RetirementStlMethodId | STL_METHOD_ID | — | — |
| 73 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 74 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 75 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 76 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 77 | RetirementUnits | UNITS | — | — |
| 78 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |
| 79 | TrxRetirementAssetId | ASSET_ID | — | — |
| 80 | TrxRetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 81 | TrxRetirementBookTypeCode | BOOK_TYPE_CODE | — | — |
| 82 | TrxRetirementCostOfRemoval | COST_OF_REMOVAL | — | — |
| 83 | TrxRetirementCostRetired | COST_RETIRED | — | — |
| 84 | TrxRetirementDateEffective | DATE_EFFECTIVE | — | — |
| 85 | TrxRetirementDateRetired | DATE_RETIRED | — | — |
| 86 | TrxRetirementEofyReserve | EOFY_RESERVE | — | — |
| 87 | TrxRetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 88 | TrxRetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 89 | TrxRetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 90 | TrxRetirementNbvRetired | NBV_RETIRED | — | — |
| 91 | TrxRetirementProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 92 | TrxRetirementRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 93 | TrxRetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 94 | TrxRetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 95 | TrxRetirementReductionRate | REDUCTION_RATE | — | — |
| 96 | TrxRetirementReferenceNum | REFERENCE_NUM | — | — |
| 97 | TrxRetirementReserveRetired | RESERVE_RETIRED | — | — |
| 98 | TrxRetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 99 | TrxRetirementRetirementId | RETIREMENT_ID | — | — |
| 100 | TrxRetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 101 | TrxRetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 102 | TrxRetirementSoldTo | SOLD_TO | — | — |
| 103 | TrxRetirementStatus | STATUS | — | — |
| 104 | TrxRetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 105 | TrxRetirementStlMethodId | STL_METHOD_ID | — | — |
| 106 | TrxRetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 107 | TrxRetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 108 | TrxRetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 109 | TrxRetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 110 | TrxRetirementUnits | UNITS | — | — |
| 111 | TrxRetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookInAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | BookInAssetId | ASSET_ID | — | — |
| 3 | BookInBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | BookInCallingInterface | CALLING_INTERFACE | — | — |
| 5 | BookInDateEffective | DATE_EFFECTIVE | — | — |
| 6 | BookInEventId | EVENT_ID | — | — |
| 7 | BookInInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 8 | BookInMassReferenceId | MASS_REFERENCE_ID | — | — |
| 9 | BookInMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 10 | BookInMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 11 | BookInSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 12 | BookInTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 13 | BookInTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 14 | BookInTransactionKey | TRANSACTION_KEY | — | — |
| 15 | BookInTransactionName | TRANSACTION_NAME | — | — |
| 16 | BookInTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 17 | BookInTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 18 | BookInTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 19 | BookOutAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 20 | BookOutAssetId | ASSET_ID | — | — |
| 21 | BookOutBookTypeCode | BOOK_TYPE_CODE | — | — |
| 22 | BookOutCallingInterface | CALLING_INTERFACE | — | — |
| 23 | BookOutDateEffective | DATE_EFFECTIVE | — | — |
| 24 | BookOutEventId | EVENT_ID | — | — |
| 25 | BookOutInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 26 | BookOutMassReferenceId | MASS_REFERENCE_ID | — | — |
| 27 | BookOutMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 28 | BookOutMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 29 | BookOutSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 30 | BookOutTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 31 | BookOutTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 32 | BookOutTransactionKey | TRANSACTION_KEY | — | — |
| 33 | BookOutTransactionName | TRANSACTION_NAME | — | — |
| 34 | BookOutTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 35 | BookOutTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 36 | BookOutTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 37 | FromTrxHdrAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 38 | FromTrxHdrAssetId | ASSET_ID | — | — |
| 39 | FromTrxHdrBookTypeCode | BOOK_TYPE_CODE | — | — |
| 40 | FromTrxHdrCallingInterface | CALLING_INTERFACE | — | — |
| 41 | FromTrxHdrDateEffective | DATE_EFFECTIVE | — | — |
| 42 | FromTrxHdrEventId | EVENT_ID | — | — |
| 43 | FromTrxHdrInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 44 | FromTrxHdrMassReferenceId | MASS_REFERENCE_ID | — | — |
| 45 | FromTrxHdrMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 46 | FromTrxHdrMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 47 | FromTrxHdrSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 48 | FromTrxHdrTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 49 | FromTrxHdrTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 50 | FromTrxHdrTransactionKey | TRANSACTION_KEY | — | — |
| 51 | FromTrxHdrTransactionName | TRANSACTION_NAME | — | — |
| 52 | FromTrxHdrTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 53 | FromTrxHdrTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 54 | FromTrxHdrTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 55 | TrxHeaderAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 56 | TrxHeaderAssetId | ASSET_ID | — | — |
| 57 | TrxHeaderBookTypeCode | BOOK_TYPE_CODE | — | — |
| 58 | TrxHeaderCallingInterface | CALLING_INTERFACE | — | — |
| 59 | TrxHeaderCreatedBy | CREATED_BY | — | — |
| 60 | TrxHeaderCreationDate | CREATION_DATE | — | — |
| 61 | TrxHeaderDateEffective | DATE_EFFECTIVE | — | — |
| 62 | TrxHeaderEventId | EVENT_ID | — | — |
| 63 | TrxHeaderInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 64 | TrxHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | TrxHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | TrxHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | TrxHeaderMassReferenceId | MASS_REFERENCE_ID | — | — |
| 68 | TrxHeaderMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 69 | TrxHeaderMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 70 | TrxHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | TrxHeaderSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 72 | TrxHeaderTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | ✅ |
| 73 | TrxHeaderTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 74 | TrxHeaderTransactionKey | TRANSACTION_KEY | — | — |
| 75 | TrxHeaderTransactionName | TRANSACTION_NAME | — | — |
| 76 | TrxHeaderTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 77 | TrxHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 78 | TrxHeaderTrxReferenceId | TRX_REFERENCE_ID | — | — |

### [[fa_trx_references|FA_TRX_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxRefBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | TrxRefDestAmortizationStartDate | DEST_AMORTIZATION_START_DATE | — | — |
| 3 | TrxRefDestAssetId | DEST_ASSET_ID | — | — |
| 4 | TrxRefDestEofyReserve | DEST_EOFY_RESERVE | — | — |
| 5 | TrxRefDestExpenseAmount | DEST_EXPENSE_AMOUNT | — | — |
| 6 | TrxRefDestTransactionHeaderId | DEST_TRANSACTION_HEADER_ID | — | — |
| 7 | TrxRefDestTransactionSubtype | DEST_TRANSACTION_SUBTYPE | — | — |
| 8 | TrxRefEventId | EVENT_ID | — | — |
| 9 | TrxRefInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 10 | TrxRefMemberAssetId | MEMBER_ASSET_ID | — | — |
| 11 | TrxRefMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 12 | TrxRefReserveTransferAmount | RESERVE_TRANSFER_AMOUNT | — | — |
| 13 | TrxRefSrcAmortizationStartDate | SRC_AMORTIZATION_START_DATE | — | — |
| 14 | TrxRefSrcAssetId | SRC_ASSET_ID | — | — |
| 15 | TrxRefSrcEofyReserve | SRC_EOFY_RESERVE | — | — |
| 16 | TrxRefSrcExpenseAmount | SRC_EXPENSE_AMOUNT | — | — |
| 17 | TrxRefSrcTransactionHeaderId | SRC_TRANSACTION_HEADER_ID | — | — |
| 18 | TrxRefSrcTransactionSubtype | SRC_TRANSACTION_SUBTYPE | — | — |
| 19 | TrxRefTransactionType | TRANSACTION_TYPE | — | — |
| 20 | TrxRefTrxReferenceId | TRX_REFERENCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
