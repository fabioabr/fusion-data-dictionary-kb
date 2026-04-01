---
id: DOC-OTHER-PVO-EventTypeExtractPVO
doc_type: system-doc
title: "EventTypeExtractPVO — PVO Cross-Module"
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
  - EventTypeExtractPVO
  - eventtypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type Extract. Acessa as tabelas: PJF_EVENT_TYPES_B, PJF_EVENT_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.EventTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 2 | 3 | 28 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_event_types_b|PJF_EVENT_TYPES_B]] — 33 atributos (1 PKs, 17 BICC)
- [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_event_types_b|PJF_EVENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeBasePEOAllowAdjustmentFlag | ALLOW_ADJUSTMENT_FLAG | — | ✅ |
| 2 | EventTypeBasePEOAllowItemFlag | ALLOW_ITEM_FLAG | — | ✅ |
| 3 | EventTypeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | EventTypeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | EventTypeBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | EventTypeBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | EventTypeBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | EventTypeBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | EventTypeBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | EventTypeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 11 | EventTypeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 12 | EventTypeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 13 | EventTypeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 14 | EventTypeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 15 | EventTypeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 16 | EventTypeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 17 | EventTypeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 18 | EventTypeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | EventTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 20 | EventTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 21 | EventTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 22 | EventTypeBasePEOEventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |
| 23 | EventTypeBasePEOInvoiceFlag | INVOICE_FLAG | — | ✅ |
| 24 | EventTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | EventTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | EventTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | EventTypeBasePEOMigrationFlag | MIGRATION_FLAG | — | ✅ |
| 28 | EventTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | EventTypeBasePEOPredefinedFlag | PREDEFINED_FLAG | — | ✅ |
| 30 | EventTypeBasePEOReclassifyFlag | RECLASSIFY_FLAG | — | ✅ |
| 31 | EventTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 32 | EventTypeBasePEORevenueFlag | REVENUE_FLAG | — | ✅ |
| 33 | EventTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_event_types_tl|PJF_EVENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventTypeTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventTypeTransLangPEODescription | DESCRIPTION | — | ✅ |
| 4 | EventTypeTransLangPEOEventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |
| 5 | EventTypeTransLangPEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 6 | EventTypeTransLangPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | EventTypeTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventTypeTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | EventTypeTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | EventTypeTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
