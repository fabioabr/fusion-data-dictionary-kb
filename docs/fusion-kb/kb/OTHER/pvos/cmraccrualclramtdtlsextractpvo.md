---
id: DOC-OTHER-PVO-CmrAccrualClrAmtDtlsExtractPVO
doc_type: system-doc
title: "CmrAccrualClrAmtDtlsExtractPVO — PVO Cross-Module"
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
  - CmrAccrualClrAmtDtlsExtractPVO
  - cmraccrualclramtdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrAccrualClrAmtDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Accrual Clr Amt Dtls Extract. Acessa as tabelas: CMR_ACCRUAL_CLR_AMT_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrAccrualClrAmtDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_accrual_clr_amt_dtls|CMR_ACCRUAL_CLR_AMT_DTLS]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[cmr_accrual_clr_amt_dtls|CMR_ACCRUAL_CLR_AMT_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAccrualClrAmtDtlsPEOAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | CmrAccrualClrAmtDtlsPEOAccrualClrDtlId | ACCRUAL_CLR_DTL_ID | 🔑 | ✅ |
| 3 | CmrAccrualClrAmtDtlsPEOAccrualClrId | ACCRUAL_CLR_ID | — | ✅ |
| 4 | CmrAccrualClrAmtDtlsPEOAccrualClrMode | ACCRUAL_CLR_MODE | — | ✅ |
| 5 | CmrAccrualClrAmtDtlsPEOCmrAccrualClrId | CMR_ACCRUAL_CLR_ID | — | ✅ |
| 6 | CmrAccrualClrAmtDtlsPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | — | ✅ |
| 7 | CmrAccrualClrAmtDtlsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 8 | CmrAccrualClrAmtDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CmrAccrualClrAmtDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CmrAccrualClrAmtDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | CmrAccrualClrAmtDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 12 | CmrAccrualClrAmtDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 13 | CmrAccrualClrAmtDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 14 | CmrAccrualClrAmtDtlsPEOEventDistributionType | EVENT_DISTRIBUTION_TYPE | — | ✅ |
| 15 | CmrAccrualClrAmtDtlsPEOEventTransactionNumber | EVENT_TRANSACTION_NUMBER | — | ✅ |
| 16 | CmrAccrualClrAmtDtlsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 17 | CmrAccrualClrAmtDtlsPEOInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 18 | CmrAccrualClrAmtDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CmrAccrualClrAmtDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CmrAccrualClrAmtDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CmrAccrualClrAmtDtlsPEOSlaAeHeaderId | SLA_AE_HEADER_ID | — | ✅ |
| 22 | CmrAccrualClrAmtDtlsPEOSlaAeLineNum | SLA_AE_LINE_NUM | — | ✅ |
| 23 | CmrAccrualClrAmtDtlsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 24 | CmrAccrualClrAmtDtlsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 25 | CmrAccrualClrAmtDtlsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 26 | CmrAccrualClrAmtDtlsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 27 | CmrAccrualClrAmtDtlsPEOTxnAccountedAmt | TXN_ACCOUNTED_AMT | — | ✅ |
| 28 | CmrAccrualClrAmtDtlsPEOTxnEnteredAmt | TXN_ENTERED_AMT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
