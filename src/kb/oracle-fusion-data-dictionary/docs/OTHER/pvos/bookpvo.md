---
id: DOC-OTHER-PVO-BookPVO
doc_type: system-doc
title: "BookPVO — PVO Cross-Module"
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
  - BookPVO
  - bookpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BookPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Book. Acessa as tabelas: FA_ADDITIONS_B, FA_BONUS_RULES, FA_BOOKS (+8).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.BookPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 326 | 11 | 1 | 51 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 72 atributos (1 BICC)
- [[fa_bonus_rules|FA_BONUS_RULES]] — 5 atributos (2 BICC)
- [[fa_books|FA_BOOKS]] — 87 atributos (1 PKs, 22 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 3 atributos
- [[fa_ceiling_types|FA_CEILING_TYPES]] — 6 atributos (2 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 6 atributos (2 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 40 atributos (4 BICC)
- [[fa_flat_rates|FA_FLAT_RATES]] — 11 atributos (4 BICC)
- [[fa_methods|FA_METHODS]] — 20 atributos (9 BICC)
- [[fa_retirements|FA_RETIREMENTS]] — 33 atributos
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 43 atributos (5 BICC)

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
| 8 | AdditionCreatedBy | CREATED_BY | — | — |
| 9 | AdditionCreationDate | CREATION_DATE | — | — |
| 10 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 11 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 12 | AdditionGrpAsstAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 13 | AdditionGrpAsstAssetId | ASSET_ID | — | — |
| 14 | AdditionGrpAsstAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 15 | AdditionGrpAsstAssetNumber | ASSET_NUMBER | — | — |
| 16 | AdditionGrpAsstAssetType | ASSET_TYPE | — | — |
| 17 | AdditionGrpAsstCommitment | COMMITMENT | — | — |
| 18 | AdditionGrpAsstContext | CONTEXT | — | — |
| 19 | AdditionGrpAsstCurrentUnits | CURRENT_UNITS | — | — |
| 20 | AdditionGrpAsstDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 21 | AdditionGrpAsstInUseFlag | IN_USE_FLAG | — | — |
| 22 | AdditionGrpAsstInventorial | INVENTORIAL | — | — |
| 23 | AdditionGrpAsstInvestmentLaw | INVESTMENT_LAW | — | — |
| 24 | AdditionGrpAsstLeaseId | LEASE_ID | — | — |
| 25 | AdditionGrpAsstManufacturerName | MANUFACTURER_NAME | — | — |
| 26 | AdditionGrpAsstModelNumber | MODEL_NUMBER | — | — |
| 27 | AdditionGrpAsstNewUsed | NEW_USED | — | — |
| 28 | AdditionGrpAsstOwnedLeased | OWNED_LEASED | — | — |
| 29 | AdditionGrpAsstParentAssetId | PARENT_ASSET_ID | — | — |
| 30 | AdditionGrpAsstProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 31 | AdditionGrpAsstPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 32 | AdditionGrpAsstSerialNumber | SERIAL_NUMBER | — | — |
| 33 | AdditionGrpAsstTagNumber | TAG_NUMBER | — | — |
| 34 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 35 | AdditionInventorial | INVENTORIAL | — | — |
| 36 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 37 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | AdditionLeaseId | LEASE_ID | — | — |
| 41 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 42 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 43 | AdditionNewUsed | NEW_USED | — | — |
| 44 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 46 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 47 | AdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 48 | AdditionPrntAssetId | ASSET_ID | — | — |
| 49 | AdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 50 | AdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 51 | AdditionPrntAssetType | ASSET_TYPE | — | — |
| 52 | AdditionPrntCommitment | COMMITMENT | — | — |
| 53 | AdditionPrntContext | CONTEXT | — | — |
| 54 | AdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 55 | AdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 56 | AdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 57 | AdditionPrntInventorial | INVENTORIAL | — | — |
| 58 | AdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 59 | AdditionPrntLeaseId | LEASE_ID | — | — |
| 60 | AdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 61 | AdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 62 | AdditionPrntNewUsed | NEW_USED | — | — |
| 63 | AdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 64 | AdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 65 | AdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 66 | AdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 67 | AdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 68 | AdditionPrntTagNumber | TAG_NUMBER | — | — |
| 69 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 70 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 71 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 72 | AdditionTagNumber | TAG_NUMBER | — | — |

### [[fa_bonus_rules|FA_BONUS_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BonusRuleBonusRule | BONUS_RULE | — | ✅ |
| 2 | BonusRuleBonusRuleId | BONUS_RULE_ID | — | — |
| 3 | BonusRuleDescription | DESCRIPTION | — | ✅ |
| 4 | BonusRuleOneTimeFlag | ONE_TIME_FLAG | — | — |
| 5 | BonusRuleSetId | SET_ID | — | — |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaBooksAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 2 | FaBooksAdjustedCost | ADJUSTED_COST | — | — |
| 3 | FaBooksAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | ✅ |
| 4 | FaBooksAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 5 | FaBooksAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 6 | FaBooksAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 7 | FaBooksAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 8 | FaBooksAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 9 | FaBooksAssetId | ASSET_ID | — | — |
| 10 | FaBooksBonusRuleId | BONUS_RULE_ID | — | — |
| 11 | FaBooksBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | FaBooksCapitalizeFlag | CAPITALIZE_FLAG | — | ✅ |
| 13 | FaBooksCeilingTypeId | CEILING_TYPE_ID | — | — |
| 14 | FaBooksCipCost | CIP_COST | — | — |
| 15 | FaBooksConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 16 | FaBooksConversionDate | CONVERSION_DATE | — | ✅ |
| 17 | FaBooksCost | COST | — | ✅ |
| 18 | FaBooksCreatedBy | CREATED_BY | — | — |
| 19 | FaBooksCreationDate | CREATION_DATE | — | — |
| 20 | FaBooksDateEffective | DATE_EFFECTIVE | — | — |
| 21 | FaBooksDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 22 | FaBooksDatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 23 | FaBooksDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 24 | FaBooksDepreciationOption | DEPRECIATION_OPTION | — | — |
| 25 | FaBooksDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 26 | FaBooksDeprnStartDate | DEPRN_START_DATE | — | ✅ |
| 27 | FaBooksDisabledFlag | DISABLED_FLAG | — | — |
| 28 | FaBooksEofyAdjCost | EOFY_ADJ_COST | — | — |
| 29 | FaBooksEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 30 | FaBooksEofyReserve | EOFY_RESERVE | — | — |
| 31 | FaBooksEopAdjCost | EOP_ADJ_COST | — | — |
| 32 | FaBooksEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 33 | FaBooksExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 34 | FaBooksExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 35 | FaBooksExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 36 | FaBooksFlatRateId | FLAT_RATE_ID | — | — |
| 37 | FaBooksFormulaFactor | FORMULA_FACTOR | — | — |
| 38 | FaBooksFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 39 | FaBooksGroupAssetId | GROUP_ASSET_ID | — | — |
| 40 | FaBooksLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | FaBooksLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | FaBooksLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | FaBooksLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 44 | FaBooksLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 45 | FaBooksLtdProceeds | LTD_PROCEEDS | — | — |
| 46 | FaBooksMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 47 | FaBooksMethodId | METHOD_ID | — | — |
| 48 | FaBooksObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | FaBooksOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 50 | FaBooksOldAdjustedCost | OLD_ADJUSTED_COST | — | ✅ |
| 51 | FaBooksOriginalCost | ORIGINAL_COST | — | ✅ |
| 52 | FaBooksOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | ✅ |
| 53 | FaBooksOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 54 | FaBooksPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 55 | FaBooksPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 56 | FaBooksPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 57 | FaBooksPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 58 | FaBooksPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 59 | FaBooksPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 60 | FaBooksProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 61 | FaBooksProrateDate | PRORATE_DATE | — | ✅ |
| 62 | FaBooksRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 63 | FaBooksRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 64 | FaBooksRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 65 | FaBooksRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 66 | FaBooksReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 67 | FaBooksReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 68 | FaBooksReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 69 | FaBooksReductionRate | REDUCTION_RATE | — | — |
| 70 | FaBooksRemainingLife1 | REMAINING_LIFE1 | — | — |
| 71 | FaBooksRemainingLife2 | REMAINING_LIFE2 | — | — |
| 72 | FaBooksRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 73 | FaBooksRetirementId | RETIREMENT_ID | — | — |
| 74 | FaBooksRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 75 | FaBooksRevalCeiling | REVAL_CEILING | — | — |
| 76 | FaBooksSalvageType | SALVAGE_TYPE | — | ✅ |
| 77 | FaBooksSalvageValue | SALVAGE_VALUE | — | ✅ |
| 78 | FaBooksShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | ✅ |
| 79 | FaBooksTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 80 | FaBooksTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 81 | FaBooksTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 82 | FaBooksTrackingMethod | TRACKING_METHOD | — | — |
| 83 | FaBooksTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 84 | FaBooksUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 85 | FaBooksUnrevaluedCost | UNREVALUED_COST | — | — |
| 86 | FaBooksYtdProceeds | YTD_PROCEEDS | — | — |
| 87 | TransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlBookControlId | BOOK_CONTROL_ID | — | — |
| 2 | BookControlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | BookControlSetOfBooksId | SET_OF_BOOKS_ID | — | — |

### [[fa_ceiling_types|FA_CEILING_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CeilingTypeCeilingName | CEILING_NAME | — | ✅ |
| 2 | CeilingTypeCeilingType | CEILING_TYPE | — | ✅ |
| 3 | CeilingTypeCeilingTypeId | CEILING_TYPE_ID | — | — |
| 4 | CeilingTypeCurrencyCode | CURRENCY_CODE | — | — |
| 5 | CeilingTypeDescription | DESCRIPTION | — | — |
| 6 | CeilingTypeSetId | SET_ID | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProrateConventionTypeConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateConventionTypeDeprWhenAcquiredFlag | DEPR_WHEN_ACQUIRED_FLAG | — | — |
| 3 | ProrateConventionTypeDescription | DESCRIPTION | — | ✅ |
| 4 | ProrateConventionTypeFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 5 | ProrateConventionTypeProrateConventionCode | PRORATE_CONVENTION_CODE | — | ✅ |
| 6 | ProrateConventionTypeSetId | SET_ID | — | — |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnPrdCntFullyRetBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPrdCntFullyRetCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 3 | DeprnPrdCntFullyRetCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 4 | DeprnPrdCntFullyRetDeprnRun | DEPRN_RUN | — | — |
| 5 | DeprnPrdCntFullyRetFiscalYear | FISCAL_YEAR | — | — |
| 6 | DeprnPrdCntFullyRetPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 7 | DeprnPrdCntFullyRetPeriodCounter | PERIOD_COUNTER | — | — |
| 8 | DeprnPrdCntFullyRetPeriodName | PERIOD_NAME | — | ✅ |
| 9 | DeprnPrdCntFullyRetPeriodNum | PERIOD_NUM | — | — |
| 10 | DeprnPrdCntFullyRetPeriodOpenDate | PERIOD_OPEN_DATE | — | — |
| 11 | DeprnPrdCntLfeCompBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | DeprnPrdCntLfeCompCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 13 | DeprnPrdCntLfeCompCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 14 | DeprnPrdCntLfeCompDeprnRun | DEPRN_RUN | — | — |
| 15 | DeprnPrdCntLfeCompFiscalYear | FISCAL_YEAR | — | — |
| 16 | DeprnPrdCntLfeCompPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 17 | DeprnPrdCntLfeCompPeriodCounter | PERIOD_COUNTER | — | — |
| 18 | DeprnPrdCntLfeCompPeriodName | PERIOD_NAME | — | ✅ |
| 19 | DeprnPrdCntLfeCompPeriodNum | PERIOD_NUM | — | — |
| 20 | DeprnPrdCntLfeCompPeriodOpenDate | PERIOD_OPEN_DATE | — | — |
| 21 | DeprnPrdCntrCapBookTypeCode | BOOK_TYPE_CODE | — | — |
| 22 | DeprnPrdCntrCapCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 23 | DeprnPrdCntrCapCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 24 | DeprnPrdCntrCapDeprnRun | DEPRN_RUN | — | — |
| 25 | DeprnPrdCntrCapFiscalYear | FISCAL_YEAR | — | — |
| 26 | DeprnPrdCntrCapPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 27 | DeprnPrdCntrCapPeriodCounter | PERIOD_COUNTER | — | — |
| 28 | DeprnPrdCntrCapPeriodName | PERIOD_NAME | — | ✅ |
| 29 | DeprnPrdCntrCapPeriodNum | PERIOD_NUM | — | — |
| 30 | DeprnPrdCntrCapPeriodOpenDate | PERIOD_OPEN_DATE | — | — |
| 31 | DeprnPrdCntrFullyResvdBookTypeCode | BOOK_TYPE_CODE | — | — |
| 32 | DeprnPrdCntrFullyResvdCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 33 | DeprnPrdCntrFullyResvdCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 34 | DeprnPrdCntrFullyResvdDeprnRun | DEPRN_RUN | — | — |
| 35 | DeprnPrdCntrFullyResvdFiscalYear | FISCAL_YEAR | — | — |
| 36 | DeprnPrdCntrFullyResvdPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 37 | DeprnPrdCntrFullyResvdPeriodCounter | PERIOD_COUNTER | — | — |
| 38 | DeprnPrdCntrFullyResvdPeriodName | PERIOD_NAME | — | ✅ |
| 39 | DeprnPrdCntrFullyResvdPeriodNum | PERIOD_NUM | — | — |
| 40 | DeprnPrdCntrFullyResvdPeriodOpenDate | PERIOD_OPEN_DATE | — | — |

### [[fa_flat_rates|FA_FLAT_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlatRateAdjustedRate | ADJUSTED_RATE | — | ✅ |
| 2 | FlatRateAdjustingRate | ADJUSTING_RATE | — | ✅ |
| 3 | FlatRateBasicRate | BASIC_RATE | — | ✅ |
| 4 | FlatRateCreatedBy | CREATED_BY | — | — |
| 5 | FlatRateCreationDate | CREATION_DATE | — | — |
| 6 | FlatRateFlatRateId | FLAT_RATE_ID | — | — |
| 7 | FlatRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | FlatRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | FlatRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | FlatRateMethodId | METHOD_ID | — | — |
| 11 | FlatRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationMethodCreatedBy | CREATED_BY | — | — |
| 2 | DepreciationMethodCreationDate | CREATION_DATE | — | — |
| 3 | DepreciationMethodDepreciateLastyearFlag | DEPRECIATE_LASTYEAR_FLAG | — | — |
| 4 | DepreciationMethodDeprnBasisRule | DEPRN_BASIS_RULE | — | ✅ |
| 5 | DepreciationMethodDeprnBasisRuleId | DEPRN_BASIS_RULE_ID | — | — |
| 6 | DepreciationMethodExcludeSalvageValueFlag | EXCLUDE_SALVAGE_VALUE_FLAG | — | ✅ |
| 7 | DepreciationMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DepreciationMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DepreciationMethodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DepreciationMethodLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 11 | DepreciationMethodMethodCode | METHOD_CODE | — | ✅ |
| 12 | DepreciationMethodMethodId | METHOD_ID | — | — |
| 13 | DepreciationMethodName | NAME | — | ✅ |
| 14 | DepreciationMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DepreciationMethodPolishAdjCalcBasisFlag | POLISH_ADJ_CALC_BASIS_FLAG | — | — |
| 16 | DepreciationMethodProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 17 | DepreciationMethodRateSourceRule | RATE_SOURCE_RULE | — | ✅ |
| 18 | DepreciationMethodSetId | SET_ID | — | — |
| 19 | DepreciationMethodStlMethodFlag | STL_METHOD_FLAG | — | ✅ |
| 20 | DepreciationMethodUseLifeInPeriodsFlag | USE_LIFE_IN_PERIODS_FLAG | — | ✅ |

### [[fa_retirements|FA_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RetirementAssetId | ASSET_ID | — | — |
| 2 | RetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 3 | RetirementBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | RetirementCostOfRemoval | COST_OF_REMOVAL | — | — |
| 5 | RetirementCostRetired | COST_RETIRED | — | — |
| 6 | RetirementDateEffective | DATE_EFFECTIVE | — | — |
| 7 | RetirementDateRetired | DATE_RETIRED | — | — |
| 8 | RetirementEofyReserve | EOFY_RESERVE | — | — |
| 9 | RetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 10 | RetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 11 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 12 | RetirementNbvRetired | NBV_RETIRED | — | — |
| 13 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 14 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 15 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 16 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 17 | RetirementReductionRate | REDUCTION_RATE | — | — |
| 18 | RetirementReferenceNum | REFERENCE_NUM | — | — |
| 19 | RetirementReserveRetired | RESERVE_RETIRED | — | — |
| 20 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 21 | RetirementRetirementId | RETIREMENT_ID | — | — |
| 22 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 23 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 24 | RetirementSoldTo | SOLD_TO | — | — |
| 25 | RetirementStatus | STATUS | — | — |
| 26 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 27 | RetirementStlMethodId | STL_METHOD_ID | — | — |
| 28 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 29 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 30 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 31 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 32 | RetirementUnits | UNITS | — | — |
| 33 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxnHeaderInAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | TrxnHeaderInAssetId | ASSET_ID | — | — |
| 3 | TrxnHeaderInBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | TrxnHeaderInCallingInterface | CALLING_INTERFACE | — | — |
| 5 | TrxnHeaderInCreatedBy | CREATED_BY | — | — |
| 6 | TrxnHeaderInCreationDate | CREATION_DATE | — | — |
| 7 | TrxnHeaderInDateEffective | DATE_EFFECTIVE | — | — |
| 8 | TrxnHeaderInEventId | EVENT_ID | — | — |
| 9 | TrxnHeaderInInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 10 | TrxnHeaderInLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | TrxnHeaderInLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | TrxnHeaderInLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | TrxnHeaderInMassReferenceId | MASS_REFERENCE_ID | — | — |
| 14 | TrxnHeaderInMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 15 | TrxnHeaderInMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 16 | TrxnHeaderInObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TrxnHeaderInSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 18 | TrxnHeaderInTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 19 | TrxnHeaderInTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 20 | TrxnHeaderInTransactionKey | TRANSACTION_KEY | — | ✅ |
| 21 | TrxnHeaderInTransactionName | TRANSACTION_NAME | — | ✅ |
| 22 | TrxnHeaderInTransactionSubtype | TRANSACTION_SUBTYPE | — | ✅ |
| 23 | TrxnHeaderInTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 24 | TrxnHeaderInTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 25 | TrxnHeaderOutAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 26 | TrxnHeaderOutAssetId | ASSET_ID | — | — |
| 27 | TrxnHeaderOutBookTypeCode | BOOK_TYPE_CODE | — | — |
| 28 | TrxnHeaderOutCallingInterface | CALLING_INTERFACE | — | — |
| 29 | TrxnHeaderOutDateEffective | DATE_EFFECTIVE | — | — |
| 30 | TrxnHeaderOutEventId | EVENT_ID | — | — |
| 31 | TrxnHeaderOutInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 32 | TrxnHeaderOutMassReferenceId | MASS_REFERENCE_ID | — | — |
| 33 | TrxnHeaderOutMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 34 | TrxnHeaderOutMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 35 | TrxnHeaderOutObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | TrxnHeaderOutSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 37 | TrxnHeaderOutTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 38 | TrxnHeaderOutTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 39 | TrxnHeaderOutTransactionKey | TRANSACTION_KEY | — | — |
| 40 | TrxnHeaderOutTransactionName | TRANSACTION_NAME | — | — |
| 41 | TrxnHeaderOutTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 42 | TrxnHeaderOutTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 43 | TrxnHeaderOutTrxReferenceId | TRX_REFERENCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
