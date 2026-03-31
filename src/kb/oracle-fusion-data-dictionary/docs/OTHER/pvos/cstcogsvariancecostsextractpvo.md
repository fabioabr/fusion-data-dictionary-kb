---
id: DOC-OTHER-PVO-CstCogsVarianceCostsExtractPVO
doc_type: system-doc
title: "CstCogsVarianceCostsExtractPVO — PVO Cross-Module"
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
  - CstCogsVarianceCostsExtractPVO
  - cstcogsvariancecostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstCogsVarianceCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Cogs Variance Costs Extract. Acessa as tabelas: CST_COGS_VARIANCE_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstCogsVarianceCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cogs_variance_costs|CST_COGS_VARIANCE_COSTS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[cst_cogs_variance_costs|CST_COGS_VARIANCE_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstCogsVarianceCostsPEOCogsTransactionId | COGS_TRANSACTION_ID | — | ✅ |
| 2 | CstCogsVarianceCostsPEOCogsVarianceCostId | COGS_VARIANCE_COST_ID | 🔑 | ✅ |
| 3 | CstCogsVarianceCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstCogsVarianceCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstCogsVarianceCostsPEOCstTransactionId | CST_TRANSACTION_ID | — | ✅ |
| 6 | CstCogsVarianceCostsPEOCstVarianceCostId | CST_VARIANCE_COST_ID | — | ✅ |
| 7 | CstCogsVarianceCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 8 | CstCogsVarianceCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CstCogsVarianceCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CstCogsVarianceCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CstCogsVarianceCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 12 | CstCogsVarianceCostsPEOQuantity | QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
