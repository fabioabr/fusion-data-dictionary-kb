---
id: DOC-OTHER-PVO-EventType
doc_type: system-doc
title: "EventType — PVO Cross-Module"
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
  - EventType
  - eventtype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventType

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type. Acessa as tabelas: PJF_EVENT_TYPES_B, PJF_EVENT_TYPES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.EventType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 14 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_event_types_b|PJF_EVENT_TYPES_B]] — 15 atributos (1 PKs, 11 BICC)
- [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[pjf_event_types_b|PJF_EVENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | EventTypeBasePEOInvoiceFlag | INVOICE_FLAG | — | ✅ |
| 5 | EventTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EventTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | EventTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | EventTypeBasePEOOAllowItemFlag | ALLOW_ITEM_FLAG | — | — |
| 9 | EventTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | EventTypeBasePEOPredefinedFlag | PREDEFINED_FLAG | — | — |
| 11 | EventTypeBasePEOReclassifyFlag | RECLASSIFY_FLAG | — | — |
| 12 | EventTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 13 | EventTypeBasePEORevenueFlag | REVENUE_FLAG | — | ✅ |
| 14 | EventTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 15 | EventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |

### [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | EventTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | EventTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | EventTypeTranslationPEOEventTypeId | EVENT_TYPE_ID | — | — |
| 5 | EventTypeTranslationPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 6 | EventTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | EventTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | EventTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | EventTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | EventTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
