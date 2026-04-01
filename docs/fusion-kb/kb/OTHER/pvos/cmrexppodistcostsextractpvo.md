---
id: DOC-OTHER-PVO-CmrExpPoDistCostsExtractPVO
doc_type: system-doc
title: "CmrExpPoDistCostsExtractPVO — PVO Cross-Module"
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
  - CmrExpPoDistCostsExtractPVO
  - cmrexppodistcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrExpPoDistCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Exp Po Dist Costs Extract. Acessa as tabelas: CMR_EXP_PO_DIST_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrExpPoDistCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 1 | 44 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_exp_po_dist_costs|CMR_EXP_PO_DIST_COSTS]] — 44 atributos (1 PKs, 44 BICC)

---

## ⚙️ Atributos

### [[cmr_exp_po_dist_costs|CMR_EXP_PO_DIST_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrExpPoDistCostsPEOApInvoiceDistributionType | AP_INVOICE_DISTRIBUTION_TYPE | — | ✅ |
| 2 | CmrExpPoDistCostsPEOAutoAccrualClrDate | AUTO_ACCRUAL_CLR_DATE | — | ✅ |
| 3 | CmrExpPoDistCostsPEOAutoAccrualClrFlag | AUTO_ACCRUAL_CLR_FLAG | — | ✅ |
| 4 | CmrExpPoDistCostsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 5 | CmrExpPoDistCostsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 6 | CmrExpPoDistCostsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 7 | CmrExpPoDistCostsPEOCmrRootReceiveTxnId | CMR_ROOT_RECEIVE_TXN_ID | — | ✅ |
| 8 | CmrExpPoDistCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CmrExpPoDistCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CmrExpPoDistCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | CmrExpPoDistCostsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 12 | CmrExpPoDistCostsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 13 | CmrExpPoDistCostsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 14 | CmrExpPoDistCostsPEOCurrentRunExpAdjAmt | CURRENT_RUN_EXP_ADJ_AMT | — | ✅ |
| 15 | CmrExpPoDistCostsPEOCurrentRunExpAdjAmtEc | CURRENT_RUN_EXP_ADJ_AMT_EC | — | ✅ |
| 16 | CmrExpPoDistCostsPEOCurrentRunInvoiceAmt | CURRENT_RUN_INVOICE_AMT | — | ✅ |
| 17 | CmrExpPoDistCostsPEODeliverToInventoryOrgId | DELIVER_TO_INVENTORY_ORG_ID | — | ✅ |
| 18 | CmrExpPoDistCostsPEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 19 | CmrExpPoDistCostsPEOExpPoDistCostId | EXP_PO_DIST_COST_ID | 🔑 | ✅ |
| 20 | CmrExpPoDistCostsPEOInclusiveFlag | INCLUSIVE_FLAG | — | ✅ |
| 21 | CmrExpPoDistCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | CmrExpPoDistCostsPEOInvoiceAcctDate | INVOICE_ACCT_DATE | — | ✅ |
| 23 | CmrExpPoDistCostsPEOInvoiceAmt | INVOICE_AMT | — | ✅ |
| 24 | CmrExpPoDistCostsPEOInvoiceAmtEnteredCurr | INVOICE_AMT_ENTERED_CURR | — | ✅ |
| 25 | CmrExpPoDistCostsPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 26 | CmrExpPoDistCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | CmrExpPoDistCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | CmrExpPoDistCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | CmrExpPoDistCostsPEONetDeliveredQty | NET_DELIVERED_QTY | — | ✅ |
| 30 | CmrExpPoDistCostsPEONetExpAdjAmt | NET_EXP_ADJ_AMT | — | ✅ |
| 31 | CmrExpPoDistCostsPEONetExpAdjAmtEnteredCurr | NET_EXP_ADJ_AMT_ENTERED_CURR | — | ✅ |
| 32 | CmrExpPoDistCostsPEONetExpAdjAmtRounded | NET_EXP_ADJ_AMT_ROUNDED | — | ✅ |
| 33 | CmrExpPoDistCostsPEONetExpAdjAmtRoundedEc | NET_EXP_ADJ_AMT_ROUNDED_EC | — | ✅ |
| 34 | CmrExpPoDistCostsPEONetInvoicedQty | NET_INVOICED_QTY | — | ✅ |
| 35 | CmrExpPoDistCostsPEOPoAmount | PO_AMOUNT | — | ✅ |
| 36 | CmrExpPoDistCostsPEOPoAmountEnteredCurr | PO_AMOUNT_ENTERED_CURR | — | ✅ |
| 37 | CmrExpPoDistCostsPEOPoAmountRounded | PO_AMOUNT_ROUNDED | — | ✅ |
| 38 | CmrExpPoDistCostsPEOPoAmountRoundedEc | PO_AMOUNT_ROUNDED_EC | — | ✅ |
| 39 | CmrExpPoDistCostsPEOPoNumber | PO_NUMBER | — | ✅ |
| 40 | CmrExpPoDistCostsPEOPoUnitValue | PO_UNIT_VALUE | — | ✅ |
| 41 | CmrExpPoDistCostsPEOPurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 42 | CmrExpPoDistCostsPEORetroEventDate | RETRO_EVENT_DATE | — | ✅ |
| 43 | CmrExpPoDistCostsPEORetroEventFlag | RETRO_EVENT_FLAG | — | ✅ |
| 44 | CmrExpPoDistCostsPEOSoldToBusinessUnitId | SOLD_TO_BUSINESS_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
