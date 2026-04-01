---
id: DOC-OTHER-PVO-LineExtractPVO
doc_type: system-doc
title: "LineExtractPVO — PVO Cross-Module"
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
  - LineExtractPVO
  - lineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Line Extract. Acessa as tabelas: DOO_LINES_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.LineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 1 | 1 | 49 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos (1 PKs, 49 BICC)

---

## ⚙️ Atributos

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 2 | LineCanceledFlag | CANCELED_FLAG | — | ✅ |
| 3 | LineCanceledQty | CANCELED_QTY | — | ✅ |
| 4 | LineCategoryCode | CATEGORY_CODE | — | ✅ |
| 5 | LineCompSeqPath | COMP_SEQ_PATH | — | ✅ |
| 6 | LineCreatedBy | CREATED_BY | — | ✅ |
| 7 | LineCreationDate | CREATION_DATE | — | ✅ |
| 8 | LineDeltaType | DELTA_TYPE | — | ✅ |
| 9 | LineDisplayLineNumber | DISPLAY_LINE_NUMBER | — | ✅ |
| 10 | LineExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 11 | LineFulfilledQty | FULFILLED_QTY | — | ✅ |
| 12 | LineFulfillmentDate | FULFILLMENT_DATE | — | ✅ |
| 13 | LineHeaderId | HEADER_ID | — | ✅ |
| 14 | LineId | LINE_ID | 🔑 | ✅ |
| 15 | LineInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | LineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 17 | LineItemTypeCode | ITEM_TYPE_CODE | — | ✅ |
| 18 | LineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | LineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | LineLineNumber | LINE_NUMBER | — | ✅ |
| 22 | LineLineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 23 | LineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | LineOnHold | ON_HOLD | — | ✅ |
| 25 | LineOpenFlag | OPEN_FLAG | — | ✅ |
| 26 | LineOrderedQty | ORDERED_QTY | — | ✅ |
| 27 | LineOrderedUom | ORDERED_UOM | — | ✅ |
| 28 | LineOrgId | ORG_ID | — | ✅ |
| 29 | LineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | ✅ |
| 30 | LineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 31 | LineOwnerId | OWNER_ID | — | ✅ |
| 32 | LineParentLineId | PARENT_LINE_ID | — | ✅ |
| 33 | LineReferenceLineId | REFERENCE_LINE_ID | — | ✅ |
| 34 | LineRmaDeliveredQty | RMA_DELIVERED_QTY | — | ✅ |
| 35 | LineRootParentLineId | ROOT_PARENT_LINE_ID | — | ✅ |
| 36 | LineScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 37 | LineShippedQty | SHIPPED_QTY | — | ✅ |
| 38 | LineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 39 | LineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 40 | LineSourceOrderId | SOURCE_ORDER_ID | — | ✅ |
| 41 | LineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 42 | LineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 43 | LineSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 44 | LineSourceScheduleId | SOURCE_SCHEDULE_ID | — | ✅ |
| 45 | LineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | ✅ |
| 46 | LineStatusCode | STATUS_CODE | — | ✅ |
| 47 | LineTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | ✅ |
| 48 | LineUnitListPrice | UNIT_LIST_PRICE | — | ✅ |
| 49 | LineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
