---
id: DOC-OTHER-PVO-PrimaryAssignmentPVO
doc_type: system-doc
title: "PrimaryAssignmentPVO — PVO Cross-Module"
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
  - PrimaryAssignmentPVO
  - primaryassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrimaryAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Primary Assignment. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_ASSIGN_GRADE_STEPS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.PrimaryAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 126 | 2 | 5 | 9 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 122 atributos (5 PKs, 9 BICC)
- [[per_assign_grade_steps_f|PER_ASSIGN_GRADE_STEPS_F]] — 4 atributos

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | AssignmentPEOActionCode | ACTION_CODE | — | — |
| 3 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | AssignmentPEOAdjustedFte | ADJUSTED_FTE | — | — |
| 5 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 6 | AssignmentPEOAnnualWorkingDuration | ANNUAL_WORKING_DURATION | — | — |
| 7 | AssignmentPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 8 | AssignmentPEOAnnualWorkingRatio | ANNUAL_WORKING_RATIO | — | — |
| 9 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | — |
| 10 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 11 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 12 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 13 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 14 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 15 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 16 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 17 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 18 | AssignmentPEOBillingTitle | BILLING_TITLE | — | — |
| 19 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 20 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 21 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 22 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 23 | AssignmentPEOCategoryCode | CATEGORY_CODE | — | — |
| 24 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 25 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 26 | AssignmentPEOCreatedBy | CREATED_BY | — | — |
| 27 | AssignmentPEOCreationDate | CREATION_DATE | — | — |
| 28 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 29 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 30 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 31 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 32 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 33 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 34 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 35 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 36 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 37 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 38 | AssignmentPEOFullPartTime | FULL_PART_TIME | — | — |
| 39 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 40 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 41 | AssignmentPEOGspEligibilityFlag | GSP_ELIGIBILITY_FLAG | — | — |
| 42 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 43 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 44 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 45 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 46 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 47 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 48 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 49 | AssignmentPEOJobId | JOB_ID | — | — |
| 50 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 51 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 52 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 56 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 57 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 58 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 59 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 60 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 61 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 62 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 63 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 65 | AssignmentPEOOvertimePeriod | OVERTIME_PERIOD | — | — |
| 66 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 67 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 68 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 69 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 70 | AssignmentPEOPersonId | PERSON_ID | — | ✅ |
| 71 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 72 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 73 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 74 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 75 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 76 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 77 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 78 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 79 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 80 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 81 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 82 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 83 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 84 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 85 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 86 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 87 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 88 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 89 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 90 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 91 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 92 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 93 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 94 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 95 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 96 | AssignmentPEOSeniorityBasis | SENIORITY_BASIS | — | — |
| 97 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 98 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 99 | AssignmentPEOSourceAssignmentId | SOURCE_ASSIGNMENT_ID | — | — |
| 100 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 101 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 102 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 103 | AssignmentPEOStandardFrequency | STANDARD_FREQUENCY | — | — |
| 104 | AssignmentPEOStandardHours | STANDARD_HOURS | — | — |
| 105 | AssignmentPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 106 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 107 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 108 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 109 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 110 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 111 | AssignmentPEOUnionId | UNION_ID | — | — |
| 112 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 113 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 114 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 115 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 116 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 117 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 118 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |
| 119 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 120 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | 🔑 | ✅ |
| 121 | EffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 122 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_assign_grade_steps_f|PER_ASSIGN_GRADE_STEPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentGradeStepPEOAssignGradeStepId | ASSIGN_GRADE_STEP_ID | — | — |
| 2 | AssignmentGradeStepPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentGradeStepPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AssignmentGradeStepPEOGradeStepId | GRADE_STEP_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
