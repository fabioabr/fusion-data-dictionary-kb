---
id: DOC-OTHER-PVO-CstTxnComponentCostsExtractPVO
doc_type: system-doc
title: "CstTxnComponentCostsExtractPVO — PVO Cross-Module"
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
  - CstTxnComponentCostsExtractPVO
  - csttxncomponentcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTxnComponentCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Txn Component Costs Extract. Acessa as tabelas: CST_TXN_COMPONENT_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTxnComponentCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_txn_component_costs|CST_TXN_COMPONENT_COSTS]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cst_txn_component_costs|CST_TXN_COMPONENT_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTxnComponentCostsPEOComponentMappingType | COMPONENT_MAPPING_TYPE | — | ✅ |
| 2 | CstTxnComponentCostsPEOCostComponentCode | COST_COMPONENT_CODE | — | ✅ |
| 3 | CstTxnComponentCostsPEOCostComponentType | COST_COMPONENT_TYPE | — | ✅ |
| 4 | CstTxnComponentCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstTxnComponentCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstTxnComponentCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | CstTxnComponentCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CstTxnComponentCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CstTxnComponentCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CstTxnComponentCostsPEOSourceCostComponentId | SOURCE_COST_COMPONENT_ID | 🔑 | ✅ |
| 11 | CstTxnComponentCostsPEOSourceCostElementId | SOURCE_COST_ELEMENT_ID | 🔑 | ✅ |
| 12 | CstTxnComponentCostsPEOTransactionCostId | TRANSACTION_COST_ID | 🔑 | ✅ |
| 13 | CstTxnComponentCostsPEOUnitCost | UNIT_COST | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
