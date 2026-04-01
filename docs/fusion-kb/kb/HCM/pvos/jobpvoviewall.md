---
id: DOC-HCM-PVO-JobPVOViewAll
doc_type: system-doc
title: "JobPVOViewAll — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - JobPVOViewAll
  - jobpvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobPVOViewAll

## 📌 Visão Geral

Visão completa (sem filtro de segurança) do cadastro de cargos. Utilizado em relatórios analíticos e auditoria da estrutura de cargos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.JobAM.JobPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 87 | 4 | 3 | 16 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 5 atributos (1 BICC)
- [[per_jobs_f|PER_JOBS_F]] — 40 atributos (3 PKs, 7 BICC)
- [[per_jobs_f_tl|PER_JOBS_F_TL]] — 24 atributos (7 BICC)
- [[per_job_evaluations|PER_JOB_EVALUATIONS]] — 18 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | — |
| 2 | SetIdSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 4 | SetIdSetPEOSetId | SET_ID | — | — |
| 5 | SetIdSetPEOSetName | SET_NAME | — | — |

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | JobId | JOB_ID | 🔑 | ✅ |
| 4 | JobPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | JobPEOActiveStatus | ACTIVE_STATUS | — | — |
| 6 | JobPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 7 | JobPEOApprovalAuthority | APPROVAL_AUTHORITY | — | — |
| 8 | JobPEOBenchmarkJobEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | JobPEOBenchmarkJobEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | JobPEOBenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | — |
| 11 | JobPEOBenchmarkJobId | BENCHMARK_JOB_ID | — | — |
| 12 | JobPEOBenchmarkJobJobCode | JOB_CODE | — | — |
| 13 | JobPEOBenchmarkJobJobId | JOB_ID | — | — |
| 14 | JobPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 15 | JobPEOCategoryCode | CATEGORY_CODE | — | — |
| 16 | JobPEOCreatedBy | CREATED_BY | — | — |
| 17 | JobPEOCreationDate | CREATION_DATE | — | — |
| 18 | JobPEOFullPartTime | FULL_PART_TIME | — | — |
| 19 | JobPEOGradeLadderId | GRADE_LADDER_ID | — | — |
| 20 | JobPEOJobCode | JOB_CODE | — | ✅ |
| 21 | JobPEOJobFamilyId | JOB_FAMILY_ID | — | — |
| 22 | JobPEOJobFunctionCode | JOB_FUNCTION_CODE | — | — |
| 23 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | JobPEOManagerLevel | MANAGER_LEVEL | — | — |
| 27 | JobPEOMedCheckupReq | MED_CHECKUP_REQ | — | — |
| 28 | JobPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | JobPEOProgressionJobEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 30 | JobPEOProgressionJobEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 31 | JobPEOProgressionJobId | PROGRESSION_JOB_ID | — | — |
| 32 | JobPEOProgressionJobJobCode | JOB_CODE | — | — |
| 33 | JobPEOProgressionJobJobId | JOB_ID | — | — |
| 34 | JobPEORegularTemporary | REGULAR_TEMPORARY | — | — |
| 35 | JobPEORequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | — |
| 36 | JobPEOSchedulingGroup | SCHEDULING_GROUP | — | — |
| 37 | JobPEOSetId | SET_ID | — | — |
| 38 | JobPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 39 | JobPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |
| 40 | JobPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |

### [[per_jobs_f_tl|PER_JOBS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenchmarkJobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | BenchmarkJobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | BenchmarkJobTranslationPEOJobId | JOB_ID | — | — |
| 4 | BenchmarkJobTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | BenchmarkJobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BenchmarkJobTranslationPEOName | NAME | — | — |
| 7 | JobTranslationPEOCreatedBy | CREATED_BY | — | — |
| 8 | JobTranslationPEOCreationDate | CREATION_DATE | — | — |
| 9 | JobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | JobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | JobTranslationPEOJobId | JOB_ID | — | — |
| 12 | JobTranslationPEOLanguage | LANGUAGE | — | — |
| 13 | JobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | JobTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | JobTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | JobTranslationPEOName | NAME | — | ✅ |
| 17 | JobTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | JobTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 19 | ProgressionJobTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 20 | ProgressionJobTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 21 | ProgressionJobTranslationPEOJobId | JOB_ID | — | — |
| 22 | ProgressionJobTranslationPEOLanguage | LANGUAGE | — | — |
| 23 | ProgressionJobTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ProgressionJobTranslationPEOName | NAME | — | — |

### [[per_job_evaluations|PER_JOB_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobEvaluationPEOAccountability | ACCOUNTABILITY | — | — |
| 2 | JobEvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | JobEvaluationPEOCreatedBy | CREATED_BY | — | — |
| 4 | JobEvaluationPEOCreationDate | CREATION_DATE | — | — |
| 5 | JobEvaluationPEODateEvaluated | DATE_EVALUATED | — | — |
| 6 | JobEvaluationPEOEvaluationSystem | EVALUATION_SYSTEM | — | — |
| 7 | JobEvaluationPEOJobEvaluationId | JOB_EVALUATION_ID | — | — |
| 8 | JobEvaluationPEOJobId | JOB_ID | — | — |
| 9 | JobEvaluationPEOKnowhow | KNOWHOW | — | — |
| 10 | JobEvaluationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | JobEvaluationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | JobEvaluationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | JobEvaluationPEOMeasuredIn | MEASURED_IN | — | — |
| 14 | JobEvaluationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | JobEvaluationPEOOverallScore | OVERALL_SCORE | — | — |
| 16 | JobEvaluationPEOPositionId | POSITION_ID | — | — |
| 17 | JobEvaluationPEOProblemSolving | PROBLEM_SOLVING | — | — |
| 18 | JobEvaluationPEOWorkingConditions | WORKING_CONDITIONS | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
