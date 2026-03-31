---
id: DOC-OTHER-PVO-SalaryHistoryPVO
doc_type: system-doc
title: "SalaryHistoryPVO — PVO Cross-Module"
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
  - SalaryHistoryPVO
  - salaryhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Salary History. Acessa as tabelas: CMP_SALARY_HISTORY_V, PER_ALL_ASSIGNMENTS_M.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.SalaryHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 2 | 6 | 45 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary_history_v|CMP_SALARY_HISTORY_V]] — 71 atributos (1 PKs, 40 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 9 atributos (5 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[cmp_salary_history_v|CMP_SALARY_HISTORY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | — | — |
| 2 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | ActionReasonId | ACTION_REASON_ID | — | — |
| 4 | AnnualizedFulltimeSalary | ANNUALIZED_FULLTIME_SALARY | — | ✅ |
| 5 | AnnualizedHours | ANNUALIZED_HOURS | — | ✅ |
| 6 | AnnualizedSalary | ANNUALIZED_SALARY | — | ✅ |
| 7 | AssignmentId | ASSIGNMENT_ID | — | — |
| 8 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | BusinessUnitId1 | BUSINESS_UNIT_ID | — | — |
| 10 | CalculationMode | CALCULATION_MODE | — | ✅ |
| 11 | Code | CODE | — | ✅ |
| 12 | ComponentUsage | COMPONENT_USAGE | — | ✅ |
| 13 | CreatedBy | CREATED_BY | — | ✅ |
| 14 | CreationDate | CREATION_DATE | — | ✅ |
| 15 | DateFrom | DATE_FROM | — | ✅ |
| 16 | DateTo | DATE_TO | — | ✅ |
| 17 | Description | DESCRIPTION | — | — |
| 18 | ElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 19 | ElementTypeId | ELEMENT_TYPE_ID | — | — |
| 20 | ForcedRanking | FORCED_RANKING | — | — |
| 21 | GeographyId | GEOGRAPHY_ID | — | ✅ |
| 22 | GeographyTypeId | GEOGRAPHY_TYPE_ID | — | ✅ |
| 23 | GradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | ✅ |
| 24 | GradeRateId | GRADE_RATE_ID | — | — |
| 25 | GradeRateMinimumLimit | GRADE_RATE_MINIMUM_LIMIT | — | — |
| 26 | HistoryDate | HISTORY_DATE | — | — |
| 27 | InputValueId | INPUT_VALUE_ID | — | — |
| 28 | InputValueLanguage | INPUT_VALUE_LANGUAGE | — | — |
| 29 | InputValueName | INPUT_VALUE_NAME | — | ✅ |
| 30 | JobId1 | JOB_ID | — | — |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 35 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 36 | MultipleComponents | MULTIPLE_COMPONENTS | — | ✅ |
| 37 | NextPerfReviewDate | NEXT_PERF_REVIEW_DATE | — | — |
| 38 | NextSalReviewDate | NEXT_SAL_REVIEW_DATE | — | ✅ |
| 39 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | PayrollAnnualFactor | PAYROLL_ANNUAL_FACTOR | — | ✅ |
| 41 | PayrollFrequencyCode | PAYROLL_FREQUENCY_CODE | — | ✅ |
| 42 | PerformanceRating | PERFORMANCE_RATING | — | — |
| 43 | PerformanceReviewId | PERFORMANCE_REVIEW_ID | — | — |
| 44 | RangeErrorWarning | RANGE_ERROR_WARNING | — | — |
| 45 | ReviewDate | REVIEW_DATE | — | — |
| 46 | SalaryAmount | SALARY_AMOUNT | — | ✅ |
| 47 | SalaryAnnualizationFactor | SALARY_ANNUALIZATION_FACTOR | — | ✅ |
| 48 | SalaryApproved | SALARY_APPROVED | — | ✅ |
| 49 | SalaryBasesName | SALARY_BASES_NAME | — | — |
| 50 | SalaryBasisCode | SALARY_BASIS_CODE | — | ✅ |
| 51 | SalaryBasisCreatedBy | SALARY_BASIS_CREATED_BY | — | ✅ |
| 52 | SalaryBasisCreationDate | SALARY_BASIS_CREATION_DATE | — | ✅ |
| 53 | SalaryBasisId | SALARY_BASIS_ID | — | ✅ |
| 54 | SalaryBasisLastUpdateDate | SALARY_BASIS_LAST_UPDATE_DATE | — | ✅ |
| 55 | SalaryBasisLastUpdatedBy | SALARY_BASIS_LAST_UPDATED_BY | — | ✅ |
| 56 | SalaryBasisName | SALARY_BASIS_NAME | — | ✅ |
| 57 | SalaryId | SALARY_ID | 🔑 | ✅ |
| 58 | SalaryReasonCode | SALARY_REASON_CODE | — | — |
| 59 | SbAmountDecimalPrecision | AMOUNT_DECIMAL_PRECISION | — | ✅ |
| 60 | SbAmountRoundingCode | AMOUNT_ROUNDING_CODE | — | ✅ |
| 61 | SbAnnualRoundingCode | ANNUAL_ROUNDING_CODE | — | ✅ |
| 62 | SbBusinessGroupId | SB_BUSINESS_GROUP_ID | — | — |
| 63 | SbLanguage | SB_LANGUAGE | — | — |
| 64 | SbRangeRoundingCode | RANGE_ROUNDING_CODE | — | ✅ |
| 65 | SbSalaryBasisId | SB_SALARY_BASIS_ID | — | — |
| 66 | SbSalaryBasisType | SALARY_BASIS_TYPE | — | ✅ |
| 67 | SbSouceLang | SB_SOUCE_LANG | — | — |
| 68 | SbStatus | STATUS | — | ✅ |
| 69 | SourceLang | SOURCE_LANG | — | — |
| 70 | WorkAtHome | WORK_AT_HOME | — | ✅ |
| 71 | ZoneGradeRateId | ZONE_GRADE_RATE_ID | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId1 | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | 🔑 | ✅ |
| 5 | EffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | JobId | JOB_ID | — | — |
| 8 | LocationId | LOCATION_ID | — | — |
| 9 | PersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
