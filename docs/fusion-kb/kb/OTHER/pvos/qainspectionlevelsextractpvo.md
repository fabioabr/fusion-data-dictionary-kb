---
id: DOC-OTHER-PVO-QaInspectionLevelsExtractPVO
doc_type: system-doc
title: "QaInspectionLevelsExtractPVO — PVO Cross-Module"
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
  - QaInspectionLevelsExtractPVO
  - qainspectionlevelsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaInspectionLevelsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Inspection Levels Extract. Acessa as tabelas: QA_INSPECTION_LEVELS_B, QA_INSPECTION_LEVELS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaInspectionLevelsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 2 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_levels_b|QA_INSPECTION_LEVELS_B]] — 13 atributos (13 BICC)
- [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_levels_b|QA_INSPECTION_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionLevelsBasePEOAcceptanceQualityLimit | ACCEPTANCE_QUALITY_LIMIT | — | ✅ |
| 2 | InspectionLevelsBasePEOFixedSamplingCount | FIXED_SAMPLING_COUNT | — | ✅ |
| 3 | InspectionLevelsBasePEOInspectionLevelCode | INSPECTION_LEVEL_CODE | — | ✅ |
| 4 | InspectionLevelsBasePEOInspectionLevelId | INSPECTION_LEVEL_ID | — | ✅ |
| 5 | InspectionLevelsBasePEONumLots | NUM_LOTS | — | ✅ |
| 6 | InspectionLevelsBasePEONumLotsInspect | NUM_LOTS_INSPECT | — | ✅ |
| 7 | InspectionLevelsBasePEOPercentSampling | PERCENT_SAMPLING | — | ✅ |
| 8 | InspectionLevelsBasePEOQuantityPerSample | QUANTITY_PER_SAMPLE | — | ✅ |
| 9 | InspectionLevelsBasePEOSampleUomCode | SAMPLE_UOM_CODE | — | ✅ |
| 10 | InspectionLevelsBasePEOSamplingEnabledFlag | SAMPLING_ENABLED_FLAG | — | ✅ |
| 11 | InspectionLevelsBasePEOSamplingPlanType | SAMPLING_PLAN_TYPE | — | ✅ |
| 12 | InspectionLevelsBasePEOSamplingStdCode | SAMPLING_STD_CODE | — | ✅ |
| 13 | InspectionLevelsBasePEOSkiplotEnabledFlag | SKIPLOT_ENABLED_FLAG | — | ✅ |

### [[qa_inspection_levels_tl|QA_INSPECTION_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionLevelsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionLevelsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionLevelsTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionLevelsTLPEOInspectionLevelId | INSPECTION_LEVEL_ID | 🔑 | ✅ |
| 5 | InspectionLevelsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InspectionLevelsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionLevelsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionLevelsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionLevelsTLPEOName | NAME | — | ✅ |
| 10 | InspectionLevelsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
