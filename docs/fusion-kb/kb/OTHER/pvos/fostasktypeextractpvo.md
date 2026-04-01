---
id: DOC-OTHER-PVO-FosTaskTypeExtractPVO
doc_type: system-doc
title: "FosTaskTypeExtractPVO — PVO Cross-Module"
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
  - FosTaskTypeExtractPVO
  - fostasktypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTaskTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Task Type Extract. Acessa as tabelas: FOS_TASK_TYPE_B, FOS_TASK_TYPE_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTaskTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 2 | 1 | 58 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[fos_task_type_b|FOS_TASK_TYPE_B]] — 46 atributos (1 PKs, 46 BICC)
- [[fos_task_type_tl|FOS_TASK_TYPE_TL]] — 14 atributos (12 BICC)

---

## ⚙️ Atributos

### [[fos_task_type_b|FOS_TASK_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | TaskTypeBPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | TaskTypeBPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | TaskTypeBPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | TaskTypeBPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | TaskTypeBPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | TaskTypeBPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | TaskTypeBPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | TaskTypeBPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 10 | TaskTypeBPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 11 | TaskTypeBPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 12 | TaskTypeBPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 13 | TaskTypeBPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 14 | TaskTypeBPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 15 | TaskTypeBPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 16 | TaskTypeBPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 17 | TaskTypeBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 18 | TaskTypeBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 19 | TaskTypeBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 20 | TaskTypeBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 21 | TaskTypeBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 22 | TaskTypeBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 23 | TaskTypeBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 24 | TaskTypeBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 25 | TaskTypeBPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 26 | TaskTypeBPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 27 | TaskTypeBPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 28 | TaskTypeBPEOCreatedBy | CREATED_BY | — | ✅ |
| 29 | TaskTypeBPEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | TaskTypeBPEODefaultConnectorUrl | DEFAULT_CONNECTOR_URL | — | ✅ |
| 31 | TaskTypeBPEODefaultEndServiceUrl | DEFAULT_END_SERVICE_URL | — | ✅ |
| 32 | TaskTypeBPEODefaultSystemId | DEFAULT_SYSTEM_ID | — | ✅ |
| 33 | TaskTypeBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 34 | TaskTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | TaskTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | TaskTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | TaskTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 38 | TaskTypeBPEOResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 39 | TaskTypeBPEORuleCode | RULE_CODE | — | ✅ |
| 40 | TaskTypeBPEORuleDictionaryId | RULE_DICTIONARY_ID | — | ✅ |
| 41 | TaskTypeBPEORuleTypeBasis | RULE_TYPE_BASIS | — | ✅ |
| 42 | TaskTypeBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 43 | TaskTypeBPEOTaskCategory | TASK_CATEGORY | — | ✅ |
| 44 | TaskTypeBPEOTaskGroupCode | TASK_GROUP_CODE | — | ✅ |
| 45 | TaskTypeBPEOTaskType | TASK_TYPE | — | ✅ |
| 46 | TaskTypeBPEOTaskTypeId | TASK_TYPE_ID | 🔑 | ✅ |

### [[fos_task_type_tl|FOS_TASK_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TaskTypeTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | TaskTypeTLPEOLanguage | LANGUAGE | — | — |
| 6 | TaskTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TaskTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TaskTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TaskTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TaskTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | TaskTypeTLPEOSourceLang | SOURCE_LANG | — | — |
| 12 | TaskTypeTLPEOTaskGroupName | TASK_GROUP_NAME | — | ✅ |
| 13 | TaskTypeTLPEOTaskName | TASK_NAME | — | ✅ |
| 14 | TaskTypeTLPEOTaskTypeId | TASK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
