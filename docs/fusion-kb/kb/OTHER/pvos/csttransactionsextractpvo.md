---
id: DOC-OTHER-PVO-CstTransactionsExtractPVO
doc_type: system-doc
title: "CstTransactionsExtractPVO — PVO Cross-Module"
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
  - CstTransactionsExtractPVO
  - csttransactionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransactionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transactions Extract. Acessa as tabelas: CST_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransactionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 115 | 1 | 1 | 115 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_transactions|CST_TRANSACTIONS]] — 115 atributos (1 PKs, 115 BICC)

---

## ⚙️ Atributos

### [[cst_transactions|CST_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransactionsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstTransactionsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstTransactionsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 4 | CstTransactionsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 5 | CstTransactionsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 6 | CstTransactionsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 7 | CstTransactionsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 8 | CstTransactionsPEOCogsPostedFlag | COGS_POSTED_FLAG | — | ✅ |
| 9 | CstTransactionsPEOConsignedAcctDistBasis | CONSIGNED_ACCT_DIST_BASIS | — | ✅ |
| 10 | CstTransactionsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 11 | CstTransactionsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 12 | CstTransactionsPEOCostDate | COST_DATE | — | ✅ |
| 13 | CstTransactionsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 14 | CstTransactionsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 15 | CstTransactionsPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 16 | CstTransactionsPEOCostStatus | COST_STATUS | — | ✅ |
| 17 | CstTransactionsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 18 | CstTransactionsPEOCostedQty | COSTED_QTY | — | ✅ |
| 19 | CstTransactionsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 20 | CstTransactionsPEOCostingUomCode | COSTING_UOM_CODE | — | ✅ |
| 21 | CstTransactionsPEOCreateAcctForConsTxns | CREATE_ACCT_FOR_CONS_TXNS | — | ✅ |
| 22 | CstTransactionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 23 | CstTransactionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 24 | CstTransactionsPEOCstInvTransactionDtlId | CST_INV_TRANSACTION_DTL_ID | — | ✅ |
| 25 | CstTransactionsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 26 | CstTransactionsPEOCstTransferOrderDistId | CST_TRANSFER_ORDER_DIST_ID | — | ✅ |
| 27 | CstTransactionsPEOCstTransferOrderLineId | CST_TRANSFER_ORDER_LINE_ID | — | ✅ |
| 28 | CstTransactionsPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | ✅ |
| 29 | CstTransactionsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 30 | CstTransactionsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 31 | CstTransactionsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 32 | CstTransactionsPEODooSplitFulfillLineId | DOO_SPLIT_FULFILL_LINE_ID | — | ✅ |
| 33 | CstTransactionsPEODsSourceLineId | DS_SOURCE_LINE_ID | — | ✅ |
| 34 | CstTransactionsPEOEnforceTxnDateOrderFlag | ENFORCE_TXN_DATE_ORDER_FLAG | — | ✅ |
| 35 | CstTransactionsPEOErrorCode | ERROR_CODE | — | ✅ |
| 36 | CstTransactionsPEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | ✅ |
| 37 | CstTransactionsPEOFobPoint | FOB_POINT | — | ✅ |
| 38 | CstTransactionsPEOIntercompanyInvoicingFlag | INTERCOMPANY_INVOICING_FLAG | — | ✅ |
| 39 | CstTransactionsPEOInternalProfitTracking | INTERNAL_PROFIT_TRACKING | — | ✅ |
| 40 | CstTransactionsPEOIntransitFlag | INTRANSIT_FLAG | — | ✅ |
| 41 | CstTransactionsPEOInvTxnSourceTypeId | INV_TXN_SOURCE_TYPE_ID | — | ✅ |
| 42 | CstTransactionsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 43 | CstTransactionsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 44 | CstTransactionsPEOItemCostProfileId | ITEM_COST_PROFILE_ID | — | ✅ |
| 45 | CstTransactionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | CstTransactionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | CstTransactionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | CstTransactionsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 49 | CstTransactionsPEOLogicalFlag | LOGICAL_FLAG | — | ✅ |
| 50 | CstTransactionsPEOManualReceiptReqdFlag | MANUAL_RECEIPT_REQD_FLAG | — | ✅ |
| 51 | CstTransactionsPEOMatchedToAddlTaxFlag | MATCHED_TO_ADDL_TAX_FLAG | — | ✅ |
| 52 | CstTransactionsPEOMatchedToCostFlag | MATCHED_TO_COST_FLAG | — | ✅ |
| 53 | CstTransactionsPEONegativeQtyCode | NEGATIVE_QTY_CODE | — | ✅ |
| 54 | CstTransactionsPEOOperationScrapCostType | OPERATION_SCRAP_COST_TYPE | — | ✅ |
| 55 | CstTransactionsPEOOwningCostOrgId | OWNING_COST_ORG_ID | — | ✅ |
| 56 | CstTransactionsPEOPartialCompletionFlag | PARTIAL_COMPLETION_FLAG | — | ✅ |
| 57 | CstTransactionsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 58 | CstTransactionsPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 59 | CstTransactionsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | ✅ |
| 60 | CstTransactionsPEOPoItemDescriptionType | PO_ITEM_DESCRIPTION_TYPE | — | ✅ |
| 61 | CstTransactionsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 62 | CstTransactionsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 63 | CstTransactionsPEOPricingOption | PRICING_OPTION | — | ✅ |
| 64 | CstTransactionsPEOProcessDate | PROCESS_DATE | — | ✅ |
| 65 | CstTransactionsPEOProjectFlag | PROJECT_FLAG | — | ✅ |
| 66 | CstTransactionsPEOPropagateCostAdjFlag | PROPAGATE_COST_ADJ_FLAG | — | ✅ |
| 67 | CstTransactionsPEOProvisionalCompletionType | PROVISIONAL_COMPLETION_TYPE | — | ✅ |
| 68 | CstTransactionsPEOQuantity | QUANTITY | — | ✅ |
| 69 | CstTransactionsPEOQuantityDepleted | QUANTITY_DEPLETED | — | ✅ |
| 70 | CstTransactionsPEOQuantityFlowCode | QUANTITY_FLOW_CODE | — | ✅ |
| 71 | CstTransactionsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 72 | CstTransactionsPEORecOnhandAvailFlag | REC_ONHAND_AVAIL_FLAG | — | ✅ |
| 73 | CstTransactionsPEOReceiptWithoutCostCode | RECEIPT_WITHOUT_COST_CODE | — | ✅ |
| 74 | CstTransactionsPEOReferenceDeliveryId | REFERENCE_DELIVERY_ID | — | ✅ |
| 75 | CstTransactionsPEOReferenceDooFullfillLineId | REFERENCE_DOO_FULLFILL_LINE_ID | — | ✅ |
| 76 | CstTransactionsPEOReferencedReturnFlag | REFERENCED_RETURN_FLAG | — | ✅ |
| 77 | CstTransactionsPEOReferencedRmaCostCode | REFERENCED_RMA_COST_CODE | — | ✅ |
| 78 | CstTransactionsPEORunMode | RUN_MODE | — | ✅ |
| 79 | CstTransactionsPEOSimpleProcFlag | SIMPLE_PROC_FLAG | — | ✅ |
| 80 | CstTransactionsPEOStagedForTxfrCostFlag | STAGED_FOR_TXFR_COST_FLAG | — | ✅ |
| 81 | CstTransactionsPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 82 | CstTransactionsPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 83 | CstTransactionsPEOTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 84 | CstTransactionsPEOTransactionCurrencyCode | TRANSACTION_CURRENCY_CODE | — | ✅ |
| 85 | CstTransactionsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 86 | CstTransactionsPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 87 | CstTransactionsPEOTransactionGroupId | TRANSACTION_GROUP_ID | — | ✅ |
| 88 | CstTransactionsPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 89 | CstTransactionsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 90 | CstTransactionsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 91 | CstTransactionsPEOTransferBookId | TRANSFER_BOOK_ID | — | ✅ |
| 92 | CstTransactionsPEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | ✅ |
| 93 | CstTransactionsPEOTransferCstInvTxnDtlId | TRANSFER_CST_INV_TXN_DTL_ID | — | ✅ |
| 94 | CstTransactionsPEOTransferCstInvTxnId | TRANSFER_CST_INV_TXN_ID | — | ✅ |
| 95 | CstTransactionsPEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 96 | CstTransactionsPEOTransferTransactionGroupId | TRANSFER_TRANSACTION_GROUP_ID | — | ✅ |
| 97 | CstTransactionsPEOTransferUomConversionFactor | TRANSFER_UOM_CONVERSION_FACTOR | — | ✅ |
| 98 | CstTransactionsPEOTransferValUnitId | TRANSFER_VAL_UNIT_ID | — | ✅ |
| 99 | CstTransactionsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 100 | CstTransactionsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 101 | CstTransactionsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 102 | CstTransactionsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 103 | CstTransactionsPEOUomCode | UOM_CODE | — | ✅ |
| 104 | CstTransactionsPEOUomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |
| 105 | CstTransactionsPEOUseItemCostFlag | USE_ITEM_COST_FLAG | — | ✅ |
| 106 | CstTransactionsPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |
| 107 | CstTransactionsPEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 108 | CstTransactionsPEOValUnitCombinationId | VAL_UNIT_COMBINATION_ID | — | ✅ |
| 109 | CstTransactionsPEOValUnitDetailId | VAL_UNIT_DETAIL_ID | — | ✅ |
| 110 | CstTransactionsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 111 | CstTransactionsPEOWoCostAllocationBasis | WO_COST_ALLOCATION_BASIS | — | ✅ |
| 112 | CstTransactionsPEOWoLayerPostedFlag | WO_LAYER_POSTED_FLAG | — | ✅ |
| 113 | CstTransactionsPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | — | ✅ |
| 114 | CstTransactionsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 115 | CstTransactionsPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
