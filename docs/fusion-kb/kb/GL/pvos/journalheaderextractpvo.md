---
id: DOC-GL-PVO-JournalHeaderExtractPVO
doc_type: system-doc
title: "JournalHeaderExtractPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JournalHeaderExtractPVO
  - journalheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Header Extract. Acessa as tabelas: GL_JE_BATCHES, GL_JE_HEADERS.

**Caminho:** `FscmTopModelAM.FinGlJrnlEntriesAM.JournalHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 164 | 2 | 1 | 1 | 1% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_batches|GL_JE_BATCHES]] — 51 atributos
- [[gl_je_headers|GL_JE_HEADERS]] — 113 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[gl_je_batches|GL_JE_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeBatchesAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlJeBatchesActualFlag | ACTUAL_FLAG | — | — |
| 3 | GlJeBatchesApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 4 | GlJeBatchesApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 5 | GlJeBatchesAttribute101 | ATTRIBUTE10 | — | — |
| 6 | GlJeBatchesAttribute11 | ATTRIBUTE1 | — | — |
| 7 | GlJeBatchesAttribute21 | ATTRIBUTE2 | — | — |
| 8 | GlJeBatchesAttribute31 | ATTRIBUTE3 | — | — |
| 9 | GlJeBatchesAttribute41 | ATTRIBUTE4 | — | — |
| 10 | GlJeBatchesAttribute51 | ATTRIBUTE5 | — | — |
| 11 | GlJeBatchesAttribute61 | ATTRIBUTE6 | — | — |
| 12 | GlJeBatchesAttribute71 | ATTRIBUTE7 | — | — |
| 13 | GlJeBatchesAttribute81 | ATTRIBUTE8 | — | — |
| 14 | GlJeBatchesAttribute91 | ATTRIBUTE9 | — | — |
| 15 | GlJeBatchesAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 16 | GlJeBatchesAttributeCategory21 | ATTRIBUTE_CATEGORY2 | — | — |
| 17 | GlJeBatchesAverageJournalFlag | AVERAGE_JOURNAL_FLAG | — | — |
| 18 | GlJeBatchesBudgetaryControlStatus | BUDGETARY_CONTROL_STATUS | — | — |
| 19 | GlJeBatchesChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 20 | GlJeBatchesControlTotal | CONTROL_TOTAL | — | — |
| 21 | GlJeBatchesCreatedBy | CREATED_BY | — | — |
| 22 | GlJeBatchesCreationDate | CREATION_DATE | — | — |
| 23 | GlJeBatchesDateCreated | DATE_CREATED | — | — |
| 24 | GlJeBatchesDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | — |
| 25 | GlJeBatchesDefaultPeriodName | DEFAULT_PERIOD_NAME | — | — |
| 26 | GlJeBatchesDescription | DESCRIPTION | — | — |
| 27 | GlJeBatchesEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 28 | GlJeBatchesErrorMessage | ERROR_MESSAGE | — | — |
| 29 | GlJeBatchesFundsStatusCode | FUNDS_STATUS_CODE | — | — |
| 30 | GlJeBatchesGroupId | GROUP_ID | — | — |
| 31 | GlJeBatchesJeBatchId | JE_BATCH_ID | — | — |
| 32 | GlJeBatchesJeSource | JE_SOURCE | — | — |
| 33 | GlJeBatchesLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 34 | GlJeBatchesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | GlJeBatchesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | GlJeBatchesName | NAME | — | — |
| 37 | GlJeBatchesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | GlJeBatchesPacketId | PACKET_ID | — | — |
| 39 | GlJeBatchesParentJeBatchId | PARENT_JE_BATCH_ID | — | — |
| 40 | GlJeBatchesPeriodSetName | PERIOD_SET_NAME | — | — |
| 41 | GlJeBatchesPostedDate | POSTED_DATE | — | — |
| 42 | GlJeBatchesPostedDateTime | POSTED_DATE | — | — |
| 43 | GlJeBatchesPostingRunId | POSTING_RUN_ID | — | — |
| 44 | GlJeBatchesRequestId | REQUEST_ID | — | — |
| 45 | GlJeBatchesRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | — |
| 46 | GlJeBatchesRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | — |
| 47 | GlJeBatchesRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 48 | GlJeBatchesRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 49 | GlJeBatchesStatus | STATUS | — | — |
| 50 | GlJeBatchesStatusVerified | STATUS_VERIFIED | — | — |
| 51 | GlJeBatchesUnreservationPacketId | UNRESERVATION_PACKET_ID | — | — |

### [[gl_je_headers|GL_JE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeHeadersAccrualRevChangeSignFlag | ACCRUAL_REV_CHANGE_SIGN_FLAG | — | — |
| 2 | GlJeHeadersAccrualRevEffectiveDate | ACCRUAL_REV_EFFECTIVE_DATE | — | — |
| 3 | GlJeHeadersAccrualRevFlag | ACCRUAL_REV_FLAG | — | — |
| 4 | GlJeHeadersAccrualRevJeHeaderId | ACCRUAL_REV_JE_HEADER_ID | — | — |
| 5 | GlJeHeadersAccrualRevPeriodName | ACCRUAL_REV_PERIOD_NAME | — | — |
| 6 | GlJeHeadersAccrualRevStatus | ACCRUAL_REV_STATUS | — | — |
| 7 | GlJeHeadersActualFlag | ACTUAL_FLAG | — | — |
| 8 | GlJeHeadersAttribute1 | ATTRIBUTE1 | — | — |
| 9 | GlJeHeadersAttribute10 | ATTRIBUTE10 | — | — |
| 10 | GlJeHeadersAttribute2 | ATTRIBUTE2 | — | — |
| 11 | GlJeHeadersAttribute3 | ATTRIBUTE3 | — | — |
| 12 | GlJeHeadersAttribute4 | ATTRIBUTE4 | — | — |
| 13 | GlJeHeadersAttribute5 | ATTRIBUTE5 | — | — |
| 14 | GlJeHeadersAttribute6 | ATTRIBUTE6 | — | — |
| 15 | GlJeHeadersAttribute7 | ATTRIBUTE7 | — | — |
| 16 | GlJeHeadersAttribute8 | ATTRIBUTE8 | — | — |
| 17 | GlJeHeadersAttribute9 | ATTRIBUTE9 | — | — |
| 18 | GlJeHeadersAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | GlJeHeadersAttributeCategory2 | ATTRIBUTE_CATEGORY2 | — | — |
| 20 | GlJeHeadersBalancedJeFlag | BALANCED_JE_FLAG | — | — |
| 21 | GlJeHeadersBalancingSegmentValue | BALANCING_SEGMENT_VALUE | — | — |
| 22 | GlJeHeadersBudgetVersionId | BUDGET_VERSION_ID | — | — |
| 23 | GlJeHeadersCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | — |
| 24 | GlJeHeadersCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | — |
| 25 | GlJeHeadersCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | — |
| 26 | GlJeHeadersControlTotal | CONTROL_TOTAL | — | — |
| 27 | GlJeHeadersConversionFlag | CONVERSION_FLAG | — | — |
| 28 | GlJeHeadersCrBalSegValue | CR_BAL_SEG_VALUE | — | — |
| 29 | GlJeHeadersCreatedBy | CREATED_BY | — | — |
| 30 | GlJeHeadersCreationDate | CREATION_DATE | — | — |
| 31 | GlJeHeadersCurrencyCode | CURRENCY_CODE | — | — |
| 32 | GlJeHeadersCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 33 | GlJeHeadersCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 34 | GlJeHeadersCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 35 | GlJeHeadersDateCreated | DATE_CREATED | — | — |
| 36 | GlJeHeadersDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | — |
| 37 | GlJeHeadersDescription | DESCRIPTION | — | — |
| 38 | GlJeHeadersDisplayAlcJournalFlag | DISPLAY_ALC_JOURNAL_FLAG | — | — |
| 39 | GlJeHeadersDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 40 | GlJeHeadersDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 41 | GlJeHeadersDrBalSegValue | DR_BAL_SEG_VALUE | — | — |
| 42 | GlJeHeadersEarliestPostableDate | EARLIEST_POSTABLE_DATE | — | — |
| 43 | GlJeHeadersEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | — |
| 44 | GlJeHeadersExternalReference | EXTERNAL_REFERENCE | — | — |
| 45 | GlJeHeadersFromRecurringHeaderId | FROM_RECURRING_HEADER_ID | — | — |
| 46 | GlJeHeadersGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 47 | GlJeHeadersGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 48 | GlJeHeadersGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 49 | GlJeHeadersGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 50 | GlJeHeadersGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 51 | GlJeHeadersGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 52 | GlJeHeadersGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 53 | GlJeHeadersGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 54 | GlJeHeadersGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 55 | GlJeHeadersGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 56 | GlJeHeadersGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 57 | GlJeHeadersGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 58 | GlJeHeadersGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 59 | GlJeHeadersGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 60 | GlJeHeadersGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 61 | GlJeHeadersGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 62 | GlJeHeadersGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 63 | GlJeHeadersGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 64 | GlJeHeadersGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 65 | GlJeHeadersGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 66 | GlJeHeadersGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 67 | GlJeHeadersGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 68 | GlJeHeadersGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 69 | GlJeHeadersGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 70 | GlJeHeadersGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 71 | GlJeHeadersGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 72 | GlJeHeadersGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 73 | GlJeHeadersGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 74 | GlJeHeadersGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 75 | GlJeHeadersGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 76 | GlJeHeadersGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 77 | GlJeHeadersIntercompanyMode | INTERCOMPANY_MODE | — | — |
| 78 | GlJeHeadersJeBatchId | JE_BATCH_ID | — | — |
| 79 | GlJeHeadersJeCategory | JE_CATEGORY | — | — |
| 80 | GlJeHeadersJeFromSlaFlag | JE_FROM_SLA_FLAG | — | — |
| 81 | GlJeHeadersJeSource | JE_SOURCE | — | — |
| 82 | GlJeHeadersLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 83 | GlJeHeadersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | GlJeHeadersLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 85 | GlJeHeadersLedgerId | LEDGER_ID | — | — |
| 86 | GlJeHeadersLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 87 | GlJeHeadersLocalDocSequenceId | LOCAL_DOC_SEQUENCE_ID | — | — |
| 88 | GlJeHeadersLocalDocSequenceValue | LOCAL_DOC_SEQUENCE_VALUE | — | — |
| 89 | GlJeHeadersMultiBalSegFlag | MULTI_BAL_SEG_FLAG | — | — |
| 90 | GlJeHeadersMultiCurrencyFlag | MULTI_CURRENCY_FLAG | — | — |
| 91 | GlJeHeadersName | NAME | — | — |
| 92 | GlJeHeadersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 93 | GlJeHeadersOriginatingBalSegValue | ORIGINATING_BAL_SEG_VALUE | — | — |
| 94 | GlJeHeadersParentJeHeaderId | PARENT_JE_HEADER_ID | — | — |
| 95 | GlJeHeadersPeriodName | PERIOD_NAME | — | — |
| 96 | GlJeHeadersPostCurrencyCode | POST_CURRENCY_CODE | — | — |
| 97 | GlJeHeadersPostMultiCurrencyFlag | POST_MULTI_CURRENCY_FLAG | — | — |
| 98 | GlJeHeadersPostedDate | POSTED_DATE | — | — |
| 99 | GlJeHeadersPostedDateTime | POSTED_DATE | — | — |
| 100 | GlJeHeadersPostingAcctSeqAssignId | POSTING_ACCT_SEQ_ASSIGN_ID | — | — |
| 101 | GlJeHeadersPostingAcctSeqValue | POSTING_ACCT_SEQ_VALUE | — | — |
| 102 | GlJeHeadersPostingAcctSeqVersionId | POSTING_ACCT_SEQ_VERSION_ID | — | — |
| 103 | GlJeHeadersReferenceDate | REFERENCE_DATE | — | — |
| 104 | GlJeHeadersReversedJeHeaderId | REVERSED_JE_HEADER_ID | — | — |
| 105 | GlJeHeadersRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | — |
| 106 | GlJeHeadersRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | — |
| 107 | GlJeHeadersRunningTotalCr | RUNNING_TOTAL_CR | — | — |
| 108 | GlJeHeadersRunningTotalDr | RUNNING_TOTAL_DR | — | — |
| 109 | GlJeHeadersStatus | STATUS | — | — |
| 110 | GlJeHeadersTaxLegalEntityId | TAX_LEGAL_ENTITY_ID | — | — |
| 111 | GlJeHeadersTaxStatusCode | TAX_STATUS_CODE | — | — |
| 112 | GlJeHeadersUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 113 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
