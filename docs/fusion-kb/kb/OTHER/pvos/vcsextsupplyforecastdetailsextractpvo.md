---
id: DOC-OTHER-PVO-VcsExtSupplyForecastDetailsExtractPVO
doc_type: system-doc
title: "VcsExtSupplyForecastDetailsExtractPVO — PVO Cross-Module"
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
  - VcsExtSupplyForecastDetailsExtractPVO
  - vcsextsupplyforecastdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtSupplyForecastDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Supply Forecast Details Extract. Acessa as tabelas: VCS_BUCKETS, VCS_PLANNING_SCH_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtSupplyForecastDetailsExtractPVO`

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
| 1 | VcsExtSupplyForecastDetailsPEOBucketId | BUCKET_ID | — | ✅ |
| 2 | VcsExtSupplyForecastDetailsPEOBucketIndex | BUCKET_INDEX | — | ✅ |
| 3 | VcsExtSupplyForecastDetailsPEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 4 | VcsExtSupplyForecastDetailsPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 5 | VcsExtSupplyForecastDetailsPEOCommitBucketId | RESPONSE_BUCKET_ID | — | ✅ |
| 6 | VcsExtSupplyForecastDetailsPEOCommitDate | COMMIT_DATE | — | ✅ |
| 7 | VcsExtSupplyForecastDetailsPEOCommitDetailVersion | COMMIT_DETAIL_VERSION | — | ✅ |
| 8 | VcsExtSupplyForecastDetailsPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 9 | VcsExtSupplyForecastDetailsPEOCommitMismatchReasonCode | COMMIT_REASON_CODE | — | ✅ |
| 10 | VcsExtSupplyForecastDetailsPEOCommitQuantity | RESPONSE_QUANTITY | — | ✅ |
| 11 | VcsExtSupplyForecastDetailsPEOCommitQuantityUOM | RESPONSE_QUANTITY_UOM | — | ✅ |
| 12 | VcsExtSupplyForecastDetailsPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 13 | VcsExtSupplyForecastDetailsPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 14 | VcsExtSupplyForecastDetailsPEOCorrelationCode | COMMIT_CORRELATION_CODE | — | ✅ |
| 15 | VcsExtSupplyForecastDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | VcsExtSupplyForecastDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | VcsExtSupplyForecastDetailsPEOCumulativeCommitQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | ✅ |
| 18 | VcsExtSupplyForecastDetailsPEOCumulativeForecastQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 19 | VcsExtSupplyForecastDetailsPEODraftEnterpriseCommitBucketId | ENT_DRAFT_BUCKET_ID | — | ✅ |
| 20 | VcsExtSupplyForecastDetailsPEODraftEnterpriseCommitQuantity | DRAFT_ENTERPRISE_QUANTITY | — | ✅ |
| 21 | VcsExtSupplyForecastDetailsPEODraftEnterpriseCommitQuantityUom | DRAFT_ENTERPRISE_QUANTITY_UOM | — | ✅ |
| 22 | VcsExtSupplyForecastDetailsPEODraftEnterpriseForecastBucketId | DRAFT_ENT_FORECAST_BUCKET_ID | — | ✅ |
| 23 | VcsExtSupplyForecastDetailsPEODraftEnterpriseForecastQuantity | DRAFT_ENT_FORECAST_QUANTITY | — | ✅ |
| 24 | VcsExtSupplyForecastDetailsPEODraftEnterpriseQtyFlag | ENT_DRAFT_QTY_FLAG | — | ✅ |
| 25 | VcsExtSupplyForecastDetailsPEODraftEnterpriseQuantityUom | DRAFT_ENT_FORECAST_UOM | — | ✅ |
| 26 | VcsExtSupplyForecastDetailsPEODraftSupplierCommitBucketId | SUP_DRAFT_BUCKET_ID | — | ✅ |
| 27 | VcsExtSupplyForecastDetailsPEODraftSupplierCommitQuantity | DRAFT_SUPPLIER_QUANTITY | — | ✅ |
| 28 | VcsExtSupplyForecastDetailsPEODraftSupplierCommitQuantityUom | DRAFT_SUPPLIER_QUANTITY_UOM | — | ✅ |
| 29 | VcsExtSupplyForecastDetailsPEODraftSupplierForecastBucketId | DRAFT_SUP_FORECAST_BUCKET_ID | — | ✅ |
| 30 | VcsExtSupplyForecastDetailsPEODraftSupplierForecastQuantity | DRAFT_SUP_FORECAST_QUANTITY | — | ✅ |
| 31 | VcsExtSupplyForecastDetailsPEODraftSupplierForecastUom | DRAFT_SUP_FORECAST_UOM | — | ✅ |
| 32 | VcsExtSupplyForecastDetailsPEODraftSupplierQtyFlag | SUP_DRAFT_QTY_FLAG | — | ✅ |
| 33 | VcsExtSupplyForecastDetailsPEOEntryDetailId | ENTRY_DETAIL_ID | 🔑 | ✅ |
| 34 | VcsExtSupplyForecastDetailsPEOForecastDetailVersion | FORECAST_DETAIL_VERSION | — | ✅ |
| 35 | VcsExtSupplyForecastDetailsPEOForecastQuantity | QUANTITY | — | ✅ |
| 36 | VcsExtSupplyForecastDetailsPEOForecastQuantityUOM | QUANTITY_UOM | — | ✅ |
| 37 | VcsExtSupplyForecastDetailsPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 38 | VcsExtSupplyForecastDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | VcsExtSupplyForecastDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | VcsExtSupplyForecastDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | VcsExtSupplyForecastDetailsPEOPublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 42 | VcsExtSupplyForecastDetailsPEOPublishedByUserName | PUBLISHED_BY | — | ✅ |
| 43 | VcsExtSupplyForecastDetailsPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 44 | VcsExtSupplyForecastDetailsPEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 45 | VcsExtSupplyForecastDetailsPEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 46 | VcsExtSupplyForecastDetailsPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
