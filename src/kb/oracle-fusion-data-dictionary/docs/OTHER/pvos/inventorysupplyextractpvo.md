---
id: DOC-OTHER-PVO-InventorySupplyExtractPVO
doc_type: system-doc
title: "InventorySupplyExtractPVO — PVO Cross-Module"
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
  - InventorySupplyExtractPVO
  - inventorysupplyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventorySupplyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Supply Extract. Acessa as tabelas: INV_ORG_PARAMETERS, INV_SUPPLY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InventorySupplyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 2 | 2 | 49 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 1 atributos (1 BICC)
- [[inv_supply|INV_SUPPLY]] — 48 atributos (2 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgParameterPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

### [[inv_supply|INV_SUPPLY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventorySupplyPEOCategoryId | CATEGORY_ID | — | ✅ |
| 2 | InventorySupplyPEOChangeFlag | CHANGE_FLAG | — | ✅ |
| 3 | InventorySupplyPEOChangeType | CHANGE_TYPE | — | ✅ |
| 4 | InventorySupplyPEOCostGroupId | COST_GROUP_ID | — | ✅ |
| 5 | InventorySupplyPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InventorySupplyPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InventorySupplyPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 8 | InventorySupplyPEOExpectedDeliveryDate | EXPECTED_DELIVERY_DATE | — | ✅ |
| 9 | InventorySupplyPEOFromOrganizationId | FROM_ORGANIZATION_ID | — | ✅ |
| 10 | InventorySupplyPEOFromSubinventory | FROM_SUBINVENTORY | — | ✅ |
| 11 | InventorySupplyPEOIntransitOwningOrgId | INTRANSIT_OWNING_ORG_ID | — | ✅ |
| 12 | InventorySupplyPEOItemId | ITEM_ID | — | ✅ |
| 13 | InventorySupplyPEOItemRevision | ITEM_REVISION | — | ✅ |
| 14 | InventorySupplyPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 15 | InventorySupplyPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 16 | InventorySupplyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | InventorySupplyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | InventorySupplyPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | InventorySupplyPEOLocationId | LOCATION_ID | — | ✅ |
| 20 | InventorySupplyPEOMrpDestinationTypeCode | MRP_DESTINATION_TYPE_CODE | — | ✅ |
| 21 | InventorySupplyPEOMrpExpectedDeliveryDate | MRP_EXPECTED_DELIVERY_DATE | — | ✅ |
| 22 | InventorySupplyPEOMrpPrimaryQuantity | MRP_PRIMARY_QUANTITY | — | ✅ |
| 23 | InventorySupplyPEOMrpPrimaryUom | MRP_PRIMARY_UOM | — | ✅ |
| 24 | InventorySupplyPEOMrpToOrganizationId | MRP_TO_ORGANIZATION_ID | — | ✅ |
| 25 | InventorySupplyPEOMrpToSubinventory | MRP_TO_SUBINVENTORY | — | ✅ |
| 26 | InventorySupplyPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 27 | InventorySupplyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | InventorySupplyPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 29 | InventorySupplyPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 30 | InventorySupplyPEOPoLineId | PO_LINE_ID | — | ✅ |
| 31 | InventorySupplyPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 32 | InventorySupplyPEOQuantity | QUANTITY | — | ✅ |
| 33 | InventorySupplyPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 34 | InventorySupplyPEOReceiptDate | RECEIPT_DATE | — | ✅ |
| 35 | InventorySupplyPEOReqHeaderId | REQ_HEADER_ID | — | ✅ |
| 36 | InventorySupplyPEOReqLineId | REQ_LINE_ID | — | ✅ |
| 37 | InventorySupplyPEORequestId | REQUEST_ID | — | ✅ |
| 38 | InventorySupplyPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 39 | InventorySupplyPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 40 | InventorySupplyPEOSupplySourceId | SUPPLY_SOURCE_ID | 🔑 | ✅ |
| 41 | InventorySupplyPEOSupplyTypeCode | SUPPLY_TYPE_CODE | 🔑 | ✅ |
| 42 | InventorySupplyPEOToOrgPrimaryQuantity | TO_ORG_PRIMARY_QUANTITY | — | ✅ |
| 43 | InventorySupplyPEOToOrgPrimaryUomCode | TO_ORG_PRIMARY_UOM_CODE | — | ✅ |
| 44 | InventorySupplyPEOToOrganizationId | TO_ORGANIZATION_ID | — | ✅ |
| 45 | InventorySupplyPEOToSubinventory | TO_SUBINVENTORY | — | ✅ |
| 46 | InventorySupplyPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 47 | InventorySupplyPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 48 | InventorySupplyPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
