---
id: DOC-OTHER-PVO-VcsDemandMeasureAttributesExtractPVO
doc_type: system-doc
title: "VcsDemandMeasureAttributesExtractPVO — PVO Cross-Module"
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
  - VcsDemandMeasureAttributesExtractPVO
  - vcsdemandmeasureattributesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDemandMeasureAttributesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Demand Measure Attributes Extract. Acessa as tabelas: VCS_DEMAND_MEASURE_ATTRIBUTES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDemandMeasureAttributesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_demand_measure_attributes|VCS_DEMAND_MEASURE_ATTRIBUTES]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[vcs_demand_measure_attributes|VCS_DEMAND_MEASURE_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDemandMeasureAttributesPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCDemandMeasureAttributesPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCDemandMeasureAttributesPEOCycleStartDate | CYCLE_START_DATE | — | ✅ |
| 4 | DCDemandMeasureAttributesPEODataReceivedFlag | DATA_RECEIVED_FLAG | — | ✅ |
| 5 | DCDemandMeasureAttributesPEOEditStartDate | EDIT_START_DATE | — | ✅ |
| 6 | DCDemandMeasureAttributesPEOEndDate | END_DATE | — | ✅ |
| 7 | DCDemandMeasureAttributesPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 8 | DCDemandMeasureAttributesPEOExpirationProcessId | EXPIRATION_PROCESS_ID | — | ✅ |
| 9 | DCDemandMeasureAttributesPEOIdentityId | IDENTITY_ID | — | ✅ |
| 10 | DCDemandMeasureAttributesPEOIntegrationStatusCode | INTEGRATION_STATUS_CODE | — | ✅ |
| 11 | DCDemandMeasureAttributesPEOLastReceivedDate | LAST_RECEIVED_DATE | — | ✅ |
| 12 | DCDemandMeasureAttributesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DCDemandMeasureAttributesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | DCDemandMeasureAttributesPEOMeasureAttributeId | MEASURE_ATTRIBUTE_ID | 🔑 | ✅ |
| 15 | DCDemandMeasureAttributesPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 16 | DCDemandMeasureAttributesPEONewCycleProcessId | NEW_CYCLE_PROCESS_ID | — | ✅ |
| 17 | DCDemandMeasureAttributesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | DCDemandMeasureAttributesPEOPublishByPartyCode | PUBLISH_BY_PARTY_CODE | — | ✅ |
| 19 | DCDemandMeasureAttributesPEOPublishByUsername | PUBLISH_BY_USERNAME | — | ✅ |
| 20 | DCDemandMeasureAttributesPEOPublishCalendar | PUBLISH_CALENDAR | — | ✅ |
| 21 | DCDemandMeasureAttributesPEOPublishDate | PUBLISH_DATE | — | ✅ |
| 22 | DCDemandMeasureAttributesPEOPublishProcessId | PUBLISH_PROCESS_ID | — | ✅ |
| 23 | DCDemandMeasureAttributesPEOPublishSourceCode | PUBLISH_SOURCE_CODE | — | ✅ |
| 24 | DCDemandMeasureAttributesPEOPublishSourceName | PUBLISH_SOURCE_NAME | — | ✅ |
| 25 | DCDemandMeasureAttributesPEOStartDate | START_DATE | — | ✅ |
| 26 | DCDemandMeasureAttributesPEOTotalQuantity | TOTAL_QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
