---
id: DOC-OTHER-PVO-CmrRcvTransactionsExtractPVO
doc_type: system-doc
title: "CmrRcvTransactionsExtractPVO — PVO Cross-Module"
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
  - CmrRcvTransactionsExtractPVO
  - cmrrcvtransactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrRcvTransactionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Rcv Transactions Extract. Acessa as tabelas: CMR_RCV_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrRcvTransactionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 143 | 1 | 1 | 143 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]] — 143 atributos (1 PKs, 143 BICC)

---

## ⚙️ Atributos

### [[cmr_rcv_transactions|CMR_RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrRcvTransactionsPEOAllocatedFlag | ALLOCATED_FLAG | — | ✅ |
| 2 | CmrRcvTransactionsPEOAsnType | ASN_TYPE | — | ✅ |
| 3 | CmrRcvTransactionsPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 4 | CmrRcvTransactionsPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 5 | CmrRcvTransactionsPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 6 | CmrRcvTransactionsPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 7 | CmrRcvTransactionsPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 8 | CmrRcvTransactionsPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 9 | CmrRcvTransactionsPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 10 | CmrRcvTransactionsPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 11 | CmrRcvTransactionsPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 12 | CmrRcvTransactionsPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 13 | CmrRcvTransactionsPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 14 | CmrRcvTransactionsPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 15 | CmrRcvTransactionsPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 16 | CmrRcvTransactionsPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 17 | CmrRcvTransactionsPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 18 | CmrRcvTransactionsPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 19 | CmrRcvTransactionsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 20 | CmrRcvTransactionsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 21 | CmrRcvTransactionsPEOCmrPoDistributionId | CMR_PO_DISTRIBUTION_ID | — | ✅ |
| 22 | CmrRcvTransactionsPEOCmrPoLineLocationId | CMR_PO_LINE_LOCATION_ID | — | ✅ |
| 23 | CmrRcvTransactionsPEOCmrRcvTransactionId | CMR_RCV_TRANSACTION_ID | 🔑 | ✅ |
| 24 | CmrRcvTransactionsPEOCmrRootDeliverTxnId | CMR_ROOT_DELIVER_TXN_ID | — | ✅ |
| 25 | CmrRcvTransactionsPEOCmrRootReceiveTxnId | CMR_ROOT_RECEIVE_TXN_ID | — | ✅ |
| 26 | CmrRcvTransactionsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 27 | CmrRcvTransactionsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 28 | CmrRcvTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 29 | CmrRcvTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | CmrRcvTransactionsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 31 | CmrRcvTransactionsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 32 | CmrRcvTransactionsPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 33 | CmrRcvTransactionsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 34 | CmrRcvTransactionsPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 35 | CmrRcvTransactionsPEOErrorCode | ERROR_CODE | — | ✅ |
| 36 | CmrRcvTransactionsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 37 | CmrRcvTransactionsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 38 | CmrRcvTransactionsPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 39 | CmrRcvTransactionsPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 40 | CmrRcvTransactionsPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 41 | CmrRcvTransactionsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 42 | CmrRcvTransactionsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 43 | CmrRcvTransactionsPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 44 | CmrRcvTransactionsPEOFtrId | FTR_ID | — | ✅ |
| 45 | CmrRcvTransactionsPEOIntendedUse | INTENDED_USE | — | ✅ |
| 46 | CmrRcvTransactionsPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 47 | CmrRcvTransactionsPEOInterfaceBatchName | INTERFACE_BATCH_NAME | — | ✅ |
| 48 | CmrRcvTransactionsPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 49 | CmrRcvTransactionsPEOInvShippingTransactionId | INV_SHIPPING_TRANSACTION_ID | — | ✅ |
| 50 | CmrRcvTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 51 | CmrRcvTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | CmrRcvTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | CmrRcvTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | CmrRcvTransactionsPEOOrigTfOrdInvShipTxnId | ORIG_TF_ORD_INV_SHIP_TXN_ID | — | ✅ |
| 55 | CmrRcvTransactionsPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 56 | CmrRcvTransactionsPEOPhysicalReturnReqdFlag | PHYSICAL_RETURN_REQD_FLAG | — | ✅ |
| 57 | CmrRcvTransactionsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 58 | CmrRcvTransactionsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 59 | CmrRcvTransactionsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 60 | CmrRcvTransactionsPEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 61 | CmrRcvTransactionsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 62 | CmrRcvTransactionsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 63 | CmrRcvTransactionsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 64 | CmrRcvTransactionsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 65 | CmrRcvTransactionsPEOPjcInterfacedStatus | PJC_INTERFACED_STATUS | — | ✅ |
| 66 | CmrRcvTransactionsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 67 | CmrRcvTransactionsPEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 68 | CmrRcvTransactionsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 69 | CmrRcvTransactionsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 70 | CmrRcvTransactionsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 71 | CmrRcvTransactionsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 72 | CmrRcvTransactionsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 73 | CmrRcvTransactionsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 74 | CmrRcvTransactionsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 75 | CmrRcvTransactionsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 76 | CmrRcvTransactionsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 77 | CmrRcvTransactionsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 78 | CmrRcvTransactionsPEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 79 | CmrRcvTransactionsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 80 | CmrRcvTransactionsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 81 | CmrRcvTransactionsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 82 | CmrRcvTransactionsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 83 | CmrRcvTransactionsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 84 | CmrRcvTransactionsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 85 | CmrRcvTransactionsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 86 | CmrRcvTransactionsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 87 | CmrRcvTransactionsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 88 | CmrRcvTransactionsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 89 | CmrRcvTransactionsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 90 | CmrRcvTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 91 | CmrRcvTransactionsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 92 | CmrRcvTransactionsPEOPreprocessedStatus | PREPROCESSED_STATUS | — | ✅ |
| 93 | CmrRcvTransactionsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 94 | CmrRcvTransactionsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 95 | CmrRcvTransactionsPEOPriorTradeInvOrgId | PRIOR_TRADE_INV_ORG_ID | — | ✅ |
| 96 | CmrRcvTransactionsPEOProcessByCaFlag | PROCESS_BY_CA_FLAG | — | ✅ |
| 97 | CmrRcvTransactionsPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 98 | CmrRcvTransactionsPEOProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 99 | CmrRcvTransactionsPEOProductType | PRODUCT_TYPE | — | ✅ |
| 100 | CmrRcvTransactionsPEORcvParentTransactionId | RCV_PARENT_TRANSACTION_ID | — | ✅ |
| 101 | CmrRcvTransactionsPEORcvPoDistributionId | RCV_PO_DISTRIBUTION_ID | — | ✅ |
| 102 | CmrRcvTransactionsPEOReceiptCreationDate | RECEIPT_CREATION_DATE | — | ✅ |
| 103 | CmrRcvTransactionsPEOReceiptLineNumber | RECEIPT_LINE_NUMBER | — | ✅ |
| 104 | CmrRcvTransactionsPEOReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 105 | CmrRcvTransactionsPEOReceiptSourceCode | RECEIPT_SOURCE_CODE | — | ✅ |
| 106 | CmrRcvTransactionsPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 107 | CmrRcvTransactionsPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | ✅ |
| 108 | CmrRcvTransactionsPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | ✅ |
| 109 | CmrRcvTransactionsPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 110 | CmrRcvTransactionsPEORootDeliverTxnDate | ROOT_DELIVER_TXN_DATE | — | ✅ |
| 111 | CmrRcvTransactionsPEORootDeliverTxnId | ROOT_DELIVER_TXN_ID | — | ✅ |
| 112 | CmrRcvTransactionsPEORootReceiveTxnId | ROOT_RECEIVE_TXN_ID | — | ✅ |
| 113 | CmrRcvTransactionsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 114 | CmrRcvTransactionsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 115 | CmrRcvTransactionsPEOShipFromInvOrgId | SHIP_FROM_INV_ORG_ID | — | ✅ |
| 116 | CmrRcvTransactionsPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 117 | CmrRcvTransactionsPEOShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 118 | CmrRcvTransactionsPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 119 | CmrRcvTransactionsPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 120 | CmrRcvTransactionsPEOShipmentLineNumber | SHIPMENT_LINE_NUMBER | — | ✅ |
| 121 | CmrRcvTransactionsPEOShipmentNum | SHIPMENT_NUM | — | ✅ |
| 122 | CmrRcvTransactionsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 123 | CmrRcvTransactionsPEOSourceDocQuantity | SOURCE_DOC_QUANTITY | — | ✅ |
| 124 | CmrRcvTransactionsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 125 | CmrRcvTransactionsPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 126 | CmrRcvTransactionsPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 127 | CmrRcvTransactionsPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 128 | CmrRcvTransactionsPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 129 | CmrRcvTransactionsPEOTaxProcessedFlag | TAX_PROCESSED_FLAG | — | ✅ |
| 130 | CmrRcvTransactionsPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 131 | CmrRcvTransactionsPEOTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 132 | CmrRcvTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 133 | CmrRcvTransactionsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 134 | CmrRcvTransactionsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 135 | CmrRcvTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 136 | CmrRcvTransactionsPEOTransferOrderDistId | TRANSFER_ORDER_DIST_ID | — | ✅ |
| 137 | CmrRcvTransactionsPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 138 | CmrRcvTransactionsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 139 | CmrRcvTransactionsPEOTransferPriceQty | TRANSFER_PRICE_QTY | — | ✅ |
| 140 | CmrRcvTransactionsPEOTransferPriceUomCode | TRANSFER_PRICE_UOM_CODE | — | ✅ |
| 141 | CmrRcvTransactionsPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 142 | CmrRcvTransactionsPEOTxnGroupId | TXN_GROUP_ID | — | ✅ |
| 143 | CmrRcvTransactionsPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
