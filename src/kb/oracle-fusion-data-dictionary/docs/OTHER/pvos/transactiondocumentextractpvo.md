---
id: DOC-OTHER-PVO-TransactionDocumentExtractPVO
doc_type: system-doc
title: "TransactionDocumentExtractPVO — PVO Cross-Module"
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
  - TransactionDocumentExtractPVO
  - transactiondocumentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDocumentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Document Extract. Acessa as tabelas: PJF_TXN_DOCUMENT_B, PJF_TXN_DOCUMENT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionDocumentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 1 | 42 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_document_b|PJF_TXN_DOCUMENT_B]] — 47 atributos (1 PKs, 31 BICC)
- [[pjf_txn_document_tl|PJF_TXN_DOCUMENT_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_document_b|PJF_TXN_DOCUMENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentBasePEOAcctDuringImport | ACCT_DURING_IMPORT | — | ✅ |
| 2 | TransactionDocumentBasePEOAcctSourceCode | ACCT_SOURCE_CODE | — | ✅ |
| 3 | TransactionDocumentBasePEOAdjustAccJournalFlag | ADJUST_ACC_JOURNAL_FLAG | — | ✅ |
| 4 | TransactionDocumentBasePEOAllowBurdenFlag | ALLOW_BURDEN_FLAG | — | ✅ |
| 5 | TransactionDocumentBasePEOAllowDuplicateRefFlag | ALLOW_DUPLICATE_REF_FLAG | — | ✅ |
| 6 | TransactionDocumentBasePEOAllowEmpOrgOverrideFlag | ALLOW_EMP_ORG_OVERRIDE_FLAG | — | ✅ |
| 7 | TransactionDocumentBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 8 | TransactionDocumentBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 9 | TransactionDocumentBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 10 | TransactionDocumentBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 11 | TransactionDocumentBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 12 | TransactionDocumentBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 13 | TransactionDocumentBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 14 | TransactionDocumentBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | TransactionDocumentBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | TransactionDocumentBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | TransactionDocumentBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | TransactionDocumentBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | TransactionDocumentBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | TransactionDocumentBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | TransactionDocumentBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | TransactionDocumentBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | TransactionDocumentBasePEOCommitmentFlag | COMMITMENT_FLAG | — | ✅ |
| 24 | TransactionDocumentBasePEOCommitmentType | COMMITMENT_TYPE | — | ✅ |
| 25 | TransactionDocumentBasePEOCostAccJournalFlag | COST_ACC_JOURNAL_FLAG | — | ✅ |
| 26 | TransactionDocumentBasePEOCostedFlag | COSTED_FLAG | — | ✅ |
| 27 | TransactionDocumentBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 28 | TransactionDocumentBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 29 | TransactionDocumentBasePEODocumentCode | DOCUMENT_CODE | — | ✅ |
| 30 | TransactionDocumentBasePEODocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 31 | TransactionDocumentBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 32 | TransactionDocumentBasePEOExpBatchApprovalFlag | EXP_BATCH_APPROVAL_FLAG | — | ✅ |
| 33 | TransactionDocumentBasePEOImportCostAccFlag | IMPORT_COST_ACC_FLAG | — | ✅ |
| 34 | TransactionDocumentBasePEOImportInClosedPeriodFlag | IMPORT_IN_CLOSED_PERIOD_FLAG | — | ✅ |
| 35 | TransactionDocumentBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | TransactionDocumentBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | TransactionDocumentBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | TransactionDocumentBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | TransactionDocumentBasePEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 40 | TransactionDocumentBasePEOProcessFundsCheck | PROCESS_FUNDS_CHECK | — | ✅ |
| 41 | TransactionDocumentBasePEOPurgeableFlag | PURGEABLE_FLAG | — | ✅ |
| 42 | TransactionDocumentBasePEORevalidateFlag | REVALIDATE_FLAG | — | ✅ |
| 43 | TransactionDocumentBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 44 | TransactionDocumentBasePEOSkipTxnControls | SKIP_TXN_CONTROLS | — | ✅ |
| 45 | TransactionDocumentBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 46 | TransactionDocumentBasePEOTiebackToSource | TIEBACK_TO_SOURCE | — | ✅ |
| 47 | TransactionDocumentBasePEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |

### [[pjf_txn_document_tl|PJF_TXN_DOCUMENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionDocumentTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionDocumentTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionDocumentTLPEODocumentId | DOCUMENT_ID | — | ✅ |
| 5 | TransactionDocumentTLPEODocumentName | DOCUMENT_NAME | — | ✅ |
| 6 | TransactionDocumentTLPEOLanguage | LANGUAGE | — | ✅ |
| 7 | TransactionDocumentTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TransactionDocumentTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | TransactionDocumentTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | TransactionDocumentTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TransactionDocumentTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
