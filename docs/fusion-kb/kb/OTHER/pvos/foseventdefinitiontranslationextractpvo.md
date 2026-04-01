---
id: DOC-OTHER-PVO-FosEventDefinitionTranslationExtractPVO
doc_type: system-doc
title: "FosEventDefinitionTranslationExtractPVO — PVO Cross-Module"
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
  - FosEventDefinitionTranslationExtractPVO
  - foseventdefinitiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosEventDefinitionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Event Definition Translation Extract. Acessa as tabelas: FOS_EVENT_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosEventDefinitionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_event_definitions_tl|FOS_EVENT_DEFINITIONS_TL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[fos_event_definitions_tl|FOS_EVENT_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDefinitionsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventDefinitionsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventDefinitionsTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | EventDefinitionsTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | EventDefinitionsTLPEOEventDefinitionId | EVENT_DEFINITION_ID | 🔑 | ✅ |
| 6 | EventDefinitionsTLPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 7 | EventDefinitionsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | EventDefinitionsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventDefinitionsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | EventDefinitionsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | EventDefinitionsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | EventDefinitionsTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | EventDefinitionsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
