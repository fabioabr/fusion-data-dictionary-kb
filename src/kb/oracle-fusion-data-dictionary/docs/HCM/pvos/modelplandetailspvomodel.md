---
id: DOC-HCM-PVO-ModelPlanDetailsPVOModel
doc_type: system-doc
title: "ModelPlanDetailsPVOModel — PVO Human Capital Management"
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
  - ModelPlanDetailsPVOModel
  - modelplandetailspvomodel
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ModelPlanDetailsPVOModel

## 📌 Visão Geral

Disponibiliza detalhes de planos de modelagem de workforce na visão do modelo, com datas de término aceitas. Utilizado em simulações what-if de planejamento organizacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.WorkforceModelingAM.ModelPlanDetailsPVOModel`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 2 | 1 | 80 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[hmo_model_plans_b|HMO_MODEL_PLANS_B]] — 20 atributos (2 BICC)
- [[hmo_model_plan_details|HMO_MODEL_PLAN_DETAILS]] — 107 atributos (1 PKs, 78 BICC)

---

## ⚙️ Atributos

### [[hmo_model_plans_b|HMO_MODEL_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ModelPlanPEOAccessToTopManager | ACCESS_TO_TOP_MANAGER | — | — |
| 2 | ModelPlanPEOActionId | ACTION_ID | — | — |
| 3 | ModelPlanPEOActionReasonId | ACTION_REASON_ID | — | — |
| 4 | ModelPlanPEOAuthorPersonId | AUTHOR_PERSON_ID | — | — |
| 5 | ModelPlanPEOCreatedBy | CREATED_BY | — | — |
| 6 | ModelPlanPEOCreationDate | CREATION_DATE | — | — |
| 7 | ModelPlanPEOEffectiveDate | EFFECTIVE_DATE | — | — |
| 8 | ModelPlanPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | ModelPlanPEOLastSyncDate | LAST_SYNC_DATE | — | — |
| 10 | ModelPlanPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ModelPlanPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ModelPlanPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ModelPlanPEOModelLoaderBatchId | MODEL_LOADER_BATCH_ID | — | — |
| 14 | ModelPlanPEOModelPlanId | MODEL_PLAN_ID | — | — |
| 15 | ModelPlanPEOModelPlanStatus | MODEL_PLAN_STATUS | — | — |
| 16 | ModelPlanPEOModelPlanType | MODEL_PLAN_TYPE | — | ✅ |
| 17 | ModelPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ModelPlanPEOTopManagerAssignmentId | TOP_MANAGER_ASSIGNMENT_ID | — | — |
| 19 | ModelPlanPEOTopManagerId | TOP_MANAGER_ID | — | — |
| 20 | ModelPlanPEOTopManagerType | TOP_MANAGER_TYPE | — | — |

### [[hmo_model_plan_details|HMO_MODEL_PLAN_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptedTerminationDate | ACCEPTED_TERMINATION_DATE | — | ✅ |
| 2 | ActionId | ACTION_ID | — | — |
| 3 | ActionReasonId | ACTION_REASON_ID | — | — |
| 4 | ActualTerminationDate | ACTUAL_TERMINATION_DATE | — | — |
| 5 | AsgFteLastUpdateDate | ASG_FTE_LAST_UPDATE_DATE | — | ✅ |
| 6 | AsgLastUpdateDate | ASG_LAST_UPDATE_DATE | — | ✅ |
| 7 | AsgSupLastUpdateDate | ASG_SUP_LAST_UPDATE_DATE | — | ✅ |
| 8 | AsgSupManagerAssignmentId | ASG_SUP_MANAGER_ASSIGNMENT_ID | — | ✅ |
| 9 | AsgSupManagerId | ASG_SUP_MANAGER_ID | — | ✅ |
| 10 | AsgSupervisorId | ASG_SUPERVISOR_ID | — | — |
| 11 | AssignGradeStepId | ASSIGN_GRADE_STEP_ID | — | — |
| 12 | AssignWorkMeasureId | ASSIGN_WORK_MEASURE_ID | — | — |
| 13 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 14 | AssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 15 | AssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 16 | AssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 17 | BargainingUnitCode | BARGAINING_UNIT_CODE | — | ✅ |
| 18 | BusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 19 | CmpLastUpdateDate | CMP_LAST_UPDATE_DATE | — | ✅ |
| 20 | CmpSalaryId | CMP_SALARY_ID | — | ✅ |
| 21 | CollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 22 | Comments | COMMENTS | — | ✅ |
| 23 | CreatedBy | CREATED_BY | — | ✅ |
| 24 | CreationDate | CREATION_DATE | — | ✅ |
| 25 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 26 | EmployeeCategory | EMPLOYEE_CATEGORY | — | ✅ |
| 27 | EmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 28 | EnterpriseId | ENTERPRISE_ID | — | — |
| 29 | Frequency | FREQUENCY | — | ✅ |
| 30 | FullPartTime | FULL_PART_TIME | — | ✅ |
| 31 | GradeId | GRADE_ID | — | ✅ |
| 32 | GradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 33 | GradeStepId | GRADE_STEP_ID | — | ✅ |
| 34 | GradeStepLastUpdateDate | GRADE_STEP_LAST_UPDATE_DATE | — | ✅ |
| 35 | HiringStatus | HIRING_STATUS | — | ✅ |
| 36 | HourlySalariedCode | HOURLY_SALARIED_CODE | — | ✅ |
| 37 | IncludedInBench | INCLUDED_IN_BENCH | — | — |
| 38 | InternalBuilding | INTERNAL_BUILDING | — | ✅ |
| 39 | InternalFloor | INTERNAL_FLOOR | — | ✅ |
| 40 | InternalMailstop | INTERNAL_MAILSTOP | — | ✅ |
| 41 | InternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | ✅ |
| 42 | JobId | JOB_ID | — | ✅ |
| 43 | LabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | ✅ |
| 44 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 47 | LatestChange | LATEST_CHANGE | — | ✅ |
| 48 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 49 | LocationId | LOCATION_ID | — | ✅ |
| 50 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 51 | ManagerFlag | MANAGER_FLAG | — | ✅ |
| 52 | ManagerId | MANAGER_ID | — | — |
| 53 | ModelPlanAsgType | MODEL_PLAN_ASG_TYPE | — | — |
| 54 | ModelPlanDetailId | MODEL_PLAN_DETAIL_ID | 🔑 | ✅ |
| 55 | ModelPlanDetailType | MODEL_PLAN_DETAIL_TYPE | — | — |
| 56 | ModelPlanId | MODEL_PLAN_ID | — | ✅ |
| 57 | NormalHours | NORMAL_HOURS | — | ✅ |
| 58 | NotifiedTerminationDate | NOTIFIED_TERMINATION_DATE | — | ✅ |
| 59 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | OpenFte | OPEN_FTE | — | ✅ |
| 61 | OpenHeadCount | OPEN_HEAD_COUNT | — | ✅ |
| 62 | OrgAnnualizedSalaryAmount | ANNUALIZED_SALARY_AMOUNT | — | — |
| 63 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 64 | PeopleGroupId | PEOPLE_GROUP_ID | — | ✅ |
| 65 | PermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | ✅ |
| 66 | PersonId | PERSON_ID | — | ✅ |
| 67 | PosEvalAccountability | POS_EVAL_ACCOUNTABILITY | — | ✅ |
| 68 | PosEvalDateEvaluated | POS_EVAL_DATE_EVALUATED | — | ✅ |
| 69 | PosEvalEvaluationId | POS_EVAL_EVALUATION_ID | — | — |
| 70 | PosEvalEvaluationSystem | POS_EVAL_EVALUATION_SYSTEM | — | ✅ |
| 71 | PosEvalKnowhow | POS_EVAL_KNOWHOW | — | ✅ |
| 72 | PosEvalLastUpdateDate | POS_EVAL_LAST_UPDATE_DATE | — | ✅ |
| 73 | PosEvalMeasuredIn | POS_EVAL_MEASURED_IN | — | ✅ |
| 74 | PosEvalOverallScore | POS_EVAL_OVERALL_SCORE | — | — |
| 75 | PosEvalProblemSolving | POS_EVAL_PROBLEM_SOLVING | — | ✅ |
| 76 | PositionCode | POSITION_CODE | — | ✅ |
| 77 | PositionId | POSITION_ID | — | ✅ |
| 78 | PositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 79 | PositionType | POSITION_TYPE | — | ✅ |
| 80 | ProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 81 | ProbationUnit | PROBATION_UNIT | — | ✅ |
| 82 | ProjectedTerminationDate | PROJECTED_TERMINATION_DATE | — | — |
| 83 | RehireAuthorizerPersonId | REHIRE_AUTHORIZER_PERSON_ID | — | — |
| 84 | RehireReason | REHIRE_REASON | — | ✅ |
| 85 | RehireRecommendation | REHIRE_RECOMMENDATION | — | ✅ |
| 86 | RequisitionInterfaceId | REQUISITION_INTERFACE_ID | — | ✅ |
| 87 | RequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 88 | RevokeUserAccess | REVOKE_USER_ACCESS | — | — |
| 89 | SalaryAmount | SALARY_AMOUNT | — | — |
| 90 | SalaryBasisId | SALARY_BASIS_ID | — | — |
| 91 | SalaryReviewDate | SALARY_REVIEW_DATE | — | ✅ |
| 92 | SeasonalEndDate | SEASONAL_END_DATE | — | ✅ |
| 93 | SeasonalFlag | SEASONAL_FLAG | — | ✅ |
| 94 | SeasonalStartDate | SEASONAL_START_DATE | — | ✅ |
| 95 | SecurityClearance | SECURITY_CLEARANCE | — | ✅ |
| 96 | TimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 97 | TimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 98 | UnionId | UNION_ID | — | — |
| 99 | VacancyHiredHeadcount | VACANCY_HIRED_HEADCOUNT | — | ✅ |
| 100 | VacancyJobSchedule | VACANCY_JOB_SCHEDULE | — | — |
| 101 | VacancyLastUpdateDate | VACANCY_LAST_UPDATE_DATE | — | ✅ |
| 102 | VacancyOpenHeadcount | VACANCY_OPEN_HEADCOUNT | — | ✅ |
| 103 | VacancyUnlimitedHire | VACANCY_UNLIMITED_HIRE | — | ✅ |
| 104 | ValidationError | VALIDATION_ERROR | — | ✅ |
| 105 | ValidationStatus | VALIDATION_STATUS | — | ✅ |
| 106 | WorkAtHome | WORK_AT_HOME | — | ✅ |
| 107 | WorkMeasureFte | WORK_MEASURE_FTE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
