---
id: DOC-OTHER-PVO-CstInvTransactionsExtractPVO
doc_type: system-doc
title: "CstInvTransactionsExtractPVO — PVO Cross-Module"
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
  - CstInvTransactionsExtractPVO
  - cstinvtransactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInvTransactionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Inv Transactions Extract. Acessa as tabelas: CST_INV_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInvTransactionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 215 | 1 | 1 | 152 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[cst_inv_transactions|CST_INV_TRANSACTIONS]] — 215 atributos (1 PKs, 152 BICC)

---

## ⚙️ Atributos

### [[cst_inv_transactions|CST_INV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInvTransactionsPEOAddnTxnCreatedFlag | ADDN_TXN_CREATED_FLAG | — | ✅ |
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
| 32 | CstInvTransactionsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | CstInvTransactionsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 34 | CstInvTransactionsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 35 | CstInvTransactionsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 36 | CstInvTransactionsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 37 | CstInvTransactionsPEOCallbackFlag | CALLBACK_FLAG | — | ✅ |
| 38 | CstInvTransactionsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 39 | CstInvTransactionsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 40 | CstInvTransactionsPEOConsumptionUnitPrice | CONSUMPTION_UNIT_PRICE | — | ✅ |
| 41 | CstInvTransactionsPEOContingentOwnerId | CONTINGENT_OWNER_ID | — | ✅ |
| 42 | CstInvTransactionsPEOContingentOwnerType | CONTINGENT_OWNER_TYPE | — | ✅ |
| 43 | CstInvTransactionsPEOCostPreprocessingStatus | COST_PREPROCESSING_STATUS | — | ✅ |
| 44 | CstInvTransactionsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 45 | CstInvTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | CstInvTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | CstInvTransactionsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | 🔑 | ✅ |
| 48 | CstInvTransactionsPEOCstTransferOrderDistId | CST_TRANSFER_ORDER_DIST_ID | — | ✅ |
| 49 | CstInvTransactionsPEOCstTransferOrderLineId | CST_TRANSFER_ORDER_LINE_ID | — | ✅ |
| 50 | CstInvTransactionsPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | ✅ |
| 51 | CstInvTransactionsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 52 | CstInvTransactionsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 53 | CstInvTransactionsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 54 | CstInvTransactionsPEOCustodyInventoryOrgId | CUSTODY_INVENTORY_ORG_ID | — | ✅ |
| 55 | CstInvTransactionsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 56 | CstInvTransactionsPEODooSplitFulfillLineId | DOO_SPLIT_FULFILL_LINE_ID | — | ✅ |
| 57 | CstInvTransactionsPEODsSourceLineId | DS_SOURCE_LINE_ID | — | ✅ |
| 58 | CstInvTransactionsPEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | ✅ |
| 59 | CstInvTransactionsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 60 | CstInvTransactionsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 61 | CstInvTransactionsPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 62 | CstInvTransactionsPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 63 | CstInvTransactionsPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 64 | CstInvTransactionsPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 65 | CstInvTransactionsPEOFobPoint | FOB_POINT | — | ✅ |
| 66 | CstInvTransactionsPEOFromGradeCode | FROM_GRADE_CODE | — | ✅ |
| 67 | CstInvTransactionsPEOIntercompanyInvoicingFlag | INTERCOMPANY_INVOICING_FLAG | — | ✅ |
| 68 | CstInvTransactionsPEOInterfaceBatchName | INTERFACE_BATCH_NAME | — | ✅ |
| 69 | CstInvTransactionsPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 70 | CstInvTransactionsPEOInternalProfitTracking | INTERNAL_PROFIT_TRACKING | — | ✅ |
| 71 | CstInvTransactionsPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 72 | CstInvTransactionsPEOInvStripingCategory | INV_STRIPING_CATEGORY | — | ✅ |
| 73 | CstInvTransactionsPEOInvTransferOrderDistId | INV_TRANSFER_ORDER_DIST_ID | — | ✅ |
| 74 | CstInvTransactionsPEOInvTransferOrderHeaderId | INV_TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 75 | CstInvTransactionsPEOInvTransferOrderLineId | INV_TRANSFER_ORDER_LINE_ID | — | ✅ |
| 76 | CstInvTransactionsPEOInvTxnSourceTypeId | INV_TXN_SOURCE_TYPE_ID | — | ✅ |
| 77 | CstInvTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 78 | CstInvTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 79 | CstInvTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 80 | CstInvTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 81 | CstInvTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 82 | CstInvTransactionsPEOLoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 83 | CstInvTransactionsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 84 | CstInvTransactionsPEOManualReceiptReqdFlag | MANUAL_RECEIPT_REQD_FLAG | — | ✅ |
| 85 | CstInvTransactionsPEOOrigTransferInventoryOrgId | ORIG_TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 86 | CstInvTransactionsPEOOriginalReceiptInvOrgId | ORIGINAL_RECEIPT_INV_ORG_ID | — | ✅ |
| 87 | CstInvTransactionsPEOOriginalReceiptNumber | ORIGINAL_RECEIPT_NUMBER | — | ✅ |
| 88 | CstInvTransactionsPEOOriginalReceiptTxnId | ORIGINAL_RECEIPT_TXN_ID | — | ✅ |
| 89 | CstInvTransactionsPEOOriginalToShipmentTxnId | ORIGINAL_TO_SHIPMENT_TXN_ID | — | ✅ |
| 90 | CstInvTransactionsPEOOriginalTransactionTempId | ORIGINAL_TRANSACTION_TEMP_ID | — | ✅ |
| 91 | CstInvTransactionsPEOOwnerName | OWNER_NAME | — | ✅ |
| 92 | CstInvTransactionsPEOOwnerType | OWNER_TYPE | — | ✅ |
| 93 | CstInvTransactionsPEOOwningEntityId | OWNING_ENTITY_ID | — | ✅ |
| 94 | CstInvTransactionsPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 95 | CstInvTransactionsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 96 | CstInvTransactionsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 97 | CstInvTransactionsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 98 | CstInvTransactionsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 99 | CstInvTransactionsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 100 | CstInvTransactionsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 101 | CstInvTransactionsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 102 | CstInvTransactionsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 103 | CstInvTransactionsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 104 | CstInvTransactionsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 105 | CstInvTransactionsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 106 | CstInvTransactionsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 107 | CstInvTransactionsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 108 | CstInvTransactionsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 109 | CstInvTransactionsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 110 | CstInvTransactionsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 111 | CstInvTransactionsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 112 | CstInvTransactionsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 113 | CstInvTransactionsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 114 | CstInvTransactionsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 115 | CstInvTransactionsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 116 | CstInvTransactionsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 117 | CstInvTransactionsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 118 | CstInvTransactionsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 119 | CstInvTransactionsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 120 | CstInvTransactionsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 121 | CstInvTransactionsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 122 | CstInvTransactionsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 123 | CstInvTransactionsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 124 | CstInvTransactionsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 125 | CstInvTransactionsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 126 | CstInvTransactionsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 127 | CstInvTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 128 | CstInvTransactionsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | ✅ |
| 129 | CstInvTransactionsPEOPoItemDescriptionType | PO_ITEM_DESCRIPTION_TYPE | — | ✅ |
| 130 | CstInvTransactionsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 131 | CstInvTransactionsPEOPricingOption | PRICING_OPTION | — | ✅ |
| 132 | CstInvTransactionsPEOPrimaryProductFlag | PRIMARY_PRODUCT_FLAG | — | ✅ |
| 133 | CstInvTransactionsPEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 134 | CstInvTransactionsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 135 | CstInvTransactionsPEOPriorBusinessUnitId | PRIOR_BUSINESS_UNIT_ID | — | ✅ |
| 136 | CstInvTransactionsPEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | ✅ |
| 137 | CstInvTransactionsPEOProjectId | PROJECT_ID | — | ✅ |
| 138 | CstInvTransactionsPEOQppTxnGroupsUpdatedFlag | QPP_TXN_GROUPS_UPDATED_FLAG | — | ✅ |
| 139 | CstInvTransactionsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 140 | CstInvTransactionsPEORecallHeaderId | RECALL_HEADER_ID | — | ✅ |
| 141 | CstInvTransactionsPEORecallLineId | RECALL_LINE_ID | — | ✅ |
| 142 | CstInvTransactionsPEOReceiptAdviceLineNumber | RECEIPT_ADVICE_LINE_NUMBER | — | ✅ |
| 143 | CstInvTransactionsPEOReceiptAdviceNumber | RECEIPT_ADVICE_NUMBER | — | ✅ |
| 144 | CstInvTransactionsPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 145 | CstInvTransactionsPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | ✅ |
| 146 | CstInvTransactionsPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | ✅ |
| 147 | CstInvTransactionsPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 148 | CstInvTransactionsPEOReferenceDeliveryId | REFERENCE_DELIVERY_ID | — | ✅ |
| 149 | CstInvTransactionsPEOReferenceDooFullfillLineId | REFERENCE_DOO_FULLFILL_LINE_ID | — | ✅ |
| 150 | CstInvTransactionsPEOReferencedReturnFlag | REFERENCED_RETURN_FLAG | — | ✅ |
| 151 | CstInvTransactionsPEOReferencedSoLineNumber | REFERENCED_SO_LINE_NUMBER | — | ✅ |
| 152 | CstInvTransactionsPEOReferencedSoNumber | REFERENCED_SO_NUMBER | — | ✅ |
| 153 | CstInvTransactionsPEOReturnBuId | RETURN_BU_ID | — | ✅ |
| 154 | CstInvTransactionsPEOReturnInvOrgId | RETURN_INV_ORG_ID | — | ✅ |
| 155 | CstInvTransactionsPEOSalesOrderSourceSystem | SALES_ORDER_SOURCE_SYSTEM | — | ✅ |
| 156 | CstInvTransactionsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 157 | CstInvTransactionsPEOSecondaryTransactionUomCode | SECONDARY_TRANSACTION_UOM_CODE | — | ✅ |
| 158 | CstInvTransactionsPEOShippingBuId | SHIPPING_BU_ID | — | ✅ |
| 159 | CstInvTransactionsPEOShippingInvOrgId | SHIPPING_INV_ORG_ID | — | ✅ |
| 160 | CstInvTransactionsPEOSimpleProcFlag | SIMPLE_PROC_FLAG | — | ✅ |
| 161 | CstInvTransactionsPEOSourceSalesOrderLineNumber | SOURCE_SALES_ORDER_LINE_NUMBER | — | ✅ |
| 162 | CstInvTransactionsPEOSourceSalesOrderNumber | SOURCE_SALES_ORDER_NUMBER | — | ✅ |
| 163 | CstInvTransactionsPEOSourceSoShipmentNumber | SOURCE_SO_SHIPMENT_NUMBER | — | ✅ |
| 164 | CstInvTransactionsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 165 | CstInvTransactionsPEOSuccessorBusinessUnitId | SUCCESSOR_BUSINESS_UNIT_ID | — | ✅ |
| 166 | CstInvTransactionsPEOSuccessorInventoryOrgId | SUCCESSOR_INVENTORY_ORG_ID | — | ✅ |
| 167 | CstInvTransactionsPEOSupplierReturnHeaderId | SUPPLIER_RETURN_HEADER_ID | — | ✅ |
| 168 | CstInvTransactionsPEOSupplierReturnLineId | SUPPLIER_RETURN_LINE_ID | — | ✅ |
| 169 | CstInvTransactionsPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 170 | CstInvTransactionsPEOTaskId | TASK_ID | — | ✅ |
| 171 | CstInvTransactionsPEOToGradeCode | TO_GRADE_CODE | — | ✅ |
| 172 | CstInvTransactionsPEOTradeAgreementFtrId | TRADE_AGREEMENT_FTR_ID | — | ✅ |
| 173 | CstInvTransactionsPEOTradeAgreementNumber | TRADE_AGREEMENT_NUMBER | — | ✅ |
| 174 | CstInvTransactionsPEOTradeAgreementPtrId | TRADE_AGREEMENT_PTR_ID | — | ✅ |
| 175 | CstInvTransactionsPEOTradeAgreementType | TRADE_AGREEMENT_TYPE | — | ✅ |
| 176 | CstInvTransactionsPEOTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 177 | CstInvTransactionsPEOTransactionCreationDate | TRANSACTION_CREATION_DATE | — | ✅ |
| 178 | CstInvTransactionsPEOTransactionCurrencyCode | TRANSACTION_CURRENCY_CODE | — | ✅ |
| 179 | CstInvTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 180 | CstInvTransactionsPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 181 | CstInvTransactionsPEOTransactionGroupId | TRANSACTION_GROUP_ID | — | ✅ |
| 182 | CstInvTransactionsPEOTransactionInterfaceId | TRANSACTION_INTERFACE_ID | — | ✅ |
| 183 | CstInvTransactionsPEOTransactionInterfaceLineNum | TRANSACTION_INTERFACE_LINE_NUM | — | ✅ |
| 184 | CstInvTransactionsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 185 | CstInvTransactionsPEOTransactionReasonId | TRANSACTION_REASON_ID | — | ✅ |
| 186 | CstInvTransactionsPEOTransactionTempId | TRANSACTION_TEMP_ID | — | ✅ |
| 187 | CstInvTransactionsPEOTransactionTimezoneCode | TRANSACTION_TIMEZONE_CODE | — | ✅ |
| 188 | CstInvTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 189 | CstInvTransactionsPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | ✅ |
| 190 | CstInvTransactionsPEOTransferInventoryOrgId | TRANSFER_INVENTORY_ORG_ID | — | ✅ |
| 191 | CstInvTransactionsPEOTransferLinkedFlag | TRANSFER_LINKED_FLAG | — | ✅ |
| 192 | CstInvTransactionsPEOTransferLocatorId | TRANSFER_LOCATOR_ID | — | ✅ |
| 193 | CstInvTransactionsPEOTransferOrderDistributionId | TRANSFER_ORDER_DISTRIBUTION_ID | — | ✅ |
| 194 | CstInvTransactionsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 195 | CstInvTransactionsPEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 196 | CstInvTransactionsPEOTransferProjectId | TRANSFER_PROJECT_ID | — | ✅ |
| 197 | CstInvTransactionsPEOTransferSubinventoryCode | TRANSFER_SUBINVENTORY_CODE | — | ✅ |
| 198 | CstInvTransactionsPEOTransferTaskId | TRANSFER_TASK_ID | — | ✅ |
| 199 | CstInvTransactionsPEOTransferToRegularTxnId | TRANSFER_TO_REGULAR_TXN_ID | — | ✅ |
| 200 | CstInvTransactionsPEOTransferTransactionGroupId | TRANSFER_TRANSACTION_GROUP_ID | — | ✅ |
| 201 | CstInvTransactionsPEOTransferTransactionId | TRANSFER_TRANSACTION_ID | — | ✅ |
| 202 | CstInvTransactionsPEOTxnChainedFlag | TXN_CHAINED_FLAG | — | ✅ |
| 203 | CstInvTransactionsPEOTxnGroupId | TXN_GROUP_ID | — | ✅ |
| 204 | CstInvTransactionsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 205 | CstInvTransactionsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 206 | CstInvTransactionsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 207 | CstInvTransactionsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 208 | CstInvTransactionsPEOWmsFlag | WMS_FLAG | — | ✅ |
| 209 | CstInvTransactionsPEOWoCostAllocationBasis | WO_COST_ALLOCATION_BASIS | — | ✅ |
| 210 | CstInvTransactionsPEOWoOperationTransactionId | WO_OPERATION_TRANSACTION_ID | — | ✅ |
| 211 | CstInvTransactionsPEOWoOutputType | WO_OUTPUT_TYPE | — | ✅ |
| 212 | CstInvTransactionsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 213 | CstInvTransactionsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 214 | CstInvTransactionsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |
| 215 | CstInvTransactionsPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
