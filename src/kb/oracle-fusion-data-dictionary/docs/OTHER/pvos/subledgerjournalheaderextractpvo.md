---
id: DOC-OTHER-PVO-SubledgerJournalHeaderExtractPVO
doc_type: system-doc
title: "SubledgerJournalHeaderExtractPVO — PVO Cross-Module"
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
  - SubledgerJournalHeaderExtractPVO
  - subledgerjournalheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Header Extract. Acessa as tabelas: FUN_SEQ_VERSIONS, XLA_AE_HEADERS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerJournalHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 2 | 2 | 56 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[fun_seq_versions|FUN_SEQ_VERSIONS]] — 6 atributos
- [[xla_ae_headers|XLA_AE_HEADERS]] — 72 atributos (2 PKs, 56 BICC)

---

## ⚙️ Atributos

### [[fun_seq_versions|FUN_SEQ_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CloseAcctSeqVersionsHeaderName | HEADER_NAME | — | — |
| 2 | CloseAcctSeqVersionsSeqVersionId | SEQ_VERSION_ID | — | — |
| 3 | CloseAcctSeqVersionsVersionName | VERSION_NAME | — | — |
| 4 | CompAcctSeqVersionsHeaderName | HEADER_NAME | — | — |
| 5 | CompAcctSeqVersionsSeqVersionId | SEQ_VERSION_ID | — | — |
| 6 | CompAcctSeqVersionsVersionName | VERSION_NAME | — | — |

