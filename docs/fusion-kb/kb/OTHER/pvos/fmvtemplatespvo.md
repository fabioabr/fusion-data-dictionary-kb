---
id: DOC-OTHER-PVO-FmvTemplatesPVO
doc_type: system-doc
title: "FmvTemplatesPVO — PVO Cross-Module"
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
  - FmvTemplatesPVO
  - fmvtemplatespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FmvTemplatesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fmv Templates. Acessa as tabelas: VRM_FMV_TEMPLATES_B, VRM_FMV_TEMPLATES_TL.

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.FmvTemplatesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 2 | 8 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 52 atributos (3 BICC)
- [[vrm_fmv_templates_tl|VRM_FMV_TEMPLATES_TL]] — 11 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | FMVTemplateBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | FMVTemplateBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | FMVTemplateBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | FMVTemplateBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | FMVTemplateBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | FMVTemplateBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | FMVTemplateBaseAttribute16 | ATTRIBUTE16 | — | — |
| 9 | FMVTemplateBaseAttribute17 | ATTRIBUTE17 | — | — |
| 10 | FMVTemplateBaseAttribute18 | ATTRIBUTE18 | — | — |
| 11 | FMVTemplateBaseAttribute19 | ATTRIBUTE19 | — | — |
| 12 | FMVTemplateBaseAttribute2 | ATTRIBUTE2 | — | — |
| 13 | FMVTemplateBaseAttribute20 | ATTRIBUTE20 | — | — |
| 14 | FMVTemplateBaseAttribute3 | ATTRIBUTE3 | — | — |
| 15 | FMVTemplateBaseAttribute4 | ATTRIBUTE4 | — | — |
| 16 | FMVTemplateBaseAttribute5 | ATTRIBUTE5 | — | — |
| 17 | FMVTemplateBaseAttribute6 | ATTRIBUTE6 | — | — |
| 18 | FMVTemplateBaseAttribute7 | ATTRIBUTE7 | — | — |
| 19 | FMVTemplateBaseAttribute8 | ATTRIBUTE8 | — | — |
| 20 | FMVTemplateBaseAttribute9 | ATTRIBUTE9 | — | — |
| 21 | FMVTemplateBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | FMVTemplateBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | FMVTemplateBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | FMVTemplateBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | FMVTemplateBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | FMVTemplateBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | FMVTemplateBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | FMVTemplateBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | FMVTemplateBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | FMVTemplateBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | FMVTemplateBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | FMVTemplateBaseCreatedBy1 | CREATED_BY | — | — |
| 33 | FMVTemplateBaseCreationDate1 | CREATION_DATE | — | — |
| 34 | FMVTemplateBaseDataSelectionTimeSpan | DATA_SELECTION_TIME_SPAN | — | — |
| 35 | FMVTemplateBaseDimensionAssignmentId | DIMENSION_ASSIGNMENT_ID | — | — |
| 36 | FMVTemplateBaseElementType | ELEMENT_TYPE | — | ✅ |
| 37 | FMVTemplateBaseFmvPriceType | FMV_PRICE_TYPE | — | — |
| 38 | FMVTemplateBaseFmvRepresentationType | FMV_REPRESENTATION_TYPE | — | ✅ |
| 39 | FMVTemplateBaseFmvToleranceCode | FMV_TOLERANCE_CODE | — | — |
| 40 | FMVTemplateBaseInUse | IN_USE | — | — |
| 41 | FMVTemplateBaseIncludeCurrentPeriods | INCLUDE_CURRENT_PERIODS | — | — |
| 42 | FMVTemplateBaseLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 43 | FMVTemplateBaseLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 44 | FMVTemplateBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 45 | FMVTemplateBaseMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 46 | FMVTemplateBaseObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 47 | FMVTemplateBaseStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 48 | FMVTemplateBaseTemplateId1 | TEMPLATE_ID | — | — |
| 49 | FMVTemplateBaseTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | — |
| 50 | FMVTemplateBaseTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | — |
| 51 | FMVTemplateBaseToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | — |
| 52 | FMVTemplateBaseUseToleranceForCompliance | USE_TOLERANCE_FOR_COMPLIANCE | — | — |

### [[vrm_fmv_templates_tl|VRM_FMV_TEMPLATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateTranslationCreatedBy | CREATED_BY | — | — |
| 2 | FMVTemplateTranslationCreationDate | CREATION_DATE | — | — |
| 3 | FMVTemplateTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | FMVTemplateTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | FMVTemplateTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | FMVTemplateTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | FMVTemplateTranslationName | NAME | — | ✅ |
| 8 | FMVTemplateTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | FMVTemplateTranslationSourceLang | SOURCE_LANG | — | — |
| 10 | Language | LANGUAGE | 🔑 | ✅ |
| 11 | TemplateId | TEMPLATE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
