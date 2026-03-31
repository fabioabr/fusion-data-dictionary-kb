---
id: DOC-OTHER-PVO-CmrTransactionsExtractPVO
doc_type: system-doc
title: "CmrTransactionsExtractPVO — PVO Cross-Module"
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
  - CmrTransactionsExtractPVO
  - cmrtransactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTransactionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Transactions Extract. Acessa as tabelas: CMR_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTransactionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 1 | 1 | 104 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_transactions|CMR_TRANSACTIONS]] — 104 atributos (1 PKs, 104 BICC)

---

## ⚙️ Atributos

### [[cmr_transactions|CMR_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTransactionsPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 2 | CmrTransactionsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 3 | CmrTransactionsPEOBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | ✅ |
| 4 | CmrTransactionsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 5 | CmrTransactionsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 6 | CmrTransactionsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | — | ✅ |
| 7 | CmrTransactionsPEOCmrRootDeliverTxnId | CMR_ROOT_DELIVER_TXN_ID | — | ✅ |
| 8 | CmrTransactionsPEOCmrRootReceiveTxnId | CMR_ROOT_RECEIVE_TXN_ID | — | ✅ |
| 9 | CmrTransactionsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 10 | CmrTransactionsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 11 | CmrTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CmrTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CmrTransactionsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 14 | CmrTransactionsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 15 | CmrTransactionsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 16 | CmrTransactionsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 17 | CmrTransactionsPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 18 | CmrTransactionsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 19 | CmrTransactionsPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 20 | CmrTransactionsPEODsReceiptSourceLineId | DS_RECEIPT_SOURCE_LINE_ID | — | ✅ |
| 21 | CmrTransactionsPEOEncumbranceAccountingFlag | ENCUMBRANCE_ACCOUNTING_FLAG | — | ✅ |
| 22 | CmrTransactionsPEOErrorCode | ERROR_CODE | — | ✅ |
| 23 | CmrTransactionsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 24 | CmrTransactionsPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 25 | CmrTransactionsPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 26 | CmrTransactionsPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 27 | CmrTransactionsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 28 | CmrTransactionsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 29 | CmrTransactionsPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 30 | CmrTransactionsPEOFtrId | FTR_ID | — | ✅ |
| 31 | CmrTransactionsPEOIntendedUse | INTENDED_USE | — | ✅ |
| 32 | CmrTransactionsPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 33 | CmrTransactionsPEOInvShippingTransactionId | INV_SHIPPING_TRANSACTION_ID | — | ✅ |
| 34 | CmrTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 35 | CmrTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | CmrTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | CmrTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | CmrTransactionsPEOLcmProcessedFlag | LCM_PROCESSED_FLAG | — | ✅ |
| 39 | CmrTransactionsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 40 | CmrTransactionsPEOLiquidatedAmount | LIQUIDATED_AMOUNT | — | ✅ |
| 41 | CmrTransactionsPEOLiquidatedQty | LIQUIDATED_QTY | — | ✅ |
| 42 | CmrTransactionsPEOManualReceiptReqdFlag | MANUAL_RECEIPT_REQD_FLAG | — | ✅ |
| 43 | CmrTransactionsPEONonrecoverableTax | NONRECOVERABLE_TAX | — | ✅ |
| 44 | CmrTransactionsPEOOwnershipChangeEventNumber | OWNERSHIP_CHANGE_EVENT_NUMBER | — | ✅ |
| 45 | CmrTransactionsPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 46 | CmrTransactionsPEOPhysicalReturnReqdFlag | PHYSICAL_RETURN_REQD_FLAG | — | ✅ |
| 47 | CmrTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 48 | CmrTransactionsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 49 | CmrTransactionsPEOPoUnitPrice | PO_UNIT_PRICE | — | ✅ |
| 50 | CmrTransactionsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 51 | CmrTransactionsPEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 52 | CmrTransactionsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 53 | CmrTransactionsPEOPriorTradeInvOrgId | PRIOR_TRADE_INV_ORG_ID | — | ✅ |
| 54 | CmrTransactionsPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 55 | CmrTransactionsPEOProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 56 | CmrTransactionsPEOProductType | PRODUCT_TYPE | — | ✅ |
| 57 | CmrTransactionsPEOProfitCenterBusinessUnitId | PROFIT_CENTER_BUSINESS_UNIT_ID | — | ✅ |
| 58 | CmrTransactionsPEOProjectFlag | PROJECT_FLAG | — | ✅ |
| 59 | CmrTransactionsPEORcvParentTransactionId | RCV_PARENT_TRANSACTION_ID | — | ✅ |
| 60 | CmrTransactionsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 61 | CmrTransactionsPEOReceiptCreationDate | RECEIPT_CREATION_DATE | — | ✅ |
| 62 | CmrTransactionsPEOReceiptLineNumber | RECEIPT_LINE_NUMBER | — | ✅ |
| 63 | CmrTransactionsPEOReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 64 | CmrTransactionsPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 65 | CmrTransactionsPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | ✅ |
| 66 | CmrTransactionsPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | ✅ |
| 67 | CmrTransactionsPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 68 | CmrTransactionsPEORootDeliverTxnDate | ROOT_DELIVER_TXN_DATE | — | ✅ |
| 69 | CmrTransactionsPEORootReceiptEventDate | ROOT_RECEIPT_EVENT_DATE | — | ✅ |
| 70 | CmrTransactionsPEORootReceiveTxnId | ROOT_RECEIVE_TXN_ID | — | ✅ |
| 71 | CmrTransactionsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 72 | CmrTransactionsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 73 | CmrTransactionsPEOShipFromInvOrgId | SHIP_FROM_INV_ORG_ID | — | ✅ |
| 74 | CmrTransactionsPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 75 | CmrTransactionsPEOShipToBusinessUnitId | SHIP_TO_BUSINESS_UNIT_ID | — | ✅ |
| 76 | CmrTransactionsPEOShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 77 | CmrTransactionsPEOShipmentLineNumber | SHIPMENT_LINE_NUMBER | — | ✅ |
| 78 | CmrTransactionsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 79 | CmrTransactionsPEOSoldToBusinessUnitId | SOLD_TO_BUSINESS_UNIT_ID | — | ✅ |
| 80 | CmrTransactionsPEOSourceDocQty | SOURCE_DOC_QTY | — | ✅ |
| 81 | CmrTransactionsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 82 | CmrTransactionsPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 83 | CmrTransactionsPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 84 | CmrTransactionsPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 85 | CmrTransactionsPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 86 | CmrTransactionsPEOTaxProcessedFlag | TAX_PROCESSED_FLAG | — | ✅ |
| 87 | CmrTransactionsPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 88 | CmrTransactionsPEOTradeEventId | TRADE_EVENT_ID | — | ✅ |
| 89 | CmrTransactionsPEOTransactionAmt | TRANSACTION_AMT | — | ✅ |
| 90 | CmrTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 91 | CmrTransactionsPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 92 | CmrTransactionsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 93 | CmrTransactionsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 94 | CmrTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 95 | CmrTransactionsPEOTransferOrderDistId | TRANSFER_ORDER_DIST_ID | — | ✅ |
| 96 | CmrTransactionsPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 97 | CmrTransactionsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 98 | CmrTransactionsPEOTransferPriceQty | TRANSFER_PRICE_QTY | — | ✅ |
| 99 | CmrTransactionsPEOTransferPriceUomCode | TRANSFER_PRICE_UOM_CODE | — | ✅ |
| 100 | CmrTransactionsPEOTransferToOwnedTxnId | TRANSFER_TO_OWNED_TXN_ID | — | ✅ |
| 101 | CmrTransactionsPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 102 | CmrTransactionsPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 103 | CmrTransactionsPEOXccNetLiquidationAmount | XCC_NET_LIQUIDATION_AMOUNT | — | ✅ |
| 104 | CmrTransactionsPEOXccNetLiquidationQty | XCC_NET_LIQUIDATION_QTY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
