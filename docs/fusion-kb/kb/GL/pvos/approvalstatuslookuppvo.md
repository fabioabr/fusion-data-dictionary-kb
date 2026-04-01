---
id: DOC-GL-PVO-ApprovalStatusLookupPVO
doc_type: system-doc
title: "ApprovalStatusLookupPVO — PVO General Ledger"
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
  - ApprovalStatusLookupPVO
  - approvalstatuslookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApprovalStatusLookupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Approval Status Lookup. Acessa as tabelas: GL_LOOKUPS.

**Caminho:** `FscmTopModelAM.FinGlShrdComnLookupAM.ApprovalStatusLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 2 | 4 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[gl_lookups|GL_LOOKUPS]] — 7 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[gl_lookups|GL_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | EnabledFlag | ENABLED_FLAG | — | — |
| 3 | EndDateActive | END_DATE_ACTIVE | — | — |
| 4 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 5 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 6 | Meaning | MEANING | — | ✅ |
| 7 | StartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
