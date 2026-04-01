---
id: DOC-OTHER-PVO-VcsSupplyForecastReferenceMeasureExtractPVO
doc_type: system-doc
title: "VcsSupplyForecastReferenceMeasureExtractPVO — PVO Cross-Module"
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
  - VcsSupplyForecastReferenceMeasureExtractPVO
  - vcssupplyforecastreferencemeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsSupplyForecastReferenceMeasureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Supply Forecast Reference Measure Extract. Acessa as tabelas: VCS_BUCKETS, VCS_REF_MEASURES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsSupplyForecastReferenceMeasureExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_buckets|VCS_BUCKETS]] — 3 atributos (3 BICC)
- [[vcs_ref_measures|VCS_REF_MEASURES]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[vcs_buckets|VCS_BUCKETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsSupplyForecastReferenceMeasurePEORefMeasureBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsSupplyForecastReferenceMeasurePEORefMeasureBucketStartDate | BKT_START_DATE | — | ✅ |
| 3 | VcsSupplyForecastReferenceMeasurePEORefMeasureBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_ref_measures|VCS_REF_MEASURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsSupplyForecastReferenceMeasurePEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 2 | VcsSupplyForecastReferenceMeasurePEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 3 | VcsSupplyForecastReferenceMeasurePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | VcsSupplyForecastReferenceMeasurePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | VcsSupplyForecastReferenceMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | VcsSupplyForecastReferenceMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | VcsSupplyForecastReferenceMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsSupplyForecastReferenceMeasurePEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 9 | VcsSupplyForecastReferenceMeasurePEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 10 | VcsSupplyForecastReferenceMeasurePEORefMeasureBucketId | BUCKET_ID | — | ✅ |
| 11 | VcsSupplyForecastReferenceMeasurePEORefMeasurePublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 12 | VcsSupplyForecastReferenceMeasurePEORefMeasurePublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 13 | VcsSupplyForecastReferenceMeasurePEORefMeasurePublishedDate | PUBLISHED_DATE | — | ✅ |
| 14 | VcsSupplyForecastReferenceMeasurePEORefMeasureQuantity | QUANTITY | — | ✅ |
| 15 | VcsSupplyForecastReferenceMeasurePEORefMeasureQuantityUOM | QUANTITY_UOM | — | ✅ |
| 16 | VcsSupplyForecastReferenceMeasurePEOReferenceDetailId | REF_DETAIL_ID | 🔑 | ✅ |
| 17 | VcsSupplyForecastReferenceMeasurePEOReferenceHeaderId | REF_HEADER_ID | — | ✅ |
| 18 | VcsSupplyForecastReferenceMeasurePEOReferenceHeaderNumber | REF_HEADER_NUMBER | — | ✅ |
| 19 | VcsSupplyForecastReferenceMeasurePEOReferenceLineId | REF_LINE_ID | — | ✅ |
| 20 | VcsSupplyForecastReferenceMeasurePEOReferenceLineLocationId | REF_LINE_LOCATION_ID | — | ✅ |
| 21 | VcsSupplyForecastReferenceMeasurePEOReferenceLineLocationNumber | REF_LINE_LOCATION_NUMBER | — | ✅ |
| 22 | VcsSupplyForecastReferenceMeasurePEOReferenceLineNumber | REF_LINE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
