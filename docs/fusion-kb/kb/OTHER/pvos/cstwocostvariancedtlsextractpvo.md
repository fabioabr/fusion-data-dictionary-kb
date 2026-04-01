---
id: DOC-OTHER-PVO-CstWOCostVarianceDtlsExtractPVO
doc_type: system-doc
title: "CstWOCostVarianceDtlsExtractPVO — PVO Cross-Module"
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
  - CstWOCostVarianceDtlsExtractPVO
  - cstwocostvariancedtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOCostVarianceDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOCost Variance Dtls Extract. Acessa as tabelas: CST_WO_DTL_COST_VARIANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOCostVarianceDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 1 | 1 | 41 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_dtl_cost_variances|CST_WO_DTL_COST_VARIANCES]] — 41 atributos (1 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[cst_wo_dtl_cost_variances|CST_WO_DTL_COST_VARIANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOCostVarianceDtlsPEOBasisType | BASIS_TYPE | — | ✅ |
| 2 | CstWOCostVarianceDtlsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CstWOCostVarianceDtlsPEOCostDate | COST_DATE | — | ✅ |
| 4 | CstWOCostVarianceDtlsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CstWOCostVarianceDtlsPEOCostOrganizationId | COST_ORGANIZATION_ID | — | ✅ |
| 6 | CstWOCostVarianceDtlsPEOCostingBatchOutputSize | COSTING_BATCH_OUTPUT_SIZE | — | ✅ |
| 7 | CstWOCostVarianceDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CstWOCostVarianceDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CstWOCostVarianceDtlsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 10 | CstWOCostVarianceDtlsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 11 | CstWOCostVarianceDtlsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CstWOCostVarianceDtlsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 13 | CstWOCostVarianceDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CstWOCostVarianceDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | CstWOCostVarianceDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | CstWOCostVarianceDtlsPEOMaterialInventoryItemId | MATERIAL_INVENTORY_ITEM_ID | — | ✅ |
| 17 | CstWOCostVarianceDtlsPEOOperationOutputItemId | OPERATION_OUTPUT_ITEM_ID | — | ✅ |
| 18 | CstWOCostVarianceDtlsPEOOperationSequenceNum | OPERATION_SEQUENCE_NUM | — | ✅ |
| 19 | CstWOCostVarianceDtlsPEOOutputInventoryItemId | OUTPUT_INVENTORY_ITEM_ID | — | ✅ |
| 20 | CstWOCostVarianceDtlsPEOOutputInventoryOrgId | OUTPUT_INVENTORY_ORG_ID | — | ✅ |
| 21 | CstWOCostVarianceDtlsPEOOutputUomCode | OUTPUT_UOM_CODE | — | ✅ |
| 22 | CstWOCostVarianceDtlsPEOResourceId | RESOURCE_ID | — | ✅ |
| 23 | CstWOCostVarianceDtlsPEOSccrSourceTypeCode | SCCR_SOURCE_TYPE_CODE | — | ✅ |
| 24 | CstWOCostVarianceDtlsPEOScenarioRollupDetailId | SCENARIO_ROLLUP_DETAIL_ID | — | ✅ |
| 25 | CstWOCostVarianceDtlsPEOScenarioRollupHeaderId | SCENARIO_ROLLUP_HEADER_ID | — | ✅ |
| 26 | CstWOCostVarianceDtlsPEOStdCostId | STD_COST_ID | — | ✅ |
| 27 | CstWOCostVarianceDtlsPEOSubstitutionFlag | SUBSTITUTION_FLAG | — | ✅ |
| 28 | CstWOCostVarianceDtlsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 29 | CstWOCostVarianceDtlsPEOUomCode | UOM_CODE | — | ✅ |
| 30 | CstWOCostVarianceDtlsPEOVarianceCost | VARIANCE_COST | — | ✅ |
| 31 | CstWOCostVarianceDtlsPEOVarianceGroup | VARIANCE_GROUP | — | ✅ |
| 32 | CstWOCostVarianceDtlsPEOVarianceType | VARIANCE_TYPE | — | ✅ |
| 33 | CstWOCostVarianceDtlsPEOWdMakeUnitCost | WD_MAKE_UNIT_COST | — | ✅ |
| 34 | CstWOCostVarianceDtlsPEOWdOperationId | WD_OPERATION_ID | — | ✅ |
| 35 | CstWOCostVarianceDtlsPEOWdScaledQty | WD_SCALED_QTY | — | ✅ |
| 36 | CstWOCostVarianceDtlsPEOWdUnitCost | WD_UNIT_COST | — | ✅ |
| 37 | CstWOCostVarianceDtlsPEOWoCompletionQty | WO_COMPLETION_QTY | — | ✅ |
| 38 | CstWOCostVarianceDtlsPEOWoDtlCostVarianceId | WO_DTL_COST_VARIANCE_ID | 🔑 | ✅ |
| 39 | CstWOCostVarianceDtlsPEOWoQuantity | WO_QUANTITY | — | ✅ |
| 40 | CstWOCostVarianceDtlsPEOWoUnitCost | WO_UNIT_COST | — | ✅ |
| 41 | CstWOCostVarianceDtlsPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
