---
id: DOC-OTHER-PVO-ServiceDefinitionExtractPVO
doc_type: system-doc
title: "ServiceDefinitionExtractPVO — PVO Cross-Module"
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
  - ServiceDefinitionExtractPVO
  - servicedefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ServiceDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Service Definition Extract. Acessa as tabelas: DOO_SERVICE_DEFINITIONS_B, DOO_SERVICE_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ServiceDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 3 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_service_definitions_b|DOO_SERVICE_DEFINITIONS_B]] — 12 atributos (1 PKs, 12 BICC)
- [[doo_service_definitions_tl|DOO_SERVICE_DEFINITIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_service_definitions_b|DOO_SERVICE_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceDefinitionCheckHolds | CHECK_HOLDS | — | ✅ |
| 2 | ServiceDefinitionCreatedBy | CREATED_BY | — | ✅ |
| 3 | ServiceDefinitionCreationDate | CREATION_DATE | — | ✅ |
| 4 | ServiceDefinitionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ServiceDefinitionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ServiceDefinitionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ServiceDefinitionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ServiceDefinitionOperationCode | OPERATION_CODE | — | ✅ |
| 9 | ServiceDefinitionServiceId | SERVICE_ID | 🔑 | ✅ |
| 10 | ServiceDefinitionSplitAllowed | SPLIT_ALLOWED | — | ✅ |
| 11 | ServiceDefinitionSystemFlag | SYSTEM_FLAG | — | ✅ |
| 12 | ServiceDefinitionTaskTypeId | TASK_TYPE_ID | — | ✅ |

### [[doo_service_definitions_tl|DOO_SERVICE_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceDefinitionTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | ServiceDefinitionTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | ServiceDefinitionTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ServiceDefinitionTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ServiceDefinitionTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ServiceDefinitionTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ServiceDefinitionTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ServiceDefinitionTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ServiceDefinitionTranslationServiceId | SERVICE_ID | 🔑 | ✅ |
| 10 | ServiceDefinitionTranslationServiceName | SERVICE_NAME | — | ✅ |
| 11 | ServiceDefinitionTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
