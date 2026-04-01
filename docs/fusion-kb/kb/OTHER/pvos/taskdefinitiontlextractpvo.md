---
id: DOC-OTHER-PVO-TaskDefinitionTLExtractPVO
doc_type: system-doc
title: "TaskDefinitionTLExtractPVO — PVO Cross-Module"
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
  - TaskDefinitionTLExtractPVO
  - taskdefinitiontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskDefinitionTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Definition TLExtract. Acessa as tabelas: DOO_TASK_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskDefinitionTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_definitions_tl|DOO_TASK_DEFINITIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

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
