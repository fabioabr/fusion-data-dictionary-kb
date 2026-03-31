---
id: DOC-OTHER-PVO-MeterDefinitionTranslationExtractPVO
doc_type: system-doc
title: "MeterDefinitionTranslationExtractPVO — PVO Cross-Module"
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
  - MeterDefinitionTranslationExtractPVO
  - meterdefinitiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeterDefinitionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meter Definition Translation Extract. Acessa as tabelas: CSE_METER_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.MeterDefinitionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_meter_definitions_tl|CSE_METER_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MeterDefinitionId | METER_DEFINITION_ID | 🔑 | ✅ |
| 8 | MeterDescription | METER_DESCRIPTION | — | ✅ |
| 9 | MeterName | METER_NAME | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
