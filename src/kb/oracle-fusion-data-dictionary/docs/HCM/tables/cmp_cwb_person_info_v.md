---
id: DOC-HCM-075
doc_type: system-doc
title: "CMP_CWB_PERSON_INFO_V — Informações de Pessoa no CWB (View)"
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
  - compensation
  - cwb-person-info-view
  - compensacao-pessoa-view
aliases:
  - CMP_CWB_PERSON_INFO_V
  - cmp_cwb_person_info_v
  - cwb-person-info-view
  - cwb-person-info-v
  - cmp-cwb-person-info-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PERSON_INFO_V

## 📌 Visão Geral

View que apresenta as **informações consolidadas de compensação por pessoa** no CWB de forma simplificada, combinando dados de múltiplas tabelas (pessoa, assignment, compensação).

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — consulta pré-montada que combina dados de múltiplas tabelas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** View pré-montada com dados de pessoa e compensação.
- **Relatórios:** Base para relatórios de compensação sem necessidade de JOINs complexos.
- **Análise:** Visão consolidada para análise de equity e compa-ratio.
- **Self-service gerencial:** Alimenta dashboards do CWB.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 2 | PERSON_NAME | VARCHAR2(360) | NULL | Identificação | Nome completo do colaborador | — | 🟡 80% |
| 3 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 4 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | [[per_all_people_f]] | 🟢 85% |
| 5 | MANAGER_NAME | VARCHAR2(360) | NULL | Identificação | Nome do gestor | — | 🟡 80% |
| 6 | CURRENT_SALARY | NUMBER | NULL | Financeiro | Salário atual | — | 🟢 85% |
| 7 | PROPOSED_SALARY | NUMBER | NULL | Financeiro | Salário proposto | — | 🟢 85% |
| 8 | MERIT_PERCENT | NUMBER | NULL | Percentual | Percentual de merit increase | — | 🟡 80% |
| 9 | BONUS_AMOUNT | NUMBER | NULL | Financeiro | Valor de bônus | — | 🟡 80% |
| 10 | COMPA_RATIO | NUMBER | NULL | Indicador | Compa-ratio | — | 🟡 80% |
| 11 | PERFORMANCE_RATING | VARCHAR2(30) | NULL | Avaliação | Rating de performance | — | 🟡 75% |
| 12 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Workflow | Status de aprovação | — | 🟡 80% |
| 13 | DEPARTMENT | VARCHAR2(240) | NULL | Organização | Departamento do colaborador | — | 🟡 75% |
| 14 | JOB_NAME | VARCHAR2(240) | NULL | Organização | Cargo do colaborador | — | 🟡 75% |
| 15 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | — | 🟢 85% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` e `MANAGER_ID` (colaborador na visao do workbench)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Visão consolidada de compensação
```sql
SELECT v.PERSON_NAME, v.JOB_NAME, v.DEPARTMENT,
       v.CURRENT_SALARY, v.PROPOSED_SALARY, v.MERIT_PERCENT,
       v.COMPA_RATIO, v.PERFORMANCE_RATING, v.APPROVAL_STATUS
FROM   CMP_CWB_PERSON_INFO_V v
WHERE  v.MANAGER_ID = :p_manager_id
  AND  v.PLAN_ID = :p_plan_id
