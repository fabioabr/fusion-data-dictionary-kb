---
id: DOC-OTHER-PVO-TransactionLineRevenueDeferralExtractPVO
doc_type: system-doc
title: "TransactionLineRevenueDeferralExtractPVO — PVO Cross-Module"
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
  - TransactionLineRevenueDeferralExtractPVO
  - transactionlinerevenuedeferralextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionLineRevenueDeferralExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Line Revenue Deferral Extract. Acessa as tabelas: AR_DEFERRED_LINES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransactionLineRevenueDeferralExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 20 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]] — 36 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[ar_deferred_lines_all|AR_DEFERRED_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArDeferredLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | ✅ |
| 2 | ArDeferredLineAcctdAmountPending | ACCTD_AMOUNT_PENDING | — | ✅ |
| 3 | ArDeferredLineAcctdAmountRecognized | ACCTD_AMOUNT_RECOGNIZED | — | ✅ |
| 4 | ArDeferredLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | ✅ |
| 5 | ArDeferredLineAmountPending | AMOUNT_PENDING | — | ✅ |
| 6 | ArDeferredLineAmountRecognized | AMOUNT_RECOGNIZED | — | ✅ |
| 7 | ArDeferredLineAttribute1 | ATTRIBUTE1 | — | — |
| 8 | ArDeferredLineAttribute10 | ATTRIBUTE10 | — | — |
| 9 | ArDeferredLineAttribute11 | ATTRIBUTE11 | — | — |
| 10 | ArDeferredLineAttribute12 | ATTRIBUTE12 | — | — |
| 11 | ArDeferredLineAttribute13 | ATTRIBUTE13 | — | — |
| 12 | ArDeferredLineAttribute14 | ATTRIBUTE14 | — | — |
| 13 | ArDeferredLineAttribute15 | ATTRIBUTE15 | — | — |
| 14 | ArDeferredLineAttribute2 | ATTRIBUTE2 | — | — |
| 15 | ArDeferredLineAttribute3 | ATTRIBUTE3 | — | — |
| 16 | ArDeferredLineAttribute4 | ATTRIBUTE4 | — | — |
| 17 | ArDeferredLineAttribute5 | ATTRIBUTE5 | — | — |
| 18 | ArDeferredLineAttribute6 | ATTRIBUTE6 | — | — |
| 19 | ArDeferredLineAttribute7 | ATTRIBUTE7 | — | — |
| 20 | ArDeferredLineAttribute8 | ATTRIBUTE8 | — | — |
| 21 | ArDeferredLineAttribute9 | ATTRIBUTE9 | — | — |
| 22 | ArDeferredLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | ArDeferredLineCreatedBy | CREATED_BY | — | ✅ |
| 24 | ArDeferredLineCreationDate | CREATION_DATE | — | ✅ |
| 25 | ArDeferredLineCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 26 | ArDeferredLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | 🔑 | ✅ |
| 27 | ArDeferredLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ArDeferredLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | ArDeferredLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ArDeferredLineLineCollectibleFlag | LINE_COLLECTIBLE_FLAG | — | ✅ |
| 31 | ArDeferredLineManualOverrideFlag | MANUAL_OVERRIDE_FLAG | — | ✅ |
| 32 | ArDeferredLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | ArDeferredLineOrgId | ORG_ID | — | ✅ |
| 34 | ArDeferredLineOriginalCollectibilityFlag | ORIGINAL_COLLECTIBILITY_FLAG | — | ✅ |
| 35 | ArDeferredLineParentLineId | PARENT_LINE_ID | — | ✅ |
| 36 | ArDeferredLineRequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
