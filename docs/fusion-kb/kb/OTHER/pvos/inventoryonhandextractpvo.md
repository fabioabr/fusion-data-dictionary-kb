---
id: DOC-OTHER-PVO-InventoryOnhandExtractPVO
doc_type: system-doc
title: "InventoryOnhandExtractPVO — PVO Cross-Module"
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
  - InventoryOnhandExtractPVO
  - inventoryonhandextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryOnhandExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Onhand Extract. Acessa as tabelas: INV_ONHAND_QUANTITIES_DETAIL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InventoryOnhandExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 1 | 1 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_onhand_quantities_detail|INV_ONHAND_QUANTITIES_DETAIL]] — 43 atributos (1 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[inv_onhand_quantities_detail|INV_ONHAND_QUANTITIES_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvOnhandQuantityPEOAgingExpirationDate | AGING_EXPIRATION_DATE | — | ✅ |
| 2 | InvOnhandQuantityPEOAgingOnsetDate | AGING_ONSET_DATE | — | ✅ |
| 3 | InvOnhandQuantityPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 4 | InvOnhandQuantityPEOCreateTransactionId | CREATE_TRANSACTION_ID | — | ✅ |
| 5 | InvOnhandQuantityPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InvOnhandQuantityPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InvOnhandQuantityPEODateReceived | DATE_RECEIVED | — | ✅ |
| 8 | InvOnhandQuantityPEOInvReservedAttribute1 | INV_RESERVED_ATTRIBUTE1 | — | ✅ |
| 9 | InvOnhandQuantityPEOInvReservedAttribute2 | INV_RESERVED_ATTRIBUTE2 | — | ✅ |
| 10 | InvOnhandQuantityPEOInvStripingCategory | INV_STRIPING_CATEGORY | — | ✅ |
| 11 | InvOnhandQuantityPEOInvUserDefAttribute1 | INV_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 12 | InvOnhandQuantityPEOInvUserDefAttribute10 | INV_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 13 | InvOnhandQuantityPEOInvUserDefAttribute2 | INV_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 14 | InvOnhandQuantityPEOInvUserDefAttribute3 | INV_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 15 | InvOnhandQuantityPEOInvUserDefAttribute4 | INV_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 16 | InvOnhandQuantityPEOInvUserDefAttribute5 | INV_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 17 | InvOnhandQuantityPEOInvUserDefAttribute6 | INV_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 18 | InvOnhandQuantityPEOInvUserDefAttribute7 | INV_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 19 | InvOnhandQuantityPEOInvUserDefAttribute8 | INV_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 20 | InvOnhandQuantityPEOInvUserDefAttribute9 | INV_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 21 | InvOnhandQuantityPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 22 | InvOnhandQuantityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | InvOnhandQuantityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | InvOnhandQuantityPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | InvOnhandQuantityPEOLocatorId | LOCATOR_ID | — | ✅ |
| 26 | InvOnhandQuantityPEOLotNumber | LOT_NUMBER | — | ✅ |
| 27 | InvOnhandQuantityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | InvOnhandQuantityPEOOnhandQuantitiesId | ONHAND_QUANTITIES_ID | 🔑 | ✅ |
| 29 | InvOnhandQuantityPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 30 | InvOnhandQuantityPEOOrigDateReceived | ORIG_DATE_RECEIVED | — | ✅ |
| 31 | InvOnhandQuantityPEOOrigSourceTxnId | ORIG_SOURCE_TXN_ID | — | ✅ |
| 32 | InvOnhandQuantityPEOOwningEntityId | OWNING_ENTITY_ID | — | ✅ |
| 33 | InvOnhandQuantityPEOOwningType | OWNING_TYPE | — | ✅ |
| 34 | InvOnhandQuantityPEOPrimaryTransactionQuantity | PRIMARY_TRANSACTION_QUANTITY | — | ✅ |
| 35 | InvOnhandQuantityPEOProjectId | PROJECT_ID | — | ✅ |
| 36 | InvOnhandQuantityPEORevision | REVISION | — | ✅ |
| 37 | InvOnhandQuantityPEOSecondaryTransactionQuantity | SECONDARY_TRANSACTION_QUANTITY | — | ✅ |
| 38 | InvOnhandQuantityPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 39 | InvOnhandQuantityPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 40 | InvOnhandQuantityPEOTaskId | TASK_ID | — | ✅ |
| 41 | InvOnhandQuantityPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 42 | InvOnhandQuantityPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 43 | InvOnhandQuantityPEOUpdateTransactionId | UPDATE_TRANSACTION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
