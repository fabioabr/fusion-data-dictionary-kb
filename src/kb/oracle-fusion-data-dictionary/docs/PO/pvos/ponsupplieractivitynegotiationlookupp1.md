---
id: DOC-PO-PVO-PonSupplierActivityNegotiationLookupP1
doc_type: system-doc
title: "PonSupplierActivityNegotiationLookupP1 — PVO Purchasing"
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
  - PonSupplierActivityNegotiationLookupP1
  - ponsupplieractivitynegotiationlookupp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PonSupplierActivityNegotiationLookupP1

## 📌 Visão Geral

Extrai valores de lookup para atividades de fornecedores em negociações (visualizou, baixou, submeteu). Padroniza a análise de engajamento e comportamento de fornecedores em eventos de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.PonSupplierActivityNegotiationLookupP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 8 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 3 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 6 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 7 | Meaning | MEANING | — | ✅ |
| 8 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
