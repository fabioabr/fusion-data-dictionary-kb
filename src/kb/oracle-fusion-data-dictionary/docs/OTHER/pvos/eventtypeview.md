---
id: DOC-OTHER-PVO-EventTypeView
doc_type: system-doc
title: "EventTypeView — PVO Cross-Module"
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
  - EventTypeView
  - eventtypeview
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventTypeView

## 📌 Visão Geral

View Object para extração BICC de dados de Event Type View. Acessa as tabelas: PJF_EVENT_TYPES_VL.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.EventTypeView`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 12 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]] — 15 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypeId | EVENT_TYPE_ID | 🔑 | ✅ |
| 2 | EventTypePEOAllowItemFlag | ALLOW_ITEM_FLAG | — | — |
| 3 | EventTypePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EventTypePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EventTypePEODescription | DESCRIPTION | — | ✅ |
| 6 | EventTypePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | EventTypePEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |
| 8 | EventTypePEOInvoiceFlag | INVOICE_FLAG | — | ✅ |
| 9 | EventTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | EventTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EventTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | EventTypePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |
| 14 | EventTypePEORevenueFlag | REVENUE_FLAG | — | ✅ |
| 15 | EventTypePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
