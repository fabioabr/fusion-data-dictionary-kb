---
id: DOC-OTHER-PVO-EventTypeTranslationExtractPVO
doc_type: system-doc
title: "EventTypeTranslationExtractPVO — PVO Cross-Module"
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
  - EventTypeTranslationExtractPVO
  - eventtypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type Translation Extract. Acessa as tabelas: PJF_EVENT_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.EventTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | EventTypeTranslationPEOEventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |
| 5 | EventTypeTranslationPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 6 | EventTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | EventTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | EventTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | EventTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | EventTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
