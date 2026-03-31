---
id: DOC-OTHER-PVO-TransferOrderLineExtractPVO
doc_type: system-doc
title: "TransferOrderLineExtractPVO — PVO Cross-Module"
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
  - TransferOrderLineExtractPVO
  - transferorderlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransferOrderLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transfer Order Line Extract. Acessa as tabelas: INV_TRANSFER_ORDER_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.TransferOrderLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 100 | 1 | 1 | 100 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transfer_order_lines|INV_TRANSFER_ORDER_LINES]] — 100 atributos (1 PKs, 100 BICC)

---

## ⚙️ Atributos

### [[inv_transfer_order_lines|INV_TRANSFER_ORDER_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionSourceType | ACTION_SOURCE_TYPE | — | ✅ |
| 2 | AllowItemSubstitutionFlag | ALLOW_ITEM_SUBSTITUTION_FLAG | — | ✅ |
| 3 | InitialRequestedQty | INITIAL_REQUESTED_QTY | — | ✅ |
| 4 | ItemSubstitutedFlag | ITEM_SUBSTITUTED_FLAG | — | ✅ |
| 5 | RepriceFlag | REPRICE_FLAG | — | ✅ |
| 6 | TOLinePEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 7 | TOLinePEOBackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 8 | TOLinePEOBuyAssessableValue | BUY_ASSESSABLE_VALUE | — | ✅ |
| 9 | TOLinePEOBuyDefaultTaxCountry | BUY_DEFAULT_TAX_COUNTRY | — | ✅ |
| 10 | TOLinePEOBuyDocumentSubType | BUY_DOCUMENT_SUB_TYPE | — | ✅ |
| 11 | TOLinePEOBuyFinalDischargeLocId | BUY_FINAL_DISCHARGE_LOC_ID | — | ✅ |
| 12 | TOLinePEOBuyFirstPtyRegId | BUY_FIRST_PTY_REG_ID | — | ✅ |
| 13 | TOLinePEOBuyIntendUseClassifId | BUY_INTEND_USE_CLASSIF_ID | — | ✅ |
| 14 | TOLinePEOBuyProductCategory | BUY_PRODUCT_CATEGORY | — | ✅ |
| 15 | TOLinePEOBuyProductFiscClassif | BUY_PRODUCT_FISC_CLASSIF | — | ✅ |
| 16 | TOLinePEOBuyProductType | BUY_PRODUCT_TYPE | — | ✅ |
| 17 | TOLinePEOBuyTaxClassifCode | BUY_TAX_CLASSIF_CODE | — | ✅ |
| 18 | TOLinePEOBuyThirdPtyRegId | BUY_THIRD_PTY_REG_ID | — | ✅ |
| 19 | TOLinePEOBuyTrxBusinessCategory | BUY_TRX_BUSINESS_CATEGORY | — | ✅ |
| 20 | TOLinePEOBuyUsrDefinedFiscClass | BUY_USR_DEFINED_FISC_CLASS | — | ✅ |
| 21 | TOLinePEOChangePartyId | CHANGE_PARTY_ID | — | ✅ |
| 22 | TOLinePEOChangeRequestedDate | CHANGE_REQUESTED_DATE | — | ✅ |
| 23 | TOLinePEOChangeStatusLookup | CHANGE_STATUS_LOOKUP | — | ✅ |
| 24 | TOLinePEOComments | COMMENTS | — | ✅ |
| 25 | TOLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | TOLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | TOLinePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 28 | TOLinePEODeliveredQty | DELIVERED_QTY | — | ✅ |
| 29 | TOLinePEODestinationLocationId | DESTINATION_LOCATION_ID | — | ✅ |
| 30 | TOLinePEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 31 | TOLinePEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | ✅ |
| 32 | TOLinePEODestinationTypeLookup | DESTINATION_TYPE_LOOKUP | — | ✅ |
| 33 | TOLinePEOFirmFlag | FIRM_FLAG | — | ✅ |
| 34 | TOLinePEOFreightCarrierId | FREIGHT_CARRIER_ID | — | ✅ |
| 35 | TOLinePEOHeaderId | HEADER_ID | — | ✅ |
| 36 | TOLinePEOInclNonrecoverableTax | INCL_NONRECOVERABLE_TAX | — | ✅ |
| 37 | TOLinePEOInclRecoverableTax | INCL_RECOVERABLE_TAX | — | ✅ |
| 38 | TOLinePEOInterfaceErrMsgCode | INTERFACE_ERR_MSG_CODE | — | ✅ |
| 39 | TOLinePEOInterfaceErrMsgText | INTERFACE_ERR_MSG_TEXT | — | ✅ |
| 40 | TOLinePEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 41 | TOLinePEOInterfaceStatusLookup | INTERFACE_STATUS_LOOKUP | — | ✅ |
| 42 | TOLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 43 | TOLinePEOItemRevision | ITEM_REVISION | — | ✅ |
| 44 | TOLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | TOLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 46 | TOLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 47 | TOLinePEOLineId | LINE_ID | 🔑 | ✅ |
| 48 | TOLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 49 | TOLinePEOMaterialReturnRequired | MATERIAL_RETURN_REQUIRED | — | ✅ |
| 50 | TOLinePEOModeOfTransportLookup | MODE_OF_TRANSPORT_LOOKUP | — | ✅ |
| 51 | TOLinePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 52 | TOLinePEONoninclNonrecoverableTax | NONINCL_NONRECOVERABLE_TAX | — | ✅ |
| 53 | TOLinePEONoninclRecoverableTax | NONINCL_RECOVERABLE_TAX | — | ✅ |
| 54 | TOLinePEONoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 55 | TOLinePEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 56 | TOLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 57 | TOLinePEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 58 | TOLinePEOOriginalLineId | ORIGINAL_LINE_ID | — | ✅ |
| 59 | TOLinePEOOriginalRequestLineId | ORIGINAL_REQUEST_LINE_ID | — | ✅ |
| 60 | TOLinePEOParentItemId | PARENT_ITEM_ID | — | ✅ |
| 61 | TOLinePEOPlannerId | PLANNER_ID | — | ✅ |
| 62 | TOLinePEOQtyUomCode | QTY_UOM_CODE | — | ✅ |
| 63 | TOLinePEOReceivedQty | RECEIVED_QTY | — | ✅ |
| 64 | TOLinePEOReqBuId | REQ_BU_ID | — | ✅ |
| 65 | TOLinePEORequestedQty | REQUESTED_QTY | — | ✅ |
| 66 | TOLinePEORequesterId | REQUESTER_ID | — | ✅ |
| 67 | TOLinePEORequisitionId | REQUISITION_ID | — | ✅ |
| 68 | TOLinePEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 69 | TOLinePEOScheduledArrivalDate | SCHEDULED_ARRIVAL_DATE | — | ✅ |
| 70 | TOLinePEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | ✅ |
| 71 | TOLinePEOSecondaryDeliveredQty | SECONDARY_DELIVERED_QTY | — | ✅ |
| 72 | TOLinePEOSecondaryQtyUomCode | SECONDARY_QTY_UOM_CODE | — | ✅ |
| 73 | TOLinePEOSecondaryReceivedQty | SECONDARY_RECEIVED_QTY | — | ✅ |
| 74 | TOLinePEOSecondaryRequestedQty | SECONDARY_REQUESTED_QTY | — | ✅ |
| 75 | TOLinePEOSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | ✅ |
| 76 | TOLinePEOSellAssessableValue | SELL_ASSESSABLE_VALUE | — | ✅ |
| 77 | TOLinePEOSellDefaultTaxCountry | SELL_DEFAULT_TAX_COUNTRY | — | ✅ |
| 78 | TOLinePEOSellDocumentSubType | SELL_DOCUMENT_SUB_TYPE | — | ✅ |
| 79 | TOLinePEOSellFinalDischargeLocId | SELL_FINAL_DISCHARGE_LOC_ID | — | ✅ |
| 80 | TOLinePEOSellFirstPtyRegId | SELL_FIRST_PTY_REG_ID | — | ✅ |
| 81 | TOLinePEOSellIntendUseClassifId | SELL_INTEND_USE_CLASSIF_ID | — | ✅ |
| 82 | TOLinePEOSellProductCategory | SELL_PRODUCT_CATEGORY | — | ✅ |
| 83 | TOLinePEOSellProductFiscClassif | SELL_PRODUCT_FISC_CLASSIF | — | ✅ |
| 84 | TOLinePEOSellProductType | SELL_PRODUCT_TYPE | — | ✅ |
| 85 | TOLinePEOSellTaxClassifCode | SELL_TAX_CLASSIF_CODE | — | ✅ |
| 86 | TOLinePEOSellThirdPtyRegId | SELL_THIRD_PTY_REG_ID | — | ✅ |
| 87 | TOLinePEOSellTrxBusinessCategory | SELL_TRX_BUSINESS_CATEGORY | — | ✅ |
| 88 | TOLinePEOSellUsrDefinedFiscClass | SELL_USR_DEFINED_FISC_CLASS | — | ✅ |
| 89 | TOLinePEOServiceLevelLookup | SERVICE_LEVEL_LOOKUP | — | ✅ |
| 90 | TOLinePEOShipmentPriorityLookup | SHIPMENT_PRIORITY_LOOKUP | — | ✅ |
| 91 | TOLinePEOShippedQty | SHIPPED_QTY | — | ✅ |
| 92 | TOLinePEOSourceHeaderId | SOURCE_HEADER_ID | — | ✅ |
| 93 | TOLinePEOSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 94 | TOLinePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 95 | TOLinePEOSourceSubinventoryCode | SOURCE_SUBINVENTORY_CODE | — | ✅ |
| 96 | TOLinePEOSourceTypeLookup | SOURCE_TYPE_LOOKUP | — | ✅ |
| 97 | TOLinePEOStatusLookup | STATUS_LOOKUP | — | ✅ |
| 98 | TOLinePEOSupplyOrderRefLineNumber | SUPPLY_ORDER_REF_LINE_NUMBER | — | ✅ |
| 99 | TOLinePEOSupplyOrderReferenceNumber | SUPPLY_ORDER_REFERENCE_NUMBER | — | ✅ |
| 100 | TOLinePEOUnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
