---
id: DOC-OTHER-PVO-PreSalaryPVO
doc_type: system-doc
title: "PreSalaryPVO — PVO Cross-Module"
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
  - PreSalaryPVO
  - presalarypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PreSalaryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pre Salary. Acessa as tabelas: CMP_PRE_SALARY_V, PER_ALL_ASSIGNMENTS_M.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PreSalaryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 2 | 1 | 19 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_pre_salary_v|CMP_PRE_SALARY_V]] — 38 atributos (1 PKs, 19 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos

---

## ⚙️ Atributos

### [[cmp_pre_salary_v|CMP_PRE_SALARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 2 | GeographyId | GEOGRAPHY_ID | — | — |
| 3 | GeographyTypeId | GEOGRAPHY_TYPE_ID | — | — |
| 4 | GradeRateMinimumLimit | GRADE_RATE_MINIMUM_LIMIT | — | — |
| 5 | JobId | JOB_ID | — | — |
| 6 | PayrollAnnualFactor | PAYROLL_ANNUAL_FACTOR | — | ✅ |
| 7 | PayrollFrequencyCode | PAYROLL_FREQUENCY_CODE | — | ✅ |
| 8 | PreSalaryPEOAnnualizationFactor | ANNUALIZATION_FACTOR | — | ✅ |
| 9 | PreSalaryPEOAnnualizedFulltimeSalary | ANNUALIZED_FULLTIME_SALARY | — | ✅ |
| 10 | PreSalaryPEOAnnualizedSalary | ANNUALIZED_SALARY | — | ✅ |
| 11 | PreSalaryPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 12 | PreSalaryPEOComparatio | COMPARATIO | — | — |
| 13 | PreSalaryPEODateFrom | DATE_FROM | — | — |
| 14 | PreSalaryPEODateTo | DATE_TO | — | — |
| 15 | PreSalaryPEOElementTypeId | ELEMENT_TYPE_ID | — | — |
| 16 | PreSalaryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | PreSalaryPEOMaximum | MAXIMUM | — | ✅ |
| 18 | PreSalaryPEOMidValue | MID_VALUE | — | ✅ |
| 19 | PreSalaryPEOMinimum | MINIMUM | — | ✅ |
| 20 | PreSalaryPEOPercentile | PERCENTILE | — | — |
| 21 | PreSalaryPEOPrevAmt | PREV_AMT | — | ✅ |
| 22 | PreSalaryPEOPrevCurrCode | PREV_CURR_CODE | — | ✅ |
| 23 | PreSalaryPEOPrevSalaryBasis | PREV_SALARY_BASIS | — | — |
| 24 | PreSalaryPEOQuartile | QUARTILE | — | — |
| 25 | PreSalaryPEOQuintile | QUINTILE | — | — |
| 26 | PreSalaryPEORangeDiffFactor | RANGE_DIFF_FACTOR | — | ✅ |
| 27 | PreSalaryPEORateFrequency | RATE_FREQUENCY | — | ✅ |
| 28 | PreSalaryPEORateId | RATE_ID | — | — |
| 29 | PreSalaryPEORateName | RATE_NAME | — | ✅ |
| 30 | PreSalaryPEORateObjectType | RATE_OBJECT_TYPE | — | ✅ |
| 31 | PreSalaryPEORateType | RATE_TYPE | — | ✅ |
| 32 | PreSalaryPEORateValue | RATE_VALUE | — | ✅ |
| 33 | PreSalaryPEOSalaryAmount | SALARY_AMOUNT | — | — |
| 34 | PreSalaryPEOSalaryChangeAmt | SALARY_CHANGE_AMT | — | ✅ |
| 35 | PreSalaryPEOSalaryChangePer | SALARY_CHANGE_PER | — | ✅ |
| 36 | SalaryId | SALARY_ID | 🔑 | ✅ |
| 37 | WorkAtHome | WORK_AT_HOME | — | — |
| 38 | ZoneGradeRateId | ZONE_GRADE_RATE_ID | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | AssignmentPEOPersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
