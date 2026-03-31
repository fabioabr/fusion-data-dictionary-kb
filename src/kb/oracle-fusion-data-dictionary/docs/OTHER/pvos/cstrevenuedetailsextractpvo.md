---
id: DOC-OTHER-PVO-CstRevenueDetailsExtractPVO
doc_type: system-doc
title: "CstRevenueDetailsExtractPVO — PVO Cross-Module"
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
  - CstRevenueDetailsExtractPVO
  - cstrevenuedetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstRevenueDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Revenue Details Extract. Acessa as tabelas: CST_REVENUE_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstRevenueDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_revenue_details|CST_REVENUE_DETAILS]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[cst_revenue_details|CST_REVENUE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstRevenueDetailsPEOAcctdRecognizedRev | ACCTD_RECOGNIZED_REV | — | ✅ |
| 2 | CstRevenueDetailsPEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 3 | CstRevenueDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstRevenueDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | CstRevenueDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstRevenueDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstRevenueDetailsPEOCtDooFullfillLineId | CT_DOO_FULLFILL_LINE_ID | — | ✅ |
| 8 | CstRevenueDetailsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 9 | CstRevenueDetailsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 10 | CstRevenueDetailsPEODistributionLineId | DISTRIBUTION_LINE_ID | — | ✅ |
| 11 | CstRevenueDetailsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 12 | CstRevenueDetailsPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 13 | CstRevenueDetailsPEODooOrderType | DOO_ORDER_TYPE | — | ✅ |
| 14 | CstRevenueDetailsPEOEventId | EVENT_ID | — | ✅ |
| 15 | CstRevenueDetailsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 16 | CstRevenueDetailsPEOFlowInstanceId | FLOW_INSTANCE_ID | — | ✅ |
| 17 | CstRevenueDetailsPEOGlDate | GL_DATE | — | ✅ |
| 18 | CstRevenueDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | CstRevenueDetailsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 20 | CstRevenueDetailsPEOInvoiceCurrency | INVOICE_CURRENCY | — | ✅ |
| 21 | CstRevenueDetailsPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 22 | CstRevenueDetailsPEOInvoiceId | INVOICE_ID | — | ✅ |
| 23 | CstRevenueDetailsPEOInvoiceLineId | INVOICE_LINE_ID | — | ✅ |
| 24 | CstRevenueDetailsPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 25 | CstRevenueDetailsPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 26 | CstRevenueDetailsPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 27 | CstRevenueDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | CstRevenueDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | CstRevenueDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | CstRevenueDetailsPEOLedgerCurrency | LEDGER_CURRENCY | — | ✅ |
| 31 | CstRevenueDetailsPEOLedgerId | LEDGER_ID | — | ✅ |
| 32 | CstRevenueDetailsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 33 | CstRevenueDetailsPEOLineNo | LINE_NO | — | ✅ |
| 34 | CstRevenueDetailsPEOMarginCalcFlag | MARGIN_CALC_FLAG | — | ✅ |
| 35 | CstRevenueDetailsPEOProfitCenterBuId | PROFIT_CENTER_BU_ID | — | ✅ |
| 36 | CstRevenueDetailsPEORecognizedRev | RECOGNIZED_REV | — | ✅ |
| 37 | CstRevenueDetailsPEORevenueDetailId | REVENUE_DETAIL_ID | 🔑 | ✅ |
| 38 | CstRevenueDetailsPEORevenueLineId | REVENUE_LINE_ID | — | ✅ |
| 39 | CstRevenueDetailsPEORevenueType | REVENUE_TYPE | — | ✅ |
| 40 | CstRevenueDetailsPEORootInventoryItemId | ROOT_INVENTORY_ITEM_ID | — | ✅ |
| 41 | CstRevenueDetailsPEOSalesOrderShipmentNumber | SALES_ORDER_SHIPMENT_NUMBER | — | ✅ |
| 42 | CstRevenueDetailsPEOSalesOrderShipmentType | SALES_ORDER_SHIPMENT_TYPE | — | ✅ |
| 43 | CstRevenueDetailsPEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |
| 44 | CstRevenueDetailsPEOSuccessorBuId | SUCCESSOR_BU_ID | — | ✅ |
| 45 | CstRevenueDetailsPEOTotalRev | TOTAL_REV | — | ✅ |
| 46 | CstRevenueDetailsPEOTxnInventoryItemId | TXN_INVENTORY_ITEM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
