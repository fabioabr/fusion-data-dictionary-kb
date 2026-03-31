---
id: DOC-OTHER-PVO-SupplyBuyOrderDetailsExtractPVO
doc_type: system-doc
title: "SupplyBuyOrderDetailsExtractPVO — PVO Cross-Module"
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
  - SupplyBuyOrderDetailsExtractPVO
  - supplybuyorderdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyBuyOrderDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Buy Order Details Extract. Acessa as tabelas: DOS_SUPPLY_BUY_ORDER_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyBuyOrderDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 1 | 1 | 60 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_buy_order_dtls|DOS_SUPPLY_BUY_ORDER_DTLS]] — 60 atributos (1 PKs, 60 BICC)

---

## ⚙️ Atributos

### [[dos_supply_buy_order_dtls|DOS_SUPPLY_BUY_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosBuyOrderDetailsPEOAuthorizationStatus | AUTHORIZATION_STATUS | — | ✅ |
| 2 | DosBuyOrderDetailsPEOAutosourceFlag | AUTOSOURCE_FLAG | — | ✅ |
| 3 | DosBuyOrderDetailsPEOBatchId | BATCH_ID | — | ✅ |
| 4 | DosBuyOrderDetailsPEOBuyerId | BUYER_ID | — | ✅ |
| 5 | DosBuyOrderDetailsPEOCarrierId | CARRIER_ID | — | ✅ |
| 6 | DosBuyOrderDetailsPEOCategoryId | CATEGORY_ID | — | ✅ |
| 7 | DosBuyOrderDetailsPEOChangeSupplyOperation | CHANGE_SUPPLY_OPERATION | — | ✅ |
| 8 | DosBuyOrderDetailsPEOContractMfgItemId | CONTRACT_MFG_ITEM_ID | — | ✅ |
| 9 | DosBuyOrderDetailsPEOContractMfgItemRevision | CONTRACT_MFG_ITEM_REVISION | — | ✅ |
| 10 | DosBuyOrderDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | DosBuyOrderDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | DosBuyOrderDetailsPEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 13 | DosBuyOrderDetailsPEODeliverToRequestorId | DELIVER_TO_REQUESTOR_ID | — | ✅ |
| 14 | DosBuyOrderDetailsPEODeliveryLeadTime | DELIVERY_LEAD_TIME | — | ✅ |
| 15 | DosBuyOrderDetailsPEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | ✅ |
| 16 | DosBuyOrderDetailsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 17 | DosBuyOrderDetailsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 18 | DosBuyOrderDetailsPEOEarliestShipDate | EARLIEST_SHIP_DATE | — | ✅ |
| 19 | DosBuyOrderDetailsPEOEndInventoryItemId | END_INVENTORY_ITEM_ID | — | ✅ |
| 20 | DosBuyOrderDetailsPEOEndItemName | END_ITEM_NAME | — | ✅ |
| 21 | DosBuyOrderDetailsPEOExecSystemDeliverToSubinv | EXEC_SYSTEM_DELIVER_TO_SUBINV | — | ✅ |
| 22 | DosBuyOrderDetailsPEOExecSystemDelvrToLocName | EXEC_SYSTEM_DELVR_TO_LOC_NAME | — | ✅ |
| 23 | DosBuyOrderDetailsPEOExecSystemDelvrToRequestor | EXEC_SYSTEM_DELVR_TO_REQUESTOR | — | ✅ |
| 24 | DosBuyOrderDetailsPEOExecSystemDestnLoctrCode | EXEC_SYSTEM_DESTN_LOCTR_CODE | — | ✅ |
| 25 | DosBuyOrderDetailsPEOExecSystemSuggestedVendor | EXEC_SYSTEM_SUGGESTED_VENDOR | — | ✅ |
| 26 | DosBuyOrderDetailsPEOExecSystemSugstdVendorSite | EXEC_SYSTEM_SUGSTD_VENDOR_SITE | — | ✅ |
| 27 | DosBuyOrderDetailsPEOFirmFlag | FIRM_FLAG | — | ✅ |
| 28 | DosBuyOrderDetailsPEOGroupCode | GROUP_CODE | — | ✅ |
| 29 | DosBuyOrderDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | DosBuyOrderDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | DosBuyOrderDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | DosBuyOrderDetailsPEOLineLocationId | LINE_LOCATION_ID | — | ✅ |
| 33 | DosBuyOrderDetailsPEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 34 | DosBuyOrderDetailsPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 35 | DosBuyOrderDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | DosBuyOrderDetailsPEOPreparerId | PREPARER_ID | — | ✅ |
| 37 | DosBuyOrderDetailsPEOPrimaryDocQuantity | PRIMARY_DOC_QUANTITY | — | ✅ |
| 38 | DosBuyOrderDetailsPEOPrimaryDocQuantityUom | PRIMARY_DOC_QUANTITY_UOM | — | ✅ |
| 39 | DosBuyOrderDetailsPEOPurchaseOrderHeaderId | PURCHASE_ORDER_HEADER_ID | — | ✅ |
| 40 | DosBuyOrderDetailsPEOPurchaseOrderLineId | PURCHASE_ORDER_LINE_ID | — | ✅ |
| 41 | DosBuyOrderDetailsPEOPurchaseOrderLineNumber | PURCHASE_ORDER_LINE_NUMBER | — | ✅ |
| 42 | DosBuyOrderDetailsPEOPurchaseOrderNumber | PURCHASE_ORDER_NUMBER | — | ✅ |
| 43 | DosBuyOrderDetailsPEOPurchaseOrderScheduleNumber | PURCHASE_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 44 | DosBuyOrderDetailsPEORequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 45 | DosBuyOrderDetailsPEORequisitionId | REQUISITION_ID | — | ✅ |
| 46 | DosBuyOrderDetailsPEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 47 | DosBuyOrderDetailsPEORequisitionLineNumber | REQUISITION_LINE_NUMBER | — | ✅ |
| 48 | DosBuyOrderDetailsPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 49 | DosBuyOrderDetailsPEORequisitionSourceTypeCode | REQUISITION_SOURCE_TYPE_CODE | — | ✅ |
| 50 | DosBuyOrderDetailsPEORequisitioningBuId | REQUISITIONING_BU_ID | — | ✅ |
| 51 | DosBuyOrderDetailsPEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | ✅ |
| 52 | DosBuyOrderDetailsPEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 53 | DosBuyOrderDetailsPEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 54 | DosBuyOrderDetailsPEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 55 | DosBuyOrderDetailsPEOShippingMethod | SHIPPING_METHOD | — | ✅ |
| 56 | DosBuyOrderDetailsPEOSuggestedVendorId | SUGGESTED_VENDOR_ID | — | ✅ |
| 57 | DosBuyOrderDetailsPEOSuggestedVendorSiteId | SUGGESTED_VENDOR_SITE_ID | — | ✅ |
| 58 | DosBuyOrderDetailsPEOSupplyBuyOrdDtlsId | SUPPLY_BUY_ORD_DTLS_ID | 🔑 | ✅ |
| 59 | DosBuyOrderDetailsPEOTrackingLineId | TRACKING_LINE_ID | — | ✅ |
| 60 | DosBuyOrderDetailsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
