---
id: DOC-OTHER-PVO-ProcessClassExtractPVO
doc_type: system-doc
title: "ProcessClassExtractPVO — PVO Cross-Module"
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
  - ProcessClassExtractPVO
  - processclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Class Extract. Acessa as tabelas: DOO_PROCESS_CLASSES_B, DOO_PROCESS_CLASSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProcessClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 3 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_classes_b|DOO_PROCESS_CLASSES_B]] — 7 atributos (1 PKs, 7 BICC)
- [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[doo_process_classes_b|DOO_PROCESS_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessClassCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProcessClassCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProcessClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProcessClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | ProcessClassLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ProcessClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProcessClassProcessClassId | PROCESS_CLASS_ID | 🔑 | ✅ |

### [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessClassTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProcessClassTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProcessClassTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ProcessClassTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProcessClassTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProcessClassTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProcessClassTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProcessClassTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProcessClassTranslationOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 10 | ProcessClassTranslationProcessClassId | PROCESS_CLASS_ID | 🔑 | ✅ |
| 11 | ProcessClassTranslationProcessClassName | PROCESS_CLASS_NAME | — | ✅ |
| 12 | ProcessClassTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
