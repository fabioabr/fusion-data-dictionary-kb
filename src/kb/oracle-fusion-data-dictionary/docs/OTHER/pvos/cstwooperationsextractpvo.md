---
id: DOC-OTHER-PVO-CstWOOperationsExtractPVO
doc_type: system-doc
title: "CstWOOperationsExtractPVO — PVO Cross-Module"
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
  - CstWOOperationsExtractPVO
  - cstwooperationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOOperationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOOperations Extract. Acessa as tabelas: CST_WORK_ORDER_OPERATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOOperationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_work_order_operations|CST_WORK_ORDER_OPERATIONS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cst_work_order_operations|CST_WORK_ORDER_OPERATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOOperationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CstWOOperationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CstWOOperationsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 4 | CstWOOperationsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | 🔑 | ✅ |
| 5 | CstWOOperationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CstWOOperationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | CstWOOperationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | CstWOOperationsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 9 | CstWOOperationsPEOOperationType | OPERATION_TYPE | — | ✅ |
| 10 | CstWOOperationsPEOOspItemId | OSP_ITEM_ID | — | ✅ |
| 11 | CstWOOperationsPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 12 | CstWOOperationsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 13 | CstWOOperationsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 14 | CstWOOperationsPEOWorkDefinitionOperationId | WORK_DEFINITION_OPERATION_ID | — | ✅ |
| 15 | CstWOOperationsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
