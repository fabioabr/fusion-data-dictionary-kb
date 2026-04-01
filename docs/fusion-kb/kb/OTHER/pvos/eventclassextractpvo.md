---
id: DOC-OTHER-PVO-EventClassExtractPVO
doc_type: system-doc
title: "EventClassExtractPVO — PVO Cross-Module"
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
  - EventClassExtractPVO
  - eventclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Class Extract. Acessa as tabelas: XLA_EVENT_CLASSES_B, XLA_EVENT_CLASSES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.EventClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 3 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_event_classes_b|XLA_EVENT_CLASSES_B]] — 10 atributos (3 PKs, 10 BICC)
- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[xla_event_classes_b|XLA_EVENT_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassBApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | EventClassBCreatedBy | CREATED_BY | — | ✅ |
| 3 | EventClassBCreationDate | CREATION_DATE | — | ✅ |
| 4 | EventClassBEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | EventClassBEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 6 | EventClassBEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 7 | EventClassBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventClassBLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | EventClassBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | EventClassBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslationApplicationId | APPLICATION_ID | — | ✅ |
| 2 | EventClassTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | EventClassTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | EventClassTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | EventClassTranslationEntityCode | ENTITY_CODE | — | ✅ |
| 6 | EventClassTranslationEventClassCode | EVENT_CLASS_CODE | — | ✅ |
| 7 | EventClassTranslationLanguage | LANGUAGE | — | ✅ |
| 8 | EventClassTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EventClassTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | EventClassTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | EventClassTranslationName | NAME | — | ✅ |
| 12 | EventClassTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