### [[xla_ae_headers|XLA_AE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEntryHeaderAccountingBatchId | ACCOUNTING_BATCH_ID | — | ✅ |
| 2 | JournalEntryHeaderAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | JournalEntryHeaderAccountingEntryStatusCode | ACCOUNTING_ENTRY_STATUS_CODE | — | ✅ |
| 4 | JournalEntryHeaderAccountingEntryTypeCode | ACCOUNTING_ENTRY_TYPE_CODE | — | ✅ |
| 5 | JournalEntryHeaderAccrualReversalFlag | ACCRUAL_REVERSAL_FLAG | — | ✅ |
| 6 | JournalEntryHeaderAeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 7 | JournalEntryHeaderAmbContextCode | AMB_CONTEXT_CODE | — | ✅ |
| 8 | JournalEntryHeaderApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 9 | JournalEntryHeaderAttribute1 | ATTRIBUTE1 | — | — |
| 10 | JournalEntryHeaderAttribute10 | ATTRIBUTE10 | — | — |
| 11 | JournalEntryHeaderAttribute11 | ATTRIBUTE11 | — | — |
| 12 | JournalEntryHeaderAttribute12 | ATTRIBUTE12 | — | — |
| 13 | JournalEntryHeaderAttribute13 | ATTRIBUTE13 | — | — |
| 14 | JournalEntryHeaderAttribute14 | ATTRIBUTE14 | — | — |
| 15 | JournalEntryHeaderAttribute15 | ATTRIBUTE15 | — | — |
| 16 | JournalEntryHeaderAttribute2 | ATTRIBUTE2 | — | — |
| 17 | JournalEntryHeaderAttribute3 | ATTRIBUTE3 | — | — |
| 18 | JournalEntryHeaderAttribute4 | ATTRIBUTE4 | — | — |
| 19 | JournalEntryHeaderAttribute5 | ATTRIBUTE5 | — | — |
| 20 | JournalEntryHeaderAttribute6 | ATTRIBUTE6 | — | — |
| 21 | JournalEntryHeaderAttribute7 | ATTRIBUTE7 | — | — |
| 22 | JournalEntryHeaderAttribute8 | ATTRIBUTE8 | — | — |
| 23 | JournalEntryHeaderAttribute9 | ATTRIBUTE9 | — | — |
| 24 | JournalEntryHeaderAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | JournalEntryHeaderBalanceTypeCode | BALANCE_TYPE_CODE | — | ✅ |
| 26 | JournalEntryHeaderBudgetVersionId | BUDGET_VERSION_ID | — | ✅ |
| 27 | JournalEntryHeaderCloseAcctSeqAssignId | CLOSE_ACCT_SEQ_ASSIGN_ID | — | ✅ |
| 28 | JournalEntryHeaderCloseAcctSeqValue | CLOSE_ACCT_SEQ_VALUE | — | ✅ |
| 29 | JournalEntryHeaderCloseAcctSeqVersionId | CLOSE_ACCT_SEQ_VERSION_ID | — | ✅ |
| 30 | JournalEntryHeaderCompletedDate | COMPLETED_DATE | — | ✅ |
| 31 | JournalEntryHeaderCompletionAcctSeqAssignId | COMPLETION_ACCT_SEQ_ASSIGN_ID | — | ✅ |
| 32 | JournalEntryHeaderCompletionAcctSeqValue | COMPLETION_ACCT_SEQ_VALUE | — | ✅ |
| 33 | JournalEntryHeaderCompletionAcctSeqVersionId | COMPLETION_ACCT_SEQ_VERSION_ID | — | ✅ |
| 34 | JournalEntryHeaderCreatedBy | CREATED_BY | — | ✅ |
| 35 | JournalEntryHeaderCreationDate | CREATION_DATE | — | ✅ |
| 36 | JournalEntryHeaderDescription | DESCRIPTION | — | ✅ |
| 37 | JournalEntryHeaderDocCategoryCode | DOC_CATEGORY_CODE | — | ✅ |
| 38 | JournalEntryHeaderDocSequenceAssignId | DOC_SEQUENCE_ASSIGN_ID | — | ✅ |
| 39 | JournalEntryHeaderDocSequenceId | DOC_SEQUENCE_ID | — | ✅ |
| 40 | JournalEntryHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 41 | JournalEntryHeaderDocSequenceVersionId | DOC_SEQUENCE_VERSION_ID | — | ✅ |
| 42 | JournalEntryHeaderEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 43 | JournalEntryHeaderEntityId | ENTITY_ID | — | ✅ |
| 44 | JournalEntryHeaderEventId | EVENT_ID | — | ✅ |
| 45 | JournalEntryHeaderEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 46 | JournalEntryHeaderFundsStatusCode | FUNDS_STATUS_CODE | — | ✅ |
| 47 | JournalEntryHeaderGlTransferDate | GL_TRANSFER_DATE | — | ✅ |
| 48 | JournalEntryHeaderGlTransferStatusCode | GL_TRANSFER_STATUS_CODE | — | ✅ |
| 49 | JournalEntryHeaderGroupId | GROUP_ID | — | ✅ |
| 50 | JournalEntryHeaderJeCategoryName | JE_CATEGORY_NAME | — | ✅ |
| 51 | JournalEntryHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | JournalEntryHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | JournalEntryHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | JournalEntryHeaderLedgerId | LEDGER_ID | — | ✅ |
| 55 | JournalEntryHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 56 | JournalEntryHeaderMergeEventId | MERGE_EVENT_ID | — | ✅ |
| 57 | JournalEntryHeaderMultiPeriodFlag | MULTIPERIOD_FLAG | — | ✅ |
| 58 | JournalEntryHeaderNeedBalFlag | NEED_BAL_CODE | — | ✅ |
| 59 | JournalEntryHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 60 | JournalEntryHeaderPacketId | PACKET_ID | — | ✅ |
| 61 | JournalEntryHeaderParentAeHeaderId | PARENT_AE_HEADER_ID | — | ✅ |
| 62 | JournalEntryHeaderParentAeLineNum | PARENT_AE_LINE_NUM | — | ✅ |
| 63 | JournalEntryHeaderPeriodName | PERIOD_NAME | — | ✅ |
| 64 | JournalEntryHeaderProductRuleCode | PRODUCT_RULE_CODE | — | ✅ |
| 65 | JournalEntryHeaderProductRuleTypeCode | PRODUCT_RULE_TYPE_CODE | — | ✅ |
| 66 | JournalEntryHeaderProductRuleVersion | PRODUCT_RULE_VERSION | — | ✅ |
| 67 | JournalEntryHeaderReferenceDate | REFERENCE_DATE | — | ✅ |
| 68 | JournalEntryHeaderRequestId | REQUEST_ID | — | ✅ |
| 69 | JournalEntryHeaderUpgBatchId | UPG_BATCH_ID | — | ✅ |
| 70 | JournalEntryHeaderUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | ✅ |
| 71 | JournalEntryHeaderUpgValidFlag | UPG_VALID_FLAG | — | ✅ |
| 72 | JournalEntryHeaderZeroAmountFlag | ZERO_AMOUNT_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
