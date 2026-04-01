---
id: DOC-OTHER-PVO-CostComponentsTLExtractPVO
doc_type: system-doc
title: "CostComponentsTLExtractPVO — PVO Cross-Module"
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
  - CostComponentsTLExtractPVO
  - costcomponentstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostComponentsTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Components TLExtract. Acessa as tabelas: CST_COST_COMPONENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostComponentsTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 10 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_components_tl|CST_COST_COMPONENTS_TL]] — 11 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_cost_components_tl|CST_COST_COMPONENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostComponentTLPEOCostComponentId | COST_COMPONENT_ID | 🔑 | ✅ |
| 2 | CostComponentTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CostComponentTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CostComponentTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | CostComponentTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CostComponentTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostComponentTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostComponentTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostComponentTLPEOName | NAME | — | ✅ |
| 10 | CostComponentTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | CostComponentTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
