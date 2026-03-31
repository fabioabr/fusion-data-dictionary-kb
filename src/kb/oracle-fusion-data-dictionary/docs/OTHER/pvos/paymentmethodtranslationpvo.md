---
id: DOC-OTHER-PVO-PaymentMethodTranslationPVO
doc_type: system-doc
title: "PaymentMethodTranslationPVO — PVO Cross-Module"
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
  - PaymentMethodTranslationPVO
  - paymentmethodtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentMethodTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Method Translation. Acessa as tabelas: IBY_PAYMENT_METHODS_B, IBY_PAYMENT_METHODS_TL.

**Caminho:** `FscmTopModelAM.FinPmtFDPmtMethodAM.PaymentMethodTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 2 | 2 | 10 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[iby_payment_methods_b|IBY_PAYMENT_METHODS_B]] — 29 atributos (1 BICC)
- [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[iby_payment_methods_b|IBY_PAYMENT_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentMthdTLAnticipatedFloat | ANTICIPATED_FLOAT | — | — |
| 2 | PaymentMthdTLBankChargeBearerAplFlag | BANK_CHARGE_BEARER_APL_FLAG | — | — |
| 3 | PaymentMthdTLCreatedBy | CREATED_BY | — | — |
| 4 | PaymentMthdTLCreationDate | CREATION_DATE | — | — |
| 5 | PaymentMthdTLDeliveryChannelAplFlag | DELIVERY_CHANNEL_APL_FLAG | — | — |
| 6 | PaymentMthdTLDocumentCategoryCode | DOCUMENT_CATEGORY_CODE | — | — |
| 7 | PaymentMthdTLEndDate | END_DATE | — | — |
| 8 | PaymentMthdTLExclusivePmtAplFlag | EXCLUSIVE_PMT_APL_FLAG | — | — |
| 9 | PaymentMthdTLExternalBankAcctAplFlag | EXTERNAL_BANK_ACCT_APL_FLAG | — | — |
| 10 | PaymentMthdTLFormatValue | FORMAT_VALUE | — | — |
| 11 | PaymentMthdTLInactiveDate | INACTIVE_DATE | — | — |
| 12 | PaymentMthdTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PaymentMthdTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PaymentMthdTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PaymentMthdTLMaturityDateOffsetDays | MATURITY_DATE_OFFSET_DAYS | — | — |
| 16 | PaymentMthdTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PaymentMthdTLPaymentFormatAplFlag | PAYMENT_FORMAT_APL_FLAG | — | — |
| 18 | PaymentMthdTLPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 19 | PaymentMthdTLPaymentReasonAplFlag | PAYMENT_REASON_APL_FLAG | — | — |
| 20 | PaymentMthdTLPaymentReasonComntAplFlag | PAYMENT_REASON_COMNT_APL_FLAG | — | — |
| 21 | PaymentMthdTLRemittanceMessage1AplFlag | REMITTANCE_MESSAGE1_APL_FLAG | — | — |
| 22 | PaymentMthdTLRemittanceMessage2AplFlag | REMITTANCE_MESSAGE2_APL_FLAG | — | — |
| 23 | PaymentMthdTLRemittanceMessage3AplFlag | REMITTANCE_MESSAGE3_APL_FLAG | — | — |
| 24 | PaymentMthdTLSeededFlag | SEEDED_FLAG | — | — |
| 25 | PaymentMthdTLSettlementPriorityAplFlag | SETTLEMENT_PRIORITY_APL_FLAG | — | — |
| 26 | PaymentMthdTLStartDate | START_DATE | — | — |
| 27 | PaymentMthdTLSupportBillsPayableFlag | SUPPORT_BILLS_PAYABLE_FLAG | — | — |
| 28 | PaymentMthdTLUniqueRemittanceIdAplFlag | UNIQUE_REMITTANCE_ID_APL_FLAG | — | — |
| 29 | PaymentMthdTLUriCheckDigitAplFlag | URI_CHECK_DIGIT_APL_FLAG | — | — |

### [[iby_payment_methods_tl|IBY_PAYMENT_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | PaymentMethodCode | PAYMENT_METHOD_CODE | 🔑 | ✅ |
| 3 | PaymentMthdBaseCreatedBy | CREATED_BY | — | ✅ |
| 4 | PaymentMthdBaseCreationDate | CREATION_DATE | — | ✅ |
| 5 | PaymentMthdBaseDescription | DESCRIPTION | — | ✅ |
| 6 | PaymentMthdBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PaymentMthdBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PaymentMthdBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PaymentMthdBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PaymentMthdBasePaymentMethodName | PAYMENT_METHOD_NAME | — | ✅ |
| 11 | PaymentMthdBaseSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
