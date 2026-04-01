---
id: DOC-OTHER-PVO-AdjustmentTransactionPVO
doc_type: system-doc
title: "AdjustmentTransactionPVO — PVO Cross-Module"
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
  - AdjustmentTransactionPVO
  - adjustmenttransactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentTransactionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Transaction. Acessa as tabelas: FA_ADDITIONS_B, FA_ADJUSTMENTS, FA_ASSET_HISTORY (+10).

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.AdjustmentTransactionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 518 | 13 | 2 | 37 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 82 atributos (5 BICC)
- [[fa_adjustments|FA_ADJUSTMENTS]] — 25 atributos (2 PKs, 10 BICC)
- [[fa_asset_history|FA_ASSET_HISTORY]] — 18 atributos
- [[fa_asset_invoices|FA_ASSET_INVOICES]] — 46 atributos (3 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (1 BICC)
- [[fa_convention_types|FA_CONVENTION_TYPES]] — 12 atributos (1 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 20 atributos (2 BICC)
- [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]] — 19 atributos (1 BICC)
- [[fa_invoice_transactions|FA_INVOICE_TRANSACTIONS]] — 8 atributos (1 BICC)
- [[fa_methods|FA_METHODS]] — 19 atributos (1 BICC)
- [[fa_retirements|FA_RETIREMENTS]] — 72 atributos (1 BICC)
- [[fa_transaction_headers|FA_TRANSACTION_HEADERS]] — 90 atributos (10 BICC)
- [[fa_trx_references|FA_TRX_REFERENCES]] — 26 atributos (1 BICC)

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

### [[fa_adjustments|FA_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 3 | AdjustmentAnnualizedAdjustment | ANNUALIZED_ADJUSTMENT | — | — |
| 4 | AdjustmentAssetId | ASSET_ID | — | — |
| 5 | AdjustmentAssetInvoiceId | ASSET_INVOICE_ID | — | — |
| 6 | AdjustmentBookTypeCode | BOOK_TYPE_CODE | — | — |
| 7 | AdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 8 | AdjustmentCreatedBy | CREATED_BY | — | — |
| 9 | AdjustmentCreationDate | CREATION_DATE | — | — |
| 10 | AdjustmentDebitCreditFlag | DEBIT_CREDIT_FLAG | — | ✅ |
| 11 | AdjustmentDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 12 | AdjustmentDistributionId | DISTRIBUTION_ID | — | — |
| 13 | AdjustmentInsertionOrder | INSERTION_ORDER | — | — |
| 14 | AdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | AdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | AdjustmentLineId | ADJUSTMENT_LINE_ID | 🔑 | ✅ |
| 18 | AdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | AdjustmentPeriodCounterAdjusted | PERIOD_COUNTER_ADJUSTED | — | — |
| 20 | AdjustmentPeriodCounterCreated | PERIOD_COUNTER_CREATED | — | — |
| 21 | AdjustmentSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 22 | AdjustmentSourceLineId | SOURCE_LINE_ID | — | — |
| 23 | AdjustmentSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 24 | AdjustmentTrackMemberFlag | TRACK_MEMBER_FLAG | — | ✅ |
| 25 | TransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

### [[fa_asset_history|FA_ASSET_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NewFaHisAssetId | ASSET_ID | — | — |
| 2 | NewFaHisAssetType | ASSET_TYPE | — | — |
| 3 | NewFaHisCategoryId | CATEGORY_ID | — | — |
| 4 | NewFaHisDateEffective | DATE_EFFECTIVE | — | — |
| 5 | NewFaHisDateIneffective | DATE_INEFFECTIVE | — | — |
| 6 | NewFaHisObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | NewFaHisTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 8 | NewFaHisTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 9 | NewFaHisUnits | UNITS | — | — |
| 10 | OldFaHisAssetId | ASSET_ID | — | — |
| 11 | OldFaHisAssetType | ASSET_TYPE | — | — |
| 12 | OldFaHisCategoryId | CATEGORY_ID | — | — |
| 13 | OldFaHisDateEffective | DATE_EFFECTIVE | — | — |
| 14 | OldFaHisDateIneffective | DATE_INEFFECTIVE | — | — |
| 15 | OldFaHisObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | OldFaHisTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 17 | OldFaHisTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 18 | OldFaHisUnits | UNITS | — | — |

### [[fa_asset_invoices|FA_ASSET_INVOICES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetInvoiceApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | — |
| 2 | AssetInvoiceAssetId | ASSET_ID | — | — |
| 3 | AssetInvoiceAssetInvoiceId | ASSET_INVOICE_ID | — | — |
| 4 | AssetInvoiceCreateBatchDate | CREATE_BATCH_DATE | — | — |
| 5 | AssetInvoiceCreateBatchId | CREATE_BATCH_ID | — | — |
| 6 | AssetInvoiceCreatedBy | CREATED_BY | — | — |
| 7 | AssetInvoiceCreationDate | CREATION_DATE | — | — |
| 8 | AssetInvoiceDateEffective | DATE_EFFECTIVE | — | — |
| 9 | AssetInvoiceDateIneffective | DATE_INEFFECTIVE | — | — |
| 10 | AssetInvoiceDeletedFlag | DELETED_FLAG | — | — |
| 11 | AssetInvoiceDepreciateInGroupFlag | DEPRECIATE_IN_GROUP_FLAG | — | — |
| 12 | AssetInvoiceDescription | DESCRIPTION | — | — |
| 13 | AssetInvoiceFeederSystemName | FEEDER_SYSTEM_NAME | — | — |
| 14 | AssetInvoiceFixedAssetsCost | FIXED_ASSETS_COST | — | — |
| 15 | AssetInvoiceInvoiceDate | INVOICE_DATE | — | — |
| 16 | AssetInvoiceInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 17 | AssetInvoiceInvoiceId | INVOICE_ID | — | — |
| 18 | AssetInvoiceInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 19 | AssetInvoiceInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 20 | AssetInvoiceInvoiceTransactionIdIn | INVOICE_TRANSACTION_ID_IN | — | — |
| 21 | AssetInvoiceInvoiceTransactionIdOut | INVOICE_TRANSACTION_ID_OUT | — | — |
| 22 | AssetInvoiceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | AssetInvoiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | AssetInvoiceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | AssetInvoiceMaterialIndicatorFlag | MATERIAL_INDICATOR_FLAG | — | — |
| 26 | AssetInvoiceMergeParentMassAdditionsId | MERGE_PARENT_MASS_ADDITIONS_ID | — | — |
| 27 | AssetInvoiceMergedCode | MERGED_CODE | — | — |
| 28 | AssetInvoiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | AssetInvoiceParentMassAdditionId | PARENT_MASS_ADDITION_ID | — | — |
| 30 | AssetInvoicePayablesBatchName | PAYABLES_BATCH_NAME | — | — |
| 31 | AssetInvoicePayablesCodeCombinationId | PAYABLES_CODE_COMBINATION_ID | — | — |
| 32 | AssetInvoicePayablesCost | PAYABLES_COST | — | — |
| 33 | AssetInvoicePayablesUnits | PAYABLES_UNITS | — | — |
| 34 | AssetInvoicePoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 35 | AssetInvoicePoNumber | PO_NUMBER | — | ✅ |
| 36 | AssetInvoicePoVendorId | PO_VENDOR_ID | — | — |
| 37 | AssetInvoicePostBatchId | POST_BATCH_ID | — | — |
| 38 | AssetInvoicePriorSourceLineId | PRIOR_SOURCE_LINE_ID | — | — |
| 39 | AssetInvoiceProjectAssetLineId | PROJECT_ASSET_LINE_ID | — | — |
| 40 | AssetInvoiceProjectId | PROJECT_ID | — | — |
| 41 | AssetInvoiceSourceLineId | SOURCE_LINE_ID | — | — |
| 42 | AssetInvoiceSplitCode | SPLIT_CODE | — | — |
| 43 | AssetInvoiceSplitMergedCode | SPLIT_MERGED_CODE | — | — |
| 44 | AssetInvoiceSplitParentMassAdditionsId | SPLIT_PARENT_MASS_ADDITIONS_ID | — | — |
| 45 | AssetInvoiceTaskId | TASK_ID | — | — |
| 46 | AssetInvoiceUnrevaluedCost | UNREVALUED_COST | — | — |

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

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnPrdCntAdjBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPrdCntAdjCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 3 | DeprnPrdCntAdjCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 4 | DeprnPrdCntAdjDeprnRun | DEPRN_RUN | — | — |
| 5 | DeprnPrdCntAdjFiscalYear | FISCAL_YEAR | — | — |
| 6 | DeprnPrdCntAdjPeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 7 | DeprnPrdCntAdjPeriodCounter | PERIOD_COUNTER | — | — |
| 8 | DeprnPrdCntAdjPeriodName | PERIOD_NAME | — | ✅ |
| 9 | DeprnPrdCntAdjPeriodNum | PERIOD_NUM | — | — |
| 10 | DeprnPrdCntAdjPeriodOpenDate | PERIOD_OPEN_DATE | — | — |
| 11 | DeprnPrdCntCreBookTypeCode | BOOK_TYPE_CODE | — | — |
| 12 | DeprnPrdCntCreCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 13 | DeprnPrdCntCreCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 14 | DeprnPrdCntCreDeprnRun | DEPRN_RUN | — | — |
| 15 | DeprnPrdCntCreFiscalYear | FISCAL_YEAR | — | — |
| 16 | DeprnPrdCntCrePeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 17 | DeprnPrdCntCrePeriodCounter | PERIOD_COUNTER | — | — |
| 18 | DeprnPrdCntCrePeriodName | PERIOD_NAME | — | ✅ |
| 19 | DeprnPrdCntCrePeriodNum | PERIOD_NUM | — | — |
| 20 | DeprnPrdCntCrePeriodOpenDate | PERIOD_OPEN_DATE | — | — |

### [[fa_distribution_history|FA_DISTRIBUTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistHistAssetId | ASSET_ID | — | — |
| 2 | DistHistAssignedTo | ASSIGNED_TO | — | — |
| 3 | DistHistBookTypeCode | BOOK_TYPE_CODE | — | — |
| 4 | DistHistCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | DistHistCreatedBy | CREATED_BY | — | — |
| 6 | DistHistCreationDate | CREATION_DATE | — | — |
| 7 | DistHistDateEffective | DATE_EFFECTIVE | — | — |
| 8 | DistHistDateIneffective | DATE_INEFFECTIVE | — | — |
| 9 | DistHistDistributionId | DISTRIBUTION_ID | — | — |
| 10 | DistHistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DistHistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DistHistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | DistHistLocationId | LOCATION_ID | — | — |
| 14 | DistHistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DistHistRetirementId | RETIREMENT_ID | — | — |
| 16 | DistHistTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 17 | DistHistTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 18 | DistHistTransactionUnits | TRANSACTION_UNITS | — | — |
| 19 | DistHistUnitsAssigned | UNITS_ASSIGNED | — | — |

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
| 7 | DeprnMthdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
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
| 10 | RetirementDistHistAssetId | ASSET_ID | — | — |
| 11 | RetirementDistHistBonusReserveRetired | BONUS_RESERVE_RETIRED | — | — |
| 12 | RetirementDistHistBookTypeCode | BOOK_TYPE_CODE | — | — |
| 13 | RetirementDistHistCostOfRemoval | COST_OF_REMOVAL | — | — |
| 14 | RetirementDistHistCostRetired | COST_RETIRED | — | — |
| 15 | RetirementDistHistDateEffective | DATE_EFFECTIVE | — | — |
| 16 | RetirementDistHistDateRetired | DATE_RETIRED | — | — |
| 17 | RetirementDistHistEofyReserve | EOFY_RESERVE | — | — |
| 18 | RetirementDistHistGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 19 | RetirementDistHistGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 20 | RetirementDistHistLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 21 | RetirementDistHistNbvRetired | NBV_RETIRED | — | — |
| 22 | RetirementDistHistProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 23 | RetirementDistHistRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 24 | RetirementDistHistRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 25 | RetirementDistHistRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 26 | RetirementDistHistReductionRate | REDUCTION_RATE | — | — |
| 27 | RetirementDistHistReferenceNum | REFERENCE_NUM | — | — |
| 28 | RetirementDistHistReserveRetired | RESERVE_RETIRED | — | — |
| 29 | RetirementDistHistRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 30 | RetirementDistHistRetirementId | RETIREMENT_ID | — | — |
| 31 | RetirementDistHistRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 32 | RetirementDistHistRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 33 | RetirementDistHistSoldTo | SOLD_TO | — | — |
| 34 | RetirementDistHistStatus | STATUS | — | — |
| 35 | RetirementDistHistStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 36 | RetirementDistHistStlMethodId | STL_METHOD_ID | — | — |
| 37 | RetirementDistHistTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 38 | RetirementDistHistTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 39 | RetirementDistHistTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 40 | RetirementDistHistTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 41 | RetirementDistHistUnits | UNITS | — | — |
| 42 | RetirementDistHistUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |
| 43 | RetirementEofyReserve | EOFY_RESERVE | — | — |
| 44 | RetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | — |
| 45 | RetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | — |
| 46 | RetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | RetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | RetirementLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 49 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | — |
| 50 | RetirementNbvRetired | NBV_RETIRED | — | — |
| 51 | RetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | — |
| 53 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | — |
| 54 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | — |
| 55 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | — |
| 56 | RetirementReductionRate | REDUCTION_RATE | — | — |
| 57 | RetirementReferenceNum | REFERENCE_NUM | — | — |
| 58 | RetirementReserveRetired | RESERVE_RETIRED | — | — |
| 59 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | — |
| 60 | RetirementRetirementId | RETIREMENT_ID | — | — |
| 61 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | — |
| 62 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | — |
| 63 | RetirementSoldTo | SOLD_TO | — | — |
| 64 | RetirementStatus | STATUS | — | — |
| 65 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | — |
| 66 | RetirementStlMethodId | STL_METHOD_ID | — | — |
| 67 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | — |
| 68 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | — |
| 69 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |
| 70 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 71 | RetirementUnits | UNITS | — | — |
| 72 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | — |

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
| 61 | SrcTrxnHeaderTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
| 62 | SrcTrxnHeaderTransactionKey | TRANSACTION_KEY | — | — |
| 63 | SrcTrxnHeaderTransactionName | TRANSACTION_NAME | — | — |
| 64 | SrcTrxnHeaderTransactionSubtype | TRANSACTION_SUBTYPE | — | — |
| 65 | SrcTrxnHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 66 | SrcTrxnHeaderTrxReferenceId | TRX_REFERENCE_ID | — | — |
| 67 | TrxnHeaderAmortizationStartDate | AMORTIZATION_START_DATE | — | ✅ |
| 68 | TrxnHeaderAssetId | ASSET_ID | — | — |
| 69 | TrxnHeaderBookTypeCode | BOOK_TYPE_CODE | — | — |
| 70 | TrxnHeaderCallingInterface | CALLING_INTERFACE | — | — |
| 71 | TrxnHeaderCreatedBy | CREATED_BY | — | — |
| 72 | TrxnHeaderCreationDate | CREATION_DATE | — | — |
| 73 | TrxnHeaderDateEffective | DATE_EFFECTIVE | — | — |
| 74 | TrxnHeaderEventId | EVENT_ID | — | — |
| 75 | TrxnHeaderInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | — |
| 76 | TrxnHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 77 | TrxnHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 78 | TrxnHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 79 | TrxnHeaderMassReferenceId | MASS_REFERENCE_ID | — | — |
| 80 | TrxnHeaderMassTransactionId | MASS_TRANSACTION_ID | — | — |
| 81 | TrxnHeaderMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | — |
| 82 | TrxnHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 83 | TrxnHeaderSourceTransactionHeaderId | SOURCE_TRANSACTION_HEADER_ID | — | ✅ |
| 84 | TrxnHeaderTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 85 | TrxnHeaderTransactionHeaderId | TRANSACTION_HEADER_ID | — | — |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
