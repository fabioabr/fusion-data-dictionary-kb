---
id: DOC-OTHER-PVO-SalaryPVO
doc_type: system-doc
title: "SalaryPVO — PVO Cross-Module"
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
  - SalaryPVO
  - salarypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Salary. Acessa as tabelas: CMP_SALARY, CMP_SALARY_BASES, CMP_SALARY_BASES_TL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.SalaryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 89 | 5 | 3 | 52 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary|CMP_SALARY]] — 29 atributos (1 PKs, 19 BICC)
- [[cmp_salary_bases|CMP_SALARY_BASES]] — 30 atributos (23 BICC)
- [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]] — 11 atributos (3 BICC)
- [[pay_input_values_tl|PAY_INPUT_VALUES_TL]] — 10 atributos (3 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[cmp_salary|CMP_SALARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryEffectiveEndDate | DATE_TO | — | — |
| 2 | SalaryEffectiveStartDate | DATE_FROM | — | — |
| 3 | SalaryId | SALARY_ID | 🔑 | ✅ |
| 4 | SalaryPEOActionId | ACTION_ID | — | — |
| 5 | SalaryPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 6 | SalaryPEOActionReasonId | ACTION_REASON_ID | — | — |
| 7 | SalaryPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 8 | SalaryPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | SalaryPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 10 | SalaryPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | SalaryPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | SalaryPEODateFrom | DATE_FROM | — | ✅ |
| 13 | SalaryPEODateTo | DATE_TO | — | ✅ |
| 14 | SalaryPEOElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 15 | SalaryPEOGeographyId | GEOGRAPHY_ID | — | ✅ |
| 16 | SalaryPEOGeographyTypeId | GEOGRAPHY_TYPE_ID | — | ✅ |
| 17 | SalaryPEOGradeRateMinimumLimit | GRADE_RATE_MINIMUM_LIMIT | — | — |
| 18 | SalaryPEOJobId | JOB_ID | — | — |
| 19 | SalaryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | SalaryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | SalaryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | SalaryPEOMultipleComponents | MULTIPLE_COMPONENTS | — | ✅ |
| 23 | SalaryPEONextSalReviewDate | NEXT_SAL_REVIEW_DATE | — | ✅ |
| 24 | SalaryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | SalaryPEOSalaryAmount | SALARY_AMOUNT | — | ✅ |
| 26 | SalaryPEOSalaryApproved | SALARY_APPROVED | — | ✅ |
| 27 | SalaryPEOSalaryBasisId | SALARY_BASIS_ID | — | ✅ |
| 28 | SalaryPEOWorkAtHome | WORK_AT_HOME | — | ✅ |
| 29 | SalaryPEOZoneGradeRateId | ZONE_GRADE_RATE_ID | — | — |

### [[cmp_salary_bases|CMP_SALARY_BASES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasesPEOAmountDecimalPrecision | AMOUNT_DECIMAL_PRECISION | — | ✅ |
| 2 | SalaryBasesPEOAmountRoundingCode | AMOUNT_ROUNDING_CODE | — | ✅ |
| 3 | SalaryBasesPEOAnnualRoundingCode | ANNUAL_ROUNDING_CODE | — | ✅ |
| 4 | SalaryBasesPEOAnnualizedHours | ANNUALIZED_HOURS | — | ✅ |
| 5 | SalaryBasesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | SalaryBasesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | SalaryBasesPEOCalculationMode | CALCULATION_MODE | — | ✅ |
| 8 | SalaryBasesPEOCode | CODE | — | ✅ |
| 9 | SalaryBasesPEOComponentUsage | COMPONENT_USAGE | — | ✅ |
| 10 | SalaryBasesPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | SalaryBasesPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | SalaryBasesPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 13 | SalaryBasesPEOGradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | ✅ |
| 14 | SalaryBasesPEOGradeRateBasisCode | GRADE_RATE_BASIS_CODE | — | ✅ |
| 15 | SalaryBasesPEOGradeRateId | GRADE_RATE_ID | — | ✅ |
| 16 | SalaryBasesPEOInputValueId | INPUT_VALUE_ID | — | — |
| 17 | SalaryBasesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | SalaryBasesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | SalaryBasesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | SalaryBasesPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 21 | SalaryBasesPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 22 | SalaryBasesPEOName | NAME | — | — |
| 23 | SalaryBasesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | SalaryBasesPEORangeErrorWarning | RANGE_ERROR_WARNING | — | — |
| 25 | SalaryBasesPEORangeRoundingCode | RANGE_ROUNDING_CODE | — | ✅ |
| 26 | SalaryBasesPEOSalaryAnnualizationFactor | SALARY_ANNUALIZATION_FACTOR | — | ✅ |
| 27 | SalaryBasesPEOSalaryBasisCode | SALARY_BASIS_CODE | — | ✅ |
| 28 | SalaryBasesPEOSalaryBasisId | SALARY_BASIS_ID | — | ✅ |
| 29 | SalaryBasesPEOSalaryBasisType | SALARY_BASIS_TYPE | — | ✅ |
| 30 | SalaryBasesPEOStatus | STATUS | — | ✅ |

### [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasesTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | SalaryBasesTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | SalaryBasesTLPEODescription | DESCRIPTION | — | — |
| 4 | SalaryBasesTLPEOLanguage | LANGUAGE | — | ✅ |
| 5 | SalaryBasesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SalaryBasesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SalaryBasesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SalaryBasesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SalaryBasesTLPEOSalaryBasisId | SALARY_BASIS_ID | — | — |
| 10 | SalaryBasesTLPEOSalaryBasisName | SALARY_BASIS_NAME | — | ✅ |
| 11 | SalaryBasesTLPEOSourceLang | SOURCE_LANG | — | — |

### [[pay_input_values_tl|PAY_INPUT_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputValueTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | InputValueTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | InputValueTranslationPEOInputValueId | INPUT_VALUE_ID | — | — |
| 4 | InputValueTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | InputValueTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InputValueTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InputValueTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InputValueTranslationPEOName | NAME | — | ✅ |
| 9 | InputValueTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InputValueTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 3 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 5 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 6 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | AssignmentPEOJobId | JOB_ID | — | — |
| 8 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 9 | AssignmentPEOPersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
