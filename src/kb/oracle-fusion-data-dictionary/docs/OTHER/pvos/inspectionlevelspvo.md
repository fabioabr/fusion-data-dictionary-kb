---
id: DOC-OTHER-PVO-InspectionLevelsPVO
doc_type: system-doc
title: "InspectionLevelsPVO — PVO Cross-Module"
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
  - InspectionLevelsPVO
  - inspectionlevelspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InspectionLevelsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inspection Levels. Acessa as tabelas: QA_INSPECTION_LEVELS_B, QA_INSPECTION_LEVELS_TL.

**Caminho:** `FscmTopModelAM.InspectionLevelAM.InspectionLevelsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 24 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_levels_b|QA_INSPECTION_LEVELS_B]] — 19 atributos (1 PKs, 13 BICC)
- [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_levels_b|QA_INSPECTION_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionLevelsBasePEOAcceptanceQualityLimit | ACCEPTANCE_QUALITY_LIMIT | — | — |
| 2 | InspectionLevelsBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | InspectionLevelsBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | InspectionLevelsBasePEOInspectionLevelCode | INSPECTION_LEVEL_CODE | — | — |
| 5 | InspectionLevelsBasePEOInspectionLevelId | INSPECTION_LEVEL_ID | 🔑 | ✅ |
| 6 | InspectionLevelsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionLevelsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionLevelsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionLevelsBasePEONumLots | NUM_LOTS | — | ✅ |
| 10 | InspectionLevelsBasePEONumLotsInspect | NUM_LOTS_INSPECT | — | ✅ |
| 11 | InspectionLevelsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | InspectionLevelsBasePEOPercentSampling | PERCENT_SAMPLING | — | ✅ |
| 13 | InspectionLevelsBasePEOQuantityPerSample | QUANTITY_PER_SAMPLE | — | — |
| 14 | InspectionLevelsBasePEOSamplingEnabledFlag | SAMPLING_ENABLED_FLAG | — | ✅ |
| 15 | InspectionLevelsBasePEOSamplingPlanType | SAMPLING_PLAN_TYPE | — | — |
| 16 | InspectionLevelsBasePEOSamplingStdCode | SAMPLING_STD_CODE | — | — |
| 17 | InspectionLevelsBasePEOSkiplotEnabledFlag | SKIPLOT_ENABLED_FLAG | — | ✅ |
| 18 | InspectionlevelsBasePEOFixedSamplingCount | FIXED_SAMPLING_COUNT | — | ✅ |
| 19 | inspectionLevelsBasePEOSampleUomCode | SAMPLE_UOM_CODE | — | — |

### [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionLevelsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionLevelsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionLevelsTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionLevelsTLPEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 5 | InspectionLevelsTLPEOLanguage | LANGUAGE | — | ✅ |
| 6 | InspectionLevelsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionLevelsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionLevelsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionLevelsTLPEOName | NAME | — | ✅ |
| 10 | InspectionLevelsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | InspectionLevelsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
