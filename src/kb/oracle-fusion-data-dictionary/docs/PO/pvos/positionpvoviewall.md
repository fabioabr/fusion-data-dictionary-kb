---
id: DOC-PO-PVO-PositionPVOViewAll
doc_type: system-doc
title: "PositionPVOViewAll — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PositionPVOViewAll
  - positionpvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PositionPVOViewAll

## 📌 Visão Geral

Extrai visão completa e irrestrita de todas as posições organizacionais, sem filtros de segurança. Permite mapeamento total da estrutura de cargos para análise administrativa e planejamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.PositionPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 161 | 11 | 3 | 98 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 8 atributos (4 BICC)
- [[hr_all_positions_f|HR_ALL_POSITIONS_F]] — 70 atributos (3 PKs, 56 BICC)
- [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]] — 24 atributos (10 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 12 atributos (6 BICC)
- [[irc_requisitions_b|IRC_REQUISITIONS_B]] — 3 atributos (2 BICC)
- [[irc_requisitions_tl|IRC_REQUISITIONS_TL]] — 4 atributos (2 BICC)
- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 3 atributos (1 BICC)
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 2 atributos (1 BICC)
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 4 atributos (2 BICC)
- [[per_job_evaluations|PER_JOB_EVALUATIONS]] — 18 atributos (12 BICC)
- [[per_position_hierarchy_f|PER_POSITION_HIERARCHY_F]] — 13 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DelegatePositionOrgUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DelegatePositionOrgUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DelegatePositionOrgUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | DelegatePositionOrgUnitPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | ParentPositionOrgUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | ParentPositionOrgUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | ParentPositionOrgUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ParentPositionOrgUnitPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_all_positions_f|HR_ALL_POSITIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DelegatePositionPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DelegatePositionPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DelegatePositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | DelegatePositionPEOPositionCode | POSITION_CODE | — | ✅ |
| 5 | DelegatePositionPEOPositionId | POSITION_ID | — | — |
| 6 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | ParentPositionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | ParentPositionPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | ParentPositionPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | ParentPositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ParentPositionPEOPositionCode | POSITION_CODE | — | ✅ |
| 13 | ParentPositionPEOPositionId | POSITION_ID | — | ✅ |
| 14 | PositionId | POSITION_ID | 🔑 | ✅ |
| 15 | PositionPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 16 | PositionPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 17 | PositionPEOAnnualWorkingDuration | ANNUAL_WORKING_DURATION | — | — |
| 18 | PositionPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 19 | PositionPEOAssignmentCategory | ASSIGNMENT_CATEGORY | — | ✅ |
| 20 | PositionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 21 | PositionPEOBargainingUnitCd | BARGAINING_UNIT_CD | — | ✅ |
| 22 | PositionPEOBudgetAmount | BUDGET_AMOUNT | — | ✅ |
| 23 | PositionPEOBudgetAmountCurrency | BUDGET_AMOUNT_CURRENCY | — | ✅ |
| 24 | PositionPEOBudgetedPositionFlag | BUDGETED_POSITION_FLAG | — | ✅ |
| 25 | PositionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 26 | PositionPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 27 | PositionPEOCalculateFte | CALCULATE_FTE | — | — |
| 28 | PositionPEOCategoryCode | CATEGORY_CODE | — | — |
| 29 | PositionPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 30 | PositionPEOCostCenter | COST_CENTER | — | — |
| 31 | PositionPEOCreatedBy | CREATED_BY | — | ✅ |
| 32 | PositionPEOCreationDate | CREATION_DATE | — | ✅ |
| 33 | PositionPEODelegatePositionId | DELEGATE_POSITION_ID | — | ✅ |
| 34 | PositionPEOEntryGradeId | ENTRY_GRADE_ID | — | ✅ |
| 35 | PositionPEOEntryStepId | ENTRY_STEP_ID | — | ✅ |
| 36 | PositionPEOFrequency | FREQUENCY | — | ✅ |
| 37 | PositionPEOFte | FTE | — | ✅ |
| 38 | PositionPEOFullPartTime | FULL_PART_TIME | — | ✅ |
| 39 | PositionPEOFundedByExistingPosition | FUNDED_BY_EXISTING_POSITION | — | ✅ |
| 40 | PositionPEOGradeLadderId | GRADE_LADDER_ID | — | — |
| 41 | PositionPEOHiringStatus | HIRING_STATUS | — | ✅ |
| 42 | PositionPEOJobId | JOB_ID | — | ✅ |
| 43 | PositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | PositionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | PositionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | PositionPEOLocationId | LOCATION_ID | — | ✅ |
| 47 | PositionPEOMaxPersons | MAX_PERSONS | — | ✅ |
| 48 | PositionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | PositionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 50 | PositionPEOOverlapAllowed | OVERLAP_ALLOWED | — | ✅ |
| 51 | PositionPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | ✅ |
| 52 | PositionPEOPositionCode | POSITION_CODE | — | ✅ |
| 53 | PositionPEOPositionSynchronizationFlag | POSITION_SYNCHRONIZATION_FLAG | — | ✅ |
| 54 | PositionPEOPositionType | POSITION_TYPE | — | ✅ |
| 55 | PositionPEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 56 | PositionPEOProbationPeriodUnitCd | PROBATION_PERIOD_UNIT_CD | — | ✅ |
| 57 | PositionPEORequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | ✅ |
| 58 | PositionPEOSeasonalEndDate | SEASONAL_END_DATE | — | ✅ |
| 59 | PositionPEOSeasonalFlag | SEASONAL_FLAG | — | ✅ |
| 60 | PositionPEOSeasonalStartDate | SEASONAL_START_DATE | — | ✅ |
| 61 | PositionPEOSecurityClearance | SECURITY_CLEARANCE | — | ✅ |
| 62 | PositionPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | ✅ |
| 63 | PositionPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | ✅ |
| 64 | PositionPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 65 | PositionPEOSupervisorAssignmentId | SUPERVISOR_ASSIGNMENT_ID | — | ✅ |
| 66 | PositionPEOSupervisorId | SUPERVISOR_ID | — | ✅ |
| 67 | PositionPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 68 | PositionPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 69 | PositionPEOUnionId | UNION_ID | — | — |
| 70 | PositionPEOWorkingHours | WORKING_HOURS | — | ✅ |

### [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DelegatePositionTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DelegatePositionTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DelegatePositionTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | DelegatePositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DelegatePositionTranslationPEOName | NAME | — | ✅ |
| 6 | DelegatePositionTranslationPEOPositionId | POSITION_ID | — | — |
| 7 | ParentPositionTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ParentPositionTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | ParentPositionTranslationPEOLanguage | LANGUAGE | — | — |
| 10 | ParentPositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ParentPositionTranslationPEOName | NAME | — | ✅ |
| 12 | ParentPositionTranslationPEOPositionId | POSITION_ID | — | — |
| 13 | PositionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 14 | PositionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 15 | PositionTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | PositionTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 17 | PositionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 18 | PositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | PositionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | PositionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | PositionTranslationPEOName | NAME | — | ✅ |
| 22 | PositionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | PositionTranslationPEOPositionId | POSITION_ID | — | — |
| 24 | PositionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DelegatePositionOrgUnitTlPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | DelegatePositionOrgUnitTlPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | DelegatePositionOrgUnitTlPEOLanguage | LANGUAGE | — | — |
| 4 | DelegatePositionOrgUnitTlPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DelegatePositionOrgUnitTlPEOName | NAME | — | ✅ |
| 6 | DelegatePositionOrgUnitTlPEOOrganizationId | ORGANIZATION_ID | — | — |
| 7 | ParentPositionOrgUnitTlPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ParentPositionOrgUnitTlPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | ParentPositionOrgUnitTlPEOLanguage | LANGUAGE | — | — |
| 10 | ParentPositionOrgUnitTlPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ParentPositionOrgUnitTlPEOName | NAME | — | ✅ |
| 12 | ParentPositionOrgUnitTlPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[irc_requisitions_b|IRC_REQUISITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | RequisitionBPEORequisitionId | REQUISITION_ID | — | — |
| 3 | RequisitionBPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |

### [[irc_requisitions_tl|IRC_REQUISITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionTranslatePEOLanguage | LANGUAGE | — | — |
| 2 | RequisitionTranslatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | RequisitionTranslatePEORequisitionId | REQUISITION_ID | — | — |
| 4 | RequisitionTranslatePEOTitle | TITLE | — | ✅ |

### [[per_action_occurrences|PER_ACTION_OCCURRENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrencesPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | ActionOccurrencesPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionOccurrencesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsPEOActionReasonId | ACTION_REASON_ID | — | — |
| 2 | ActionReasonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsTranslationPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ActionReasonsTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonsTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_job_evaluations|PER_JOB_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobEvaluationPEOAccountability | ACCOUNTABILITY | — | ✅ |
| 2 | JobEvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | JobEvaluationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | JobEvaluationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | JobEvaluationPEODateEvaluated | DATE_EVALUATED | — | ✅ |
| 6 | JobEvaluationPEOEvaluationSystem | EVALUATION_SYSTEM | — | ✅ |
| 7 | JobEvaluationPEOJobEvaluationId | JOB_EVALUATION_ID | — | ✅ |
| 8 | JobEvaluationPEOJobId | JOB_ID | — | — |
| 9 | JobEvaluationPEOKnowhow | KNOWHOW | — | ✅ |
| 10 | JobEvaluationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | JobEvaluationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | JobEvaluationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | JobEvaluationPEOMeasuredIn | MEASURED_IN | — | ✅ |
| 14 | JobEvaluationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | JobEvaluationPEOOverallScore | OVERALL_SCORE | — | ✅ |
| 16 | JobEvaluationPEOPositionId | POSITION_ID | — | — |
| 17 | JobEvaluationPEOProblemSolving | PROBLEM_SOLVING | — | ✅ |
| 18 | JobEvaluationPEOWorkingConditions | WORKING_CONDITIONS | — | — |

### [[per_position_hierarchy_f|PER_POSITION_HIERARCHY_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionHierarchyPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | PositionHierarchyPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | PositionHierarchyPEOCreatedBy | CREATED_BY | — | — |
| 4 | PositionHierarchyPEOCreationDate | CREATION_DATE | — | — |
| 5 | PositionHierarchyPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 6 | PositionHierarchyPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PositionHierarchyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PositionHierarchyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PositionHierarchyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PositionHierarchyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PositionHierarchyPEOParentPositionId | PARENT_POSITION_ID | — | — |
| 12 | PositionHierarchyPEOPositionHierarchyId | POSITION_HIERARCHY_ID | — | — |
| 13 | PositionHierarchyPEOPositionId1 | POSITION_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
