---
id: DOC-OTHER-PVO-SCPlanningSchedDetailsHist
doc_type: system-doc
title: "SCPlanningSchedDetailsHist — PVO Cross-Module"
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
  - SCPlanningSchedDetailsHist
  - scplanningscheddetailshist
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SCPlanningSchedDetailsHist

## 📌 Visão Geral

View Object para extração BICC de dados de SCPlanning Sched Details Hist. Acessa as tabelas: VCS_BUCKETS, VCS_BUCKET_ASSOCIATIONS, VCS_COLLAB_ENT_HIST (+4).

**Caminho:** `FscmTopModelAM.SupplyCollaborationAM.SCPlanningSchedDetailsHist`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 191 | 7 | 2 | 45 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_buckets|VCS_BUCKETS]] — 9 atributos (2 BICC)
- [[vcs_bucket_associations|VCS_BUCKET_ASSOCIATIONS]] — 9 atributos (1 BICC)
- [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]] — 83 atributos (1 PKs, 25 BICC)
- [[vcs_mngd_exceptions_hist_v|VCS_MNGD_EXCEPTIONS_HIST_V]] — 6 atributos (2 BICC)
- [[vcs_participants|VCS_PARTICIPANTS]] — 26 atributos (2 BICC)
- [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]] — 47 atributos (1 PKs, 12 BICC)
- [[vcs_schedule|VCS_SCHEDULE]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[vcs_buckets|VCS_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BucketsBktEndDate | BKT_END_DATE | — | — |
| 2 | BucketsBktStartDate | BKT_START_DATE | — | ✅ |
| 3 | BucketsBucketId | BUCKET_ID | — | — |
| 4 | BucketsBucketType | BUCKET_TYPE | — | — |
| 5 | BucketsCreatedBy | CREATED_BY | — | — |
| 6 | BucketsCreationDate | CREATION_DATE | — | — |
| 7 | BucketsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BucketsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | BucketsLastUpdatedBy | LAST_UPDATED_BY | — | — |

### [[vcs_bucket_associations|VCS_BUCKET_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BucketsAssociationAssociationTypeCode | ASSOCIATION_TYPE_CODE | — | — |
| 2 | BucketsAssociationBaseBucketId | BASE_BUCKET_ID | — | — |
| 3 | BucketsAssociationCreatedBy | CREATED_BY | — | — |
| 4 | BucketsAssociationCreationDate | CREATION_DATE | — | — |
| 5 | BucketsAssociationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BucketsAssociationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | BucketsAssociationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | BucketsAssociationRelatedBucketId | RELATED_BUCKET_ID | — | — |
| 9 | BucketsAssociationVcsScheduleId | VCS_SCHEDULE_ID | — | — |

### [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MainCollabBucketCountCommitHorizonMonthly | BUCKET_COUNT_CH_MONTHLY | — | ✅ |
| 2 | MainCollabBucketCountCommitHorizonWeekly | BUCKET_COUNT_CH_WEEKLY | — | ✅ |
| 3 | MainCollabBucketCountForecastHorizonMonthly | BUCKET_COUNT_FH_MONTHLY | — | ✅ |
| 4 | MainCollabBucketCountForecastHorizonWeekly | BUCKET_COUNT_FH_WEEKLY | — | ✅ |
| 5 | MainCollabCollabEntryVersion | COLLAB_ENTRY_VERSION | — | — |
| 6 | MainCollabCollabSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 7 | MainCollabCommitDate | COMMIT_DATE | — | ✅ |
| 8 | MainCollabCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 9 | MainCollabCommitHorizonCqty | COMMIT_HORIZON_CQTY | — | ✅ |
| 10 | MainCollabCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | ✅ |
| 11 | MainCollabCommitHorizonFqty | COMMIT_HORIZON_FQTY | — | ✅ |
| 12 | MainCollabCommitMismatchCountMonthly | COMMIT_MISMATCH_COUNT_MONTHLY | — | ✅ |
| 13 | MainCollabCommitMismatchCountWeekly | COMMIT_MISMATCH_COUNT_WEEKLY | — | ✅ |
| 14 | MainCollabCommitToForecastMAPEMonthly | CTF_MAPE_MONTHLY | — | ✅ |
| 15 | MainCollabCommitToForecastMAPEWeekly | CTF_MAPE_WEEKLY | — | ✅ |
| 16 | MainCollabCreatedBy | CREATED_BY | — | — |
| 17 | MainCollabCreationDate | CREATION_DATE | — | — |
| 18 | MainCollabDetailLastUpdateEnt | DETAIL_LAST_UPDATE_ENT | — | — |
| 19 | MainCollabDetailLastUpdateSup | DETAIL_LAST_UPDATE_SUP | — | — |
| 20 | MainCollabEntDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | — |
| 21 | MainCollabEntryId | ENTRY_ID | 🔑 | ✅ |
| 22 | MainCollabEntryTypeId | ENTRY_TYPE_ID | — | — |
| 23 | MainCollabForecastChangeCountMonthly | FORECAST_CHANGE_COUNT_MONTHLY | — | ✅ |
| 24 | MainCollabForecastChangeCountWeekly | FORECAST_CHANGE_COUNT_WEEKLY | — | ✅ |
| 25 | MainCollabForecastChangeMAPEMonthly | FORECAST_CHANGE_MAPE_MONTHLY | — | ✅ |
| 26 | MainCollabForecastChangeMAPEWeekly | FORECAST_CHANGE_MAPE_WEEKLY | — | ✅ |
| 27 | MainCollabForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | ✅ |
| 28 | MainCollabForecastHorizonFqty | FORECAST_HORIZON_FQTY | — | ✅ |
| 29 | MainCollabInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 30 | MainCollabInventoryItemOrgId | INVENTORY_ITEM_ORG_ID | — | — |
| 31 | MainCollabLastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | — |
| 32 | MainCollabLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | MainCollabLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | MainCollabLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | MainCollabMaxCommitVersion | MAX_COMMIT_VERSION | — | — |
| 36 | MainCollabMaxForecastVersion | MAX_FORECAST_VERSION | — | ✅ |
| 37 | MainCollabObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | MainCollabOrchCorrelationCode | ORCH_CORRELATION_CODE | — | — |
| 39 | MainCollabPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | — |
| 40 | MainCollabPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | ✅ |
| 41 | MainCollabPublishedBy | PUBLISHED_BY | — | — |
| 42 | MainCollabPublishedDate | PUBLISHED_DATE | — | ✅ |
| 43 | MainCollabShipFromId | SHIP_FROM_ID | — | — |
| 44 | MainCollabShipToId | SHIP_TO_ID | — | — |
| 45 | MainCollabSlaDays | SLA_DAYS | — | — |
| 46 | MainCollabStatusCode | STATUS_CODE | — | — |
| 47 | MainCollabSupDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | — |
| 48 | MainCollabTimeLevel | TIME_LEVEL | — | — |
| 49 | PreviousCollabCollabEntryVersion | COLLAB_ENTRY_VERSION | — | — |
| 50 | PreviousCollabCollabSourceId | COLLAB_SOURCE_ID | — | — |
| 51 | PreviousCollabCommitDate | COMMIT_DATE | — | — |
| 52 | PreviousCollabCommitDueDate | COMMIT_DUE_DATE | — | — |
| 53 | PreviousCollabCommitHorizonCqty | COMMIT_HORIZON_CQTY | — | — |
| 54 | PreviousCollabCommitHorizonEndDate | COMMIT_HORIZON_END_DATE | — | — |
| 55 | PreviousCollabCommitHorizonFqty | COMMIT_HORIZON_FQTY | — | — |
| 56 | PreviousCollabCreatedBy | CREATED_BY | — | — |
| 57 | PreviousCollabCreationDate | CREATION_DATE | — | — |
| 58 | PreviousCollabDetailLastUpdateEnt | DETAIL_LAST_UPDATE_ENT | — | — |
| 59 | PreviousCollabDetailLastUpdateSup | DETAIL_LAST_UPDATE_SUP | — | — |
| 60 | PreviousCollabEntDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | — |
| 61 | PreviousCollabEntryId | ENTRY_ID | — | — |
| 62 | PreviousCollabEntryTypeId | ENTRY_TYPE_ID | — | — |
| 63 | PreviousCollabForecastHorizonEndDate | FORECAST_HORIZON_END_DATE | — | — |
| 64 | PreviousCollabForecastHorizonFqty | FORECAST_HORIZON_FQTY | — | — |
| 65 | PreviousCollabInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 66 | PreviousCollabInventoryItemOrgId | INVENTORY_ITEM_ORG_ID | — | — |
| 67 | PreviousCollabLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 68 | PreviousCollabLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 69 | PreviousCollabLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 70 | PreviousCollabMaxCommitVersion | MAX_COMMIT_VERSION | — | — |
| 71 | PreviousCollabMaxForecastVersion | MAX_FORECAST_VERSION | — | — |
| 72 | PreviousCollabObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | PreviousCollabOrchCorrelationCode | ORCH_CORRELATION_CODE | — | — |
| 74 | PreviousCollabPublishCycleEndDate | PUBLISH_CYCLE_END_DATE | — | — |
| 75 | PreviousCollabPublishCycleStartDate | PUBLISH_CYCLE_START_DATE | — | — |
| 76 | PreviousCollabPublishedBy | PUBLISHED_BY | — | — |
| 77 | PreviousCollabPublishedDate | PUBLISHED_DATE | — | — |
| 78 | PreviousCollabShipFromId | SHIP_FROM_ID | — | — |
| 79 | PreviousCollabShipToId | SHIP_TO_ID | — | — |
| 80 | PreviousCollabSlaDays | SLA_DAYS | — | — |
| 81 | PreviousCollabStatusCode | STATUS_CODE | — | — |
| 82 | PreviousCollabSupDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | — |
| 83 | PreviousCollabTimeLevel | TIME_LEVEL | — | — |

### [[vcs_mngd_exceptions_hist_v|VCS_MNGD_EXCEPTIONS_HIST_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollabCommitExceptionsCollaborationEntryId | COLLABORATION_ENTRY_ID | — | ✅ |
| 2 | CollabCommitExceptionsExceptionFlag | EXCEPTION_FLAG | — | — |
| 3 | CollabCommitExceptionsExceptionTypeCode | EXCEPTION_TYPE_CODE | — | — |
| 4 | CollabForecastExceptionsCollaborationEntryId | COLLABORATION_ENTRY_ID | — | ✅ |
| 5 | CollabForecastExceptionsExceptionFlag | EXCEPTION_FLAG | — | — |
| 6 | CollabForecastExceptionsExceptionTypeCode | EXCEPTION_TYPE_CODE | — | — |

### [[vcs_participants|VCS_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipFromCreatedBy | CREATED_BY | — | — |
| 2 | ShipFromCreationDate | CREATION_DATE | — | — |
| 3 | ShipFromCustomerId | CUSTOMER_ID | — | — |
| 4 | ShipFromCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 5 | ShipFromLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ShipFromLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ShipFromLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ShipFromObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ShipFromOrganizationId | ORGANIZATION_ID | — | — |
| 10 | ShipFromPartnerCode | PARTNER_CODE | — | — |
| 11 | ShipFromVcsParticipantId | VCS_PARTICIPANT_ID | — | — |
| 12 | ShipFromVendorId | VENDOR_ID | — | — |
| 13 | ShipFromVendorSiteId | VENDOR_SITE_ID | — | — |
| 14 | ShipToCreatedBy | CREATED_BY | — | — |
| 15 | ShipToCreationDate | CREATION_DATE | — | — |
| 16 | ShipToCustomerId | CUSTOMER_ID | — | — |
| 17 | ShipToCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 18 | ShipToLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ShipToLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ShipToLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | ShipToObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ShipToOrganizationId | ORGANIZATION_ID | — | — |
| 23 | ShipToPartnerCode | PARTNER_CODE | — | — |
| 24 | ShipToVcsParticipantId | VCS_PARTICIPANT_ID | — | — |
| 25 | ShipToVendorId | VENDOR_ID | — | — |
| 26 | ShipToVendorSiteId | VENDOR_SITE_ID | — | — |

### [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrentCycleScheduleBucketId | BUCKET_ID | — | ✅ |
| 2 | CurrentCycleScheduleBucketIndex | BUCKET_INDEX | — | — |
| 3 | CurrentCycleScheduleCollabEntryId | COLLAB_ENTRY_ID | 🔑 | ✅ |
| 4 | CurrentCycleScheduleCollabSourceId | COLLAB_SOURCE_ID | — | — |
| 5 | CurrentCycleScheduleCommitCorrelationCode | COMMIT_CORRELATION_CODE | — | — |
| 6 | CurrentCycleScheduleCommitDate | COMMIT_DATE | — | — |
| 7 | CurrentCycleScheduleCommitDetailVersion | COMMIT_DETAIL_VERSION | — | ✅ |
| 8 | CurrentCycleScheduleCommitDueDate | COMMIT_DUE_DATE | — | — |
| 9 | CurrentCycleScheduleCommitReasonCode | COMMIT_REASON_CODE | — | — |
| 10 | CurrentCycleScheduleCommittedBy | COMMITTED_BY | — | — |
| 11 | CurrentCycleScheduleCommittedByParty | COMMITTED_BY_PARTY | — | ✅ |
| 12 | CurrentCycleScheduleCreatedBy | CREATED_BY | — | — |
| 13 | CurrentCycleScheduleCreationDate | CREATION_DATE | — | — |
| 14 | CurrentCycleScheduleCumulativeQuantity | CUMULATIVE_QUANTITY | — | — |
| 15 | CurrentCycleScheduleCumulativeResponseQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | — |
| 16 | CurrentCycleScheduleDraftEntForecastBucketId | DRAFT_ENT_FORECAST_BUCKET_ID | — | — |
| 17 | CurrentCycleScheduleDraftEntForecastQuantity | DRAFT_ENT_FORECAST_QUANTITY | — | — |
| 18 | CurrentCycleScheduleDraftEntForecastUom | DRAFT_ENT_FORECAST_UOM | — | — |
| 19 | CurrentCycleScheduleDraftEnterpriseQuantity | DRAFT_ENTERPRISE_QUANTITY | — | — |
| 20 | CurrentCycleScheduleDraftEnterpriseQuantityUom | DRAFT_ENTERPRISE_QUANTITY_UOM | — | — |
| 21 | CurrentCycleScheduleDraftSupForecastBucketId | DRAFT_SUP_FORECAST_BUCKET_ID | — | — |
| 22 | CurrentCycleScheduleDraftSupForecastQuantity | DRAFT_SUP_FORECAST_QUANTITY | — | — |
| 23 | CurrentCycleScheduleDraftSupForecastUom | DRAFT_SUP_FORECAST_UOM | — | — |
| 24 | CurrentCycleScheduleDraftSupplierQuantity | DRAFT_SUPPLIER_QUANTITY | — | — |
| 25 | CurrentCycleScheduleDraftSupplierQuantityUom | DRAFT_SUPPLIER_QUANTITY_UOM | — | — |
| 26 | CurrentCycleScheduleEntDraftBucketId | ENT_DRAFT_BUCKET_ID | — | — |
| 27 | CurrentCycleScheduleEntDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | — |
| 28 | CurrentCycleScheduleEntryDetailId | ENTRY_DETAIL_ID | — | — |
| 29 | CurrentCycleScheduleForecastDetailVersion | FORECAST_DETAIL_VERSION | — | ✅ |
| 30 | CurrentCycleScheduleIsCurrentFlag | IS_CURRENT_FLAG | — | — |
| 31 | CurrentCycleScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | CurrentCycleScheduleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | CurrentCycleScheduleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | CurrentCycleScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | CurrentCycleSchedulePublishedBy | PUBLISHED_BY | — | ✅ |
| 36 | CurrentCycleSchedulePublishedByParty | PUBLISHED_BY_PARTY | — | ✅ |
| 37 | CurrentCycleSchedulePublishedDate | PUBLISHED_DATE | — | ✅ |
| 38 | CurrentCycleSchedulePublisherOrderType | PUBLISHER_ORDER_TYPE | — | — |
| 39 | CurrentCycleScheduleQuantity | QUANTITY | — | ✅ |
| 40 | CurrentCycleScheduleQuantityUom | QUANTITY_UOM | — | — |
| 41 | CurrentCycleScheduleReceivedDate | RECEIVED_DATE | — | — |
| 42 | CurrentCycleScheduleResponseBucketId | RESPONSE_BUCKET_ID | — | — |
| 43 | CurrentCycleScheduleResponseQuantity | RESPONSE_QUANTITY | — | ✅ |
| 44 | CurrentCycleScheduleResponseQuantityUom | RESPONSE_QUANTITY_UOM | — | — |
| 45 | CurrentCycleScheduleStatusCode | STATUS_CODE | — | — |
| 46 | CurrentCycleScheduleSupDraftBucketId | SUP_DRAFT_BUCKET_ID | — | — |
| 47 | CurrentCycleScheduleSupDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | — |

### [[vcs_schedule|VCS_SCHEDULE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BucketsScheduleCreatedBy | CREATED_BY | — | — |
| 2 | BucketsScheduleCreationDate | CREATION_DATE | — | — |
| 3 | BucketsScheduleDisplayedAggregationLevel | DISPLAYED_AGGREGATION_LEVEL | — | — |
| 4 | BucketsScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | BucketsScheduleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | BucketsScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | BucketsScheduleScheduleEndDate | SCHEDULE_END_DATE | — | — |
| 8 | BucketsScheduleScheduleStartDate | SCHEDULE_START_DATE | — | — |
| 9 | BucketsScheduleSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 10 | BucketsScheduleStatusCode | STATUS_CODE | — | — |
| 11 | BucketsScheduleVcsScheduleId | VCS_SCHEDULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
