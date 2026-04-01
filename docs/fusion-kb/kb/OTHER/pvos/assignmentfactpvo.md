---
id: DOC-OTHER-PVO-AssignmentFactPVO
doc_type: system-doc
title: "AssignmentFactPVO — PVO Cross-Module"
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
  - AssignmentFactPVO
  - assignmentfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentFactPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Fact. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_ASSIGN_WORK_MEASURES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 144 | 2 | 5 | 77 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 127 atributos (5 PKs, 73 BICC)
- [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]] — 17 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | AssignmentPEOActionCode | ACTION_CODE | — | ✅ |
| 3 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | AssignmentPEOAdjustedFte | ADJUSTED_FTE | — | — |
| 5 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | ✅ |
| 6 | AssignmentPEOAnnualWorkingDuration | ANNUAL_WORKING_DURATION | — | — |
| 7 | AssignmentPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 8 | AssignmentPEOAnnualWorkingRatio | ANNUAL_WORKING_RATIO | — | — |
| 9 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | ✅ |
| 10 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 11 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 12 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | ✅ |
| 13 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 14 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 15 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 16 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | ✅ |
| 17 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | ✅ |
| 18 | AssignmentPEOBillingTitle | BILLING_TITLE | — | ✅ |
| 19 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 20 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 21 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 22 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | ✅ |
| 23 | AssignmentPEOCategoryCode | CATEGORY_CODE | — | — |
| 24 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 25 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 26 | AssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | AssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | ✅ |
| 29 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 30 | AssignmentPEODutiesType | DUTIES_TYPE | — | ✅ |
| 31 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | ✅ |
| 32 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 33 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 34 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 35 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 36 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 37 | AssignmentPEOFrequency | FREQUENCY | — | ✅ |
| 38 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 39 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 40 | AssignmentPEOGspEligibilityFlag | GSP_ELIGIBILITY_FLAG | — | ✅ |
| 41 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | ✅ |
| 42 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 43 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | ✅ |
| 44 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | ✅ |
| 45 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | ✅ |
| 46 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | ✅ |
| 47 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | ✅ |
| 48 | AssignmentPEOJobId | JOB_ID | — | — |
| 49 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | ✅ |
| 50 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | ✅ |
| 51 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | AssignmentPEOLastWorkingDate | LAST_WORKING_DATE | — | — |
| 55 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 56 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 57 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | ✅ |
| 58 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 59 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | ✅ |
| 60 | AssignmentPEONormalHours | NORMAL_HOURS | — | ✅ |
| 61 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | ✅ |
| 62 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | ✅ |
| 63 | AssignmentPEONotificationDate | NOTIFICATION_DATE | — | — |
| 64 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 66 | AssignmentPEOOvertimePeriod | OVERTIME_PERIOD | — | — |
| 67 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 68 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 69 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 70 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 71 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 72 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 73 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 74 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 75 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 76 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | ✅ |
| 77 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 78 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | ✅ |
| 79 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 80 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | ✅ |
| 81 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | ✅ |
| 82 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 83 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | ✅ |
| 84 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | ✅ |
| 85 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | ✅ |
| 86 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | ✅ |
| 87 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | ✅ |
| 88 | AssignmentPEOReasonCode | REASON_CODE | — | ✅ |
| 89 | AssignmentPEORecordCreator | RECORD_CREATOR | — | ✅ |
| 90 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 91 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 92 | AssignmentPEORehireAuthorizerPersonId | REHIRE_AUTHORIZER_PERSON_ID | — | — |
| 93 | AssignmentPEORehireReason | REHIRE_REASON | — | — |
| 94 | AssignmentPEORehireRecommendation | REHIRE_RECOMMENDATION | — | — |
| 95 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | ✅ |
| 96 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | ✅ |
| 97 | AssignmentPEOReviewUserAccess | REVIEW_USER_ACCESS | — | — |
| 98 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | ✅ |
| 99 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | ✅ |
| 100 | AssignmentPEOSeniorityBasis | SENIORITY_BASIS | — | ✅ |
| 101 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 102 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 103 | AssignmentPEOSourceAssignmentId | SOURCE_ASSIGNMENT_ID | — | ✅ |
| 104 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 105 | AssignmentPEOSourceType | SOURCE_TYPE | — | ✅ |
| 106 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 107 | AssignmentPEOStandardFrequency | STANDARD_FREQUENCY | — | — |
| 108 | AssignmentPEOStandardHours | STANDARD_HOURS | — | — |
| 109 | AssignmentPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 110 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | ✅ |
| 111 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |
| 112 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 113 | AssignmentPEOTerminationDate | TERMINATION_DATE | — | — |
| 114 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 115 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 116 | AssignmentPEOUnionId | UNION_ID | — | — |
| 117 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 118 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | ✅ |
| 119 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | ✅ |
| 120 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 121 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 122 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | ✅ |
| 123 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | ✅ |
| 124 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 125 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | 🔑 | ✅ |
| 126 | EffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 127 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_assign_work_measures_f|PER_ASSIGN_WORK_MEASURES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentWorkMeasurePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | AssignmentWorkMeasurePEOAddsToBudget | ADDS_TO_BUDGET | — | — |
| 3 | AssignmentWorkMeasurePEOAssignWorkMeasureId | ASSIGN_WORK_MEASURE_ID | — | — |
| 4 | AssignmentWorkMeasurePEOAssignmentId | ASSIGNMENT_ID | — | — |
| 5 | AssignmentWorkMeasurePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | AssignmentWorkMeasurePEOCreatedBy | CREATED_BY | — | — |
| 7 | AssignmentWorkMeasurePEOCreationDate | CREATION_DATE | — | — |
| 8 | AssignmentWorkMeasurePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | AssignmentWorkMeasurePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | AssignmentWorkMeasurePEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 11 | AssignmentWorkMeasurePEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 12 | AssignmentWorkMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | AssignmentWorkMeasurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | AssignmentWorkMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | AssignmentWorkMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AssignmentWorkMeasurePEOUnit | UNIT | — | ✅ |
| 17 | AssignmentWorkMeasurePEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
