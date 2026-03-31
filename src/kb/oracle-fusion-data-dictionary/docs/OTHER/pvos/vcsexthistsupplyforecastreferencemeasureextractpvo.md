---
id: DOC-OTHER-PVO-VcsExtHistSupplyForecastReferenceMeasureExtractPVO
doc_type: system-doc
title: "VcsExtHistSupplyForecastReferenceMeasureExtractPVO — PVO Cross-Module"
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
  - VcsExtHistSupplyForecastReferenceMeasureExtractPVO
  - vcsexthistsupplyforecastreferencemeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtHistSupplyForecastReferenceMeasureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Hist Supply Forecast Reference Measure Extract. Acessa as tabelas: VCS_BUCKETS, VCS_REF_MEASURES_HIST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtHistSupplyForecastReferenceMeasureExtractPVO`

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
| 1 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureBucketStartDate | BKT_START_DATE | — | ✅ |
| 3 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_ref_measures_hist|VCS_REF_MEASURES_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsExtHistSupplyForecastReferenceMeasurePEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 2 | VcsExtHistSupplyForecastReferenceMeasurePEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 3 | VcsExtHistSupplyForecastReferenceMeasurePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | VcsExtHistSupplyForecastReferenceMeasurePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | VcsExtHistSupplyForecastReferenceMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | VcsExtHistSupplyForecastReferenceMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | VcsExtHistSupplyForecastReferenceMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsExtHistSupplyForecastReferenceMeasurePEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 9 | VcsExtHistSupplyForecastReferenceMeasurePEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 10 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureBucketId | BUCKET_ID | — | ✅ |
| 11 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasurePublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 12 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasurePublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 13 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasurePublishedDate | PUBLISHED_DATE | — | ✅ |
| 14 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureQuantity | QUANTITY | — | ✅ |
| 15 | VcsExtHistSupplyForecastReferenceMeasurePEORefMeasureQuantityUOM | QUANTITY_UOM | — | ✅ |
| 16 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceDetailId | REF_DETAIL_ID | 🔑 | ✅ |
| 17 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceHeaderId | REF_HEADER_ID | — | ✅ |
| 18 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceHeaderNumber | REF_HEADER_NUMBER | — | ✅ |
| 19 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceLineId | REF_LINE_ID | — | ✅ |
| 20 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceLineLocationId | REF_LINE_LOCATION_ID | — | ✅ |
| 21 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceLineLocationNumber | REF_LINE_LOCATION_NUMBER | — | ✅ |
| 22 | VcsExtHistSupplyForecastReferenceMeasurePEOReferenceLineNumber | REF_LINE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
