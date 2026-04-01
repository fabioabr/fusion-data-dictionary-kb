---
id: DOC-HCM-PVO-PersonInfoPVOViewAll
doc_type: system-doc
title: "PersonInfoPVOViewAll — PVO Human Capital Management"
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
  - PersonInfoPVOViewAll
  - personinfopvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonInfoPVOViewAll

## 📌 Visão Geral

Versão ViewAll das informações de compensação do colaborador, sem restrições de segurança. Permite análise completa de dados salariais para planejamento de workforce compensation.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PersonInfoPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 171 | 1 | 1 | 152 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_person_info_v|CMP_CWB_PERSON_INFO_V]] — 171 atributos (1 PKs, 152 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_person_info_v|CMP_CWB_PERSON_INFO_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonEventId | PERSON_EVENT_ID | 🔑 | ✅ |
| 2 | PersonInformationPEOAccessCode | ACCESS_CODE | — | ✅ |
| 3 | PersonInformationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 4 | PersonInformationPEOAdjustedChangeAmount | ADJUSTED_CHANGE_AMOUNT | — | ✅ |
| 5 | PersonInformationPEOAdjustedSalaryCurrent | ADJUSTED_SALARY_CURRENT | — | ✅ |
| 6 | PersonInformationPEOAdjustedSalaryNew | ADJUSTED_SALARY_NEW | — | ✅ |
| 7 | PersonInformationPEOAdjustedSvcDate | ADJUSTED_SVC_DATE | — | ✅ |
| 8 | PersonInformationPEOAdjustmentFactor | ADJUSTMENT_FACTOR | — | ✅ |
| 9 | PersonInformationPEOApprovalCode | APPROVAL_CODE | — | ✅ |
| 10 | PersonInformationPEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 11 | PersonInformationPEOAssignmentAssignmentId | ASSIGNMENT_ASSIGNMENT_ID | — | — |
| 12 | PersonInformationPEOAssignmentChangeDate | ASSIGNMENT_CHANGE_DATE | — | ✅ |
| 13 | PersonInformationPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 14 | PersonInformationPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 15 | PersonInformationPEOAssignmentPostedDate | ASSIGNMENT_POSTED_DATE | — | ✅ |
| 16 | PersonInformationPEOAssignmentPostingDate | ASSIGNMENT_POSTING_DATE | — | ✅ |
| 17 | PersonInformationPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | ✅ |
| 18 | PersonInformationPEOBaseSalary | BASE_SALARY | — | ✅ |
| 19 | PersonInformationPEOBaseSalaryChangeDate | BASE_SALARY_CHANGE_DATE | — | ✅ |
| 20 | PersonInformationPEOBaseSalaryChangeVal | BASE_SALARY_CHANGE_VAL | — | ✅ |
| 21 | PersonInformationPEOBaseSalaryCurrency | BASE_SALARY_CURRENCY | — | ✅ |
| 22 | PersonInformationPEOBaseSalaryFrequency | BASE_SALARY_FREQUENCY | — | ✅ |
| 23 | PersonInformationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 24 | PersonInformationPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 25 | PersonInformationPEOCustomSegment1 | CUSTOM_SEGMENT1 | — | ✅ |
| 26 | PersonInformationPEOCustomSegment10 | CUSTOM_SEGMENT10 | — | ✅ |
| 27 | PersonInformationPEOCustomSegment11 | CUSTOM_SEGMENT11 | — | ✅ |
| 28 | PersonInformationPEOCustomSegment12 | CUSTOM_SEGMENT12 | — | ✅ |
| 29 | PersonInformationPEOCustomSegment13 | CUSTOM_SEGMENT13 | — | ✅ |
| 30 | PersonInformationPEOCustomSegment14 | CUSTOM_SEGMENT14 | — | ✅ |
| 31 | PersonInformationPEOCustomSegment15 | CUSTOM_SEGMENT15 | — | ✅ |
| 32 | PersonInformationPEOCustomSegment16 | CUSTOM_SEGMENT16 | — | ✅ |
| 33 | PersonInformationPEOCustomSegment17 | CUSTOM_SEGMENT17 | — | ✅ |
| 34 | PersonInformationPEOCustomSegment18 | CUSTOM_SEGMENT18 | — | ✅ |
| 35 | PersonInformationPEOCustomSegment19 | CUSTOM_SEGMENT19 | — | ✅ |
| 36 | PersonInformationPEOCustomSegment2 | CUSTOM_SEGMENT2 | — | ✅ |
| 37 | PersonInformationPEOCustomSegment20 | CUSTOM_SEGMENT20 | — | ✅ |
| 38 | PersonInformationPEOCustomSegment21 | CUSTOM_SEGMENT21 | — | ✅ |
| 39 | PersonInformationPEOCustomSegment22 | CUSTOM_SEGMENT22 | — | ✅ |
| 40 | PersonInformationPEOCustomSegment23 | CUSTOM_SEGMENT23 | — | ✅ |
| 41 | PersonInformationPEOCustomSegment24 | CUSTOM_SEGMENT24 | — | ✅ |
| 42 | PersonInformationPEOCustomSegment25 | CUSTOM_SEGMENT25 | — | ✅ |
| 43 | PersonInformationPEOCustomSegment26 | CUSTOM_SEGMENT26 | — | ✅ |
| 44 | PersonInformationPEOCustomSegment27 | CUSTOM_SEGMENT27 | — | ✅ |
| 45 | PersonInformationPEOCustomSegment28 | CUSTOM_SEGMENT28 | — | ✅ |
| 46 | PersonInformationPEOCustomSegment29 | CUSTOM_SEGMENT29 | — | ✅ |
| 47 | PersonInformationPEOCustomSegment3 | CUSTOM_SEGMENT3 | — | ✅ |
| 48 | PersonInformationPEOCustomSegment30 | CUSTOM_SEGMENT30 | — | ✅ |
| 49 | PersonInformationPEOCustomSegment31 | CUSTOM_SEGMENT31 | — | ✅ |
| 50 | PersonInformationPEOCustomSegment32 | CUSTOM_SEGMENT32 | — | ✅ |
| 51 | PersonInformationPEOCustomSegment33 | CUSTOM_SEGMENT33 | — | ✅ |
| 52 | PersonInformationPEOCustomSegment34 | CUSTOM_SEGMENT34 | — | ✅ |
| 53 | PersonInformationPEOCustomSegment35 | CUSTOM_SEGMENT35 | — | ✅ |
| 54 | PersonInformationPEOCustomSegment36 | CUSTOM_SEGMENT36 | — | ✅ |
| 55 | PersonInformationPEOCustomSegment37 | CUSTOM_SEGMENT37 | — | ✅ |
| 56 | PersonInformationPEOCustomSegment38 | CUSTOM_SEGMENT38 | — | ✅ |
| 57 | PersonInformationPEOCustomSegment39 | CUSTOM_SEGMENT39 | — | ✅ |
| 58 | PersonInformationPEOCustomSegment4 | CUSTOM_SEGMENT4 | — | ✅ |
| 59 | PersonInformationPEOCustomSegment40 | CUSTOM_SEGMENT40 | — | ✅ |
| 60 | PersonInformationPEOCustomSegment41 | CUSTOM_SEGMENT41 | — | ✅ |
| 61 | PersonInformationPEOCustomSegment42 | CUSTOM_SEGMENT42 | — | ✅ |
| 62 | PersonInformationPEOCustomSegment43 | CUSTOM_SEGMENT43 | — | ✅ |
| 63 | PersonInformationPEOCustomSegment44 | CUSTOM_SEGMENT44 | — | ✅ |
| 64 | PersonInformationPEOCustomSegment45 | CUSTOM_SEGMENT45 | — | ✅ |
| 65 | PersonInformationPEOCustomSegment46 | CUSTOM_SEGMENT46 | — | ✅ |
| 66 | PersonInformationPEOCustomSegment47 | CUSTOM_SEGMENT47 | — | ✅ |
| 67 | PersonInformationPEOCustomSegment48 | CUSTOM_SEGMENT48 | — | ✅ |
| 68 | PersonInformationPEOCustomSegment49 | CUSTOM_SEGMENT49 | — | ✅ |
| 69 | PersonInformationPEOCustomSegment5 | CUSTOM_SEGMENT5 | — | ✅ |
| 70 | PersonInformationPEOCustomSegment50 | CUSTOM_SEGMENT50 | — | ✅ |
| 71 | PersonInformationPEOCustomSegment6 | CUSTOM_SEGMENT6 | — | ✅ |
| 72 | PersonInformationPEOCustomSegment7 | CUSTOM_SEGMENT7 | — | ✅ |
| 73 | PersonInformationPEOCustomSegment8 | CUSTOM_SEGMENT8 | — | ✅ |
| 74 | PersonInformationPEOCustomSegment9 | CUSTOM_SEGMENT9 | — | ✅ |
| 75 | PersonInformationPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 76 | PersonInformationPEODisabilityStatus | DISABILITY_STATUS | — | ✅ |
| 77 | PersonInformationPEODoNotPostFlag | DO_NOT_POST_FLAG | — | ✅ |
| 78 | PersonInformationPEODueDate | DUE_DATE | — | ✅ |
| 79 | PersonInformationPEOEffectiveDate | EFFECTIVE_DATE | — | ✅ |
| 80 | PersonInformationPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 81 | PersonInformationPEOEmpStatusCode | EMP_STATUS_CODE | — | ✅ |
| 82 | PersonInformationPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 83 | PersonInformationPEOEthnicity | ETHNICITY | — | ✅ |
| 84 | PersonInformationPEOFrequency | FREQUENCY | — | ✅ |
| 85 | PersonInformationPEOFteAnnualChangeAmt | FTE_ANNUAL_CHANGE_AMT | — | ✅ |
| 86 | PersonInformationPEOFteAnnualSalaryCurrent | FTE_ANNUAL_SALARY_CURRENT | — | ✅ |
| 87 | PersonInformationPEOFteAnnualSalaryNew | FTE_ANNUAL_SALARY_NEW | — | ✅ |
| 88 | PersonInformationPEOFteAnnualizationFactor | FTE_ANNUALIZATION_FACTOR | — | — |
| 89 | PersonInformationPEOFteFactor | FTE_FACTOR | — | ✅ |
| 90 | PersonInformationPEOGradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | ✅ |
| 91 | PersonInformationPEOGradeAttribute1 | GRADE_ATTRIBUTE1 | — | ✅ |
| 92 | PersonInformationPEOGradeAttribute2 | GRADE_ATTRIBUTE2 | — | ✅ |
| 93 | PersonInformationPEOGradeAttribute3 | GRADE_ATTRIBUTE3 | — | ✅ |
| 94 | PersonInformationPEOGradeChangeDate | GRADE_CHANGE_DATE | — | ✅ |
| 95 | PersonInformationPEOGradeComparatio | GRADE_COMPARATIO | — | ✅ |
| 96 | PersonInformationPEOGradeDecile | GRADE_DECILE | — | ✅ |
| 97 | PersonInformationPEOGradeId | GRADE_ID | — | ✅ |
| 98 | PersonInformationPEOGradeMaxVal | GRADE_MAX_VAL | — | ✅ |
| 99 | PersonInformationPEOGradeMidPoint | GRADE_MID_POINT | — | ✅ |
| 100 | PersonInformationPEOGradeMinVal | GRADE_MIN_VAL | — | ✅ |
| 101 | PersonInformationPEOGradePctInRange | GRADE_PCT_IN_RANGE | — | ✅ |
| 102 | PersonInformationPEOGradeQuartile | GRADE_QUARTILE | — | ✅ |
| 103 | PersonInformationPEOGradeQuintile | GRADE_QUINTILE | — | ✅ |
| 104 | PersonInformationPEOGradeRateId | GRADE_RATE_ID | — | — |
| 105 | PersonInformationPEOJobAttribute1 | JOB_ATTRIBUTE1 | — | ✅ |
| 106 | PersonInformationPEOJobAttribute2 | JOB_ATTRIBUTE2 | — | ✅ |
| 107 | PersonInformationPEOJobAttribute3 | JOB_ATTRIBUTE3 | — | ✅ |
| 108 | PersonInformationPEOJobAttribute4 | JOB_ATTRIBUTE4 | — | ✅ |
| 109 | PersonInformationPEOJobAttribute5 | JOB_ATTRIBUTE5 | — | ✅ |
| 110 | PersonInformationPEOJobAttribute6 | JOB_ATTRIBUTE6 | — | ✅ |
| 111 | PersonInformationPEOJobChangeDate | JOB_CHANGE_DATE | — | ✅ |
| 112 | PersonInformationPEOJobId | JOB_ID | — | ✅ |
| 113 | PersonInformationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 114 | PersonInformationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 115 | PersonInformationPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 116 | PersonInformationPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 117 | PersonInformationPEOLocationId | LOCATION_ID | — | ✅ |
| 118 | PersonInformationPEOMgrOverrideDate | MGR_OVERRIDE_DATE | — | ✅ |
| 119 | PersonInformationPEOMgrStatusCode | MGR_STATUS_CODE | — | ✅ |
| 120 | PersonInformationPEONationality | NATIONALITY | — | ✅ |
| 121 | PersonInformationPEONewBaseSalary | NEW_BASE_SALARY | — | ✅ |
| 122 | PersonInformationPEONewGradeComparatio | NEW_GRADE_COMPARATIO | — | ✅ |
| 123 | PersonInformationPEONewGradeDecile | NEW_GRADE_DECILE | — | ✅ |
| 124 | PersonInformationPEONewGradePctInRange | NEW_GRADE_PCT_IN_RANGE | — | ✅ |
| 125 | PersonInformationPEONewGradeQuartile | NEW_GRADE_QUARTILE | — | ✅ |
| 126 | PersonInformationPEONewGradeQuintile | NEW_GRADE_QUINTILE | — | ✅ |
| 127 | PersonInformationPEONonDiscriminationCode | NON_DISCRIMINATION_CODE | — | ✅ |
| 128 | PersonInformationPEONormalHours | NORMAL_HOURS | — | ✅ |
| 129 | PersonInformationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 130 | PersonInformationPEOOriginalStartDate | ORIGINAL_START_DATE | — | ✅ |
| 131 | PersonInformationPEOPayAnnualizationFactor | PAY_ANNUALIZATION_FACTOR | — | ✅ |
| 132 | PersonInformationPEOPayrollId | PAYROLL_ID | — | ✅ |
| 133 | PersonInformationPEOPerformanceDate | PERFORMANCE_DATE | — | ✅ |
| 134 | PersonInformationPEOPerformanceRating | PERFORMANCE_RATING | — | ✅ |
| 135 | PersonInformationPEOPerformanceRatingDate | PERFORMANCE_RATING_DATE | — | ✅ |
| 136 | PersonInformationPEOPerformanceRatingType | PERFORMANCE_RATING_TYPE | — | ✅ |
| 137 | PersonInformationPEOPeriodCompType | PERIOD_COMP_TYPE | — | ✅ |
| 138 | PersonInformationPEOPeriodId | PERIOD_ID | — | — |
| 139 | PersonInformationPEOPersonId | PERSON_ID | — | ✅ |
| 140 | PersonInformationPEOPlaceholderFlag | PLACEHOLDER_FLAG | — | ✅ |
| 141 | PersonInformationPEOPlanId | PLAN_ID | — | — |
| 142 | PersonInformationPEOPlanPeriodId | PLAN_PERIOD_ID | — | — |
| 143 | PersonInformationPEOPositionChangeDate | POSITION_CHANGE_DATE | — | ✅ |
| 144 | PersonInformationPEOPositionId | POSITION_ID | — | — |
| 145 | PersonInformationPEOPriorSalary | PRIOR_SALARY | — | ✅ |
| 146 | PersonInformationPEOPriorSalaryChgPct | PRIOR_SALARY_CHG_PCT | — | — |
| 147 | PersonInformationPEOReassignmentDate | MGR_OVERRIDE_DATE | — | ✅ |
| 148 | PersonInformationPEOReassignmentMgrID | MGR_OVERRIDE_PERSON_ID | — | — |
| 149 | PersonInformationPEOReligion | RELIGION | — | ✅ |
| 150 | PersonInformationPEOReviewMgrID | RVW_MGR_PERSON_ID | — | — |
| 151 | PersonInformationPEORiskOfLoss | RISK_OF_LOSS | — | ✅ |
| 152 | PersonInformationPEOSalaryBasisId | SALARY_BASIS_ID | — | — |
| 153 | PersonInformationPEOSecondaryMgrID | SEC_MGR_PERSON_ID | — | — |
| 154 | PersonInformationPEOSex | SEX | — | ✅ |
| 155 | PersonInformationPEOStartDate | START_DATE | — | ✅ |
| 156 | PersonInformationPEOSubmitDate | SUBMIT_DATE | — | ✅ |
| 157 | PersonInformationPEOSupervisorId | SUPERVISOR_ID | — | — |
| 158 | PersonInformationPEOUserPreferredExchangeRate | USER_PREFERRED_EXCHANGE_RATE | — | ✅ |
| 159 | PersonInformationPEOVeteranStatus | VETERAN_STATUS | — | ✅ |
| 160 | PersonInformationPEOWorkTelephone | WORK_TELEPHONE | — | ✅ |
| 161 | PersonInformationPEOWorkerNumber | WORKER_NUMBER | — | ✅ |
| 162 | PersonInformationPEOWorkerPotential | WORKER_POTENTIAL | — | ✅ |
| 163 | PersonInformationPEOWorkingHours | WORKING_HOURS | — | ✅ |
| 164 | PersonInformationPEOWsMgrAssignmentId | WS_MGR_ASSIGNMENT_ID | — | — |
| 165 | PersonInformationPEOWsMgrPersonEventId | WS_MGR_PERSON_EVENT_ID | — | ✅ |
| 166 | PersonInformationPEOWsMgrPersonId | WS_MGR_PERSON_ID | — | ✅ |
| 167 | PersonInformationPEOXchgRate | XCHG_RATE | — | — |
| 168 | PersonInformationPEOYearsEmployed | YEARS_EMPLOYED | — | ✅ |
| 169 | PersonInformationPEOYearsInGrade | YEARS_IN_GRADE | — | ✅ |
| 170 | PersonInformationPEOYearsInJob | YEARS_IN_JOB | — | ✅ |
| 171 | PersonInformationPEOYearsInPosition | YEARS_IN_POSITION | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
