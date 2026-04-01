---
id: DOC-OTHER-PVO-TaskTypeExtractPVO
doc_type: system-doc
title: "TaskTypeExtractPVO — PVO Cross-Module"
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
  - TaskTypeExtractPVO
  - tasktypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Type Extract. Acessa as tabelas: DOO_TASK_TYPES_B, DOO_TASK_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 3 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_types_b|DOO_TASK_TYPES_B]] — 12 atributos (1 PKs, 12 BICC)
- [[doo_task_types_tl|DOO_TASK_TYPES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[doo_task_types_b|DOO_TASK_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | TaskTypeCreatedBy | CREATED_BY | — | ✅ |
| 3 | TaskTypeCreationDate | CREATION_DATE | — | ✅ |
| 4 | TaskTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaskTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaskTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TaskTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | TaskTypeOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 9 | TaskTypeSeededFlag | SEEDED_FLAG | — | ✅ |
| 10 | TaskTypeTaskSubTypeCode | TASK_SUB_TYPE_CODE | — | ✅ |
| 11 | TaskTypeTaskType | TASK_TYPE | — | ✅ |
| 12 | TaskTypeTaskTypeId | TASK_TYPE_ID | 🔑 | ✅ |

### [[doo_task_types_tl|DOO_TASK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypeTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskTypeTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | TaskTypeTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TaskTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaskTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaskTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaskTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | TaskTypeTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 10 | TaskTypeTranslationTaskTypeId | TASK_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
