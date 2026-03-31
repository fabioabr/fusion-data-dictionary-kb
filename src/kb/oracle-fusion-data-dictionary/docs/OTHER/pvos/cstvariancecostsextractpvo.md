---
id: DOC-OTHER-PVO-CstVarianceCostsExtractPVO
doc_type: system-doc
title: "CstVarianceCostsExtractPVO — PVO Cross-Module"
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
  - CstVarianceCostsExtractPVO
  - cstvariancecostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstVarianceCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Variance Costs Extract. Acessa as tabelas: CST_VARIANCE_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstVarianceCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 1 | 32 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_variance_costs|CST_VARIANCE_COSTS]] — 32 atributos (1 PKs, 32 BICC)

---

## ⚙️ Atributos

### [[cst_variance_costs|CST_VARIANCE_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstVarianceCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstVarianceCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstVarianceCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 4 | CstVarianceCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CstVarianceCostsPEOCostDate | COST_DATE | — | ✅ |
| 6 | CstVarianceCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 7 | CstVarianceCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 8 | CstVarianceCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 9 | CstVarianceCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 10 | CstVarianceCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 11 | CstVarianceCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CstVarianceCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CstVarianceCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | CstVarianceCostsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 15 | CstVarianceCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 16 | CstVarianceCostsPEODistributionType | DISTRIBUTION_TYPE | — | ✅ |
| 17 | CstVarianceCostsPEOEffDate | EFF_DATE | — | ✅ |
| 18 | CstVarianceCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 19 | CstVarianceCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 20 | CstVarianceCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CstVarianceCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CstVarianceCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CstVarianceCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 24 | CstVarianceCostsPEOQuantity | QUANTITY | — | ✅ |
| 25 | CstVarianceCostsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 26 | CstVarianceCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 27 | CstVarianceCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 28 | CstVarianceCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 29 | CstVarianceCostsPEOUomCode | UOM_CODE | — | ✅ |
| 30 | CstVarianceCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 31 | CstVarianceCostsPEOVarianceCostId | VARIANCE_COST_ID | 🔑 | ✅ |
| 32 | CstVarianceCostsPEOWoCostPostedFlag | WO_COST_POSTED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
