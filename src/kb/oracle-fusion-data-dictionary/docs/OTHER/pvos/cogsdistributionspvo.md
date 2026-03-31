---
id: DOC-OTHER-PVO-COGSDistributionsPVO
doc_type: system-doc
title: "COGSDistributionsPVO — PVO Cross-Module"
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
  - COGSDistributionsPVO
  - cogsdistributionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# COGSDistributionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de COGSDistributions. Acessa as tabelas: CST_COGS_LAYER_COSTS, CST_COGS_TRANSACTIONS, CST_COST_DISTRIBUTIONS (+6).

**Caminho:** `FscmTopModelAM.COGSDistributionsAM.COGSDistributionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 181 | 9 | 2 | 178 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cogs_layer_costs|CST_COGS_LAYER_COSTS]] — 15 atributos (1 PKs, 15 BICC)
- [[cst_cogs_transactions|CST_COGS_TRANSACTIONS]] — 23 atributos (23 BICC)
- [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]] — 28 atributos (28 BICC)
- [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]] — 25 atributos (1 PKs, 25 BICC)
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 3 atributos (3 BICC)
- [[cst_revenue_lines|CST_REVENUE_LINES]] — 48 atributos (45 BICC)
- [[cst_sales_order_details|CST_SALES_ORDER_DETAILS]] — 31 atributos (31 BICC)
- [[cst_transactions|CST_TRANSACTIONS]] — 2 atributos (2 BICC)
- [[gl_calendars|GL_CALENDARS]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cst_cogs_layer_costs|CST_COGS_LAYER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CogsLayerCostId | COGS_LAYER_COST_ID | 🔑 | ✅ |
| 2 | CogsLayersCostsPEOCogsTransactionId | COGS_TRANSACTION_ID | — | ✅ |
| 3 | CogsLayersCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CogsLayersCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CogsLayersCostsPEOCstLayerCostId | CST_LAYER_COST_ID | — | ✅ |
| 6 | CogsLayersCostsPEOCstTransactionId | CST_TRANSACTION_ID | — | ✅ |
| 7 | CogsLayersCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 8 | CogsLayersCostsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 9 | CogsLayersCostsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | CogsLayersCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CogsLayersCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CogsLayersCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CogsLayersCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 14 | CogsLayersCostsPEOQuantity | QUANTITY | — | ✅ |
| 15 | CogsLayersCostsPEORequestId | REQUEST_ID | — | ✅ |

### [[cst_cogs_transactions|CST_COGS_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | COGSTransactionsPEOCogsPercentage | COGS_PERCENTAGE | — | ✅ |
| 2 | COGSTransactionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | COGSTransactionsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | COGSTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | COGSTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | COGSTransactionsPEOCstTransactionId | CST_TRANSACTION_ID | — | ✅ |
| 7 | COGSTransactionsPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 8 | COGSTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | COGSTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 10 | COGSTransactionsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | COGSTransactionsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | COGSTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | COGSTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | COGSTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | COGSTransactionsPEORequestId | REQUEST_ID | — | ✅ |
| 16 | COGSTransactionsPEORevenueLineId | REVENUE_LINE_ID | — | ✅ |
| 17 | COGSTransactionsPEORmaTransactionId | RMA_TRANSACTION_ID | — | ✅ |
| 18 | COGSTransactionsPEOShipmentFullfillLineId | SHIPMENT_FULLFILL_LINE_ID | — | ✅ |
| 19 | COGSTransactionsPEOTransactionActionId | TRANSACTION_ACTION_ID | — | ✅ |
| 20 | COGSTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 21 | COGSTransactionsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 22 | COGSTransactionsPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 23 | COGSTransactionsPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |

### [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionsPEOAccountedFlag | ACCOUNTED_FLAG | — | ✅ |
| 2 | CostDistributionsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CostDistributionsPEOBaseCurrencyCode | BASE_CURRENCY_CODE | — | ✅ |
| 4 | CostDistributionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CostDistributionsPEOCostOrganizationId | COST_ORGANIZATION_ID | — | ✅ |
| 6 | CostDistributionsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 7 | CostDistributionsPEOCostTransactionUom | COST_TRANSACTION_UOM | — | ✅ |
| 8 | CostDistributionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CostDistributionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CostDistributionsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 11 | CostDistributionsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 12 | CostDistributionsPEOEffDate | EFF_DATE | — | ✅ |
| 13 | CostDistributionsPEOEntityCode | ENTITY_CODE | — | ✅ |
| 14 | CostDistributionsPEOEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 15 | CostDistributionsPEOEventId | EVENT_ID | — | ✅ |
| 16 | CostDistributionsPEOEventTypeCode | EVENT_TYPE_CODE | — | ✅ |
| 17 | CostDistributionsPEOGlDate | GL_DATE | — | ✅ |
| 18 | CostDistributionsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 19 | CostDistributionsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 20 | CostDistributionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CostDistributionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CostDistributionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CostDistributionsPEOLayerQuantity | LAYER_QUANTITY | — | ✅ |
| 24 | CostDistributionsPEOLedgerId | LEDGER_ID | — | ✅ |
| 25 | CostDistributionsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 26 | CostDistributionsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 27 | CostDistributionsPEORequestId | REQUEST_ID | — | ✅ |
| 28 | CostDistributionsPEOTransactionId | TRANSACTION_ID | — | ✅ |

### [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionLinesPEOAccountingDefinitionId | ACCOUNTING_DEFINITION_ID | — | ✅ |
| 2 | CostDistributionLinesPEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CostDistributionLinesPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 4 | CostDistributionLinesPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CostDistributionLinesPEOCostId | COST_ID | — | ✅ |
| 6 | CostDistributionLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CostDistributionLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CostDistributionLinesPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 9 | CostDistributionLinesPEODrCrSign | DR_CR_SIGN | — | ✅ |
| 10 | CostDistributionLinesPEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | ✅ |
| 11 | CostDistributionLinesPEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 12 | CostDistributionLinesPEOEventId | EVENT_ID | — | ✅ |
| 13 | CostDistributionLinesPEOExchangeDate | EXCHANGE_DATE | — | ✅ |
| 14 | CostDistributionLinesPEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 15 | CostDistributionLinesPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 16 | CostDistributionLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CostDistributionLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | CostDistributionLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CostDistributionLinesPEOLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 20 | CostDistributionLinesPEOLineNumber | LINE_NUMBER | — | ✅ |
| 21 | CostDistributionLinesPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | ✅ |
| 22 | CostDistributionLinesPEOSlaCodeCombinationId | SLA_CODE_COMBINATION_ID | — | ✅ |
| 23 | CostDistributionLinesPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 24 | CostDistributionLinesPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 25 | DistributionLineId | DISTRIBUTION_LINE_ID | 🔑 | ✅ |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | ✅ |
| 2 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | ✅ |

### [[cst_revenue_lines|CST_REVENUE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueLinesPEOAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | RevenueLinesPEOAtoTopModelFlineId | ATO_TOP_MODEL_FLINE_ID | — | — |
| 3 | RevenueLinesPEOAtoTopModelItemId | ATO_TOP_MODEL_ITEM_ID | — | — |
| 4 | RevenueLinesPEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 5 | RevenueLinesPEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 6 | RevenueLinesPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 7 | RevenueLinesPEOConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | — |
| 8 | RevenueLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | RevenueLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | RevenueLinesPEOCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 11 | RevenueLinesPEOCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 12 | RevenueLinesPEODeliveryId | DELIVERY_ID | — | ✅ |
| 13 | RevenueLinesPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 14 | RevenueLinesPEODooFulfillLineId | DOO_FULFILL_LINE_ID | — | ✅ |
| 15 | RevenueLinesPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 16 | RevenueLinesPEODooOrderType | DOO_ORDER_TYPE | — | ✅ |
| 17 | RevenueLinesPEODooReferenceFulfillLineId | DOO_REFERENCE_FULFILL_LINE_ID | — | ✅ |
| 18 | RevenueLinesPEOExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 19 | RevenueLinesPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 20 | RevenueLinesPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 21 | RevenueLinesPEOGlDate | GL_DATE | — | ✅ |
| 22 | RevenueLinesPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 23 | RevenueLinesPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 24 | RevenueLinesPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 25 | RevenueLinesPEOInvoiceLineAmount | INVOICE_LINE_AMOUNT | — | ✅ |
| 26 | RevenueLinesPEOInvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 27 | RevenueLinesPEOInvoiceSource | INVOICE_SOURCE | — | ✅ |
| 28 | RevenueLinesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 29 | RevenueLinesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 30 | RevenueLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | RevenueLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 32 | RevenueLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | RevenueLinesPEOLedgerId | LEDGER_ID | — | ✅ |
| 34 | RevenueLinesPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 35 | RevenueLinesPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 36 | RevenueLinesPEOPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | ✅ |
| 37 | RevenueLinesPEOPreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | ✅ |
| 38 | RevenueLinesPEOQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 39 | RevenueLinesPEOReferenceLineId | REFERENCE_LINE_ID | — | ✅ |
| 40 | RevenueLinesPEORequestId | REQUEST_ID | — | ✅ |
| 41 | RevenueLinesPEORevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 42 | RevenueLinesPEORevenueLineId | REVENUE_LINE_ID | — | ✅ |
| 43 | RevenueLinesPEORevenuePercentage | REVENUE_PERCENTAGE | — | ✅ |
| 44 | RevenueLinesPEORootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
| 45 | RevenueLinesPEOTxnProcessingGroupId | TXN_PROCESSING_GROUP_ID | — | ✅ |
| 46 | RevenueLinesPEOUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 47 | RevenueLinesPEOUomCode | UOM_CODE | — | ✅ |
| 48 | RevenueLinesPEOWarehouseId | WAREHOUSE_ID | — | ✅ |

### [[cst_sales_order_details|CST_SALES_ORDER_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesOrderDetailsPEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 2 | SalesOrderDetailsPEOConversionDate | CONVERSION_DATE | — | ✅ |
| 3 | SalesOrderDetailsPEOConversionRate | CONVERSION_RATE | — | ✅ |
| 4 | SalesOrderDetailsPEOConversionTypeCode | CONVERSION_TYPE_CODE | — | ✅ |
| 5 | SalesOrderDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | SalesOrderDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | SalesOrderDetailsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 8 | SalesOrderDetailsPEODooLineId | DOO_LINE_ID | — | ✅ |
| 9 | SalesOrderDetailsPEODooLineNumber | DOO_LINE_NUMBER | — | ✅ |
| 10 | SalesOrderDetailsPEODooOrderCurrency | DOO_ORDER_CURRENCY | — | ✅ |
| 11 | SalesOrderDetailsPEODooOrderHeaderId | DOO_ORDER_HEADER_ID | — | ✅ |
| 12 | SalesOrderDetailsPEODooOrderNumber | DOO_ORDER_NUMBER | — | ✅ |
| 13 | SalesOrderDetailsPEODooOrderedDate | DOO_ORDERED_DATE | — | ✅ |
| 14 | SalesOrderDetailsPEODooUnitSellingPrice | DOO_UNIT_SELLING_PRICE | — | ✅ |
| 15 | SalesOrderDetailsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 16 | SalesOrderDetailsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 17 | SalesOrderDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 18 | SalesOrderDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 19 | SalesOrderDetailsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 20 | SalesOrderDetailsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 21 | SalesOrderDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | SalesOrderDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | SalesOrderDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | SalesOrderDetailsPEOParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 25 | SalesOrderDetailsPEOReferencedDooFulfillLineId | REFERENCED_DOO_FULFILL_LINE_ID | — | ✅ |
| 26 | SalesOrderDetailsPEORequestId | REQUEST_ID | — | ✅ |
| 27 | SalesOrderDetailsPEORootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
| 28 | SalesOrderDetailsPEOSalesRepId | SALES_REP_ID | — | ✅ |
| 29 | SalesOrderDetailsPEOSellingLegalEntityId | SELLING_LEGAL_ENTITY_ID | — | ✅ |
| 30 | SalesOrderDetailsPEOSellingOrgId | SELLING_ORG_ID | — | ✅ |
| 31 | SalesOrderDetailsPEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |

### [[cst_transactions|CST_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 2 | TransactionId | TRANSACTION_ID | — | ✅ |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsCalendarId | CALENDAR_ID | — | ✅ |
| 2 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | ✅ |
| 4 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 5 | GlCalendarsPeriodType | PERIOD_TYPE | — | ✅ |
| 6 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
