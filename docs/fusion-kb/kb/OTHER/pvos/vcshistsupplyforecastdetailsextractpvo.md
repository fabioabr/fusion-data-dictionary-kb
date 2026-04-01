---
id: DOC-OTHER-PVO-VcsHistSupplyForecastDetailsExtractPVO
doc_type: system-doc
title: "VcsHistSupplyForecastDetailsExtractPVO — PVO Cross-Module"
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
  - VcsHistSupplyForecastDetailsExtractPVO
  - vcshistsupplyforecastdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsHistSupplyForecastDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Hist Supply Forecast Details Extract. Acessa as tabelas: VCS_BUCKETS, VCS_PLANNING_SCH_DETAILS_HIST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsHistSupplyForecastDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 1 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_buckets|VCS_BUCKETS]] — 4 atributos (4 BICC)
- [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]] — 32 atributos (1 PKs, 32 BICC)

---

## ⚙️ Atributos

### [[vcs_buckets|VCS_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsBucketsPEOBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsBucketsPEOBucketId | BUCKET_ID | — | ✅ |
| 3 | VcsBucketsPEOBucketStartDate | BKT_START_DATE | — | ✅ |
| 4 | VcsBucketsPEOBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_planning_sch_details_hist|VCS_PLANNING_SCH_DETAILS_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsHistSupplyForecastDetailsPEOBucketId | BUCKET_ID | — | ✅ |
| 2 | VcsHistSupplyForecastDetailsPEOBucketIndex | BUCKET_INDEX | — | ✅ |
| 3 | VcsHistSupplyForecastDetailsPEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 4 | VcsHistSupplyForecastDetailsPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 5 | VcsHistSupplyForecastDetailsPEOCommitBucketId | RESPONSE_BUCKET_ID | — | ✅ |
| 6 | VcsHistSupplyForecastDetailsPEOCommitDate | COMMIT_DATE | — | ✅ |
| 7 | VcsHistSupplyForecastDetailsPEOCommitDetailVersion | COMMIT_DETAIL_VERSION | — | ✅ |
| 8 | VcsHistSupplyForecastDetailsPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 9 | VcsHistSupplyForecastDetailsPEOCommitMismatchReasonCode | COMMIT_REASON_CODE | — | ✅ |
| 10 | VcsHistSupplyForecastDetailsPEOCommitQuantity | RESPONSE_QUANTITY | — | ✅ |
| 11 | VcsHistSupplyForecastDetailsPEOCommitQuantityUOM | RESPONSE_QUANTITY_UOM | — | ✅ |
| 12 | VcsHistSupplyForecastDetailsPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 13 | VcsHistSupplyForecastDetailsPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 14 | VcsHistSupplyForecastDetailsPEOCorrelationCode | COMMIT_CORRELATION_CODE | — | ✅ |
| 15 | VcsHistSupplyForecastDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | VcsHistSupplyForecastDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | VcsHistSupplyForecastDetailsPEOCumulativeCommitQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | ✅ |
| 18 | VcsHistSupplyForecastDetailsPEOCumulativeForecastQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 19 | VcsHistSupplyForecastDetailsPEOEntryDetailId | ENTRY_DETAIL_ID | 🔑 | ✅ |
| 20 | VcsHistSupplyForecastDetailsPEOForecastDetailVersion | FORECAST_DETAIL_VERSION | — | ✅ |
| 21 | VcsHistSupplyForecastDetailsPEOForecastQuantity | QUANTITY | — | ✅ |
| 22 | VcsHistSupplyForecastDetailsPEOForecastQuantityUOM | QUANTITY_UOM | — | ✅ |
| 23 | VcsHistSupplyForecastDetailsPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 24 | VcsHistSupplyForecastDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | VcsHistSupplyForecastDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | VcsHistSupplyForecastDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | VcsHistSupplyForecastDetailsPEOPublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 28 | VcsHistSupplyForecastDetailsPEOPublishedByUserName | PUBLISHED_BY | — | ✅ |
| 29 | VcsHistSupplyForecastDetailsPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 30 | VcsHistSupplyForecastDetailsPEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 31 | VcsHistSupplyForecastDetailsPEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 32 | VcsHistSupplyForecastDetailsPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
