---
id: DOC-OTHER-PVO-VcsExtHistSupplyForecastDetailsExtractPVO
doc_type: system-doc
title: "VcsExtHistSupplyForecastDetailsExtractPVO — PVO Cross-Module"
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
  - VcsExtHistSupplyForecastDetailsExtractPVO
  - vcsexthistsupplyforecastdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtHistSupplyForecastDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Hist Supply Forecast Details Extract. Acessa as tabelas: VCS_BUCKETS, VCS_PLANNING_SCH_DETAILS_HIST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtHistSupplyForecastDetailsExtractPVO`

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
| 1 | VcsExtHistSupplyForecastDetailsPEOBucketId | BUCKET_ID | — | ✅ |
| 2 | VcsExtHistSupplyForecastDetailsPEOBucketIndex | BUCKET_INDEX | — | ✅ |
| 3 | VcsExtHistSupplyForecastDetailsPEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 4 | VcsExtHistSupplyForecastDetailsPEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 5 | VcsExtHistSupplyForecastDetailsPEOCommitBucketId | RESPONSE_BUCKET_ID | — | ✅ |
| 6 | VcsExtHistSupplyForecastDetailsPEOCommitDate | COMMIT_DATE | — | ✅ |
| 7 | VcsExtHistSupplyForecastDetailsPEOCommitDetailVersion | COMMIT_DETAIL_VERSION | — | ✅ |
| 8 | VcsExtHistSupplyForecastDetailsPEOCommitDueDate | COMMIT_DUE_DATE | — | ✅ |
| 9 | VcsExtHistSupplyForecastDetailsPEOCommitMismatchReasonCode | COMMIT_REASON_CODE | — | ✅ |
| 10 | VcsExtHistSupplyForecastDetailsPEOCommitQuantity | RESPONSE_QUANTITY | — | ✅ |
| 11 | VcsExtHistSupplyForecastDetailsPEOCommitQuantityUOM | RESPONSE_QUANTITY_UOM | — | ✅ |
| 12 | VcsExtHistSupplyForecastDetailsPEOCommittedByPartyCode | COMMITTED_BY_PARTY | — | ✅ |
| 13 | VcsExtHistSupplyForecastDetailsPEOCommittedByPersonId | COMMITTED_BY | — | ✅ |
| 14 | VcsExtHistSupplyForecastDetailsPEOCorrelationCode | COMMIT_CORRELATION_CODE | — | ✅ |
| 15 | VcsExtHistSupplyForecastDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | VcsExtHistSupplyForecastDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | VcsExtHistSupplyForecastDetailsPEOCumulativeCommitQuantity | CUMULATIVE_RESPONSE_QUANTITY | — | ✅ |
| 18 | VcsExtHistSupplyForecastDetailsPEOCumulativeForecastQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 19 | VcsExtHistSupplyForecastDetailsPEOEntryDetailId | ENTRY_DETAIL_ID | 🔑 | ✅ |
| 20 | VcsExtHistSupplyForecastDetailsPEOForecastDetailVersion | FORECAST_DETAIL_VERSION | — | ✅ |
| 21 | VcsExtHistSupplyForecastDetailsPEOForecastQuantity | QUANTITY | — | ✅ |
| 22 | VcsExtHistSupplyForecastDetailsPEOForecastQuantityUOM | QUANTITY_UOM | — | ✅ |
| 23 | VcsExtHistSupplyForecastDetailsPEOIsCurrentFlag | IS_CURRENT_FLAG | — | ✅ |
| 24 | VcsExtHistSupplyForecastDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | VcsExtHistSupplyForecastDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | VcsExtHistSupplyForecastDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | VcsExtHistSupplyForecastDetailsPEOPublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 28 | VcsExtHistSupplyForecastDetailsPEOPublishedByUserName | PUBLISHED_BY | — | ✅ |
| 29 | VcsExtHistSupplyForecastDetailsPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 30 | VcsExtHistSupplyForecastDetailsPEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 31 | VcsExtHistSupplyForecastDetailsPEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 32 | VcsExtHistSupplyForecastDetailsPEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
