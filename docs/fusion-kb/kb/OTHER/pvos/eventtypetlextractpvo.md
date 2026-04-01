---
id: DOC-OTHER-PVO-EventTypeTLExtractPVO
doc_type: system-doc
title: "EventTypeTLExtractPVO — PVO Cross-Module"
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
  - EventTypeTLExtractPVO
  - eventtypetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventTypeTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type TLExtract. Acessa as tabelas: XLA_EVENT_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.EventTypeTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 5 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 14 atributos (5 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | EventTypeTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | EventTypeTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | EventTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | EventTypeTranslationEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 6 | EventTypeTranslationEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 7 | EventTypeTranslationEventTypeCode | EVENT_TYPE_CODE | 🔑 | ✅ |
| 8 | EventTypeTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 9 | EventTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | EventTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EventTypeTranslationName | NAME | — | ✅ |
| 13 | EventTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | EventTypeTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
