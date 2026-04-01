---
id: DOC-OTHER-PVO-VcsDemandMeasuresExtractPVO
doc_type: system-doc
title: "VcsDemandMeasuresExtractPVO — PVO Cross-Module"
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
  - VcsDemandMeasuresExtractPVO
  - vcsdemandmeasuresextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDemandMeasuresExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Demand Measures Extract. Acessa as tabelas: VCS_DEMAND_MEASURES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDemandMeasuresExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_demand_measures|VCS_DEMAND_MEASURES]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[vcs_demand_measures|VCS_DEMAND_MEASURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDemandMeasuresPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCDemandMeasuresPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCDemandMeasuresPEOCurrentCycleFlag | CURRENT_CYCLE_FLAG | — | ✅ |
| 4 | DCDemandMeasuresPEOIdentityId | IDENTITY_ID | — | ✅ |
| 5 | DCDemandMeasuresPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DCDemandMeasuresPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DCDemandMeasuresPEOMeasureDate | MEASURE_DATE | — | ✅ |
| 8 | DCDemandMeasuresPEOMeasureDetailsId | MEASURE_DETAILS_ID | 🔑 | ✅ |
| 9 | DCDemandMeasuresPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 10 | DCDemandMeasuresPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | DCDemandMeasuresPEOPublishByUsername | PUB_BY_USERNAME | — | ✅ |
| 12 | DCDemandMeasuresPEOPublishDate | PUB_DATE | — | ✅ |
| 13 | DCDemandMeasuresPEOPublishSourceCode | PUB_SOURCE_CODE | — | ✅ |
| 14 | DCDemandMeasuresPEOQuantity | QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
