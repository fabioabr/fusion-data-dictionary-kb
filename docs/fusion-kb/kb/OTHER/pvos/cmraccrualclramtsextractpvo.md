---
id: DOC-OTHER-PVO-CmrAccrualClrAmtsExtractPVO
doc_type: system-doc
title: "CmrAccrualClrAmtsExtractPVO — PVO Cross-Module"
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
  - CmrAccrualClrAmtsExtractPVO
  - cmraccrualclramtsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrAccrualClrAmtsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Accrual Clr Amts Extract. Acessa as tabelas: CMR_ACCRUAL_CLR_AMTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrAccrualClrAmtsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_accrual_clr_amts|CMR_ACCRUAL_CLR_AMTS]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[cmr_accrual_clr_amts|CMR_ACCRUAL_CLR_AMTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAccrualClrAmtsPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | ✅ |
| 2 | CmrAccrualClrAmtsPEOAccrualClrAmt | ACCRUAL_CLR_AMT | — | ✅ |
| 3 | CmrAccrualClrAmtsPEOAccrualClrGroupId | ACCRUAL_CLR_GROUP_ID | — | ✅ |
| 4 | CmrAccrualClrAmtsPEOAccrualClrId | ACCRUAL_CLR_ID | 🔑 | ✅ |
| 5 | CmrAccrualClrAmtsPEOAccrualClrMode | ACCRUAL_CLR_MODE | — | ✅ |
| 6 | CmrAccrualClrAmtsPEOAccrualClrReasonDesc | ACCRUAL_CLR_REASON_DESC | — | ✅ |
| 7 | CmrAccrualClrAmtsPEOAccrualClrRuleName | ACCRUAL_CLR_RULE_NAME | — | ✅ |
| 8 | CmrAccrualClrAmtsPEOAccrualProcessedFlag | ACCRUAL_PROCESSED_FLAG | — | ✅ |
| 9 | CmrAccrualClrAmtsPEOApAccrualAmt | AP_ACCRUAL_AMT | — | ✅ |
| 10 | CmrAccrualClrAmtsPEOApAccrualAmtAccrual | AP_ACCRUAL_AMT_ACCRUAL | — | ✅ |
| 11 | CmrAccrualClrAmtsPEOApAccrualAmtNonrectax | AP_ACCRUAL_AMT_NONRECTAX | — | ✅ |
| 12 | CmrAccrualClrAmtsPEOApAccrualAmtRectax | AP_ACCRUAL_AMT_RECTAX | — | ✅ |
| 13 | CmrAccrualClrAmtsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 14 | CmrAccrualClrAmtsPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 15 | CmrAccrualClrAmtsPEOCmrAccrualAmt | CMR_ACCRUAL_AMT | — | ✅ |
| 16 | CmrAccrualClrAmtsPEOCmrAccrualAmtAccrual | CMR_ACCRUAL_AMT_ACCRUAL | — | ✅ |
| 17 | CmrAccrualClrAmtsPEOCmrAccrualAmtNonrectax | CMR_ACCRUAL_AMT_NONRECTAX | — | ✅ |
| 18 | CmrAccrualClrAmtsPEOCmrAccrualAmtRectax | CMR_ACCRUAL_AMT_RECTAX | — | ✅ |
| 19 | CmrAccrualClrAmtsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 20 | CmrAccrualClrAmtsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 21 | CmrAccrualClrAmtsPEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | CmrAccrualClrAmtsPEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | CmrAccrualClrAmtsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 24 | CmrAccrualClrAmtsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 25 | CmrAccrualClrAmtsPEODeliveryProcessedFlag | DELIVERY_PROCESSED_FLAG | — | ✅ |
| 26 | CmrAccrualClrAmtsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 27 | CmrAccrualClrAmtsPEOEnteredAmount | ENTERED_AMOUNT | — | ✅ |
| 28 | CmrAccrualClrAmtsPEOEnteredApAccrualAmt | ENTERED_AP_ACCRUAL_AMT | — | ✅ |
| 29 | CmrAccrualClrAmtsPEOEnteredApNonrectaxAmt | ENTERED_AP_NONRECTAX_AMT | — | ✅ |
| 30 | CmrAccrualClrAmtsPEOEnteredCmrAccrualAmt | ENTERED_CMR_ACCRUAL_AMT | — | ✅ |
| 31 | CmrAccrualClrAmtsPEOEnteredCmrNonrectaxAmt | ENTERED_CMR_NONRECTAX_AMT | — | ✅ |
| 32 | CmrAccrualClrAmtsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 33 | CmrAccrualClrAmtsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 34 | CmrAccrualClrAmtsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 35 | CmrAccrualClrAmtsPEOInvoiceQty | INVOICE_QTY | — | ✅ |
| 36 | CmrAccrualClrAmtsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | CmrAccrualClrAmtsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | CmrAccrualClrAmtsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | CmrAccrualClrAmtsPEOLatestAccountingEventId | LATEST_ACCOUNTING_EVENT_ID | — | ✅ |
| 40 | CmrAccrualClrAmtsPEOLatestCmrApInvoiceDistId | LATEST_CMR_AP_INVOICE_DIST_ID | — | ✅ |
| 41 | CmrAccrualClrAmtsPEOLatestTxnDate | LATEST_TXN_DATE | — | ✅ |
| 42 | CmrAccrualClrAmtsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 43 | CmrAccrualClrAmtsPEOReceivedQty | RECEIVED_QTY | — | ✅ |
| 44 | CmrAccrualClrAmtsPEOReversalAccrualClrId | REVERSAL_ACCRUAL_CLR_ID | — | ✅ |
| 45 | CmrAccrualClrAmtsPEOSoldToBusinessUnitId | SOLD_TO_BUSINESS_UNIT_ID | — | ✅ |
| 46 | CmrAccrualClrAmtsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
