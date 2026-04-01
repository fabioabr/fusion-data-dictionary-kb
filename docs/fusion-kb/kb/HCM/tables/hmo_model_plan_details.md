---
id: DOC-HCM-132
doc_type: system-doc
title: "HMO_MODEL_PLAN_DETAILS — Detalhes de Planos de Modelo Organizacional"
system: Oracle Fusion Cloud HCM
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
  - workforce-modeling
  - detalhes-modelo
  - headcount
  - hmo
aliases:
  - HMO_MODEL_PLAN_DETAILS
  - hmo_model_plan_details
  - hmo-model-plan-details
  - DOC-HCM-132
  - detalhes-de-planos-de-modelo-organizacional
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HMO_MODEL_PLAN_DETAILS

## 📌 Visão Geral

Armazena os **detalhes granulares** dos planos de modelo organizacional — as mudanças propostas em departamentos, posições, headcount e hierarquias.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhes de mudanças:** Propostas específicas de cada reorganização.
- **Impacto em posições:** Criação, eliminação ou transferência de posições.
- **Headcount planejado:** Projeção de quantidade de colaboradores.
- **Análise de impacto:** Avaliação de efeitos da reorganização.
- **Simulação:** Cenários hipotéticos antes da efetivação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MODEL_PLAN_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟡 80% |
| 2 | MODEL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de modelo | [[hmo_model_plans_b]] | 🟢 90% |
| 3 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento afetado | [[per_departments]] | 🟡 80% |
| 4 | POSITION_ID | NUMBER(18) | NULL | FK | Posição afetada | [[hr_all_positions_f]] | 🟡 75% |
| 5 | CHANGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de mudança (ADD, REMOVE, TRANSFER, MODIFY) | — | 🟡 75% |
| 6 | PLANNED_HEADCOUNT | NUMBER | NULL | Indicador | Headcount planejado | — | 🟡 70% |
| 7 | CURRENT_HEADCOUNT | NUMBER | NULL | Indicador | Headcount atual | — | 🟡 70% |
| 8 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade planejada | — | 🟡 75% |
| 9 | NOTES | VARCHAR2(2000) | NULL | Texto | Observações sobre a mudança | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hmo_model_plans_b]] — via `MODEL_PLAN_ID` (plano do modelo de headcount)
- [[per_departments]] — via `DEPARTMENT_ID` (departamento do detalhe do modelo)
- [[hr_all_positions_f]] — via `POSITION_ID` (posicao no detalhe do modelo de headcount)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Detalhes de um plano de modelo
```sql
SELECT d.DEPARTMENT_ID, d.POSITION_ID, d.CHANGE_TYPE,
       d.PLANNED_HEADCOUNT, d.CURRENT_HEADCOUNT
FROM   HMO_MODEL_PLAN_DETAILS d
WHERE  d.MODEL_PLAN_ID = :p_plan_id;
```

### Mudanças de headcount
```sql
SELECT d.DEPARTMENT_ID, d.CURRENT_HEADCOUNT, d.PLANNED_HEADCOUNT,
       (d.PLANNED_HEADCOUNT - d.CURRENT_HEADCOUNT) AS delta
FROM   HMO_MODEL_PLAN_DETAILS d
WHERE  d.MODEL_PLAN_ID = :p_plan_id
  AND  d.PLANNED_HEADCOUNT != d.CURRENT_HEADCOUNT;
```

---

## 🔒 Observações

- Cada plano de modelo pode ter múltiplos detalhes (um por mudança proposta).
- O `CHANGE_TYPE` classifica: ADD (nova posição), REMOVE (eliminar), TRANSFER, MODIFY.
- A diferença entre `PLANNED_HEADCOUNT` e `CURRENT_HEADCOUNT` indica o delta.
- Detalhes são referência para efetivação das mudanças após aprovação do plano.

---

## 🔗 PVOs Relacionados

