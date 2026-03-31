---
id: DOC-GL-PVO-RateTypePVO
doc_type: system-doc
title: "RateTypePVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RateTypePVO
  - ratetypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Type. Acessa as tabelas: HCM_LOOKUPS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.RateTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 8 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[hcm_lookups|HCM_LOOKUPS]] — 14 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[hcm_lookups|HCM_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HcmLookupPEOCreatedBy | CREATED_BY | — | — |
| 2 | HcmLookupPEOCreationDate | CREATION_DATE | — | — |
| 3 | HcmLookupPEODescription | DESCRIPTION | — | ✅ |
| 4 | HcmLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | HcmLookupPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | HcmLookupPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | HcmLookupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | HcmLookupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | HcmLookupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | HcmLookupPEOMeaning | MEANING | — | ✅ |
| 11 | HcmLookupPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 12 | HcmLookupPEOTag | TAG | — | — |
| 13 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 14 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
