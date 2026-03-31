---
id: DOC-OTHER-PVO-TransactionType
doc_type: system-doc
title: "TransactionType — PVO Cross-Module"
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
  - TransactionType
  - transactiontype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionType

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Type. Acessa as tabelas: CN_LOOKUPS.

**Caminho:** `FscmTopModelAM.CnLookupAM.TransactionType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 4 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[cn_lookups|CN_LOOKUPS]] — 8 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[cn_lookups|CN_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | EnabledFlag | ENABLED_FLAG | — | — |
| 3 | EndDateActive | END_DATE_ACTIVE | — | — |
| 4 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 5 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 6 | Meaning | MEANING | — | ✅ |
| 7 | RowId1 | ROW_ID | — | — |
| 8 | StartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
