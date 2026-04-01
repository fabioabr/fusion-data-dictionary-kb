---
id: DOC-OTHER-PVO-AdditionBasePVO
doc_type: system-doc
title: "AdditionBasePVO — PVO Cross-Module"
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
  - AdditionBasePVO
  - additionbasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdditionBasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Addition Base. Acessa as tabelas: FA_ADDITIONS_B, FA_ADDITIONS_TL, FA_ADDITIONS_VL (+16).

**Caminho:** `FscmTopModelAM.FinFaTrackDescDetailsAM.AdditionBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 363 | 19 | 5 | 81 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 56 atributos (1 PKs, 22 BICC)
- [[fa_additions_tl|FA_ADDITIONS_TL]] — 23 atributos (1 PKs, 9 BICC)
- [[fa_additions_vl|FA_ADDITIONS_VL]] — 2 atributos (1 BICC)
- [[fa_balances_extract|FA_BALANCES_EXTRACT]] — 3 atributos
- [[fa_bonus_rules|FA_BONUS_RULES]] — 2 atributos (1 BICC)
- [[fa_books|FA_BOOKS]] — 88 atributos (1 PKs, 30 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (1 PKs, 2 BICC)
- [[fa_cash_gen_units|FA_CASH_GEN_UNITS]] — 3 atributos (1 BICC)
- [[fa_ceiling_types|FA_CEILING_TYPES]] — 4 atributos (1 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 3 atributos (2 BICC)
- [[fa_deprn_extract|FA_DEPRN_EXTRACT]] — 3 atributos
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 9 atributos (2 BICC)
- [[fa_flat_rates|FA_FLAT_RATES]] — 4 atributos (2 BICC)
- [[fa_methods|FA_METHODS]] — 7 atributos (3 BICC)
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 48 atributos (1 PKs, 3 BICC)
- [[fa_trx_extract|FA_TRX_EXTRACT]] — 3 atributos
- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 3 | AdditionAssetNumber | ASSET_NUMBER | — | ✅ |
| 4 | AdditionAssetType | ASSET_TYPE | — | ✅ |
| 5 | AdditionCommitment | COMMITMENT | — | ✅ |
| 6 | AdditionContext | CONTEXT | — | — |
| 7 | AdditionCreatedBy | CREATED_BY | — | ✅ |
| 8 | AdditionCreationDate | CREATION_DATE | — | ✅ |
| 9 | AdditionCurrentUnits | CURRENT_UNITS | — | ✅ |
| 10 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 11 | AdditionInUseFlag | IN_USE_FLAG | — | ✅ |
| 12 | AdditionInventorial | INVENTORIAL | — | ✅ |
| 13 | AdditionInvestmentLaw | INVESTMENT_LAW | — | ✅ |
| 14 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | AdditionLeaseId | LEASE_ID | — | — |
| 18 | AdditionManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 19 | AdditionModelNumber | MODEL_NUMBER | — | ✅ |
| 20 | AdditionNewUsed | NEW_USED | — | ✅ |
| 21 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | AdditionOwnedLeased | OWNED_LEASED | — | ✅ |
| 23 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 24 | AdditionPrntAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 25 | AdditionPrntAssetId | ASSET_ID | — | — |
| 26 | AdditionPrntAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 27 | AdditionPrntAssetNumber | ASSET_NUMBER | — | ✅ |
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
| 38 | AdditionPrntLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
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
| 52 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | ✅ |
| 53 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | ✅ |
| 54 | AdditionSerialNumber | SERIAL_NUMBER | — | ✅ |
| 55 | AdditionTagNumber | TAG_NUMBER | — | ✅ |
| 56 | AssetId | ASSET_ID | 🔑 | ✅ |

### [[fa_additions_tl|FA_ADDITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionTLAssetId | ASSET_ID | — | ✅ |
| 2 | AdditionTLCreatedBy | CREATED_BY | — | ✅ |
| 3 | AdditionTLCreationDate | CREATION_DATE | — | ✅ |
| 4 | AdditionTLDescription | DESCRIPTION | — | ✅ |
| 5 | AdditionTLLangAssetId | ASSET_ID | — | — |
| 6 | AdditionTLLangCreatedBy | CREATED_BY | — | — |
| 7 | AdditionTLLangCreationDate | CREATION_DATE | — | — |
| 8 | AdditionTLLangDescription | DESCRIPTION | — | — |
| 9 | AdditionTLLangLanguage | LANGUAGE | — | — |
| 10 | AdditionTLLangLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | AdditionTLLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | AdditionTLLangLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | AdditionTLLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | AdditionTLLangSourceLang | SOURCE_LANG | — | — |
| 15 | AdditionTLLanguage | LANGUAGE | 🔑 | ✅ |
| 16 | AdditionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AdditionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | AdditionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | AdditionTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | AdditionTLSourceLang | SOURCE_LANG | — | ✅ |
| 21 | AssetId1 | ASSET_ID | — | — |
| 22 | Language | LANGUAGE | — | — |
| 23 | ParentAdditionTLDescription | DESCRIPTION | — | ✅ |

### [[fa_additions_vl|FA_ADDITIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupAdditionPEOAssetId1 | ASSET_ID | — | — |
| 2 | GroupAdditionPEODescription | DESCRIPTION | — | ✅ |

### [[fa_balances_extract|FA_BALANCES_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalancesExtractPEOAssetId | ASSET_ID | — | — |
| 2 | BalancesExtractPEOBalancesExtractId | BALANCES_EXTRACT_ID | — | — |
| 3 | BalancesExtractPEOPeriodCounter | PERIOD_COUNTER | — | — |

### [[fa_bonus_rules|FA_BONUS_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BonusRuleId | BONUS_RULE_ID | — | — |
| 2 | BonusRulePEOBonusRule | BONUS_RULE | — | ✅ |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FaBooksAdjustedCapacity | ADJUSTED_CAPACITY | — | ✅ |
| 2 | FaBooksAdjustedCost | ADJUSTED_COST | — | ✅ |
| 3 | FaBooksAdjustedRecoverableCost | ADJUSTED_RECOVERABLE_COST | — | — |
| 4 | FaBooksAllocateToFullyRetFlag | ALLOCATE_TO_FULLY_RET_FLAG | — | — |
| 5 | FaBooksAllocateToFullyRsvFlag | ALLOCATE_TO_FULLY_RSV_FLAG | — | — |
| 6 | FaBooksAllowedDeprnLimit | ALLOWED_DEPRN_LIMIT | — | ✅ |
| 7 | FaBooksAllowedDeprnLimitAmount | ALLOWED_DEPRN_LIMIT_AMOUNT | — | ✅ |
| 8 | FaBooksAnnualDeprnRoundingFlag | ANNUAL_DEPRN_ROUNDING_FLAG | — | — |
| 9 | FaBooksAssetId | ASSET_ID | — | — |
| 10 | FaBooksBonusRuleId | BONUS_RULE_ID | — | — |
| 11 | FaBooksBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 12 | FaBooksCapitalizeFlag | CAPITALIZE_FLAG | — | — |
| 13 | FaBooksCeilingTypeId | CEILING_TYPE_ID | — | — |
| 14 | FaBooksCipCost | CIP_COST | — | — |
| 15 | FaBooksConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 16 | FaBooksConversionDate | CONVERSION_DATE | — | ✅ |
| 17 | FaBooksCost | COST | — | ✅ |
| 18 | FaBooksCreatedBy | CREATED_BY | — | — |
| 19 | FaBooksCreationDate | CREATION_DATE | — | — |
| 20 | FaBooksDateEffective | DATE_EFFECTIVE | — | ✅ |
| 21 | FaBooksDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 22 | FaBooksDatePlacedInService | DATE_PLACED_IN_SERVICE | — | ✅ |
| 23 | FaBooksDepreciateFlag | DEPRECIATE_FLAG | — | ✅ |
| 24 | FaBooksDepreciationOption | DEPRECIATION_OPTION | — | — |
| 25 | FaBooksDeprnLimitType | DEPRN_LIMIT_TYPE | — | ✅ |
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
| 39 | FaBooksGroupAssetId | GROUP_ASSET_ID | — | ✅ |
| 40 | FaBooksLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | FaBooksLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | FaBooksLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | FaBooksLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 44 | FaBooksLowValueAssetFlag | LOW_VALUE_ASSET_FLAG | — | ✅ |
| 45 | FaBooksLtdCostOfRemoval | LTD_COST_OF_REMOVAL | — | — |
| 46 | FaBooksLtdProceeds | LTD_PROCEEDS | — | — |
| 47 | FaBooksMemberRollupFlag | MEMBER_ROLLUP_FLAG | — | — |
| 48 | FaBooksMethodId | METHOD_ID | — | — |
| 49 | FaBooksObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | FaBooksOldAdjustedCapacity | OLD_ADJUSTED_CAPACITY | — | — |
| 51 | FaBooksOldAdjustedCost | OLD_ADJUSTED_COST | — | — |
| 52 | FaBooksOriginalCost | ORIGINAL_COST | — | ✅ |
| 53 | FaBooksOriginalDeprnStartDate | ORIGINAL_DEPRN_START_DATE | — | ✅ |
| 54 | FaBooksOverDepreciateOption | OVER_DEPRECIATE_OPTION | — | — |
| 55 | FaBooksPercentSalvageValue | PERCENT_SALVAGE_VALUE | — | ✅ |
| 56 | FaBooksPeriodCounterCapitalized | PERIOD_COUNTER_CAPITALIZED | — | — |
| 57 | FaBooksPeriodCounterFullyReserved | PERIOD_COUNTER_FULLY_RESERVED | — | — |
| 58 | FaBooksPeriodCounterFullyRetired | PERIOD_COUNTER_FULLY_RETIRED | — | — |
| 59 | FaBooksPeriodCounterLifeComplete | PERIOD_COUNTER_LIFE_COMPLETE | — | — |
| 60 | FaBooksPriorEofyReserve | PRIOR_EOFY_RESERVE | — | — |
| 61 | FaBooksProductionCapacity | PRODUCTION_CAPACITY | — | ✅ |
| 62 | FaBooksProrateDate | PRORATE_DATE | — | ✅ |
| 63 | FaBooksRateAdjustmentFactor | RATE_ADJUSTMENT_FACTOR | — | — |
| 64 | FaBooksRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 65 | FaBooksRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 66 | FaBooksRecoverableCost | RECOVERABLE_COST | — | ✅ |
| 67 | FaBooksReduceAdditionFlag | REDUCE_ADDITION_FLAG | — | — |
| 68 | FaBooksReduceAdjustmentFlag | REDUCE_ADJUSTMENT_FLAG | — | — |
| 69 | FaBooksReduceRetirementFlag | REDUCE_RETIREMENT_FLAG | — | — |
| 70 | FaBooksReductionRate | REDUCTION_RATE | — | ✅ |
| 71 | FaBooksRemainingLife1 | REMAINING_LIFE1 | — | — |
| 72 | FaBooksRemainingLife2 | REMAINING_LIFE2 | — | — |
| 73 | FaBooksRetirementDeprnOption | RETIREMENT_DEPRN_OPTION | — | — |
| 74 | FaBooksRetirementId | RETIREMENT_ID | — | — |
| 75 | FaBooksRevalAmortizationBasis | REVAL_AMORTIZATION_BASIS | — | ✅ |
| 76 | FaBooksRevalCeiling | REVAL_CEILING | — | — |
| 77 | FaBooksSalvageType | SALVAGE_TYPE | — | ✅ |
| 78 | FaBooksSalvageValue | SALVAGE_VALUE | — | ✅ |
| 79 | FaBooksShortFiscalYearFlag | SHORT_FISCAL_YEAR_FLAG | — | ✅ |
| 80 | FaBooksTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 81 | FaBooksTerminalGainLossAmount | TERMINAL_GAIN_LOSS_AMOUNT | — | — |
| 82 | FaBooksTerminalGainLossFlag | TERMINAL_GAIN_LOSS_FLAG | — | — |
| 83 | FaBooksTrackingMethod | TRACKING_METHOD | — | — |
| 84 | FaBooksTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |
| 85 | FaBooksTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 86 | FaBooksUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 87 | FaBooksUnrevaluedCost | UNREVALUED_COST | — | — |
| 88 | FaBooksYtdProceeds | YTD_PROCEEDS | — | — |

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
| 20 | BkCtrlBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
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
| 80 | BkCtrlSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 81 | BkCtrlUsePercentSalvageValueFlag | USE_PERCENT_SALVAGE_VALUE_FLAG | — | — |

### [[fa_cash_gen_units|FA_CASH_GEN_UNITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashGenUnitPEOCashGeneratingUnit | CASH_GENERATING_UNIT | — | ✅ |
| 2 | CashGenUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | CashGeneratingUnitId | CASH_GENERATING_UNIT_ID | — | — |

### [[fa_ceiling_types|FA_CEILING_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CeilingTypePEOCeilingName | CEILING_NAME | — | ✅ |
| 2 | CeilingTypePEOCeilingType | CEILING_TYPE | — | — |
| 3 | CeilingTypePEOCeilingTypeId | CEILING_TYPE_ID | — | — |
| 4 | CeilingTypePEODescription | DESCRIPTION | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateConventionTypePEODescription | DESCRIPTION | — | ✅ |
| 3 | ProrateConventionTypePEOProrateConventionCode | PRORATE_CONVENTION_CODE | — | ✅ |

### [[fa_deprn_extract|FA_DEPRN_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnExtractPEOAssetId | ASSET_ID | — | — |
| 2 | DeprnExtractPEODeprnExtractId | DEPRN_EXTRACT_ID | — | — |
| 3 | DeprnExtractPEOPeriodCounter | PERIOD_COUNTER | — | — |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPeriodFullyResPEOPeriodName | PERIOD_NAME | — | ✅ |
| 3 | DeprnPeriodFullyRetiredPEOBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | DeprnPeriodFullyRetiredPEOFiscalYear | FISCAL_YEAR | — | — |
| 5 | DeprnPeriodFullyRetiredPEOPeriodCounter | PERIOD_COUNTER | — | — |
| 6 | DeprnPeriodFullyRetiredPEOPeriodName | PERIOD_NAME | — | ✅ |
| 7 | DeprnPeriodFullyRetiredPEOPeriodNum | PERIOD_NUM | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PeriodCounter | PERIOD_COUNTER | — | — |

### [[fa_flat_rates|FA_FLAT_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationFlatRatePEOAdjustedRate | ADJUSTED_RATE | — | ✅ |
| 2 | DepreciationFlatRatePEOBasicRate | BASIC_RATE | — | ✅ |
| 3 | FlatRateId | FLAT_RATE_ID | — | — |
| 4 | MethodId1 | METHOD_ID | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepreciationMethodPEODeprnBasisRule | DEPRN_BASIS_RULE_ID | — | ✅ |
| 2 | DepreciationMethodPEOLifeInMonths | LIFE_IN_MONTHS | — | ✅ |
| 3 | DepreciationMethodPEOMethodCode | METHOD_CODE | — | — |
| 4 | DepreciationMethodPEOName | NAME | — | ✅ |
| 5 | MethodId | METHOD_ID | — | — |
| 6 | ProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 7 | UseLifeInPeriodsFlag | USE_LIFE_IN_PERIODS_FLAG | — | — |

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
| 10 | TrxHdrInLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | TrxHdrInLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | TrxHdrInLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | TrxHdrInMassReferenceId | MASS_REFERENCE_ID | — | — |
| 14 | TrxHdrInMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 15 | TrxHdrInMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 16 | TrxHdrInObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TrxHdrInSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 18 | TrxHdrInTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 19 | TrxHdrInTransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |
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
| 34 | TrxHdrOutLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
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

### [[fa_trx_extract|FA_TRX_EXTRACT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtractPEOAssetId | ASSET_ID | — | — |
| 2 | TrxExtractPEOPeriodCounter | PERIOD_COUNTER | — | — |
| 3 | TrxExtractPEOTrxExtractId | TRX_EXTRACT_ID | — | — |

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 2 | SetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 3 | SetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 4 | SetIdAssignmentSetId | SET_ID | — | — |

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
