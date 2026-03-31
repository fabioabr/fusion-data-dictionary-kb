---
id: DOC-OTHER-PVO-VcsSupplyForecastDetailsExtractPVO
doc_type: system-doc
title: "VcsSupplyForecastDetailsExtractPVO — PVO Cross-Module"
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
  - VcsSupplyForecastDetailsExtractPVO
  - vcssupplyforecastdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsSupplyForecastDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Supply Forecast Details Extract. Acessa as tabelas: VCS_BUCKETS, VCS_PLANNING_SCH_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsSupplyForecastDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 2 | 50 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_buckets|VCS_BUCKETS]] — 4 atributos (1 PKs, 4 BICC)
- [[vcs_planning_sch_details|VCS_PLANNING_SCH_DETAILS]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[vcs_buckets|VCS_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsBucketsPEOBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsBucketsPEOBucketId | BUCKET_ID | 🔑 | ✅ |
| 3 | VcsBucketsPEOBucketStartDate | BKT_START_DATE | — | ✅ |
| 4 | VcsBucketsPEOBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_planning_sch_details|VCS_PLANNING_SCH_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsSupplyForecastDetailsPEOBucketId | BUCKET_ID | — | ✅ |
| 2 | VcsSupplyForecastDetailsPEOBucketIndex | BUCKET_INDEX | — | ✅ |
| 3 | VcsSupplyForecastDetailsPEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 4 | VcsSupplyForecastDetailsPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 5 | VcsSupplyForecastDetailsPEOCommitBucketId | RESPONSE_BUCKET_ID | — | ✅ |
| 6 | VcsSupplyForecastDetailsPEOCommitDate | COMMIT_DATE | — | ✅ |
| 7 | VcsSupplyForecastDetailsPEOCommitDetailVersion | COMMIT_DETAIL_VERSION | — | ✅ |
| 8 | VcsSupplyForecastDetailsPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 9 | VcsSupplyForecastDetailsPEOCommitMismatchReasonCode | COMMIT_REASON_CODE | — | ✅ |
| 10 | VcsSupplyForecastDetailsPEOCommitQuantity | RESPONSE_QUANTITY | — | ✅ |
| 11 | VcsSupplyForecastDetailsPEOCommitQuantityUOM | RESPONSE_QUANTITY_UOM | — | ✅ |
| 12 | VcsSupplyForecastDetailsPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 13 | VcsSupplyForecastDetailsPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 14 | VcsSupplyForecastDetailsPEOCorrelationCode | COMMIT_CORRELATION_CODE | — | ✅ |
| 15 | VcsSupplyForecastDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | VcsSupplyForecastDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | VcsSupplyForecastDetailsPEOCumulativeCommitQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | ✅ |
| 18 | VcsSupplyForecastDetailsPEOCumulativeForecastQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 19 | VcsSupplyForecastDetailsPEODraftEnterpriseCommitBucketId | ENT_DRAFT_BUCKET_ID | — | ✅ |
| 20 | VcsSupplyForecastDetailsPEODraftEnterpriseCommitQuantity | DRAFT_ENTERPRISE_QUANTITY | — | ✅ |
| 21 | VcsSupplyForecastDetailsPEODraftEnterpriseCommitQuantityUom | DRAFT_ENTERPRISE_QUANTITY_UOM | — | ✅ |
| 22 | VcsSupplyForecastDetailsPEODraftEnterpriseForecastBucketId | DRAFT_ENT_FORECAST_BUCKET_ID | — | ✅ |
| 23 | VcsSupplyForecastDetailsPEODraftEnterpriseForecastQuantity | DRAFT_ENT_FORECAST_QUANTITY | — | ✅ |
| 24 | VcsSupplyForecastDetailsPEODraftEnterpriseForecastUom | DRAFT_ENT_FORECAST_UOM | — | ✅ |
| 25 | VcsSupplyForecastDetailsPEODraftEnterpriseQtyFlag | ENT_DRAFT_QTY_FLAG | — | ✅ |
| 26 | VcsSupplyForecastDetailsPEODraftSupplierCommitBucketId | SUP_DRAFT_BUCKET_ID | — | ✅ |
| 27 | VcsSupplyForecastDetailsPEODraftSupplierCommitQuantity | DRAFT_SUPPLIER_QUANTITY | — | ✅ |
| 28 | VcsSupplyForecastDetailsPEODraftSupplierCommitQuantityUom | DRAFT_SUPPLIER_QUANTITY_UOM | — | ✅ |
| 29 | VcsSupplyForecastDetailsPEODraftSupplierForecastBucketId | DRAFT_SUP_FORECAST_BUCKET_ID | — | ✅ |
| 30 | VcsSupplyForecastDetailsPEODraftSupplierForecastQuantity | DRAFT_SUP_FORECAST_QUANTITY | — | ✅ |
| 31 | VcsSupplyForecastDetailsPEODraftSupplierForecastUom | DRAFT_SUP_FORECAST_UOM | — | ✅ |
| 32 | VcsSupplyForecastDetailsPEODraftSupplierQtyFlag | SUP_DRAFT_QTY_FLAG | — | ✅ |
| 33 | VcsSupplyForecastDetailsPEOEntryDetailId | ENTRY_DETAIL_ID | 🔑 | ✅ |
| 34 | VcsSupplyForecastDetailsPEOForecastDetailVersion | FORECAST_DETAIL_VERSION | — | ✅ |
| 35 | VcsSupplyForecastDetailsPEOForecastQuantity | QUANTITY | — | ✅ |
| 36 | VcsSupplyForecastDetailsPEOForecastQuantityUOM | QUANTITY_UOM | — | ✅ |
| 37 | VcsSupplyForecastDetailsPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 38 | VcsSupplyForecastDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | VcsSupplyForecastDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | VcsSupplyForecastDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | VcsSupplyForecastDetailsPEOPublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 42 | VcsSupplyForecastDetailsPEOPublishedByUserName | PUBLISHED_BY | — | ✅ |
| 43 | VcsSupplyForecastDetailsPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 44 | VcsSupplyForecastDetailsPEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 45 | VcsSupplyForecastDetailsPEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 46 | VcsSupplyForecastDetailsPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
