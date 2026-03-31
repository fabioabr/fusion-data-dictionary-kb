---
id: DOC-OTHER-PVO-VcsExtSupplyForecastReferenceMeasureExtractPVO
doc_type: system-doc
title: "VcsExtSupplyForecastReferenceMeasureExtractPVO — PVO Cross-Module"
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
  - VcsExtSupplyForecastReferenceMeasureExtractPVO
  - vcsextsupplyforecastreferencemeasureextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsExtSupplyForecastReferenceMeasureExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Ext Supply Forecast Reference Measure Extract. Acessa as tabelas: VCS_BUCKETS, VCS_REF_MEASURES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsBiccExtractAM.VcsExtSupplyForecastReferenceMeasureExtractPVO`

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
| 1 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureBucketEndDate | BKT_END_DATE | — | ✅ |
| 2 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureBucketStartDate | BKT_START_DATE | — | ✅ |
| 3 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureBucketType | BUCKET_TYPE | — | ✅ |

### [[vcs_ref_measures|VCS_REF_MEASURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | VcsExtSupplyForecastReferenceMeasurePEOCollaborationOrderForecastEntryId | COLLAB_ENTRY_ID | — | ✅ |
| 2 | VcsExtSupplyForecastReferenceMeasurePEOCollaborationSourceId | COLLAB_SOURCE_ID | — | ✅ |
| 3 | VcsExtSupplyForecastReferenceMeasurePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | VcsExtSupplyForecastReferenceMeasurePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | VcsExtSupplyForecastReferenceMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | VcsExtSupplyForecastReferenceMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | VcsExtSupplyForecastReferenceMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | VcsExtSupplyForecastReferenceMeasurePEOPublisherOrderType | PUBLISHER_ORDER_TYPE | — | ✅ |
| 9 | VcsExtSupplyForecastReferenceMeasurePEOReceivedDate | RECEIVED_DATE | — | ✅ |
| 10 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureBucketId | BUCKET_ID | — | ✅ |
| 11 | VcsExtSupplyForecastReferenceMeasurePEORefMeasurePublishedByPartyCode | PUBLISHED_BY_PARTY | — | ✅ |
| 12 | VcsExtSupplyForecastReferenceMeasurePEORefMeasurePublishedByPersonId | PUBLISHED_BY | — | ✅ |
| 13 | VcsExtSupplyForecastReferenceMeasurePEORefMeasurePublishedDate | PUBLISHED_DATE | — | ✅ |
| 14 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureQuantity | QUANTITY | — | ✅ |
| 15 | VcsExtSupplyForecastReferenceMeasurePEORefMeasureQuantityUOM | QUANTITY_UOM | — | ✅ |
| 16 | VcsExtSupplyForecastReferenceMeasurePEOReferenceDetailId | REF_DETAIL_ID | 🔑 | ✅ |
| 17 | VcsExtSupplyForecastReferenceMeasurePEOReferenceHeaderId | REF_HEADER_ID | — | ✅ |
| 18 | VcsExtSupplyForecastReferenceMeasurePEOReferenceHeaderNumber | REF_HEADER_NUMBER | — | ✅ |
| 19 | VcsExtSupplyForecastReferenceMeasurePEOReferenceLineId | REF_LINE_ID | — | ✅ |
| 20 | VcsExtSupplyForecastReferenceMeasurePEOReferenceLineLocationId | REF_LINE_LOCATION_ID | — | ✅ |
| 21 | VcsExtSupplyForecastReferenceMeasurePEOReferenceLineLocationNumber | REF_LINE_LOCATION_NUMBER | — | ✅ |
| 22 | VcsExtSupplyForecastReferenceMeasurePEOReferenceLineNumber | REF_LINE_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