ORDER BY v.DEPARTMENT, v.PERSON_NAME;
```

### Filtros comuns
- `APPROVAL_STATUS = 'SUBMITTED'` — Propostas submetidas
- `COMPA_RATIO < 0.8` — Abaixo de 80% do midpoint
- `PERFORMANCE_RATING = '5'` — Top performers

---

## 🔒 Observações

- View somente leitura — dados derivados de `CMP_CWB_PERSON_INFO` e tabelas de pessoas.
- Inclui nomes, departamento e cargo para facilitar análise sem JOINs adicionais.
- Contém dados de compensação sensíveis — classificar como `restricted`.

---

## 🔗 PVOs Relacionados

### [[personinfopvo|PersonInfoPVO]] (HCM · BICC: 152/171)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CODE | PersonInformationPEOAccessCode | ✅ |
| ACTION_REASON_ID | PersonInformationPEOActionReasonId | — |
| ADJUSTED_CHANGE_AMOUNT | PersonInformationPEOAdjustedChangeAmount | ✅ |
| ADJUSTED_SALARY_CURRENT | PersonInformationPEOAdjustedSalaryCurrent | ✅ |
| ADJUSTED_SALARY_NEW | PersonInformationPEOAdjustedSalaryNew | ✅ |
| ADJUSTED_SVC_DATE | PersonInformationPEOAdjustedSvcDate | ✅ |
| ADJUSTMENT_FACTOR | PersonInformationPEOAdjustmentFactor | ✅ |
| APPROVAL_CODE | PersonInformationPEOApprovalCode | ✅ |
| APPROVAL_DATE | PersonInformationPEOApprovalDate | ✅ |
| ASSIGNMENT_ASSIGNMENT_ID | PersonInformationPEOAssignmentAssignmentId | — |
| ASSIGNMENT_CHANGE_DATE | PersonInformationPEOAssignmentChangeDate | ✅ |
| ASSIGNMENT_ID | PersonInformationPEOAssignmentId | — |
| ASSIGNMENT_NAME | PersonInformationPEOAssignmentName | — |
| ASSIGNMENT_POSTED_DATE | PersonInformationPEOAssignmentPostedDate | ✅ |
| ASSIGNMENT_POSTING_DATE | PersonInformationPEOAssignmentPostingDate | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | PersonInformationPEOAssignmentStatusTypeId | ✅ |
| BASE_SALARY | PersonInformationPEOBaseSalary | ✅ |
| BASE_SALARY_CHANGE_DATE | PersonInformationPEOBaseSalaryChangeDate | ✅ |
| BASE_SALARY_CHANGE_VAL | PersonInformationPEOBaseSalaryChangeVal | ✅ |
| BASE_SALARY_CURRENCY | PersonInformationPEOBaseSalaryCurrency | ✅ |
| BASE_SALARY_FREQUENCY | PersonInformationPEOBaseSalaryFrequency | ✅ |
| BUSINESS_GROUP_ID | PersonInformationPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | PersonInformationPEOBusinessUnitId | — |
| CUSTOM_SEGMENT1 | PersonInformationPEOCustomSegment1 | ✅ |
| CUSTOM_SEGMENT10 | PersonInformationPEOCustomSegment10 | ✅ |
| CUSTOM_SEGMENT11 | PersonInformationPEOCustomSegment11 | ✅ |
| CUSTOM_SEGMENT12 | PersonInformationPEOCustomSegment12 | ✅ |
| CUSTOM_SEGMENT13 | PersonInformationPEOCustomSegment13 | ✅ |
| CUSTOM_SEGMENT14 | PersonInformationPEOCustomSegment14 | ✅ |
| CUSTOM_SEGMENT15 | PersonInformationPEOCustomSegment15 | ✅ |
| CUSTOM_SEGMENT16 | PersonInformationPEOCustomSegment16 | ✅ |
| CUSTOM_SEGMENT17 | PersonInformationPEOCustomSegment17 | ✅ |
| CUSTOM_SEGMENT18 | PersonInformationPEOCustomSegment18 | ✅ |
| CUSTOM_SEGMENT19 | PersonInformationPEOCustomSegment19 | ✅ |
| CUSTOM_SEGMENT2 | PersonInformationPEOCustomSegment2 | ✅ |
| CUSTOM_SEGMENT20 | PersonInformationPEOCustomSegment20 | ✅ |
| CUSTOM_SEGMENT21 | PersonInformationPEOCustomSegment21 | ✅ |
| CUSTOM_SEGMENT22 | PersonInformationPEOCustomSegment22 | ✅ |
| CUSTOM_SEGMENT23 | PersonInformationPEOCustomSegment23 | ✅ |
| CUSTOM_SEGMENT24 | PersonInformationPEOCustomSegment24 | ✅ |
| CUSTOM_SEGMENT25 | PersonInformationPEOCustomSegment25 | ✅ |
| CUSTOM_SEGMENT26 | PersonInformationPEOCustomSegment26 | ✅ |
| CUSTOM_SEGMENT27 | PersonInformationPEOCustomSegment27 | ✅ |
| CUSTOM_SEGMENT28 | PersonInformationPEOCustomSegment28 | ✅ |
| CUSTOM_SEGMENT29 | PersonInformationPEOCustomSegment29 | ✅ |
| CUSTOM_SEGMENT3 | PersonInformationPEOCustomSegment3 | ✅ |
| CUSTOM_SEGMENT30 | PersonInformationPEOCustomSegment30 | ✅ |
| CUSTOM_SEGMENT31 | PersonInformationPEOCustomSegment31 | ✅ |
| CUSTOM_SEGMENT32 | PersonInformationPEOCustomSegment32 | ✅ |
| CUSTOM_SEGMENT33 | PersonInformationPEOCustomSegment33 | ✅ |
| CUSTOM_SEGMENT34 | PersonInformationPEOCustomSegment34 | ✅ |
| CUSTOM_SEGMENT35 | PersonInformationPEOCustomSegment35 | ✅ |
| CUSTOM_SEGMENT36 | PersonInformationPEOCustomSegment36 | ✅ |
| CUSTOM_SEGMENT37 | PersonInformationPEOCustomSegment37 | ✅ |
| CUSTOM_SEGMENT38 | PersonInformationPEOCustomSegment38 | ✅ |
| CUSTOM_SEGMENT39 | PersonInformationPEOCustomSegment39 | ✅ |
| CUSTOM_SEGMENT4 | PersonInformationPEOCustomSegment4 | ✅ |
| CUSTOM_SEGMENT40 | PersonInformationPEOCustomSegment40 | ✅ |
| CUSTOM_SEGMENT41 | PersonInformationPEOCustomSegment41 | ✅ |
| CUSTOM_SEGMENT42 | PersonInformationPEOCustomSegment42 | ✅ |
| CUSTOM_SEGMENT43 | PersonInformationPEOCustomSegment43 | ✅ |
| CUSTOM_SEGMENT44 | PersonInformationPEOCustomSegment44 | ✅ |
| CUSTOM_SEGMENT45 | PersonInformationPEOCustomSegment45 | ✅ |
| CUSTOM_SEGMENT46 | PersonInformationPEOCustomSegment46 | ✅ |
| CUSTOM_SEGMENT47 | PersonInformationPEOCustomSegment47 | ✅ |
| CUSTOM_SEGMENT48 | PersonInformationPEOCustomSegment48 | ✅ |
| CUSTOM_SEGMENT49 | PersonInformationPEOCustomSegment49 | ✅ |
| CUSTOM_SEGMENT5 | PersonInformationPEOCustomSegment5 | ✅ |
| CUSTOM_SEGMENT50 | PersonInformationPEOCustomSegment50 | ✅ |
| CUSTOM_SEGMENT6 | PersonInformationPEOCustomSegment6 | ✅ |
| CUSTOM_SEGMENT7 | PersonInformationPEOCustomSegment7 | ✅ |
| CUSTOM_SEGMENT8 | PersonInformationPEOCustomSegment8 | ✅ |
| CUSTOM_SEGMENT9 | PersonInformationPEOCustomSegment9 | ✅ |
| DATE_OF_BIRTH | PersonInformationPEODateOfBirth | ✅ |
| DISABILITY_STATUS | PersonInformationPEODisabilityStatus | ✅ |
| DO_NOT_POST_FLAG | PersonInformationPEODoNotPostFlag | ✅ |
| DUE_DATE | PersonInformationPEODueDate | ✅ |
| EFFECTIVE_DATE | PersonInformationPEOEffectiveDate | ✅ |
| EMAIL_ADDRESS | PersonInformationPEOEmailAddress | ✅ |
| EMP_STATUS_CODE | PersonInformationPEOEmpStatusCode | ✅ |
| EMPLOYMENT_CATEGORY | PersonInformationPEOEmploymentCategory | ✅ |
| ETHNICITY | PersonInformationPEOEthnicity | ✅ |
| FREQUENCY | PersonInformationPEOFrequency | ✅ |
| FTE_ANNUAL_CHANGE_AMT | PersonInformationPEOFteAnnualChangeAmt | ✅ |
| FTE_ANNUAL_SALARY_CURRENT | PersonInformationPEOFteAnnualSalaryCurrent | ✅ |
| FTE_ANNUAL_SALARY_NEW | PersonInformationPEOFteAnnualSalaryNew | ✅ |
| FTE_ANNUALIZATION_FACTOR | PersonInformationPEOFteAnnualizationFactor | — |
| FTE_FACTOR | PersonInformationPEOFteFactor | ✅ |
| GRADE_ANNUALIZATION_FACTOR | PersonInformationPEOGradeAnnualizationFactor | ✅ |
| GRADE_ATTRIBUTE1 | PersonInformationPEOGradeAttribute1 | ✅ |
| GRADE_ATTRIBUTE2 | PersonInformationPEOGradeAttribute2 | ✅ |
| GRADE_ATTRIBUTE3 | PersonInformationPEOGradeAttribute3 | ✅ |
| GRADE_CHANGE_DATE | PersonInformationPEOGradeChangeDate | ✅ |
| GRADE_COMPARATIO | PersonInformationPEOGradeComparatio | ✅ |
| GRADE_DECILE | PersonInformationPEOGradeDecile | ✅ |
| GRADE_ID | PersonInformationPEOGradeId | ✅ |
| GRADE_MAX_VAL | PersonInformationPEOGradeMaxVal | ✅ |
| GRADE_MID_POINT | PersonInformationPEOGradeMidPoint | ✅ |
| GRADE_MIN_VAL | PersonInformationPEOGradeMinVal | ✅ |
| GRADE_PCT_IN_RANGE | PersonInformationPEOGradePctInRange | ✅ |
| GRADE_QUARTILE | PersonInformationPEOGradeQuartile | ✅ |
| GRADE_QUINTILE | PersonInformationPEOGradeQuintile | ✅ |
| GRADE_RATE_ID | PersonInformationPEOGradeRateId | — |
| JOB_ATTRIBUTE1 | PersonInformationPEOJobAttribute1 | ✅ |
| JOB_ATTRIBUTE2 | PersonInformationPEOJobAttribute2 | ✅ |
| JOB_ATTRIBUTE3 | PersonInformationPEOJobAttribute3 | ✅ |
| JOB_ATTRIBUTE4 | PersonInformationPEOJobAttribute4 | ✅ |
| JOB_ATTRIBUTE5 | PersonInformationPEOJobAttribute5 | ✅ |
| JOB_ATTRIBUTE6 | PersonInformationPEOJobAttribute6 | ✅ |
| JOB_CHANGE_DATE | PersonInformationPEOJobChangeDate | ✅ |
| JOB_ID | PersonInformationPEOJobId | ✅ |
| LAST_UPDATE_DATE | PersonInformationPEOLastUpdateDate | ✅ |
| LAST_UPDATED_BY | PersonInformationPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | PersonInformationPEOLegalEntityId | ✅ |
| LEGISLATION_CODE | PersonInformationPEOLegislationCode | ✅ |
| LOCATION_ID | PersonInformationPEOLocationId | ✅ |
| MGR_OVERRIDE_DATE | PersonInformationPEOMgrOverrideDate | ✅ |
| MGR_OVERRIDE_DATE | PersonInformationPEOReassignmentDate | ✅ |
| MGR_OVERRIDE_PERSON_ID | PersonInformationPEOReassignmentMgrID | — |
| MGR_STATUS_CODE | PersonInformationPEOMgrStatusCode | ✅ |
| NATIONALITY | PersonInformationPEONationality | ✅ |
| NEW_BASE_SALARY | PersonInformationPEONewBaseSalary | ✅ |
| NEW_GRADE_COMPARATIO | PersonInformationPEONewGradeComparatio | ✅ |
| NEW_GRADE_DECILE | PersonInformationPEONewGradeDecile | ✅ |
| NEW_GRADE_PCT_IN_RANGE | PersonInformationPEONewGradePctInRange | ✅ |
| NEW_GRADE_QUARTILE | PersonInformationPEONewGradeQuartile | ✅ |
| NEW_GRADE_QUINTILE | PersonInformationPEONewGradeQuintile | ✅ |
| NON_DISCRIMINATION_CODE | PersonInformationPEONonDiscriminationCode | ✅ |
| NORMAL_HOURS | PersonInformationPEONormalHours | ✅ |
| ORGANIZATION_ID | PersonInformationPEOOrganizationId | ✅ |
| ORIGINAL_START_DATE | PersonInformationPEOOriginalStartDate | ✅ |
| PAY_ANNUALIZATION_FACTOR | PersonInformationPEOPayAnnualizationFactor | ✅ |
| PAYROLL_ID | PersonInformationPEOPayrollId | ✅ |
| PERFORMANCE_DATE | PersonInformationPEOPerformanceDate | ✅ |
| PERFORMANCE_RATING | PersonInformationPEOPerformanceRating | ✅ |
| PERFORMANCE_RATING_DATE | PersonInformationPEOPerformanceRatingDate | ✅ |
| PERFORMANCE_RATING_TYPE | PersonInformationPEOPerformanceRatingType | ✅ |
| PERIOD_COMP_TYPE | PersonInformationPEOPeriodCompType | ✅ |
| PERIOD_ID | PersonInformationPEOPeriodId | — |
| PERSON_EVENT_ID | PersonEventId | ✅ |
| PERSON_ID | PersonInformationPEOPersonId | ✅ |
| PLACEHOLDER_FLAG | PersonInformationPEOPlaceholderFlag | ✅ |
| PLAN_ID | PersonInformationPEOPlanId | — |
| PLAN_PERIOD_ID | PersonInformationPEOPlanPeriodId | — |
| POSITION_CHANGE_DATE | PersonInformationPEOPositionChangeDate | ✅ |
| POSITION_ID | PersonInformationPEOPositionId | — |
| PRIOR_SALARY | PersonInformationPEOPriorSalary | ✅ |
| PRIOR_SALARY_CHG_PCT | PersonInformationPEOPriorSalaryChgPct | — |
| RELIGION | PersonInformationPEOReligion | ✅ |
| RISK_OF_LOSS | PersonInformationPEORiskOfLoss | ✅ |
| RVW_MGR_PERSON_ID | PersonInformationPEOReviewMgrID | — |
| SALARY_BASIS_ID | PersonInformationPEOSalaryBasisId | — |
| SEC_MGR_PERSON_ID | PersonInformationPEOSecondaryMgrID | — |
| SEX | PersonInformationPEOSex | ✅ |
| START_DATE | PersonInformationPEOStartDate | ✅ |
| SUBMIT_DATE | PersonInformationPEOSubmitDate | ✅ |
| SUPERVISOR_ID | PersonInformationPEOSupervisorId | — |
| USER_PREFERRED_EXCHANGE_RATE | PersonInformationPEOUserPreferredExchangeRate | ✅ |
| VETERAN_STATUS | PersonInformationPEOVeteranStatus | ✅ |
| WORK_TELEPHONE | PersonInformationPEOWorkTelephone | ✅ |
| WORKER_NUMBER | PersonInformationPEOWorkerNumber | ✅ |
| WORKER_POTENTIAL | PersonInformationPEOWorkerPotential | ✅ |
| WORKING_HOURS | PersonInformationPEOWorkingHours | ✅ |
| WS_MGR_ASSIGNMENT_ID | PersonInformationPEOWsMgrAssignmentId | — |
| WS_MGR_PERSON_EVENT_ID | PersonInformationPEOWsMgrPersonEventId | ✅ |
| WS_MGR_PERSON_ID | PersonInformationPEOWsMgrPersonId | ✅ |
| XCHG_RATE | PersonInformationPEOXchgRate | — |
| YEARS_EMPLOYED | PersonInformationPEOYearsEmployed | ✅ |
| YEARS_IN_GRADE | PersonInformationPEOYearsInGrade | ✅ |
| YEARS_IN_JOB | PersonInformationPEOYearsInJob | ✅ |
| YEARS_IN_POSITION | PersonInformationPEOYearsInPosition | ✅ |

### [[personinfopvoviewall|PersonInfoPVOViewAll]] (HCM · BICC: 152/171)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_CODE | PersonInformationPEOAccessCode | ✅ |
| ACTION_REASON_ID | PersonInformationPEOActionReasonId | — |
| ADJUSTED_CHANGE_AMOUNT | PersonInformationPEOAdjustedChangeAmount | ✅ |
| ADJUSTED_SALARY_CURRENT | PersonInformationPEOAdjustedSalaryCurrent | ✅ |
| ADJUSTED_SALARY_NEW | PersonInformationPEOAdjustedSalaryNew | ✅ |
| ADJUSTED_SVC_DATE | PersonInformationPEOAdjustedSvcDate | ✅ |
| ADJUSTMENT_FACTOR | PersonInformationPEOAdjustmentFactor | ✅ |
| APPROVAL_CODE | PersonInformationPEOApprovalCode | ✅ |
| APPROVAL_DATE | PersonInformationPEOApprovalDate | ✅ |
| ASSIGNMENT_ASSIGNMENT_ID | PersonInformationPEOAssignmentAssignmentId | — |
| ASSIGNMENT_CHANGE_DATE | PersonInformationPEOAssignmentChangeDate | ✅ |
| ASSIGNMENT_ID | PersonInformationPEOAssignmentId | — |
| ASSIGNMENT_NAME | PersonInformationPEOAssignmentName | — |
| ASSIGNMENT_POSTED_DATE | PersonInformationPEOAssignmentPostedDate | ✅ |
| ASSIGNMENT_POSTING_DATE | PersonInformationPEOAssignmentPostingDate | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | PersonInformationPEOAssignmentStatusTypeId | ✅ |
| BASE_SALARY | PersonInformationPEOBaseSalary | ✅ |
| BASE_SALARY_CHANGE_DATE | PersonInformationPEOBaseSalaryChangeDate | ✅ |
| BASE_SALARY_CHANGE_VAL | PersonInformationPEOBaseSalaryChangeVal | ✅ |
| BASE_SALARY_CURRENCY | PersonInformationPEOBaseSalaryCurrency | ✅ |
| BASE_SALARY_FREQUENCY | PersonInformationPEOBaseSalaryFrequency | ✅ |
| BUSINESS_GROUP_ID | PersonInformationPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | PersonInformationPEOBusinessUnitId | — |
| CUSTOM_SEGMENT1 | PersonInformationPEOCustomSegment1 | ✅ |
| CUSTOM_SEGMENT10 | PersonInformationPEOCustomSegment10 | ✅ |
| CUSTOM_SEGMENT11 | PersonInformationPEOCustomSegment11 | ✅ |
| CUSTOM_SEGMENT12 | PersonInformationPEOCustomSegment12 | ✅ |
| CUSTOM_SEGMENT13 | PersonInformationPEOCustomSegment13 | ✅ |
| CUSTOM_SEGMENT14 | PersonInformationPEOCustomSegment14 | ✅ |
| CUSTOM_SEGMENT15 | PersonInformationPEOCustomSegment15 | ✅ |
| CUSTOM_SEGMENT16 | PersonInformationPEOCustomSegment16 | ✅ |
| CUSTOM_SEGMENT17 | PersonInformationPEOCustomSegment17 | ✅ |
| CUSTOM_SEGMENT18 | PersonInformationPEOCustomSegment18 | ✅ |
| CUSTOM_SEGMENT19 | PersonInformationPEOCustomSegment19 | ✅ |
| CUSTOM_SEGMENT2 | PersonInformationPEOCustomSegment2 | ✅ |
| CUSTOM_SEGMENT20 | PersonInformationPEOCustomSegment20 | ✅ |
| CUSTOM_SEGMENT21 | PersonInformationPEOCustomSegment21 | ✅ |
| CUSTOM_SEGMENT22 | PersonInformationPEOCustomSegment22 | ✅ |
| CUSTOM_SEGMENT23 | PersonInformationPEOCustomSegment23 | ✅ |
| CUSTOM_SEGMENT24 | PersonInformationPEOCustomSegment24 | ✅ |
| CUSTOM_SEGMENT25 | PersonInformationPEOCustomSegment25 | ✅ |
| CUSTOM_SEGMENT26 | PersonInformationPEOCustomSegment26 | ✅ |
| CUSTOM_SEGMENT27 | PersonInformationPEOCustomSegment27 | ✅ |
| CUSTOM_SEGMENT28 | PersonInformationPEOCustomSegment28 | ✅ |
| CUSTOM_SEGMENT29 | PersonInformationPEOCustomSegment29 | ✅ |
| CUSTOM_SEGMENT3 | PersonInformationPEOCustomSegment3 | ✅ |
| CUSTOM_SEGMENT30 | PersonInformationPEOCustomSegment30 | ✅ |
| CUSTOM_SEGMENT31 | PersonInformationPEOCustomSegment31 | ✅ |
| CUSTOM_SEGMENT32 | PersonInformationPEOCustomSegment32 | ✅ |
| CUSTOM_SEGMENT33 | PersonInformationPEOCustomSegment33 | ✅ |
| CUSTOM_SEGMENT34 | PersonInformationPEOCustomSegment34 | ✅ |
| CUSTOM_SEGMENT35 | PersonInformationPEOCustomSegment35 | ✅ |
| CUSTOM_SEGMENT36 | PersonInformationPEOCustomSegment36 | ✅ |
| CUSTOM_SEGMENT37 | PersonInformationPEOCustomSegment37 | ✅ |
| CUSTOM_SEGMENT38 | PersonInformationPEOCustomSegment38 | ✅ |
| CUSTOM_SEGMENT39 | PersonInformationPEOCustomSegment39 | ✅ |
| CUSTOM_SEGMENT4 | PersonInformationPEOCustomSegment4 | ✅ |
| CUSTOM_SEGMENT40 | PersonInformationPEOCustomSegment40 | ✅ |
| CUSTOM_SEGMENT41 | PersonInformationPEOCustomSegment41 | ✅ |
| CUSTOM_SEGMENT42 | PersonInformationPEOCustomSegment42 | ✅ |
| CUSTOM_SEGMENT43 | PersonInformationPEOCustomSegment43 | ✅ |
| CUSTOM_SEGMENT44 | PersonInformationPEOCustomSegment44 | ✅ |
| CUSTOM_SEGMENT45 | PersonInformationPEOCustomSegment45 | ✅ |
| CUSTOM_SEGMENT46 | PersonInformationPEOCustomSegment46 | ✅ |
| CUSTOM_SEGMENT47 | PersonInformationPEOCustomSegment47 | ✅ |
| CUSTOM_SEGMENT48 | PersonInformationPEOCustomSegment48 | ✅ |
| CUSTOM_SEGMENT49 | PersonInformationPEOCustomSegment49 | ✅ |
| CUSTOM_SEGMENT5 | PersonInformationPEOCustomSegment5 | ✅ |
| CUSTOM_SEGMENT50 | PersonInformationPEOCustomSegment50 | ✅ |
| CUSTOM_SEGMENT6 | PersonInformationPEOCustomSegment6 | ✅ |
| CUSTOM_SEGMENT7 | PersonInformationPEOCustomSegment7 | ✅ |
| CUSTOM_SEGMENT8 | PersonInformationPEOCustomSegment8 | ✅ |
| CUSTOM_SEGMENT9 | PersonInformationPEOCustomSegment9 | ✅ |
| DATE_OF_BIRTH | PersonInformationPEODateOfBirth | ✅ |
| DISABILITY_STATUS | PersonInformationPEODisabilityStatus | ✅ |
| DO_NOT_POST_FLAG | PersonInformationPEODoNotPostFlag | ✅ |
| DUE_DATE | PersonInformationPEODueDate | ✅ |
| EFFECTIVE_DATE | PersonInformationPEOEffectiveDate | ✅ |
| EMAIL_ADDRESS | PersonInformationPEOEmailAddress | ✅ |
| EMP_STATUS_CODE | PersonInformationPEOEmpStatusCode | ✅ |
| EMPLOYMENT_CATEGORY | PersonInformationPEOEmploymentCategory | ✅ |
| ETHNICITY | PersonInformationPEOEthnicity | ✅ |
| FREQUENCY | PersonInformationPEOFrequency | ✅ |
| FTE_ANNUAL_CHANGE_AMT | PersonInformationPEOFteAnnualChangeAmt | ✅ |
| FTE_ANNUAL_SALARY_CURRENT | PersonInformationPEOFteAnnualSalaryCurrent | ✅ |
| FTE_ANNUAL_SALARY_NEW | PersonInformationPEOFteAnnualSalaryNew | ✅ |
| FTE_ANNUALIZATION_FACTOR | PersonInformationPEOFteAnnualizationFactor | — |
| FTE_FACTOR | PersonInformationPEOFteFactor | ✅ |
| GRADE_ANNUALIZATION_FACTOR | PersonInformationPEOGradeAnnualizationFactor | ✅ |
| GRADE_ATTRIBUTE1 | PersonInformationPEOGradeAttribute1 | ✅ |
| GRADE_ATTRIBUTE2 | PersonInformationPEOGradeAttribute2 | ✅ |
| GRADE_ATTRIBUTE3 | PersonInformationPEOGradeAttribute3 | ✅ |
| GRADE_CHANGE_DATE | PersonInformationPEOGradeChangeDate | ✅ |
| GRADE_COMPARATIO | PersonInformationPEOGradeComparatio | ✅ |
| GRADE_DECILE | PersonInformationPEOGradeDecile | ✅ |
| GRADE_ID | PersonInformationPEOGradeId | ✅ |
| GRADE_MAX_VAL | PersonInformationPEOGradeMaxVal | ✅ |
| GRADE_MID_POINT | PersonInformationPEOGradeMidPoint | ✅ |
| GRADE_MIN_VAL | PersonInformationPEOGradeMinVal | ✅ |
| GRADE_PCT_IN_RANGE | PersonInformationPEOGradePctInRange | ✅ |
| GRADE_QUARTILE | PersonInformationPEOGradeQuartile | ✅ |
| GRADE_QUINTILE | PersonInformationPEOGradeQuintile | ✅ |
| GRADE_RATE_ID | PersonInformationPEOGradeRateId | — |
| JOB_ATTRIBUTE1 | PersonInformationPEOJobAttribute1 | ✅ |
| JOB_ATTRIBUTE2 | PersonInformationPEOJobAttribute2 | ✅ |
| JOB_ATTRIBUTE3 | PersonInformationPEOJobAttribute3 | ✅ |
| JOB_ATTRIBUTE4 | PersonInformationPEOJobAttribute4 | ✅ |
| JOB_ATTRIBUTE5 | PersonInformationPEOJobAttribute5 | ✅ |
| JOB_ATTRIBUTE6 | PersonInformationPEOJobAttribute6 | ✅ |
| JOB_CHANGE_DATE | PersonInformationPEOJobChangeDate | ✅ |
| JOB_ID | PersonInformationPEOJobId | ✅ |
| LAST_UPDATE_DATE | PersonInformationPEOLastUpdateDate | ✅ |
| LAST_UPDATED_BY | PersonInformationPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | PersonInformationPEOLegalEntityId | ✅ |
| LEGISLATION_CODE | PersonInformationPEOLegislationCode | ✅ |
| LOCATION_ID | PersonInformationPEOLocationId | ✅ |
| MGR_OVERRIDE_DATE | PersonInformationPEOMgrOverrideDate | ✅ |
| MGR_OVERRIDE_DATE | PersonInformationPEOReassignmentDate | ✅ |
| MGR_OVERRIDE_PERSON_ID | PersonInformationPEOReassignmentMgrID | — |
| MGR_STATUS_CODE | PersonInformationPEOMgrStatusCode | ✅ |
| NATIONALITY | PersonInformationPEONationality | ✅ |
| NEW_BASE_SALARY | PersonInformationPEONewBaseSalary | ✅ |
| NEW_GRADE_COMPARATIO | PersonInformationPEONewGradeComparatio | ✅ |
| NEW_GRADE_DECILE | PersonInformationPEONewGradeDecile | ✅ |
| NEW_GRADE_PCT_IN_RANGE | PersonInformationPEONewGradePctInRange | ✅ |
| NEW_GRADE_QUARTILE | PersonInformationPEONewGradeQuartile | ✅ |
| NEW_GRADE_QUINTILE | PersonInformationPEONewGradeQuintile | ✅ |
| NON_DISCRIMINATION_CODE | PersonInformationPEONonDiscriminationCode | ✅ |
| NORMAL_HOURS | PersonInformationPEONormalHours | ✅ |
| ORGANIZATION_ID | PersonInformationPEOOrganizationId | ✅ |
| ORIGINAL_START_DATE | PersonInformationPEOOriginalStartDate | ✅ |
| PAY_ANNUALIZATION_FACTOR | PersonInformationPEOPayAnnualizationFactor | ✅ |
| PAYROLL_ID | PersonInformationPEOPayrollId | ✅ |
| PERFORMANCE_DATE | PersonInformationPEOPerformanceDate | ✅ |
| PERFORMANCE_RATING | PersonInformationPEOPerformanceRating | ✅ |
| PERFORMANCE_RATING_DATE | PersonInformationPEOPerformanceRatingDate | ✅ |
| PERFORMANCE_RATING_TYPE | PersonInformationPEOPerformanceRatingType | ✅ |
| PERIOD_COMP_TYPE | PersonInformationPEOPeriodCompType | ✅ |
| PERIOD_ID | PersonInformationPEOPeriodId | — |
| PERSON_EVENT_ID | PersonEventId | ✅ |
| PERSON_ID | PersonInformationPEOPersonId | ✅ |
| PLACEHOLDER_FLAG | PersonInformationPEOPlaceholderFlag | ✅ |
| PLAN_ID | PersonInformationPEOPlanId | — |
| PLAN_PERIOD_ID | PersonInformationPEOPlanPeriodId | — |
| POSITION_CHANGE_DATE | PersonInformationPEOPositionChangeDate | ✅ |
| POSITION_ID | PersonInformationPEOPositionId | — |
| PRIOR_SALARY | PersonInformationPEOPriorSalary | ✅ |
| PRIOR_SALARY_CHG_PCT | PersonInformationPEOPriorSalaryChgPct | — |
| RELIGION | PersonInformationPEOReligion | ✅ |
| RISK_OF_LOSS | PersonInformationPEORiskOfLoss | ✅ |
| RVW_MGR_PERSON_ID | PersonInformationPEOReviewMgrID | — |
| SALARY_BASIS_ID | PersonInformationPEOSalaryBasisId | — |
| SEC_MGR_PERSON_ID | PersonInformationPEOSecondaryMgrID | — |
| SEX | PersonInformationPEOSex | ✅ |
| START_DATE | PersonInformationPEOStartDate | ✅ |
| SUBMIT_DATE | PersonInformationPEOSubmitDate | ✅ |
| SUPERVISOR_ID | PersonInformationPEOSupervisorId | — |
| USER_PREFERRED_EXCHANGE_RATE | PersonInformationPEOUserPreferredExchangeRate | ✅ |
| VETERAN_STATUS | PersonInformationPEOVeteranStatus | ✅ |
| WORK_TELEPHONE | PersonInformationPEOWorkTelephone | ✅ |
| WORKER_NUMBER | PersonInformationPEOWorkerNumber | ✅ |
| WORKER_POTENTIAL | PersonInformationPEOWorkerPotential | ✅ |
| WORKING_HOURS | PersonInformationPEOWorkingHours | ✅ |
| WS_MGR_ASSIGNMENT_ID | PersonInformationPEOWsMgrAssignmentId | — |
| WS_MGR_PERSON_EVENT_ID | PersonInformationPEOWsMgrPersonEventId | ✅ |
| WS_MGR_PERSON_ID | PersonInformationPEOWsMgrPersonId | ✅ |
| XCHG_RATE | PersonInformationPEOXchgRate | — |
| YEARS_EMPLOYED | PersonInformationPEOYearsEmployed | ✅ |
| YEARS_IN_GRADE | PersonInformationPEOYearsInGrade | ✅ |
| YEARS_IN_JOB | PersonInformationPEOYearsInJob | ✅ |
| YEARS_IN_POSITION | PersonInformationPEOYearsInPosition | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PERSON_INFO_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbpersoninfov.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
