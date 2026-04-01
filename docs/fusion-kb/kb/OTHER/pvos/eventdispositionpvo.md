---
id: DOC-OTHER-PVO-EventDispositionPVO
doc_type: system-doc
title: "EventDispositionPVO — PVO Cross-Module"
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
  - EventDispositionPVO
  - eventdispositionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventDispositionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Disposition. Acessa as tabelas: PER_PERSON_NAMES_F_V, QA_INSPECTION_PLANS_B, QA_IP_EVENTS (+1).

**Caminho:** `FscmTopModelAM.ResultsAM.EventDispositionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 109 | 4 | 1 | 68 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]] — 27 atributos
- [[qa_ip_events|QA_IP_EVENTS]] — 60 atributos (54 BICC)
- [[qa_ip_event_dispositions|QA_IP_EVENT_DISPOSITIONS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 2 | CreatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CreatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CreatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 5 | LastUpdatedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 6 | LastUpdatedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | LastUpdatedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | LastUpdatedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansBaseRptPEOApprover | APPROVER | — | — |
| 2 | InspectionPlansBaseRptPEOAssetGroupId | ASSET_GROUP_ID | — | — |
| 3 | InspectionPlansBaseRptPEOAssetId | ASSET_ID | — | — |
| 4 | InspectionPlansBaseRptPEOCategoryId | CATEGORY_ID | — | — |
| 5 | InspectionPlansBaseRptPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 6 | InspectionPlansBaseRptPEOCreatedBy | CREATED_BY | — | — |
| 7 | InspectionPlansBaseRptPEOCreationDate | CREATION_DATE | — | — |
| 8 | InspectionPlansBaseRptPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | InspectionPlansBaseRptPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 10 | InspectionPlansBaseRptPEOEnabledFlag | ENABLED_FLAG | — | — |
| 11 | InspectionPlansBaseRptPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | — |
| 12 | InspectionPlansBaseRptPEOInspectionPlanCode | INSPECTION_PLAN_CODE | — | — |
| 13 | InspectionPlansBaseRptPEOInspectionPlanId | INSPECTION_PLAN_ID | — | — |
| 14 | InspectionPlansBaseRptPEOInspectionPlanStatus | INSPECTION_PLAN_STATUS | — | — |
| 15 | InspectionPlansBaseRptPEOInspectionPlanType | INSPECTION_PLAN_TYPE | — | — |
| 16 | InspectionPlansBaseRptPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 17 | InspectionPlansBaseRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | InspectionPlansBaseRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | InspectionPlansBaseRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | InspectionPlansBaseRptPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | InspectionPlansBaseRptPEOOptionalFlag | OPTIONAL_FLAG | — | — |
| 22 | InspectionPlansBaseRptPEOOrganizationId | ORGANIZATION_ID | — | — |
| 23 | InspectionPlansBaseRptPEOOwner | OWNER | — | — |
| 24 | InspectionPlansBaseRptPEOResourceId | RESOURCE_ID | — | — |
| 25 | InspectionPlansBaseRptPEORevision | REVISION | — | — |
| 26 | InspectionPlansBaseRptPEOVersionNumber | VERSION_NUMBER | — | — |
| 27 | InspectionPlansBaseRptPEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[qa_ip_events|QA_IP_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionEventsPEOAcceptanceNumber | ACCEPTANCE_NUMBER | — | — |
| 2 | InspectionEventsPEOCategoryId | CATEGORY_ID | — | ✅ |
| 3 | InspectionEventsPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 4 | InspectionEventsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | InspectionEventsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | InspectionEventsPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 7 | InspectionEventsPEODispatchStatus | DISPATCH_STATUS | — | ✅ |
| 8 | InspectionEventsPEODispositionDate | DISPOSITION_DATE | — | ✅ |
| 9 | InspectionEventsPEODocLineNumber | DOC_LINE_NUM | — | ✅ |
| 10 | InspectionEventsPEODocNumber | DOC_NUMBER | — | ✅ |
| 11 | InspectionEventsPEODocScheduleNumber | DOC_SCHEDULE_NUMBER | — | ✅ |
| 12 | InspectionEventsPEODocType | DOC_TYPE | — | ✅ |
| 13 | InspectionEventsPEODraftFlag | DRAFT_FLAG | — | ✅ |
| 14 | InspectionEventsPEOEventType | EVENT_TYPE | — | ✅ |
| 15 | InspectionEventsPEOInlineFlag | INLINE_FLAG | — | ✅ |
| 16 | InspectionEventsPEOInspectedBy | INSPECTED_BY | — | ✅ |
| 17 | InspectionEventsPEOInspectionDate | INSPECTION_DATE | — | ✅ |
| 18 | InspectionEventsPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 19 | InspectionEventsPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 20 | InspectionEventsPEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 21 | InspectionEventsPEOInterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 22 | InspectionEventsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 23 | InspectionEventsPEOIpCriteriaId | IP_CRITERIA_ID | — | ✅ |
| 24 | InspectionEventsPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 25 | InspectionEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | InspectionEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | InspectionEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | InspectionEventsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 29 | InspectionEventsPEOLotNumber | LOT_NUMBER | — | ✅ |
| 30 | InspectionEventsPEONonConformanceCount | NON_CONFORMANCE_COUNT | — | — |
| 31 | InspectionEventsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | InspectionEventsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 33 | InspectionEventsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 34 | InspectionEventsPEOOriginalDisposition | ORIGINAL_DISPOSITION | — | ✅ |
| 35 | InspectionEventsPEOQtyAccepted | QTY_ACCEPTED | — | ✅ |
| 36 | InspectionEventsPEOQtyInspected | QTY_INSPECTED | — | ✅ |
| 37 | InspectionEventsPEOQtyRejected | QTY_REJECTED | — | ✅ |
| 38 | InspectionEventsPEOQtyRequested | QTY_REQUESTED | — | ✅ |
| 39 | InspectionEventsPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 40 | InspectionEventsPEORejectionNumber | REJECTION_NUMBER | — | — |
| 41 | InspectionEventsPEOResourceId | RESOURCE_ID | — | ✅ |
| 42 | InspectionEventsPEORevisionId | REVISION_ID | — | ✅ |
| 43 | InspectionEventsPEOSampleSizeCode | SAMPLE_SIZE_CODE | — | — |
| 44 | InspectionEventsPEOSamplingQty | SAMPLING_QTY | — | ✅ |
| 45 | InspectionEventsPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 46 | InspectionEventsPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 47 | InspectionEventsPEOSourceLineQty | SOURCE_LINE_QTY | — | ✅ |
| 48 | InspectionEventsPEOSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 49 | InspectionEventsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 50 | InspectionEventsPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 51 | InspectionEventsPEOSupplierLotNum | SUPPLIER_LOT_NUM | — | ✅ |
| 52 | InspectionEventsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 53 | InspectionEventsPEOTotalSampleQuantity | TOTAL_SAMPLE_QUANTITY | — | — |
| 54 | InspectionEventsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 55 | InspectionEventsPEOUomCode | UOM_CODE | — | ✅ |
| 56 | InspectionEventsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 57 | InspectionEventsPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 58 | InspectionEventsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 59 | InspectionEventsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 60 | InspectionEventsRptPEOAssetId | ASSET_ID | — | — |

### [[qa_ip_event_dispositions|QA_IP_EVENT_DISPOSITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDispositionPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EventDispositionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EventDispositionPEODisposition | DISPOSITION | — | ✅ |
| 4 | EventDispositionPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 5 | EventDispositionPEOIpEventDispositionId | IP_EVENT_DISPOSITION_ID | 🔑 | ✅ |
| 6 | EventDispositionPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 7 | EventDispositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventDispositionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | EventDispositionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | EventDispositionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | EventDispositionPEOQuantity | QUANTITY | — | ✅ |
| 12 | EventDispositionPEORcvIntTxnId | RCV_INT_TXN_ID | — | ✅ |
| 13 | EventDispositionPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 14 | EventDispositionPEOWoOperationTxnId | WO_OPERATION_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
