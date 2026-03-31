---
id: DOC-OTHER-PVO-ItemSupplierAssociationExtractPVO
doc_type: system-doc
title: "ItemSupplierAssociationExtractPVO — PVO Cross-Module"
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
  - ItemSupplierAssociationExtractPVO
  - itemsupplierassociationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemSupplierAssociationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Supplier Association Extract. Acessa as tabelas: EGO_ITEM_ASSOCIATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemSupplierAssociationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 7 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 18 atributos (7 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAssociationPEOAcdType | ACD_TYPE | 🔑 | ✅ |
| 2 | ItemSupplierAssociationPEOAssociationId | ASSOCIATION_ID | — | ✅ |
| 3 | ItemSupplierAssociationPEOChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |
| 4 | ItemSupplierAssociationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ItemSupplierAssociationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ItemSupplierAssociationPEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 7 | ItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 8 | ItemSupplierAssociationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ItemSupplierAssociationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ItemSupplierAssociationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 12 | ItemSupplierAssociationPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 13 | ItemSupplierAssociationPEOStatusCode | STATUS_CODE | — | ✅ |
| 14 | ItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | 🔑 | ✅ |
| 15 | ItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | 🔑 | ✅ |
| 16 | ItemSupplierAssociationPEOVersionEndDate | VERSION_END_DATE | — | ✅ |
| 17 | ItemSupplierAssociationPEOVersionId | VERSION_ID | 🔑 | ✅ |
| 18 | ItemSupplierAssociationPEOVersionStartDate | VERSION_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
