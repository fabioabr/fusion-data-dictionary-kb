---
id: DOC-OTHER-PVO-InvItemLocatorExtractPVO
doc_type: system-doc
title: "InvItemLocatorExtractPVO — PVO Cross-Module"
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
  - InvItemLocatorExtractPVO
  - invitemlocatorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvItemLocatorExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Item Locator Extract. Acessa as tabelas: INV_SECONDARY_LOCATORS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvItemLocatorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 3 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_secondary_locators|INV_SECONDARY_LOCATORS]] — 24 atributos (3 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[inv_secondary_locators|INV_SECONDARY_LOCATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemLocatorPEOCountRequired | COUNT_REQUIRED | — | ✅ |
| 2 | ItemLocatorPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ItemLocatorPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ItemLocatorPEODefaultCountTypeCode | DEFAULT_COUNT_TYPE_CODE | — | ✅ |
| 5 | ItemLocatorPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 6 | ItemLocatorPEOItemLocatorId | ITEM_LOCATOR_ID | — | ✅ |
| 7 | ItemLocatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | ItemLocatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | ItemLocatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ItemLocatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ItemLocatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ItemLocatorPEOMaximumQuantity | MAXIMUM_QUANTITY | — | ✅ |
| 13 | ItemLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | ItemLocatorPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 15 | ItemLocatorPEOParLevel | PAR_LEVEL | — | ✅ |
| 16 | ItemLocatorPEOParMaxQty | PAR_MAX_QTY | — | ✅ |
| 17 | ItemLocatorPEOParUomCode | PAR_UOM_CODE | — | ✅ |
| 18 | ItemLocatorPEOPickingOrder | PICKING_ORDER | — | ✅ |
| 19 | ItemLocatorPEOPrimaryLocatorFlag | PRIMARY_LOCATOR_FLAG | — | ✅ |
| 20 | ItemLocatorPEOQtyCountTolerance | QTY_COUNT_TOLERANCE | — | ✅ |
| 21 | ItemLocatorPEORequestId | REQUEST_ID | — | ✅ |
| 22 | ItemLocatorPEOSecondaryLocator | SECONDARY_LOCATOR | 🔑 | ✅ |
| 23 | ItemLocatorPEOStatusId | STATUS_ID | — | ✅ |
| 24 | ItemLocatorPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
