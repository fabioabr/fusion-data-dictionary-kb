---
id: DOC-OTHER-PVO-VcsMeasureDefinitionsExtractPVO
doc_type: system-doc
title: "VcsMeasureDefinitionsExtractPVO — PVO Cross-Module"
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
  - VcsMeasureDefinitionsExtractPVO
  - vcsmeasuredefinitionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsMeasureDefinitionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Measure Definitions Extract. Acessa as tabelas: VCS_MEASURE_DEFINITIONS_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsMeasureDefinitionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_measure_definitions_b|VCS_MEASURE_DEFINITIONS_B]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[vcs_measure_definitions_b|VCS_MEASURE_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCMeasureDefinitionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCMeasureDefinitionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCMeasureDefinitionsPEODataTypeCode | DATA_TYPE_CODE | — | ✅ |
| 4 | DCMeasureDefinitionsPEOExpireFlag | EXPIRE_FLAG | — | ✅ |
| 5 | DCMeasureDefinitionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DCMeasureDefinitionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DCMeasureDefinitionsPEOMeasureId | MEASURE_ID | 🔑 | ✅ |
| 8 | DCMeasureDefinitionsPEOMeasureTypeCode | MEASURE_CODE | — | ✅ |
| 9 | DCMeasureDefinitionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
