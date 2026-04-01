---
id: DOC-OTHER-PVO-AssetRetirementPVO
doc_type: system-doc
title: "AssetRetirementPVO — PVO Cross-Module"
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
  - AssetRetirementPVO
  - assetretirementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetRetirementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Retirement. Acessa as tabelas: FA_ADDITIONS_B, FA_ASSET_RETIREMENTS_V, FA_BOOK_CONTROLS (+5).

**Caminho:** `FscmTopModelAM.FinFaRetRetirementsAM.AssetRetirementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 248 | 8 | 1 | 24 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 50 atributos (2 BICC)
- [[fa_asset_retirements_v|FA_ASSET_RETIREMENTS_V]] — 57 atributos (1 PKs, 14 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 92 atributos (1 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 6 atributos (2 BICC)
- [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]] — 3 atributos
- [[fa_methods|FA_METHODS]] — 13 atributos (2 BICC)
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 18 atributos (1 BICC)
- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 9 atributos (2 BICC)

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
| 12 | AdditionInUseFlag | IN_USE_FLAG | — | — |
| 13 | AdditionInventorial | INVENTORIAL | — | — |
| 14 | AdditionInvestmentLaw | INVESTMENT_LAW | — | — |
| 15 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AdditionLeaseId | LEASE_ID | — | — |
| 19 | AdditionManufacturerName | MANUFACTURER_NAME | — | — |
| 20 | AdditionModelNumber | MODEL_NUMBER | — | — |
| 21 | AdditionNewUsed | NEW_USED | — | — |
| 22 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AdditionOwnedLeased | OWNED_LEASED | — | — |
| 24 | AdditionParentAssetId | PARENT_ASSET_ID | — | — |
| 25 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 26 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 27 | AdditionSerialNumber | SERIAL_NUMBER | — | — |
| 28 | AdditionTagNumber | TAG_NUMBER | — | — |
| 29 | AdditionTrdAsstIdAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 30 | AdditionTrdAsstIdAssetId | ASSET_ID | — | — |
| 31 | AdditionTrdAsstIdAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 32 | AdditionTrdAsstIdAssetNumber | ASSET_NUMBER | — | ✅ |
| 33 | AdditionTrdAsstIdAssetType | ASSET_TYPE | — | — |
| 34 | AdditionTrdAsstIdCommitment | COMMITMENT | — | — |
| 35 | AdditionTrdAsstIdContext | CONTEXT | — | — |
| 36 | AdditionTrdAsstIdCurrentUnits | CURRENT_UNITS | — | — |
| 37 | AdditionTrdAsstIdDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 38 | AdditionTrdAsstIdInUseFlag | IN_USE_FLAG | — | — |
| 39 | AdditionTrdAsstIdInventorial | INVENTORIAL | — | — |
| 40 | AdditionTrdAsstIdInvestmentLaw | INVESTMENT_LAW | — | — |
| 41 | AdditionTrdAsstIdLeaseId | LEASE_ID | — | — |
| 42 | AdditionTrdAsstIdManufacturerName | MANUFACTURER_NAME | — | — |
| 43 | AdditionTrdAsstIdModelNumber | MODEL_NUMBER | — | — |
| 44 | AdditionTrdAsstIdNewUsed | NEW_USED | — | — |
| 45 | AdditionTrdAsstIdOwnedLeased | OWNED_LEASED | — | — |
| 46 | AdditionTrdAsstIdParentAssetId | PARENT_ASSET_ID | — | — |
| 47 | AdditionTrdAsstIdProperty12451250Code | PROPERTY_1245_1250_CODE | — | — |
| 48 | AdditionTrdAsstIdPropertyTypeCode | PROPERTY_TYPE_CODE | — | — |
| 49 | AdditionTrdAsstIdSerialNumber | SERIAL_NUMBER | — | — |
| 50 | AdditionTrdAsstIdTagNumber | TAG_NUMBER | — | — |

### [[fa_asset_retirements_v|FA_ASSET_RETIREMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetRetirementsAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | AssetRetirementsAssetId | ASSET_ID | — | — |
| 3 | AssetRetirementsBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 4 | AssetRetirementsBookTypeCode | BOOK_TYPE_CODE | — | — |
| 5 | AssetRetirementsCallingInterface | CALLING_INTERFACE | — | — |
| 6 | AssetRetirementsCostOfRemoval | COST_OF_REMOVAL | — | — |
| 7 | AssetRetirementsCostRetired | COST_RETIRED | — | — |
| 8 | AssetRetirementsCreatedBy | CREATED_BY | — | — |
| 9 | AssetRetirementsCreationDate | CREATION_DATE | — | — |
| 10 | AssetRetirementsDateEffective | DATE_EFFECTIVE | — | — |
| 11 | AssetRetirementsDateRetired | DATE_RETIRED | — | — |
| 12 | AssetRetirementsEofyReserve | EOFY_RESERVE | — | — |
| 13 | AssetRetirementsEventId | EVENT_ID | — | — |
| 14 | AssetRetirementsGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 15 | AssetRetirementsGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | ✅ |
| 16 | AssetRetirementsImpairReserveRetired | IMPAIR_RESERVE_RETIRED | — | — |
| 17 | AssetRetirementsInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 18 | AssetRetirementsItcRecaptureId | ITC_RECAPTURE_ID | — | — |
| 19 | AssetRetirementsItcRecaptured | ITC_RECAPTURED | — | — |
| 20 | AssetRetirementsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | AssetRetirementsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | AssetRetirementsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | AssetRetirementsLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 24 | AssetRetirementsMassReferenceId | MASS_REFERENCE_ID | — | — |
| 25 | AssetRetirementsMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 26 | AssetRetirementsMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 27 | AssetRetirementsNbvRetired | NBV_RETIRED | — | — |
| 28 | AssetRetirementsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | AssetRetirementsProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 30 | AssetRetirementsRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 31 | AssetRetirementsRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 32 | AssetRetirementsRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 33 | AssetRetirementsReductionRate | REDUCTION_RATE | — | — |
| 34 | AssetRetirementsReferenceNum | REFERENCE_NUM | — | ✅ |
| 35 | AssetRetirementsReserveRetired | RESERVE_RETIRED | — | — |
| 36 | AssetRetirementsRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 37 | AssetRetirementsRetirementId | RETIREMENT_ID | — | — |
| 38 | AssetRetirementsRetirementTypeCode | RETIREMENT_TYPE_CODE | — | ✅ |
| 39 | AssetRetirementsRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 40 | AssetRetirementsSoldTo | SOLD_TO | — | ✅ |
| 41 | AssetRetirementsSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 42 | AssetRetirementsStatus | STATUS | — | ✅ |
| 43 | AssetRetirementsStlDeprnAmount | STL_DEPRN_AMOUNT | — | ✅ |
| 44 | AssetRetirementsStlMethodId | STL_METHOD_ID | — | — |
| 45 | AssetRetirementsTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 46 | AssetRetirementsTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 47 | AssetRetirementsTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 48 | AssetRetirementsTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 49 | AssetRetirementsTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 50 | AssetRetirementsTransactionKey | TRANSACTION_KEY | — | ✅ |
| 51 | AssetRetirementsTransactionName | TRANSACTION_NAME | — | ✅ |
| 52 | AssetRetirementsTransactionSubtype | TRANSACTION_SUBTYPE | — | ✅ |
| 53 | AssetRetirementsTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 54 | AssetRetirementsTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 55 | AssetRetirementsUnits | UNITS | — | ✅ |
| 56 | AssetRetirementsUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |
| 57 | TransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BkCtrlAccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | BkCtrlAllowBackdatedTransfersFlag | ALLOW_BACKDATED_TRANSFERS_FLAG | — | — |
| 3 | BkCtrlAllowBonusDeprnFlag | ALLOW_BONUS_DEPRN_FLAG | — | — |
| 4 | BkCtrlAllowCipAssetsFlag | ALLOW_CIP_ASSETS_FLAG | — | — |
| 5 | BkCtrlAllowCipDepGroupFlag | ALLOW_CIP_DEP_GROUP_FLAG | — | — |
| 6 | BkCtrlAllowCipMemberFlag | ALLOW_CIP_MEMBER_FLAG | — | — |
| 7 | BkCtrlAllowCostCeiling | ALLOW_COST_CEILING | — | — |
| 8 | BkCtrlAllowCostSignChangeFlag | ALLOW_COST_SIGN_CHANGE_FLAG | — | — |
| 9 | BkCtrlAllowDeprnAdjustments | ALLOW_DEPRN_ADJUSTMENTS | — | — |
| 10 | BkCtrlAllowDeprnExpCeiling | ALLOW_DEPRN_EXP_CEILING | — | — |
| 11 | BkCtrlAllowGroupDeprnFlag | ALLOW_GROUP_DEPRN_FLAG | — | — |
| 12 | BkCtrlAllowImpairmentFlag | ALLOW_IMPAIRMENT_FLAG | — | — |
| 13 | BkCtrlAllowIntercoGroupFlag | ALLOW_INTERCO_GROUP_FLAG | — | — |
| 14 | BkCtrlAllowMassChanges | ALLOW_MASS_CHANGES | — | — |
| 15 | BkCtrlAllowMassCopy | ALLOW_MASS_COPY | — | — |
| 16 | BkCtrlAllowMemberTrackingFlag | ALLOW_MEMBER_TRACKING_FLAG | — | — |
| 17 | BkCtrlAllowPurgeFlag | ALLOW_PURGE_FLAG | — | — |
| 18 | BkCtrlAllowRevalFlag | ALLOW_REVAL_FLAG | — | — |
| 19 | BkCtrlAmortizeFlag | AMORTIZE_FLAG | — | — |
| 20 | BkCtrlAmortizeRevalReserveFlag | AMORTIZE_REVAL_RESERVE_FLAG | — | — |
| 21 | BkCtrlBookClass | BOOK_CLASS | — | — |
| 22 | BkCtrlBookControlId | BOOK_CONTROL_ID | — | — |
| 23 | BkCtrlBookTypeCode | BOOK_TYPE_CODE | — | — |
| 24 | BkCtrlBookTypeName | BOOK_TYPE_NAME | — | — |
| 25 | BkCtrlCapitalGainThreshold | CAPITAL_GAIN_THRESHOLD | — | — |
| 26 | BkCtrlCopyAdditionsFlag | COPY_ADDITIONS_FLAG | — | — |
| 27 | BkCtrlCopyAdjustmentsFlag | COPY_ADJUSTMENTS_FLAG | — | — |
| 28 | BkCtrlCopyAllCostAdjustmentsFlag | COPY_ALL_COST_ADJUSTMENTS_FLAG | — | — |
| 29 | BkCtrlCopyAmortAdajExpFlag | COPY_AMORT_ADAJ_EXP_FLAG | — | — |
| 30 | BkCtrlCopyGroupAdditionFlag | COPY_GROUP_ADDITION_FLAG | — | — |
| 31 | BkCtrlCopyGroupAssignmentFlag | COPY_GROUP_ASSIGNMENT_FLAG | — | — |
| 32 | BkCtrlCopyRetirementsFlag | COPY_RETIREMENTS_FLAG | — | — |
| 33 | BkCtrlCopySalvageValueFlag | COPY_SALVAGE_VALUE_FLAG | — | — |
| 34 | BkCtrlCostOfRemovalClearingAcct | COST_OF_REMOVAL_CLEARING_ACCT | — | — |
| 35 | BkCtrlCostOfRemovalGainAcct | COST_OF_REMOVAL_GAIN_ACCT | — | — |
| 36 | BkCtrlCostOfRemovalLossAcct | COST_OF_REMOVAL_LOSS_ACCT | — | — |
| 37 | BkCtrlCreateAccountingRequestId | CREATE_ACCOUNTING_REQUEST_ID | — | — |
| 38 | BkCtrlCreatedBy | CREATED_BY | — | — |
| 39 | BkCtrlCreationDate | CREATION_DATE | — | — |
| 40 | BkCtrlCurrentFiscalYear | CURRENT_FISCAL_YEAR | — | — |
| 41 | BkCtrlDateIneffective | DATE_INEFFECTIVE | — | — |
| 42 | BkCtrlDefaultDpisToInvDateFlag | DEFAULT_DPIS_TO_INV_DATE_FLAG | — | — |
| 43 | BkCtrlDefaultLifeExtensionCeiling | DEFAULT_LIFE_EXTENSION_CEILING | — | — |
| 44 | BkCtrlDefaultLifeExtensionFactor | DEFAULT_LIFE_EXTENSION_FACTOR | — | — |
| 45 | BkCtrlDefaultMaxFullyRsvdRevals | DEFAULT_MAX_FULLY_RSVD_REVALS | — | — |
| 46 | BkCtrlDefaultRevalFullyRsvdFlag | DEFAULT_REVAL_FULLY_RSVD_FLAG | — | — |
| 47 | BkCtrlDeferredDeprnExpenseAcct | DEFERRED_DEPRN_EXPENSE_ACCT | — | — |
| 48 | BkCtrlDeferredDeprnReserveAcct | DEFERRED_DEPRN_RESERVE_ACCT | — | — |
| 49 | BkCtrlDeprFirstYearRetFlag | DEPR_FIRST_YEAR_RET_FLAG | — | — |
| 50 | BkCtrlDeprnAdjustmentAcct | DEPRN_ADJUSTMENT_ACCT | — | — |
| 51 | BkCtrlDeprnAllocationCode | DEPRN_ALLOCATION_CODE | — | — |
| 52 | BkCtrlDeprnCalendar | DEPRN_CALENDAR | — | — |
| 53 | BkCtrlDeprnRequestId | DEPRN_REQUEST_ID | — | — |
| 54 | BkCtrlDeprnStatus | DEPRN_STATUS | — | — |
| 55 | BkCtrlDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | — |
| 56 | BkCtrlFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 57 | BkCtrlFlexbuilderDefaultsCcid | FLEXBUILDER_DEFAULTS_CCID | — | — |
| 58 | BkCtrlFullyReservedFlag | FULLY_RESERVED_FLAG | — | — |
| 59 | BkCtrlGlPostingAllowedFlag | GL_POSTING_ALLOWED_FLAG | — | — |
| 60 | BkCtrlImmediateCopyFlag | IMMEDIATE_COPY_FLAG | — | — |
| 61 | BkCtrlInitialDate | INITIAL_DATE | — | — |
| 62 | BkCtrlInitialPeriodCounter | INITIAL_PERIOD_COUNTER | — | — |
| 63 | BkCtrlItcAllowedFlag | ITC_ALLOWED_FLAG | — | — |
| 64 | BkCtrlLastDeprnRunDate | LAST_DEPRN_RUN_DATE | — | — |
| 65 | BkCtrlLastMassCopyPeriodCounter | LAST_MASS_COPY_PERIOD_COUNTER | — | — |
| 66 | BkCtrlLastPeriodCounter | LAST_PERIOD_COUNTER | — | — |
| 67 | BkCtrlLastPurgePeriodCounter | LAST_PURGE_PERIOD_COUNTER | — | — |
| 68 | BkCtrlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | BkCtrlLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | BkCtrlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | BkCtrlMassCopySourceBook | MASS_COPY_SOURCE_BOOK | — | — |
| 72 | BkCtrlMassRequestId | MASS_REQUEST_ID | — | — |
| 73 | BkCtrlMcSourceFlag | MC_SOURCE_FLAG | — | — |
| 74 | BkCtrlNbvAmountThreshold | NBV_AMOUNT_THRESHOLD | — | — |
| 75 | BkCtrlNbvFractionThreshold | NBV_FRACTION_THRESHOLD | — | — |
| 76 | BkCtrlNbvRetiredGainAcct | NBV_RETIRED_GAIN_ACCT | — | — |
| 77 | BkCtrlNbvRetiredLossAcct | NBV_RETIRED_LOSS_ACCT | — | — |
| 78 | BkCtrlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 79 | BkCtrlProceedsOfSaleClearingAcct | PROCEEDS_OF_SALE_CLEARING_ACCT | — | — |
| 80 | BkCtrlProceedsOfSaleGainAcct | PROCEEDS_OF_SALE_GAIN_ACCT | — | — |
| 81 | BkCtrlProceedsOfSaleLossAcct | PROCEEDS_OF_SALE_LOSS_ACCT | — | — |
| 82 | BkCtrlProrateCalendar | PRORATE_CALENDAR | — | — |
| 83 | BkCtrlRetireRevalReserveFlag | RETIRE_REVAL_RESERVE_FLAG | — | — |
| 84 | BkCtrlRevalDeprnReserveFlag | REVAL_DEPRN_RESERVE_FLAG | — | — |
| 85 | BkCtrlRevalRsvRetiredGainAcct | REVAL_RSV_RETIRED_GAIN_ACCT | — | — |
| 86 | BkCtrlRevalRsvRetiredLossAcct | REVAL_RSV_RETIRED_LOSS_ACCT | — | — |
| 87 | BkCtrlRevalYtdDeprnFlag | REVAL_YTD_DEPRN_FLAG | — | — |
| 88 | BkCtrlRoundAnnualDepreciation | ROUND_ANNUAL_DEPRECIATION | — | — |
| 89 | BkCtrlSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 90 | BkCtrlSorpEnabledFlag | SORP_ENABLED_FLAG | — | — |
| 91 | BkCtrlUseNbvThresholdFlag | USE_NBV_THRESHOLD_FLAG | — | — |
| 92 | BkCtrlUsePercentSalvageValueFlag | USE_PERCENT_SALVAGE_VALUE_FLAG | — | — |

### [[fa_convention_types|FA_CONVENTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProrateConventionConventionTypeId | CONVENTION_TYPE_ID | — | — |
| 2 | ProrateConventionDeprWhenAcquiredFlag | DEPR_WHEN_ACQUIRED_FLAG | — | — |
| 3 | ProrateConventionDescription | DESCRIPTION | — | ✅ |
| 4 | ProrateConventionFiscalYearName | FISCAL_YEAR_NAME | — | — |
| 5 | ProrateConventionProrateConventionCode | PRORATE_CONVENTION_CODE | — | ✅ |
| 6 | ProrateConventionSetId | SET_ID | — | — |

### [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTrxnBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | InvTrxnInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 3 | InvTrxnTransactionType | TRANSACTION_TYPE | — | — |

### [[fa_methods|FA_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnMethdDepreciateLastyearFlag | DEPRECIATE_LASTYEAR_FLAG | — | — |
| 2 | DeprnMethdDeprnBasisRule | DEPRN_BASIS_RULE | — | — |
| 3 | DeprnMethdDeprnBasisRuleId | DEPRN_BASIS_RULE_ID | — | — |
| 4 | DeprnMethdExcludeSalvageValueFlag | EXCLUDE_SALVAGE_VALUE_FLAG | — | — |
| 5 | DeprnMethdLifeInMonths | LIFE_IN_MONTHS | — | — |
| 6 | DeprnMethdMethodCode | METHOD_CODE | — | ✅ |
| 7 | DeprnMethdMethodId | METHOD_ID | — | — |
| 8 | DeprnMethdName | NAME | — | ✅ |
| 9 | DeprnMethdPolishAdjCalcBasisFlag | POLISH_ADJ_CALC_BASIS_FLAG | — | — |
| 10 | DeprnMethdProratePeriodsPerYear | PRORATE_PERIODS_PER_YEAR | — | — |
| 11 | DeprnMethdRateSourceRule | RATE_SOURCE_RULE | — | — |
| 12 | DeprnMethdSetId | SET_ID | — | — |
| 13 | DeprnMethdStlMethodFlag | STL_METHOD_FLAG | — | — |

### [[fa_transaction_headers|FA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxnHdrAmortizationStartDate | AMORTIZATION_START_DATE | — | — |
| 2 | TrxnHdrAssetId | ASSET_ID | — | — |
| 3 | TrxnHdrBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | TrxnHdrCallingInterface | CALLING_INTERFACE | — | — |
| 5 | TrxnHdrDateEffective | DATE_EFFECTIVE | — | — |
| 6 | TrxnHdrEventId | EVENT_ID | — | — |
| 7 | TrxnHdrInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 8 | TrxnHdrMassReferenceId | MASS_REFERENCE_ID | — | — |
| 9 | TrxnHdrMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 10 | TrxnHdrMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 11 | TrxnHdrSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | — |
| 12 | TrxnHdrTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 13 | TrxnHdrTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 14 | TrxnHdrTransactionKey | TRANSACTION_KEY | — | — |
| 15 | TrxnHdrTransactionName | TRANSACTION_NAME | — | — |
| 16 | TrxnHdrTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 17 | TrxnHdrTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 18 | TrxnHdrTrxReferenceId | TRX_REFERENCE_ID | — | — |

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdAssignCreatedBy | CREATED_BY | — | — |
| 2 | SetIdAssignCreationDate | CREATION_DATE | — | — |
| 3 | SetIdAssignDeterminantType | DETERMINANT_TYPE | — | — |
| 4 | SetIdAssignDeterminantValue | DETERMINANT_VALUE | — | — |
| 5 | SetIdAssignLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SetIdAssignLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SetIdAssignLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SetIdAssignReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 9 | SetIdAssignSetId | SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
