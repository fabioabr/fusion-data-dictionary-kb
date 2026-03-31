---
id: DOC-OTHER-PVO-CstWOOSPCostsExtractPVO
doc_type: system-doc
title: "CstWOOSPCostsExtractPVO — PVO Cross-Module"
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
  - CstWOOSPCostsExtractPVO
  - cstwoospcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOOSPCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOOSPCosts Extract. Acessa as tabelas: CST_WO_OSP_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOOSPCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_osp_costs|CST_WO_OSP_COSTS]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[cst_wo_osp_costs|CST_WO_OSP_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOOSPCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstWOOSPCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstWOOSPCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 4 | CstWOOSPCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CstWOOSPCostsPEOCostDate | COST_DATE | — | ✅ |
| 6 | CstWOOSPCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 7 | CstWOOSPCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 8 | CstWOOSPCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 9 | CstWOOSPCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 10 | CstWOOSPCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 11 | CstWOOSPCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CstWOOSPCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CstWOOSPCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | CstWOOSPCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 15 | CstWOOSPCostsPEOEffDate | EFF_DATE | — | ✅ |
| 16 | CstWOOSPCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 17 | CstWOOSPCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 18 | CstWOOSPCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CstWOOSPCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CstWOOSPCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CstWOOSPCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 22 | CstWOOSPCostsPEOQuantity | QUANTITY | — | ✅ |
| 23 | CstWOOSPCostsPEOStdCostId | STD_COST_ID | — | ✅ |
| 24 | CstWOOSPCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 25 | CstWOOSPCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 26 | CstWOOSPCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 27 | CstWOOSPCostsPEOUomCode | UOM_CODE | — | ✅ |
| 28 | CstWOOSPCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 29 | CstWOOSPCostsPEOWoOspCostId | WO_OSP_COST_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
