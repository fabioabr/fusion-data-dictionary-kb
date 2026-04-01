---
id: DOC-OTHER-PVO-CstWOOperationOutputsExtractPVO
doc_type: system-doc
title: "CstWOOperationOutputsExtractPVO — PVO Cross-Module"
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
  - CstWOOperationOutputsExtractPVO
  - cstwooperationoutputsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOOperationOutputsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOOperation Outputs Extract. Acessa as tabelas: CST_WO_OPERATION_OUTPUTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOOperationOutputsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_operation_outputs|CST_WO_OPERATION_OUTPUTS]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[cst_wo_operation_outputs|CST_WO_OPERATION_OUTPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOOperationOutputsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 2 | CstWOOperationOutputsPEOCostAllocationBasis | COST_ALLOCATION_BASIS | — | ✅ |
| 3 | CstWOOperationOutputsPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | ✅ |
| 4 | CstWOOperationOutputsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstWOOperationOutputsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstWOOperationOutputsPEOCstWoOperationOutputId | CST_WO_OPERATION_OUTPUT_ID | 🔑 | ✅ |
| 7 | CstWOOperationOutputsPEOCstWoUpdateEventId | CST_WO_UPDATE_EVENT_ID | — | ✅ |
| 8 | CstWOOperationOutputsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 9 | CstWOOperationOutputsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 10 | CstWOOperationOutputsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | CstWOOperationOutputsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CstWOOperationOutputsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | CstWOOperationOutputsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CstWOOperationOutputsPEOOutputQuantity | OUTPUT_QUANTITY | — | ✅ |
| 15 | CstWOOperationOutputsPEOOutputSeqNumber | OUTPUT_SEQ_NUMBER | — | ✅ |
| 16 | CstWOOperationOutputsPEOOutputType | OUTPUT_TYPE | — | ✅ |
| 17 | CstWOOperationOutputsPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 18 | CstWOOperationOutputsPEOUomCode | UOM_CODE | — | ✅ |
| 19 | CstWOOperationOutputsPEOWdOperationOutputId | WD_OPERATION_OUTPUT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
