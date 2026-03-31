---
id: DOC-OTHER-PVO-CashRemitRefExtractPVO
doc_type: system-doc
title: "CashRemitRefExtractPVO — PVO Cross-Module"
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
  - CashRemitRefExtractPVO
  - cashremitrefextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CashRemitRefExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cash Remit Ref Extract. Acessa as tabelas: AR_CASH_REMIT_REFS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.CashRemitRefExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 1 | 35 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_cash_remit_refs_all|AR_CASH_REMIT_REFS_ALL]] — 35 atributos (1 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[ar_cash_remit_refs_all|AR_CASH_REMIT_REFS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmountApplied | AMOUNT_APPLIED | — | ✅ |
| 2 | ArCashRemitRefAmountAppliedFrom | AMOUNT_APPLIED_FROM | — | ✅ |
| 3 | ArCashRemitRefAutoapplyFlag | AUTOAPPLY_FLAG | — | ✅ |
| 4 | ArCashRemitRefAutomatchRuleId | AUTOMATCH_RULE_ID | — | ✅ |
| 5 | ArCashRemitRefBankAccountNumber | BANK_ACCOUNT_NUMBER | — | ✅ |
| 6 | ArCashRemitRefCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 7 | ArCashRemitRefCreatedBy | CREATED_BY | — | ✅ |
| 8 | ArCashRemitRefCreationDate | CREATION_DATE | — | ✅ |
| 9 | ArCashRemitRefCustomerId | CUSTOMER_ID | — | ✅ |
| 10 | ArCashRemitRefCustomerNumber | CUSTOMER_NUMBER | — | ✅ |
| 11 | ArCashRemitRefCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 12 | ArCashRemitRefInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 13 | ArCashRemitRefInvoiceReference | INVOICE_REFERENCE | — | ✅ |
| 14 | ArCashRemitRefInvoiceStatus | INVOICE_STATUS | — | ✅ |
| 15 | ArCashRemitRefLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ArCashRemitRefLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | ArCashRemitRefLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ArCashRemitRefLockboxMatchingOption | LOCKBOX_MATCHING_OPTION | — | ✅ |
| 19 | ArCashRemitRefMatchingDateReference | MATCHING_DATE_REFERENCE | — | ✅ |
| 20 | ArCashRemitRefObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | ArCashRemitRefOrgId | ORG_ID | — | ✅ |
| 22 | ArCashRemitRefPayUnrelatedCustomers | PAY_UNRELATED_CUSTOMERS | — | ✅ |
| 23 | ArCashRemitRefPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | ✅ |
| 24 | ArCashRemitRefProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 25 | ArCashRemitRefProgramId | PROGRAM_ID | — | ✅ |
| 26 | ArCashRemitRefProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 27 | ArCashRemitRefReceiptReferenceStatus | RECEIPT_REFERENCE_STATUS | — | ✅ |
| 28 | ArCashRemitRefReferenceSource | REFERENCE_SOURCE | — | ✅ |
| 29 | ArCashRemitRefRemitReferenceId | REMIT_REFERENCE_ID | 🔑 | ✅ |
| 30 | ArCashRemitRefRequestId | REQUEST_ID | — | ✅ |
| 31 | ArCashRemitRefResolvedMatchInstallment | RESOLVED_MATCH_INSTALLMENT | — | ✅ |
| 32 | ArCashRemitRefResolvedMatchingDate | RESOLVED_MATCHING_DATE | — | ✅ |
| 33 | ArCashRemitRefResolvedMatchingNumber | RESOLVED_MATCHING_NUMBER | — | ✅ |
| 34 | ArCashRemitRefTransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | ✅ |
| 35 | ArCashRemitRefTransitRoutingNumber | TRANSIT_ROUTING_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
