---
id: DOC-OTHER-PVO-ItemSupplierAssociation
doc_type: system-doc
title: "ItemSupplierAssociation — PVO Cross-Module"
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
  - ItemSupplierAssociation
  - itemsupplierassociation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemSupplierAssociation

## 📌 Visão Geral

View Object para extração BICC de dados de Item Supplier Association. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemSupplierAssociation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 7 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 26 atributos (7 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcdType | ACD_TYPE | 🔑 | ✅ |
| 2 | AssociationId | ASSOCIATION_ID | — | ✅ |
| 3 | ChangeBitMap | CHANGE_BIT_MAP | — | ✅ |
| 4 | ChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | ImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 8 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 9 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 10 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 16 | PrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 17 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 18 | ProgramName | PROGRAM_NAME | — | ✅ |
| 19 | RequestId | REQUEST_ID | — | ✅ |
| 20 | StatusCode | STATUS_CODE | — | ✅ |
| 21 | StyleItemId | STYLE_ITEM_ID | — | ✅ |
| 22 | SupplierId | SUPPLIER_ID | 🔑 | ✅ |
| 23 | SupplierSiteId | SUPPLIER_SITE_ID | 🔑 | ✅ |
| 24 | VersionEndDate | VERSION_END_DATE | — | ✅ |
| 25 | VersionId | VERSION_ID | 🔑 | ✅ |
| 26 | VersionStartDate | VERSION_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
