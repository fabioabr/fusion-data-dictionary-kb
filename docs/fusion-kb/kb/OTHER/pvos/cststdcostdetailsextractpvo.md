---
id: DOC-OTHER-PVO-CstStdCostDetailsExtractPVO
doc_type: system-doc
title: "CstStdCostDetailsExtractPVO — PVO Cross-Module"
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
  - CstStdCostDetailsExtractPVO
  - cststdcostdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstStdCostDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Std Cost Details Extract. Acessa as tabelas: CST_STD_COSTS, CST_STD_COST_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstStdCostDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 2 | 1 | 39 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_std_costs|CST_STD_COSTS]] — 28 atributos (28 BICC)
- [[cst_std_cost_details|CST_STD_COST_DETAILS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cst_std_costs|CST_STD_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstStdCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstStdCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 3 | CstStdCostsPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 4 | CstStdCostsPEOCostType | COST_TYPE | — | ✅ |
| 5 | CstStdCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstStdCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstStdCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CstStdCostsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 9 | CstStdCostsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | CstStdCostsPEOFromPeriodName | FROM_PERIOD_NAME | — | ✅ |
| 11 | CstStdCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | CstStdCostsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 13 | CstStdCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CstStdCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | CstStdCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | CstStdCostsPEOLastUsedDate | LAST_USED_DATE | — | ✅ |
| 17 | CstStdCostsPEOPreviousEffectiveEndDate | PREVIOUS_EFFECTIVE_END_DATE | — | ✅ |
| 18 | CstStdCostsPEOPreviousEffectiveStartDate | PREVIOUS_EFFECTIVE_START_DATE | — | ✅ |
| 19 | CstStdCostsPEOPreviousStdCostId | PREVIOUS_STD_COST_ID | — | ✅ |
| 20 | CstStdCostsPEOPreviousTotalCost | PREVIOUS_TOTAL_COST | — | ✅ |
| 21 | CstStdCostsPEOScenarioId | SCENARIO_ID | — | ✅ |
| 22 | CstStdCostsPEOStatusCode | STATUS_CODE | — | ✅ |
| 23 | CstStdCostsPEOStdCostId | STD_COST_ID | — | ✅ |
| 24 | CstStdCostsPEOToPeriodName | TO_PERIOD_NAME | — | ✅ |
| 25 | CstStdCostsPEOTotalCost | TOTAL_COST | — | ✅ |
| 26 | CstStdCostsPEOUomCode | UOM_CODE | — | ✅ |
| 27 | CstStdCostsPEOValStructureId | VAL_STRUCTURE_ID | — | ✅ |
| 28 | CstStdCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |

### [[cst_std_cost_details|CST_STD_COST_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstStdCostDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 2 | CstStdCostDetailsPEOCostLevelCode | COST_LEVEL_CODE | — | ✅ |
| 3 | CstStdCostDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstStdCostDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstStdCostDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 6 | CstStdCostDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CstStdCostDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CstStdCostDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CstStdCostDetailsPEOStdCostDetailId | STD_COST_DETAIL_ID | 🔑 | ✅ |
| 10 | CstStdCostDetailsPEOStdCostId | STD_COST_ID | — | ✅ |
| 11 | CstStdCostDetailsPEOUnitCost | UNIT_COST | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
