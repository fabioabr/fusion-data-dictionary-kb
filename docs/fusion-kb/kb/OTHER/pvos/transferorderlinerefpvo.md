---
id: DOC-OTHER-PVO-TransferOrderLineRefPVO
doc_type: system-doc
title: "TransferOrderLineRefPVO — PVO Cross-Module"
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
  - TransferOrderLineRefPVO
  - transferorderlinerefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransferOrderLineRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transfer Order Line Ref. Acessa as tabelas: INV_ORG_PARAMETERS_V, INV_TRANSFER_ORDER_HEADERS, INV_TRANSFER_ORDER_LINES (+1).

**Caminho:** `FscmTopModelAM.InventoryAM.TransferOrderLineRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 270 | 4 | 1 | 30 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 2 atributos
- [[inv_transfer_order_headers|INV_TRANSFER_ORDER_HEADERS]] — 28 atributos (3 BICC)
- [[inv_transfer_order_lines|INV_TRANSFER_ORDER_LINES]] — 191 atributos (1 PKs, 27 BICC)
- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 49 atributos

---

## ⚙️ Atributos

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DestinationOrgParameterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | SourceOrgParameterPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[inv_transfer_order_headers|INV_TRANSFER_ORDER_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OriginalTOHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 2 | OriginalTOHeaderPEOCreatedBy | CREATED_BY | — | — |
| 3 | OriginalTOHeaderPEOCreationDate | CREATION_DATE | — | — |
| 4 | OriginalTOHeaderPEODescription | DESCRIPTION | — | — |
| 5 | OriginalTOHeaderPEOFulfillOrchestrationRequired | FULFILL_ORCHESTRATION_REQUIRED | — | — |
| 6 | OriginalTOHeaderPEOHeaderId | HEADER_ID | — | — |
| 7 | OriginalTOHeaderPEOHeaderNumber | HEADER_NUMBER | — | — |
| 8 | OriginalTOHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | OriginalTOHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | OriginalTOHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | OriginalTOHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OriginalTOHeaderPEOOrderedDate | ORDERED_DATE | — | — |
| 13 | OriginalTOHeaderPEOReqBuId | REQ_BU_ID | — | — |
| 14 | OriginalTOHeaderPEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | — |
| 15 | TransferOrderHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 16 | TransferOrderHeaderPEOCreatedBy | CREATED_BY | — | — |
| 17 | TransferOrderHeaderPEOCreationDate | CREATION_DATE | — | — |
| 18 | TransferOrderHeaderPEODescription | DESCRIPTION | — | ✅ |
| 19 | TransferOrderHeaderPEOFulfillOrchestrationRequired | FULFILL_ORCHESTRATION_REQUIRED | — | — |
| 20 | TransferOrderHeaderPEOHeaderId | HEADER_ID | — | — |
| 21 | TransferOrderHeaderPEOHeaderNumber | HEADER_NUMBER | — | ✅ |
| 22 | TransferOrderHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 23 | TransferOrderHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | TransferOrderHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | TransferOrderHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | TransferOrderHeaderPEOOrderedDate | ORDERED_DATE | — | — |
| 27 | TransferOrderHeaderPEOReqBuId | REQ_BU_ID | — | — |
| 28 | TransferOrderHeaderPEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | ✅ |

### [[inv_transfer_order_lines|INV_TRANSFER_ORDER_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OriginalTOLinePEOAgreementPtrId | AGREEMENT_PTR_ID | — | — |
| 2 | OriginalTOLinePEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 3 | OriginalTOLinePEOBuyAssessableValue | BUY_ASSESSABLE_VALUE | — | — |
| 4 | OriginalTOLinePEOBuyDefaultTaxCountry | BUY_DEFAULT_TAX_COUNTRY | — | — |
| 5 | OriginalTOLinePEOBuyDocumentSubType | BUY_DOCUMENT_SUB_TYPE | — | — |
| 6 | OriginalTOLinePEOBuyFinalDischargeLocId | BUY_FINAL_DISCHARGE_LOC_ID | — | — |
| 7 | OriginalTOLinePEOBuyFirstPtyRegId | BUY_FIRST_PTY_REG_ID | — | — |
| 8 | OriginalTOLinePEOBuyIntendUseClassifId | BUY_INTEND_USE_CLASSIF_ID | — | — |
| 9 | OriginalTOLinePEOBuyProductCategory | BUY_PRODUCT_CATEGORY | — | — |
| 10 | OriginalTOLinePEOBuyProductFiscClassif | BUY_PRODUCT_FISC_CLASSIF | — | — |
| 11 | OriginalTOLinePEOBuyProductType | BUY_PRODUCT_TYPE | — | — |
| 12 | OriginalTOLinePEOBuyTaxClassifCode | BUY_TAX_CLASSIF_CODE | — | — |
| 13 | OriginalTOLinePEOBuyThirdPtyRegId | BUY_THIRD_PTY_REG_ID | — | — |
| 14 | OriginalTOLinePEOBuyTrxBusinessCategory | BUY_TRX_BUSINESS_CATEGORY | — | — |
| 15 | OriginalTOLinePEOBuyUsrDefinedFiscClass | BUY_USR_DEFINED_FISC_CLASS | — | — |
| 16 | OriginalTOLinePEOChangePartyId | CHANGE_PARTY_ID | — | — |
| 17 | OriginalTOLinePEOChangeRequestedDate | CHANGE_REQUESTED_DATE | — | — |
| 18 | OriginalTOLinePEOChangeStatusLookup | CHANGE_STATUS_LOOKUP | — | — |
| 19 | OriginalTOLinePEOComments | COMMENTS | — | — |
| 20 | OriginalTOLinePEOCreatedBy | CREATED_BY | — | — |
| 21 | OriginalTOLinePEOCreationDate | CREATION_DATE | — | — |
| 22 | OriginalTOLinePEOCurrencyCode | CURRENCY_CODE | — | — |
| 23 | OriginalTOLinePEODeliveredQty | DELIVERED_QTY | — | — |
| 24 | OriginalTOLinePEODestinationLocationId | DESTINATION_LOCATION_ID | — | — |
| 25 | OriginalTOLinePEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 26 | OriginalTOLinePEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | — |
| 27 | OriginalTOLinePEODestinationTypeLookup | DESTINATION_TYPE_LOOKUP | — | — |
| 28 | OriginalTOLinePEOFirmFlag | FIRM_FLAG | — | — |
| 29 | OriginalTOLinePEOFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 30 | OriginalTOLinePEOHeaderId | HEADER_ID | — | — |
| 31 | OriginalTOLinePEOInclNonrecoverableTax | INCL_NONRECOVERABLE_TAX | — | — |
| 32 | OriginalTOLinePEOInclRecoverableTax | INCL_RECOVERABLE_TAX | — | — |
| 33 | OriginalTOLinePEOInterfaceErrMsgCode | INTERFACE_ERR_MSG_CODE | — | — |
| 34 | OriginalTOLinePEOInterfaceErrMsgText | INTERFACE_ERR_MSG_TEXT | — | — |
| 35 | OriginalTOLinePEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 36 | OriginalTOLinePEOInterfaceStatusLookup | INTERFACE_STATUS_LOOKUP | — | — |
| 37 | OriginalTOLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 38 | OriginalTOLinePEOItemRevision | ITEM_REVISION | — | — |
| 39 | OriginalTOLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 40 | OriginalTOLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | OriginalTOLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | OriginalTOLinePEOLineId | LINE_ID | — | — |
| 43 | OriginalTOLinePEOLineNumber | LINE_NUMBER | — | — |
| 44 | OriginalTOLinePEOMaterialReturnRequired | MATERIAL_RETURN_REQUIRED | — | — |
| 45 | OriginalTOLinePEOModeOfTransportLookup | MODE_OF_TRANSPORT_LOOKUP | — | — |
| 46 | OriginalTOLinePEONeedByDate | NEED_BY_DATE | — | — |
| 47 | OriginalTOLinePEONoninclNonrecoverableTax | NONINCL_NONRECOVERABLE_TAX | — | — |
| 48 | OriginalTOLinePEONoninclRecoverableTax | NONINCL_RECOVERABLE_TAX | — | — |
| 49 | OriginalTOLinePEONoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 50 | OriginalTOLinePEONoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 51 | OriginalTOLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | OriginalTOLinePEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | — |
| 53 | OriginalTOLinePEOOriginalLineId | ORIGINAL_LINE_ID | — | — |
| 54 | OriginalTOLinePEOOriginalRequestLineId | ORIGINAL_REQUEST_LINE_ID | — | — |
| 55 | OriginalTOLinePEOParentItemId | PARENT_ITEM_ID | — | — |
| 56 | OriginalTOLinePEOPlannerId | PLANNER_ID | — | — |
| 57 | OriginalTOLinePEOQtyUomCode | QTY_UOM_CODE | — | — |
| 58 | OriginalTOLinePEOReceivedQty | RECEIVED_QTY | — | — |
| 59 | OriginalTOLinePEOReqBuId | REQ_BU_ID | — | — |
| 60 | OriginalTOLinePEORequestedQty | REQUESTED_QTY | — | — |
| 61 | OriginalTOLinePEORequesterId | REQUESTER_ID | — | — |
| 62 | OriginalTOLinePEORequisitionId | REQUISITION_ID | — | — |
| 63 | OriginalTOLinePEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 64 | OriginalTOLinePEOScheduledArrivalDate | SCHEDULED_ARRIVAL_DATE | — | — |
| 65 | OriginalTOLinePEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | — |
| 66 | OriginalTOLinePEOSecondaryDeliveredQty | SECONDARY_DELIVERED_QTY | — | — |
| 67 | OriginalTOLinePEOSecondaryQtyUomCode | SECONDARY_QTY_UOM_CODE | — | — |
| 68 | OriginalTOLinePEOSecondaryReceivedQty | SECONDARY_RECEIVED_QTY | — | — |
| 69 | OriginalTOLinePEOSecondaryRequestedQty | SECONDARY_REQUESTED_QTY | — | — |
| 70 | OriginalTOLinePEOSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | — |
| 71 | OriginalTOLinePEOSellAssessableValue | SELL_ASSESSABLE_VALUE | — | — |
| 72 | OriginalTOLinePEOSellDefaultTaxCountry | SELL_DEFAULT_TAX_COUNTRY | — | — |
| 73 | OriginalTOLinePEOSellDocumentSubType | SELL_DOCUMENT_SUB_TYPE | — | — |
| 74 | OriginalTOLinePEOSellFinalDischargeLocId | SELL_FINAL_DISCHARGE_LOC_ID | — | — |
| 75 | OriginalTOLinePEOSellFirstPtyRegId | SELL_FIRST_PTY_REG_ID | — | — |
| 76 | OriginalTOLinePEOSellIntendUseClassifId | SELL_INTEND_USE_CLASSIF_ID | — | — |
| 77 | OriginalTOLinePEOSellProductCategory | SELL_PRODUCT_CATEGORY | — | — |
| 78 | OriginalTOLinePEOSellProductFiscClassif | SELL_PRODUCT_FISC_CLASSIF | — | — |
| 79 | OriginalTOLinePEOSellProductType | SELL_PRODUCT_TYPE | — | — |
| 80 | OriginalTOLinePEOSellTaxClassifCode | SELL_TAX_CLASSIF_CODE | — | — |
| 81 | OriginalTOLinePEOSellThirdPtyRegId | SELL_THIRD_PTY_REG_ID | — | — |
| 82 | OriginalTOLinePEOSellTrxBusinessCategory | SELL_TRX_BUSINESS_CATEGORY | — | — |
| 83 | OriginalTOLinePEOSellUsrDefinedFiscClass | SELL_USR_DEFINED_FISC_CLASS | — | — |
| 84 | OriginalTOLinePEOServiceLevelLookup | SERVICE_LEVEL_LOOKUP | — | — |
| 85 | OriginalTOLinePEOShipmentPriorityLookup | SHIPMENT_PRIORITY_LOOKUP | — | — |
| 86 | OriginalTOLinePEOShippedQty | SHIPPED_QTY | — | — |
| 87 | OriginalTOLinePEOSourceHeaderId | SOURCE_HEADER_ID | — | — |
| 88 | OriginalTOLinePEOSourceLineId | SOURCE_LINE_ID | — | — |
| 89 | OriginalTOLinePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 90 | OriginalTOLinePEOSourceSubinventoryCode | SOURCE_SUBINVENTORY_CODE | — | — |
| 91 | OriginalTOLinePEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | — |
| 92 | OriginalTOLinePEOStatusLookup | STATUS_LOOKUP | — | — |
| 93 | OriginalTOLinePEOUnitPrice | UNIT_PRICE | — | — |
| 94 | OriginalTOLinePEOUnitTax | UNIT_TAX | — | — |
| 95 | TransferOrderLinePEOAgreementPtrId | AGREEMENT_PTR_ID | — | — |
| 96 | TransferOrderLinePEOAllowItemSubstitutionFlag | ALLOW_ITEM_SUBSTITUTION_FLAG | — | ✅ |
| 97 | TransferOrderLinePEOBackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 98 | TransferOrderLinePEOBuyAssessableValue | BUY_ASSESSABLE_VALUE | — | — |
| 99 | TransferOrderLinePEOBuyDefaultTaxCountry | BUY_DEFAULT_TAX_COUNTRY | — | — |
| 100 | TransferOrderLinePEOBuyDocumentSubType | BUY_DOCUMENT_SUB_TYPE | — | — |
| 101 | TransferOrderLinePEOBuyFinalDischargeLocId | BUY_FINAL_DISCHARGE_LOC_ID | — | — |
| 102 | TransferOrderLinePEOBuyFirstPtyRegId | BUY_FIRST_PTY_REG_ID | — | — |
| 103 | TransferOrderLinePEOBuyIntendUseClassifId | BUY_INTEND_USE_CLASSIF_ID | — | — |
| 104 | TransferOrderLinePEOBuyProductCategory | BUY_PRODUCT_CATEGORY | — | — |
| 105 | TransferOrderLinePEOBuyProductFiscClassif | BUY_PRODUCT_FISC_CLASSIF | — | — |
| 106 | TransferOrderLinePEOBuyProductType | BUY_PRODUCT_TYPE | — | — |
| 107 | TransferOrderLinePEOBuyTaxClassifCode | BUY_TAX_CLASSIF_CODE | — | — |
| 108 | TransferOrderLinePEOBuyThirdPtyRegId | BUY_THIRD_PTY_REG_ID | — | — |
| 109 | TransferOrderLinePEOBuyTrxBusinessCategory | BUY_TRX_BUSINESS_CATEGORY | — | — |
| 110 | TransferOrderLinePEOBuyUsrDefinedFiscClass | BUY_USR_DEFINED_FISC_CLASS | — | — |
| 111 | TransferOrderLinePEOChangePartyId | CHANGE_PARTY_ID | — | — |
| 112 | TransferOrderLinePEOChangeRequestedDate | CHANGE_REQUESTED_DATE | — | — |
| 113 | TransferOrderLinePEOChangeStatusLookup | CHANGE_STATUS_LOOKUP | — | ✅ |
| 114 | TransferOrderLinePEOComments | COMMENTS | — | ✅ |
| 115 | TransferOrderLinePEOCreatedBy | CREATED_BY | — | — |
| 116 | TransferOrderLinePEOCreationDate | CREATION_DATE | — | — |
| 117 | TransferOrderLinePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 118 | TransferOrderLinePEODeliveredQty | DELIVERED_QTY | — | ✅ |
| 119 | TransferOrderLinePEODestinationLocationId | DESTINATION_LOCATION_ID | — | — |
| 120 | TransferOrderLinePEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 121 | TransferOrderLinePEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | — |
| 122 | TransferOrderLinePEODestinationTypeLookup | DESTINATION_TYPE_LOOKUP | — | ✅ |
| 123 | TransferOrderLinePEOFirmFlag | FIRM_FLAG | — | ✅ |
| 124 | TransferOrderLinePEOFreightCarrierId | FREIGHT_CARRIER_ID | — | — |
| 125 | TransferOrderLinePEOHeaderId | HEADER_ID | — | ✅ |
| 126 | TransferOrderLinePEOInclNonrecoverableTax | INCL_NONRECOVERABLE_TAX | — | — |
| 127 | TransferOrderLinePEOInclRecoverableTax | INCL_RECOVERABLE_TAX | — | — |
| 128 | TransferOrderLinePEOInitialRequestedQty | INITIAL_REQUESTED_QTY | — | — |
| 129 | TransferOrderLinePEOInterfaceErrMsgCode | INTERFACE_ERR_MSG_CODE | — | — |
| 130 | TransferOrderLinePEOInterfaceErrMsgText | INTERFACE_ERR_MSG_TEXT | — | ✅ |
| 131 | TransferOrderLinePEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 132 | TransferOrderLinePEOInterfaceStatusLookup | INTERFACE_STATUS_LOOKUP | — | — |
| 133 | TransferOrderLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 134 | TransferOrderLinePEOItemRevision | ITEM_REVISION | — | — |
| 135 | TransferOrderLinePEOItemSubstitutedFlag | ITEM_SUBSTITUTED_FLAG | — | ✅ |
| 136 | TransferOrderLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 137 | TransferOrderLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 138 | TransferOrderLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 139 | TransferOrderLinePEOLineId | LINE_ID | 🔑 | ✅ |
| 140 | TransferOrderLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 141 | TransferOrderLinePEOMaterialReturnRequired | MATERIAL_RETURN_REQUIRED | — | ✅ |
| 142 | TransferOrderLinePEOModeOfTransportLookup | MODE_OF_TRANSPORT_LOOKUP | — | — |
| 143 | TransferOrderLinePEONeedByDate | NEED_BY_DATE | — | — |
| 144 | TransferOrderLinePEONoninclNonrecoverableTax | NONINCL_NONRECOVERABLE_TAX | — | — |
| 145 | TransferOrderLinePEONoninclRecoverableTax | NONINCL_RECOVERABLE_TAX | — | — |
| 146 | TransferOrderLinePEONoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 147 | TransferOrderLinePEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 148 | TransferOrderLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 149 | TransferOrderLinePEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | — |
| 150 | TransferOrderLinePEOOriginalLineId | ORIGINAL_LINE_ID | — | — |
| 151 | TransferOrderLinePEOOriginalRequestLineId | ORIGINAL_REQUEST_LINE_ID | — | — |
| 152 | TransferOrderLinePEOParentItemId | PARENT_ITEM_ID | — | — |
| 153 | TransferOrderLinePEOPlannerId | PLANNER_ID | — | — |
| 154 | TransferOrderLinePEOQtyUomCode | QTY_UOM_CODE | — | ✅ |
| 155 | TransferOrderLinePEOReceivedQty | RECEIVED_QTY | — | ✅ |
| 156 | TransferOrderLinePEOReqBuId | REQ_BU_ID | — | — |
| 157 | TransferOrderLinePEORequestedQty | REQUESTED_QTY | — | ✅ |
| 158 | TransferOrderLinePEORequesterId | REQUESTER_ID | — | — |
| 159 | TransferOrderLinePEORequisitionId | REQUISITION_ID | — | — |
| 160 | TransferOrderLinePEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 161 | TransferOrderLinePEOScheduledArrivalDate | SCHEDULED_ARRIVAL_DATE | — | — |
| 162 | TransferOrderLinePEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | — |
| 163 | TransferOrderLinePEOSecondaryDeliveredQty | SECONDARY_DELIVERED_QTY | — | ✅ |
| 164 | TransferOrderLinePEOSecondaryQtyUomCode | SECONDARY_QTY_UOM_CODE | — | ✅ |
| 165 | TransferOrderLinePEOSecondaryReceivedQty | SECONDARY_RECEIVED_QTY | — | ✅ |
| 166 | TransferOrderLinePEOSecondaryRequestedQty | SECONDARY_REQUESTED_QTY | — | ✅ |
| 167 | TransferOrderLinePEOSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | ✅ |
| 168 | TransferOrderLinePEOSellAssessableValue | SELL_ASSESSABLE_VALUE | — | — |
| 169 | TransferOrderLinePEOSellDefaultTaxCountry | SELL_DEFAULT_TAX_COUNTRY | — | — |
| 170 | TransferOrderLinePEOSellDocumentSubType | SELL_DOCUMENT_SUB_TYPE | — | — |
| 171 | TransferOrderLinePEOSellFinalDischargeLocId | SELL_FINAL_DISCHARGE_LOC_ID | — | — |
| 172 | TransferOrderLinePEOSellFirstPtyRegId | SELL_FIRST_PTY_REG_ID | — | — |
| 173 | TransferOrderLinePEOSellIntendUseClassifId | SELL_INTEND_USE_CLASSIF_ID | — | — |
| 174 | TransferOrderLinePEOSellProductCategory | SELL_PRODUCT_CATEGORY | — | — |
| 175 | TransferOrderLinePEOSellProductFiscClassif | SELL_PRODUCT_FISC_CLASSIF | — | — |
| 176 | TransferOrderLinePEOSellProductType | SELL_PRODUCT_TYPE | — | — |
| 177 | TransferOrderLinePEOSellTaxClassifCode | SELL_TAX_CLASSIF_CODE | — | — |
| 178 | TransferOrderLinePEOSellThirdPtyRegId | SELL_THIRD_PTY_REG_ID | — | — |
| 179 | TransferOrderLinePEOSellTrxBusinessCategory | SELL_TRX_BUSINESS_CATEGORY | — | — |
| 180 | TransferOrderLinePEOSellUsrDefinedFiscClass | SELL_USR_DEFINED_FISC_CLASS | — | — |
| 181 | TransferOrderLinePEOServiceLevelLookup | SERVICE_LEVEL_LOOKUP | — | — |
| 182 | TransferOrderLinePEOShipmentPriorityLookup | SHIPMENT_PRIORITY_LOOKUP | — | — |
| 183 | TransferOrderLinePEOShippedQty | SHIPPED_QTY | — | ✅ |
| 184 | TransferOrderLinePEOSourceHeaderId | SOURCE_HEADER_ID | — | — |
| 185 | TransferOrderLinePEOSourceLineId | SOURCE_LINE_ID | — | — |
| 186 | TransferOrderLinePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 187 | TransferOrderLinePEOSourceSubinventoryCode | SOURCE_SUBINVENTORY_CODE | — | — |
| 188 | TransferOrderLinePEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | ✅ |
| 189 | TransferOrderLinePEOStatusLookup | STATUS_LOOKUP | — | ✅ |
| 190 | TransferOrderLinePEOUnitPrice | UNIT_PRICE | — | — |
| 191 | TransferOrderLinePEOUnitTax | UNIT_TAX | — | — |

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentStatus | DOCUMENT_STATUS | — | — |
| 2 | RequisitionHeaderPEOActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | — |
| 3 | RequisitionHeaderPEOApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 4 | RequisitionHeaderPEOApprovedDate | APPROVED_DATE | — | — |
| 5 | RequisitionHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 6 | RequisitionHeaderPEOChangePendingFlag | CHANGE_PENDING_FLAG | — | — |
| 7 | RequisitionHeaderPEOCreatedBy | CREATED_BY | — | — |
| 8 | RequisitionHeaderPEOCreationDate | CREATION_DATE | — | — |
| 9 | RequisitionHeaderPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 10 | RequisitionHeaderPEODescription | DESCRIPTION | — | — |
| 11 | RequisitionHeaderPEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 12 | RequisitionHeaderPEOEmergencyPoNumber | EMERGENCY_PO_NUMBER | — | — |
| 13 | RequisitionHeaderPEOEmergencyReqFlag | EMERGENCY_REQ_FLAG | — | — |
| 14 | RequisitionHeaderPEOExternallyManagedFlag | EXTERNALLY_MANAGED_FLAG | — | — |
| 15 | RequisitionHeaderPEOFundsChkFailWarnFlag | FUNDS_CHK_FAIL_WARN_FLAG | — | — |
| 16 | RequisitionHeaderPEOFundsOverrideApproverId | FUNDS_OVERRIDE_APPROVER_ID | — | — |
| 17 | RequisitionHeaderPEOFundsStatus | FUNDS_STATUS | — | — |
| 18 | RequisitionHeaderPEOHasCanceledLines | HAS_CANCELED_LINES | — | — |
| 19 | RequisitionHeaderPEOHasIncompleteLines | HAS_INCOMPLETE_LINES | — | — |
| 20 | RequisitionHeaderPEOHasPendingApprLines | HAS_PENDING_APPR_LINES | — | — |
| 21 | RequisitionHeaderPEOHasRejectedLines | HAS_REJECTED_LINES | — | — |
| 22 | RequisitionHeaderPEOHasReturnedLines | HAS_RETURNED_LINES | — | — |
| 23 | RequisitionHeaderPEOHasWithdrawnLines | HAS_WITHDRAWN_LINES | — | — |
| 24 | RequisitionHeaderPEOInsufficientFundsFlag | INSUFFICIENT_FUNDS_FLAG | — | — |
| 25 | RequisitionHeaderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 26 | RequisitionHeaderPEOInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | — |
| 27 | RequisitionHeaderPEOInternalTransferReqFlag | INTERNAL_TRANSFER_REQ_FLAG | — | — |
| 28 | RequisitionHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | RequisitionHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | RequisitionHeaderPEOJustification | JUSTIFICATION | — | — |
| 31 | RequisitionHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | RequisitionHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | RequisitionHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | RequisitionHeaderPEOLineGroup | LINE_GROUP | — | — |
| 35 | RequisitionHeaderPEOLockedByBuyerFlag | LOCKED_BY_BUYER_FLAG | — | — |
| 36 | RequisitionHeaderPEOModifyingApproverId | MODIFYING_APPROVER_ID | — | — |
| 37 | RequisitionHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | RequisitionHeaderPEOOverridingApproverId | OVERRIDING_APPROVER_ID | — | — |
| 39 | RequisitionHeaderPEOPcardId | PCARD_ID | — | — |
| 40 | RequisitionHeaderPEOPrcBuId | PRC_BU_ID | — | — |
| 41 | RequisitionHeaderPEOPreparerId | PREPARER_ID | — | — |
| 42 | RequisitionHeaderPEOReqBuId | REQ_BU_ID | — | — |
| 43 | RequisitionHeaderPEOReqImportApproverId | REQ_IMPORT_APPROVER_ID | — | — |
| 44 | RequisitionHeaderPEORequestId | REQUEST_ID | — | — |
| 45 | RequisitionHeaderPEORequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 46 | RequisitionHeaderPEORequisitionNumber | REQUISITION_NUMBER | — | — |
| 47 | RequisitionHeaderPEOSoldtoLeId | SOLDTO_LE_ID | — | — |
| 48 | RequisitionHeaderPEOSubmissionDate | SUBMISSION_DATE | — | — |
| 49 | RequisitionHeaderPEOTaxUserOverrideHdrFlag | TAX_USER_OVERRIDE_HDR_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
