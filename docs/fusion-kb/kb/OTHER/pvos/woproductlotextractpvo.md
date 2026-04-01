---
id: DOC-OTHER-PVO-WOProductLotExtractPVO
doc_type: system-doc
title: "WOProductLotExtractPVO — PVO Cross-Module"
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
  - WOProductLotExtractPVO
  - woproductlotextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOProductLotExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOProduct Lot Extract. Acessa as tabelas: WIE_WO_PRODUCT_LOTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOProductLotExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductLotPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkOrderProductLotPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderProductLotPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 4 | WorkOrderProductLotPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | WorkOrderProductLotPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | WorkOrderProductLotPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WorkOrderProductLotPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | WorkOrderProductLotPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | WorkOrderProductLotPEOLotNumber | LOT_NUMBER | — | ✅ |
| 10 | WorkOrderProductLotPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | WorkOrderProductLotPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | WorkOrderProductLotPEORequestId | REQUEST_ID | — | ✅ |
| 13 | WorkOrderProductLotPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | — | ✅ |
| 14 | WorkOrderProductLotPEOWoProductLotId | WO_PRODUCT_LOT_ID | 🔑 | ✅ |
| 15 | WorkOrderProductLotPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
