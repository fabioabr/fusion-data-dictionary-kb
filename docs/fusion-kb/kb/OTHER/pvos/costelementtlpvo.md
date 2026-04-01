---
id: DOC-OTHER-PVO-CostElementTLPVO
doc_type: system-doc
title: "CostElementTLPVO — PVO Cross-Module"
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
  - CostElementTLPVO
  - costelementtlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostElementTLPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cost Element TL. Acessa as tabelas: CST_COST_ELEMENTS_TL.

**Caminho:** `FscmTopModelAM.CostElementAM.CostElementTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 8 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]] — 10 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_cost_elements_tl|CST_COST_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostElementDesc | COST_ELEMENT_DESC | — | ✅ |
| 2 | CostElementId | COST_ELEMENT_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
