---
id: DOC-OTHER-PVO-PersonManagerHierarchyAssignmentPVO
doc_type: system-doc
title: "PersonManagerHierarchyAssignmentPVO — PVO Cross-Module"
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
  - PersonManagerHierarchyAssignmentPVO
  - personmanagerhierarchyassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonManagerHierarchyAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Manager Hierarchy Assignment. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_ASSIGNMENT_SUPERVISORS_F, PER_JOBS_F (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ManagerHierarchyAM.PersonManagerHierarchyAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 177 | 4 | 2 | 26 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 107 atributos (2 PKs, 15 BICC)
- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 20 atributos (4 BICC)
- [[per_jobs_f|PER_JOBS_F]] — 23 atributos (3 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 27 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | AssignmentPEOActionCode | ACTION_CODE | — | — |
| 3 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 5 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | — |
| 6 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentPEOBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 16 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 17 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 21 | AssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | AssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 27 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 28 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 29 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 30 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 31 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 32 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 33 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 34 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 35 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 36 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 37 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 38 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 39 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 40 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 41 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 42 | AssignmentPEOJobId | JOB_ID | — | — |
| 43 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 44 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 45 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 49 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 50 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 51 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 52 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 53 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 54 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 55 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 56 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 58 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 59 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 60 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 61 | AssignmentPEOPersonId | PERSON_ID | 🔑 | ✅ |
| 62 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 63 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 64 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 65 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 66 | AssignmentPEOPositionId | POSITION_ID | — | ✅ |
| 67 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 68 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 69 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 70 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 71 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 72 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 73 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 74 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 75 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 76 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 77 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 78 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 79 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 80 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 81 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 82 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 83 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 84 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 85 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 86 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 87 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 88 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 89 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 90 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 91 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 92 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 93 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 94 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 95 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 96 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 97 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 98 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 99 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 100 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 101 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 102 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 103 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |
| 104 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 105 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | ✅ |
| 106 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 107 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | AssignmentSupervisorPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | AssignmentSupervisorPEOAssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | — | — |
| 4 | AssignmentSupervisorPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | AssignmentSupervisorPEOCreatedBy | CREATED_BY | — | — |
| 6 | AssignmentSupervisorPEOCreationDate | CREATION_DATE | — | — |
| 7 | AssignmentSupervisorPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | AssignmentSupervisorPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | AssignmentSupervisorPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 10 | AssignmentSupervisorPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 11 | AssignmentSupervisorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignmentSupervisorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AssignmentSupervisorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AssignmentSupervisorPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 15 | AssignmentSupervisorPEOManagerId | MANAGER_ID | — | ✅ |
| 16 | AssignmentSupervisorPEOManagerType | MANAGER_TYPE | — | ✅ |
| 17 | AssignmentSupervisorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | AssignmentSupervisorPEOPersonId | PERSON_ID | — | — |
| 19 | AssignmentSupervisorPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 20 | AssignmentSupervisorPEOWorkingPercentage | WORKING_PERCENTAGE | — | — |

### [[per_jobs_f|PER_JOBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | JobPEOActiveStatus | ACTIVE_STATUS | — | — |
| 3 | JobPEOApprovalAuthority | APPROVAL_AUTHORITY | — | — |
| 4 | JobPEOBenchmarkJobFlag | BENCHMARK_JOB_FLAG | — | — |
| 5 | JobPEOBenchmarkJobId | BENCHMARK_JOB_ID | — | — |
| 6 | JobPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | JobPEOCreatedBy | CREATED_BY | — | — |
| 8 | JobPEOCreationDate | CREATION_DATE | — | — |
| 9 | JobPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | JobPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | JobPEOFullPartTime | FULL_PART_TIME | — | — |
| 12 | JobPEOJobCode | JOB_CODE | — | — |
| 13 | JobPEOJobFamilyId | JOB_FAMILY_ID | — | — |
| 14 | JobPEOJobFunctionCode | JOB_FUNCTION_CODE | — | — |
| 15 | JobPEOJobId | JOB_ID | — | ✅ |
| 16 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | JobPEOManagerLevel | MANAGER_LEVEL | — | — |
| 20 | JobPEOMedCheckupReq | MED_CHECKUP_REQ | — | — |
| 21 | JobPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | JobPEORegularTemporary | REGULAR_TEMPORARY | — | — |
| 23 | JobPEOSetId | SET_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PersonNamePEOCreatedBy | CREATED_BY | — | — |
| 3 | PersonNamePEOCreationDate | CREATION_DATE | — | — |
| 4 | PersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 5 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 8 | PersonNamePEOFullName | FULL_NAME | — | — |
| 9 | PersonNamePEOHonors | HONORS | — | — |
| 10 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 11 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 12 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | — |
| 16 | PersonNamePEOListName | LIST_NAME | — | — |
| 17 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 18 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 19 | PersonNamePEONameType | NAME_TYPE | — | — |
| 20 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 22 | PersonNamePEOPersonId | PERSON_ID | — | — |
| 23 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 24 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 25 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 26 | PersonNamePEOSuffix | SUFFIX | — | — |
| 27 | PersonNamePEOTitle | TITLE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
