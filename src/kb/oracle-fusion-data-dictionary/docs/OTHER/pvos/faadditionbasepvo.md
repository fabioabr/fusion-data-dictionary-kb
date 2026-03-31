---
id: DOC-OTHER-PVO-FaAdditionBasePVO
doc_type: system-doc
title: "FaAdditionBasePVO — PVO Cross-Module"
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
  - FaAdditionBasePVO
  - faadditionbasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaAdditionBasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Addition Base. Acessa as tabelas: FA_ADDITIONS_B, FA_ADDITIONS_TL, FA_ADD_WARRANTIES (+6).

**Caminho:** `FscmTopModelAM.FinFaTrackDescDetailsAM.FaAdditionBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 350 | 9 | 1 | 1 | 0% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 58 atributos (1 PKs, 1 BICC)
- [[fa_additions_tl|FA_ADDITIONS_TL]] — 10 atributos
- [[fa_add_warranties|FA_ADD_WARRANTIES]] — 10 atributos
- [[fa_books|FA_BOOKS]] — 96 atributos
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos
- [[fa_leases|FA_LEASES]] — 26 atributos
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 48 atributos
- [[fa_warranties|FA_WARRANTIES]] — 17 atributos
- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 4 atributos

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 3 | AdditionAssetNumber | ASSET_NUMBER | — | — |
| 4 | AdditionAssetType | ASSET_TYPE | — | — |
| 5 | AdditionCommitment | COMMITMENT | — | — |
| 6 | AdditionContext | CONTEXT | — | — |
| 7 | AdditionCreatedBy | CREATED_BY | — | — |
| 8 | AdditionCreationDate | CREATION_DATE | — | — |
| 9 | AdditionCurrentUnits | CURRENT_UNITS | — | — |
| 10 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 11 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 12 | AdditionInventorial | INVENTORIAL | — | — |
| 13 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 14 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | AdditionLeaseId | LEASE_ID | — | — |
| 18 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 19 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 20 | AdditionNewUsed | NEW_USED | — | — |
| 21 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 23 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 24 | AdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 25 | AdditionPrntAssetId | ASSET_ID | — | — |
| 26 | AdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 27 | AdditionPrntAssetNumber | ASSET_NUMBER | — | — |
| 28 | AdditionPrntAssetType | ASSET_TYPE | — | — |
| 29 | AdditionPrntCommitment | COMMITMENT | — | — |
| 30 | AdditionPrntContext | CONTEXT | — | — |
| 31 | AdditionPrntCreatedBy | CREATED_BY | — | — |
| 32 | AdditionPrntCreationDate | CREATION_DATE | — | — |
| 33 | AdditionPrntCurrentUnits | CURRENT_UNITS | — | — |
| 34 | AdditionPrntDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 35 | AdditionPrntInUseFlag | IN_USE_FLAG | — | — |
| 36 | AdditionPrntInventorial | INVENTORIAL | — | — |
| 37 | AdditionPrntInvestmentLaw | INVESTMENT_LAW | — | — |
| 38 | AdditionPrntLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 39 | AdditionPrntLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | AdditionPrntLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | AdditionPrntLeaseId | LEASE_ID | — | — |
| 42 | AdditionPrntManufacturerName | MANUFACTURER_NAME | — | — |
| 43 | AdditionPrntModelNumber | MODEL_NUMBER | — | — |
| 44 | AdditionPrntNewUsed | NEW_USED | — | — |
| 45 | AdditionPrntObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | AdditionPrntOwnedLeased | OWNED_LEASED | — | — |
| 47 | AdditionPrntParentAssetId | PARENT_ASSET_ID | — | — |
| 48 | AdditionPrntProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 49 | AdditionPrntPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 50 | AdditionPrntSerialNumber | SERIAL_NUMBER | — | — |
| 51 | AdditionPrntTagNumber | TAG_NUMBER | — | — |
| 52 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 53 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 54 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 55 | AdditionTagNumber | TAG_NUMBER | — | — |
| 56 | AssetId | ASSET_ID | 🔑 | ✅ |
| 57 | AssetKeyCcid | ASSET_KEY_CCID | — | — |
| 58 | CurrentUnits | CURRENT_UNITS | — | — |

### [[fa_additions_tl|FA_ADDITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionTLAssetId | ASSET_ID | — | — |
| 2 | AdditionTLCreatedBy | CREATED_BY | — | — |
| 3 | AdditionTLCreationDate | CREATION_DATE | — | — |
| 4 | AdditionTLDescription | DESCRIPTION | — | — |
| 5 | AdditionTLLanguage | LANGUAGE | — | — |
| 6 | AdditionTLLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AdditionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AdditionTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AdditionTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AdditionTLSourceLang | SOURCE_LANG | — | — |

### [[fa_add_warranties|FA_ADD_WARRANTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetAddWarrantiesAssetId1 | ASSET_ID | — | — |
| 2 | AssetAddWarrantiesCreatedBy2 | CREATED_BY | — | — |
| 3 | AssetAddWarrantiesCreationDate2 | CREATION_DATE | — | — |
| 4 | AssetAddWarrantiesDateEffective | DATE_EFFECTIVE | — | — |
| 5 | AssetAddWarrantiesDateIneffective | DATE_INEFFECTIVE | — | — |
| 6 | AssetAddWarrantiesLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 7 | AssetAddWarrantiesLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 8 | AssetAddWarrantiesLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 9 | AssetAddWarrantiesObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 10 | AssetAddWarrantiesWarrantyId | WARRANTY_ID | — | — |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 2 | ConversionDate | CONVERSION_DATE | — | — |
| 3 | DepreciateFlag | DEPRECIATE_FLAG | — | — |
| 4 | DeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 5 | FaBooksAdjustedCapacity | ADJUSTED_CAPACITY | — | — |
| 6 | FaBooksAdjustedCost | ADJUSTED_COST | — | — |
| 7 | FaBooksAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 8 | FaBooksAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 9 | FaBooksAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 10 | FaBooksAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | — |
| 11 | FaBooksAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | — |
| 12 | FaBooksAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 13 | FaBooksAssetId | ASSET_ID | — | — |
| 14 | FaBooksBonusRuleId | BONUS_RULE_ID | — | — |
| 15 | FaBooksBookTypeCode | BOOK_TYPE_CODE | — | — |
| 16 | FaBooksCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 17 | FaBooksCeilingTypeId | CEILING_TYPE_ID | — | — |
| 18 | FaBooksCipCost | CIP_COST | — | — |
| 19 | FaBooksConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 20 | FaBooksConversionDate | CONVERSION_DATE | — | — |
| 21 | FaBooksCost | COST | — | — |
| 22 | FaBooksCreatedBy | CREATED_BY | — | — |
| 23 | FaBooksCreationDate | CREATION_DATE | — | — |
| 24 | FaBooksDateEffective | DATE_EFFECTIVE | — | — |
| 25 | FaBooksDateIneffective | DATE_INEFFECTIVE | — | — |
| 26 | FaBooksDatePlacedInService | DATE_PLACED_IN_SERVICE | — | — |
| 27 | FaBooksDepreciateFlag | DEPRECIATE_FLAG | — | — |
| 28 | FaBooksDepreciationOption | DEPRECIATION_OPTION | — | — |
| 29 | FaBooksDeprnLimitType | DEPRN_LIMIT_TYPE | — | — |
| 30 | FaBooksDeprnStartDate | DEPRN_START_DATE | — | — |
| 31 | FaBooksDisabledFlag | DISABLED_FLAG | — | — |
| 32 | FaBooksEofyAdjCost | EOFY_ADJ_COST | — | — |
| 33 | FaBooksEofyFormulaFactor | EOFY_FORMULA_FACTOR | — | — |
| 34 | FaBooksEofyReserve | EOFY_RESERVE | — | — |
| 35 | FaBooksEopAdjCost | EOP_ADJ_COST | — | — |
| 36 | FaBooksEopFormulaFactor | EOP_FORMULA_FACTOR | — | — |
| 37 | FaBooksExcessAllocationOption | EXCESS_ALLOCATION_OPTION | — | — |
| 38 | FaBooksExcludeFullyRsvFlag | EXCLUDE_FULLY_RSV_FLAG | — | — |
| 39 | FaBooksExcludeProceedsFromBasis | EXCLUDE_PROCEEDS_FROM_BASIS | — | — |
| 40 | FaBooksFlatRateId | FLAT_RATE_ID | — | — |
| 41 | FaBooksFormulaFactor | FORMULA_FACTOR | — | — |
| 42 | FaBooksFullyRsvdRevalsCounter | FULLY_RSVD_REVALS_COUNTER | — | — |
| 43 | FaBooksGroupAssetId | GROUP_ASSET_ID | — | — |
| 44 | FaBooksLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 45 | FaBooksLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | FaBooksLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | FaBooksLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 48 | FaBooksLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 49 | FaBooksLtdProceeds | LTD_PROCEEDS | — | — |
| 50 | FaBooksMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 51 | FaBooksMethodId | METHOD_ID | — | — |
| 52 | FaBooksObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | FaBooksOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 54 | FaBooksOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 55 | FaBooksOriginalCost | ORIGINAL_COST | — | — |
| 56 | FaBooksOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 57 | FaBooksOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 58 | FaBooksPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | — |
| 59 | FaBooksPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 60 | FaBooksPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 61 | FaBooksPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 62 | FaBooksPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 63 | FaBooksPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 64 | FaBooksProductionCapacity | PRODUCTION_CAPACITY | — | — |
| 65 | FaBooksProrateDate | PRORATE_DATE | — | — |
| 66 | FaBooksRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 67 | FaBooksRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 68 | FaBooksRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 69 | FaBooksRecoverableCost | RECOVERABLE_COST | — | — |
| 70 | FaBooksReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 71 | FaBooksReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 72 | FaBooksReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 73 | FaBooksReductionRate | REDUCTION_RATE | — | — |
| 74 | FaBooksRemainingLife1 | REMAINING_LIFE1 | — | — |
| 75 | FaBooksRemainingLife2 | REMAINING_LIFE2 | — | — |
| 76 | FaBooksRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 77 | FaBooksRetirementId | RETIREMENT_ID | — | — |
| 78 | FaBooksRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | — |
| 79 | FaBooksRevalCeiling | REVAL_CEILING | — | — |
| 80 | FaBooksSalvageType | SALVAGE_TYPE | — | — |
| 81 | FaBooksSalvageValue | SALVAGE_VALUE | — | — |
| 82 | FaBooksShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |
| 83 | FaBooksTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 84 | FaBooksTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 85 | FaBooksTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 86 | FaBooksTrackingMethod | TRACKING_METHOD | — | — |
| 87 | FaBooksTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 88 | FaBooksTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 89 | FaBooksUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 90 | FaBooksUnrevaluedCost | UNREVALUED_COST | — | — |
| 91 | FaBooksYtdProceeds | YTD_PROCEEDS | — | — |
| 92 | GroupAssetId | GROUP_ASSET_ID | — | — |
| 93 | OriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | — |
| 94 | ProrateDate | PRORATE_DATE | — | — |
| 95 | ReductionRate | REDUCTION_RATE | — | — |
| 96 | ShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | — |

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
| 60 | BkCtrlLastUpdateDate | LAST_UPDATE_DATE | — | — |
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

### [[fa_leases|FA_LEASES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetLeasesAssetLife | ASSET_LIFE | — | — |
| 2 | AssetLeasesAttributeCategoryCode1 | ATTRIBUTE_CATEGORY_CODE | — | — |
| 3 | AssetLeasesBargainPurchaseOption | BARGAIN_PURCHASE_OPTION | — | — |
| 4 | AssetLeasesCostCapitalized | COST_CAPITALIZED | — | — |
| 5 | AssetLeasesCreatedBy1 | CREATED_BY | — | — |
| 6 | AssetLeasesCreationDate1 | CREATION_DATE | — | — |
| 7 | AssetLeasesCurrencyCode | CURRENCY_CODE | — | — |
| 8 | AssetLeasesDescription | DESCRIPTION | — | — |
| 9 | AssetLeasesDistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 10 | AssetLeasesFairValue | FAIR_VALUE | — | — |
| 11 | AssetLeasesFasbLeaseType | FASB_LEASE_TYPE | — | — |
| 12 | AssetLeasesLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 13 | AssetLeasesLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 14 | AssetLeasesLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 15 | AssetLeasesLeaseId1 | LEASE_ID | — | — |
| 16 | AssetLeasesLeaseId2 | LEASE_ID | — | — |
| 17 | AssetLeasesLeaseNumber | LEASE_NUMBER | — | — |
| 18 | AssetLeasesLeaseTerm | LEASE_TERM | — | — |
| 19 | AssetLeasesLeaseType | LEASE_TYPE | — | — |
| 20 | AssetLeasesLessorId | LESSOR_ID | — | — |
| 21 | AssetLeasesLessorSiteId | LESSOR_SITE_ID | — | — |
| 22 | AssetLeasesObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 23 | AssetLeasesPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 24 | AssetLeasesPresentValue | PRESENT_VALUE | — | — |
| 25 | AssetLeasesTermsId | TERMS_ID | — | — |
| 26 | AssetLeasesTransferOwnership | TRANSFER_OWNERSHIP | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxHdrInAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | TrxHdrInAssetId | ASSET_ID | — | — |
| 3 | TrxHdrInBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | TrxHdrInCallingInterface | CALLING_INTERFACE | — | — |
| 5 | TrxHdrInCreatedBy | CREATED_BY | — | — |
| 6 | TrxHdrInCreationDate | CREATION_DATE | — | — |
| 7 | TrxHdrInDateEffective | DATE_EFFECTIVE | — | — |
| 8 | TrxHdrInEventId | EVENT_ID | — | — |
| 9 | TrxHdrInInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 10 | TrxHdrInLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | TrxHdrInLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | TrxHdrInLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | TrxHdrInMassReferenceId | MASS_REFERENCE_ID | — | — |
| 14 | TrxHdrInMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 15 | TrxHdrInMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 16 | TrxHdrInObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TrxHdrInSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 18 | TrxHdrInTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 19 | TrxHdrInTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 20 | TrxHdrInTransactionKey | TRANSACTION_KEY | — | — |
| 21 | TrxHdrInTransactionName | TRANSACTION_NAME | — | — |
| 22 | TrxHdrInTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 23 | TrxHdrInTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 24 | TrxHdrInTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 25 | TrxHdrOutAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 26 | TrxHdrOutAssetId | ASSET_ID | — | — |
| 27 | TrxHdrOutBookTypeCode | BOOK_TYPE_CODE | — | — |
| 28 | TrxHdrOutCallingInterface | CALLING_INTERFACE | — | — |
| 29 | TrxHdrOutCreatedBy | CREATED_BY | — | — |
| 30 | TrxHdrOutCreationDate | CREATION_DATE | — | — |
| 31 | TrxHdrOutDateEffective | DATE_EFFECTIVE | — | — |
| 32 | TrxHdrOutEventId | EVENT_ID | — | — |
| 33 | TrxHdrOutInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 34 | TrxHdrOutLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 35 | TrxHdrOutLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 36 | TrxHdrOutLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 37 | TrxHdrOutMassReferenceId | MASS_REFERENCE_ID | — | — |
| 38 | TrxHdrOutMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 39 | TrxHdrOutMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 40 | TrxHdrOutObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | TrxHdrOutSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 42 | TrxHdrOutTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 43 | TrxHdrOutTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 44 | TrxHdrOutTransactionKey | TRANSACTION_KEY | — | — |
| 45 | TrxHdrOutTransactionName | TRANSACTION_NAME | — | — |
| 46 | TrxHdrOutTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 47 | TrxHdrOutTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 48 | TrxHdrOutTrxReferenceId | TRX_REFERENCE_ID | — | — |

### [[fa_warranties|FA_WARRANTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetWarrantiesAttributeCategoryCode2 | ATTRIBUTE_CATEGORY_CODE | — | — |
| 2 | AssetWarrantiesCost | COST | — | — |
| 3 | AssetWarrantiesCreatedBy3 | CREATED_BY | — | — |
| 4 | AssetWarrantiesCreationDate3 | CREATION_DATE | — | — |
| 5 | AssetWarrantiesCurrencyCode1 | CURRENCY_CODE | — | — |
| 6 | AssetWarrantiesDescription1 | DESCRIPTION | — | — |
| 7 | AssetWarrantiesEmployeeId | EMPLOYEE_ID | — | — |
| 8 | AssetWarrantiesEndDate | END_DATE | — | — |
| 9 | AssetWarrantiesLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 10 | AssetWarrantiesLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 11 | AssetWarrantiesLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 12 | AssetWarrantiesObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 13 | AssetWarrantiesPoVendorId | PO_VENDOR_ID | — | — |
| 14 | AssetWarrantiesRenewFlag | RENEW_FLAG | — | — |
| 15 | AssetWarrantiesStartDate | START_DATE | — | — |
| 16 | AssetWarrantiesWarrantyId1 | WARRANTY_ID | — | — |
| 17 | AssetWarrantiesWarrantyNumber | WARRANTY_NUMBER | — | — |

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 2 | SetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 3 | SetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 4 | SetIdAssignmentSetId | SET_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
