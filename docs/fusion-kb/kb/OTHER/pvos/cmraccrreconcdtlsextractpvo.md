---
id: DOC-OTHER-PVO-CmrAccrReconcDtlsExtractPVO
doc_type: system-doc
title: "CmrAccrReconcDtlsExtractPVO — PVO Cross-Module"
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
  - CmrAccrReconcDtlsExtractPVO
  - cmraccrreconcdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrAccrReconcDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Accr Reconc Dtls Extract. Acessa as tabelas: CMR_ACCR_RECONC_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrAccrReconcDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_accr_reconc_dtls|CMR_ACCR_RECONC_DTLS]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[cmr_accr_reconc_dtls|CMR_ACCR_RECONC_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAccrReconcDtlsPEOAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | CmrAccrReconcDtlsPEOAccrualClrId | ACCRUAL_CLR_ID | — | ✅ |
| 3 | CmrAccrReconcDtlsPEOCmrAccrReconcDtlId | CMR_ACCR_RECONC_DTL_ID | 🔑 | ✅ |
| 4 | CmrAccrReconcDtlsPEOCmrAccrReconcHeaderId | CMR_ACCR_RECONC_HEADER_ID | — | ✅ |
| 5 | CmrAccrReconcDtlsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 6 | CmrAccrReconcDtlsPEOCmrSubLedgerId | CMR_SUB_LEDGER_ID | — | ✅ |
| 7 | CmrAccrReconcDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CmrAccrReconcDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CmrAccrReconcDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CmrAccrReconcDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 11 | CmrAccrReconcDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 12 | CmrAccrReconcDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 13 | CmrAccrReconcDtlsPEOEventAccountedAmt | EVENT_ACCOUNTED_AMT | — | ✅ |
| 14 | CmrAccrReconcDtlsPEOEventCostId | EVENT_COST_ID | — | ✅ |
| 15 | CmrAccrReconcDtlsPEOEventDistributionType | EVENT_DISTRIBUTION_TYPE | — | ✅ |
| 16 | CmrAccrReconcDtlsPEOEventEnteredAmt | EVENT_ENTERED_AMT | — | ✅ |
| 17 | CmrAccrReconcDtlsPEOEventQty | EVENT_QTY | — | ✅ |
| 18 | CmrAccrReconcDtlsPEOEventTransactionDate | EVENT_TRANSACTION_DATE | — | ✅ |
| 19 | CmrAccrReconcDtlsPEOEventTransactionNumber | EVENT_TRANSACTION_NUMBER | — | ✅ |
| 20 | CmrAccrReconcDtlsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 21 | CmrAccrReconcDtlsPEOEventUomCode | EVENT_UOM_CODE | — | ✅ |
| 22 | CmrAccrReconcDtlsPEOInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 23 | CmrAccrReconcDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | CmrAccrReconcDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | CmrAccrReconcDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | CmrAccrReconcDtlsPEOSlaAeHeaderId | SLA_AE_HEADER_ID | — | ✅ |
| 27 | CmrAccrReconcDtlsPEOSlaAeLineNum | SLA_AE_LINE_NUM | — | ✅ |
| 28 | CmrAccrReconcDtlsPEOSlaEventId | SLA_EVENT_ID | — | ✅ |
| 29 | CmrAccrReconcDtlsPEOTradeEventId | TRADE_EVENT_ID | — | ✅ |
| 30 | CmrAccrReconcDtlsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
