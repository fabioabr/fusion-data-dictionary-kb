---
id: DOC-OTHER-PVO-PlantShiftExceptionExtractPVO
doc_type: system-doc
title: "PlantShiftExceptionExtractPVO — PVO Cross-Module"
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
  - PlantShiftExceptionExtractPVO
  - plantshiftexceptionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlantShiftExceptionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Plant Shift Exception Extract. Acessa as tabelas: RCS_PLANT_SHIFT_EXC_B, RCS_PLANT_SHIFT_EXC_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.PlantShiftExceptionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_plant_shift_exc_b|RCS_PLANT_SHIFT_EXC_B]] — 17 atributos (1 PKs, 17 BICC)
- [[rcs_plant_shift_exc_tl|RCS_PLANT_SHIFT_EXC_TL]] — 4 atributos (4 BICC)

---

## ⚙️ Atributos

### [[rcs_plant_shift_exc_b|RCS_PLANT_SHIFT_EXC_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlantShiftExcId | PLANT_SHIFT_EXC_ID | 🔑 | ✅ |
| 2 | PlantShiftExceptionPEOAssociatedShiftId | ASSOCIATED_SHIFT_ID | — | ✅ |
| 3 | PlantShiftExceptionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PlantShiftExceptionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PlantShiftExceptionPEOEndDate | END_DATE | — | ✅ |
| 6 | PlantShiftExceptionPEOExcDuration | EXC_DURATION | — | ✅ |
| 7 | PlantShiftExceptionPEOExcEndTime | EXC_END_TIME | — | ✅ |
| 8 | PlantShiftExceptionPEOExcStartTime | EXC_START_TIME | — | ✅ |
| 9 | PlantShiftExceptionPEOExceptionType | EXCEPTION_TYPE | — | ✅ |
| 10 | PlantShiftExceptionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PlantShiftExceptionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PlantShiftExceptionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PlantShiftExceptionPEOMfgWcId | MFG_WC_ID | — | ✅ |
| 14 | PlantShiftExceptionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | PlantShiftExceptionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | PlantShiftExceptionPEOScheduleId | SCHEDULE_ID | — | ✅ |
| 17 | PlantShiftExceptionPEOStartDate | START_DATE | — | ✅ |

### [[rcs_plant_shift_exc_tl|RCS_PLANT_SHIFT_EXC_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlantShiftExceptionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 2 | PlantShiftExceptionTranslationPEOName | NAME | — | ✅ |
| 3 | PlantShiftExceptionTranslationPEOPlantShiftExcId1 | PLANT_SHIFT_EXC_ID | — | ✅ |
| 4 | PlantShiftExceptionTranslationPEOReason | REASON | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
