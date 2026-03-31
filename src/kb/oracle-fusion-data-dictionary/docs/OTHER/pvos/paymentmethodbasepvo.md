---
id: DOC-OTHER-PVO-PaymentMethodBasePVO
doc_type: system-doc
title: "PaymentMethodBasePVO — PVO Cross-Module"
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
  - PaymentMethodBasePVO
  - paymentmethodbasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentMethodBasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Method Base. Acessa as tabelas: IBY_PAYMENT_METHODS_B.

**Caminho:** `FscmTopModelAM.FinPmtFDPmtMethodAM.PaymentMethodBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 6 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[iby_payment_methods_b|IBY_PAYMENT_METHODS_B]] — 29 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[iby_payment_methods_b|IBY_PAYMENT_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnticipatedFloat | ANTICIPATED_FLOAT | — | — |
| 2 | BankChargeBearerAplFlag | BANK_CHARGE_BEARER_APL_FLAG | — | — |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DeliveryChannelAplFlag | DELIVERY_CHANNEL_APL_FLAG | — | — |
| 6 | DocumentCategoryCode | DOCUMENT_CATEGORY_CODE | — | — |
| 7 | EndDate | END_DATE | — | — |
| 8 | ExclusivePmtAplFlag | EXCLUSIVE_PMT_APL_FLAG | — | — |
| 9 | ExternalBankAcctAplFlag | EXTERNAL_BANK_ACCT_APL_FLAG | — | — |
| 10 | FormatValue | FORMAT_VALUE | — | — |
| 11 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | MaturityDateOffsetDays | MATURITY_DATE_OFFSET_DAYS | — | — |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PaymentFormatAplFlag | PAYMENT_FORMAT_APL_FLAG | — | — |
| 18 | PaymentMethodCode | PAYMENT_METHOD_CODE | 🔑 | ✅ |
| 19 | PaymentReasonAplFlag | PAYMENT_REASON_APL_FLAG | — | — |
| 20 | PaymentReasonComntAplFlag | PAYMENT_REASON_COMNT_APL_FLAG | — | — |
| 21 | RemittanceMessage1AplFlag | REMITTANCE_MESSAGE1_APL_FLAG | — | — |
| 22 | RemittanceMessage2AplFlag | REMITTANCE_MESSAGE2_APL_FLAG | — | — |
| 23 | RemittanceMessage3AplFlag | REMITTANCE_MESSAGE3_APL_FLAG | — | — |
| 24 | SeededFlag | SEEDED_FLAG | — | — |
| 25 | SettlementPriorityAplFlag | SETTLEMENT_PRIORITY_APL_FLAG | — | — |
| 26 | StartDate | START_DATE | — | — |
| 27 | SupportBillsPayableFlag | SUPPORT_BILLS_PAYABLE_FLAG | — | — |
| 28 | UniqueRemittanceIdAplFlag | UNIQUE_REMITTANCE_ID_APL_FLAG | — | — |
| 29 | UriCheckDigitAplFlag | URI_CHECK_DIGIT_APL_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
