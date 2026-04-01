---
id: DOC-HCM-PVO-PjrLookupsAdjustTypeCriteriaPVO
doc_type: system-doc
title: "PjrLookupsAdjustTypeCriteriaPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PjrLookupsAdjustTypeCriteriaPVO
  - pjrlookupsadjusttypecriteriapvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjrLookupsAdjustTypeCriteriaPVO

## 📌 Visão Geral

Extrai valores de lookup para critérios de ajuste de alocação de recursos em projetos. Dimensão de referência para configuração de regras de resource management.

**Caminho:** `FscmTopModelAM.PjrAssignmentAM.PjrLookupsAdjustTypeCriteriaPVO`

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
