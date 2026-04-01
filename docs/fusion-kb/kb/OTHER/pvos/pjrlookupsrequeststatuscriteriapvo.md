---
id: DOC-OTHER-PVO-PjrLookupsRequestStatusCriteriaPVO
doc_type: system-doc
title: "PjrLookupsRequestStatusCriteriaPVO — PVO Cross-Module"
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
  - PjrLookupsRequestStatusCriteriaPVO
  - pjrlookupsrequeststatuscriteriapvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjrLookupsRequestStatusCriteriaPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pjr Lookups Request Status Criteria. Acessa as tabelas: PJR_LOOKUPS.

**Caminho:** `FscmTopModelAM.PjrResourceRequestAM.PjrLookupsRequestStatusCriteriaPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_lookups|PJR_LOOKUPS]] — 9 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pjr_lookups|PJR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 2 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 3 | PjrLookupPEODescription | DESCRIPTION | — | — |
| 4 | PjrLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | PjrLookupPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | PjrLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | PjrLookupPEOMeaning | MEANING | — | — |
| 8 | PjrLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 9 | PjrLookupPEOTag | TAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
