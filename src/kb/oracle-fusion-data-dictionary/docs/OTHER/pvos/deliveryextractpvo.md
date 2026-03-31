---
id: DOC-OTHER-PVO-DeliveryExtractPVO
doc_type: system-doc
title: "DeliveryExtractPVO — PVO Cross-Module"
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
  - DeliveryExtractPVO
  - deliveryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Delivery Extract. Acessa as tabelas: WSH_NEW_DELIVERIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WshBiccExtractAM.DeliveryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 1 | 1 | 96 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wsh_new_deliveries|WSH_NEW_DELIVERIES]] — 96 atributos (1 PKs, 96 BICC)

---

## ⚙️ Atributos

### [[wsh_new_deliveries|WSH_NEW_DELIVERIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryPEOActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 2 | DeliveryPEOAdditionalShipmentInfo | ADDITIONAL_SHIPMENT_INFO | — | ✅ |
| 3 | DeliveryPEOApBatchId | AP_BATCH_ID | — | ✅ |
| 4 | DeliveryPEOAsnDateSent | ASN_DATE_SENT | — | ✅ |
| 5 | DeliveryPEOAsnSeqNumber | ASN_SEQ_NUMBER | — | ✅ |
| 6 | DeliveryPEOAsnStatusCode | ASN_STATUS_CODE | — | ✅ |
| 7 | DeliveryPEOAutoApExcludeFlag | AUTO_AP_EXCLUDE_FLAG | — | ✅ |
| 8 | DeliveryPEOAutoScExcludeFlag | AUTO_SC_EXCLUDE_FLAG | — | ✅ |
| 9 | DeliveryPEOBatchId | BATCH_ID | — | ✅ |
| 10 | DeliveryPEOBillOfLadingNumber | BILL_OF_LADING_NUMBER | — | ✅ |
| 11 | DeliveryPEOBillOfLadingSeqId | BILL_OF_LADING_SEQ_ID | — | ✅ |
| 12 | DeliveryPEOBillOfLadingSignature | BILL_OF_LADING_SIGNATURE | — | ✅ |
| 13 | DeliveryPEOCarrierId | CARRIER_ID | — | ✅ |
| 14 | DeliveryPEOCertificateNumber | CERTIFICATE_NUMBER | — | ✅ |
| 15 | DeliveryPEOCloseBatchId | CLOSE_BATCH_ID | — | ✅ |
| 16 | DeliveryPEOCodAmount | COD_AMOUNT | — | ✅ |
| 17 | DeliveryPEOCodChargePaidBy | COD_CHARGE_PAID_BY | — | ✅ |
| 18 | DeliveryPEOCodCurrencyCode | COD_CURRENCY_CODE | — | ✅ |
| 19 | DeliveryPEOCodRemitTo | COD_REMIT_TO | — | ✅ |
| 20 | DeliveryPEOCommercialInvoiceNumber | COMMERCIAL_INVOICE_NUMBER | — | ✅ |
| 21 | DeliveryPEOCommercialInvoiceSeqId | COMMERCIAL_INVOICE_SEQ_ID | — | ✅ |
| 22 | DeliveryPEOCommercialInvoiceSignature | COMMERCIAL_INVOICE_SIGNATURE | — | ✅ |
| 23 | DeliveryPEOConfirmDate | CONFIRM_DATE | — | ✅ |
| 24 | DeliveryPEOConfirmedBy | CONFIRMED_BY | — | ✅ |
| 25 | DeliveryPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | DeliveryPEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | DeliveryPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 28 | DeliveryPEODeliveryId | DELIVERY_ID | 🔑 | ✅ |
| 29 | DeliveryPEODeliveryName | DELIVERY_NAME | — | ✅ |
| 30 | DeliveryPEODeliveryType | DELIVERY_TYPE | — | ✅ |
| 31 | DeliveryPEODescription | DESCRIPTION | — | ✅ |
| 32 | DeliveryPEODockCode | DOCK_CODE | — | ✅ |
| 33 | DeliveryPEOERecordId | E_RECORD_ID | — | ✅ |
| 34 | DeliveryPEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | ✅ |
| 35 | DeliveryPEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | ✅ |
| 36 | DeliveryPEOExternalSysTxnReference | EXTERNAL_SYS_TXN_REFERENCE | — | ✅ |
| 37 | DeliveryPEOFdProcessingStatus | FD_PROCESSING_STATUS | — | ✅ |
| 38 | DeliveryPEOFobCode | FOB_CODE | — | ✅ |
| 39 | DeliveryPEOFobLocationId | FOB_LOCATION_ID | — | ✅ |
| 40 | DeliveryPEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 41 | DeliveryPEOGrossAmount | GROSS_AMOUNT | — | ✅ |
| 42 | DeliveryPEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 43 | DeliveryPEOHashString | HASH_STRING | — | ✅ |
| 44 | DeliveryPEOHashValue | HASH_VALUE | — | ✅ |
| 45 | DeliveryPEOInitialPickupDate | INITIAL_PICKUP_DATE | — | ✅ |
| 46 | DeliveryPEOInitialPickupLocationId | INITIAL_PICKUP_LOCATION_ID | — | ✅ |
| 47 | DeliveryPEOInterfaceBatchId | INTERFACE_BATCH_ID | — | ✅ |
| 48 | DeliveryPEOJobSetName | JOB_SET_NAME | — | ✅ |
| 49 | DeliveryPEOJobSetPackageName | JOB_SET_PACKAGE_NAME | — | ✅ |
| 50 | DeliveryPEOJobSetProcessId | JOB_SET_PROCESS_ID | — | ✅ |
| 51 | DeliveryPEOKeyVersion | KEY_VERSION | — | ✅ |
| 52 | DeliveryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | DeliveryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 54 | DeliveryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 55 | DeliveryPEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | ✅ |
| 56 | DeliveryPEOLatestPickupDate | LATEST_PICKUP_DATE | — | ✅ |
| 57 | DeliveryPEOLoadingOrderFlag | LOADING_ORDER_FLAG | — | ✅ |
| 58 | DeliveryPEOLoadingSequence | LOADING_SEQUENCE | — | ✅ |
| 59 | DeliveryPEOModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 60 | DeliveryPEONetAmount | NET_AMOUNT | — | ✅ |
| 61 | DeliveryPEONetWeight | NET_WEIGHT | — | ✅ |
| 62 | DeliveryPEONumberOfLpn | NUMBER_OF_LPN | — | ✅ |
| 63 | DeliveryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 64 | DeliveryPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 65 | DeliveryPEOPackingSlipNumber | PACKING_SLIP_NUMBER | — | ✅ |
| 66 | DeliveryPEOPackingSlipSeqId | PACKING_SLIP_SEQ_ID | — | ✅ |
| 67 | DeliveryPEOPackingSlipSignature | PACKING_SLIP_SIGNATURE | — | ✅ |
| 68 | DeliveryPEOPackingSlipStatus | PACKING_SLIP_STATUS | — | ✅ |
| 69 | DeliveryPEOPendingInterfaceFlag | PENDING_INTERFACE_FLAG | — | ✅ |
| 70 | DeliveryPEOPlannedFlag | PLANNED_FLAG | — | ✅ |
| 71 | DeliveryPEOProblemContactReference | PROBLEM_CONTACT_REFERENCE | — | ✅ |
| 72 | DeliveryPEORcvShipmentHeaderId | RCV_SHIPMENT_HEADER_ID | — | ✅ |
| 73 | DeliveryPEORcvShipmentNum | RCV_SHIPMENT_NUM | — | ✅ |
| 74 | DeliveryPEOReasonOfTransport | REASON_OF_TRANSPORT | — | ✅ |
| 75 | DeliveryPEORequestId | REQUEST_ID | — | ✅ |
| 76 | DeliveryPEORoutingInstructions | ROUTING_INSTRUCTIONS | — | ✅ |
| 77 | DeliveryPEOSealCode | SEAL_CODE | — | ✅ |
| 78 | DeliveryPEOServiceLevel | SERVICE_LEVEL | — | ✅ |
| 79 | DeliveryPEOShipMethodCode | SHIP_METHOD_CODE | — | ✅ |
| 80 | DeliveryPEOShipToLocationType | SHIP_TO_LOCATION_TYPE | — | ✅ |
| 81 | DeliveryPEOShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 82 | DeliveryPEOShippingMarks | SHIPPING_MARKS | — | ✅ |
| 83 | DeliveryPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 84 | DeliveryPEOSourceHeaderId | SOURCE_HEADER_ID | — | ✅ |
| 85 | DeliveryPEOSourceLineType | SOURCE_LINE_TYPE | — | ✅ |
| 86 | DeliveryPEOStatusCode | STATUS_CODE | — | ✅ |
| 87 | DeliveryPEOTpShipmentNumber | TP_SHIPMENT_NUMBER | — | ✅ |
| 88 | DeliveryPEOUltimateDropoffDate | ULTIMATE_DROPOFF_DATE | — | ✅ |
| 89 | DeliveryPEOUltimateDropoffLocationId | ULTIMATE_DROPOFF_LOCATION_ID | — | ✅ |
| 90 | DeliveryPEOVehicleItemId | VEHICLE_ITEM_ID | — | ✅ |
| 91 | DeliveryPEOVehicleNumber | VEHICLE_NUMBER | — | ✅ |
| 92 | DeliveryPEOVolume | VOLUME | — | ✅ |
| 93 | DeliveryPEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 94 | DeliveryPEOWaybill | WAYBILL | — | ✅ |
| 95 | DeliveryPEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 96 | DeliveryPEOWvFrozenFlag | WV_FROZEN_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
