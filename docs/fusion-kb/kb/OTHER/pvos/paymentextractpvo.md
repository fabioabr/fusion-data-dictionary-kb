---
id: DOC-OTHER-PVO-PaymentExtractPVO
doc_type: system-doc
title: "PaymentExtractPVO — PVO Cross-Module"
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
  - PaymentExtractPVO
  - paymentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Extract. Acessa as tabelas: DOO_PAYMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.PaymentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_payments|DOO_PAYMENTS]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[doo_payments|DOO_PAYMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentAmount | AMOUNT | — | ✅ |
| 2 | PaymentAuthorizationStatus | AUTHORIZATION_STATUS | — | ✅ |
| 3 | PaymentAuthorizedInSourceFlag | AUTHORIZED_IN_SOURCE_FLAG | — | ✅ |
| 4 | PaymentAuthorizedOn | AUTHORIZED_ON | — | ✅ |
| 5 | PaymentCreatedBy | CREATED_BY | — | ✅ |
| 6 | PaymentCreationDate | CREATION_DATE | — | ✅ |
| 7 | PaymentDeltaType | DELTA_TYPE | — | ✅ |
| 8 | PaymentFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 9 | PaymentHeaderId | HEADER_ID | — | ✅ |
| 10 | PaymentInstrumentAssignmentId | INSTRUMENT_ASSIGNMENT_ID | — | ✅ |
| 11 | PaymentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PaymentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | PaymentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | PaymentLineId | LINE_ID | — | ✅ |
| 15 | PaymentModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | PaymentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PaymentOrigSysPaymentRef | ORIG_SYS_PAYMENT_REF | — | ✅ |
| 18 | PaymentPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 19 | PaymentPaymentSetId | PAYMENT_SET_ID | — | ✅ |
| 20 | PaymentReceiptMethodId | RECEIPT_METHOD_ID | — | ✅ |
| 21 | PaymentReferencePaymentTrxId | REFERENCE_PAYMENT_TRX_ID | — | ✅ |
| 22 | PaymentTransactionExtensionId | TRANSACTION_EXTENSION_ID | — | ✅ |
| 23 | PaymentTrxId | PAYMENT_TRX_ID | 🔑 | ✅ |
| 24 | PaymentUniquePaymentReference | UNIQUE_PAYMENT_REFERENCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
