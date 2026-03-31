---
id: DOC-OTHER-PVO-TrackedObjectRelatedPartyRef
doc_type: system-doc
title: "TrackedObjectRelatedPartyRef — PVO Cross-Module"
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
  - TrackedObjectRelatedPartyRef
  - trackedobjectrelatedpartyref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TrackedObjectRelatedPartyRef

## 📌 Visão Geral

View Object para extração BICC de dados de Tracked Object Related Party Ref. Acessa as tabelas: CSE_TRACKED_OBJECTS, CSE_TRACKED_OBJECT_REFS.

**Caminho:** `FscmTopModelAM.ProductGenealogyAM.TrackedObjectRelatedPartyRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 2 | 50 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_tracked_objects|CSE_TRACKED_OBJECTS]] — 29 atributos (1 PKs, 29 BICC)
- [[cse_tracked_object_refs|CSE_TRACKED_OBJECT_REFS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cse_tracked_objects|CSE_TRACKED_OBJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrackedObjectPEOAdfbcPackage | ADFBC_PACKAGE | — | ✅ |
| 2 | TrackedObjectPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | TrackedObjectPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | TrackedObjectPEODataSource | DATA_SOURCE | — | ✅ |
| 5 | TrackedObjectPEODataSourceType | DATA_SOURCE_TYPE | — | ✅ |
| 6 | TrackedObjectPEODisplayAttribute1 | DISPLAY_ATTRIBUTE1 | — | ✅ |
| 7 | TrackedObjectPEODisplayAttribute2 | DISPLAY_ATTRIBUTE2 | — | ✅ |
| 8 | TrackedObjectPEODisplayAttribute3 | DISPLAY_ATTRIBUTE3 | — | ✅ |
| 9 | TrackedObjectPEODisplayAttribute4 | DISPLAY_ATTRIBUTE4 | — | ✅ |
| 10 | TrackedObjectPEODisplayAttribute5 | DISPLAY_ATTRIBUTE5 | — | ✅ |
| 11 | TrackedObjectPEOInvTxnSourceTypeId | INV_TXN_SOURCE_TYPE_ID | — | ✅ |
| 12 | TrackedObjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | TrackedObjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | TrackedObjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | TrackedObjectPEOObjectCode | OBJECT_CODE | — | ✅ |
| 16 | TrackedObjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | TrackedObjectPEOParentObjectCode | PARENT_OBJECT_CODE | — | ✅ |
| 18 | TrackedObjectPEOPkAttribute1 | PK_ATTRIBUTE1 | — | ✅ |
| 19 | TrackedObjectPEOPkAttribute2 | PK_ATTRIBUTE2 | — | ✅ |
| 20 | TrackedObjectPEOPkAttribute3 | PK_ATTRIBUTE3 | — | ✅ |
| 21 | TrackedObjectPEOPkAttribute4 | PK_ATTRIBUTE4 | — | ✅ |
| 22 | TrackedObjectPEOPkAttribute5 | PK_ATTRIBUTE5 | — | ✅ |
| 23 | TrackedObjectPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 24 | TrackedObjectPEOTrackedObjectId | TRACKED_OBJECT_ID | 🔑 | ✅ |
| 25 | TrackedObjectPEOUkAttribute1 | UK_ATTRIBUTE1 | — | ✅ |
| 26 | TrackedObjectPEOUkAttribute2 | UK_ATTRIBUTE2 | — | ✅ |
| 27 | TrackedObjectPEOUkAttribute3 | UK_ATTRIBUTE3 | — | ✅ |
| 28 | TrackedObjectPEOUkAttribute4 | UK_ATTRIBUTE4 | — | ✅ |
| 29 | TrackedObjectPEOUkAttribute5 | UK_ATTRIBUTE5 | — | ✅ |

### [[cse_tracked_object_refs|CSE_TRACKED_OBJECT_REFS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | GenObjectId | GEN_OBJECT_ID | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PkValue1 | PK_VALUE1 | — | ✅ |
| 10 | PkValue2 | PK_VALUE2 | — | ✅ |
| 11 | PkValue3 | PK_VALUE3 | — | ✅ |
| 12 | PkValue4 | PK_VALUE4 | — | ✅ |
| 13 | PkValue5 | PK_VALUE5 | — | ✅ |
| 14 | TrackedObjectCode | TRACKED_OBJECT_CODE | — | ✅ |
| 15 | TrackedObjectRefId | TRACKED_OBJECT_REF_ID | 🔑 | ✅ |
| 16 | TransactionId | TRANSACTION_ID | — | ✅ |
| 17 | UkValue1 | UK_VALUE1 | — | ✅ |
| 18 | UkValue2 | UK_VALUE2 | — | ✅ |
| 19 | UkValue3 | UK_VALUE3 | — | ✅ |
| 20 | UkValue4 | UK_VALUE4 | — | ✅ |
| 21 | UkValue5 | UK_VALUE5 | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
