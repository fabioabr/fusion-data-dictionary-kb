---
id: DOC-OTHER-PVO-CstCogsLayerCostsExtractPVO
doc_type: system-doc
title: "CstCogsLayerCostsExtractPVO — PVO Cross-Module"
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
  - CstCogsLayerCostsExtractPVO
  - cstcogslayercostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCogsLayerCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Cogs Layer Costs Extract. Acessa as tabelas: CST_COGS_LAYER_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstCogsLayerCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cogs_layer_costs|CST_COGS_LAYER_COSTS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[cst_cogs_layer_costs|CST_COGS_LAYER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCogsLayersCostsPEOCogsLayerCostId | COGS_LAYER_COST_ID | 🔑 | ✅ |
| 2 | CstCogsLayersCostsPEOCogsTransactionId | COGS_TRANSACTION_ID | — | ✅ |
| 3 | CstCogsLayersCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstCogsLayersCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstCogsLayersCostsPEOCstLayerCostId | CST_LAYER_COST_ID | — | ✅ |
| 6 | CstCogsLayersCostsPEOCstTransactionId | CST_TRANSACTION_ID | — | ✅ |
| 7 | CstCogsLayersCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 8 | CstCogsLayersCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CstCogsLayersCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CstCogsLayersCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CstCogsLayersCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 12 | CstCogsLayersCostsPEOQuantity | QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
