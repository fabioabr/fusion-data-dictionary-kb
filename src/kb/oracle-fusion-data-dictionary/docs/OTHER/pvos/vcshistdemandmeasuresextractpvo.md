---
id: DOC-OTHER-PVO-VcsHistDemandMeasuresExtractPVO
doc_type: system-doc
title: "VcsHistDemandMeasuresExtractPVO — PVO Cross-Module"
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
  - VcsHistDemandMeasuresExtractPVO
  - vcshistdemandmeasuresextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsHistDemandMeasuresExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Hist Demand Measures Extract. Acessa as tabelas: VCS_DEMAND_MEASURES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsHistDemandMeasuresExtractPVO`

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
| 1 | DCHistDemandMeasuresPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCHistDemandMeasuresPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCHistDemandMeasuresPEOCurrentCycleFlag | CURRENT_CYCLE_FLAG | — | ✅ |
| 4 | DCHistDemandMeasuresPEOIdentityId | IDENTITY_ID | — | ✅ |
| 5 | DCHistDemandMeasuresPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DCHistDemandMeasuresPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DCHistDemandMeasuresPEOMeasureDate | MEASURE_DATE | — | ✅ |
| 8 | DCHistDemandMeasuresPEOMeasureDetailsId | MEASURE_DETAILS_ID | 🔑 | ✅ |
| 9 | DCHistDemandMeasuresPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 10 | DCHistDemandMeasuresPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | DCHistDemandMeasuresPEOPublishByUsername | PUB_BY_USERNAME | — | ✅ |
| 12 | DCHistDemandMeasuresPEOPublishDate | PUB_DATE | — | ✅ |
| 13 | DCHistDemandMeasuresPEOPublishSourceCode | PUB_SOURCE_CODE | — | ✅ |
| 14 | DCHistDemandMeasuresPEOQuantity | QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
