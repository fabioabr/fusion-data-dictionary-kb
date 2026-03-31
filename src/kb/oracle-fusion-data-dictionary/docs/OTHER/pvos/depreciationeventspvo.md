---
id: DOC-OTHER-PVO-DepreciationEventsPVO
doc_type: system-doc
title: "DepreciationEventsPVO — PVO Cross-Module"
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
  - DepreciationEventsPVO
  - depreciationeventspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationEventsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Events. Acessa as tabelas: FA_ADDITIONS_B, FA_BOOK_CONTROLS, FA_DEPRN_EVENTS (+3).

**Caminho:** `FscmTopModelAM.FinFaDeprDepreciationAM.DepreciationEventsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 212 | 6 | 4 | 25 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 28 atributos (2 BICC)
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 81 atributos (3 BICC)
- [[fa_deprn_events|FA_DEPRN_EVENTS]] — 14 atributos (4 PKs, 9 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 5 atributos (1 BICC)
- [[xla_events|XLA_EVENTS]] — 70 atributos (8 BICC)
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 14 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 2 | AdditionAssetId | ASSET_ID | — | — |
| 3 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | — |
| 4 | AdditionAssetNumber | ASSET_NUMBER | — | ✅ |
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

### [[fa_deprn_events|FA_DEPRN_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | 🔑 | ✅ |
| 2 | BookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 3 | DeprnEventCreatedBy | CREATED_BY | — | — |
| 4 | DeprnEventCreationDate | CREATION_DATE | — | — |
| 5 | DeprnEventDeprnRunDate | DEPRN_RUN_DATE | — | ✅ |
| 6 | DeprnEventEventId | EVENT_ID | — | ✅ |
| 7 | DeprnEventLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | DeprnEventLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | DeprnEventLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | DeprnEventObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | DeprnEventReversalDate | REVERSAL_DATE | — | ✅ |
| 12 | DeprnEventReversalEventId | REVERSAL_EVENT_ID | — | ✅ |
| 13 | DeprnRunId | DEPRN_RUN_ID | 🔑 | ✅ |
| 14 | PeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 2 | DeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 3 | DeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 4 | DeprnPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 5 | DeprnPeriodPeriodNum | PERIOD_NUM | — | — |

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventApplicationId | APPLICATION_ID | — | — |
| 2 | EventBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | — |
| 3 | EventCreatedBy | CREATED_BY | — | — |
| 4 | EventCreationDate | CREATION_DATE | — | — |
| 5 | EventEntityId | ENTITY_ID | — | — |
| 6 | EventEventDate | EVENT_DATE | — | ✅ |
| 7 | EventEventId | EVENT_ID | — | — |
| 8 | EventEventNumber | EVENT_NUMBER | — | — |
| 9 | EventEventStatusCode | EVENT_STATUS_CODE | — | — |
| 10 | EventEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 11 | EventHasWarningsFlag | HAS_WARNINGS_FLAG | — | — |
| 12 | EventLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | EventLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | EventLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | EventMergeEventSetId | MERGE_EVENT_SET_ID | — | — |
| 16 | EventObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | EventOnHoldFlag | ON_HOLD_FLAG | — | — |
| 18 | EventProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 19 | EventReferenceChar1 | REFERENCE_CHAR_1 | — | — |
| 20 | EventReferenceChar2 | REFERENCE_CHAR_2 | — | — |
| 21 | EventReferenceChar3 | REFERENCE_CHAR_3 | — | — |
| 22 | EventReferenceChar4 | REFERENCE_CHAR_4 | — | — |
| 23 | EventReferenceDate1 | REFERENCE_DATE_1 | — | — |
| 24 | EventReferenceDate2 | REFERENCE_DATE_2 | — | — |
| 25 | EventReferenceDate3 | REFERENCE_DATE_3 | — | — |
| 26 | EventReferenceDate4 | REFERENCE_DATE_4 | — | — |
| 27 | EventReferenceNum1 | REFERENCE_NUM_1 | — | — |
| 28 | EventReferenceNum2 | REFERENCE_NUM_2 | — | — |
| 29 | EventReferenceNum3 | REFERENCE_NUM_3 | — | — |
| 30 | EventReferenceNum4 | REFERENCE_NUM_4 | — | — |
| 31 | EventRequestId | REQUEST_ID | — | — |
| 32 | EventTransactionDate | TRANSACTION_DATE | — | ✅ |
| 33 | EventUpgBatchId | UPG_BATCH_ID | — | — |
| 34 | EventUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 35 | EventUpgValidFlag | UPG_VALID_FLAG | — | — |
| 36 | RevEventApplicationId | APPLICATION_ID | — | — |
| 37 | RevEventBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | — |
| 38 | RevEventCreatedBy | CREATED_BY | — | — |
| 39 | RevEventCreationDate | CREATION_DATE | — | — |
| 40 | RevEventEntityId | ENTITY_ID | — | — |
| 41 | RevEventEventDate | EVENT_DATE | — | ✅ |
| 42 | RevEventEventId | EVENT_ID | — | — |
| 43 | RevEventEventNumber | EVENT_NUMBER | — | — |
| 44 | RevEventEventStatusCode | EVENT_STATUS_CODE | — | — |
| 45 | RevEventEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 46 | RevEventHasWarningsFlag | HAS_WARNINGS_FLAG | — | — |
| 47 | RevEventLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | RevEventLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | RevEventLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | RevEventMergeEventSetId | MERGE_EVENT_SET_ID | — | — |
| 51 | RevEventObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | RevEventOnHoldFlag | ON_HOLD_FLAG | — | — |
| 53 | RevEventProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 54 | RevEventReferenceChar1 | REFERENCE_CHAR_1 | — | — |
| 55 | RevEventReferenceChar2 | REFERENCE_CHAR_2 | — | — |
| 56 | RevEventReferenceChar3 | REFERENCE_CHAR_3 | — | — |
| 57 | RevEventReferenceChar4 | REFERENCE_CHAR_4 | — | — |
| 58 | RevEventReferenceDate1 | REFERENCE_DATE_1 | — | — |
| 59 | RevEventReferenceDate2 | REFERENCE_DATE_2 | — | — |
| 60 | RevEventReferenceDate3 | REFERENCE_DATE_3 | — | — |
| 61 | RevEventReferenceDate4 | REFERENCE_DATE_4 | — | — |
| 62 | RevEventReferenceNum1 | REFERENCE_NUM_1 | — | — |
| 63 | RevEventReferenceNum2 | REFERENCE_NUM_2 | — | — |
| 64 | RevEventReferenceNum3 | REFERENCE_NUM_3 | — | — |
| 65 | RevEventReferenceNum4 | REFERENCE_NUM_4 | — | — |
| 66 | RevEventRequestId | REQUEST_ID | — | — |
| 67 | RevEventTransactionDate | TRANSACTION_DATE | — | ✅ |
| 68 | RevEventUpgBatchId | UPG_BATCH_ID | — | — |
| 69 | RevEventUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 70 | RevEventUpgValidFlag | UPG_VALID_FLAG | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeDescription | DESCRIPTION | — | — |
| 3 | EventTypeEntityCode | ENTITY_CODE | — | — |
| 4 | EventTypeEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventTypeEventTypeCode | EVENT_TYPE_CODE | — | — |
| 6 | EventTypeLanguage | LANGUAGE | — | — |
| 7 | EventTypeName | NAME | — | ✅ |
| 8 | RevEventTypeApplicationId | APPLICATION_ID | — | — |
| 9 | RevEventTypeDescription | DESCRIPTION | — | — |
| 10 | RevEventTypeEntityCode | ENTITY_CODE | — | — |
| 11 | RevEventTypeEventClassCode | EVENT_CLASS_CODE | — | — |
| 12 | RevEventTypeEventTypeCode | EVENT_TYPE_CODE | — | — |
| 13 | RevEventTypeLanguage | LANGUAGE | — | — |
| 14 | RevEventTypeName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
