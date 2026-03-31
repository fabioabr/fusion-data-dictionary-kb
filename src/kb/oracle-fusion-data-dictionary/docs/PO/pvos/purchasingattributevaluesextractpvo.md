---
id: DOC-PO-PVO-PurchasingAttributeValuesExtractPVO
doc_type: system-doc
title: "PurchasingAttributeValuesExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingAttributeValuesExtractPVO
  - purchasingattributevaluesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAttributeValuesExtractPVO

## 📌 Visão Geral

Extrai os valores de atributos descritivos flexíveis (DFF) de documentos de compra para carga BICC. Permite análise de campos customizados utilizados pela organização em procurement.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingAttributeValuesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_attribute_values|PO_ATTRIBUTE_VALUES]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[po_attribute_values|PO_ATTRIBUTE_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttachmentUrl | ATTACHMENT_URL | — | ✅ |
| 2 | AttributeValuesId | ATTRIBUTE_VALUES_ID | 🔑 | ✅ |
| 3 | Availability | AVAILABILITY | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | LastUpdatedProgram | LAST_UPDATED_PROGRAM | — | ✅ |
| 12 | LeadTime | LEAD_TIME | — | ✅ |
| 13 | ManufacturerPartNum | MANUFACTURER_PART_NUM | — | ✅ |
| 14 | ManufacturerUrl | MANUFACTURER_URL | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | PackagingString | PACKAGING_STRING | — | ✅ |
| 17 | Picture | PICTURE | — | ✅ |
| 18 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 19 | PoLineId | PO_LINE_ID | — | ✅ |
| 20 | PrcBuId | PRC_BU_ID | — | ✅ |
| 21 | RebuildSearchIndexFlag | REBUILD_SEARCH_INDEX_FLAG | — | ✅ |
| 22 | RequestId | REQUEST_ID | — | ✅ |
| 23 | RoundingFactor | ROUNDING_FACTOR | — | ✅ |
| 24 | SupplierUrl | SUPPLIER_URL | — | ✅ |
| 25 | ThumbnailImage | THUMBNAIL_IMAGE | — | ✅ |
| 26 | Unspsc | UNSPSC | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
