---
id: DOC-OTHER-PVO-CmrAccrReconcHeadersExtractPVO
doc_type: system-doc
title: "CmrAccrReconcHeadersExtractPVO — PVO Cross-Module"
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
  - CmrAccrReconcHeadersExtractPVO
  - cmraccrreconcheadersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrAccrReconcHeadersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Accr Reconc Headers Extract. Acessa as tabelas: CMR_ACCR_RECONC_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrAccrReconcHeadersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 1 | 1 | 37 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_accr_reconc_headers|CMR_ACCR_RECONC_HEADERS]] — 37 atributos (1 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[cmr_accr_reconc_headers|CMR_ACCR_RECONC_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAccrReconcHeadersPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | CmrAccrReconcHeadersPEOAccrualClrAmt | ACCRUAL_CLR_AMT | — | ✅ |
| 3 | CmrAccrReconcHeadersPEOAccrualClrFlag | ACCRUAL_CLR_FLAG | — | ✅ |
| 4 | CmrAccrReconcHeadersPEOApAccrualAmt | AP_ACCRUAL_AMT | — | ✅ |
| 5 | CmrAccrReconcHeadersPEOApAccrualAmtAccrual | AP_ACCRUAL_AMT_ACCRUAL | — | ✅ |
| 6 | CmrAccrReconcHeadersPEOApAccrualAmtNonrectax | AP_ACCRUAL_AMT_NONRECTAX | — | ✅ |
| 7 | CmrAccrReconcHeadersPEOApAccrualAmtRectax | AP_ACCRUAL_AMT_RECTAX | — | ✅ |
| 8 | CmrAccrReconcHeadersPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 9 | CmrAccrReconcHeadersPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 10 | CmrAccrReconcHeadersPEOCmrAccrReconcHeaderId | CMR_ACCR_RECONC_HEADER_ID | 🔑 | ✅ |
| 11 | CmrAccrReconcHeadersPEOCmrAccrualAmt | CMR_ACCRUAL_AMT | — | ✅ |
| 12 | CmrAccrReconcHeadersPEOCmrAccrualAmtAccrual | CMR_ACCRUAL_AMT_ACCRUAL | — | ✅ |
| 13 | CmrAccrReconcHeadersPEOCmrAccrualAmtNonrectax | CMR_ACCRUAL_AMT_NONRECTAX | — | ✅ |
| 14 | CmrAccrReconcHeadersPEOCmrAccrualAmtRectax | CMR_ACCRUAL_AMT_RECTAX | — | ✅ |
| 15 | CmrAccrReconcHeadersPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 16 | CmrAccrReconcHeadersPEOCreatedBy | CREATED_BY | — | ✅ |
| 17 | CmrAccrReconcHeadersPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | CmrAccrReconcHeadersPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 19 | CmrAccrReconcHeadersPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 20 | CmrAccrReconcHeadersPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 21 | CmrAccrReconcHeadersPEOEnteredApAccrualAmt | ENTERED_AP_ACCRUAL_AMT | — | ✅ |
| 22 | CmrAccrReconcHeadersPEOEnteredApNonrectaxAmt | ENTERED_AP_NONRECTAX_AMT | — | ✅ |
| 23 | CmrAccrReconcHeadersPEOEnteredApRectaxAmt | ENTERED_AP_RECTAX_AMT | — | ✅ |
| 24 | CmrAccrReconcHeadersPEOEnteredCmrAccrualAmt | ENTERED_CMR_ACCRUAL_AMT | — | ✅ |
| 25 | CmrAccrReconcHeadersPEOEnteredCmrNonrectaxAmt | ENTERED_CMR_NONRECTAX_AMT | — | ✅ |
| 26 | CmrAccrReconcHeadersPEOEnteredCmrRectaxAmt | ENTERED_CMR_RECTAX_AMT | — | ✅ |
| 27 | CmrAccrReconcHeadersPEOEventEnteredAmt | EVENT_ENTERED_AMT | — | ✅ |
| 28 | CmrAccrReconcHeadersPEOEventLatestTxnDate | EVENT_LATEST_TXN_DATE | — | ✅ |
| 29 | CmrAccrReconcHeadersPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 30 | CmrAccrReconcHeadersPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 31 | CmrAccrReconcHeadersPEOInvoiceQty | INVOICE_QTY | — | ✅ |
| 32 | CmrAccrReconcHeadersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | CmrAccrReconcHeadersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 34 | CmrAccrReconcHeadersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | CmrAccrReconcHeadersPEOProcessRunId | PROCESS_RUN_ID | — | ✅ |
| 36 | CmrAccrReconcHeadersPEOReceivedQty | RECEIVED_QTY | — | ✅ |
| 37 | CmrAccrReconcHeadersPEOSoldToBusinessUnitId | SOLD_TO_BUSINESS_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
