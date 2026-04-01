---
id: DOC-OTHER-PVO-DocumentCategoryPVO
doc_type: system-doc
title: "DocumentCategoryPVO — PVO Cross-Module"
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
  - DocumentCategoryPVO
  - documentcategorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DocumentCategoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Document Category. Acessa as tabelas: HCM_LOOKUPS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DocumentOfRecordsAM.DocumentCategoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 4 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 14 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentCategoryPEOCreatedBy | CREATED_BY | — | — |
| 2 | DocumentCategoryPEOCreationDate | CREATION_DATE | — | — |
| 3 | DocumentCategoryPEODescription | DESCRIPTION | — | — |
| 4 | DocumentCategoryPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | DocumentCategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | DocumentCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DocumentCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DocumentCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DocumentCategoryPEOMeaning | MEANING | — | ✅ |
| 10 | DocumentCategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 11 | DocumentCategoryPEOTag | TAG | — | — |
| 12 | DocumentCategoryPEOnabledFlag | ENABLED_FLAG | — | — |
| 13 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 14 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
