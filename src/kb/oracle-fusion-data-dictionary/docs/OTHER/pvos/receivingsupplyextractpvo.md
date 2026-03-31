---
id: DOC-OTHER-PVO-ReceivingSupplyExtractPVO
doc_type: system-doc
title: "ReceivingSupplyExtractPVO — PVO Cross-Module"
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
  - ReceivingSupplyExtractPVO
  - receivingsupplyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingSupplyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receiving Supply Extract. Acessa as tabelas: RCV_SUPPLY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RcvBiccExtractAM.ReceivingSupplyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 1 | 2 | 58 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcv_supply|RCV_SUPPLY]] — 58 atributos (2 PKs, 58 BICC)

---

## ⚙️ Atributos

### [[rcv_supply|RCV_SUPPLY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeFlag | CHANGE_FLAG | — | ✅ |
| 2 | ChangeType | CHANGE_TYPE | — | ✅ |
| 3 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 7 | FromOrganizationId | FROM_ORGANIZATION_ID | — | ✅ |
| 8 | FromSubinventory | FROM_SUBINVENTORY | — | ✅ |
| 9 | IntransitOwningOrgId | INTRANSIT_OWNING_ORG_ID | — | ✅ |
| 10 | InvReservedAttribute1 | INV_RESERVED_ATTRIBUTE1 | — | ✅ |
| 11 | InvReservedAttribute2 | INV_RESERVED_ATTRIBUTE2 | — | ✅ |
| 12 | InvStripingCategory | INV_STRIPING_CATEGORY | — | ✅ |
| 13 | InvUserDefAttribute1 | INV_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 14 | InvUserDefAttribute10 | INV_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 15 | InvUserDefAttribute2 | INV_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 16 | InvUserDefAttribute3 | INV_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 17 | InvUserDefAttribute4 | INV_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 18 | InvUserDefAttribute5 | INV_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 19 | InvUserDefAttribute6 | INV_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 20 | InvUserDefAttribute7 | INV_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 21 | InvUserDefAttribute8 | INV_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 22 | InvUserDefAttribute9 | INV_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 23 | ItemId | ITEM_ID | — | ✅ |
| 24 | ItemRevision | ITEM_REVISION | — | ✅ |
| 25 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 26 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | LocationId | LOCATION_ID | — | ✅ |
| 31 | LpnId | LPN_ID | — | ✅ |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | PoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 34 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 35 | PoLineId | PO_LINE_ID | — | ✅ |
| 36 | PoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 37 | ProjectId | PROJECT_ID | — | ✅ |
| 38 | Quantity | QUANTITY | — | ✅ |
| 39 | RcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 40 | ReceiptDate | RECEIPT_DATE | — | ✅ |
| 41 | ReqHeaderId | REQ_HEADER_ID | — | ✅ |
| 42 | ReqLineId | REQ_LINE_ID | — | ✅ |
| 43 | RequestId | REQUEST_ID | — | ✅ |
| 44 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 45 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 46 | ShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 47 | ShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 48 | SupplySourceId | SUPPLY_SOURCE_ID | 🔑 | ✅ |
| 49 | SupplyTypeCode | SUPPLY_TYPE_CODE | 🔑 | ✅ |
| 50 | TaskId | TASK_ID | — | ✅ |
| 51 | ToLocatorId | TO_LOCATOR_ID | — | ✅ |
| 52 | ToOrgPrimaryQuantity | TO_ORG_PRIMARY_QUANTITY | — | ✅ |
| 53 | ToOrgPrimaryUomCode | TO_ORG_PRIMARY_UOM_CODE | — | ✅ |
| 54 | ToOrganizationId | TO_ORGANIZATION_ID | — | ✅ |
| 55 | ToSubinventory | TO_SUBINVENTORY | — | ✅ |
| 56 | TransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 57 | TransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 58 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
