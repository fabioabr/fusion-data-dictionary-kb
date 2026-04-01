---
id: DOC-OTHER-PVO-CostElementTLExtractPVO
doc_type: system-doc
title: "CostElementTLExtractPVO — PVO Cross-Module"
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
  - CostElementTLExtractPVO
  - costelementtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostElementTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Element TLExtract. Acessa as tabelas: CST_COST_ELEMENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CostElementTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementTLPEOCostElementDesc | COST_ELEMENT_DESC | — | ✅ |
| 2 | CostElementTLPEOCostElementId | COST_ELEMENT_ID | 🔑 | ✅ |
| 3 | CostElementTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CostElementTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CostElementTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | CostElementTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CostElementTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CostElementTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CostElementTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | CostElementTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
