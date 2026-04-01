---
id: DOC-OTHER-PVO-PIMLookupsItemType
doc_type: system-doc
title: "PIMLookupsItemType — PVO Cross-Module"
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
  - PIMLookupsItemType
  - pimlookupsitemtype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PIMLookupsItemType

## 📌 Visão Geral

View Object para extração BICC de dados de PIMLookups Item Type. Acessa as tabelas: FND_LOOKUPS.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.PIMLookupsItemType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 3 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 8 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | DisplaySequence | DISPLAY_SEQUENCE | — | — |
| 3 | EnabledFlag | ENABLED_FLAG | — | — |
| 4 | EndDateActive | END_DATE_ACTIVE | — | — |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | Meaning | MEANING | — | ✅ |
| 8 | StartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
