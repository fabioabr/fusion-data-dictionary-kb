---
id: DOC-OTHER-PVO-VcsHistSupplyForecastReferenceMeasureExtractPVO
doc_type: system-doc
title: "VcsHistSupplyForecastReferenceMeasureExtractPVO — PVO Cross-Module"
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
  - VcsHistSupplyForecastReferenceMeasureExtractPVO
  - vcshistsupplyforecastreferencemeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsHistSupplyForecastReferenceMeasureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Hist Supply Forecast Reference Measure Extract. Acessa as tabelas: VCS_BUCKETS, VCS_REF_MEASURES_HIST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsHistSupplyForecastReferenceMeasureExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_buckets|VCS_BUCKETS]] — 3 atributos (3 BICC)
- [[vcs_ref_measures_hist|VCS_REF_MEASURES_HIST]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[vcs_buckets|VCS_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureBucketStartDate | BKT_START_DATE | — | ✅ |
| 3 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_ref_measures_hist|VCS_REF_MEASURES_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsHistSupplyForecastReferenceMeasurePEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 2 | VcsHistSupplyForecastReferenceMeasurePEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 3 | VcsHistSupplyForecastReferenceMeasurePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | VcsHistSupplyForecastReferenceMeasurePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | VcsHistSupplyForecastReferenceMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | VcsHistSupplyForecastReferenceMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | VcsHistSupplyForecastReferenceMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsHistSupplyForecastReferenceMeasurePEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 9 | VcsHistSupplyForecastReferenceMeasurePEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 10 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureBucketId | BUCKET_ID | — | ✅ |
| 11 | VcsHistSupplyForecastReferenceMeasurePEORefMeasurePublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 12 | VcsHistSupplyForecastReferenceMeasurePEORefMeasurePublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 13 | VcsHistSupplyForecastReferenceMeasurePEORefMeasurePublishedDate | PUBLISHED_DATE | — | ✅ |
| 14 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureQuantity | QUANTITY | — | ✅ |
| 15 | VcsHistSupplyForecastReferenceMeasurePEORefMeasureQuantityUOM | QUANTITY_UOM | — | ✅ |
| 16 | VcsHistSupplyForecastReferenceMeasurePEOReferenceDetailId | REF_DETAIL_ID | 🔑 | ✅ |
| 17 | VcsHistSupplyForecastReferenceMeasurePEOReferenceHeaderId | REF_HEADER_ID | — | ✅ |
| 18 | VcsHistSupplyForecastReferenceMeasurePEOReferenceHeaderNumber | REF_HEADER_NUMBER | — | ✅ |
| 19 | VcsHistSupplyForecastReferenceMeasurePEOReferenceLineId | REF_LINE_ID | — | ✅ |
| 20 | VcsHistSupplyForecastReferenceMeasurePEOReferenceLineLocationId | REF_LINE_LOCATION_ID | — | ✅ |
| 21 | VcsHistSupplyForecastReferenceMeasurePEOReferenceLineLocationNumber | REF_LINE_LOCATION_NUMBER | — | ✅ |
| 22 | VcsHistSupplyForecastReferenceMeasurePEOReferenceLineNumber | REF_LINE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
