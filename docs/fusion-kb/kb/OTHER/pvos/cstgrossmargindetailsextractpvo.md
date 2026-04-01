---
id: DOC-OTHER-PVO-CstGrossMarginDetailsExtractPVO
doc_type: system-doc
title: "CstGrossMarginDetailsExtractPVO — PVO Cross-Module"
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
  - CstGrossMarginDetailsExtractPVO
  - cstgrossmargindetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstGrossMarginDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Gross Margin Details Extract. Acessa as tabelas: CST_GROSS_MARGIN_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstGrossMarginDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 1 | 44 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_gross_margin_details|CST_GROSS_MARGIN_DETAILS]] — 44 atributos (1 PKs, 44 BICC)

---

## ⚙️ Atributos

### [[cst_gross_margin_details|CST_GROSS_MARGIN_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstGrossMarginDetailsPEOCogsAccountId | COGS_ACCOUNT_ID | — | ✅ |
| 2 | CstGrossMarginDetailsPEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 3 | CstGrossMarginDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstGrossMarginDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | CstGrossMarginDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstGrossMarginDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstGrossMarginDetailsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CstGrossMarginDetailsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 9 | CstGrossMarginDetailsPEOCustomerType | CUSTOMER_TYPE | — | ✅ |
| 10 | CstGrossMarginDetailsPEODocLineId | DOC_LINE_ID | — | ✅ |
| 11 | CstGrossMarginDetailsPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 12 | CstGrossMarginDetailsPEODooOrderType | DOO_ORDER_TYPE | — | ✅ |
| 13 | CstGrossMarginDetailsPEOGlDate | GL_DATE | — | ✅ |
| 14 | CstGrossMarginDetailsPEOGrossMarginDetailId | GROSS_MARGIN_DETAIL_ID | 🔑 | ✅ |
| 15 | CstGrossMarginDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | CstGrossMarginDetailsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 17 | CstGrossMarginDetailsPEOInvoiceId | INVOICE_ID | — | ✅ |
| 18 | CstGrossMarginDetailsPEOInvoiceLineId | INVOICE_LINE_ID | — | ✅ |
| 19 | CstGrossMarginDetailsPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 20 | CstGrossMarginDetailsPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 21 | CstGrossMarginDetailsPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 22 | CstGrossMarginDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CstGrossMarginDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CstGrossMarginDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CstGrossMarginDetailsPEOOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 26 | CstGrossMarginDetailsPEOProfitCenterBuId | PROFIT_CENTER_BU_ID | — | ✅ |
| 27 | CstGrossMarginDetailsPEORecognizedCogsAmount | RECOGNIZED_COGS_AMOUNT | — | ✅ |
| 28 | CstGrossMarginDetailsPEORecognizedCogsOverheadAmt | RECOGNIZED_COGS_OVERHEAD_AMT | — | ✅ |
| 29 | CstGrossMarginDetailsPEORecognizedCogsProfitAmt | RECOGNIZED_COGS_PROFIT_AMT | — | ✅ |
| 30 | CstGrossMarginDetailsPEORecognizedCogsResourceAmt | RECOGNIZED_COGS_RESOURCE_AMT | — | ✅ |
| 31 | CstGrossMarginDetailsPEORecognizedGrossMargin | RECOGNIZED_GROSS_MARGIN | — | ✅ |
| 32 | CstGrossMarginDetailsPEORecognizedRev | RECOGNIZED_REV | — | ✅ |
| 33 | CstGrossMarginDetailsPEORevenueRecognitionSrc | REVENUE_RECOGNITION_SRC | — | ✅ |
| 34 | CstGrossMarginDetailsPEORootInventoryItemId | ROOT_INVENTORY_ITEM_ID | — | ✅ |
| 35 | CstGrossMarginDetailsPEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |
| 36 | CstGrossMarginDetailsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 37 | CstGrossMarginDetailsPEOShipmentType | SHIPMENT_TYPE | — | ✅ |
| 38 | CstGrossMarginDetailsPEOSuccessorBuId | SUCCESSOR_BU_ID | — | ✅ |
| 39 | CstGrossMarginDetailsPEOUnrecognizedCogsAmount | UNRECOGNIZED_COGS_AMOUNT | — | ✅ |
| 40 | CstGrossMarginDetailsPEOUnrecognizedCogsOverheadAmt | UNRECOGNIZED_COGS_OVERHEAD_AMT | — | ✅ |
| 41 | CstGrossMarginDetailsPEOUnrecognizedCogsProfitAmt | UNRECOGNIZED_COGS_PROFIT_AMT | — | ✅ |
| 42 | CstGrossMarginDetailsPEOUnrecognizedCogsResourceAmt | UNRECOGNIZED_COGS_RESOURCE_AMT | — | ✅ |
| 43 | CstGrossMarginDetailsPEOUnrecognizedGrossMargin | UNRECOGNIZED_GROSS_MARGIN | — | ✅ |
| 44 | CstGrossMarginDetailsPEOUnrecognizedRev | UNRECOGNIZED_REV | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
