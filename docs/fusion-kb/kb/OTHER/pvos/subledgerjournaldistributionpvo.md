---
id: DOC-OTHER-PVO-SubledgerJournalDistributionPVO
doc_type: system-doc
title: "SubledgerJournalDistributionPVO — PVO Cross-Module"
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
  - SubledgerJournalDistributionPVO
  - subledgerjournaldistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalDistributionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Distribution. Acessa as tabelas: FND_DOCUMENT_SEQUENCES, FND_DOC_SEQUENCE_CATEGORIES, FUN_SEQ_ASSIGNMENTS (+19).

**Caminho:** `FscmTopModelAM.FinXlaJrnlEnterJrnlAM.SubledgerJournalDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 626 | 22 | 3 | 120 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos
- [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]] — 11 atributos
- [[fun_seq_assignments|FUN_SEQ_ASSIGNMENTS]] — 32 atributos
- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 33 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 26 atributos
- [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]] — 2 atributos
- [[gl_ledgers|GL_LEDGERS]] — 4 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 10 atributos
- [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]] — 22 atributos
- [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]] — 9 atributos
- [[xla_ae_headers|XLA_AE_HEADERS]] — 55 atributos (14 BICC)
- [[xla_ae_lines|XLA_AE_LINES]] — 120 atributos (78 BICC)
- [[xla_distribution_links|XLA_DISTRIBUTION_LINKS]] — 92 atributos (3 PKs, 23 BICC)
- [[xla_event_classes_vl|XLA_EVENT_CLASSES_VL]] — 6 atributos
- [[xla_event_types_b|XLA_EVENT_TYPES_B]] — 9 atributos
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 13 atributos
- [[xla_subledgers|XLA_SUBLEDGERS]] — 24 atributos
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 28 atributos (2 BICC)
- [[xla_sup_ref_combinations|XLA_SUP_REF_COMBINATIONS]] — 66 atributos (1 BICC)
- [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]] — 32 atributos (1 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 17 atributos

---

## ⚙️ Atributos

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqName | NAME | — | — |
| 5 | DocSeqTableName | TABLE_NAME | — | — |

### [[fnd_doc_sequence_categories|FND_DOC_SEQUENCE_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqCategApplicationId | APPLICATION_ID | — | — |
| 2 | DocSeqCategCode | CODE | — | — |
| 3 | DocSeqCategCreatedBy | CREATED_BY | — | — |
| 4 | DocSeqCategCreationDate | CREATION_DATE | — | — |
| 5 | DocSeqCategDescription | DESCRIPTION | — | — |
| 6 | DocSeqCategLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | DocSeqCategLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DocSeqCategLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DocSeqCategModuleId | MODULE_ID | — | — |
| 10 | DocSeqCategName | NAME | — | — |
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
| 31 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 32 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |

### [[fun_seq_versions|FUN_SEQ_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClActSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 2 | ClActSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | ClActSeqVerEndDate | END_DATE | — | — |
| 4 | ClActSeqVerHeaderName | HEADER_NAME | — | — |
| 5 | ClActSeqVerInitialValue | INITIAL_VALUE | — | — |
| 6 | ClActSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 7 | ClActSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 8 | ClActSeqVerStartDate | START_DATE | — | — |
| 9 | ClActSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 10 | ClActSeqVerVersionName | VERSION_NAME | — | — |
| 11 | CmActSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 12 | CmActSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 13 | CmActSeqVerEndDate | END_DATE | — | — |
| 14 | CmActSeqVerHeaderName | HEADER_NAME | — | — |
| 15 | CmActSeqVerInitialValue | INITIAL_VALUE | — | — |
| 16 | CmActSeqVerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | CmActSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 18 | CmActSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 19 | CmActSeqVerStartDate | START_DATE | — | — |
| 20 | CmActSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 21 | CmActSeqVerVersionName | VERSION_NAME | — | — |
| 22 | DocSeqVerCurrentValue | CURRENT_VALUE | — | — |
| 23 | DocSeqVerDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 24 | DocSeqVerEndDate | END_DATE | — | — |
| 25 | DocSeqVerHeaderName | HEADER_NAME | — | — |
| 26 | DocSeqVerInitialValue | INITIAL_VALUE | — | — |
| 27 | DocSeqVerSeqHeaderId | SEQ_HEADER_ID | — | — |
| 28 | DocSeqVerSeqVersionId | SEQ_VERSION_ID | — | — |
| 29 | DocSeqVerStartDate | START_DATE | — | — |
| 30 | DocSeqVerUseStatusCode | USE_STATUS_CODE | — | — |
| 31 | DocSeqVerVersionName | VERSION_NAME | — | — |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionTypeXlalineConversionType | CONVERSION_TYPE | — | — |
| 2 | ConversionTypeXlalineDescription | DESCRIPTION | — | — |
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
| 26 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |

### [[gl_encumbrance_types_vl|GL_ENCUMBRANCE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEncumbranceTypeEncumbranceType | ENCUMBRANCE_TYPE | — | — |
| 2 | JournalEncumbranceTypeEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersCurrencyCode | CURRENCY_CODE | — | — |
| 3 | LedgersLedgerId | LEDGER_ID | — | ✅ |
| 4 | LedgersName | NAME | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
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

### [[xla_acct_line_types_b|XLA_ACCT_LINE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlLineRuleAccountingClassCode | ACCOUNTING_CLASS_CODE | — | — |
| 2 | JrnlLineRuleAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | — |
| 3 | JrnlLineRuleAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 4 | JrnlLineRuleApplicationId | APPLICATION_ID | — | — |
| 5 | JrnlLineRuleBusinessClassCode | BUSINESS_CLASS_CODE | — | — |
| 6 | JrnlLineRuleBusinessMethodCode | BUSINESS_METHOD_CODE | — | — |
| 7 | JrnlLineRuleCrossLedgerBalancingFlag | CROSS_LEDGER_BALANCING_FLAG | — | — |
| 8 | JrnlLineRuleEnabledFlag | ENABLED_FLAG | — | — |
| 9 | JrnlLineRuleEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 10 | JrnlLineRuleEntityCode | ENTITY_CODE | — | — |
| 11 | JrnlLineRuleEventClassCode | EVENT_CLASS_CODE | — | — |
| 12 | JrnlLineRuleGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | — |
| 13 | JrnlLineRuleGlTransferModeCode | GL_TRANSFER_MODE_CODE | — | — |
| 14 | JrnlLineRuleJournalLineRuleCode | ACCOUNTING_LINE_CODE | — | — |
| 15 | JrnlLineRuleJournalLineRuleTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | — |
| 16 | JrnlLineRuleMergeDuplicateCode | MERGE_DUPLICATE_CODE | — | — |
| 17 | JrnlLineRuleMpaOptionCode | MPA_OPTION_CODE | — | — |
| 18 | JrnlLineRuleNaturalSideCode | NATURAL_SIDE_CODE | — | — |
| 19 | JrnlLineRuleRoundingClassCode | ROUNDING_CLASS_CODE | — | — |
| 20 | JrnlLineRuleSwitchSideFlag | SWITCH_SIDE_FLAG | — | — |
| 21 | JrnlLineRuleTransAttrLang | TRANS_ATTR_LANG | — | — |
| 22 | JrnlLineRuleTransactionCoaId | TRANSACTION_COA_ID | — | — |

### [[xla_acct_line_types_tl|XLA_ACCT_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlLineRuleDescription | DESCRIPTION | — | — |
| 2 | JrnlLineRuleName | NAME | — | — |
| 3 | JrnlLineRuleTLAccountingLineCode | ACCOUNTING_LINE_CODE | — | — |
| 4 | JrnlLineRuleTLAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | — |
| 5 | JrnlLineRuleTLAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 6 | JrnlLineRuleTLApplicationId | APPLICATION_ID | — | — |
| 7 | JrnlLineRuleTLEntityCode | ENTITY_CODE | — | — |
| 8 | JrnlLineRuleTLEventClassCode | EVENT_CLASS_CODE | — | — |
| 9 | JrnlLineRuleTLLanguage | LANGUAGE | — | — |

### [[xla_ae_headers|XLA_AE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlahdrAccountingBatchId | ACCOUNTING_BATCH_ID | — | — |
| 2 | XlahdrAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | XlahdrAccountingEntryStatusCode | ACCOUNTING_ENTRY_STATUS_CODE | — | — |
| 4 | XlahdrAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | — |
| 5 | XlahdrAccrualReversalFlag | ACCRUAL_REVERSAL_FLAG | — | — |
| 6 | XlahdrAeHeaderId | AE_HEADER_ID | — | — |
| 7 | XlahdrAmbContextCode | AMB_CONTEXT_CODE | — | — |
| 8 | XlahdrApplicationId | APPLICATION_ID | — | — |
| 9 | XlahdrBalanceTypeCode | BALANCE_TYPE_CODE | — | ✅ |
| 10 | XlahdrBudgetVersionId | BUDGET_VERSION_ID | — | ✅ |
| 11 | XlahdrCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | — |
| 12 | XlahdrCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | — |
| 13 | XlahdrCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | — |
| 14 | XlahdrCompletedDate | COMPLETED_DATE | — | — |
| 15 | XlahdrCompletionAcctSeqAssignId | COMPLETION_ACCT_SEQ_ASSIGN_ID | — | — |
| 16 | XlahdrCompletionAcctSeqValue | COMPLETION_ACCT_SEQ_VALUE | — | — |
| 17 | XlahdrCompletionAcctSeqVersionId | COMPLETION_ACCT_SEQ_VERSION_ID | — | — |
| 18 | XlahdrCreatedBy | CREATED_BY | — | ✅ |
| 19 | XlahdrCreationDate | CREATION_DATE | — | ✅ |
| 20 | XlahdrDescription | DESCRIPTION | — | ✅ |
| 21 | XlahdrDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 22 | XlahdrDocSequenceAssignId | DOC_SEQUENCE_ASSIGN_ID | — | — |
| 23 | XlahdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 24 | XlahdrDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 25 | XlahdrDocSequenceVersionId | DOC_SEQUENCE_VERSION_ID | — | — |
| 26 | XlahdrEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 27 | XlahdrEntityId | ENTITY_ID | — | — |
| 28 | XlahdrEventId | EVENT_ID | — | — |
| 29 | XlahdrEventTypeCode | EVENT_TYPE_CODE | — | — |
| 30 | XlahdrFundsStatusCode | FUNDS_STATUS_CODE | — | — |
| 31 | XlahdrGlTransferDate | GL_TRANSFER_DATE | — | ✅ |
| 32 | XlahdrGlTransferStatusCode | GL_TRANSFER_STATUS_CODE | — | ✅ |
| 33 | XlahdrGroupId | GROUP_ID | — | — |
| 34 | XlahdrJeCategoryName | JE_CATEGORY_NAME | — | ✅ |
| 35 | XlahdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | XlahdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | XlahdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | XlahdrLedgerId | LEDGER_ID | — | ✅ |
| 39 | XlahdrMergeEventId | MERGE_EVENT_ID | — | — |
| 40 | XlahdrMultiPeriodFlag | MULTIPERIOD_FLAG | — | — |
| 41 | XlahdrNeedBalFlag | NEED_BAL_CODE | — | — |
| 42 | XlahdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | XlahdrPacketId | PACKET_ID | — | — |
| 44 | XlahdrParentAeHeaderId | PARENT_AE_HEADER_ID | — | — |
| 45 | XlahdrParentAeLineNum | PARENT_AE_LINE_NUM | — | — |
| 46 | XlahdrPeriodName | PERIOD_NAME | — | ✅ |
| 47 | XlahdrProductRuleCode | PRODUCT_RULE_CODE | — | — |
| 48 | XlahdrProductRuleTypeCode | PRODUCT_RULE_TYPE_CODE | — | — |
| 49 | XlahdrProductRuleVersion | PRODUCT_RULE_VERSION | — | — |
| 50 | XlahdrReferenceDate | REFERENCE_DATE | — | — |
| 51 | XlahdrRequestId | REQUEST_ID | — | — |
| 52 | XlahdrUpgBatchId | UPG_BATCH_ID | — | — |
| 53 | XlahdrUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 54 | XlahdrUpgValidFlag | UPG_VALID_FLAG | — | — |
| 55 | XlahdrZeroAmountFlag | ZERO_AMOUNT_FLAG | — | — |

### [[xla_ae_lines|XLA_AE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Sr1 | SR1 | — | ✅ |
| 2 | Sr10 | SR10 | — | ✅ |
| 3 | Sr11 | SR11 | — | ✅ |
| 4 | Sr12 | SR12 | — | ✅ |
| 5 | Sr13 | SR13 | — | ✅ |
| 6 | Sr14 | SR14 | — | ✅ |
| 7 | Sr15 | SR15 | — | ✅ |
| 8 | Sr16 | SR16 | — | ✅ |
| 9 | Sr17 | SR17 | — | ✅ |
| 10 | Sr18 | SR18 | — | ✅ |
| 11 | Sr19 | SR19 | — | ✅ |
| 12 | Sr2 | SR2 | — | ✅ |
| 13 | Sr20 | SR20 | — | ✅ |
| 14 | Sr21 | SR21 | — | ✅ |
| 15 | Sr22 | SR22 | — | ✅ |
| 16 | Sr23 | SR23 | — | ✅ |
| 17 | Sr24 | SR24 | — | ✅ |
| 18 | Sr25 | SR25 | — | ✅ |
| 19 | Sr26 | SR26 | — | ✅ |
| 20 | Sr27 | SR27 | — | ✅ |
| 21 | Sr28 | SR28 | — | ✅ |
| 22 | Sr29 | SR29 | — | ✅ |
| 23 | Sr3 | SR3 | — | ✅ |
| 24 | Sr30 | SR30 | — | ✅ |
| 25 | Sr31 | SR31 | — | ✅ |
| 26 | Sr32 | SR32 | — | ✅ |
| 27 | Sr33 | SR33 | — | ✅ |
| 28 | Sr34 | SR34 | — | ✅ |
| 29 | Sr35 | SR35 | — | ✅ |
| 30 | Sr36 | SR36 | — | ✅ |
| 31 | Sr37 | SR37 | — | ✅ |
| 32 | Sr38 | SR38 | — | ✅ |
| 33 | Sr39 | SR39 | — | ✅ |
| 34 | Sr4 | SR4 | — | ✅ |
| 35 | Sr40 | SR40 | — | ✅ |
| 36 | Sr41 | SR41 | — | ✅ |
| 37 | Sr42 | SR42 | — | ✅ |
| 38 | Sr43 | SR43 | — | ✅ |
| 39 | Sr44 | SR44 | — | ✅ |
| 40 | Sr45 | SR45 | — | ✅ |
| 41 | Sr46 | SR46 | — | ✅ |
| 42 | Sr47 | SR47 | — | ✅ |
| 43 | Sr48 | SR48 | — | ✅ |
| 44 | Sr49 | SR49 | — | ✅ |
| 45 | Sr5 | SR5 | — | ✅ |
| 46 | Sr50 | SR50 | — | ✅ |
| 47 | Sr6 | SR6 | — | ✅ |
| 48 | Sr7 | SR7 | — | ✅ |
| 49 | Sr8 | SR8 | — | ✅ |
| 50 | Sr9 | SR9 | — | ✅ |
| 51 | XlalinesAccountOverlaySourceId | ACCOUNT_OVERLAY_SOURCE_ID | — | — |
| 52 | XlalinesAccountedCr | ACCOUNTED_CR | — | — |
| 53 | XlalinesAccountedDr | ACCOUNTED_DR | — | — |
| 54 | XlalinesAccountingClassCode | ACCOUNTING_CLASS_CODE | — | ✅ |
| 55 | XlalinesAccountingDate | ACCOUNTING_DATE | — | — |
| 56 | XlalinesAeHeaderId | AE_HEADER_ID | — | — |
| 57 | XlalinesAeLineNum | AE_LINE_NUM | — | ✅ |
| 58 | XlalinesAnalyticalBalanceFlag | ANALYTICAL_BALANCE_FLAG | — | — |
| 59 | XlalinesApplicationId | APPLICATION_ID | — | ✅ |
| 60 | XlalinesBusinessClassCode | BUSINESS_CLASS_CODE | — | — |
| 61 | XlalinesCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 62 | XlalinesControlBalanceFlag | CONTROL_BALANCE_FLAG | — | — |
| 63 | XlalinesCreatedBy | CREATED_BY | — | — |
| 64 | XlalinesCreationDate | CREATION_DATE | — | — |
| 65 | XlalinesCurrencyCode | CURRENCY_CODE | — | ✅ |
| 66 | XlalinesCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 67 | XlalinesCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 68 | XlalinesCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 69 | XlalinesDescription | DESCRIPTION | — | ✅ |
| 70 | XlalinesDisplayedLineNumber | DISPLAYED_LINE_NUMBER | — | — |
| 71 | XlalinesEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 72 | XlalinesEnteredCr | ENTERED_CR | — | — |
| 73 | XlalinesEnteredDr | ENTERED_DR | — | — |
| 74 | XlalinesFundsStatusCode | FUNDS_STATUS_CODE | — | — |
| 75 | XlalinesGainOrLossFlag | GAIN_OR_LOSS_FLAG | — | — |
| 76 | XlalinesGlSlLinkId | GL_SL_LINK_ID | — | ✅ |
| 77 | XlalinesGlSlLinkTable | GL_SL_LINK_TABLE | — | ✅ |
| 78 | XlalinesGlTransferModeCode | GL_TRANSFER_MODE_CODE | — | — |
| 79 | XlalinesJgzzReconRef | JGZZ_RECON_REF | — | — |
| 80 | XlalinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 81 | XlalinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 82 | XlalinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 83 | XlalinesLedgerId | LEDGER_ID | — | — |
| 84 | XlalinesMergeCodeCombinationId | MERGE_CODE_COMBINATION_ID | — | — |
| 85 | XlalinesMergePartyId | MERGE_PARTY_ID | — | — |
| 86 | XlalinesMergePartySiteId | MERGE_PARTY_SITE_ID | — | — |
| 87 | XlalinesMpaAccrualEntryFlag | MPA_ACCRUAL_ENTRY_FLAG | — | — |
| 88 | XlalinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | XlalinesOverriddenCodeCombinationId | OVERRIDDEN_CODE_COMBINATION_ID | — | ✅ |
| 90 | XlalinesOverrideReason | OVERRIDE_REASON | — | ✅ |
| 91 | XlalinesPartyId | PARTY_ID | — | ✅ |
| 92 | XlalinesPartySiteId | PARTY_SITE_ID | — | ✅ |
| 93 | XlalinesPartyTypeCode | PARTY_TYPE_CODE | — | ✅ |
| 94 | XlalinesRequestId | REQUEST_ID | — | — |
| 95 | XlalinesSourceId | SOURCE_ID | — | — |
| 96 | XlalinesSourceTable | SOURCE_TABLE | — | — |
| 97 | XlalinesSr51 | SR51 | — | ✅ |
| 98 | XlalinesSr52 | SR52 | — | ✅ |
| 99 | XlalinesSr53 | SR53 | — | ✅ |
| 100 | XlalinesSr54 | SR54 | — | ✅ |
| 101 | XlalinesSr55 | SR55 | — | ✅ |
| 102 | XlalinesSr56 | SR56 | — | ✅ |
| 103 | XlalinesSr57 | SR57 | — | ✅ |
| 104 | XlalinesSr58 | SR58 | — | ✅ |
| 105 | XlalinesSr59 | SR59 | — | ✅ |
| 106 | XlalinesSr60 | SR60 | — | ✅ |
| 107 | XlalinesStatisticalAmount | STATISTICAL_AMOUNT | — | — |
| 108 | XlalinesSubledgerXccCompleteStatus | SUBLEDGER_XCC_COMPLETE_STATUS | — | — |
| 109 | XlalinesSubstitutedCcid | SUBSTITUTED_CCID | — | — |
| 110 | XlalinesSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | — |
| 111 | XlalinesSuppRefValues | SUPP_REF_VALUES | — | — |
| 112 | XlalinesUnroundedAccountedCr | UNROUNDED_ACCOUNTED_CR | — | — |
| 113 | XlalinesUnroundedAccountedDr | UNROUNDED_ACCOUNTED_DR | — | — |
| 114 | XlalinesUnroundedEnteredCr | UNROUNDED_ENTERED_CR | — | — |
| 115 | XlalinesUnroundedEnteredDr | UNROUNDED_ENTERED_DR | — | — |
| 116 | XlalinesUpgBatchId | UPG_BATCH_ID | — | ✅ |
| 117 | XlalinesUpgTaxReferenceId1 | UPG_TAX_REFERENCE_ID1 | — | — |
| 118 | XlalinesUpgTaxReferenceId2 | UPG_TAX_REFERENCE_ID2 | — | — |
| 119 | XlalinesUpgTaxReferenceId3 | UPG_TAX_REFERENCE_ID3 | — | — |
| 120 | XlalinesUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |

### [[xla_distribution_links|XLA_DISTRIBUTION_LINKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 2 | RefAeHeaderId | REF_AE_HEADER_ID | 🔑 | ✅ |
| 3 | TempLineNum | TEMP_LINE_NUM | 🔑 | ✅ |
| 4 | XladistlinkAccountingLineCode | ACCOUNTING_LINE_CODE | — | — |
| 5 | XladistlinkAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | — | — |
| 6 | XladistlinkAeLineNum | AE_LINE_NUM | — | — |
| 7 | XladistlinkAllocToApplicationId | ALLOC_TO_APPLICATION_ID | — | — |
| 8 | XladistlinkAllocToDistIdChar1 | ALLOC_TO_DIST_ID_CHAR_1 | — | — |
| 9 | XladistlinkAllocToDistIdChar2 | ALLOC_TO_DIST_ID_CHAR_2 | — | — |
| 10 | XladistlinkAllocToDistIdChar3 | ALLOC_TO_DIST_ID_CHAR_3 | — | — |
| 11 | XladistlinkAllocToDistIdChar4 | ALLOC_TO_DIST_ID_CHAR_4 | — | — |
| 12 | XladistlinkAllocToDistIdChar5 | ALLOC_TO_DIST_ID_CHAR_5 | — | — |
| 13 | XladistlinkAllocToDistIdNum1 | ALLOC_TO_DIST_ID_NUM_1 | — | — |
| 14 | XladistlinkAllocToDistIdNum2 | ALLOC_TO_DIST_ID_NUM_2 | — | — |
| 15 | XladistlinkAllocToDistIdNum3 | ALLOC_TO_DIST_ID_NUM_3 | — | — |
| 16 | XladistlinkAllocToDistIdNum4 | ALLOC_TO_DIST_ID_NUM_4 | — | — |
| 17 | XladistlinkAllocToDistIdNum5 | ALLOC_TO_DIST_ID_NUM_5 | — | — |
| 18 | XladistlinkAllocToDistributionType | ALLOC_TO_DISTRIBUTION_TYPE | — | — |
| 19 | XladistlinkAllocToEntityCode | ALLOC_TO_ENTITY_CODE | — | — |
| 20 | XladistlinkAllocToSourceIdChar1 | ALLOC_TO_SOURCE_ID_CHAR_1 | — | — |
| 21 | XladistlinkAllocToSourceIdChar2 | ALLOC_TO_SOURCE_ID_CHAR_2 | — | — |
| 22 | XladistlinkAllocToSourceIdChar3 | ALLOC_TO_SOURCE_ID_CHAR_3 | — | — |
| 23 | XladistlinkAllocToSourceIdChar4 | ALLOC_TO_SOURCE_ID_CHAR_4 | — | — |
| 24 | XladistlinkAllocToSourceIdNum1 | ALLOC_TO_SOURCE_ID_NUM_1 | — | — |
| 25 | XladistlinkAllocToSourceIdNum2 | ALLOC_TO_SOURCE_ID_NUM_2 | — | — |
| 26 | XladistlinkAllocToSourceIdNum3 | ALLOC_TO_SOURCE_ID_NUM_3 | — | — |
| 27 | XladistlinkAllocToSourceIdNum4 | ALLOC_TO_SOURCE_ID_NUM_4 | — | — |
| 28 | XladistlinkApplicationId | APPLICATION_ID | — | ✅ |
| 29 | XladistlinkAppliedToApplicationId | APPLIED_TO_APPLICATION_ID | — | — |
| 30 | XladistlinkAppliedToDistIdChar1 | APPLIED_TO_DIST_ID_CHAR_1 | — | — |
| 31 | XladistlinkAppliedToDistIdChar2 | APPLIED_TO_DIST_ID_CHAR_2 | — | — |
| 32 | XladistlinkAppliedToDistIdChar3 | APPLIED_TO_DIST_ID_CHAR_3 | — | — |
| 33 | XladistlinkAppliedToDistIdChar4 | APPLIED_TO_DIST_ID_CHAR_4 | — | — |
| 34 | XladistlinkAppliedToDistIdChar5 | APPLIED_TO_DIST_ID_CHAR_5 | — | — |
| 35 | XladistlinkAppliedToDistIdNum1 | APPLIED_TO_DIST_ID_NUM_1 | — | — |
| 36 | XladistlinkAppliedToDistIdNum2 | APPLIED_TO_DIST_ID_NUM_2 | — | — |
| 37 | XladistlinkAppliedToDistIdNum3 | APPLIED_TO_DIST_ID_NUM_3 | — | — |
| 38 | XladistlinkAppliedToDistIdNum4 | APPLIED_TO_DIST_ID_NUM_4 | — | — |
| 39 | XladistlinkAppliedToDistIdNum5 | APPLIED_TO_DIST_ID_NUM_5 | — | — |
| 40 | XladistlinkAppliedToDistributionType | APPLIED_TO_DISTRIBUTION_TYPE | — | ✅ |
| 41 | XladistlinkAppliedToEntityCode | APPLIED_TO_ENTITY_CODE | — | — |
| 42 | XladistlinkAppliedToEntityId | APPLIED_TO_ENTITY_ID | — | — |
| 43 | XladistlinkAppliedToSourceIdChar1 | APPLIED_TO_SOURCE_ID_CHAR_1 | — | — |
| 44 | XladistlinkAppliedToSourceIdChar2 | APPLIED_TO_SOURCE_ID_CHAR_2 | — | — |
| 45 | XladistlinkAppliedToSourceIdChar3 | APPLIED_TO_SOURCE_ID_CHAR_3 | — | — |
| 46 | XladistlinkAppliedToSourceIdChar4 | APPLIED_TO_SOURCE_ID_CHAR_4 | — | — |
| 47 | XladistlinkAppliedToSourceIdNum1 | APPLIED_TO_SOURCE_ID_NUM_1 | — | ✅ |
| 48 | XladistlinkAppliedToSourceIdNum2 | APPLIED_TO_SOURCE_ID_NUM_2 | — | — |
| 49 | XladistlinkAppliedToSourceIdNum3 | APPLIED_TO_SOURCE_ID_NUM_3 | — | — |
| 50 | XladistlinkAppliedToSourceIdNum4 | APPLIED_TO_SOURCE_ID_NUM_4 | — | — |
| 51 | XladistlinkCalculateAcctdAmtsFlag | CALCULATE_ACCTD_AMTS_FLAG | — | — |
| 52 | XladistlinkCalculateGLAmtsFlag | CALCULATE_G_L_AMTS_FLAG | — | — |
| 53 | XladistlinkCreatedBy | CREATED_BY | — | ✅ |
| 54 | XladistlinkCreationDate | CREATION_DATE | — | ✅ |
| 55 | XladistlinkDocRoundingAcctdAmt | DOC_ROUNDING_ACCTD_AMT | — | — |
| 56 | XladistlinkDocRoundingEnteredAmt | DOC_ROUNDING_ENTERED_AMT | — | — |
| 57 | XladistlinkDocumentRoundingLevel | DOCUMENT_ROUNDING_LEVEL | — | — |
| 58 | XladistlinkEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 59 | XladistlinkEventId | EVENT_ID | — | — |
| 60 | XladistlinkEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 61 | XladistlinkGainOrLossRef | GAIN_OR_LOSS_REF | — | — |
| 62 | XladistlinkLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | XladistlinkLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | XladistlinkLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 65 | XladistlinkLineDefinitionCode | LINE_DEFINITION_CODE | — | — |
| 66 | XladistlinkLineDefinitionOwnerCode | LINE_DEFINITION_OWNER_CODE | — | — |
| 67 | XladistlinkMergeDuplicateCode | MERGE_DUPLICATE_CODE | — | — |
| 68 | XladistlinkObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | XladistlinkRefAeLineNum | REF_AE_LINE_NUM | — | ✅ |
| 70 | XladistlinkRefEventId | REF_EVENT_ID | — | — |
| 71 | XladistlinkRefTempLineNum | REF_TEMP_LINE_NUM | — | — |
| 72 | XladistlinkRoundingClassCode | ROUNDING_CLASS_CODE | — | — |
| 73 | XladistlinkSourceDistributionIdChar1 | SOURCE_DISTRIBUTION_ID_CHAR_1 | — | — |
| 74 | XladistlinkSourceDistributionIdChar2 | SOURCE_DISTRIBUTION_ID_CHAR_2 | — | — |
| 75 | XladistlinkSourceDistributionIdChar3 | SOURCE_DISTRIBUTION_ID_CHAR_3 | — | — |
| 76 | XladistlinkSourceDistributionIdChar4 | SOURCE_DISTRIBUTION_ID_CHAR_4 | — | ✅ |
| 77 | XladistlinkSourceDistributionIdChar5 | SOURCE_DISTRIBUTION_ID_CHAR_5 | — | — |
| 78 | XladistlinkSourceDistributionIdNum1 | SOURCE_DISTRIBUTION_ID_NUM_1 | — | ✅ |
| 79 | XladistlinkSourceDistributionIdNum2 | SOURCE_DISTRIBUTION_ID_NUM_2 | — | ✅ |
| 80 | XladistlinkSourceDistributionIdNum3 | SOURCE_DISTRIBUTION_ID_NUM_3 | — | ✅ |
| 81 | XladistlinkSourceDistributionIdNum4 | SOURCE_DISTRIBUTION_ID_NUM_4 | — | — |
| 82 | XladistlinkSourceDistributionIdNum5 | SOURCE_DISTRIBUTION_ID_NUM_5 | — | ✅ |
| 83 | XladistlinkSourceDistributionType | SOURCE_DISTRIBUTION_TYPE | — | ✅ |
| 84 | XladistlinkStatisticalAmount | STATISTICAL_AMOUNT | — | — |
| 85 | XladistlinkTaxLineRefId | TAX_LINE_REF_ID | — | — |
| 86 | XladistlinkTaxRecNrecDistRefId | TAX_REC_NREC_DIST_REF_ID | — | — |
| 87 | XladistlinkTaxSummaryLineRefId | TAX_SUMMARY_LINE_REF_ID | — | — |
| 88 | XladistlinkUnroundedAccountedCr | UNROUNDED_ACCOUNTED_CR | — | ✅ |
| 89 | XladistlinkUnroundedAccountedDr | UNROUNDED_ACCOUNTED_DR | — | ✅ |
| 90 | XladistlinkUnroundedEnteredCr | UNROUNDED_ENTERED_CR | — | ✅ |
| 91 | XladistlinkUnroundedEnteredDr | UNROUNDED_ENTERED_DR | — | ✅ |
| 92 | XladistlinkUpgBatchId | UPG_BATCH_ID | — | — |

### [[xla_event_classes_vl|XLA_EVENT_CLASSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClsVLApplicationId | APPLICATION_ID | — | — |
| 2 | EventClsVLDescription | DESCRIPTION | — | — |
| 3 | EventClsVLEntityCode | ENTITY_CODE | — | — |
| 4 | EventClsVLEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventClsVLName | NAME | — | — |
| 6 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |

### [[xla_event_types_b|XLA_EVENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeAccountingFlag | ACCOUNTING_FLAG | — | — |
| 2 | EventTypeApplicationId | APPLICATION_ID | — | — |
| 3 | EventTypeEnabledFlag | ENABLED_FLAG | — | — |
| 4 | EventTypeEntityCode | ENTITY_CODE | — | — |
| 5 | EventTypeEventClassCode | EVENT_CLASS_CODE | — | — |
| 6 | EventTypeEventTypeCode | EVENT_TYPE_CODE | — | — |
| 7 | EventTypeTaxFlag | TAX_FLAG | — | — |
| 8 | EventTypeTransactionReversalFlag | TRANSACTION_REVERSAL_FLAG | — | — |
| 9 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeDescription | DESCRIPTION | — | — |
| 2 | EventTypeName | NAME | — | — |
| 3 | EventTypeTLApplicationId | APPLICATION_ID | — | — |
| 4 | EventTypeTLEntityCode | ENTITY_CODE | — | — |
| 5 | EventTypeTLEventClassCode | EVENT_CLASS_CODE | — | — |
| 6 | EventTypeTLEventTypeCode | EVENT_TYPE_CODE | — | — |
| 7 | EventTypeTLLanguage | LANGUAGE | — | — |
| 8 | EventTypeXlaHdrApplicationId | APPLICATION_ID | — | — |
| 9 | EventTypeXlaHdrEntityCode | ENTITY_CODE | — | — |
| 10 | EventTypeXlaHdrEventClassCode | EVENT_CLASS_CODE | — | — |
| 11 | EventTypeXlaHdrEventTypeCode | EVENT_TYPE_CODE | — | — |
| 12 | EventTypeXlaHdrLanguage | LANGUAGE | — | — |
| 13 | EventTypeXlaHdrName | NAME | — | — |

### [[xla_subledgers|XLA_SUBLEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplnSetupAccountingEnabled | ACCOUNTING_ENABLED | — | — |
| 2 | SubledgerApplnSetupAlcEnabledFlag | ALC_ENABLED_FLAG | — | — |
| 3 | SubledgerApplnSetupApplicationId | APPLICATION_ID | — | — |
| 4 | SubledgerApplnSetupApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 5 | SubledgerApplnSetupApplicationTypeCode | APPLICATION_TYPE_CODE | — | — |
| 6 | SubledgerApplnSetupControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | — |
| 7 | SubledgerApplnSetupDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 8 | SubledgerApplnSetupHeaderAccountingEnabled | ACCOUNTING_ENABLED | — | — |
| 9 | SubledgerApplnSetupHeaderAlcEnabledFlag | ALC_ENABLED_FLAG | — | — |
| 10 | SubledgerApplnSetupHeaderApplicationId | APPLICATION_ID | — | — |
| 11 | SubledgerApplnSetupHeaderApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 12 | SubledgerApplnSetupHeaderApplicationTypeCode | APPLICATION_TYPE_CODE | — | — |
| 13 | SubledgerApplnSetupHeaderControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | — |
| 14 | SubledgerApplnSetupHeaderDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 15 | SubledgerApplnSetupHeaderJeSourceName | JE_SOURCE_NAME | — | — |
| 16 | SubledgerApplnSetupHeaderRemoteUrl | REMOTE_URL | — | — |
| 17 | SubledgerApplnSetupHeaderRowLockingFlag | ROW_LOCKING_FLAG | — | — |
| 18 | SubledgerApplnSetupHeaderSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 19 | SubledgerApplnSetupHeaderValuationMethodFlag | VALUATION_METHOD_FLAG | — | — |
| 20 | SubledgerApplnSetupJeSourceName | JE_SOURCE_NAME | — | — |
| 21 | SubledgerApplnSetupRemoteUrl | REMOTE_URL | — | — |
| 22 | SubledgerApplnSetupRowLockingFlag | ROW_LOCKING_FLAG | — | — |
| 23 | SubledgerApplnSetupSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 24 | SubledgerApplnSetupValuationMethodFlag | VALUATION_METHOD_FLAG | — | — |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaApplnVLHdrApplicationId | APPLICATION_ID | — | — |
| 2 | XlaApplnVLHdrApplicationName | APPLICATION_NAME | — | — |
| 3 | XlaApplnVLHdrApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 4 | XlaApplnVLHdrDescription | DESCRIPTION | — | — |
| 5 | XlaApplnVLHdrDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 6 | XlaApplnVLHdrJeSourceName | JE_SOURCE_NAME | — | — |
| 7 | XlaApplnVLHdrSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 8 | XlaApplnVLLinesApplicationId | APPLICATION_ID | — | — |
| 9 | XlaApplnVLLinesApplicationName | APPLICATION_NAME | — | — |
| 10 | XlaApplnVLLinesApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 11 | XlaApplnVLLinesDescription | DESCRIPTION | — | — |
| 12 | XlaApplnVLLinesDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 13 | XlaApplnVLLinesJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 14 | XlaApplnVLLinesSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 15 | XlaApplnVLTrxEntityApplicationId | APPLICATION_ID | — | — |
| 16 | XlaApplnVLTrxEntityApplicationName | APPLICATION_NAME | — | — |
| 17 | XlaApplnVLTrxEntityApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 18 | XlaApplnVLTrxEntityDescription | DESCRIPTION | — | — |
| 19 | XlaApplnVLTrxEntityDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 20 | XlaApplnVLTrxEntityJeSourceName | JE_SOURCE_NAME | — | — |
| 21 | XlaApplnVLTrxEntitySecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |
| 22 | XlaApplnVLdistLinkApplicationId | APPLICATION_ID | — | — |
| 23 | XlaApplnVLdistLinkApplicationName | APPLICATION_NAME | — | — |
| 24 | XlaApplnVLdistLinkApplicationShortName | APPLICATION_SHORT_NAME | — | — |
| 25 | XlaApplnVLdistLinkDescription | DESCRIPTION | — | — |
| 26 | XlaApplnVLdistLinkDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | — |
| 27 | XlaApplnVLdistLinkJeSourceName | JE_SOURCE_NAME | — | — |
| 28 | XlaApplnVLdistLinkSecurityFunctionName | SECURITY_FUNCTION_NAME | — | — |

### [[xla_sup_ref_combinations|XLA_SUP_REF_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppRefCombinationCreatedBy | CREATED_BY | — | — |
| 2 | SuppRefCombinationCreationDate | CREATION_DATE | — | — |
| 3 | SuppRefCombinationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | SuppRefCombinationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | SuppRefCombinationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | SuppRefCombinationSupRefCode1 | SUP_REF_CODE1 | — | — |
| 7 | SuppRefCombinationSupRefCode10 | SUP_REF_CODE10 | — | — |
| 8 | SuppRefCombinationSupRefCode11 | SUP_REF_CODE11 | — | — |
| 9 | SuppRefCombinationSupRefCode12 | SUP_REF_CODE12 | — | — |
| 10 | SuppRefCombinationSupRefCode13 | SUP_REF_CODE13 | — | — |
| 11 | SuppRefCombinationSupRefCode14 | SUP_REF_CODE14 | — | — |
| 12 | SuppRefCombinationSupRefCode15 | SUP_REF_CODE15 | — | — |
| 13 | SuppRefCombinationSupRefCode16 | SUP_REF_CODE16 | — | — |
| 14 | SuppRefCombinationSupRefCode17 | SUP_REF_CODE17 | — | — |
| 15 | SuppRefCombinationSupRefCode18 | SUP_REF_CODE18 | — | — |
| 16 | SuppRefCombinationSupRefCode19 | SUP_REF_CODE19 | — | — |
| 17 | SuppRefCombinationSupRefCode2 | SUP_REF_CODE2 | — | — |
| 18 | SuppRefCombinationSupRefCode20 | SUP_REF_CODE20 | — | — |
| 19 | SuppRefCombinationSupRefCode21 | SUP_REF_CODE21 | — | — |
| 20 | SuppRefCombinationSupRefCode22 | SUP_REF_CODE22 | — | — |
| 21 | SuppRefCombinationSupRefCode23 | SUP_REF_CODE23 | — | — |
| 22 | SuppRefCombinationSupRefCode24 | SUP_REF_CODE24 | — | — |
| 23 | SuppRefCombinationSupRefCode25 | SUP_REF_CODE25 | — | — |
| 24 | SuppRefCombinationSupRefCode26 | SUP_REF_CODE26 | — | — |
| 25 | SuppRefCombinationSupRefCode27 | SUP_REF_CODE27 | — | — |
| 26 | SuppRefCombinationSupRefCode28 | SUP_REF_CODE28 | — | — |
| 27 | SuppRefCombinationSupRefCode29 | SUP_REF_CODE29 | — | — |
| 28 | SuppRefCombinationSupRefCode3 | SUP_REF_CODE3 | — | — |
| 29 | SuppRefCombinationSupRefCode30 | SUP_REF_CODE30 | — | — |
| 30 | SuppRefCombinationSupRefCode31 | SUP_REF_CODE31 | — | — |
| 31 | SuppRefCombinationSupRefCode32 | SUP_REF_CODE32 | — | — |
| 32 | SuppRefCombinationSupRefCode33 | SUP_REF_CODE33 | — | — |
| 33 | SuppRefCombinationSupRefCode34 | SUP_REF_CODE34 | — | — |
| 34 | SuppRefCombinationSupRefCode35 | SUP_REF_CODE35 | — | — |
| 35 | SuppRefCombinationSupRefCode36 | SUP_REF_CODE36 | — | — |
| 36 | SuppRefCombinationSupRefCode37 | SUP_REF_CODE37 | — | — |
| 37 | SuppRefCombinationSupRefCode38 | SUP_REF_CODE38 | — | — |
| 38 | SuppRefCombinationSupRefCode39 | SUP_REF_CODE39 | — | — |
| 39 | SuppRefCombinationSupRefCode4 | SUP_REF_CODE4 | — | — |
| 40 | SuppRefCombinationSupRefCode40 | SUP_REF_CODE40 | — | — |
| 41 | SuppRefCombinationSupRefCode41 | SUP_REF_CODE41 | — | — |
| 42 | SuppRefCombinationSupRefCode42 | SUP_REF_CODE42 | — | — |
| 43 | SuppRefCombinationSupRefCode43 | SUP_REF_CODE43 | — | — |
| 44 | SuppRefCombinationSupRefCode44 | SUP_REF_CODE44 | — | — |
| 45 | SuppRefCombinationSupRefCode45 | SUP_REF_CODE45 | — | — |
| 46 | SuppRefCombinationSupRefCode46 | SUP_REF_CODE46 | — | — |
| 47 | SuppRefCombinationSupRefCode47 | SUP_REF_CODE47 | — | — |
| 48 | SuppRefCombinationSupRefCode48 | SUP_REF_CODE48 | — | — |
| 49 | SuppRefCombinationSupRefCode49 | SUP_REF_CODE49 | — | — |
| 50 | SuppRefCombinationSupRefCode5 | SUP_REF_CODE5 | — | — |
| 51 | SuppRefCombinationSupRefCode50 | SUP_REF_CODE50 | — | — |
| 52 | SuppRefCombinationSupRefCode51 | SUP_REF_CODE51 | — | — |
| 53 | SuppRefCombinationSupRefCode52 | SUP_REF_CODE52 | — | — |
| 54 | SuppRefCombinationSupRefCode53 | SUP_REF_CODE53 | — | — |
| 55 | SuppRefCombinationSupRefCode54 | SUP_REF_CODE54 | — | — |
| 56 | SuppRefCombinationSupRefCode55 | SUP_REF_CODE55 | — | — |
| 57 | SuppRefCombinationSupRefCode56 | SUP_REF_CODE56 | — | — |
| 58 | SuppRefCombinationSupRefCode57 | SUP_REF_CODE57 | — | — |
| 59 | SuppRefCombinationSupRefCode58 | SUP_REF_CODE58 | — | — |
| 60 | SuppRefCombinationSupRefCode59 | SUP_REF_CODE59 | — | — |
| 61 | SuppRefCombinationSupRefCode6 | SUP_REF_CODE6 | — | — |
| 62 | SuppRefCombinationSupRefCode60 | SUP_REF_CODE60 | — | — |
| 63 | SuppRefCombinationSupRefCode7 | SUP_REF_CODE7 | — | — |
| 64 | SuppRefCombinationSupRefCode8 | SUP_REF_CODE8 | — | — |
| 65 | SuppRefCombinationSupRefCode9 | SUP_REF_CODE9 | — | — |
| 66 | SuppRefCombinationSuppRefCombinationId | SUPP_REF_COMBINATION_ID | — | ✅ |

### [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionEntityApplicationId | APPLICATION_ID | — | — |
| 2 | TransactionEntityCreatedBy | CREATED_BY | — | — |
| 3 | TransactionEntityCreationDate | CREATION_DATE | — | — |
| 4 | TransactionEntityEntityCode | ENTITY_CODE | — | — |
| 5 | TransactionEntityEntityId | ENTITY_ID | — | — |
| 6 | TransactionEntityLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | TransactionEntityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TransactionEntityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TransactionEntityLedgerId | LEDGER_ID | — | — |
| 10 | TransactionEntityLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 11 | TransactionEntityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | TransactionEntityOriginalTransactionNumber | ORIGINAL_TRANSACTION_NUMBER | — | — |
| 13 | TransactionEntitySecurityIdChar1 | SECURITY_ID_CHAR_1 | — | — |
| 14 | TransactionEntitySecurityIdChar2 | SECURITY_ID_CHAR_2 | — | — |
| 15 | TransactionEntitySecurityIdChar3 | SECURITY_ID_CHAR_3 | — | — |
| 16 | TransactionEntitySecurityIdInt1 | SECURITY_ID_INT_1 | — | ✅ |
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
| 9 | LegalEntName | NAME | — | — |
| 10 | LegalEntParentPsuId | PARENT_PSU_ID | — | — |
| 11 | LegalEntPartyId | PARTY_ID | — | — |
| 12 | LegalEntPsuFlag | PSU_FLAG | — | — |
| 13 | LegalEntSubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 14 | LegalEntTransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | — |
| 15 | LegalEntTypeOfCompany | TYPE_OF_COMPANY | — | — |
| 16 | XlahdrLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | XleEntityProfilesName | NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