### [[modelplandetailsfactpvo|ModelPlanDetailsFactPVO]] (HCM · BICC: 71/107)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_TERMINATION_DATE | AcceptedTerminationDate | — |
| ACTION_ID | ActionId | — |
| ACTION_REASON_ID | ActionReasonId | — |
| ACTUAL_TERMINATION_DATE | ActualTerminationDate | — |
| ANNUALIZED_SALARY_AMOUNT | OrgAnnualizedSalaryAmount | — |
| ASG_FTE_LAST_UPDATE_DATE | AsgFteLastUpdateDate | ✅ |
| ASG_LAST_UPDATE_DATE | AsgLastUpdateDate | ✅ |
| ASG_SUP_LAST_UPDATE_DATE | AsgSupLastUpdateDate | ✅ |
| ASG_SUP_MANAGER_ASSIGNMENT_ID | AsgSupManagerAssignmentId | ✅ |
| ASG_SUP_MANAGER_ID | AsgSupManagerId | ✅ |
| ASG_SUPERVISOR_ID | AsgSupervisorId | — |
| ASSIGN_GRADE_STEP_ID | AssignGradeStepId | — |
| ASSIGN_WORK_MEASURE_ID | AssignWorkMeasureId | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentName | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentStatusType | ✅ |
| ASSIGNMENT_TYPE | AssignmentType | ✅ |
| BARGAINING_UNIT_CODE | BargainingUnitCode | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| CMP_LAST_UPDATE_DATE | CmpLastUpdateDate | ✅ |
| CMP_SALARY_ID | CmpSalaryId | ✅ |
| COLLECTIVE_AGREEMENT_ID | CollectiveAgreementId | — |
| COMMENTS | Comments | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| EMPLOYEE_CATEGORY | EmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | EmploymentCategory | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| FREQUENCY | Frequency | ✅ |
| FULL_PART_TIME | FullPartTime | ✅ |
| GRADE_ID | GradeId | ✅ |
| GRADE_LADDER_PGM_ID | GradeLadderPgmId | — |
| GRADE_STEP_ID | GradeStepId | ✅ |
| GRADE_STEP_LAST_UPDATE_DATE | GradeStepLastUpdateDate | ✅ |
| HIRING_STATUS | HiringStatus | ✅ |
| HOURLY_SALARIED_CODE | HourlySalariedCode | ✅ |
| INCLUDED_IN_BENCH | IncludedInBench | — |
| INTERNAL_BUILDING | InternalBuilding | ✅ |
| INTERNAL_FLOOR | InternalFloor | ✅ |
| INTERNAL_MAILSTOP | InternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | InternalOfficeNumber | ✅ |
| JOB_ID | JobId | ✅ |
| LABOUR_UNION_MEMBER_FLAG | LabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_CHANGE | LatestChange | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | — |
| MANAGER_FLAG | ManagerFlag | ✅ |
| MANAGER_ID | ManagerId | — |
| MODEL_PLAN_ASG_TYPE | ModelPlanAsgType | — |
| MODEL_PLAN_DETAIL_ID | ModelPlanDetailId | ✅ |
| MODEL_PLAN_DETAIL_TYPE | ModelPlanDetailType | — |
| MODEL_PLAN_ID | ModelPlanId | ✅ |
| NORMAL_HOURS | NormalHours | ✅ |
| NOTIFIED_TERMINATION_DATE | NotifiedTerminationDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPEN_FTE | OpenFte | ✅ |
| OPEN_HEAD_COUNT | OpenHeadCount | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PEOPLE_GROUP_ID | PeopleGroupId | ✅ |
| PERMANENT_TEMPORARY_FLAG | PermanentTemporaryFlag | ✅ |
| PERSON_ID | PersonId | ✅ |
| POS_EVAL_ACCOUNTABILITY | PosEvalAccountability | ✅ |
| POS_EVAL_DATE_EVALUATED | PosEvalDateEvaluated | ✅ |
| POS_EVAL_EVALUATION_ID | PosEvalEvaluationId | — |
| POS_EVAL_EVALUATION_SYSTEM | PosEvalEvaluationSystem | ✅ |
| POS_EVAL_KNOWHOW | PosEvalKnowhow | ✅ |
| POS_EVAL_LAST_UPDATE_DATE | PosEvalLastUpdateDate | ✅ |
| POS_EVAL_MEASURED_IN | PosEvalMeasuredIn | ✅ |
| POS_EVAL_OVERALL_SCORE | PosEvalOverallScore | — |
| POS_EVAL_PROBLEM_SOLVING | PosEvalProblemSolving | ✅ |
| POSITION_CODE | PositionCode | ✅ |
| POSITION_ID | PositionId | ✅ |
| POSITION_OVERRIDE_FLAG | PositionOverrideFlag | — |
| POSITION_TYPE | PositionType | ✅ |
| PROBATION_PERIOD | ProbationPeriod | ✅ |
| PROBATION_UNIT | ProbationUnit | ✅ |
| PROJECTED_TERMINATION_DATE | ProjectedTerminationDate | — |
| REHIRE_AUTHORIZER_PERSON_ID | RehireAuthorizerPersonId | — |
| REHIRE_REASON | RehireReason | — |
| REHIRE_RECOMMENDATION | RehireRecommendation | — |
| REQUISITION_INTERFACE_ID | RequisitionInterfaceId | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REVOKE_USER_ACCESS | RevokeUserAccess | — |
| SALARY_AMOUNT | SalaryAmount | — |
| SALARY_BASIS_ID | SalaryBasisId | — |
| SALARY_REVIEW_DATE | SalaryReviewDate | ✅ |
| SEASONAL_END_DATE | SeasonalEndDate | ✅ |
| SEASONAL_FLAG | SeasonalFlag | ✅ |
| SEASONAL_START_DATE | SeasonalStartDate | ✅ |
| SECURITY_CLEARANCE | SecurityClearance | ✅ |
| TIME_NORMAL_FINISH | TimeNormalFinish | ✅ |
| TIME_NORMAL_START | TimeNormalStart | ✅ |
| UNION_ID | UnionId | — |
| VACANCY_HIRED_HEADCOUNT | VacancyHiredHeadcount | ✅ |
| VACANCY_JOB_SCHEDULE | VacancyJobSchedule | — |
| VACANCY_LAST_UPDATE_DATE | VacancyLastUpdateDate | ✅ |
| VACANCY_OPEN_HEADCOUNT | VacancyOpenHeadcount | ✅ |
| VACANCY_UNLIMITED_HIRE | VacancyUnlimitedHire | ✅ |
| VALIDATION_ERROR | ValidationError | — |
| VALIDATION_STATUS | ValidationStatus | — |
| WORK_AT_HOME | WorkAtHome | ✅ |
| WORK_MEASURE_FTE | WorkMeasureFte | ✅ |

