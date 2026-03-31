---
id: DOC-OTHER-PVO-ItemClassP1
doc_type: system-doc
title: "ItemClassP1 — PVO Cross-Module"
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
  - ItemClassP1
  - itemclassp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemClassP1

## 📌 Visão Geral

View Object para extração BICC de dados de Item Class P1. Acessa as tabelas: EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL.

**Caminho:** `FscmTopModelAM.ItemClassesAM.ItemClassP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 2 | 1 | 15 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 42 atributos (1 PKs, 8 BICC)
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 15 atributos (7 BICC)

---

## ⚙️ Atributos

### [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 2 | ItemClassBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 3 | ItemClassBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 4 | ItemClassBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 5 | ItemClassBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 6 | ItemClassBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 7 | ItemClassBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 8 | ItemClassBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 9 | ItemClassBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 10 | ItemClassBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 11 | ItemClassBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 12 | ItemClassBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 13 | ItemClassBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 14 | ItemClassBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 15 | ItemClassBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 16 | ItemClassBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 17 | ItemClassBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 18 | ItemClassBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 19 | ItemClassBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 20 | ItemClassBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 21 | ItemClassBasePEOChangeOrderTypeId | CHANGE_ORDER_TYPE_ID | — | — |
| 22 | ItemClassBasePEOCreatedBy | CREATED_BY | — | — |
| 23 | ItemClassBasePEOCreationDate | CREATION_DATE | — | — |
| 24 | ItemClassBasePEODefaultItemClassFlag | DEFAULT_ITEM_CLASS_FLAG | — | ✅ |
| 25 | ItemClassBasePEOItemClassCode | ITEM_CLASS_CODE | — | ✅ |
| 26 | ItemClassBasePEOItemCreationAllowedFlag | ITEM_CREATION_ALLOWED_FLAG | — | ✅ |
| 27 | ItemClassBasePEOItemDescGenMethod | ITEM_DESC_GEN_METHOD | — | — |
| 28 | ItemClassBasePEOItemNumGenMethod | ITEM_NUM_GEN_METHOD | — | — |
| 29 | ItemClassBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 30 | ItemClassBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 31 | ItemClassBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | ItemClassBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | ItemClassBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | ItemClassBasePEONirChangeTypeId | NIR_CHANGE_TYPE_ID | — | — |
| 35 | ItemClassBasePEONirReqd | NIR_REQD | — | ✅ |
| 36 | ItemClassBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | ItemClassBasePEOParentItemClassId | PARENT_ITEM_CLASS_ID | — | ✅ |
| 38 | ItemClassBasePEORequestId | REQUEST_ID | — | — |
| 39 | ItemClassBasePEOVersionEnabledFlag | VERSION_ENABLED_FLAG | — | — |
| 40 | ItemClassCode | ITEM_CLASS_CODE | — | ✅ |
| 41 | ItemClassId | ITEM_CLASS_ID | 🔑 | ✅ |
| 42 | ItemClassId2 | ITEM_CLASS_ID | — | — |

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Description1 | DESCRIPTION | — | ✅ |
| 5 | ItemClassId1 | ITEM_CLASS_ID | — | — |
| 6 | ItemClassId3 | ITEM_CLASS_ID | — | — |
| 7 | ItemClassName | ITEM_CLASS_NAME | — | ✅ |
| 8 | ItemClassName1 | ITEM_CLASS_NAME | — | ✅ |
| 9 | Language | LANGUAGE | — | ✅ |
| 10 | Language1 | LANGUAGE | — | — |
| 11 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
