---
id: DOC-OTHER-PVO-PackingUnitExtractPVO
doc_type: system-doc
title: "PackingUnitExtractPVO — PVO Cross-Module"
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
  - PackingUnitExtractPVO
  - packingunitextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PackingUnitExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Packing Unit Extract. Acessa as tabelas: INV_LICENSE_PLATE_NUMBERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.PackingUnitExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 114 | 1 | 0 | 73 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[inv_license_plate_numbers|INV_LICENSE_PLATE_NUMBERS]] — 114 atributos (73 BICC)

---

## ⚙️ Atributos

### [[inv_license_plate_numbers|INV_LICENSE_PLATE_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PackingUnitPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PackingUnitPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PackingUnitPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PackingUnitPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PackingUnitPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PackingUnitPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PackingUnitPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PackingUnitPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PackingUnitPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PackingUnitPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PackingUnitPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PackingUnitPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PackingUnitPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PackingUnitPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | PackingUnitPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | PackingUnitPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | PackingUnitPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | PackingUnitPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | PackingUnitPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | PackingUnitPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | PackingUnitPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | PackingUnitPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | PackingUnitPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | PackingUnitPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | PackingUnitPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | PackingUnitPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | PackingUnitPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | PackingUnitPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | PackingUnitPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | PackingUnitPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | PackingUnitPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | PackingUnitPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | PackingUnitPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | PackingUnitPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | PackingUnitPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | PackingUnitPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | PackingUnitPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | PackingUnitPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | PackingUnitPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | PackingUnitPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | PackingUnitPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | PackingUnitPEOBatchId | BATCH_ID | — | ✅ |
| 43 | PackingUnitPEOCarrierId | CARRIER_ID | — | ✅ |
| 44 | PackingUnitPEOContainerTypeCode | CONTAINER_TYPE_CODE | — | ✅ |
| 45 | PackingUnitPEOContainerVolume | CONTAINER_VOLUME | — | ✅ |
| 46 | PackingUnitPEOContainerVolumeUom | CONTAINER_VOLUME_UOM | — | ✅ |
| 47 | PackingUnitPEOContentVolume | CONTENT_VOLUME | — | ✅ |
| 48 | PackingUnitPEOContentVolumeUomCode | CONTENT_VOLUME_UOM_CODE | — | ✅ |
| 49 | PackingUnitPEOCreatedBy | CREATED_BY | — | ✅ |
| 50 | PackingUnitPEOCreationDate | CREATION_DATE | — | ✅ |
| 51 | PackingUnitPEODeliveryId | DELIVERY_ID | — | ✅ |
| 52 | PackingUnitPEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | ✅ |
| 53 | PackingUnitPEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | ✅ |
| 54 | PackingUnitPEOFillPercent | FILL_PERCENT | — | ✅ |
| 55 | PackingUnitPEOFilledVolume | FILLED_VOLUME | — | ✅ |
| 56 | PackingUnitPEOFobCode | FOB_CODE | — | ✅ |
| 57 | PackingUnitPEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 58 | PackingUnitPEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 59 | PackingUnitPEOGrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | ✅ |
| 60 | PackingUnitPEOHomogeneousContainer | HOMOGENEOUS_CONTAINER | — | ✅ |
| 61 | PackingUnitPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 62 | PackingUnitPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 63 | PackingUnitPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 64 | PackingUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | PackingUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 66 | PackingUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 67 | PackingUnitPEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | ✅ |
| 68 | PackingUnitPEOLatestPickupDate | LATEST_PICKUP_DATE | — | ✅ |
| 69 | PackingUnitPEOLicensePlateNumber | LICENSE_PLATE_NUMBER | — | ✅ |
| 70 | PackingUnitPEOLocatorId | LOCATOR_ID | — | ✅ |
| 71 | PackingUnitPEOLotNumber | LOT_NUMBER | — | ✅ |
| 72 | PackingUnitPEOLpnContext | LPN_CONTEXT | — | ✅ |
| 73 | PackingUnitPEOLpnId | LPN_ID | — | ✅ |
| 74 | PackingUnitPEOLpnReusability | LPN_REUSABILITY | — | ✅ |
| 75 | PackingUnitPEOMasterSerialNumber | MASTER_SERIAL_NUMBER | — | ✅ |
| 76 | PackingUnitPEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | ✅ |
| 77 | PackingUnitPEOMaximumVolume | MAXIMUM_VOLUME | — | ✅ |
| 78 | PackingUnitPEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | ✅ |
| 79 | PackingUnitPEOModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 80 | PackingUnitPEONetWeight | NET_WEIGHT | — | ✅ |
| 81 | PackingUnitPEONetWeightUomCode | NET_WEIGHT_UOM_CODE | — | ✅ |
| 82 | PackingUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 83 | PackingUnitPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 84 | PackingUnitPEOOutermostLpnId | OUTERMOST_LPN_ID | — | ✅ |
| 85 | PackingUnitPEOOutsourcerPartyId | OUTSOURCER_PARTY_ID | — | ✅ |
| 86 | PackingUnitPEOPackingInstructions | PACKING_INSTRUCTIONS | — | ✅ |
| 87 | PackingUnitPEOParentLpnId | PARENT_LPN_ID | — | ✅ |
| 88 | PackingUnitPEORequestId | REQUEST_ID | — | ✅ |
| 89 | PackingUnitPEORevision | REVISION | — | ✅ |
| 90 | PackingUnitPEOSealCode | SEAL_CODE | — | ✅ |
| 91 | PackingUnitPEOSealedStatus | SEALED_STATUS | — | ✅ |
| 92 | PackingUnitPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 93 | PackingUnitPEOServiceLevel | SERVICE_LEVEL | — | ✅ |
| 94 | PackingUnitPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 95 | PackingUnitPEOShipMethodCode | SHIP_METHOD_CODE | — | ✅ |
| 96 | PackingUnitPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 97 | PackingUnitPEOShipToLocationType | SHIP_TO_LOCATION_TYPE | — | ✅ |
| 98 | PackingUnitPEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 99 | PackingUnitPEOShippingInstructions | SHIPPING_INSTRUCTIONS | — | ✅ |
| 100 | PackingUnitPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 101 | PackingUnitPEOSourceHeaderId | SOURCE_HEADER_ID | — | ✅ |
| 102 | PackingUnitPEOSourceLineDetailId | SOURCE_LINE_DETAIL_ID | — | ✅ |
| 103 | PackingUnitPEOSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 104 | PackingUnitPEOSourceName | SOURCE_NAME | — | ✅ |
| 105 | PackingUnitPEOSourceTypeId | SOURCE_TYPE_ID | — | ✅ |
| 106 | PackingUnitPEOStatusId | STATUS_ID | — | ✅ |
| 107 | PackingUnitPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 108 | PackingUnitPEOTareWeight | TARE_WEIGHT | — | ✅ |
| 109 | PackingUnitPEOTareWeightUomCode | TARE_WEIGHT_UOM_CODE | — | ✅ |
| 110 | PackingUnitPEOTpShipmentNumber | TP_SHIPMENT_NUMBER | — | ✅ |
| 111 | PackingUnitPEOTrackingNumber | TRACKING_NUMBER | — | ✅ |
| 112 | PackingUnitPEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 113 | PackingUnitPEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 114 | PackingUnitPEOWvFrozenFlag | WV_FROZEN_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