### [[modelplandetailspvomodel|ModelPlanDetailsPVOModel]] (HCM · BICC: 78/107)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_TERMINATION_DATE | AcceptedTerminationDate | ✅ |
| ACTION_ID | ActionId | — |
| ACTION_REASON_ID | ActionReasonId | — |
| ACTUAL_TERMINATION_DATE | ActualTerminationDate | — |
| ANNUALIZED_SALARY_AMOUNT | OrgAnnualizedSalaryAmount | — |
| ASG_FTE_LAST_UPDATE_DATE | AsgFteLastUpdateDate | ✅ |
| ASG_LAST_UPDATE_DATE | AsgLastUpdateDate | ✅ |
| ASG_SUP_LAST_UPDATE_DATE | AsgSupLastUpdateDate | ✅ |
| ASG_SUP_MANAGER_ASSIGNMENT_ID | AsgSupManagerAssignmentId | ✅ |
| ASG_SUP_MANAGER_ID | AsgSupManagerId | ✅ |
| ASG_SUPERVISOR_ID | AsgSupervisorId | — |
| ASSIGN_GRADE_STEP_ID | AssignGradeStepId | — |
| ASSIGN_WORK_MEASURE_ID | AssignWorkMeasureId | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentName | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentStatusType | ✅ |
| ASSIGNMENT_TYPE | AssignmentType | ✅ |
| BARGAINING_UNIT_CODE | BargainingUnitCode | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| CMP_LAST_UPDATE_DATE | CmpLastUpdateDate | ✅ |
| CMP_SALARY_ID | CmpSalaryId | ✅ |
| COLLECTIVE_AGREEMENT_ID | CollectiveAgreementId | — |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| EMPLOYEE_CATEGORY | EmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | EmploymentCategory | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| FREQUENCY | Frequency | ✅ |
| FULL_PART_TIME | FullPartTime | ✅ |
| GRADE_ID | GradeId | ✅ |
| GRADE_LADDER_PGM_ID | GradeLadderPgmId | — |
| GRADE_STEP_ID | GradeStepId | ✅ |
| GRADE_STEP_LAST_UPDATE_DATE | GradeStepLastUpdateDate | ✅ |
| HIRING_STATUS | HiringStatus | ✅ |
| HOURLY_SALARIED_CODE | HourlySalariedCode | ✅ |
| INCLUDED_IN_BENCH | IncludedInBench | — |
| INTERNAL_BUILDING | InternalBuilding | ✅ |
| INTERNAL_FLOOR | InternalFloor | ✅ |
| INTERNAL_MAILSTOP | InternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | InternalOfficeNumber | ✅ |
| JOB_ID | JobId | ✅ |
| LABOUR_UNION_MEMBER_FLAG | LabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_CHANGE | LatestChange | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | — |
| MANAGER_FLAG | ManagerFlag | ✅ |
| MANAGER_ID | ManagerId | — |
| MODEL_PLAN_ASG_TYPE | ModelPlanAsgType | — |
| MODEL_PLAN_DETAIL_ID | ModelPlanDetailId | ✅ |
| MODEL_PLAN_DETAIL_TYPE | ModelPlanDetailType | — |
| MODEL_PLAN_ID | ModelPlanId | ✅ |
| NORMAL_HOURS | NormalHours | ✅ |
| NOTIFIED_TERMINATION_DATE | NotifiedTerminationDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPEN_FTE | OpenFte | ✅ |
| OPEN_HEAD_COUNT | OpenHeadCount | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PEOPLE_GROUP_ID | PeopleGroupId | ✅ |
| PERMANENT_TEMPORARY_FLAG | PermanentTemporaryFlag | ✅ |
| PERSON_ID | PersonId | ✅ |
| POS_EVAL_ACCOUNTABILITY | PosEvalAccountability | ✅ |
| POS_EVAL_DATE_EVALUATED | PosEvalDateEvaluated | ✅ |
| POS_EVAL_EVALUATION_ID | PosEvalEvaluationId | — |
| POS_EVAL_EVALUATION_SYSTEM | PosEvalEvaluationSystem | ✅ |
| POS_EVAL_KNOWHOW | PosEvalKnowhow | ✅ |
| POS_EVAL_LAST_UPDATE_DATE | PosEvalLastUpdateDate | ✅ |
| POS_EVAL_MEASURED_IN | PosEvalMeasuredIn | ✅ |
| POS_EVAL_OVERALL_SCORE | PosEvalOverallScore | — |
| POS_EVAL_PROBLEM_SOLVING | PosEvalProblemSolving | ✅ |
| POSITION_CODE | PositionCode | ✅ |
| POSITION_ID | PositionId | ✅ |
| POSITION_OVERRIDE_FLAG | PositionOverrideFlag | — |
| POSITION_TYPE | PositionType | ✅ |
| PROBATION_PERIOD | ProbationPeriod | ✅ |
| PROBATION_UNIT | ProbationUnit | ✅ |
| PROJECTED_TERMINATION_DATE | ProjectedTerminationDate | — |
| REHIRE_AUTHORIZER_PERSON_ID | RehireAuthorizerPersonId | — |
| REHIRE_REASON | RehireReason | ✅ |
| REHIRE_RECOMMENDATION | RehireRecommendation | ✅ |
| REQUISITION_INTERFACE_ID | RequisitionInterfaceId | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REVOKE_USER_ACCESS | RevokeUserAccess | — |
| SALARY_AMOUNT | SalaryAmount | — |
| SALARY_BASIS_ID | SalaryBasisId | — |
| SALARY_REVIEW_DATE | SalaryReviewDate | ✅ |
| SEASONAL_END_DATE | SeasonalEndDate | ✅ |
| SEASONAL_FLAG | SeasonalFlag | ✅ |
| SEASONAL_START_DATE | SeasonalStartDate | ✅ |
| SECURITY_CLEARANCE | SecurityClearance | ✅ |
| TIME_NORMAL_FINISH | TimeNormalFinish | ✅ |
| TIME_NORMAL_START | TimeNormalStart | ✅ |
| UNION_ID | UnionId | — |
| VACANCY_HIRED_HEADCOUNT | VacancyHiredHeadcount | ✅ |
| VACANCY_JOB_SCHEDULE | VacancyJobSchedule | — |
| VACANCY_LAST_UPDATE_DATE | VacancyLastUpdateDate | ✅ |
| VACANCY_OPEN_HEADCOUNT | VacancyOpenHeadcount | ✅ |
| VACANCY_UNLIMITED_HIRE | VacancyUnlimitedHire | ✅ |
| VALIDATION_ERROR | ValidationError | ✅ |
| VALIDATION_STATUS | ValidationStatus | ✅ |
| WORK_AT_HOME | WorkAtHome | ✅ |
| WORK_MEASURE_FTE | WorkMeasureFte | ✅ |

---

## 📚 Referências

- [Oracle Docs — HMO_MODEL_PLAN_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hmomodelplandetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
