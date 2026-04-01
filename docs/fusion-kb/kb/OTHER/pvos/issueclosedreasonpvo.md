---
id: DOC-OTHER-PVO-IssueClosedReasonPVO
doc_type: system-doc
title: "IssueClosedReasonPVO — PVO Cross-Module"
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
  - IssueClosedReasonPVO
  - issueclosedreasonpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IssueClosedReasonPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Issue Closed Reason. Acessa as tabelas: PJE_LOOKUPS.

**Caminho:** `FscmTopModelAM.PjeCommonAM.IssueClosedReasonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[pje_lookups|PJE_LOOKUPS]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[pje_lookups|PJE_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 2 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 3 | PjeLookupPEODescription | DESCRIPTION | — | ✅ |
| 4 | PjeLookupPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 5 | PjeLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | PjeLookupPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 7 | PjeLookupPEOMeaning | MEANING | — | ✅ |
| 8 | PjeLookupPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 9 | PjeLookupPEOTag | TAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
