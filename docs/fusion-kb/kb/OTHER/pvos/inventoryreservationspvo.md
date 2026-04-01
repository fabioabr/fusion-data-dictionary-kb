---
id: DOC-OTHER-PVO-InventoryReservationsPVO
doc_type: system-doc
title: "InventoryReservationsPVO — PVO Cross-Module"
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
  - InventoryReservationsPVO
  - inventoryreservationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryReservationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Reservations. Acessa as tabelas: INV_RESERVATIONS.

**Caminho:** `FscmTopModelAM.InventoryAM.InventoryReservationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 10 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[inv_reservations|INV_RESERVATIONS]] — 64 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[inv_reservations|INV_RESERVATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContainerLpnId | CONTAINER_LPN_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | CrossdockCriteriaId | CROSSDOCK_CRITERIA_ID | — | — |
| 5 | CrossdockFlag | CROSSDOCK_FLAG | — | — |
| 6 | DemandShipDate | DEMAND_SHIP_DATE | — | — |
| 7 | DemandSourceDelivery | DEMAND_SOURCE_DELIVERY | — | — |
| 8 | DemandSourceHeaderId | DEMAND_SOURCE_HEADER_ID | — | — |
| 9 | DemandSourceLineDetail | DEMAND_SOURCE_LINE_DETAIL | — | — |
| 10 | DemandSourceLineId | DEMAND_SOURCE_LINE_ID | — | — |
| 11 | DemandSourceName | DEMAND_SOURCE_NAME | — | — |
| 12 | DemandSourceTypeId | DEMAND_SOURCE_TYPE_ID | — | — |
| 13 | DetailedQuantity | DETAILED_QUANTITY | — | ✅ |
| 14 | ExceptionCode | EXCEPTION_CODE | — | — |
| 15 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 17 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | LocatorId | LOCATOR_ID | — | ✅ |
| 22 | LotNumber | LOT_NUMBER | — | — |
| 23 | LpnId | LPN_ID | — | — |
| 24 | NColumn1 | N_COLUMN1 | — | — |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 27 | OrigDemandSourceHeaderId | ORIG_DEMAND_SOURCE_HEADER_ID | — | — |
| 28 | OrigDemandSourceLineDetail | ORIG_DEMAND_SOURCE_LINE_DETAIL | — | — |
| 29 | OrigDemandSourceLineId | ORIG_DEMAND_SOURCE_LINE_ID | — | — |
| 30 | OrigDemandSourceLineNumber | ORIG_DEMAND_SOURCE_LINE_NUMBER | — | — |
| 31 | OrigDemandSourceTypeId | ORIG_DEMAND_SOURCE_TYPE_ID | — | — |
| 32 | OrigSupplySourceHeaderId | ORIG_SUPPLY_SOURCE_HEADER_ID | — | — |
| 33 | OrigSupplySourceLineDetail | ORIG_SUPPLY_SOURCE_LINE_DETAIL | — | — |
| 34 | OrigSupplySourceLineId | ORIG_SUPPLY_SOURCE_LINE_ID | — | — |
| 35 | OrigSupplySourceTypeId | ORIG_SUPPLY_SOURCE_TYPE_ID | — | — |
| 36 | PrimaryReservationQuantity | PRIMARY_RESERVATION_QUANTITY | — | ✅ |
| 37 | PrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 38 | ProjectId | PROJECT_ID | — | — |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | RequirementDate | REQUIREMENT_DATE | — | — |
| 41 | ReservationId | RESERVATION_ID | 🔑 | ✅ |
| 42 | ReservationQuantity | RESERVATION_QUANTITY | — | — |
| 43 | ReservationUomCode | RESERVATION_UOM_CODE | — | — |
| 44 | Revision | REVISION | — | — |
| 45 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 46 | SalesOrderShipmentNumber | SALES_ORDER_SHIPMENT_NUMBER | — | — |
| 47 | SecondaryDetailedQuantity | SECONDARY_DETAILED_QUANTITY | — | — |
| 48 | SecondaryReservationQuantity | SECONDARY_RESERVATION_QUANTITY | — | — |
| 49 | SecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 50 | SerialReservationQuantity | SERIAL_RESERVATION_QUANTITY | — | — |
| 51 | ShipReadyFlag | SHIP_READY_FLAG | — | — |
| 52 | ShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 53 | SourceFulfillmentLineId | SOURCE_FULFILLMENT_LINE_ID | — | — |
| 54 | SourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 55 | SourceShipmentNumber | SOURCE_SHIPMENT_NUMBER | — | — |
| 56 | StagedFlag | STAGED_FLAG | — | — |
| 57 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 58 | SupplyReceiptDate | SUPPLY_RECEIPT_DATE | — | — |
| 59 | SupplySourceHeaderId | SUPPLY_SOURCE_HEADER_ID | — | — |
| 60 | SupplySourceLineDetail | SUPPLY_SOURCE_LINE_DETAIL | — | — |
| 61 | SupplySourceLineId | SUPPLY_SOURCE_LINE_ID | — | — |
| 62 | SupplySourceName | SUPPLY_SOURCE_NAME | — | — |
| 63 | SupplySourceTypeId | SUPPLY_SOURCE_TYPE_ID | — | ✅ |
| 64 | TaskId | TASK_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
