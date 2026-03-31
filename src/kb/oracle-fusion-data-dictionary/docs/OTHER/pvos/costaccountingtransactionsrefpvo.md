---
id: DOC-OTHER-PVO-CostAccountingTransactionsRefPVO
doc_type: system-doc
title: "CostAccountingTransactionsRefPVO — PVO Cross-Module"
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
  - CostAccountingTransactionsRefPVO
  - costaccountingtransactionsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostAccountingTransactionsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Accounting Transactions Ref. Acessa as tabelas: AP_INVOICES_ALL, AP_INVOICE_DISTRIBUTIONS_ALL, AP_INVOICE_LINES_ALL (+30).

**Caminho:** `FscmTopModelAM.CostTransactionAM.CostAccountingTransactionsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 793 | 33 | 4 | 62 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 3 atributos
- [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]] — 6 atributos
- [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]] — 3 atributos
- [[cmr_ap_invoice_dtls|CMR_AP_INVOICE_DTLS]] — 66 atributos (1 BICC)
- [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]] — 84 atributos
- [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]] — 91 atributos (1 BICC)
- [[cmr_r_active_purchase_orddtl_v|CMR_R_ACTIVE_PURCHASE_ORDDTL_V]] — 2 atributos
- [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]] — 94 atributos (1 PKs, 31 BICC)
- [[cst_all_expense_pool_txns_v|CST_ALL_EXPENSE_POOL_TXNS_V]] — 16 atributos (3 BICC)
- [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]] — 31 atributos (1 PKs, 12 BICC)
- [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]] — 28 atributos (1 PKs, 6 BICC)
- [[cst_cost_orgs_v|CST_COST_ORGS_V]] — 4 atributos
- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 6 atributos
- [[cst_inv_transactions|CST_INV_TRANSACTIONS]] — 53 atributos (1 PKs, 2 BICC)
- [[cst_trade_events|CST_TRADE_EVENTS]] — 4 atributos
- [[cst_txn_invoice_asc_v|CST_TXN_INVOICE_ASC_V]] — 3 atributos
- [[cst_work_orders|CST_WORK_ORDERS]] — 3 atributos
- [[doo_document_references|DOO_DOCUMENT_REFERENCES]] — 23 atributos
- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 115 atributos
- [[doo_headers_all|DOO_HEADERS_ALL]] — 31 atributos
- [[doo_lines_all|DOO_LINES_ALL]] — 5 atributos
- [[doo_order_totals|DOO_ORDER_TOTALS]] — 4 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 3 atributos
- [[gl_calendars|GL_CALENDARS]] — 6 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[po_headers_all|PO_HEADERS_ALL]] — 3 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 5 atributos
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 11 atributos
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 62 atributos
- [[xla_cst_distribution_lines_vl|XLA_CST_DISTRIBUTION_LINES_VL]] — 9 atributos (6 BICC)
- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 6 atributos
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 7 atributos

---

## ⚙️ Atributos

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 2 | InvoiceHeaderPEOInvoiceId | INVOICE_ID | — | — |
| 3 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[ap_invoice_distributions_all|AP_INVOICE_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceDistributionPEOAmount | AMOUNT | — | — |
| 2 | InvoiceDistributionPEOInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 3 | InvoiceDistributionPEOInvoiceId | INVOICE_ID | — | — |
| 4 | InvoiceDistributionPEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 5 | InvoiceDistributionPEOLineTypeLookupCode | LINE_TYPE_LOOKUP_CODE | — | — |
| 6 | InvoiceDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceLinePEOInvoiceId | INVOICE_ID | — | — |
| 2 | InvoiceLinePEOLineNumber | LINE_NUMBER | — | — |
| 3 | InvoiceLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[cmr_ap_invoice_dtls|CMR_AP_INVOICE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrApInvoiceDtlsPEOAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | CmrApInvoiceDtlsPEOChargeApplicableToDistId | CHARGE_APPLICABLE_TO_DIST_ID | — | — |
| 3 | CmrApInvoiceDtlsPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | — | — |
| 4 | CmrApInvoiceDtlsPEOCmrApInvoiceLineId | CMR_AP_INVOICE_LINE_ID | — | — |
| 5 | CmrApInvoiceDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 6 | CmrApInvoiceDtlsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 7 | CmrApInvoiceDtlsPEOConsumptionAdviceHeaderId | CONSUMPTION_ADVICE_HEADER_ID | — | — |
| 8 | CmrApInvoiceDtlsPEOConsumptionAdviceLineId | CONSUMPTION_ADVICE_LINE_ID | — | — |
| 9 | CmrApInvoiceDtlsPEOCorrectedInvoiceDistId | CORRECTED_INVOICE_DIST_ID | — | — |
| 10 | CmrApInvoiceDtlsPEOCreatedBy | CREATED_BY | — | — |
| 11 | CmrApInvoiceDtlsPEOCreationDate | CREATION_DATE | — | — |
| 12 | CmrApInvoiceDtlsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 13 | CmrApInvoiceDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 14 | CmrApInvoiceDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 15 | CmrApInvoiceDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 16 | CmrApInvoiceDtlsPEODistCodeCombinationId | DIST_CODE_COMBINATION_ID | — | — |
| 17 | CmrApInvoiceDtlsPEODistributionMatchType | DISTRIBUTION_MATCH_TYPE | — | — |
| 18 | CmrApInvoiceDtlsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 19 | CmrApInvoiceDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 20 | CmrApInvoiceDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 21 | CmrApInvoiceDtlsPEOFinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 22 | CmrApInvoiceDtlsPEOFiscalChargeType | FISCAL_CHARGE_TYPE | — | — |
| 23 | CmrApInvoiceDtlsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | — |
| 24 | CmrApInvoiceDtlsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | — |
| 25 | CmrApInvoiceDtlsPEOInclusiveFlag | INCLUSIVE_FLAG | — | — |
| 26 | CmrApInvoiceDtlsPEOInvoiceAmt | INVOICE_AMT | — | — |
| 27 | CmrApInvoiceDtlsPEOInvoiceBaseAmount | INVOICE_BASE_AMOUNT | — | — |
| 28 | CmrApInvoiceDtlsPEOInvoiceCreationDate | INVOICE_CREATION_DATE | — | — |
| 29 | CmrApInvoiceDtlsPEOInvoiceDistributionType | INVOICE_DISTRIBUTION_TYPE | — | — |
| 30 | CmrApInvoiceDtlsPEOInvoiceId | INVOICE_ID | — | — |
| 31 | CmrApInvoiceDtlsPEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 32 | CmrApInvoiceDtlsPEOInvoiceLineType | INVOICE_LINE_TYPE | — | — |
| 33 | CmrApInvoiceDtlsPEOInvoiceNumber | INVOICE_NUMBER | — | — |
| 34 | CmrApInvoiceDtlsPEOInvoiceQty | INVOICE_QTY | — | — |
| 35 | CmrApInvoiceDtlsPEOInvoiceQtyInPoUom | INVOICE_QTY_IN_PO_UOM | — | — |
| 36 | CmrApInvoiceDtlsPEOInvoiceQtyInPrimaryUom | INVOICE_QTY_IN_PRIMARY_UOM | — | — |
| 37 | CmrApInvoiceDtlsPEOInvoiceSource | INVOICE_SOURCE | — | — |
| 38 | CmrApInvoiceDtlsPEOInvoiceType | INVOICE_TYPE | — | — |
| 39 | CmrApInvoiceDtlsPEOInvoicingBuFuncCurrCode | INVOICING_BU_FUNC_CURR_CODE | — | — |
| 40 | CmrApInvoiceDtlsPEOInvoicingBusinessUnitId | INVOICING_BUSINESS_UNIT_ID | — | — |
| 41 | CmrApInvoiceDtlsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 42 | CmrApInvoiceDtlsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 43 | CmrApInvoiceDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | CmrApInvoiceDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | CmrApInvoiceDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | CmrApInvoiceDtlsPEOLcmAssociationProcessedFlag | LCM_ASSOCIATION_PROCESSED_FLAG | — | — |
| 47 | CmrApInvoiceDtlsPEOLcmAssociationRequestId | LCM_ASSOCIATION_REQUEST_ID | — | — |
| 48 | CmrApInvoiceDtlsPEOLcmEnabledFlag | LCM_ENABLED_FLAG | — | — |
| 49 | CmrApInvoiceDtlsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | — |
| 50 | CmrApInvoiceDtlsPEOLineCancelledFlag | LINE_CANCELLED_FLAG | — | — |
| 51 | CmrApInvoiceDtlsPEOOnlineAssocProcessId | ONLINE_ASSOC_PROCESS_ID | — | — |
| 52 | CmrApInvoiceDtlsPEOParentReversalId | PARENT_REVERSAL_ID | — | — |
| 53 | CmrApInvoiceDtlsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 54 | CmrApInvoiceDtlsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | — |
| 55 | CmrApInvoiceDtlsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | — |
| 56 | CmrApInvoiceDtlsPEOProcurementBusinessUnitId | PROCUREMENT_BUSINESS_UNIT_ID | — | — |
| 57 | CmrApInvoiceDtlsPEORcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 58 | CmrApInvoiceDtlsPEORelatedDistributionId | RELATED_DISTRIBUTION_ID | — | — |
| 59 | CmrApInvoiceDtlsPEORequestId | REQUEST_ID | — | — |
| 60 | CmrApInvoiceDtlsPEOReversalFlag | REVERSAL_FLAG | — | — |
| 61 | CmrApInvoiceDtlsPEOSelfAssessedFlag | SELF_ASSESSED_FLAG | — | — |
| 62 | CmrApInvoiceDtlsPEOTaxCodeId | TAX_CODE_ID | — | — |
| 63 | CmrApInvoiceDtlsPEOTaxPointBasis | TAX_POINT_BASIS | — | — |
| 64 | CmrApInvoiceDtlsPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 65 | CmrApInvoiceDtlsPEOVendorId | VENDOR_ID | — | — |
| 66 | CmrApInvoiceDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | — |

### [[cmr_purchase_order_dtls|CMR_PURCHASE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderDtlsPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | — |
| 2 | PurchaseOrderDtlsPEOAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | — |
| 3 | PurchaseOrderDtlsPEOActiveFlag | ACTIVE_FLAG | — | — |
| 4 | PurchaseOrderDtlsPEOActiveForCaFlag | ACTIVE_FOR_CA_FLAG | — | — |
| 5 | PurchaseOrderDtlsPEOAgentId | AGENT_ID | — | — |
| 6 | PurchaseOrderDtlsPEOAmountCancelled | AMOUNT_CANCELLED | — | — |
| 7 | PurchaseOrderDtlsPEOAmountOrdered | AMOUNT_ORDERED | — | — |
| 8 | PurchaseOrderDtlsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 9 | PurchaseOrderDtlsPEOCategoryId | CATEGORY_ID | — | — |
| 10 | PurchaseOrderDtlsPEOChargeAccountId | CHARGE_ACCOUNT_ID | — | — |
| 11 | PurchaseOrderDtlsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 12 | PurchaseOrderDtlsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | — |
| 13 | PurchaseOrderDtlsPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 14 | PurchaseOrderDtlsPEOConvFactorToPrimaryUom | CONV_FACTOR_TO_PRIMARY_UOM | — | — |
| 15 | PurchaseOrderDtlsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 16 | PurchaseOrderDtlsPEOCreatedBy | CREATED_BY | — | — |
| 17 | PurchaseOrderDtlsPEOCreationDate | CREATION_DATE | — | — |
| 18 | PurchaseOrderDtlsPEOCurrencyCode | CURRENCY_CODE | — | — |
| 19 | PurchaseOrderDtlsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 20 | PurchaseOrderDtlsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 21 | PurchaseOrderDtlsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 22 | PurchaseOrderDtlsPEODefaultInventoryOrgId | DEFAULT_INVENTORY_ORG_ID | — | — |
| 23 | PurchaseOrderDtlsPEODeliverToBuFuncCurrCode | DELIVER_TO_BU_FUNC_CURR_CODE | — | — |
| 24 | PurchaseOrderDtlsPEODeliverToBusinessUnitId | DELIVER_TO_BUSINESS_UNIT_ID | — | — |
| 25 | PurchaseOrderDtlsPEODeliverToInventoryOrgId | DELIVER_TO_INVENTORY_ORG_ID | — | — |
| 26 | PurchaseOrderDtlsPEODestinationChargeAccountId | DESTINATION_CHARGE_ACCOUNT_ID | — | — |
| 27 | PurchaseOrderDtlsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 28 | PurchaseOrderDtlsPEODestinationVarianceAcctId | DESTINATION_VARIANCE_ACCT_ID | — | — |
| 29 | PurchaseOrderDtlsPEODistributionNumber | DISTRIBUTION_NUMBER | — | — |
| 30 | PurchaseOrderDtlsPEOEventDate | EVENT_DATE | — | — |
| 31 | PurchaseOrderDtlsPEOEventType | EVENT_TYPE | — | — |
| 32 | PurchaseOrderDtlsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 33 | PurchaseOrderDtlsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 34 | PurchaseOrderDtlsPEOIntendedUse | INTENDED_USE | — | — |
| 35 | PurchaseOrderDtlsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 36 | PurchaseOrderDtlsPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 37 | PurchaseOrderDtlsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 38 | PurchaseOrderDtlsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 39 | PurchaseOrderDtlsPEOLastRunPeriodId | LAST_RUN_PERIOD_ID | — | — |
| 40 | PurchaseOrderDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 41 | PurchaseOrderDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | PurchaseOrderDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | PurchaseOrderDtlsPEOLineNumber | LINE_NUMBER | — | — |
| 44 | PurchaseOrderDtlsPEOMatchOption | MATCH_OPTION | — | — |
| 45 | PurchaseOrderDtlsPEOMatchingBasis | MATCHING_BASIS | — | — |
| 46 | PurchaseOrderDtlsPEONeedByDate | NEED_BY_DATE | — | — |
| 47 | PurchaseOrderDtlsPEONonrecoverableInclusiveTax | NONRECOVERABLE_INCLUSIVE_TAX | — | — |
| 48 | PurchaseOrderDtlsPEONonrecoverableTax | NONRECOVERABLE_TAX | — | — |
| 49 | PurchaseOrderDtlsPEONrTaxInPrimaryUom | NR_TAX_IN_PRIMARY_UOM | — | — |
| 50 | PurchaseOrderDtlsPEOOrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | — |
| 51 | PurchaseOrderDtlsPEOPeriodEndAccruedFlag | PERIOD_END_ACCRUED_FLAG | — | — |
| 52 | PurchaseOrderDtlsPEOPoHeaderId | PO_HEADER_ID | — | — |
| 53 | PurchaseOrderDtlsPEOPoLineId | PO_LINE_ID | — | — |
| 54 | PurchaseOrderDtlsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | — |
| 55 | PurchaseOrderDtlsPEOPoNumber | PO_NUMBER | — | — |
| 56 | PurchaseOrderDtlsPEOPrice | PRICE | — | — |
| 57 | PurchaseOrderDtlsPEOPriceInPrimaryUom | PRICE_IN_PRIMARY_UOM | — | — |
| 58 | PurchaseOrderDtlsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | — |
| 59 | PurchaseOrderDtlsPEOProcessedByRaFlag | PROCESSED_BY_RA_FLAG | — | — |
| 60 | PurchaseOrderDtlsPEOProcurementBusinessUnitId | PROCUREMENT_BUSINESS_UNIT_ID | — | — |
| 61 | PurchaseOrderDtlsPEOProductFiscalClassification | PRODUCT_FISCAL_CLASSIFICATION | — | — |
| 62 | PurchaseOrderDtlsPEOPromisedDate | PROMISED_DATE | — | — |
| 63 | PurchaseOrderDtlsPEOPurchaseBasis | PURCHASE_BASIS | — | — |
| 64 | PurchaseOrderDtlsPEOQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 65 | PurchaseOrderDtlsPEOQuantityOrdered | QUANTITY_ORDERED | — | — |
| 66 | PurchaseOrderDtlsPEORequestId | REQUEST_ID | — | — |
| 67 | PurchaseOrderDtlsPEORequisitioningBuId | REQUISITIONING_BU_ID | — | — |
| 68 | PurchaseOrderDtlsPEOSecondaryQtyCancelled | SECONDARY_QTY_CANCELLED | — | — |
| 69 | PurchaseOrderDtlsPEOSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 70 | PurchaseOrderDtlsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 71 | PurchaseOrderDtlsPEOSfoPrimaryTradeRelationId | SFO_PRIMARY_TRADE_RELATION_ID | — | — |
| 72 | PurchaseOrderDtlsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 73 | PurchaseOrderDtlsPEOShipmentNumber | SHIPMENT_NUMBER | — | — |
| 74 | PurchaseOrderDtlsPEOSoldToBusinessUnitId | SOLD_TO_BUSINESS_UNIT_ID | — | — |
| 75 | PurchaseOrderDtlsPEOSoldToLegalEntityId | SOLD_TO_LEGAL_ENTITY_ID | — | — |
| 76 | PurchaseOrderDtlsPEOSupplierItem | SUPPLIER_ITEM | — | — |
| 77 | PurchaseOrderDtlsPEOTaxExclusivePrice | TAX_EXCLUSIVE_PRICE | — | — |
| 78 | PurchaseOrderDtlsPEOTradeOrgBuFuncCurrCode | TRADE_ORG_BU_FUNC_CURR_CODE | — | — |
| 79 | PurchaseOrderDtlsPEOTradeOrganizationId | TRADE_ORGANIZATION_ID | — | — |
| 80 | PurchaseOrderDtlsPEOUomCode | UOM_CODE | — | — |
| 81 | PurchaseOrderDtlsPEOUseForGpFlag | USE_FOR_GP_FLAG | — | — |
| 82 | PurchaseOrderDtlsPEOVarianceAccountId | VARIANCE_ACCOUNT_ID | — | — |
| 83 | PurchaseOrderDtlsPEOVendorId | VENDOR_ID | — | — |
| 84 | PurchaseOrderDtlsPEOVendorSiteId | VENDOR_SITE_ID | — | — |

### [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvTransactionsPEOAllocatedFlag | ALLOCATED_FLAG | — | — |
| 2 | CmrRcvTransactionsPEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 3 | CmrRcvTransactionsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | CmrRcvTransactionsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | — |
| 5 | CmrRcvTransactionsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | — |
| 6 | CmrRcvTransactionsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | — |
| 7 | CmrRcvTransactionsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | — |
| 8 | CmrRcvTransactionsPEOCmrRootDeliverTxnId | CMR_ROOT_DELIVER_TXN_ID | — | — |
| 9 | CmrRcvTransactionsPEOCmrRootReceiveTxnId | CMR_ROOT_RECEIVE_TXN_ID | — | — |
| 10 | CmrRcvTransactionsPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 11 | CmrRcvTransactionsPEOCreatedBy | CREATED_BY | — | — |
| 12 | CmrRcvTransactionsPEOCreationDate | CREATION_DATE | — | — |
| 13 | CmrRcvTransactionsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 14 | CmrRcvTransactionsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 15 | CmrRcvTransactionsPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 16 | CmrRcvTransactionsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | — |
| 17 | CmrRcvTransactionsPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | — |
| 18 | CmrRcvTransactionsPEOErrorCode | ERROR_CODE | — | — |
| 19 | CmrRcvTransactionsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 20 | CmrRcvTransactionsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 21 | CmrRcvTransactionsPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 22 | CmrRcvTransactionsPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 23 | CmrRcvTransactionsPEOFtrId | FTR_ID | — | — |
| 24 | CmrRcvTransactionsPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | — |
| 25 | CmrRcvTransactionsPEOInterfaceBatchName | INTERFACE_BATCH_NAME | — | — |
| 26 | CmrRcvTransactionsPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | — |
| 27 | CmrRcvTransactionsPEOInvShippingTransactionId | INV_SHIPPING_TRANSACTION_ID | — | — |
| 28 | CmrRcvTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 29 | CmrRcvTransactionsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | CmrRcvTransactionsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | CmrRcvTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | CmrRcvTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | CmrRcvTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | CmrRcvTransactionsPEOOrigTfOrdInvShipTxnId | ORIG_TF_ORD_INV_SHIP_TXN_ID | — | — |
| 35 | CmrRcvTransactionsPEOParentTransactionId | PARENT_TRANSACTION_ID | — | — |
| 36 | CmrRcvTransactionsPEOPhysicalReturnReqdFlag | PHYSICAL_RETURN_REQD_FLAG | — | — |
| 37 | CmrRcvTransactionsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 38 | CmrRcvTransactionsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 39 | CmrRcvTransactionsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 40 | CmrRcvTransactionsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 41 | CmrRcvTransactionsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 42 | CmrRcvTransactionsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 43 | CmrRcvTransactionsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 44 | CmrRcvTransactionsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 45 | CmrRcvTransactionsPEOPjcInterfacedStatus | PJC_INTERFACED_STATUS | — | — |
| 46 | CmrRcvTransactionsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 47 | CmrRcvTransactionsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 48 | CmrRcvTransactionsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 49 | CmrRcvTransactionsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 50 | CmrRcvTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 51 | CmrRcvTransactionsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | — |
| 52 | CmrRcvTransactionsPEOPreprocessedStatus | PREPROCESSED_STATUS | — | — |
| 53 | CmrRcvTransactionsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | — |
| 54 | CmrRcvTransactionsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 55 | CmrRcvTransactionsPEOPriorTradeInvOrgId | PRIOR_TRADE_INV_ORG_ID | — | — |
| 56 | CmrRcvTransactionsPEOProcessByCaFlag | PROCESS_BY_CA_FLAG | — | — |
| 57 | CmrRcvTransactionsPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 58 | CmrRcvTransactionsPEOProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | — |
| 59 | CmrRcvTransactionsPEOProductType | PRODUCT_TYPE | — | — |
| 60 | CmrRcvTransactionsPEORcvParentTransactionId | RCV_PARENT_TRANSACTION_ID | — | — |
| 61 | CmrRcvTransactionsPEOReceiptCreationDate | RECEIPT_CREATION_DATE | — | — |
| 62 | CmrRcvTransactionsPEOReceiptLineNumber | RECEIPT_LINE_NUMBER | — | — |
| 63 | CmrRcvTransactionsPEOReceiptNumber | RECEIPT_NUMBER | — | — |
| 64 | CmrRcvTransactionsPEORequestId | REQUEST_ID | — | — |
| 65 | CmrRcvTransactionsPEORootDeliverTxnId | ROOT_DELIVER_TXN_ID | — | — |
| 66 | CmrRcvTransactionsPEORootReceiveTxnId | ROOT_RECEIVE_TXN_ID | — | — |
| 67 | CmrRcvTransactionsPEOShipFromInvOrgId | SHIP_FROM_INV_ORG_ID | — | — |
| 68 | CmrRcvTransactionsPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 69 | CmrRcvTransactionsPEOShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | — |
| 70 | CmrRcvTransactionsPEOShipmentLineNumber | SHIPMENT_LINE_NUMBER | — | — |
| 71 | CmrRcvTransactionsPEOShipmentNumber | SHIPMENT_NUMBER | — | — |
| 72 | CmrRcvTransactionsPEOSourceDocQuantity | SOURCE_DOC_QUANTITY | — | — |
| 73 | CmrRcvTransactionsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | — |
| 74 | CmrRcvTransactionsPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | — |
| 75 | CmrRcvTransactionsPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 76 | CmrRcvTransactionsPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | — |
| 77 | CmrRcvTransactionsPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | — |
| 78 | CmrRcvTransactionsPEOTaxProcessedFlag | TAX_PROCESSED_FLAG | — | — |
| 79 | CmrRcvTransactionsPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 80 | CmrRcvTransactionsPEOTransactionAmount | TRANSACTION_AMOUNT | — | — |
| 81 | CmrRcvTransactionsPEOTransactionDate | TRANSACTION_DATE | — | — |
| 82 | CmrRcvTransactionsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | — |
| 83 | CmrRcvTransactionsPEOTransactionType | TRANSACTION_TYPE | — | — |
| 84 | CmrRcvTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | — |
| 85 | CmrRcvTransactionsPEOTransferOrderDistId | TRANSFER_ORDER_DIST_ID | — | — |
| 86 | CmrRcvTransactionsPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | — |
| 87 | CmrRcvTransactionsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | — |
| 88 | CmrRcvTransactionsPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 89 | CmrRcvTransactionsPEOTxnFlowHeaderId | TXN_FLOW_HEADER_ID | — | — |
| 90 | CmrRcvTransactionsPEOTxnGroupId | TXN_GROUP_ID | — | — |
| 91 | CmrRcvTransactionsPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |

### [[cmr_r_active_purchase_orddtl_v|CMR_R_ACTIVE_PURCHASE_ORDDTL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchaseOrderDtlsPEORecoverableInclusiveTax | RECOVERABLE_INCLUSIVE_TAX | — | — |
| 2 | PurchaseOrderDtlsPEORecoverableTax | RECOVERABLE_TAX | — | — |

### [[cst_all_cost_transactions_v|CST_ALL_COST_TRANSACTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostAllTransactionsVPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CostAllTransactionsVPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 3 | CostAllTransactionsVPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | — |
| 4 | CostAllTransactionsVPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 5 | CostAllTransactionsVPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 6 | CostAllTransactionsVPEOCogsPercentage | COGS_PERCENTAGE | — | — |
| 7 | CostAllTransactionsVPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 8 | CostAllTransactionsVPEOCostBookId | COST_BOOK_ID | — | — |
| 9 | CostAllTransactionsVPEOCostDate | COST_DATE | — | ✅ |
| 10 | CostAllTransactionsVPEOCostMethodCode | COST_METHOD_CODE | — | — |
| 11 | CostAllTransactionsVPEOCostOrgId | COST_ORG_ID | — | — |
| 12 | CostAllTransactionsVPEOCostStatus | COST_STATUS | — | ✅ |
| 13 | CostAllTransactionsVPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 14 | CostAllTransactionsVPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 15 | CostAllTransactionsVPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | CostAllTransactionsVPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | CostAllTransactionsVPEOCstInvTransactionDtlId | CST_INV_TRANSACTION_DTL_ID | — | — |
| 18 | CostAllTransactionsVPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | — |
| 19 | CostAllTransactionsVPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | — |
| 20 | CostAllTransactionsVPEOCstWoResourceTxnId | CST_WO_RESOURCE_TXN_ID | — | — |
| 21 | CostAllTransactionsVPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | — |
| 22 | CostAllTransactionsVPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | — |
| 23 | CostAllTransactionsVPEODeliveryId | DELIVERY_ID | — | — |
| 24 | CostAllTransactionsVPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | — |
| 25 | CostAllTransactionsVPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 26 | CostAllTransactionsVPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 27 | CostAllTransactionsVPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | — |
| 28 | CostAllTransactionsVPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | — |
| 29 | CostAllTransactionsVPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | — |
| 30 | CostAllTransactionsVPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | — |
| 31 | CostAllTransactionsVPEOFromGradeCode | FROM_GRADE_CODE | — | ✅ |
| 32 | CostAllTransactionsVPEOGradeCode | GRADE_CODE | — | ✅ |
| 33 | CostAllTransactionsVPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 34 | CostAllTransactionsVPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 35 | CostAllTransactionsVPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 36 | CostAllTransactionsVPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 37 | CostAllTransactionsVPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | CostAllTransactionsVPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | CostAllTransactionsVPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | CostAllTransactionsVPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 41 | CostAllTransactionsVPEOLotNumber | LOT_NUMBER | — | ✅ |
| 42 | CostAllTransactionsVPEOParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 43 | CostAllTransactionsVPEOPeriodName | PERIOD_NAME | — | — |
| 44 | CostAllTransactionsVPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 45 | CostAllTransactionsVPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 46 | CostAllTransactionsVPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 47 | CostAllTransactionsVPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 48 | CostAllTransactionsVPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 49 | CostAllTransactionsVPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 50 | CostAllTransactionsVPEOPjcTaskId | PJC_TASK_ID | — | — |
| 51 | CostAllTransactionsVPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 52 | CostAllTransactionsVPEOPoDistributionId | PO_DISTRIBUTION_ID | — | — |
| 53 | CostAllTransactionsVPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | — |
| 54 | CostAllTransactionsVPEOPoItemDescriptionType | PO_ITEM_DESCRIPTION_TYPE | — | — |
| 55 | CostAllTransactionsVPEOPrimaryQty | PRIMARY_QTY | — | — |
| 56 | CostAllTransactionsVPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 57 | CostAllTransactionsVPEOProjectId | PROJECT_ID | — | — |
| 58 | CostAllTransactionsVPEOQuantity | QUANTITY | — | ✅ |
| 59 | CostAllTransactionsVPEORcvTransactionId | RCV_TRANSACTION_ID | — | — |
| 60 | CostAllTransactionsVPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | — |
| 61 | CostAllTransactionsVPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | — |
| 62 | CostAllTransactionsVPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | — |
| 63 | CostAllTransactionsVPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | — |
| 64 | CostAllTransactionsVPEOResourceId | RESOURCE_ID | — | — |
| 65 | CostAllTransactionsVPEORevenueLineId | REVENUE_LINE_ID | — | — |
| 66 | CostAllTransactionsVPEORmaTransactionId | RMA_TRANSACTION_ID | — | — |
| 67 | CostAllTransactionsVPEOSecondaryQty | SECONDARY_TRANSACTION_QTY | — | — |
| 68 | CostAllTransactionsVPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 69 | CostAllTransactionsVPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 70 | CostAllTransactionsVPEOShipmentFullfillLineId | SHIPMENT_FULLFILL_LINE_ID | — | — |
| 71 | CostAllTransactionsVPEOSourceTable | SOURCE_TABLE | — | — |
| 72 | CostAllTransactionsVPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 73 | CostAllTransactionsVPEOTaskId | TASK_ID | — | — |
| 74 | CostAllTransactionsVPEOToGradeCode | TO_GRADE_CODE | — | ✅ |
| 75 | CostAllTransactionsVPEOTransactionAmount | TRANSACTION_AMOUNT | — | — |
| 76 | CostAllTransactionsVPEOTransactionCurrencyCode | TRANSACTION_CURRENCY_CODE | — | — |
| 77 | CostAllTransactionsVPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 78 | CostAllTransactionsVPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 79 | CostAllTransactionsVPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 80 | CostAllTransactionsVPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 81 | CostAllTransactionsVPEOTransactionReasonId | TRANSACTION_REASON_ID | — | — |
| 82 | CostAllTransactionsVPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | — |
| 83 | CostAllTransactionsVPEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | — |
| 84 | CostAllTransactionsVPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | — |
| 85 | CostAllTransactionsVPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 86 | CostAllTransactionsVPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 87 | CostAllTransactionsVPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 88 | CostAllTransactionsVPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 89 | CostAllTransactionsVPEOUomCode | UOM_CODE | — | ✅ |
| 90 | CostAllTransactionsVPEOValUnitId | VAL_UNIT_ID | — | — |
| 91 | CostAllTransactionsVPEOVendorLotNumber | VENDOR_LOT_NUMBER | — | ✅ |
| 92 | CostAllTransactionsVPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | — |
| 93 | CostAllTransactionsVPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 94 | CostAllTransactionsVPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | — |

### [[cst_all_expense_pool_txns_v|CST_ALL_EXPENSE_POOL_TXNS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAllExpensePoolTxnsVPEOAbsorptionType | ABSORPTION_TYPE | — | — |
| 2 | CstAllExpensePoolTxnsVPEOCostDriver | COST_DRIVER | — | — |
| 3 | CstAllExpensePoolTxnsVPEOCostDriverValue | COST_DRIVER_VALUE | — | — |
| 4 | CstAllExpensePoolTxnsVPEOCostId | COST_ID | — | — |
| 5 | CstAllExpensePoolTxnsVPEOCostReference | COST_REFERENCE | — | ✅ |
| 6 | CstAllExpensePoolTxnsVPEOCostSource | COST_SOURCE | — | ✅ |
| 7 | CstAllExpensePoolTxnsVPEOEstimatedRate | ESTIMATED_RATE | — | — |
| 8 | CstAllExpensePoolTxnsVPEOExpensePoolId | EXPENSE_POOL_ID | — | — |
| 9 | CstAllExpensePoolTxnsVPEOOverheadId | OVERHEAD_ID | — | — |
| 10 | CstAllExpensePoolTxnsVPEORuleCode | RULE_CODE | — | — |
| 11 | CstAllExpensePoolTxnsVPEORuleDetailId | RULE_DETAIL_ID | — | — |
| 12 | CstAllExpensePoolTxnsVPEOSourceTable | SOURCE_TABLE | — | — |
| 13 | CstAllExpensePoolTxnsVPEOStdCostId | STD_COST_ID | — | — |
| 14 | CstAllExpensePoolTxnsVPEOTransactionCostId | TRANSACTION_COST_ID | — | — |
| 15 | CstAllExpensePoolTxnsVPEOTransactionId | TRANSACTION_ID | — | — |
| 16 | CstAllExpensePoolTxnsVPEOUnitCost | UNIT_COST | — | ✅ |

### [[cst_cost_distributions|CST_COST_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionsPEOAccountedFlag | ACCOUNTED_FLAG | — | — |
| 2 | CostDistributionsPEOAccountingPeriodName | ACCOUNTING_PERIOD_NAME | — | — |
| 3 | CostDistributionsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | — |
| 4 | CostDistributionsPEOBaseCurrencyCode | BASE_CURRENCY_CODE | — | ✅ |
| 5 | CostDistributionsPEOCostBookId | COST_BOOK_ID | — | — |
| 6 | CostDistributionsPEOCostOrganizationId | COST_ORGANIZATION_ID | — | — |
| 7 | CostDistributionsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | — |
| 8 | CostDistributionsPEOCostTransactionUom | COST_TRANSACTION_UOM | — | ✅ |
| 9 | CostDistributionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | CostDistributionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | CostDistributionsPEODepTrxnId | DEP_TRXN_ID | — | — |
| 12 | CostDistributionsPEODistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 13 | CostDistributionsPEOEffDate | EFF_DATE | — | — |
| 14 | CostDistributionsPEOEntityCode | ENTITY_CODE | — | — |
| 15 | CostDistributionsPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 16 | CostDistributionsPEOEventId | EVENT_ID | — | — |
| 17 | CostDistributionsPEOEventTypeCode | EVENT_TYPE_CODE | — | — |
| 18 | CostDistributionsPEOGlDate | GL_DATE | — | ✅ |
| 19 | CostDistributionsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 20 | CostDistributionsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 21 | CostDistributionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CostDistributionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CostDistributionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CostDistributionsPEOLayerQuantity | LAYER_QUANTITY | — | — |
| 25 | CostDistributionsPEOLedgerId | LEDGER_ID | — | — |
| 26 | CostDistributionsPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 27 | CostDistributionsPEOPeriodName | PERIOD_NAME | — | — |
| 28 | CostDistributionsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 29 | CostDistributionsPEORequestId | REQUEST_ID | — | — |
| 30 | CostDistributionsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 31 | CostDistributionsPEOTransactionNumber | TRANSACTION_NUMBER | — | ✅ |

### [[cst_cost_distribution_lines|CST_COST_DISTRIBUTION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostDistributionLinesPEOAccountingDefinitionId | ACCOUNTING_DEFINITION_ID | — | — |
| 2 | CostDistributionLinesPEOAccountingLineType | ACCOUNTING_LINE_TYPE | — | ✅ |
| 3 | CostDistributionLinesPEOAeHeaderId | AE_HEADER_ID | — | ✅ |
| 4 | CostDistributionLinesPEOAeLineNum | AE_LINE_NUM | — | — |
| 5 | CostDistributionLinesPEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 6 | CostDistributionLinesPEOCostElementId | COST_ELEMENT_ID | — | — |
| 7 | CostDistributionLinesPEOCostId | COST_ID | — | — |
| 8 | CostDistributionLinesPEOCreatedBy | CREATED_BY | — | — |
| 9 | CostDistributionLinesPEOCreationDate | CREATION_DATE | — | — |
| 10 | CostDistributionLinesPEODistributionId | DISTRIBUTION_ID | — | — |
| 11 | CostDistributionLinesPEODistributionLineId | DISTRIBUTION_LINE_ID | 🔑 | ✅ |
| 12 | CostDistributionLinesPEODrCrSign | DR_CR_SIGN | — | ✅ |
| 13 | CostDistributionLinesPEOEnteredCurrencyAmount | ENTERED_CURRENCY_AMOUNT | — | — |
| 14 | CostDistributionLinesPEOEnteredCurrencyCode | ENTERED_CURRENCY_CODE | — | ✅ |
| 15 | CostDistributionLinesPEOEventId | EVENT_ID | — | — |
| 16 | CostDistributionLinesPEOExchangeDate | EXCHANGE_DATE | — | — |
| 17 | CostDistributionLinesPEOExchangeRate | EXCHANGE_RATE | — | — |
| 18 | CostDistributionLinesPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 19 | CostDistributionLinesPEOGlDate | GL_DATE | — | — |
| 20 | CostDistributionLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CostDistributionLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | CostDistributionLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CostDistributionLinesPEOLedgerAmount | LEDGER_AMOUNT | — | — |
| 24 | CostDistributionLinesPEOLineNumber | LINE_NUMBER | — | — |
| 25 | CostDistributionLinesPEOPjcTxnStatusCode | PJC_TXN_STATUS_CODE | — | — |
| 26 | CostDistributionLinesPEOSlaCodeCombinationId | SLA_CODE_COMBINATION_ID | — | — |
| 27 | CostDistributionLinesPEOSourceTable | SOURCE_TABLE | — | — |
| 28 | CostDistributionLinesPEOTransactionCostId | TRANSACTION_COST_ID | — | — |

### [[cst_cost_orgs_v|CST_COST_ORGS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrganizationVPEOCostOrgId | COST_ORG_ID | — | — |
| 2 | CostOrganizationVPEOCostOrgName | COST_ORG_NAME | — | — |
| 3 | CostOrganizationVPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | CostOrganizationVPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | — |
| 2 | CostOrgBookPEOCdConversionType | CD_CONVERSION_TYPE | — | — |
| 3 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | — |
| 4 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | — |
| 5 | CostOrgBookPEOLedgerId | LEDGER_ID | — | — |
| 6 | CostOrgBookPEOUsdConversionType | USD_CONVERSION_TYPE | — | — |

### [[cst_inv_transactions|CST_INV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 2 | CstInvTransactionsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CstInvTransactionsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CstInvTransactionsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CstInvTransactionsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CstInvTransactionsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CstInvTransactionsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CstInvTransactionsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CstInvTransactionsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CstInvTransactionsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CstInvTransactionsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CstInvTransactionsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CstInvTransactionsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CstInvTransactionsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CstInvTransactionsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 16 | CstInvTransactionsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 17 | CstInvTransactionsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 18 | CstInvTransactionsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 19 | CstInvTransactionsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 20 | CstInvTransactionsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 21 | CstInvTransactionsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 22 | CstInvTransactionsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 23 | CstInvTransactionsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 24 | CstInvTransactionsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 25 | CstInvTransactionsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 26 | CstInvTransactionsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 27 | CstInvTransactionsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 28 | CstInvTransactionsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 29 | CstInvTransactionsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 30 | CstInvTransactionsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 31 | CstInvTransactionsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 32 | CstInvTransactionsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | 🔑 | ✅ |
| 33 | CstInvTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 34 | CstInvTransactionsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 35 | CstInvTransactionsPEOPriorBusinessUnitId | PRIOR_BUSINESS_UNIT_ID | — | — |
| 36 | CstInvTransactionsPEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | — |
| 37 | CstInvTransactionsPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 38 | CstInvTransactionsPEOSuccessorBusinessUnitId | SUCCESSOR_BUSINESS_UNIT_ID | — | — |
| 39 | CstInvTransactionsPEOSuccessorInventoryOrgId | SUCCESSOR_INVENTORY_ORG_ID | — | — |
| 40 | CstInvTransactionsPEOTransferInventoryOrgId | TRANSFER_INVENTORY_ORG_ID | — | — |
| 41 | CstInvTransactionsPEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | — |
| 42 | CstInvTransactionsPEOTransferSubinventoryCode | TRANSFER_SUBINVENTORY_CODE | — | — |
| 43 | CstInvTransactionsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |
| 44 | PJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 45 | PJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 46 | PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 47 | PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 48 | PJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 49 | PJC_RESERVED_ATTRIBUTE1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 50 | PJC_TASK_ID | PJC_TASK_ID | — | — |
| 51 | PJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 52 | ProjectId | PROJECT_ID | — | — |
| 53 | TaskId | TASK_ID | — | — |

### [[cst_trade_events|CST_TRADE_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TradeEventPEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 2 | TradeEventPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 3 | TradeEventPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | — |
| 4 | TradeEventPEOTradeEventId | TRADE_EVENT_ID | — | — |

### [[cst_txn_invoice_asc_v|CST_TXN_INVOICE_ASC_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceCMRDistPEOCmrApInvoiceDistId | CMR_AP_INVOICE_DIST_ID | — | — |
| 2 | InvoiceCMRDistPEOTransactionCostId | TRANSACTION_COST_ID | — | — |
| 3 | InvoiceCMRDistPEOTransactionId | TRANSACTION_ID | — | — |

### [[cst_work_orders|CST_WORK_ORDERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrderPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | — |
| 2 | CstWorkOrderPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | — |
| 3 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |

### [[doo_document_references|DOO_DOCUMENT_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentReferencesPEODeltaType | DELTA_TYPE | — | — |
| 2 | DocumentReferencesPEODocAltUserKey | DOC_ALT_USER_KEY | — | — |
| 3 | DocumentReferencesPEODocContextId | DOC_CONTEXT_ID | — | — |
| 4 | DocumentReferencesPEODocId | DOC_ID | — | — |
| 5 | DocumentReferencesPEODocLineAltUserKey | DOC_LINE_ALT_USER_KEY | — | — |
| 6 | DocumentReferencesPEODocLineContextId | DOC_LINE_CONTEXT_ID | — | — |
| 7 | DocumentReferencesPEODocLineId | DOC_LINE_ID | — | — |
| 8 | DocumentReferencesPEODocLineUserKey | DOC_LINE_USER_KEY | — | — |
| 9 | DocumentReferencesPEODocRefType | DOC_REF_TYPE | — | — |
| 10 | DocumentReferencesPEODocSublineAltUserKey | DOC_SUBLINE_ALT_USER_KEY | — | — |
| 11 | DocumentReferencesPEODocSublineContextId | DOC_SUBLINE_CONTEXT_ID | — | — |
| 12 | DocumentReferencesPEODocSublineId | DOC_SUBLINE_ID | — | — |
| 13 | DocumentReferencesPEODocSublineUserKey | DOC_SUBLINE_USER_KEY | — | — |
| 14 | DocumentReferencesPEODocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 15 | DocumentReferencesPEODocUserKey | DOC_USER_KEY | — | — |
| 16 | DocumentReferencesPEOFulfillLineId | FULFILL_LINE_ID | — | — |
| 17 | DocumentReferencesPEOHeaderId | HEADER_ID | — | — |
| 18 | DocumentReferencesPEOLineId | LINE_ID | — | — |
| 19 | DocumentReferencesPEOModifiedFlag | MODIFIED_FLAG | — | — |
| 20 | DocumentReferencesPEOOwnerTableId | OWNER_TABLE_ID | — | — |
| 21 | DocumentReferencesPEOOwnerTableName | OWNER_TABLE_NAME | — | — |
| 22 | DocumentReferencesPEOReferenceDocSystemRefId | REFERENCE_DOC_SYSTEM_REF_ID | — | — |
| 23 | DocumentReferencesPEOTaskType | TASK_TYPE | — | — |

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLinePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | FulfillLinePEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 3 | FulfillLinePEOActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 4 | FulfillLinePEOBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 5 | FulfillLinePEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 6 | FulfillLinePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 7 | FulfillLinePEOBillingTrxTypeId | BILLING_TRX_TYPE_ID | — | — |
| 8 | FulfillLinePEOCanceledFlag | CANCELED_FLAG | — | — |
| 9 | FulfillLinePEOCanceledQty | CANCELED_QTY | — | — |
| 10 | FulfillLinePEOCarrierId | CARRIER_ID | — | — |
| 11 | FulfillLinePEOCategoryCode | CATEGORY_CODE | — | — |
| 12 | FulfillLinePEOCompSeqPath | COMP_SEQ_PATH | — | — |
| 13 | FulfillLinePEOConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 14 | FulfillLinePEOCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 15 | FulfillLinePEOCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 16 | FulfillLinePEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 17 | FulfillLinePEODeltaType | DELTA_TYPE | — | — |
| 18 | FulfillLinePEODemandClassCode | DEMAND_CLASS_CODE | — | — |
| 19 | FulfillLinePEODestinationOrgId | DESTINATION_ORG_ID | — | — |
| 20 | FulfillLinePEOEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 21 | FulfillLinePEOEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 22 | FulfillLinePEOEstimateMargin | ESTIMATE_MARGIN | — | — |
| 23 | FulfillLinePEOExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 24 | FulfillLinePEOExtendedAmount | EXTENDED_AMOUNT | — | — |
| 25 | FulfillLinePEOFobPointCode | FOB_POINT_CODE | — | — |
| 26 | FulfillLinePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 27 | FulfillLinePEOFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 28 | FulfillLinePEOFulfillLineId | FULFILL_LINE_ID | — | — |
| 29 | FulfillLinePEOFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 30 | FulfillLinePEOFulfillOrgId | FULFILL_ORG_ID | — | — |
| 31 | FulfillLinePEOFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 32 | FulfillLinePEOFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 33 | FulfillLinePEOFulfilledQty | FULFILLED_QTY | — | — |
| 34 | FulfillLinePEOFulfillmentDate | FULFILLMENT_DATE | — | — |
| 35 | FulfillLinePEOFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 36 | FulfillLinePEOGopReferenceId | GOP_REFERENCE_ID | — | — |
| 37 | FulfillLinePEOHeaderId | HEADER_ID | — | — |
| 38 | FulfillLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 39 | FulfillLinePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 40 | FulfillLinePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 41 | FulfillLinePEOInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | — |
| 42 | FulfillLinePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 43 | FulfillLinePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 44 | FulfillLinePEOItemSubTypeCode | ITEM_SUB_TYPE_CODE | — | — |
| 45 | FulfillLinePEOItemTypeCode | ITEM_TYPE_CODE | — | — |
| 46 | FulfillLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | FulfillLinePEOLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 48 | FulfillLinePEOLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 49 | FulfillLinePEOLineId | LINE_ID | — | — |
| 50 | FulfillLinePEOLineTypeCode | LINE_TYPE_CODE | — | — |
| 51 | FulfillLinePEOOnHold | ON_HOLD | — | — |
| 52 | FulfillLinePEOOpenFlag | OPEN_FLAG | — | — |
| 53 | FulfillLinePEOOrderedQty | ORDERED_QTY | — | — |
| 54 | FulfillLinePEOOrderedUom | ORDERED_UOM | — | — |
| 55 | FulfillLinePEOOrgId | ORG_ID | — | — |
| 56 | FulfillLinePEOOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 57 | FulfillLinePEOOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 58 | FulfillLinePEOOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 59 | FulfillLinePEOOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 60 | FulfillLinePEOOwnerId | OWNER_ID | — | — |
| 61 | FulfillLinePEOPackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 62 | FulfillLinePEOParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 63 | FulfillLinePEOPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 64 | FulfillLinePEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 65 | FulfillLinePEOPromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 66 | FulfillLinePEOPromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 67 | FulfillLinePEOReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 68 | FulfillLinePEORemnantFlag | REMNANT_FLAG | — | — |
| 69 | FulfillLinePEORequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 70 | FulfillLinePEORequestShipDate | REQUEST_SHIP_DATE | — | — |
| 71 | FulfillLinePEORequestType | REQUEST_TYPE | — | — |
| 72 | FulfillLinePEOReservableFlag | RESERVABLE_FLAG | — | — |
| 73 | FulfillLinePEOReservationId | RESERVATION_ID | — | — |
| 74 | FulfillLinePEOReservedQty | RESERVED_QTY | — | — |
| 75 | FulfillLinePEOReturnReasonCode | RETURN_REASON_CODE | — | — |
| 76 | FulfillLinePEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 77 | FulfillLinePEORmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 78 | FulfillLinePEORootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 79 | FulfillLinePEOScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 80 | FulfillLinePEOScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 81 | FulfillLinePEOSchedulingReasonCode | SCHEDULING_REASON_CODE | — | — |
| 82 | FulfillLinePEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 83 | FulfillLinePEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 84 | FulfillLinePEOShipSetName | SHIP_SET_NAME | — | — |
| 85 | FulfillLinePEOShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 86 | FulfillLinePEOShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 87 | FulfillLinePEOShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 88 | FulfillLinePEOShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 89 | FulfillLinePEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 90 | FulfillLinePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 91 | FulfillLinePEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 92 | FulfillLinePEOShippableFlag | SHIPPABLE_FLAG | — | — |
| 93 | FulfillLinePEOShippedQty | SHIPPED_QTY | — | — |
| 94 | FulfillLinePEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 95 | FulfillLinePEOSourceLineId | SOURCE_LINE_ID | — | — |
| 96 | FulfillLinePEOSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 97 | FulfillLinePEOSourceOrderId | SOURCE_ORDER_ID | — | — |
| 98 | FulfillLinePEOSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 99 | FulfillLinePEOSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 100 | FulfillLinePEOSourceOrgId | SOURCE_ORG_ID | — | — |
| 101 | FulfillLinePEOSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | — |
| 102 | FulfillLinePEOSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 103 | FulfillLinePEOSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 104 | FulfillLinePEOSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 105 | FulfillLinePEOStatusCode | STATUS_CODE | — | — |
| 106 | FulfillLinePEOStatusRulesetId | STATUS_RULESET_ID | — | — |
| 107 | FulfillLinePEOSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 108 | FulfillLinePEOSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 109 | FulfillLinePEOSupplierId | SUPPLIER_ID | — | — |
| 110 | FulfillLinePEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 111 | FulfillLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 112 | FulfillLinePEOTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 113 | FulfillLinePEOTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 114 | FulfillLinePEOUnitListPrice | UNIT_LIST_PRICE | — | — |
| 115 | FulfillLinePEOUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderPEOCanceledFlag | CANCELED_FLAG | — | — |
| 2 | HeaderPEOChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 3 | HeaderPEOConversionDate | CONVERSION_DATE | — | — |
| 4 | HeaderPEOConversionRate | CONVERSION_RATE | — | — |
| 5 | HeaderPEOConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 6 | HeaderPEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 7 | HeaderPEOHeaderId | HEADER_ID | — | — |
| 8 | HeaderPEOIsEditable | IS_EDITABLE | — | — |
| 9 | HeaderPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 10 | HeaderPEOOnHold | ON_HOLD | — | — |
| 11 | HeaderPEOOpenFlag | OPEN_FLAG | — | — |
| 12 | HeaderPEOOrderNumber | ORDER_NUMBER | — | — |
| 13 | HeaderPEOOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 14 | HeaderPEOOrderedDate | ORDERED_DATE | — | — |
| 15 | HeaderPEOOrgId | ORG_ID | — | — |
| 16 | HeaderPEOOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 17 | HeaderPEOOwnerId | OWNER_ID | — | — |
| 18 | HeaderPEOPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 19 | HeaderPEOSalesChannelCode | SALES_CHANNEL_CODE | — | — |
| 20 | HeaderPEOSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 21 | HeaderPEOSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 22 | HeaderPEOSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 23 | HeaderPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 24 | HeaderPEOSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 25 | HeaderPEOSourceOrderId | SOURCE_ORDER_ID | — | — |
| 26 | HeaderPEOSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 27 | HeaderPEOSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 28 | HeaderPEOSourceOrgId | SOURCE_ORG_ID | — | — |
| 29 | HeaderPEOStatusCode | STATUS_CODE | — | — |
| 30 | HeaderPEOSubmittedFlag | SUBMITTED_FLAG | — | — |
| 31 | HeaderPEOTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinePEODisplayLineNumber | DISPLAY_LINE_NUMBER | — | — |
| 2 | LinePEOHeaderId | HEADER_ID | — | — |
| 3 | LinePEOLineId | LINE_ID | — | — |
| 4 | LinePEOLineNumber | LINE_NUMBER | — | — |
| 5 | LinePEOSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |

### [[doo_order_totals|DOO_ORDER_TOTALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTotalPEOHeaderId | HEADER_ID | — | — |
| 2 | OrderTotalPEOOrderTotalId | ORDER_TOTAL_ID | — | — |
| 3 | OrderTotalPEOTotalAmount | TOTAL_AMOUNT | — | — |
| 4 | OrderTotalPEOTotalCode | TOTAL_CODE | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 2 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TradingPartnerItemPEOTpType | TP_TYPE | — | — |
| 2 | TradingPartnerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 3 | TradingPartnerItemTpItemId | TP_ITEM_ID | — | — |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarPEOCalendarId | CALENDAR_ID | — | — |
| 2 | CalendarPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | CalendarPEOPeriodSetId | PERIOD_SET_ID | — | — |
| 4 | CalendarPEOPeriodSetName | PERIOD_SET_NAME | — | — |
| 5 | CalendarPEOPeriodType | PERIOD_TYPE | — | — |
| 6 | CalendarPEOPeriodTypeId | PERIOD_TYPE_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerPEOChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgerPEOLedgerId | LEDGER_ID | — | — |
| 3 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingDocumentHeaderPEOPoHeaderId | PO_HEADER_ID | — | — |
| 2 | PurchasingDocumentHeaderPEOPrcBuId | PRC_BU_ID | — | — |
| 3 | WorkOrderAnalyticsPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | RcvShipmentHeadersWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | — |
| 3 | ReceivingShipmentReceiptHeaderPEOFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 4 | ReceivingShipmentReceiptHeaderPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 5 | ReceivingShipmentReceiptHeaderPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RcvShipmentLinesAmount | AMOUNT | — | — |
| 3 | RcvShipmentLinesAmountReceived | AMOUNT_RECEIVED | — | — |
| 4 | RcvShipmentLinesAmountShipped | AMOUNT_SHIPPED | — | — |
| 5 | RcvShipmentLinesApprovalStatus | APPROVAL_STATUS | — | — |
| 6 | RcvShipmentLinesAsnLineFlag | ASN_LINE_FLAG | — | — |
| 7 | RcvShipmentLinesAsnLpnId | ASN_LPN_ID | — | — |
| 8 | RcvShipmentLinesAssessableValue | ASSESSABLE_VALUE | — | — |
| 9 | RcvShipmentLinesQuantityReceived | QUANTITY_RECEIVED | — | — |
| 10 | RcvShipmentLinesShipFromLocationId | SHIP_FROM_LOCATION_ID | — | — |
| 11 | RcvShipmentLinesShipmentLineId | SHIPMENT_LINE_ID | — | — |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 5 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | — |
| 6 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 7 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | — |
| 8 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 9 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 10 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 11 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 12 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 13 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 14 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 15 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 16 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 17 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 18 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 19 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 20 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 21 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 22 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 25 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 28 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 30 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 31 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 32 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 33 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 34 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 35 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 36 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 37 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 38 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | — |
| 39 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | — |
| 40 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 41 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 42 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 43 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 44 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 45 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 46 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 47 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 48 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 49 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 50 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 51 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 52 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 53 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 54 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 55 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 56 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 57 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 58 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 59 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 60 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 61 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 62 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[xla_cst_distribution_lines_vl|XLA_CST_DISTRIBUTION_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AeLineNum | AE_LINE_NUM | — | — |
| 2 | XlaCostDistributionLinesVPEOAeHeaderId | AE_HEADER_ID | — | — |
| 3 | XlaCostDistributionLinesVPEOAeLineNum | AE_LINE_NUM | — | — |
| 4 | XlaCostDistributionLinesVPEOGlBatchDesc | GL_BATCH_DESC | — | ✅ |
| 5 | XlaCostDistributionLinesVPEOGlBatchName | GL_BATCH_NAME | — | ✅ |
| 6 | XlaCostDistributionLinesVPEOGlBatchStatus | GL_BATCH_STATUS | — | ✅ |
| 7 | XlaCostDistributionLinesVPEOGlTransferDate | GL_TRANSFER_DATE | — | ✅ |
| 8 | XlaCostDistributionLinesVPEOGlTransferStatusCode | GL_TRANSFER_STATUS_CODE | — | ✅ |
| 9 | XlaCostDistributionLinesVPEOXlaAeHdrId | XLA_AE_HDR_ID | — | ✅ |

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | EventClassTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EventClassTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventClassTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventClassTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | EventClassTranslationPEOName | NAME | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EventTypeTranslationPEOEntityCode | ENTITY_CODE | — | — |
| 4 | EventTypeTranslationPEOEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventTypeTranslationPEOEventTypeCode | EVENT_TYPE_CODE | — | — |
| 6 | EventTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | EventTypeTranslationPEOName | NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
