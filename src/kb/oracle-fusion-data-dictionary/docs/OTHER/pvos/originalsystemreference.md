---
id: DOC-OTHER-PVO-OriginalSystemReference
doc_type: system-doc
title: "OriginalSystemReference — PVO Cross-Module"
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
  - OriginalSystemReference
  - originalsystemreference
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OriginalSystemReference

## 📌 Visão Geral

View Object para extração BICC de dados de Original System Reference. Acessa as tabelas: HZ_ORIG_SYSTEMS_VL, HZ_ORIG_SYS_REFERENCES.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.OriginalSystemReference`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 6 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hz_orig_systems_vl|HZ_ORIG_SYSTEMS_VL]] — 19 atributos (2 BICC)
- [[hz_orig_sys_references|HZ_ORIG_SYS_REFERENCES]] — 19 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hz_orig_systems_vl|HZ_ORIG_SYSTEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrigSystemCreatedBy | CREATED_BY | — | — |
| 2 | OrigSystemCreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | OrigSystemCreationDate | CREATION_DATE | — | — |
| 4 | OrigSystemDescription | DESCRIPTION | — | — |
| 5 | OrigSystemEnableForAssetFlag | ENABLE_FOR_ASSET_FLAG | — | — |
| 6 | OrigSystemEnableForItemsFlag | ENABLE_FOR_ITEMS_FLAG | — | — |
| 7 | OrigSystemEnableForPlanningFlag | ENABLE_FOR_PLANNING_FLAG | — | — |
| 8 | OrigSystemEnableForTcaFlag | ENABLE_FOR_TCA_FLAG | — | — |
| 9 | OrigSystemEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | OrigSystemLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | OrigSystemLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | OrigSystemLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | OrigSystemObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrigSystemOrigSystem | ORIG_SYSTEM | — | — |
| 15 | OrigSystemOrigSystemId | ORIG_SYSTEM_ID | — | — |
| 16 | OrigSystemOrigSystemName | ORIG_SYSTEM_NAME | — | ✅ |
| 17 | OrigSystemOrigSystemType | ORIG_SYSTEM_TYPE | — | — |
| 18 | OrigSystemStartDateActive | START_DATE_ACTIVE | — | — |
| 19 | OrigSystemStatus | STATUS | — | — |

### [[hz_orig_sys_references|HZ_ORIG_SYS_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrigSystemRefId | ORIG_SYSTEM_REF_ID | 🔑 | ✅ |
| 2 | OriginalSystemReferenceCreatedBy | CREATED_BY | — | — |
| 3 | OriginalSystemReferenceCreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | OriginalSystemReferenceCreationDate | CREATION_DATE | — | — |
| 5 | OriginalSystemReferenceEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | OriginalSystemReferenceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | OriginalSystemReferenceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | OriginalSystemReferenceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | OriginalSystemReferenceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | OriginalSystemReferenceOldOrigSystemReference | OLD_ORIG_SYSTEM_REFERENCE | — | — |
| 11 | OriginalSystemReferenceOrigSystem | ORIG_SYSTEM | — | — |
| 12 | OriginalSystemReferenceOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 13 | OriginalSystemReferenceOwnerTableId | OWNER_TABLE_ID | — | — |
| 14 | OriginalSystemReferenceOwnerTableName | OWNER_TABLE_NAME | — | — |
| 15 | OriginalSystemReferencePartyId | PARTY_ID | — | — |
| 16 | OriginalSystemReferenceReasonCode | REASON_CODE | — | — |
| 17 | OriginalSystemReferenceRequestId | REQUEST_ID | — | ✅ |
| 18 | OriginalSystemReferenceStartDateActive | START_DATE_ACTIVE | — | — |
| 19 | OriginalSystemReferenceStatus | STATUS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
