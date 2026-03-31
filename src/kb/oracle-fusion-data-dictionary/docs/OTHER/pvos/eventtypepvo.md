---
id: DOC-OTHER-PVO-EventTypePVO
doc_type: system-doc
title: "EventTypePVO — PVO Cross-Module"
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
  - EventTypePVO
  - eventtypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type. Acessa as tabelas: XLA_EVENT_CLASSES_B, XLA_EVENT_CLASSES_TL, XLA_EVENT_TYPES_B (+2).

**Caminho:** `FscmTopModelAM.FinXlaAmsEventModelsAM.EventTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 5 | 4 | 12 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[xla_event_classes_b|XLA_EVENT_CLASSES_B]] — 10 atributos (1 BICC)
- [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]] — 7 atributos (1 BICC)
- [[xla_event_types_b|XLA_EVENT_TYPES_B]] — 14 atributos (4 PKs, 5 BICC)
- [[xla_event_types_tl|XLA_EVENT_TYPES_TL]] — 14 atributos (3 BICC)
- [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]] — 9 atributos (2 BICC)

---

## ⚙️ Atributos

### [[xla_event_classes_b|XLA_EVENT_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassApplicationId | APPLICATION_ID | — | — |
| 2 | EventClassCreatedBy | CREATED_BY | — | — |
| 3 | EventClassCreationDate | CREATION_DATE | — | — |
| 4 | EventClassEnabledFlag | ENABLED_FLAG | — | — |
| 5 | EventClassEntityCode | ENTITY_CODE | — | — |
| 6 | EventClassEventClassCode | EVENT_CLASS_CODE | — | — |
| 7 | EventClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | EventClassLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | EventClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[xla_event_classes_tl|XLA_EVENT_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventClassTranslatedApplicationId | APPLICATION_ID | — | — |
| 2 | EventClassTranslatedDescription | DESCRIPTION | — | — |
| 3 | EventClassTranslatedEntityCode | ENTITY_CODE | — | — |
| 4 | EventClassTranslatedEventClassCode | EVENT_CLASS_CODE | — | — |
| 5 | EventClassTranslatedLanguage | LANGUAGE | — | — |
| 6 | EventClassTranslatedName | NAME | — | ✅ |
| 7 | EventClassTranslatedSourceLang | SOURCE_LANG | — | — |

### [[xla_event_types_b|XLA_EVENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | EntityCode | ENTITY_CODE | 🔑 | ✅ |
| 3 | EventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 4 | EventTypeAccountingFlag | ACCOUNTING_FLAG | — | — |
| 5 | EventTypeCode | EVENT_TYPE_CODE | 🔑 | ✅ |
| 6 | EventTypeCreatedBy | CREATED_BY | — | — |
| 7 | EventTypeCreationDate | CREATION_DATE | — | — |
| 8 | EventTypeEnabledFlag | ENABLED_FLAG | — | — |
| 9 | EventTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EventTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | EventTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | EventTypeTaxFlag | TAX_FLAG | — | — |
| 14 | EventTypeTransactionReversalFlag | TRANSACTION_REVERSAL_FLAG | — | — |

### [[xla_event_types_tl|XLA_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslatedApplicationId | APPLICATION_ID | — | — |
| 2 | EventTypeTranslatedCreatedBy | CREATED_BY | — | — |
| 3 | EventTypeTranslatedCreationDate | CREATION_DATE | — | — |
| 4 | EventTypeTranslatedDescription | DESCRIPTION | — | ✅ |
| 5 | EventTypeTranslatedEntityCode | ENTITY_CODE | — | — |
| 6 | EventTypeTranslatedEventClassCode | EVENT_CLASS_CODE | — | — |
| 7 | EventTypeTranslatedEventTypeCode | EVENT_TYPE_CODE | — | — |
| 8 | EventTypeTranslatedLanguage | LANGUAGE | — | — |
| 9 | EventTypeTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventTypeTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EventTypeTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | EventTypeTranslatedName | NAME | — | ✅ |
| 13 | EventTypeTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | EventTypeTranslatedSourceLang | SOURCE_LANG | — | — |

### [[xla_subledgers_vl|XLA_SUBLEDGERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XlaApplnTranslationApplicationId | APPLICATION_ID | — | — |
| 2 | XlaApplnTranslationApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | XlaApplnTranslationCreatedBy | CREATED_BY | — | — |
| 4 | XlaApplnTranslationCreationDate | CREATION_DATE | — | — |
| 5 | XlaApplnTranslationDescription | DESCRIPTION | — | — |
| 6 | XlaApplnTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | XlaApplnTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | XlaApplnTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | XlaApplnTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
