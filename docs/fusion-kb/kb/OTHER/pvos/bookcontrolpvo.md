---
id: DOC-OTHER-PVO-BookControlPVO
doc_type: system-doc
title: "BookControlPVO — PVO Cross-Module"
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
  - BookControlPVO
  - bookcontrolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BookControlPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Book Control. Acessa as tabelas: FA_BOOK_CONTROLS, FA_DEPRN_PERIODS, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.FinFaSharedSetupBookCtrlsAM.BookControlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 147 | 4 | 1 | 51 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[fa_book_controls|FA_BOOK_CONTROLS]] — 99 atributos (1 PKs, 46 BICC)
- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 28 atributos (3 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingFlexStructure | ACCOUNTING_FLEX_STRUCTURE | — | — |
| 2 | AllowBackdatedTransfersFlag | ALLOW_BACKDATED_TRANSFERS_FLAG | — | — |
| 3 | AllowCipAssetsFlag | ALLOW_CIP_ASSETS_FLAG | — | ✅ |
| 4 | AllowCipDepGroupFlag | ALLOW_CIP_DEP_GROUP_FLAG | — | — |
| 5 | AllowCipMemberFlag | ALLOW_CIP_MEMBER_FLAG | — | — |
| 6 | AllowCostCeiling | ALLOW_COST_CEILING | — | — |
| 7 | AllowCostSignChangeFlag | ALLOW_COST_SIGN_CHANGE_FLAG | — | ✅ |
| 8 | AllowDeprnAdjustments | ALLOW_DEPRN_ADJUSTMENTS | — | — |
| 9 | AllowDeprnExpCeiling | ALLOW_DEPRN_EXP_CEILING | — | — |
| 10 | AllowDeprnOverrideFlag | ALLOW_DEPRN_OVERRIDE_FLAG | — | — |
| 11 | AllowGroupDeprnFlag | ALLOW_GROUP_DEPRN_FLAG | — | — |
| 12 | AllowImpairmentFlag | ALLOW_IMPAIRMENT_FLAG | — | ✅ |
| 13 | AllowIntercoGroupFlag | ALLOW_INTERCO_GROUP_FLAG | — | — |
| 14 | AllowMassChanges | ALLOW_MASS_CHANGES | — | ✅ |
| 15 | AllowMassCopy | ALLOW_MASS_COPY | — | — |
| 16 | AllowMemberTrackingFlag | ALLOW_MEMBER_TRACKING_FLAG | — | — |
| 17 | AllowPurgeFlag | ALLOW_PURGE_FLAG | — | — |
| 18 | AllowRevalFlag | ALLOW_REVAL_FLAG | — | ✅ |
| 19 | AmortizeFlag | AMORTIZE_FLAG | — | ✅ |
| 20 | AmortizeRevalReserveFlag | AMORTIZE_REVAL_RESERVE_FLAG | — | — |
| 21 | AsscCorpBookBookTypeCode | BOOK_TYPE_CODE | — | — |
| 22 | AsscCorpBookBookTypeName | BOOK_TYPE_NAME | — | ✅ |
| 23 | BookClass | BOOK_CLASS | — | ✅ |
| 24 | BookControlId | BOOK_CONTROL_ID | — | ✅ |
| 25 | BookCtrlCreatedBy | CREATED_BY | — | — |
| 26 | BookCtrlCreationDate | CREATION_DATE | — | ✅ |
| 27 | BookCtrlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | BookCtrlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | BookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 30 | BookTypeName | BOOK_TYPE_NAME | — | ✅ |
| 31 | BookTypeName2 | BOOK_TYPE_NAME | — | — |
| 32 | CapThresholdAmount | CAP_THRESHOLD_AMOUNT | — | ✅ |
| 33 | CapThresholdType | CAP_THRESHOLD_TYPE | — | ✅ |
| 34 | CapitalGainThreshold | CAPITAL_GAIN_THRESHOLD | — | — |
| 35 | CopyAdditionsFlag | COPY_ADDITIONS_FLAG | — | — |
| 36 | CopyAdjustmentsFlag | COPY_ADJUSTMENTS_FLAG | — | — |
| 37 | CopyGroupAdditionFlag | COPY_GROUP_ADDITION_FLAG | — | — |
| 38 | CopyGroupAssignmentFlag | COPY_GROUP_ASSIGNMENT_FLAG | — | — |
| 39 | CopyRetirementsFlag | COPY_RETIREMENTS_FLAG | — | — |
| 40 | CopySalvageValueFlag | COPY_SALVAGE_VALUE_FLAG | — | — |
| 41 | CostOfRemovalClearingAcct | COST_OF_REMOVAL_CLEARING_ACCT | — | ✅ |
| 42 | CostOfRemovalGainAcct | COST_OF_REMOVAL_GAIN_ACCT | — | ✅ |
| 43 | CostOfRemovalLossAcct | COST_OF_REMOVAL_LOSS_ACCT | — | ✅ |
| 44 | CreateAccountingRequestId | CREATE_ACCOUNTING_REQUEST_ID | — | — |
| 45 | CreatedBy | CREATED_BY | — | ✅ |
| 46 | CreationDate | CREATION_DATE | — | ✅ |
| 47 | CurrentFiscalYear | CURRENT_FISCAL_YEAR | — | ✅ |
| 48 | DateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 49 | DefaultLifeExtensionCeiling | DEFAULT_LIFE_EXTENSION_CEILING | — | — |
| 50 | DefaultLifeExtensionFactor | DEFAULT_LIFE_EXTENSION_FACTOR | — | — |
| 51 | DefaultMaxFullyRsvdRevals | DEFAULT_MAX_FULLY_RSVD_REVALS | — | — |
| 52 | DefaultRevalFullyRsvdFlag | DEFAULT_REVAL_FULLY_RSVD_FLAG | — | — |
| 53 | DeferredDeprnExpenseAcct | DEFERRED_DEPRN_EXPENSE_ACCT | — | ✅ |
| 54 | DeferredDeprnReserveAcct | DEFERRED_DEPRN_RESERVE_ACCT | — | ✅ |
| 55 | DeprFirstYearRetFlag | DEPR_FIRST_YEAR_RET_FLAG | — | — |
| 56 | DeprFirstYearRetFlag1 | DEPR_FIRST_YEAR_RET_FLAG | — | — |
| 57 | DeprnAdjustmentAcct | DEPRN_ADJUSTMENT_ACCT | — | ✅ |
| 58 | DeprnAllocationCode | DEPRN_ALLOCATION_CODE | — | ✅ |
| 59 | DeprnCalendar | DEPRN_CALENDAR | — | ✅ |
| 60 | DeprnRequestId | DEPRN_REQUEST_ID | — | — |
| 61 | DeprnStatus | DEPRN_STATUS | — | ✅ |
| 62 | DistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | ✅ |
| 63 | FiscalYearName | FISCAL_YEAR_NAME | — | ✅ |
| 64 | FlexbuilderDefaultsCcid | FLEXBUILDER_DEFAULTS_CCID | — | — |
| 65 | FullyReservedFlag | FULLY_RESERVED_FLAG | — | — |
| 66 | GlPostingAllowedFlag | GL_POSTING_ALLOWED_FLAG | — | ✅ |
| 67 | ImmediateCopyFlag | IMMEDIATE_COPY_FLAG | — | — |
| 68 | InitialDate | INITIAL_DATE | — | — |
| 69 | InitialPeriodCounter | INITIAL_PERIOD_COUNTER | — | — |
| 70 | LastDeprnRunDate | LAST_DEPRN_RUN_DATE | — | ✅ |
| 71 | LastMassCopyPeriodCounter | LAST_MASS_COPY_PERIOD_COUNTER | — | — |
| 72 | LastPeriodCounter | LAST_PERIOD_COUNTER | — | ✅ |
| 73 | LastPurgePeriodCounter | LAST_PURGE_PERIOD_COUNTER | — | — |
| 74 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 77 | LowValueThresholdAmount | LOW_VALUE_THRESHOLD_AMOUNT | — | ✅ |
| 78 | MassCopySourceBook | MASS_COPY_SOURCE_BOOK | — | — |
| 79 | MassRequestId | MASS_REQUEST_ID | — | — |
| 80 | McSourceFlag | MC_SOURCE_FLAG | — | — |
| 81 | NbvAmountThreshold | NBV_AMOUNT_THRESHOLD | — | ✅ |
| 82 | NbvFractionThreshold | NBV_FRACTION_THRESHOLD | — | ✅ |
| 83 | NbvRetiredGainAcct | NBV_RETIRED_GAIN_ACCT | — | ✅ |
| 84 | NbvRetiredLossAcct | NBV_RETIRED_LOSS_ACCT | — | ✅ |
| 85 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 86 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 87 | ProceedsOfSaleClearingAcct | PROCEEDS_OF_SALE_CLEARING_ACCT | — | ✅ |
| 88 | ProceedsOfSaleGainAcct | PROCEEDS_OF_SALE_GAIN_ACCT | — | ✅ |
| 89 | ProceedsOfSaleLossAcct | PROCEEDS_OF_SALE_LOSS_ACCT | — | ✅ |
| 90 | ProrateCalendar | PRORATE_CALENDAR | — | — |
| 91 | RetireRevalReserveFlag | RETIRE_REVAL_RESERVE_FLAG | — | — |
| 92 | RevalDeprnReserveFlag | REVAL_DEPRN_RESERVE_FLAG | — | — |
| 93 | RevalRsvRetiredGainAcct | REVAL_RSV_RETIRED_GAIN_ACCT | — | ✅ |
| 94 | RevalRsvRetiredLossAcct | REVAL_RSV_RETIRED_LOSS_ACCT | — | ✅ |
| 95 | RevalYtdDeprnFlag | REVAL_YTD_DEPRN_FLAG | — | — |
| 96 | RoundAnnualDepreciation | ROUND_ANNUAL_DEPRECIATION | — | — |
| 97 | SetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 98 | UseNbvThresholdFlag | USE_NBV_THRESHOLD_FLAG | — | — |
| 99 | UsePercentSalvageValueFlag | USE_PERCENT_SALVAGE_VALUE_FLAG | — | — |

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookTypeCode1 | BOOK_TYPE_CODE | — | — |
| 2 | CurrDeprnPeriodCounter | PERIOD_COUNTER | — | ✅ |
| 3 | CurrDeprnPeriodName | PERIOD_NAME | — | ✅ |
| 4 | InitDeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 5 | InitDeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 6 | InitDeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 7 | InitDeprnPeriodPeriodName | PERIOD_NAME | — | — |
| 8 | InitDeprnPeriodPeriodNum | PERIOD_NUM | — | — |
| 9 | LastDeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 10 | LastDeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 11 | LastDeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 12 | LastDeprnPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 13 | LastDeprnPeriodPeriodNum | PERIOD_NUM | — | — |
| 14 | LastPurgeDeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 15 | LastPurgeDeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 16 | LastPurgeDeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 17 | LastPurgeDeprnPeriodPeriodName | PERIOD_NAME | — | — |
| 18 | LastPurgeDeprnPeriodPeriodNum | PERIOD_NUM | — | — |
| 19 | MassCopyDeprnPeriodBookTypeCode | BOOK_TYPE_CODE | — | — |
| 20 | MassCopyDeprnPeriodFiscalYear | FISCAL_YEAR | — | — |
| 21 | MassCopyDeprnPeriodPeriodCounter | PERIOD_COUNTER | — | — |
| 22 | MassCopyDeprnPeriodPeriodName | PERIOD_NAME | — | — |
| 23 | MassCopyDeprnPeriodPeriodNum | PERIOD_NUM | — | — |
| 24 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 25 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 26 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 27 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 28 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |

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
