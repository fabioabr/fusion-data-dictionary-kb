---
id: DOC-OTHER-PVO-JournalEntryLinePVO
doc_type: system-doc
title: "JournalEntryLinePVO — PVO Cross-Module"
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
  - JournalEntryLinePVO
  - journalentrylinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalEntryLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Entry Line. Acessa as tabelas: FND_DOCUMENT_SEQUENCES, FND_DOC_SEQUENCE_CATEGORIES, FUN_SEQ_ASSIGNMENTS (+15).

**Caminho:** `FscmTopModelAM.FinXlaJrnlEnterJrnlAM.JournalEntryLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 531 | 18 | 2 | 131 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]] — 11 atributos (2 BICC)
- [[fun_seq_assignments|FUN_SEQ_ASSIGNMENTS]] — 30 atributos
- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 32 atributos (6 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 25 atributos (1 BICC)
- [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]] — 2 atributos (1 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 32 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (4 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[xla_ae_headers|XLA_AE_HEADERS]] — 55 atributos (19 BICC)
- [[xla_ae_lines|XLA_AE_LINES]] — 120 atributos (2 PKs, 87 BICC)
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 7 atributos (1 BICC)
- [[xla_gl_ledgers|XLA_GL_LEDGERS]] — 84 atributos (1 BICC)
- [[xla_subledgers|XLA_SUBLEDGERS]] — 36 atributos (2 BICC)
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 21 atributos
- [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]] — 32 atributos (3 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 17 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqName | NAME | — | ✅ |
| 5 | DocSeqTableName | TABLE_NAME | — | — |

### [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqCategApplicationId | APPLICATION_ID | — | — |
| 2 | DocSeqCategCode | CODE | — | — |
| 3 | DocSeqCategCreatedBy | CREATED_BY | — | — |
| 4 | DocSeqCategCreationDate | CREATION_DATE | — | — |
| 5 | DocSeqCategDescription | DESCRIPTION | — | — |
| 6 | DocSeqCategLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DocSeqCategLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DocSeqCategLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DocSeqCategModuleId | MODULE_ID | — | — |
| 10 | DocSeqCategName | NAME | — | ✅ |
| 11 | DocSeqCategTableName | TABLE_NAME | — | — |

### [[fun_seq_assignments|FUN_SEQ_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClActSeqAsgnAccountingEntryType | ACCOUNTING_ENTRY_TYPE | — | — |
| 2 | ClActSeqAsgnAccountingEventType | ACCOUNTING_EVENT_TYPE | — | — |
| 3 | ClActSeqAsgnAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | ClActSeqAsgnBalanceType | BALANCE_TYPE | — | — |
| 5 | ClActSeqAsgnControlAttributeStructure | CONTROL_ATTRIBUTE_STRUCTURE | — | — |
| 6 | ClActSeqAsgnDocumentCategory | DOCUMENT_CATEGORY | — | — |
| 7 | ClActSeqAsgnEndDate | END_DATE | — | — |
| 8 | ClActSeqAsgnJournalCategory | JOURNAL_CATEGORY | — | — |
| 9 | ClActSeqAsgnJournalSource | JOURNAL_SOURCE | — | — |
| 10 | ClActSeqAsgnLinkToAssignmentId | LINK_TO_ASSIGNMENT_ID | — | — |
| 11 | ClActSeqAsgnPriority | PRIORITY | — | — |
| 12 | ClActSeqAsgnSeqContextId | SEQ_CONTEXT_ID | — | — |
| 13 | ClActSeqAsgnSeqHeaderId | SEQ_HEADER_ID | — | — |
| 14 | ClActSeqAsgnStartDate | START_DATE | — | — |
| 15 | ClActSeqAsgnUseStatusCode | USE_STATUS_CODE | — | — |
| 16 | CmActSeqAsgnAccountingEntryType | ACCOUNTING_ENTRY_TYPE | — | — |
| 17 | CmActSeqAsgnAccountingEventType | ACCOUNTING_EVENT_TYPE | — | — |
| 18 | CmActSeqAsgnAssignmentId | ASSIGNMENT_ID | — | — |
| 19 | CmActSeqAsgnBalanceType | BALANCE_TYPE | — | — |
| 20 | CmActSeqAsgnControlAttributeStructure | CONTROL_ATTRIBUTE_STRUCTURE | — | — |
| 21 | CmActSeqAsgnDocumentCategory | DOCUMENT_CATEGORY | — | — |
| 22 | CmActSeqAsgnEndDate | END_DATE | — | — |
| 23 | CmActSeqAsgnJournalCategory | JOURNAL_CATEGORY | — | — |
| 24 | CmActSeqAsgnJournalSource | JOURNAL_SOURCE | — | — |
| 25 | CmActSeqAsgnLinkToAssignmentId | LINK_TO_ASSIGNMENT_ID | — | — |
| 26 | CmActSeqAsgnPriority | PRIORITY | — | — |
| 27 | CmActSeqAsgnSeqContextId | SEQ_CONTEXT_ID | — | — |
| 28 | CmActSeqAsgnSeqHeaderId | SEQ_HEADER_ID | — | — |
| 29 | CmActSeqAsgnStartDate | START_DATE | — | — |
| 30 | CmActSeqAsgnUseStatusCode | USE_STATUS_CODE | — | — |

### [[fun_seq_versions|FUN_SEQ_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClActSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 2 | ClActSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | ClActSeqVerEndDate | END_DATE | — | — |
| 4 | ClActSeqVerHeaderName | HEADER_NAME | — | ✅ |
| 5 | ClActSeqVerInitialValue | INITIAL_VALUE | — | — |
| 6 | ClActSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 7 | ClActSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 8 | ClActSeqVerStartDate | START_DATE | — | — |
| 9 | ClActSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 10 | ClActSeqVerVersionName | VERSION_NAME | — | ✅ |
| 11 | CmActSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 12 | CmActSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 13 | CmActSeqVerEndDate | END_DATE | — | — |
| 14 | CmActSeqVerHeaderName | HEADER_NAME | — | ✅ |
| 15 | CmActSeqVerInitialValue | INITIAL_VALUE | — | — |
| 16 | CmActSeqVerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | CmActSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 18 | CmActSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 19 | CmActSeqVerStartDate | START_DATE | — | — |
| 20 | CmActSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 21 | CmActSeqVerVersionName | VERSION_NAME | — | ✅ |
| 22 | DocSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 23 | DocSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 24 | DocSeqVerEndDate | END_DATE | — | — |
| 25 | DocSeqVerHeaderName | HEADER_NAME | — | ✅ |
| 26 | DocSeqVerInitialValue | INITIAL_VALUE | — | — |
| 27 | DocSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 28 | DocSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 29 | DocSeqVerStartDate | START_DATE | — | — |
| 30 | DocSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 31 | DocSeqVerVersionName | VERSION_NAME | — | ✅ |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionTypeXlalineConversionType | CONVERSION_TYPE | — | — |
| 2 | ConversionTypeXlalineDescription | DESCRIPTION | — | ✅ |
| 3 | ConversionTypeXlalineEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 4 | ConversionTypeXlalineEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 5 | ConversionTypeXlalineFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 6 | ConversionTypeXlalineFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 7 | ConversionTypeXlalineFemScenario | FEM_SCENARIO | — | — |
| 8 | ConversionTypeXlalineFemTimeframe | FEM_TIMEFRAME | — | — |
| 9 | ConversionTypeXlalineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ConversionTypeXlalinePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 11 | ConversionTypeXlalineSecurityFlag | SECURITY_FLAG | — | — |
| 12 | ConversionTypeXlalineUserConversionType | USER_CONVERSION_TYPE | — | — |
| 13 | ConversionTypeXlalineUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 14 | DailyConvConversionType | CONVERSION_TYPE | — | — |
| 15 | DailyConvDescription | DESCRIPTION | — | — |
| 16 | DailyConvEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 17 | DailyConvEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 18 | DailyConvFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 19 | DailyConvFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 20 | DailyConvFemScenario | FEM_SCENARIO | — | — |
| 21 | DailyConvFemTimeframe | FEM_TIMEFRAME | — | — |
| 22 | DailyConvPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 23 | DailyConvSecurityFlag | SECURITY_FLAG | — | — |
| 24 | DailyConvUserConversionType | USER_CONVERSION_TYPE | — | — |
| 25 | DailyConvUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEncumbranceTypeEncumbranceType | ENCUMBRANCE_TYPE | — | ✅ |
| 2 | JournalEncumbranceTypeEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctAccountName | ACCOUNT_NAME | — | — |
| 3 | CustAcctAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | CustAcctAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | — |
| 5 | CustAcctArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 6 | CustAcctAutopayFlag | AUTOPAY_FLAG | — | — |
| 7 | CustAcctComments | COMMENTS | — | — |
| 8 | CustAcctCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 9 | CustAcctCreatedBy | CREATED_BY | — | — |
| 10 | CustAcctCreatedByModule | CREATED_BY_MODULE | — | — |
| 11 | CustAcctCreationDate | CREATION_DATE | — | — |
| 12 | CustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 13 | CustAcctCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 14 | CustAcctCustomerType | CUSTOMER_TYPE | — | — |
| 15 | CustAcctDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 16 | CustAcctDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 17 | CustAcctHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 18 | CustAcctHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 19 | CustAcctLastBatchId | LAST_BATCH_ID | — | — |
| 20 | CustAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CustAcctLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | CustAcctLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CustAcctNpaNumber | NPA_NUMBER | — | — |
| 24 | CustAcctOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 25 | CustAcctPartyId | PARTY_ID | — | — |
| 26 | CustAcctSellingPartyId | SELLING_PARTY_ID | — | — |
| 27 | CustAcctSourceCode | SOURCE_CODE | — | — |
| 28 | CustAcctStatus | STATUS | — | — |
| 29 | CustAcctStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 30 | CustAcctTaxCode | TAX_CODE | — | — |
| 31 | CustAcctTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 32 | CustAcctTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
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
| 6 | UserUpdatedByObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[xla_ae_headers|XLA_AE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlahdrAccountingBatchId | ACCOUNTING_BATCH_ID | — | — |
| 2 | XlahdrAccountingDate | ACCOUNTING_DATE | — | — |
| 3 | XlahdrAccountingEntryStatusCode | ACCOUNTING_ENTRY_STATUS_CODE | — | — |
| 4 | XlahdrAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | ✅ |
| 5 | XlahdrAccrualReversalFlag | ACCRUAL_REVERSAL_FLAG | — | — |
| 6 | XlahdrAeHeaderId | AE_HEADER_ID | — | — |
| 7 | XlahdrAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 8 | XlahdrApplicationId | APPLICATION_ID | — | — |
| 9 | XlahdrBalanceTypeCode | BALANCE_TYPE_CODE | — | ✅ |
| 10 | XlahdrBudgetVersionId | BUDGET_VERSION_ID | — | — |
| 11 | XlahdrCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | — |
| 12 | XlahdrCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | ✅ |
| 13 | XlahdrCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | — |
| 14 | XlahdrCompletedDate | COMPLETED_DATE | — | ✅ |
| 15 | XlahdrCompletionAcctSeqAssignId | COMPLETION_ACCT_SEQ_ASSIGN_ID | — | — |
| 16 | XlahdrCompletionAcctSeqValue | COMPLETION_ACCT_SEQ_VALUE | — | ✅ |
| 17 | XlahdrCompletionAcctSeqVersionId | COMPLETION_ACCT_SEQ_VERSION_ID | — | — |
| 18 | XlahdrCreatedBy | CREATED_BY | — | ✅ |
| 19 | XlahdrCreationDate | CREATION_DATE | — | ✅ |
| 20 | XlahdrDescription | DESCRIPTION | — | ✅ |
| 21 | XlahdrDocCategoryCode | DOC_CATEGORY_CODE | — | ✅ |
| 22 | XlahdrDocSequenceAssignId | DOC_SEQUENCE_ASSIGN_ID | — | — |
| 23 | XlahdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 24 | XlahdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 25 | XlahdrDocSequenceVersionId | DOC_SEQUENCE_VERSION_ID | — | — |
| 26 | XlahdrEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 27 | XlahdrEntityId | ENTITY_ID | — | — |
| 28 | XlahdrEventId | EVENT_ID | — | — |
| 29 | XlahdrEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 30 | XlahdrFundsStatusCode | FUNDS_STATUS_CODE | — | ✅ |
| 31 | XlahdrGlTransferDate | GL_TRANSFER_DATE | — | ✅ |
| 32 | XlahdrGlTransferStatusCode | GL_TRANSFER_STATUS_CODE | — | — |
| 33 | XlahdrGroupId | GROUP_ID | — | — |
| 34 | XlahdrJeCategoryName | JE_CATEGORY_NAME | — | ✅ |
| 35 | XlahdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | XlahdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | XlahdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | XlahdrLedgerId | LEDGER_ID | — | — |
| 39 | XlahdrMergeEventId | MERGE_EVENT_ID | — | — |
| 40 | XlahdrMultiPeriodFlag | MULTIPERIOD_FLAG | — | ✅ |
| 41 | XlahdrNeedBalFlag | NEED_BAL_CODE | — | — |
| 42 | XlahdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | XlahdrPacketId | PACKET_ID | — | — |
| 44 | XlahdrParentAeHeaderId | PARENT_AE_HEADER_ID | — | — |
| 45 | XlahdrParentAeLineNum | PARENT_AE_LINE_NUM | — | — |
| 46 | XlahdrPeriodName | PERIOD_NAME | — | ✅ |
| 47 | XlahdrProductRuleCode | PRODUCT_RULE_CODE | — | — |
| 48 | XlahdrProductRuleTypeCode | PRODUCT_RULE_TYPE_CODE | — | — |
| 49 | XlahdrProductRuleVersion | PRODUCT_RULE_VERSION | — | — |
| 50 | XlahdrReferenceDate | REFERENCE_DATE | — | ✅ |
| 51 | XlahdrRequestId | REQUEST_ID | — | — |
| 52 | XlahdrUpgBatchId | UPG_BATCH_ID | — | — |
| 53 | XlahdrUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 54 | XlahdrUpgValidFlag | UPG_VALID_FLAG | — | — |
| 55 | XlahdrZeroAmountFlag | ZERO_AMOUNT_FLAG | — | — |

### [[xla_ae_lines|XLA_AE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 2 | AeLineNum | AE_LINE_NUM | 🔑 | ✅ |
| 3 | Sr1 | SR1 | — | ✅ |
| 4 | Sr10 | SR10 | — | ✅ |
| 5 | Sr11 | SR11 | — | ✅ |
| 6 | Sr12 | SR12 | — | ✅ |
| 7 | Sr13 | SR13 | — | ✅ |
| 8 | Sr14 | SR14 | — | ✅ |
| 9 | Sr15 | SR15 | — | ✅ |
| 10 | Sr16 | SR16 | — | ✅ |
| 11 | Sr17 | SR17 | — | ✅ |
| 12 | Sr18 | SR18 | — | ✅ |
| 13 | Sr19 | SR19 | — | ✅ |
| 14 | Sr2 | SR2 | — | ✅ |
| 15 | Sr20 | SR20 | — | ✅ |
| 16 | Sr21 | SR21 | — | ✅ |
| 17 | Sr22 | SR22 | — | ✅ |
| 18 | Sr23 | SR23 | — | ✅ |
| 19 | Sr24 | SR24 | — | ✅ |
| 20 | Sr25 | SR25 | — | ✅ |
| 21 | Sr26 | SR26 | — | ✅ |
| 22 | Sr27 | SR27 | — | ✅ |
| 23 | Sr28 | SR28 | — | ✅ |
| 24 | Sr29 | SR29 | — | ✅ |
| 25 | Sr3 | SR3 | — | ✅ |
| 26 | Sr30 | SR30 | — | ✅ |
| 27 | Sr31 | SR31 | — | ✅ |
| 28 | Sr32 | SR32 | — | ✅ |
| 29 | Sr33 | SR33 | — | ✅ |
| 30 | Sr34 | SR34 | — | ✅ |
| 31 | Sr35 | SR35 | — | ✅ |
| 32 | Sr36 | SR36 | — | ✅ |
| 33 | Sr37 | SR37 | — | ✅ |
| 34 | Sr38 | SR38 | — | ✅ |
| 35 | Sr39 | SR39 | — | ✅ |
| 36 | Sr4 | SR4 | — | ✅ |
| 37 | Sr40 | SR40 | — | ✅ |
| 38 | Sr41 | SR41 | — | ✅ |
| 39 | Sr42 | SR42 | — | ✅ |
| 40 | Sr43 | SR43 | — | ✅ |
| 41 | Sr44 | SR44 | — | ✅ |
| 42 | Sr45 | SR45 | — | ✅ |
| 43 | Sr46 | SR46 | — | ✅ |
| 44 | Sr47 | SR47 | — | ✅ |
| 45 | Sr48 | SR48 | — | ✅ |
| 46 | Sr49 | SR49 | — | ✅ |
| 47 | Sr5 | SR5 | — | ✅ |
| 48 | Sr50 | SR50 | — | ✅ |
| 49 | Sr51 | SR51 | — | ✅ |
| 50 | Sr52 | SR52 | — | ✅ |
| 51 | Sr53 | SR53 | — | ✅ |
| 52 | Sr54 | SR54 | — | ✅ |
| 53 | Sr55 | SR55 | — | ✅ |
| 54 | Sr56 | SR56 | — | ✅ |
| 55 | Sr57 | SR57 | — | ✅ |
| 56 | Sr58 | SR58 | — | ✅ |
| 57 | Sr59 | SR59 | — | ✅ |
| 58 | Sr6 | SR6 | — | ✅ |
| 59 | Sr60 | SR60 | — | ✅ |
| 60 | Sr7 | SR7 | — | ✅ |
| 61 | Sr8 | SR8 | — | ✅ |
| 62 | Sr9 | SR9 | — | ✅ |
| 63 | XlalinesAccountOverlaySourceId | ACCOUNT_OVERLAY_SOURCE_ID | — | — |
| 64 | XlalinesAccountedCr | ACCOUNTED_CR | — | ✅ |
| 65 | XlalinesAccountedDr | ACCOUNTED_DR | — | ✅ |
| 66 | XlalinesAccountingClassCode | ACCOUNTING_CLASS_CODE | — | — |
| 67 | XlalinesAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 68 | XlalinesAnalyticalBalanceFlag | ANALYTICAL_BALANCE_FLAG | — | — |
| 69 | XlalinesApplicationId | APPLICATION_ID | — | ✅ |
| 70 | XlalinesBusinessClassCode | BUSINESS_CLASS_CODE | — | ✅ |
| 71 | XlalinesCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 72 | XlalinesControlBalanceFlag | CONTROL_BALANCE_FLAG | — | — |
| 73 | XlalinesCreatedBy | CREATED_BY | — | — |
| 74 | XlalinesCreationDate | CREATION_DATE | — | — |
| 75 | XlalinesCurrencyCode | CURRENCY_CODE | — | ✅ |
| 76 | XlalinesCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 77 | XlalinesCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 78 | XlalinesCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 79 | XlalinesDescription | DESCRIPTION | — | ✅ |
| 80 | XlalinesDisplayedLineNumber | DISPLAYED_LINE_NUMBER | — | ✅ |
| 81 | XlalinesEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 82 | XlalinesEnteredCr | ENTERED_CR | — | ✅ |
| 83 | XlalinesEnteredDr | ENTERED_DR | — | ✅ |
| 84 | XlalinesFundsStatusCode | FUNDS_STATUS_CODE | — | — |
| 85 | XlalinesGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | — |
| 86 | XlalinesGlSlLinkId | GL_SL_LINK_ID | — | ✅ |
| 87 | XlalinesGlSlLinkTable | GL_SL_LINK_TABLE | — | ✅ |
| 88 | XlalinesGlTransferModeCode | GL_TRANSFER_MODE_CODE | — | — |
| 89 | XlalinesJgzzReconRef | JGZZ_RECON_REF | — | ✅ |
| 90 | XlalinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 91 | XlalinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 92 | XlalinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 93 | XlalinesLedgerId | LEDGER_ID | — | — |
| 94 | XlalinesMergeCodeCombinationId | MERGE_CODE_COMBINATION_ID | — | — |
| 95 | XlalinesMergePartyId | MERGE_PARTY_ID | — | — |
| 96 | XlalinesMergePartySiteId | MERGE_PARTY_SITE_ID | — | — |
| 97 | XlalinesMpaAccrualEntryFlag | MPA_ACCRUAL_ENTRY_FLAG | — | — |
| 98 | XlalinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 99 | XlalinesOverriddenCodeCombinationId | OVERRIDDEN_CODE_COMBINATION_ID | — | — |
| 100 | XlalinesOverrideReason | OVERRIDE_REASON | — | ✅ |
| 101 | XlalinesPartyId | PARTY_ID | — | — |
| 102 | XlalinesPartySiteId | PARTY_SITE_ID | — | — |
| 103 | XlalinesPartyTypeCode | PARTY_TYPE_CODE | — | — |
| 104 | XlalinesPeriodName | PERIOD_NAME | — | — |
| 105 | XlalinesRequestId | REQUEST_ID | — | — |
| 106 | XlalinesSourceId | SOURCE_ID | — | — |
| 107 | XlalinesSourceTable | SOURCE_TABLE | — | — |
| 108 | XlalinesStatisticalAmount | STATISTICAL_AMOUNT | — | ✅ |
| 109 | XlalinesSubledgerXccCompleteStatus | SUBLEDGER_XCC_COMPLETE_STATUS | — | ✅ |
| 110 | XlalinesSubstitutedCcid | SUBSTITUTED_CCID | — | — |
| 111 | XlalinesSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | — |
| 112 | XlalinesUnroundedAccountedCr | UNROUNDED_ACCOUNTED_CR | — | ✅ |
| 113 | XlalinesUnroundedAccountedDr | UNROUNDED_ACCOUNTED_DR | — | ✅ |
| 114 | XlalinesUnroundedEnteredCr | UNROUNDED_ENTERED_CR | — | ✅ |
| 115 | XlalinesUnroundedEnteredDr | UNROUNDED_ENTERED_DR | — | ✅ |
| 116 | XlalinesUpgBatchId | UPG_BATCH_ID | — | — |
| 117 | XlalinesUpgTaxReferenceId1 | UPG_TAX_REFERENCE_ID1 | — | — |
| 118 | XlalinesUpgTaxReferenceId2 | UPG_TAX_REFERENCE_ID2 | — | — |
| 119 | XlalinesUpgTaxReferenceId3 | UPG_TAX_REFERENCE_ID3 | — | — |
| 120 | XlalinesUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvntTypeXlaHdrVLApplicationId | APPLICATION_ID | — | — |
| 2 | EvntTypeXlaHdrVLDescription | DESCRIPTION | — | — |
| 3 | EvntTypeXlaHdrVLEntityCode | ENTITY_CODE | — | — |
| 4 | EvntTypeXlaHdrVLEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EvntTypeXlaHdrVLEventTypeCode | EVENT_TYPE_CODE | — | — |
| 6 | EvntTypeXlaHdrVLLanguage | LANGUAGE | — | — |
| 7 | EvntTypeXlaHdrVLName | NAME | — | ✅ |

### [[xla_gl_ledgers|XLA_GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaGlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | XlaGlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | XlaGlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | XlaGlLedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 5 | XlaGlLedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 6 | XlaGlLedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 7 | XlaGlLedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 8 | XlaGlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 9 | XlaGlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 10 | XlaGlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 11 | XlaGlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 12 | XlaGlLedgersCompleteFlag | COMPLETE_FLAG | — | — |
| 13 | XlaGlLedgersCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 14 | XlaGlLedgersConfigurationId | CONFIGURATION_ID | — | — |
| 15 | XlaGlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 16 | XlaGlLedgersCreateJeFlag | CREATE_JE_FLAG | — | — |
| 17 | XlaGlLedgersCreatedBy | CREATED_BY | — | — |
| 18 | XlaGlLedgersCreationDate | CREATION_DATE | — | — |
| 19 | XlaGlLedgersCriteriaSetId | CRITERIA_SET_ID | — | — |
| 20 | XlaGlLedgersCrossLgrClrAccCcid | CROSS_LGR_CLR_ACC_CCID | — | — |
| 21 | XlaGlLedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 22 | XlaGlLedgersCurrencyCode | CURRENCY_CODE | — | — |
| 23 | XlaGlLedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 24 | XlaGlLedgersDescription | DESCRIPTION | — | — |
| 25 | XlaGlLedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 26 | XlaGlLedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 27 | XlaGlLedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 28 | XlaGlLedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 29 | XlaGlLedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 30 | XlaGlLedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 31 | XlaGlLedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 32 | XlaGlLedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 33 | XlaGlLedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 34 | XlaGlLedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 35 | XlaGlLedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 36 | XlaGlLedgersIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 37 | XlaGlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 38 | XlaGlLedgersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | XlaGlLedgersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | XlaGlLedgersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | XlaGlLedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 42 | XlaGlLedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 43 | XlaGlLedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 44 | XlaGlLedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 45 | XlaGlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 46 | XlaGlLedgersLedgerId | LEDGER_ID | — | — |
| 47 | XlaGlLedgersMgtSegColumnName | MGT_SEG_COLUMN_NAME | — | — |
| 48 | XlaGlLedgersMgtSegValueOptionCode | MGT_SEG_VALUE_OPTION_CODE | — | — |
| 49 | XlaGlLedgersMgtSegValueSetId | MGT_SEG_VALUE_SET_ID | — | — |
| 50 | XlaGlLedgersName | NAME | — | — |
| 51 | XlaGlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 52 | XlaGlLedgersNumberOfProcessors | NUMBER_OF_PROCESSORS | — | — |
| 53 | XlaGlLedgersObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 54 | XlaGlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | XlaGlLedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 56 | XlaGlLedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 57 | XlaGlLedgersPeriodSetName | PERIOD_SET_NAME | — | — |
| 58 | XlaGlLedgersPopUpStatAccountFlag | POP_UP_STAT_ACCOUNT_FLAG | — | — |
| 59 | XlaGlLedgersPriorPrdNotificationFlag | PRIOR_PRD_NOTIFICATION_FLAG | — | — |
| 60 | XlaGlLedgersProcessingUnitSize | PROCESSING_UNIT_SIZE | — | — |
| 61 | XlaGlLedgersReleaseUpgradeFrom | RELEASE_UPGRADE_FROM | — | — |
| 62 | XlaGlLedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 63 | XlaGlLedgersResEncumbCodeCombinationId | RES_ENCUMB_CODE_COMBINATION_ID | — | — |
| 64 | XlaGlLedgersRetEarnCodeCombinationId | RET_EARN_CODE_COMBINATION_ID | — | — |
| 65 | XlaGlLedgersRevalFromPriLgrCurr | REVAL_FROM_PRI_LGR_CURR | — | — |
| 66 | XlaGlLedgersRoundingCodeCombinationId | ROUNDING_CODE_COMBINATION_ID | — | — |
| 67 | XlaGlLedgersShortName | SHORT_NAME | — | — |
| 68 | XlaGlLedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 69 | XlaGlLedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 70 | XlaGlLedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 71 | XlaGlLedgersSlaDescriptionLanguage | SLA_DESCRIPTION_LANGUAGE | — | — |
| 72 | XlaGlLedgersSlaEnteredCurBalSusCcid | SLA_ENTERED_CUR_BAL_SUS_CCID | — | — |
| 73 | XlaGlLedgersSlaLedgerCashBasisFlag | SLA_LEDGER_CASH_BASIS_FLAG | — | — |
| 74 | XlaGlLedgersSlaLedgerCurBalSusCcid | SLA_LEDGER_CUR_BAL_SUS_CCID | — | — |
| 75 | XlaGlLedgersSlaSequencingFlag | SLA_SEQUENCING_FLAG | — | — |
| 76 | XlaGlLedgersSuspenseAllowedFlag | SUSPENSE_ALLOWED_FLAG | — | — |
| 77 | XlaGlLedgersThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 78 | XlaGlLedgersTrackRoundingImbalanceFlag | TRACK_ROUNDING_IMBALANCE_FLAG | — | — |
| 79 | XlaGlLedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 80 | XlaGlLedgersTranslateEodFlag | TRANSLATE_EOD_FLAG | — | — |
| 81 | XlaGlLedgersTranslateQatdFlag | TRANSLATE_QATD_FLAG | — | — |
| 82 | XlaGlLedgersTranslateYatdFlag | TRANSLATE_YATD_FLAG | — | — |
| 83 | XlaGlLedgersUssglOptionCode | USSGL_OPTION_CODE | — | — |
| 84 | XlaGlLedgersValidateJournalRefDate | VALIDATE_JOURNAL_REF_DATE | — | — |

### [[xla_subledgers|XLA_SUBLEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplnSetupAccountingEnabled | ACCOUNTING_ENABLED | — | — |
| 2 | SubledgerApplnSetupAlcEnabledFlag | ALC_ENABLED_FLAG | — | — |
| 3 | SubledgerApplnSetupApplicationId | APPLICATION_ID | — | — |
| 4 | SubledgerApplnSetupApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 5 | SubledgerApplnSetupApplicationTypeCode | APPLICATION_TYPE_CODE | — | — |
| 6 | SubledgerApplnSetupControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | — |
| 7 | SubledgerApplnSetupCreatedBy | CREATED_BY | — | — |
| 8 | SubledgerApplnSetupCreationDate | CREATION_DATE | — | — |
| 9 | SubledgerApplnSetupDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 10 | SubledgerApplnSetupHeaderAccountingEnabled | ACCOUNTING_ENABLED | — | — |
| 11 | SubledgerApplnSetupHeaderAlcEnabledFlag | ALC_ENABLED_FLAG | — | — |
| 12 | SubledgerApplnSetupHeaderApplicationId | APPLICATION_ID | — | — |
| 13 | SubledgerApplnSetupHeaderApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 14 | SubledgerApplnSetupHeaderApplicationTypeCode | APPLICATION_TYPE_CODE | — | — |
| 15 | SubledgerApplnSetupHeaderControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | — |
| 16 | SubledgerApplnSetupHeaderCreatedBy | CREATED_BY | — | — |
| 17 | SubledgerApplnSetupHeaderCreationDate | CREATION_DATE | — | — |
| 18 | SubledgerApplnSetupHeaderDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 19 | SubledgerApplnSetupHeaderJeSourceName | JE_SOURCE_NAME | — | — |
| 20 | SubledgerApplnSetupHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | SubledgerApplnSetupHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | SubledgerApplnSetupHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | SubledgerApplnSetupHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | SubledgerApplnSetupHeaderRemoteUrl | REMOTE_URL | — | — |
| 25 | SubledgerApplnSetupHeaderRowLockingFlag | ROW_LOCKING_FLAG | — | — |
| 26 | SubledgerApplnSetupHeaderSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 27 | SubledgerApplnSetupHeaderValuationMethodFlag | VALUATION_METHOD_FLAG | — | — |
| 28 | SubledgerApplnSetupJeSourceName | JE_SOURCE_NAME | — | — |
| 29 | SubledgerApplnSetupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | SubledgerApplnSetupLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | SubledgerApplnSetupLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | SubledgerApplnSetupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | SubledgerApplnSetupRemoteUrl | REMOTE_URL | — | — |
| 34 | SubledgerApplnSetupRowLockingFlag | ROW_LOCKING_FLAG | — | — |
| 35 | SubledgerApplnSetupSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 36 | SubledgerApplnSetupValuationMethodFlag | VALUATION_METHOD_FLAG | — | — |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaApplnVLHdrApplicationId | APPLICATION_ID | — | — |
| 2 | XlaApplnVLHdrApplicationName | APPLICATION_NAME | — | — |
| 3 | XlaApplnVLHdrApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 4 | XlaApplnVLHdrDescription | DESCRIPTION | — | — |
| 5 | XlaApplnVLHdrDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 6 | XlaApplnVLHdrJeSourceName | JE_SOURCE_NAME | — | — |
| 7 | XlaApplnVLHdrSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 8 | XlaApplnVLLinesApplicationId | APPLICATION_ID | — | — |
| 9 | XlaApplnVLLinesApplicationName | APPLICATION_NAME | — | — |
| 10 | XlaApplnVLLinesApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 11 | XlaApplnVLLinesDescription | DESCRIPTION | — | — |
| 12 | XlaApplnVLLinesDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 13 | XlaApplnVLLinesJeSourceName | JE_SOURCE_NAME | — | — |
| 14 | XlaApplnVLLinesSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 15 | XlaApplnVLTrxEntityApplicationId | APPLICATION_ID | — | — |
| 16 | XlaApplnVLTrxEntityApplicationName | APPLICATION_NAME | — | — |
| 17 | XlaApplnVLTrxEntityApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 18 | XlaApplnVLTrxEntityDescription | DESCRIPTION | — | — |
| 19 | XlaApplnVLTrxEntityDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 20 | XlaApplnVLTrxEntityJeSourceName | JE_SOURCE_NAME | — | — |
| 21 | XlaApplnVLTrxEntitySecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |

### [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionEntityApplicationId | APPLICATION_ID | — | — |
| 2 | TransactionEntityCreatedBy | CREATED_BY | — | — |
| 3 | TransactionEntityCreationDate | CREATION_DATE | — | — |
| 4 | TransactionEntityEntityCode | ENTITY_CODE | — | ✅ |
| 5 | TransactionEntityEntityId | ENTITY_ID | — | ✅ |
| 6 | TransactionEntityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionEntityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TransactionEntityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TransactionEntityLedgerId | LEDGER_ID | — | — |
| 10 | TransactionEntityLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 11 | TransactionEntityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | TransactionEntityOriginalTransactionNumber | ORIGINAL_TRANSACTION_NUMBER | — | — |
| 13 | TransactionEntitySecurityIdChar1 | SECURITY_ID_CHAR_1 | — | — |
| 14 | TransactionEntitySecurityIdChar2 | SECURITY_ID_CHAR_2 | — | — |
| 15 | TransactionEntitySecurityIdChar3 | SECURITY_ID_CHAR_3 | — | — |
| 16 | TransactionEntitySecurityIdInt1 | SECURITY_ID_INT_1 | — | — |
| 17 | TransactionEntitySecurityIdInt2 | SECURITY_ID_INT_2 | — | — |
| 18 | TransactionEntitySecurityIdInt3 | SECURITY_ID_INT_3 | — | — |
| 19 | TransactionEntitySourceApplicationId | SOURCE_APPLICATION_ID | — | — |
| 20 | TransactionEntitySourceIdChar1 | SOURCE_ID_CHAR_1 | — | — |
| 21 | TransactionEntitySourceIdChar2 | SOURCE_ID_CHAR_2 | — | — |
| 22 | TransactionEntitySourceIdChar3 | SOURCE_ID_CHAR_3 | — | — |
| 23 | TransactionEntitySourceIdChar4 | SOURCE_ID_CHAR_4 | — | — |
| 24 | TransactionEntitySourceIdInt1 | SOURCE_ID_INT_1 | — | — |
| 25 | TransactionEntitySourceIdInt2 | SOURCE_ID_INT_2 | — | — |
| 26 | TransactionEntitySourceIdInt3 | SOURCE_ID_INT_3 | — | — |
| 27 | TransactionEntitySourceIdInt4 | SOURCE_ID_INT_4 | — | — |
| 28 | TransactionEntityTransactionNum | TRANSACTION_NUMBER | — | — |
| 29 | TransactionEntityUpgBatchId | UPG_BATCH_ID | — | — |
| 30 | TransactionEntityUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 31 | TransactionEntityUpgValidFlag | UPG_VALID_FLAG | — | — |
| 32 | TransactionEntityValuationMethod | VALUATION_METHOD | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntActivityCode | ACTIVITY_CODE | — | — |
| 2 | LegalEntEffectiveFrom | EFFECTIVE_FROM | — | — |
| 3 | LegalEntEffectiveTo | EFFECTIVE_TO | — | — |
| 4 | LegalEntEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | LegalEntGeographyId | GEOGRAPHY_ID | — | — |
| 6 | LegalEntLegalEmployerFlag | LEGAL_EMPLOYER_FLAG | — | — |
| 7 | LegalEntLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 8 | LegalEntLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 9 | LegalEntName | NAME | — | ✅ |
| 10 | LegalEntParentPsuId | PARENT_PSU_ID | — | — |
| 11 | LegalEntPartyId | PARTY_ID | — | — |
| 12 | LegalEntPsuFlag | PSU_FLAG | — | — |
| 13 | LegalEntSubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 14 | LegalEntTransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | — |
| 15 | LegalEntTypeOfCompany | TYPE_OF_COMPANY | — | — |
| 16 | XlahdrLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | XleEntityProfilesName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
