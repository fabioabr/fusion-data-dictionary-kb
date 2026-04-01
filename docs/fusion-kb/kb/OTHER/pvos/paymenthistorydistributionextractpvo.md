---
id: DOC-OTHER-PVO-PaymentHistoryDistributionExtractPVO
doc_type: system-doc
title: "PaymentHistoryDistributionExtractPVO — PVO Cross-Module"
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
  - PaymentHistoryDistributionExtractPVO
  - paymenthistorydistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentHistoryDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment History Distribution Extract. Acessa as tabelas: AP_PAYMENT_HIST_DISTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.PaymentHistoryDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_payment_hist_dists|AP_PAYMENT_HIST_DISTS]] — 36 atributos (1 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[ap_payment_hist_dists|AP_PAYMENT_HIST_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApPaymentHistDistsAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | ApPaymentHistDistsAmount | AMOUNT | — | ✅ |
| 3 | ApPaymentHistDistsAmountVariance | AMOUNT_VARIANCE | — | ✅ |
| 4 | ApPaymentHistDistsAwtRelatedId | AWT_RELATED_ID | — | ✅ |
| 5 | ApPaymentHistDistsBankCurrAmount | BANK_CURR_AMOUNT | — | ✅ |
| 6 | ApPaymentHistDistsClearedBaseAmount | CLEARED_BASE_AMOUNT | — | ✅ |
| 7 | ApPaymentHistDistsCreatedBy | CREATED_BY | — | ✅ |
| 8 | ApPaymentHistDistsCreationDate | CREATION_DATE | — | ✅ |
| 9 | ApPaymentHistDistsHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 10 | ApPaymentHistDistsInvoiceAdjustmentEventId | INVOICE_ADJUSTMENT_EVENT_ID | — | ✅ |
| 11 | ApPaymentHistDistsInvoiceBaseAmtVariance | INVOICE_BASE_AMT_VARIANCE | — | ✅ |
| 12 | ApPaymentHistDistsInvoiceBaseQtyVariance | INVOICE_BASE_QTY_VARIANCE | — | ✅ |
| 13 | ApPaymentHistDistsInvoiceDistAmount | INVOICE_DIST_AMOUNT | — | ✅ |
| 14 | ApPaymentHistDistsInvoiceDistBaseAmount | INVOICE_DIST_BASE_AMOUNT | — | ✅ |
| 15 | ApPaymentHistDistsInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 16 | ApPaymentHistDistsInvoicePaymentId | INVOICE_PAYMENT_ID | — | ✅ |
| 17 | ApPaymentHistDistsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | ApPaymentHistDistsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | ApPaymentHistDistsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | ApPaymentHistDistsMaturedBaseAmount | MATURED_BASE_AMOUNT | — | ✅ |
| 21 | ApPaymentHistDistsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | ApPaymentHistDistsPaAdditionFlag | PA_ADDITION_FLAG | — | ✅ |
| 23 | ApPaymentHistDistsPaidBaseAmount | PAID_BASE_AMOUNT | — | ✅ |
| 24 | ApPaymentHistDistsPayDistLookupCode | PAY_DIST_LOOKUP_CODE | — | ✅ |
| 25 | ApPaymentHistDistsPaymentHistDistId | PAYMENT_HIST_DIST_ID | 🔑 | ✅ |
| 26 | ApPaymentHistDistsPaymentHistoryId | PAYMENT_HISTORY_ID | — | ✅ |
| 27 | ApPaymentHistDistsProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 28 | ApPaymentHistDistsProgramId | PROGRAM_ID | — | ✅ |
| 29 | ApPaymentHistDistsProgramLoginId | PROGRAM_LOGIN_ID | — | ✅ |
| 30 | ApPaymentHistDistsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 31 | ApPaymentHistDistsQuantityVariance | QUANTITY_VARIANCE | — | ✅ |
| 32 | ApPaymentHistDistsReleaseInvDistDerivedFrom | RELEASE_INV_DIST_DERIVED_FROM | — | ✅ |
| 33 | ApPaymentHistDistsRequestId | REQUEST_ID | — | ✅ |
| 34 | ApPaymentHistDistsReversalFlag | REVERSAL_FLAG | — | ✅ |
| 35 | ApPaymentHistDistsReversedPayHistDistId | REVERSED_PAY_HIST_DIST_ID | — | ✅ |
| 36 | ApPaymentHistDistsRoundingAmt | ROUNDING_AMT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
