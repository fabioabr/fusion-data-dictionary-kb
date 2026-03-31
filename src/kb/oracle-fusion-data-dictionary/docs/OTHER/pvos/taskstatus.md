---
id: DOC-OTHER-PVO-TaskStatus
doc_type: system-doc
title: "TaskStatus — PVO Cross-Module"
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
  - TaskStatus
  - taskstatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Task Status. Acessa as tabelas: DOO_SERVICE_DEFINITIONS_B, DOO_SERVICE_DEFINITIONS_TL, DOO_STATUSES_B (+6).

**Caminho:** `FscmTopModelAM.DooTopAM.TaskStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 89 | 9 | 1 | 14 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[doo_service_definitions_b|DOO_SERVICE_DEFINITIONS_B]] — 15 atributos
- [[doo_service_definitions_tl|DOO_SERVICE_DEFINITIONS_TL]] — 11 atributos (1 BICC)
- [[doo_statuses_b|DOO_STATUSES_B]] — 1 atributos
- [[doo_statuses_tl|DOO_STATUSES_TL]] — 10 atributos (2 BICC)
- [[doo_task_definitions_b|DOO_TASK_DEFINITIONS_B]] — 9 atributos (1 PKs, 2 BICC)
- [[doo_task_definitions_tl|DOO_TASK_DEFINITIONS_TL]] — 11 atributos (3 BICC)
- [[doo_task_statuses|DOO_TASK_STATUSES]] — 12 atributos (1 BICC)
- [[doo_task_types_b|DOO_TASK_TYPES_B]] — 10 atributos (3 BICC)
- [[doo_task_types_tl|DOO_TASK_TYPES_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[doo_service_definitions_b|DOO_SERVICE_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceCheckHolds | CHECK_HOLDS | — | — |
| 2 | ServiceCreatedBy | CREATED_BY | — | — |
| 3 | ServiceCreationDate | CREATION_DATE | — | — |
| 4 | ServiceFilterRlsId | FILTER_RLS_ID | — | — |
| 5 | ServiceFilterRlsName | FILTER_RLS_NAME | — | — |
| 6 | ServiceLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ServiceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ServiceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ServiceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ServiceOperationCode | OPERATION_CODE | — | — |
| 11 | ServiceServiceId | SERVICE_ID | — | — |
| 12 | ServiceServiceUri | SERVICE_URI | — | — |
| 13 | ServiceSplitAllowed | SPLIT_ALLOWED | — | — |
| 14 | ServiceSystemFlag | SYSTEM_FLAG | — | — |
| 15 | ServiceTaskTypeId | TASK_TYPE_ID | — | — |

### [[doo_service_definitions_tl|DOO_SERVICE_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceTranslationCreatedBy | CREATED_BY | — | — |
| 2 | ServiceTranslationCreationDate | CREATION_DATE | — | — |
| 3 | ServiceTranslationDescription | DESCRIPTION | — | — |
| 4 | ServiceTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | ServiceTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | ServiceTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ServiceTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ServiceTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ServiceTranslationServiceId | SERVICE_ID | — | — |
| 10 | ServiceTranslationServiceName | SERVICE_NAME | — | — |
| 11 | ServiceTranslationSourceLang | SOURCE_LANG | — | — |

### [[doo_statuses_b|DOO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusStatusId | STATUS_ID | — | — |

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatusTranslationCreatedBy | CREATED_BY | — | — |
| 2 | StatusTranslationCreationDate | CREATION_DATE | — | — |
| 3 | StatusTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | StatusTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | StatusTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | StatusTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | StatusTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | StatusTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | StatusTranslationSourceLang | SOURCE_LANG | — | — |
| 10 | StatusTranslationStatusId | STATUS_ID | — | — |

### [[doo_task_definitions_b|DOO_TASK_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskCreatedBy | CREATED_BY | — | — |
| 2 | TaskCreationDate | CREATION_DATE | — | — |
| 3 | TaskLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | TaskLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | TaskLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | TaskObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | TaskOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | — |
| 8 | TaskTaskId | TASK_ID | 🔑 | ✅ |
| 9 | TaskTaskTypeId | TASK_TYPE_ID | — | — |

### [[doo_task_definitions_tl|DOO_TASK_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTranslationCreatedBy | CREATED_BY | — | — |
| 2 | TaskTranslationCreationDate | CREATION_DATE | — | — |
| 3 | TaskTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | TaskTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | TaskTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | TaskTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaskTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaskTranslationName | NAME | — | ✅ |
| 9 | TaskTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TaskTranslationSourceLang | SOURCE_LANG | — | — |
| 11 | TaskTranslationTaskId | TASK_ID | — | — |

### [[doo_task_statuses|DOO_TASK_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStatusCreatedBy | CREATED_BY | — | — |
| 2 | TaskStatusCreationDate | CREATION_DATE | — | — |
| 3 | TaskStatusId | TASK_STATUS_ID | — | — |
| 4 | TaskStatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaskStatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TaskStatusLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TaskStatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TaskStatusSeededFlag | SEEDED_FLAG | — | — |
| 9 | TaskStatusSplitPriority | SPLIT_PRIORITY | — | — |
| 10 | TaskStatusStatusCode | STATUS_CODE | — | — |
| 11 | TaskStatusTaskTypeId | TASK_TYPE_ID | — | — |
| 12 | TaskTypeId | TASK_TYPE_ID | — | — |

### [[doo_task_types_b|DOO_TASK_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeCreatedBy | CREATED_BY | — | — |
| 2 | TaskTypeCreationDate | CREATION_DATE | — | — |
| 3 | TaskTypeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | TaskTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | TaskTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | TaskTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | TaskTypeSeededFlag | SEEDED_FLAG | — | ✅ |
| 8 | TaskTypeTaskSubTypeCode | TASK_SUB_TYPE_CODE | — | — |
| 9 | TaskTypeTaskType | TASK_TYPE | — | ✅ |
| 10 | TaskTypeTaskTypeId | TASK_TYPE_ID | — | ✅ |

### [[doo_task_types_tl|DOO_TASK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeTranslationCreatedBy | CREATED_BY | — | — |
| 2 | TaskTypeTranslationCreationDate | CREATION_DATE | — | — |
| 3 | TaskTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | TaskTypeTranslationLanguage | LANGUAGE | — | ✅ |
| 5 | TaskTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | TaskTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaskTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaskTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | TaskTypeTranslationSourceLang | SOURCE_LANG | — | — |
| 10 | TaskTypeTranslationTaskTypeId | TASK_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
