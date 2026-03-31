---
id: DOC-OTHER-PVO-TransactionBatchExtractPVO
doc_type: system-doc
title: "TransactionBatchExtractPVO — PVO Cross-Module"
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
  - TransactionBatchExtractPVO
  - transactionbatchextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionBatchExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Batch Extract. Acessa as tabelas: RA_BATCHES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransactionBatchExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 1 | 1 | 33 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[ra_batches_all|RA_BATCHES_ALL]] — 49 atributos (1 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[ra_batches_all|RA_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaBatchAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RaBatchAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RaBatchAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RaBatchAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RaBatchAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RaBatchAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RaBatchAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RaBatchAttribute2 | ATTRIBUTE2 | — | — |
| 9 | RaBatchAttribute3 | ATTRIBUTE3 | — | — |
| 10 | RaBatchAttribute4 | ATTRIBUTE4 | — | — |
| 11 | RaBatchAttribute5 | ATTRIBUTE5 | — | — |
| 12 | RaBatchAttribute6 | ATTRIBUTE6 | — | — |
| 13 | RaBatchAttribute7 | ATTRIBUTE7 | — | — |
| 14 | RaBatchAttribute8 | ATTRIBUTE8 | — | — |
| 15 | RaBatchAttribute9 | ATTRIBUTE9 | — | — |
| 16 | RaBatchAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | RaBatchBatchDate | BATCH_DATE | — | ✅ |
| 18 | RaBatchBatchId | BATCH_ID | 🔑 | ✅ |
| 19 | RaBatchBatchProcessStatus | BATCH_PROCESS_STATUS | — | ✅ |
| 20 | RaBatchBatchSourceId | BATCH_SOURCE_ID | — | ✅ |
| 21 | RaBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | ✅ |
| 22 | RaBatchComments | COMMENTS | — | ✅ |
| 23 | RaBatchControlAmount | CONTROL_AMOUNT | — | ✅ |
| 24 | RaBatchControlCount | CONTROL_COUNT | — | ✅ |
| 25 | RaBatchCreatedBy | CREATED_BY | — | ✅ |
| 26 | RaBatchCreationDate | CREATION_DATE | — | ✅ |
| 27 | RaBatchCurrencyCode | CURRENCY_CODE | — | ✅ |
| 28 | RaBatchExchangeDate | EXCHANGE_DATE | — | ✅ |
| 29 | RaBatchExchangeRate | EXCHANGE_RATE | — | ✅ |
| 30 | RaBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 31 | RaBatchGlDate | GL_DATE | — | ✅ |
| 32 | RaBatchIssueDate | ISSUE_DATE | — | ✅ |
| 33 | RaBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | RaBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | RaBatchLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | RaBatchMaturityDate | MATURITY_DATE | — | ✅ |
| 37 | RaBatchName | NAME | — | ✅ |
| 38 | RaBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | RaBatchOrgId | ORG_ID | — | ✅ |
| 40 | RaBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 41 | RaBatchProgramId | PROGRAM_ID | — | ✅ |
| 42 | RaBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 43 | RaBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | ✅ |
| 44 | RaBatchRequestId | REQUEST_ID | — | ✅ |
| 45 | RaBatchSelectionCriteriaId | SELECTION_CRITERIA_ID | — | ✅ |
| 46 | RaBatchSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 47 | RaBatchSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 48 | RaBatchStatus | STATUS | — | ✅ |
| 49 | RaBatchType | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
