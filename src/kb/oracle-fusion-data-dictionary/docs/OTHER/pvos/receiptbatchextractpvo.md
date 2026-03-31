---
id: DOC-OTHER-PVO-ReceiptBatchExtractPVO
doc_type: system-doc
title: "ReceiptBatchExtractPVO — PVO Cross-Module"
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
  - ReceiptBatchExtractPVO
  - receiptbatchextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptBatchExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receipt Batch Extract. Acessa as tabelas: AR_BATCHES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceiptBatchExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 1 | 50 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 66 atributos (1 PKs, 50 BICC)

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArBatchActualAmount | ACTUAL_AMOUNT | — | ✅ |
| 2 | ArBatchActualCount | ACTUAL_COUNT | — | ✅ |
| 3 | ArBatchAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ArBatchAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ArBatchAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ArBatchAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ArBatchAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ArBatchAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ArBatchAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ArBatchAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ArBatchAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ArBatchAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ArBatchAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ArBatchAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ArBatchAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ArBatchAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ArBatchAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ArBatchAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ArBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | ✅ |
| 20 | ArBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | ✅ |
| 21 | ArBatchAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | ✅ |
| 22 | ArBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | ✅ |
| 23 | ArBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | ✅ |
| 24 | ArBatchBatchDate | BATCH_DATE | — | ✅ |
| 25 | ArBatchBatchId | BATCH_ID | 🔑 | ✅ |
| 26 | ArBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | ✅ |
| 27 | ArBatchClosedDate | CLOSED_DATE | — | ✅ |
| 28 | ArBatchComments | COMMENTS | — | ✅ |
| 29 | ArBatchControlAmount | CONTROL_AMOUNT | — | ✅ |
| 30 | ArBatchControlCount | CONTROL_COUNT | — | ✅ |
| 31 | ArBatchCreatedBy | CREATED_BY | — | ✅ |
| 32 | ArBatchCreationDate | CREATION_DATE | — | ✅ |
| 33 | ArBatchCurrencyCode | CURRENCY_CODE | — | ✅ |
| 34 | ArBatchDepositDate | DEPOSIT_DATE | — | ✅ |
| 35 | ArBatchExchangeDate | EXCHANGE_DATE | — | ✅ |
| 36 | ArBatchExchangeRate | EXCHANGE_RATE | — | ✅ |
| 37 | ArBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 38 | ArBatchGlDate | GL_DATE | — | ✅ |
| 39 | ArBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ArBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 41 | ArBatchLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | ArBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | ✅ |
| 43 | ArBatchLockboxId | LOCKBOX_ID | — | ✅ |
| 44 | ArBatchMediaReference | MEDIA_REFERENCE | — | ✅ |
| 45 | ArBatchName | NAME | — | ✅ |
| 46 | ArBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | ArBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | ✅ |
| 48 | ArBatchOperationRequestId | OPERATION_REQUEST_ID | — | ✅ |
| 49 | ArBatchOrgId | ORG_ID | — | ✅ |
| 50 | ArBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 51 | ArBatchProgramId | PROGRAM_ID | — | ✅ |
| 52 | ArBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 53 | ArBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | ✅ |
| 54 | ArBatchReceiptClassId | RECEIPT_CLASS_ID | — | ✅ |
| 55 | ArBatchReceiptMethodId | RECEIPT_METHOD_ID | — | ✅ |
| 56 | ArBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | ✅ |
| 57 | ArBatchRemitMethodCode | REMIT_METHOD_CODE | — | ✅ |
| 58 | ArBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | ✅ |
| 59 | ArBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | ✅ |
| 60 | ArBatchRequestId | REQUEST_ID | — | ✅ |
| 61 | ArBatchSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 62 | ArBatchStatus | STATUS | — | ✅ |
| 63 | ArBatchTransmissionId | TRANSMISSION_ID | — | ✅ |
| 64 | ArBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | ✅ |
| 65 | ArBatchType | TYPE | — | ✅ |
| 66 | ArBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
