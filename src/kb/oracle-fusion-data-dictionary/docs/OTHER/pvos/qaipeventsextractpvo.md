---
id: DOC-OTHER-PVO-QaIpEventsExtractPVO
doc_type: system-doc
title: "QaIpEventsExtractPVO — PVO Cross-Module"
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
  - QaIpEventsExtractPVO
  - qaipeventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaIpEventsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Ip Events Extract. Acessa as tabelas: QA_IP_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaIpEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 1 | 1 | 60 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_ip_events|QA_IP_EVENTS]] — 60 atributos (1 PKs, 60 BICC)

---

## ⚙️ Atributos

### [[qa_ip_events|QA_IP_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaIpEventsPEOAcceptanceNumber | ACCEPTANCE_NUMBER | — | ✅ |
| 2 | QaIpEventsPEOAssetId | ASSET_ID | — | ✅ |
| 3 | QaIpEventsPEOCategoryId | CATEGORY_ID | — | ✅ |
| 4 | QaIpEventsPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 5 | QaIpEventsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | QaIpEventsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | QaIpEventsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 8 | QaIpEventsPEODispatchStatus | DISPATCH_STATUS | — | ✅ |
| 9 | QaIpEventsPEODispositionDate | DISPOSITION_DATE | — | ✅ |
| 10 | QaIpEventsPEODocLineNumber | DOC_LINE_NUM | — | ✅ |
| 11 | QaIpEventsPEODocNumber | DOC_NUMBER | — | ✅ |
| 12 | QaIpEventsPEODocScheduleNumber | DOC_SCHEDULE_NUMBER | — | ✅ |
| 13 | QaIpEventsPEODocType | DOC_TYPE | — | ✅ |
| 14 | QaIpEventsPEODraftFlag | DRAFT_FLAG | — | ✅ |
| 15 | QaIpEventsPEOEventType | EVENT_TYPE | — | ✅ |
| 16 | QaIpEventsPEOInlineFlag | INLINE_FLAG | — | ✅ |
| 17 | QaIpEventsPEOInspectedBy | INSPECTED_BY | — | ✅ |
| 18 | QaIpEventsPEOInspectionDate | INSPECTION_DATE | — | ✅ |
| 19 | QaIpEventsPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 20 | QaIpEventsPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 21 | QaIpEventsPEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 22 | QaIpEventsPEOInterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 23 | QaIpEventsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 24 | QaIpEventsPEOIpCriteriaId | IP_CRITERIA_ID | — | ✅ |
| 25 | QaIpEventsPEOIpEventId | IP_EVENT_ID | 🔑 | ✅ |
| 26 | QaIpEventsPEOItemRevision | ITEM_REVISION | — | ✅ |
| 27 | QaIpEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | QaIpEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | QaIpEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | QaIpEventsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 31 | QaIpEventsPEOLotNumber | LOT_NUMBER | — | ✅ |
| 32 | QaIpEventsPEONonConformanceCount | NON_CONFORMANCE_COUNT | — | ✅ |
| 33 | QaIpEventsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 34 | QaIpEventsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 35 | QaIpEventsPEOOriginalDisposition | ORIGINAL_DISPOSITION | — | ✅ |
| 36 | QaIpEventsPEOQtyAccepted | QTY_ACCEPTED | — | ✅ |
| 37 | QaIpEventsPEOQtyInspected | QTY_INSPECTED | — | ✅ |
| 38 | QaIpEventsPEOQtyRejected | QTY_REJECTED | — | ✅ |
| 39 | QaIpEventsPEOQtyRequested | QTY_REQUESTED | — | ✅ |
| 40 | QaIpEventsPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 41 | QaIpEventsPEORejectionNumber | REJECTION_NUMBER | — | ✅ |
| 42 | QaIpEventsPEOResourceId | RESOURCE_ID | — | ✅ |
| 43 | QaIpEventsPEORevisionId | REVISION_ID | — | ✅ |
| 44 | QaIpEventsPEOSampleSizeCode | SAMPLE_SIZE_CODE | — | ✅ |
| 45 | QaIpEventsPEOSamplingQty | SAMPLING_QTY | — | ✅ |
| 46 | QaIpEventsPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 47 | QaIpEventsPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 48 | QaIpEventsPEOSourceLineQty | SOURCE_LINE_QTY | — | ✅ |
| 49 | QaIpEventsPEOSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 50 | QaIpEventsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 51 | QaIpEventsPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 52 | QaIpEventsPEOSupplierLotNum | SUPPLIER_LOT_NUM | — | ✅ |
| 53 | QaIpEventsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 54 | QaIpEventsPEOTotalSampleQuantity | TOTAL_SAMPLE_QUANTITY | — | ✅ |
| 55 | QaIpEventsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 56 | QaIpEventsPEOUomCode | UOM_CODE | — | ✅ |
| 57 | QaIpEventsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 58 | QaIpEventsPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 59 | QaIpEventsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 60 | QaIpEventsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
