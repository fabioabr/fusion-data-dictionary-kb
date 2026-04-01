---
id: DOC-OTHER-PVO-SupplyTransferOrderDetailsExtractPVO
doc_type: system-doc
title: "SupplyTransferOrderDetailsExtractPVO — PVO Cross-Module"
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
  - SupplyTransferOrderDetailsExtractPVO
  - supplytransferorderdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyTransferOrderDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Transfer Order Details Extract. Acessa as tabelas: DOS_SUPPLY_TRANSFER_ORDER_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyTransferOrderDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 1 | 1 | 103 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_supply_transfer_order_dtls|DOS_SUPPLY_TRANSFER_ORDER_DTLS]] — 103 atributos (1 PKs, 103 BICC)

---

## ⚙️ Atributos

### [[dos_supply_transfer_order_dtls|DOS_SUPPLY_TRANSFER_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosTransferOrderDetailsPEOAgreementId | AGREEMENT_ID | — | ✅ |
| 2 | DosTransferOrderDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | DosTransferOrderDetailsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 4 | DosTransferOrderDetailsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 5 | DosTransferOrderDetailsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 6 | DosTransferOrderDetailsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 7 | DosTransferOrderDetailsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 8 | DosTransferOrderDetailsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 9 | DosTransferOrderDetailsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 10 | DosTransferOrderDetailsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 11 | DosTransferOrderDetailsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 12 | DosTransferOrderDetailsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 13 | DosTransferOrderDetailsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 14 | DosTransferOrderDetailsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 15 | DosTransferOrderDetailsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 16 | DosTransferOrderDetailsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 17 | DosTransferOrderDetailsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 18 | DosTransferOrderDetailsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 19 | DosTransferOrderDetailsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 20 | DosTransferOrderDetailsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 21 | DosTransferOrderDetailsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 22 | DosTransferOrderDetailsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 23 | DosTransferOrderDetailsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 24 | DosTransferOrderDetailsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 25 | DosTransferOrderDetailsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 26 | DosTransferOrderDetailsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 27 | DosTransferOrderDetailsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 28 | DosTransferOrderDetailsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 29 | DosTransferOrderDetailsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 30 | DosTransferOrderDetailsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 31 | DosTransferOrderDetailsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 32 | DosTransferOrderDetailsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 33 | DosTransferOrderDetailsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 34 | DosTransferOrderDetailsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 35 | DosTransferOrderDetailsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 36 | DosTransferOrderDetailsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 37 | DosTransferOrderDetailsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 38 | DosTransferOrderDetailsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 39 | DosTransferOrderDetailsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 40 | DosTransferOrderDetailsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 41 | DosTransferOrderDetailsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 42 | DosTransferOrderDetailsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 43 | DosTransferOrderDetailsPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 44 | DosTransferOrderDetailsPEOBudgetDate | BUDGET_DATE | — | ✅ |
| 45 | DosTransferOrderDetailsPEOCarrierId | CARRIER_ID | — | ✅ |
| 46 | DosTransferOrderDetailsPEOChangeSupplyOperation | CHANGE_SUPPLY_OPERATION | — | ✅ |
| 47 | DosTransferOrderDetailsPEOComments | COMMENTS | — | ✅ |
| 48 | DosTransferOrderDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 49 | DosTransferOrderDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 50 | DosTransferOrderDetailsPEODeliverToRequestorId | DELIVER_TO_REQUESTOR_ID | — | ✅ |
| 51 | DosTransferOrderDetailsPEODestinationLocationId | DESTINATION_LOCATION_ID | — | ✅ |
| 52 | DosTransferOrderDetailsPEODestinationSubinventoryCode | DESTINATION_SUBINVENTORY_CODE | — | ✅ |
| 53 | DosTransferOrderDetailsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 54 | DosTransferOrderDetailsPEODooShipmentFlag | DOO_SHIPMENT_FLAG | — | ✅ |
| 55 | DosTransferOrderDetailsPEOEndInventoryItemId | END_INVENTORY_ITEM_ID | — | ✅ |
| 56 | DosTransferOrderDetailsPEOEndItemName | END_ITEM_NAME | — | ✅ |
| 57 | DosTransferOrderDetailsPEOExecSystemDeliverToSubinv | EXEC_SYSTEM_DELIVER_TO_SUBINV | — | ✅ |
| 58 | DosTransferOrderDetailsPEOExecSystemDelvrToLocName | EXEC_SYSTEM_DELVR_TO_LOC_NAME | — | ✅ |
| 59 | DosTransferOrderDetailsPEOExecSystemDelvrToRequestor | EXEC_SYSTEM_DELVR_TO_REQUESTOR | — | ✅ |
| 60 | DosTransferOrderDetailsPEOExecSystemDestnLoctrCode | EXEC_SYSTEM_DESTN_LOCTR_CODE | — | ✅ |
| 61 | DosTransferOrderDetailsPEOExecSystemSourceLoctrCode | EXEC_SYSTEM_SOURCE_LOCTR_CODE | — | ✅ |
| 62 | DosTransferOrderDetailsPEOExecSystemSourceOrgCode | EXEC_SYSTEM_SOURCE_ORG_CODE | — | ✅ |
| 63 | DosTransferOrderDetailsPEOFirmDemandFlag | FIRM_DEMAND_FLAG | — | ✅ |
| 64 | DosTransferOrderDetailsPEOFundsStatus | FUNDS_STATUS | — | ✅ |
| 65 | DosTransferOrderDetailsPEOGroupCode | GROUP_CODE | — | ✅ |
| 66 | DosTransferOrderDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 67 | DosTransferOrderDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 68 | DosTransferOrderDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 69 | DosTransferOrderDetailsPEOLoadType | LOAD_TYPE | — | ✅ |
| 70 | DosTransferOrderDetailsPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 71 | DosTransferOrderDetailsPEONoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 72 | DosTransferOrderDetailsPEONoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 73 | DosTransferOrderDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 74 | DosTransferOrderDetailsPEOPreparerId | PREPARER_ID | — | ✅ |
| 75 | DosTransferOrderDetailsPEOPrimaryDocQuantity | PRIMARY_DOC_QUANTITY | — | ✅ |
| 76 | DosTransferOrderDetailsPEOPrimaryDocQuantityUom | PRIMARY_DOC_QUANTITY_UOM | — | ✅ |
| 77 | DosTransferOrderDetailsPEORepriceFlag | REPRICE_FLAG | — | ✅ |
| 78 | DosTransferOrderDetailsPEORequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 79 | DosTransferOrderDetailsPEOSalesOrderHeaderId | SALES_ORDER_HEADER_ID | — | ✅ |
| 80 | DosTransferOrderDetailsPEOSalesOrderHeaderNumber | SALES_ORDER_HEADER_NUMBER | — | ✅ |
| 81 | DosTransferOrderDetailsPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 82 | DosTransferOrderDetailsPEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 83 | DosTransferOrderDetailsPEOScheduledShipDate | SCHEDULED_SHIP_DATE | — | ✅ |
| 84 | DosTransferOrderDetailsPEOShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 85 | DosTransferOrderDetailsPEOShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 86 | DosTransferOrderDetailsPEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 87 | DosTransferOrderDetailsPEOShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 88 | DosTransferOrderDetailsPEOShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 89 | DosTransferOrderDetailsPEOShippingMethod | SHIPPING_METHOD | — | ✅ |
| 90 | DosTransferOrderDetailsPEOSourceBuId | SOURCE_BU_ID | — | ✅ |
| 91 | DosTransferOrderDetailsPEOSourceLocationId | SOURCE_LOCATION_ID | — | ✅ |
| 92 | DosTransferOrderDetailsPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 93 | DosTransferOrderDetailsPEOSourceSubinventoryCode | SOURCE_SUBINVENTORY_CODE | — | ✅ |
| 94 | DosTransferOrderDetailsPEOSupplyTransferDetailsId | SUPPLY_TRANSFER_DETAILS_ID | 🔑 | ✅ |
| 95 | DosTransferOrderDetailsPEOTrackingLineId | TRACKING_LINE_ID | — | ✅ |
| 96 | DosTransferOrderDetailsPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 97 | DosTransferOrderDetailsPEOTransferOrderHeaderNumber | TRANSFER_ORDER_HEADER_NUMBER | — | ✅ |
| 98 | DosTransferOrderDetailsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 99 | DosTransferOrderDetailsPEOTransferOrderLineNumber | TRANSFER_ORDER_LINE_NUMBER | — | ✅ |
| 100 | DosTransferOrderDetailsPEOTransferPrice | TRANSFER_PRICE | — | ✅ |
| 101 | DosTransferOrderDetailsPEOTransferPriceCurrencyCode | TRANSFER_PRICE_CURRENCY_CODE | — | ✅ |
| 102 | DosTransferOrderDetailsPEOUnitPrice | UNIT_PRICE | — | ✅ |
| 103 | DosTransferOrderDetailsPEOUnitPriceCurrencyCode | UNIT_PRICE_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
