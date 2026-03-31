---
id: DOC-OTHER-PVO-TaskDefinitionExtractPVO
doc_type: system-doc
title: "TaskDefinitionExtractPVO — PVO Cross-Module"
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
  - TaskDefinitionExtractPVO
  - taskdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Definition Extract. Acessa as tabelas: DOO_TASK_DEFINITIONS_B, DOO_TASK_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_definitions_b|DOO_TASK_DEFINITIONS_B]] — 10 atributos (1 PKs, 10 BICC)
- [[doo_task_definitions_tl|DOO_TASK_DEFINITIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_task_definitions_b|DOO_TASK_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskDefinitionAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | TaskDefinitionCreatedBy | CREATED_BY | — | ✅ |
| 3 | TaskDefinitionCreationDate | CREATION_DATE | — | ✅ |
| 4 | TaskDefinitionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaskDefinitionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaskDefinitionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TaskDefinitionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | TaskDefinitionOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 9 | TaskDefinitionTaskId | TASK_ID | 🔑 | ✅ |
| 10 | TaskDefinitionTaskTypeId | TASK_TYPE_ID | — | ✅ |

### [[doo_task_definitions_tl|DOO_TASK_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskDefinitionTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskDefinitionTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskDefinitionTranslationDisplayName | DISPLAY_NAME | — | ✅ |
| 4 | TaskDefinitionTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TaskDefinitionTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaskDefinitionTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaskDefinitionTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaskDefinitionTranslationName | NAME | — | ✅ |
| 9 | TaskDefinitionTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TaskDefinitionTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 11 | TaskDefinitionTranslationTaskId | TASK_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
