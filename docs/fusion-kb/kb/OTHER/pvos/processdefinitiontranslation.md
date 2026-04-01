---
id: DOC-OTHER-PVO-ProcessDefinitionTranslation
doc_type: system-doc
title: "ProcessDefinitionTranslation — PVO Cross-Module"
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
  - ProcessDefinitionTranslation
  - processdefinitiontranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessDefinitionTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Process Definition Translation. Acessa as tabelas: DOO_PROCESS_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.ProcessDefinitionTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_definitions_tl|DOO_PROCESS_DEFINITIONS_TL]] — 12 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[doo_process_definitions_tl|DOO_PROCESS_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DooProcessId | DOO_PROCESS_ID | 🔑 | ✅ |
| 5 | DooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProcessDisplayName | PROCESS_DISPLAY_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
