---
id: DOC-OTHER-PVO-DepreciationDetailPVO
doc_type: system-doc
title: "DepreciationDetailPVO — PVO Cross-Module"
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
  - DepreciationDetailPVO
  - depreciationdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Detail. Acessa as tabelas: FA_ADDITIONS_B, FA_ASSET_HISTORY, FA_BOOKS (+6).

**Caminho:** `FscmTopModelAM.FinFaDeprDepreciationAM.DepreciationDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 362 | 9 | 5 | 36 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 72 atributos (1 BICC)
- [[fa_asset_history|FA_ASSET_HISTORY]] — 14 atributos (1 PKs, 4 BICC)
- [[fa_books|FA_BOOKS]] — 81 atributos
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (3 BICC)
- [[fa_deprn_detail|FA_DEPRN_DETAIL]] — 28 atributos (4 PKs, 17 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 16 atributos (5 BICC)
- [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]] — 19 atributos (6 BICC)
- [[fa_retirements|FA_RETIREMENTS]] — 33 atributos
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 18 atributos

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetHistAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 3 | AdditionAssetHistAssetId | ASSET_ID | — | — |
| 4 | AdditionAssetHistAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 5 | AdditionAssetHistAssetNumber | ASSET_NUMBER | — | — |
| 6 | AdditionAssetHistAssetType | ASSET_TYPE | — | — |
| 7 | AdditionAssetHistCommitment | COMMITMENT | — | — |
| 8 | AdditionAssetHistContext | CONTEXT | — | — |
| 9 | AdditionAssetHistCurrentUnits | CURRENT_UNITS | — | — |
| 10 | AdditionAssetHistDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 11 | AdditionAssetHistInUseFlag | IN_USE_FLAG | — | — |
| 12 | AdditionAssetHistInventorial | INVENTORIAL | — | — |
| 13 | AdditionAssetHistInvestmentLaw | INVESTMENT_LAW | — | — |
| 14 | AdditionAssetHistLeaseId | LEASE_ID | — | — |
| 15 | AdditionAssetHistManufacturerName | MANUFACTURER_NAME | — | — |
| 16 | AdditionAssetHistModelNumber | MODEL_NUMBER | — | — |
| 17 | AdditionAssetHistNewUsed | NEW_USED | — | — |
| 18 | AdditionAssetHistOwnedLeased | OWNED_LEASED | — | — |
| 19 | AdditionAssetHistParentAssetId | PARENT_ASSET_ID | — | — |
| 20 | AdditionAssetHistProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 21 | AdditionAssetHistPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 22 | AdditionAssetHistSerialNumber | SERIAL_NUMBER | — | — |
| 23 | AdditionAssetHistTagNumber | TAG_NUMBER | — | — |
| 24 | AdditionAssetId | ASSET_ID | — | — |
| 25 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 26 | AdditionAssetNumber | ASSET_NUMBER | — | — |
| 27 | AdditionAssetType | ASSET_TYPE | — | — |
| 28 | AdditionCommitment | COMMITMENT | — | — |
| 29 | AdditionContext | CONTEXT | — | — |
| 30 | AdditionCreatedBy | CREATED_BY | — | — |
| 31 | AdditionCreationDate | CREATION_DATE | — | — |
| 32 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 33 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
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
| 58 | BkCtrlLastPeriodCounter | LAST_PERIOD_COUNTER | — | ✅ |
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

### [[fa_deprn_detail|FA_DEPRN_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | 🔑 | ✅ |
| 2 | BookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 3 | DeprnDetAdditionCostToClear | ADDITION_COST_TO_CLEAR | — | ✅ |
| 4 | DeprnDetBonusDeprnAdjustmentAmount | BONUS_DEPRN_ADJUSTMENT_AMOUNT | — | — |
| 5 | DeprnDetBonusDeprnAmount | BONUS_DEPRN_AMOUNT | — | — |
| 6 | DeprnDetBonusDeprnReserve | BONUS_DEPRN_RESERVE | — | — |
| 7 | DeprnDetBonusYtdDeprn | BONUS_YTD_DEPRN | — | — |
| 8 | DeprnDetCost | COST | — | ✅ |
| 9 | DeprnDetCreatedBy | CREATED_BY | — | ✅ |
| 10 | DeprnDetCreationDate | CREATION_DATE | — | ✅ |
| 11 | DeprnDetDeprnAdjustmentAmount | DEPRN_ADJUSTMENT_AMOUNT | — | ✅ |
| 12 | DeprnDetDeprnAmount | DEPRN_AMOUNT | — | ✅ |
| 13 | DeprnDetDeprnReserve | DEPRN_RESERVE | — | ✅ |
| 14 | DeprnDetDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 15 | DeprnDetDeprnRunId | DEPRN_RUN_ID | — | ✅ |
| 16 | DeprnDetDeprnSourceCode | DEPRN_SOURCE_CODE | — | ✅ |
| 17 | DeprnDetEventId | EVENT_ID | — | — |
| 18 | DeprnDetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | DeprnDetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | DeprnDetLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | DeprnDetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | DeprnDetRevalAmortization | REVAL_AMORTIZATION | — | — |
| 23 | DeprnDetRevalDeprnExpense | REVAL_DEPRN_EXPENSE | — | — |
| 24 | DeprnDetRevalReserve | REVAL_RESERVE | — | — |
| 25 | DeprnDetYtdDeprn | YTD_DEPRN | — | ✅ |
| 26 | DeprnDetYtdRevalDeprnExpense | YTD_REVAL_DEPRN_EXPENSE | — | — |
| 27 | DistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 28 | PeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPeriodCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | ✅ |
| 3 | DeprnPeriodCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | ✅ |
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
| 1 | TrxHdrAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | TrxHdrAssetId | ASSET_ID | — | — |
| 3 | TrxHdrBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | TrxHdrCallingInterface | CALLING_INTERFACE | — | — |
| 5 | TrxHdrDateEffective | DATE_EFFECTIVE | — | — |
| 6 | TrxHdrEventId | EVENT_ID | — | — |
| 7 | TrxHdrInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 8 | TrxHdrMassReferenceId | MASS_REFERENCE_ID | — | — |
| 9 | TrxHdrMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 10 | TrxHdrMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 11 | TrxHdrSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 12 | TrxHdrTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 13 | TrxHdrTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 14 | TrxHdrTransactionKey | TRANSACTION_KEY | — | — |
| 15 | TrxHdrTransactionName | TRANSACTION_NAME | — | — |
| 16 | TrxHdrTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 17 | TrxHdrTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 18 | TrxHdrTrxReferenceId | TRX_REFERENCE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
