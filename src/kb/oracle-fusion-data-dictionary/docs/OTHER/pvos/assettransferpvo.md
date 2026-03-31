---
id: DOC-OTHER-PVO-AssetTransferPVO
doc_type: system-doc
title: "AssetTransferPVO — PVO Cross-Module"
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
  - AssetTransferPVO
  - assettransferpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetTransferPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Transfer. Acessa as tabelas: FA_ADDITIONS_B, FA_ASSET_TRANSFER_V, FA_BOOK_CONTROLS.

**Caminho:** `FscmTopModelAM.FinFaTrackTransfersAM.AssetTransferPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 3 | 1 | 6 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 28 atributos (1 BICC)
- [[fa_asset_transfer_v|FA_ASSET_TRANSFER_V]] — 16 atributos (1 PKs, 4 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (1 BICC)

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

### [[fa_asset_transfer_v|FA_ASSET_TRANSFER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AstTransferAssetId | ASSET_ID | — | — |
| 2 | AstTransferBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | AstTransferDateEffective | DATE_EFFECTIVE | — | — |
| 4 | AstTransferFromAssignedTo | FROM_ASSIGNED_TO | — | — |
| 5 | AstTransferFromCodeCombinationId | FROM_CODE_COMBINATION_ID | — | — |
| 6 | AstTransferFromDistributionId | FROM_DISTRIBUTION_ID | — | — |
| 7 | AstTransferFromLocationId | FROM_LOCATION_ID | — | — |
| 8 | AstTransferToAssignedTo | TO_ASSIGNED_TO | — | — |
| 9 | AstTransferToCodeCombinationId | TO_CODE_COMBINATION_ID | — | — |
| 10 | AstTransferToLocationId | TO_LOCATION_ID | — | — |
| 11 | AstTransferTransactionDateEntered | TRANSACTION_DATE_ENTERED | — | — |
| 12 | AstTransferTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |
| 13 | AstTransferTransactionSubtype | TRANSACTION_SUBTYPE | — | ✅ |
| 14 | AstTransferTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 15 | AstTransferTransferredUnits | TRANSFERRED_UNITS | — | ✅ |
| 16 | ToDistributionId | TO_DISTRIBUTION_ID | 🔑 | ✅ |

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
