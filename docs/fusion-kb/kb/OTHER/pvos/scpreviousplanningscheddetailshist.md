---
id: DOC-OTHER-PVO-SCPreviousPlanningSchedDetailsHist
doc_type: system-doc
title: "SCPreviousPlanningSchedDetailsHist — PVO Cross-Module"
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
  - SCPreviousPlanningSchedDetailsHist
  - scpreviousplanningscheddetailshist
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SCPreviousPlanningSchedDetailsHist

## 📌 Visão Geral

View Object para extração BICC de dados de SCPrevious Planning Sched Details Hist. Acessa as tabelas: VCS_COLLAB_ENT_HIST, VCS_PLANNING_SCH_DETAILS_HIST.

**Caminho:** `FscmTopModelAM.SupplyCollaborationAM.SCPreviousPlanningSchedDetailsHist`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 2 | 1 | 5 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]] — 4 atributos
- [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]] — 47 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[vcs_collab_ent_hist|VCS_COLLAB_ENT_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntryId | ENTRY_ID | — | — |
| 2 | LastPublishedPlanName | LAST_PUBLISHED_PLAN_NAME | — | — |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ShipFromId | SHIP_FROM_ID | — | — |

### [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PreviousCycleSchedBucketId | BUCKET_ID | — | — |
| 2 | PreviousCycleSchedBucketIndex | BUCKET_INDEX | — | — |
| 3 | PreviousCycleSchedCollabEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 4 | PreviousCycleSchedCollabSourceId | COLLAB_SOURCE_ID | — | — |
| 5 | PreviousCycleSchedCommitCorrelationCode | COMMIT_CORRELATION_CODE | — | — |
| 6 | PreviousCycleSchedCommitDate | COMMIT_DATE | — | — |
| 7 | PreviousCycleSchedCommitDetailVersion | COMMIT_DETAIL_VERSION | — | — |
| 8 | PreviousCycleSchedCommitDueDate | COMMIT_DUE_DATE | — | — |
| 9 | PreviousCycleSchedCommitReasonCode | COMMIT_REASON_CODE | — | — |
| 10 | PreviousCycleSchedCommittedBy | COMMITTED_BY | — | — |
| 11 | PreviousCycleSchedCommittedByParty | COMMITTED_BY_PARTY | — | — |
| 12 | PreviousCycleSchedCreatedBy | CREATED_BY | — | — |
| 13 | PreviousCycleSchedCreationDate | CREATION_DATE | — | — |
| 14 | PreviousCycleSchedCumulativeQuantity | CUMULATIVE_QUANTITY | — | — |
| 15 | PreviousCycleSchedCumulativeResponseQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | — |
| 16 | PreviousCycleSchedDraftEntForecastBucketId | DRAFT_ENT_FORECAST_BUCKET_ID | — | — |
| 17 | PreviousCycleSchedDraftEntForecastQuantity | DRAFT_ENT_FORECAST_QUANTITY | — | — |
| 18 | PreviousCycleSchedDraftEntForecastUom | DRAFT_ENT_FORECAST_UOM | — | — |
| 19 | PreviousCycleSchedDraftEnterpriseQuantity | DRAFT_ENTERPRISE_QUANTITY | — | — |
| 20 | PreviousCycleSchedDraftEnterpriseQuantityUom | DRAFT_ENTERPRISE_QUANTITY_UOM | — | — |
| 21 | PreviousCycleSchedDraftSupForecastBucketId | DRAFT_SUP_FORECAST_BUCKET_ID | — | — |
| 22 | PreviousCycleSchedDraftSupForecastQuantity | DRAFT_SUP_FORECAST_QUANTITY | — | — |
| 23 | PreviousCycleSchedDraftSupForecastUom | DRAFT_SUP_FORECAST_UOM | — | — |
| 24 | PreviousCycleSchedDraftSupplierQuantity | DRAFT_SUPPLIER_QUANTITY | — | — |
| 25 | PreviousCycleSchedDraftSupplierQuantityUom | DRAFT_SUPPLIER_QUANTITY_UOM | — | — |
| 26 | PreviousCycleSchedEntDraftBucketId | ENT_DRAFT_BUCKET_ID | — | — |
| 27 | PreviousCycleSchedEntDraftQtyFlag | ENT_DRAFT_QTY_FLAG | — | — |
| 28 | PreviousCycleSchedEntryDetailId | ENTRY_DETAIL_ID | 🔑 | ✅ |
| 29 | PreviousCycleSchedForecastDetailVersion | FORECAST_DETAIL_VERSION | — | — |
| 30 | PreviousCycleSchedIsCurrentFlag | IS_CURRENT_FLAG | — | — |
| 31 | PreviousCycleSchedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | PreviousCycleSchedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | PreviousCycleSchedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | PreviousCycleSchedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | PreviousCycleSchedPreviousCollabQuantityUom | QUANTITY_UOM | — | — |
| 36 | PreviousCycleSchedPublishedBy | PUBLISHED_BY | — | — |
| 37 | PreviousCycleSchedPublishedByParty | PUBLISHED_BY_PARTY | — | — |
| 38 | PreviousCycleSchedPublishedDate | PUBLISHED_DATE | — | — |
| 39 | PreviousCycleSchedPublisherOrderType | PUBLISHER_ORDER_TYPE | — | — |
| 40 | PreviousCycleSchedQuantity | QUANTITY | — | ✅ |
| 41 | PreviousCycleSchedReceivedDate | RECEIVED_DATE | — | — |
| 42 | PreviousCycleSchedResponseBucketId | RESPONSE_BUCKET_ID | — | — |
| 43 | PreviousCycleSchedResponseQuantity | RESPONSE_QUANTITY | — | ✅ |
| 44 | PreviousCycleSchedResponseQuantityUom | RESPONSE_QUANTITY_UOM | — | — |
| 45 | PreviousCycleSchedStatusCode | STATUS_CODE | — | — |
| 46 | PreviousCycleSchedSupDraftBucketId | SUP_DRAFT_BUCKET_ID | — | — |
| 47 | PreviousCycleSchedSupDraftQtyFlag | SUP_DRAFT_QTY_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
