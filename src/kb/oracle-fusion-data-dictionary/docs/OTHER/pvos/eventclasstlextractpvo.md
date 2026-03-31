---
id: DOC-OTHER-PVO-EventClassTLExtractPVO
doc_type: system-doc
title: "EventClassTLExtractPVO — PVO Cross-Module"
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
  - EventClassTLExtractPVO
  - eventclasstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventClassTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Class TLExtract. Acessa as tabelas: XLA_EVENT_CLASSES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.EventClassTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 4 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 13 atributos (4 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslationApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | EventClassTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | EventClassTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | EventClassTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | EventClassTranslationEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 6 | EventClassTranslationEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 7 | EventClassTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | EventClassTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventClassTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | EventClassTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | EventClassTranslationName | NAME | — | ✅ |
| 12 | EventClassTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | EventClassTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
