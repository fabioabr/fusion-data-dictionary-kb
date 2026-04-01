---
id: DOC-OTHER-PVO-FMVProfilePVO
doc_type: system-doc
title: "FMVProfilePVO — PVO Cross-Module"
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
  - FMVProfilePVO
  - fmvprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FMVProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de FMVProfile. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, VRM_FMV_TEMPLATES_B (+3).

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.FMVProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 6 | 1 | 29 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 21 atributos (10 BICC)
- [[vrm_fmv_templates_tl|VRM_FMV_TEMPLATES_TL]] — 11 atributos (3 BICC)
- [[vrm_fmv_templ_assignments|VRM_FMV_TEMPL_ASSIGNMENTS]] — 21 atributos (1 PKs, 10 BICC)
- [[vrm_price_eff_periods_vl|VRM_PRICE_EFF_PERIODS_VL]] — 22 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBaseCreatedBy | DISPLAY_NAME | — | ✅ |
| 2 | FMVTemplateBaseLastUpdatedBy | DISPLAY_NAME | — | ✅ |
| 3 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 6 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBaseCreatedBy1 | CREATED_BY | — | ✅ |
| 2 | FMVTemplateBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | FMVTemplateBaseDataSelectionTimeSpan | DATA_SELECTION_TIME_SPAN | — | ✅ |
| 4 | FMVTemplateBaseDimensionAssignmentId | DIMENSION_ASSIGNMENT_ID | — | — |
| 5 | FMVTemplateBaseElementType | ELEMENT_TYPE | — | — |
| 6 | FMVTemplateBaseFmvPriceType | FMV_PRICE_TYPE | — | — |
| 7 | FMVTemplateBaseFmvRepresentationType | FMV_REPRESENTATION_TYPE | — | ✅ |
| 8 | FMVTemplateBaseFmvToleranceCode | FMV_TOLERANCE_CODE | — | — |
| 9 | FMVTemplateBaseInUse | IN_USE | — | ✅ |
| 10 | FMVTemplateBaseIncludeCurrentPeriods | INCLUDE_CURRENT_PERIODS | — | ✅ |
| 11 | FMVTemplateBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | FMVTemplateBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | FMVTemplateBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 14 | FMVTemplateBaseMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 15 | FMVTemplateBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | FMVTemplateBaseStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 17 | FMVTemplateBaseTemplateId | TEMPLATE_ID | — | — |
| 18 | FMVTemplateBaseTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | — |
| 19 | FMVTemplateBaseTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | — |
| 20 | FMVTemplateBaseToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | — |
| 21 | FMVTemplateBaseUseToleranceForCompliance | USE_TOLERANCE_FOR_COMPLIANCE | — | ✅ |

### [[vrm_fmv_templates_tl|VRM_FMV_TEMPLATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateTranslationCreatedBy | CREATED_BY | — | — |
| 2 | FMVTemplateTranslationCreationDate | CREATION_DATE | — | — |
| 3 | FMVTemplateTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | FMVTemplateTranslationLanguage | LANGUAGE | — | — |
| 5 | FMVTemplateTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | FMVTemplateTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | FMVTemplateTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | FMVTemplateTranslationName | NAME | — | ✅ |
| 9 | FMVTemplateTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | FMVTemplateTranslationSourceLang | SOURCE_LANG | — | — |
| 11 | FMVTemplateTranslationTemplateId | TEMPLATE_ID | — | — |

### [[vrm_fmv_templ_assignments|VRM_FMV_TEMPL_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateAssignmentsCreatedBy | CREATED_BY | — | — |
| 2 | FMVTemplateAssignmentsCreationDate | CREATION_DATE | — | — |
| 3 | FMVTemplateAssignmentsDataSelectionTimeSpan | DATA_SELECTION_TIME_SPAN | — | — |
| 4 | FMVTemplateAssignmentsElementType | ELEMENT_TYPE | — | ✅ |
| 5 | FMVTemplateAssignmentsFmvToleranceCode | FMV_TOLERANCE_CODE | — | ✅ |
| 6 | FMVTemplateAssignmentsFromPeriodId | FROM_PERIOD_ID | — | — |
| 7 | FMVTemplateAssignmentsInUse | IN_USE | — | ✅ |
| 8 | FMVTemplateAssignmentsInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 9 | FMVTemplateAssignmentsItemType | ITEM_TYPE | — | ✅ |
| 10 | FMVTemplateAssignmentsItemTypeId | ITEM_TYPE_ID | — | — |
| 11 | FMVTemplateAssignmentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | FMVTemplateAssignmentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | FMVTemplateAssignmentsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | FMVTemplateAssignmentsMinimumLineCount | MINIMUM_LINE_COUNT | — | ✅ |
| 15 | FMVTemplateAssignmentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | FMVTemplateAssignmentsTemplateId | TEMPLATE_ID | — | — |
| 17 | FMVTemplateAssignmentsToPeriodId | TO_PERIOD_ID | — | — |
| 18 | FMVTemplateAssignmentsTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | ✅ |
| 19 | FMVTemplateAssignmentsTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | ✅ |
| 20 | FMVTemplateAssignmentsToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 21 | TemplateAssignmentId | TEMPLATE_ASSIGNMENT_ID | 🔑 | ✅ |

### [[vrm_price_eff_periods_vl|VRM_PRICE_EFF_PERIODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FromEffectivePeriodVLCreatedBy | CREATED_BY | — | — |
| 2 | FromEffectivePeriodVLCreationDate | CREATION_DATE | — | — |
| 3 | FromEffectivePeriodVLEndDate | END_DATE | — | — |
| 4 | FromEffectivePeriodVLInUse | IN_USE | — | — |
| 5 | FromEffectivePeriodVLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | FromEffectivePeriodVLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | FromEffectivePeriodVLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | FromEffectivePeriodVLName | NAME | — | ✅ |
| 9 | FromEffectivePeriodVLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | FromEffectivePeriodVLPriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |
| 11 | FromEffectivePeriodVLStartDate | START_DATE | — | — |
| 12 | ToEffectivePeriodVLCreatedBy | CREATED_BY | — | — |
| 13 | ToEffectivePeriodVLCreationDate | CREATION_DATE | — | — |
| 14 | ToEffectivePeriodVLEndDate | END_DATE | — | — |
| 15 | ToEffectivePeriodVLInUse | IN_USE | — | — |
| 16 | ToEffectivePeriodVLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ToEffectivePeriodVLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ToEffectivePeriodVLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ToEffectivePeriodVLName | NAME | — | ✅ |
| 20 | ToEffectivePeriodVLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ToEffectivePeriodVLPriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |
| 22 | ToEffectivePeriodVLStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
