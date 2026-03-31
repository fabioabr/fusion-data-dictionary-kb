---
id: DOC-HCM-PVO-AssignmentNoDePVO
doc_type: system-doc
title: "AssignmentNoDePVO — PVO Human Capital Management"
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
  - AssignmentNoDePVO
  - assignmentnodepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentNoDePVO

## 📌 Visão Geral

Disponibiliza assignments sem campos derivados (NoDE), com acao, rank e nome. Versao otimizada para consultas que nao requerem calculos derivados.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentNoDePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 1 | 5 | 71 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 125 atributos (5 PKs, 71 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | AssignmentNoDePEOActionCode | ACTION_CODE | — | ✅ |
| 3 | AssignmentNoDePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 4 | AssignmentNoDePEOAdjustedFte | ADJUSTED_FTE | — | — |
| 5 | AssignmentNoDePEOAnnualWorkingDuration | ANNUAL_WORKING_DURATION | — | — |
| 6 | AssignmentNoDePEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 7 | AssignmentNoDePEOAnnualWorkingRatio | ANNUAL_WORKING_RATIO | — | — |
| 8 | AssignmentNoDePEOApplicantRank | APPLICANT_RANK | — | ✅ |
| 9 | AssignmentNoDePEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 10 | AssignmentNoDePEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 11 | AssignmentNoDePEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | ✅ |
| 12 | AssignmentNoDePEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 13 | AssignmentNoDePEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | ✅ |
| 14 | AssignmentNoDePEOAssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 15 | AssignmentNoDePEOAutoEndFlag | AUTO_END_FLAG | — | ✅ |
| 16 | AssignmentNoDePEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | ✅ |
| 17 | AssignmentNoDePEOBillingTitle | BILLING_TITLE | — | ✅ |
| 18 | AssignmentNoDePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 19 | AssignmentNoDePEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 20 | AssignmentNoDePEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 21 | AssignmentNoDePEOCategoryCode | CATEGORY_CODE | — | — |
| 22 | AssignmentNoDePEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 23 | AssignmentNoDePEOContractId | CONTRACT_ID | — | — |
| 24 | AssignmentNoDePEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | AssignmentNoDePEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | AssignmentNoDePEODateProbationEnd | DATE_PROBATION_END | — | ✅ |
| 27 | AssignmentNoDePEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 28 | AssignmentNoDePEODutiesType | DUTIES_TYPE | — | ✅ |
| 29 | AssignmentNoDePEOEmployeeCategory | EMPLOYEE_CATEGORY | — | ✅ |
| 30 | AssignmentNoDePEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | ✅ |
| 31 | AssignmentNoDePEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 32 | AssignmentNoDePEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 33 | AssignmentNoDePEOFrequency | FREQUENCY | — | ✅ |
| 34 | AssignmentNoDePEOFullPartTime | FULL_PART_TIME | — | — |
| 35 | AssignmentNoDePEOGradeId | GRADE_ID | — | — |
| 36 | AssignmentNoDePEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 37 | AssignmentNoDePEOGspEligibilityFlag | GSP_ELIGIBILITY_FLAG | — | ✅ |
| 38 | AssignmentNoDePEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | ✅ |
| 39 | AssignmentNoDePEOIdFlexNum | ID_FLEX_NUM | — | — |
| 40 | AssignmentNoDePEOInternalBuilding | INTERNAL_BUILDING | — | ✅ |
| 41 | AssignmentNoDePEOInternalFloor | INTERNAL_FLOOR | — | ✅ |
| 42 | AssignmentNoDePEOInternalLocation | INTERNAL_LOCATION | — | ✅ |
| 43 | AssignmentNoDePEOInternalMailstop | INTERNAL_MAILSTOP | — | ✅ |
| 44 | AssignmentNoDePEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | ✅ |
| 45 | AssignmentNoDePEOJobId | JOB_ID | — | — |
| 46 | AssignmentNoDePEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | ✅ |
| 47 | AssignmentNoDePEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | ✅ |
| 48 | AssignmentNoDePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | AssignmentNoDePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | AssignmentNoDePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | AssignmentNoDePEOLastWorkingDate | LAST_WORKING_DATE | — | — |
| 52 | AssignmentNoDePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 53 | AssignmentNoDePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 54 | AssignmentNoDePEOLinkageType | LINKAGE_TYPE | — | ✅ |
| 55 | AssignmentNoDePEOLocationId | LOCATION_ID | — | — |
| 56 | AssignmentNoDePEOManagerFlag | MANAGER_FLAG | — | ✅ |
| 57 | AssignmentNoDePEONormalHours | NORMAL_HOURS | — | ✅ |
| 58 | AssignmentNoDePEONoticePeriod | NOTICE_PERIOD | — | ✅ |
| 59 | AssignmentNoDePEONoticePeriodUom | NOTICE_PERIOD_UOM | — | ✅ |
| 60 | AssignmentNoDePEONotificationDate | NOTIFICATION_DATE | — | — |
| 61 | AssignmentNoDePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | AssignmentNoDePEOOrganizationId | ORGANIZATION_ID | — | — |
| 63 | AssignmentNoDePEOOvertimePeriod | OVERTIME_PERIOD | — | — |
| 64 | AssignmentNoDePEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 65 | AssignmentNoDePEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 66 | AssignmentNoDePEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 67 | AssignmentNoDePEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 68 | AssignmentNoDePEOPersonId | PERSON_ID | — | — |
| 69 | AssignmentNoDePEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 70 | AssignmentNoDePEOPersonTypeId | PERSON_TYPE_ID | — | ✅ |
| 71 | AssignmentNoDePEOPoHeaderId | PO_HEADER_ID | — | — |
| 72 | AssignmentNoDePEOPoLineId | PO_LINE_ID | — | — |
| 73 | AssignmentNoDePEOPositionId | POSITION_ID | — | — |
| 74 | AssignmentNoDePEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | ✅ |
| 75 | AssignmentNoDePEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 76 | AssignmentNoDePEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | ✅ |
| 77 | AssignmentNoDePEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 78 | AssignmentNoDePEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | ✅ |
| 79 | AssignmentNoDePEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | ✅ |
| 80 | AssignmentNoDePEOProbationPeriod | PROBATION_PERIOD | — | ✅ |
| 81 | AssignmentNoDePEOProbationUnit | PROBATION_UNIT | — | ✅ |
| 82 | AssignmentNoDePEOProjectTitle | PROJECT_TITLE | — | ✅ |
| 83 | AssignmentNoDePEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | ✅ |
| 84 | AssignmentNoDePEOProjectedStartDate | PROJECTED_START_DATE | — | ✅ |
| 85 | AssignmentNoDePEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | ✅ |
| 86 | AssignmentNoDePEOReasonCode | REASON_CODE | — | ✅ |
| 87 | AssignmentNoDePEORecordCreator | RECORD_CREATOR | — | ✅ |
| 88 | AssignmentNoDePEORecruiterId | RECRUITER_ID | — | — |
| 89 | AssignmentNoDePEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 90 | AssignmentNoDePEORehireAuthorizerPersonId | REHIRE_AUTHORIZER_PERSON_ID | — | — |
| 91 | AssignmentNoDePEORehireReason | REHIRE_REASON | — | — |
| 92 | AssignmentNoDePEORehireRecommendation | REHIRE_RECOMMENDATION | — | — |
| 93 | AssignmentNoDePEORetirementAge | RETIREMENT_AGE | — | ✅ |
| 94 | AssignmentNoDePEORetirementDate | RETIREMENT_DATE | — | ✅ |
| 95 | AssignmentNoDePEOReviewUserAccess | REVIEW_USER_ACCESS | — | — |
| 96 | AssignmentNoDePEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | ✅ |
| 97 | AssignmentNoDePEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | ✅ |
| 98 | AssignmentNoDePEOSeniorityBasis | SENIORITY_BASIS | — | ✅ |
| 99 | AssignmentNoDePEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 100 | AssignmentNoDePEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 101 | AssignmentNoDePEOSourceAssignmentId | SOURCE_ASSIGNMENT_ID | — | ✅ |
| 102 | AssignmentNoDePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 103 | AssignmentNoDePEOSourceType | SOURCE_TYPE | — | ✅ |
| 104 | AssignmentNoDePEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 105 | AssignmentNoDePEOStandardFrequency | STANDARD_FREQUENCY | — | — |
| 106 | AssignmentNoDePEOStandardHours | STANDARD_HOURS | — | — |
| 107 | AssignmentNoDePEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 108 | AssignmentNoDePEOStepEntryDate | STEP_ENTRY_DATE | — | ✅ |
| 109 | AssignmentNoDePEOSystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |
| 110 | AssignmentNoDePEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 111 | AssignmentNoDePEOTerminationDate | TERMINATION_DATE | — | — |
| 112 | AssignmentNoDePEOTimeNormalFinish | TIME_NORMAL_FINISH | — | ✅ |
| 113 | AssignmentNoDePEOTimeNormalStart | TIME_NORMAL_START | — | ✅ |
| 114 | AssignmentNoDePEOUnionId | UNION_ID | — | — |
| 115 | AssignmentNoDePEOVacancyId | VACANCY_ID | — | — |
| 116 | AssignmentNoDePEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | ✅ |
| 117 | AssignmentNoDePEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | ✅ |
| 118 | AssignmentNoDePEOVendorId | VENDOR_ID | — | — |
| 119 | AssignmentNoDePEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 120 | AssignmentNoDePEOWorkAtHome | WORK_AT_HOME | — | ✅ |
| 121 | AssignmentNoDePEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | ✅ |
| 122 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 123 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | 🔑 | ✅ |
| 124 | EffectiveSequence | EFFECTIVE_SEQUENCE | 🔑 | ✅ |
| 125 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
