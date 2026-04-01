---
id: DOC-PO-PVO-ProductLine
doc_type: system-doc
title: "ProductLine — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ProductLine
  - productline
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductLine

## 📌 Visão Geral

Extrai linhas de produto configuradas como valores de lookup, com código e descrição. Suporta classificação e segmentação de propostas e portfólios por linha de produto.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductLine`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 12 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 13 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IMLookupCreatedBy | CREATED_BY | — | ✅ |
| 2 | IMLookupCreationDate | CREATION_DATE | — | ✅ |
| 3 | IMLookupDescription | DESCRIPTION | — | — |
| 4 | IMLookupDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | IMLookupEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | IMLookupEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 7 | IMLookupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IMLookupLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | IMLookupLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | IMLookupLookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 11 | IMLookupLookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 12 | IMLookupMeaning | MEANING | — | ✅ |
| 13 | IMLookupStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
