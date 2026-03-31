---
id: DOC-OTHER-PVO-DeliveryPVO
doc_type: system-doc
title: "DeliveryPVO — PVO Cross-Module"
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
  - DeliveryPVO
  - deliverypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Delivery. Acessa as tabelas: INV_ORG_PARAMETERS_V, PER_PERSON_NAMES_F_V, WSH_NEW_DELIVERIES.

**Caminho:** `FscmTopModelAM.WshDeliveriesAM.DeliveryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 3 | 1 | 18 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[wsh_new_deliveries|WSH_NEW_DELIVERIES]] — 93 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 2 | OrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 3 | OrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 2 | CreatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CreatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CreatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 5 | LastUpdatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 6 | LastUpdatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | LastUpdatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | LastUpdatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[wsh_new_deliveries|WSH_NEW_DELIVERIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryId | DELIVERY_ID | 🔑 | ✅ |
| 2 | DeliveryPEOAcceptanceFlag | ACCEPTANCE_FLAG | — | — |
| 3 | DeliveryPEOAcceptedBy | ACCEPTED_BY | — | — |
| 4 | DeliveryPEOAcceptedDate | ACCEPTED_DATE | — | — |
| 5 | DeliveryPEOAcknowledgedBy | ACKNOWLEDGED_BY | — | — |
| 6 | DeliveryPEOActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 7 | DeliveryPEOActualShipDateTime | ACTUAL_SHIP_DATE | — | — |
| 8 | DeliveryPEOAdditionalShipmentInfo | ADDITIONAL_SHIPMENT_INFO | — | — |
| 9 | DeliveryPEOApBatchId | AP_BATCH_ID | — | — |
| 10 | DeliveryPEOAsnDateSent | ASN_DATE_SENT | — | — |
| 11 | DeliveryPEOAsnSeqNumber | ASN_SEQ_NUMBER | — | — |
| 12 | DeliveryPEOAsnStatusCode | ASN_STATUS_CODE | — | — |
| 13 | DeliveryPEOAutoApExcludeFlag | AUTO_AP_EXCLUDE_FLAG | — | — |
| 14 | DeliveryPEOAutoScExcludeFlag | AUTO_SC_EXCLUDE_FLAG | — | — |
| 15 | DeliveryPEOBatchId | BATCH_ID | — | — |
| 16 | DeliveryPEOBillFreightTo | BILL_FREIGHT_TO | — | — |
| 17 | DeliveryPEOBillOfLadingNumber | BILL_OF_LADING_NUMBER | — | ✅ |
| 18 | DeliveryPEOBookingNumber | BOOKING_NUMBER | — | — |
| 19 | DeliveryPEOCarriedBy | CARRIED_BY | — | — |
| 20 | DeliveryPEOCarrierId | CARRIER_ID | — | — |
| 21 | DeliveryPEOCodAmount | COD_AMOUNT | — | — |
| 22 | DeliveryPEOCodChargePaidBy | COD_CHARGE_PAID_BY | — | — |
| 23 | DeliveryPEOCodCurrencyCode | COD_CURRENCY_CODE | — | — |
| 24 | DeliveryPEOCodRemitTo | COD_REMIT_TO | — | — |
| 25 | DeliveryPEOConfirmDate | CONFIRM_DATE | — | ✅ |
| 26 | DeliveryPEOConfirmedBy | CONFIRMED_BY | — | — |
| 27 | DeliveryPEOCreatedBy | CREATED_BY | — | — |
| 28 | DeliveryPEOCreationDate | CREATION_DATE | — | — |
| 29 | DeliveryPEOCurrencyCode | CURRENCY_CODE | — | — |
| 30 | DeliveryPEODeliveredDate | DELIVERED_DATE | — | ✅ |
| 31 | DeliveryPEODeliveryName | DELIVERY_NAME | — | ✅ |
| 32 | DeliveryPEODeliveryType | DELIVERY_TYPE | — | — |
| 33 | DeliveryPEODescription | DESCRIPTION | — | — |
| 34 | DeliveryPEODockCode | DOCK_CODE | — | — |
| 35 | DeliveryPEOEarliestDropoffDate | EARLIEST_DROPOFF_DATE | — | — |
| 36 | DeliveryPEOEarliestPickupDate | EARLIEST_PICKUP_DATE | — | — |
| 37 | DeliveryPEOEntryNumber | ENTRY_NUMBER | — | — |
| 38 | DeliveryPEOExternalSysTxnReference | EXTERNAL_SYS_TXN_REFERENCE | — | — |
| 39 | DeliveryPEOFobCode | FOB_CODE | — | ✅ |
| 40 | DeliveryPEOFobLocationId | FOB_LOCATION_ID | — | — |
| 41 | DeliveryPEOFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 42 | DeliveryPEOFtzNumber | FTZ_NUMBER | — | — |
| 43 | DeliveryPEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 44 | DeliveryPEOHashString | HASH_STRING | — | — |
| 45 | DeliveryPEOHashValue | HASH_VALUE | — | — |
| 46 | DeliveryPEOInBondCode | IN_BOND_CODE | — | — |
| 47 | DeliveryPEOInitialPickupDate | INITIAL_PICKUP_DATE | — | — |
| 48 | DeliveryPEOInitialPickupLocationId | INITIAL_PICKUP_LOCATION_ID | — | — |
| 49 | DeliveryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 50 | DeliveryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 51 | DeliveryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | DeliveryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 53 | DeliveryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 54 | DeliveryPEOLatestDropoffDate | LATEST_DROPOFF_DATE | — | — |
| 55 | DeliveryPEOLatestPickupDate | LATEST_PICKUP_DATE | — | — |
| 56 | DeliveryPEOLoadingOrderFlag | LOADING_ORDER_FLAG | — | — |
| 57 | DeliveryPEOLoadingSequence | LOADING_SEQUENCE | — | — |
| 58 | DeliveryPEOModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 59 | DeliveryPEONetWeight | NET_WEIGHT | — | — |
| 60 | DeliveryPEONumberOfLpn | NUMBER_OF_LPN | — | — |
| 61 | DeliveryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | DeliveryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 63 | DeliveryPEOOutsourcerPartyId | OUTSOURCER_PARTY_ID | — | — |
| 64 | DeliveryPEOPackingSlipNumber | PACKING_SLIP_NUMBER | — | ✅ |
| 65 | DeliveryPEOPackingSlipStatus | PACKING_SLIP_STATUS | — | — |
| 66 | DeliveryPEOPendingInterfaceFlag | PENDING_INTERFACE_FLAG | — | — |
| 67 | DeliveryPEOPlannedFlag | PLANNED_FLAG | — | — |
| 68 | DeliveryPEOPortOfDischarge | PORT_OF_DISCHARGE | — | — |
| 69 | DeliveryPEOPortOfLoading | PORT_OF_LOADING | — | — |
| 70 | DeliveryPEOProblemContactReference | PROBLEM_CONTACT_REFERENCE | — | — |
| 71 | DeliveryPEOReasonOfTransport | REASON_OF_TRANSPORT | — | — |
| 72 | DeliveryPEORequestId | REQUEST_ID | — | — |
| 73 | DeliveryPEORoutingInstructions | ROUTING_INSTRUCTIONS | — | — |
| 74 | DeliveryPEOSealCode | SEAL_CODE | — | ✅ |
| 75 | DeliveryPEOServiceContract | SERVICE_CONTRACT | — | — |
| 76 | DeliveryPEOServiceLevel | SERVICE_LEVEL | — | — |
| 77 | DeliveryPEOShipMethodCode | SHIP_METHOD_CODE | — | — |
| 78 | DeliveryPEOShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 79 | DeliveryPEOShippingMarks | SHIPPING_MARKS | — | — |
| 80 | DeliveryPEOSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 81 | DeliveryPEOSourceHeaderId | SOURCE_HEADER_ID | — | — |
| 82 | DeliveryPEOSourceLineType | SOURCE_LINE_TYPE | — | ✅ |
| 83 | DeliveryPEOStatusCode | STATUS_CODE | — | — |
| 84 | DeliveryPEOUltimateDropoffDate | ULTIMATE_DROPOFF_DATE | — | — |
| 85 | DeliveryPEOUltimateDropoffLocationId | ULTIMATE_DROPOFF_LOCATION_ID | — | — |
| 86 | DeliveryPEOVehicleItemId | VEHICLE_ITEM_ID | — | — |
| 87 | DeliveryPEOVehicleNumber | VEHICLE_NUMBER | — | ✅ |
| 88 | DeliveryPEOVolume | VOLUME | — | ✅ |
| 89 | DeliveryPEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 90 | DeliveryPEOWaybill | WAYBILL | — | ✅ |
| 91 | DeliveryPEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 92 | DeliveryPEOWvFrozenFlag | WV_FROZEN_FLAG | — | — |
| 93 | RcvShipmentNum | RCV_SHIPMENT_NUM | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
