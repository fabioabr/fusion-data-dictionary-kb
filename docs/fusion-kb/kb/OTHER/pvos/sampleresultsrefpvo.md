---
id: DOC-OTHER-PVO-SampleResultsRefPVO
doc_type: system-doc
title: "SampleResultsRefPVO — PVO Cross-Module"
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
  - SampleResultsRefPVO
  - sampleresultsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SampleResultsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sample Results Ref. Acessa as tabelas: PER_PERSON_NAMES_F_V, QA_INSPECTION_PLANS_B, QA_IP_EVENTS (+2).

**Caminho:** `FscmTopModelAM.ResultsAM.SampleResultsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 169 | 5 | 1 | 86 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[qa_inspection_plans_b|QA_INSPECTION_PLANS_B]] — 27 atributos
- [[qa_ip_events|QA_IP_EVENTS]] — 60 atributos (54 BICC)
- [[qa_samples|QA_SAMPLES]] — 14 atributos (14 BICC)
- [[qa_sample_results|QA_SAMPLE_RESULTS]] — 60 atributos (1 PKs, 18 BICC)

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
| 1 | InspectionEventsRptPEOAcceptanceNumber | ACCEPTANCE_NUMBER | — | — |
| 2 | InspectionEventsRptPEOAssetId | ASSET_ID | — | — |
| 3 | InspectionEventsRptPEOCategoryId | CATEGORY_ID | — | ✅ |
| 4 | InspectionEventsRptPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 5 | InspectionEventsRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InspectionEventsRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InspectionEventsRptPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 8 | InspectionEventsRptPEODispatchStatus | DISPATCH_STATUS | — | ✅ |
| 9 | InspectionEventsRptPEODispositionDate | DISPOSITION_DATE | — | ✅ |
| 10 | InspectionEventsRptPEODocLineNumber | DOC_LINE_NUM | — | ✅ |
| 11 | InspectionEventsRptPEODocNumber | DOC_NUMBER | — | ✅ |
| 12 | InspectionEventsRptPEODocScheduleNumber | DOC_SCHEDULE_NUMBER | — | ✅ |
| 13 | InspectionEventsRptPEODocType | DOC_TYPE | — | ✅ |
| 14 | InspectionEventsRptPEODraftFlag | DRAFT_FLAG | — | ✅ |
| 15 | InspectionEventsRptPEOEventType | EVENT_TYPE | — | ✅ |
| 16 | InspectionEventsRptPEOInlineFlag | INLINE_FLAG | — | ✅ |
| 17 | InspectionEventsRptPEOInspectedBy | INSPECTED_BY | — | ✅ |
| 18 | InspectionEventsRptPEOInspectionDate | INSPECTION_DATE | — | ✅ |
| 19 | InspectionEventsRptPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 20 | InspectionEventsRptPEOInspectionPlanId | INSPECTION_PLAN_ID | — | ✅ |
| 21 | InspectionEventsRptPEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 22 | InspectionEventsRptPEOInterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 23 | InspectionEventsRptPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 24 | InspectionEventsRptPEOIpCriteriaId | IP_CRITERIA_ID | — | ✅ |
| 25 | InspectionEventsRptPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 26 | InspectionEventsRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | InspectionEventsRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | InspectionEventsRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | InspectionEventsRptPEOLocatorId | LOCATOR_ID | — | ✅ |
| 30 | InspectionEventsRptPEOLotNumber | LOT_NUMBER | — | ✅ |
| 31 | InspectionEventsRptPEONonConformanceCount | NON_CONFORMANCE_COUNT | — | — |
| 32 | InspectionEventsRptPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | InspectionEventsRptPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 34 | InspectionEventsRptPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 35 | InspectionEventsRptPEOOriginalDisposition | ORIGINAL_DISPOSITION | — | ✅ |
| 36 | InspectionEventsRptPEOQtyAccepted | QTY_ACCEPTED | — | ✅ |
| 37 | InspectionEventsRptPEOQtyInspected | QTY_INSPECTED | — | ✅ |
| 38 | InspectionEventsRptPEOQtyRejected | QTY_REJECTED | — | ✅ |
| 39 | InspectionEventsRptPEOQtyRequested | QTY_REQUESTED | — | ✅ |
| 40 | InspectionEventsRptPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 41 | InspectionEventsRptPEORejectionNumber | REJECTION_NUMBER | — | — |
| 42 | InspectionEventsRptPEOResourceId | RESOURCE_ID | — | ✅ |
| 43 | InspectionEventsRptPEORevisionId | REVISION_ID | — | ✅ |
| 44 | InspectionEventsRptPEOSampleSizeCode | SAMPLE_SIZE_CODE | — | — |
| 45 | InspectionEventsRptPEOSamplingQty | SAMPLING_QTY | — | ✅ |
| 46 | InspectionEventsRptPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 47 | InspectionEventsRptPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 48 | InspectionEventsRptPEOSourceLineQty | SOURCE_LINE_QTY | — | ✅ |
| 49 | InspectionEventsRptPEOSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 50 | InspectionEventsRptPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 51 | InspectionEventsRptPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 52 | InspectionEventsRptPEOSupplierLotNum | SUPPLIER_LOT_NUM | — | ✅ |
| 53 | InspectionEventsRptPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 54 | InspectionEventsRptPEOTotalSampleQuantity | TOTAL_SAMPLE_QUANTITY | — | — |
| 55 | InspectionEventsRptPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 56 | InspectionEventsRptPEOUomCode | UOM_CODE | — | ✅ |
| 57 | InspectionEventsRptPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 58 | InspectionEventsRptPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 59 | InspectionEventsRptPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 60 | InspectionEventsRptPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[qa_samples|QA_SAMPLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SamplesRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SamplesRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SamplesRptPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 4 | SamplesRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SamplesRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | SamplesRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | SamplesRptPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SamplesRptPEOOriginalDisposition | ORIGINAL_DISPOSITION | — | ✅ |
| 9 | SamplesRptPEOQuantity | QUANTITY | — | ✅ |
| 10 | SamplesRptPEOSampleId | SAMPLE_ID | — | ✅ |
| 11 | SamplesRptPEOSampleNumber | SAMPLE_NUMBER | — | ✅ |
| 12 | SamplesRptPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 13 | SamplesRptPEOUomCode | UOM_CODE | — | ✅ |
| 14 | SamplesRptPEOWoOperationTxnId | WO_OPERATION_TXN_ID | — | ✅ |

### [[qa_sample_results|QA_SAMPLE_RESULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SampleResultsRptPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | SampleResultsRptPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | SampleResultsRptPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | SampleResultsRptPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | SampleResultsRptPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | SampleResultsRptPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | SampleResultsRptPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | SampleResultsRptPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | SampleResultsRptPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | SampleResultsRptPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | SampleResultsRptPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | SampleResultsRptPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | SampleResultsRptPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | SampleResultsRptPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | SampleResultsRptPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | SampleResultsRptPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | SampleResultsRptPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | SampleResultsRptPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | SampleResultsRptPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | SampleResultsRptPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | SampleResultsRptPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | SampleResultsRptPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | SampleResultsRptPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | SampleResultsRptPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | SampleResultsRptPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | SampleResultsRptPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | SampleResultsRptPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | SampleResultsRptPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | SampleResultsRptPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | SampleResultsRptPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | SampleResultsRptPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | SampleResultsRptPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | SampleResultsRptPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | SampleResultsRptPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | SampleResultsRptPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | SampleResultsRptPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | SampleResultsRptPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | SampleResultsRptPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | SampleResultsRptPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | SampleResultsRptPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | SampleResultsRptPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | SampleResultsRptPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 43 | SampleResultsRptPEOComments | COMMENTS | — | ✅ |
| 44 | SampleResultsRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 45 | SampleResultsRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 46 | SampleResultsRptPEOInspectionDate | INSPECTION_DATE | — | ✅ |
| 47 | SampleResultsRptPEOIpEventId | IP_EVENT_ID | — | ✅ |
| 48 | SampleResultsRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | SampleResultsRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | SampleResultsRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | SampleResultsRptPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | SampleResultsRptPEOOptionalFlag | OPTIONAL_FLAG | — | — |
| 53 | SampleResultsRptPEOQuantity | QUANTITY | — | ✅ |
| 54 | SampleResultsRptPEOResultValueChar | RESULT_VALUE_CHAR | — | ✅ |
| 55 | SampleResultsRptPEOResultValueDate | RESULT_VALUE_DATE | — | ✅ |
| 56 | SampleResultsRptPEOResultValueNum | RESULT_VALUE_NUM | — | ✅ |
| 57 | SampleResultsRptPEOSampleId | SAMPLE_ID | — | ✅ |
| 58 | SampleResultsRptPEOSampleResultId | SAMPLE_RESULT_ID | 🔑 | ✅ |
| 59 | SampleResultsRptPEOUomCode | UOM_CODE | — | ✅ |
| 60 | SampleResultsRptPEOUserSequence | USER_SEQUENCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
