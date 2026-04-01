---
id: DOC-OTHER-PVO-CstWOCostVariancesExtractPVO
doc_type: system-doc
title: "CstWOCostVariancesExtractPVO — PVO Cross-Module"
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
  - CstWOCostVariancesExtractPVO
  - cstwocostvariancesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOCostVariancesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOCost Variances Extract. Acessa as tabelas: CST_WO_COST_VARIANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOCostVariancesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_cost_variances|CST_WO_COST_VARIANCES]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[cst_wo_cost_variances|CST_WO_COST_VARIANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOCostVariancesPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 2 | CstWOCostVariancesPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CstWOCostVariancesPEOCostDate | COST_DATE | — | ✅ |
| 4 | CstWOCostVariancesPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CstWOCostVariancesPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 6 | CstWOCostVariancesPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstWOCostVariancesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstWOCostVariancesPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 9 | CstWOCostVariancesPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CstWOCostVariancesPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 11 | CstWOCostVariancesPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | CstWOCostVariancesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CstWOCostVariancesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | CstWOCostVariancesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CstWOCostVariancesPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 16 | CstWOCostVariancesPEOQuantity | QUANTITY | — | ✅ |
| 17 | CstWOCostVariancesPEOReversalCostVarianceId | REVERSAL_COST_VARIANCE_ID | — | ✅ |
| 18 | CstWOCostVariancesPEOReversalFlag | REVERSAL_FLAG | — | ✅ |
| 19 | CstWOCostVariancesPEOUomCode | UOM_CODE | — | ✅ |
| 20 | CstWOCostVariancesPEOVarianceAmount | VARIANCE_AMOUNT | — | ✅ |
| 21 | CstWOCostVariancesPEOVarianceGroup | VARIANCE_GROUP | — | ✅ |
| 22 | CstWOCostVariancesPEOVarianceType | VARIANCE_TYPE | — | ✅ |
| 23 | CstWOCostVariancesPEOWoCostVarianceId | WO_COST_VARIANCE_ID | 🔑 | ✅ |
| 24 | CstWOCostVariancesPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
