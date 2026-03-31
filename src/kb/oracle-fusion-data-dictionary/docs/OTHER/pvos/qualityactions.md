---
id: DOC-OTHER-PVO-QualityActions
doc_type: system-doc
title: "QualityActions — PVO Cross-Module"
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
  - QualityActions
  - qualityactions
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityActions

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Actions. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_USERS.

**Caminho:** `FscmTopModelAM.QualityActionsAnalyticsAM.QualityActions`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 131 | 2 | 0 | 3 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 BICC)
- [[per_users|PER_USERS]] — 22 atributos (1 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOActionCode | ACTION_CODE | — | — |
| 2 | AssignmentPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentPEOAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentPEOApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentPEOAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentPEOAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentPEOAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentPEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentPEOAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentPEOAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentPEOBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentPEOBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 16 | AssignmentPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 17 | AssignmentPEOCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentPEOCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentPEOContractId | CONTRACT_ID | — | — |
| 21 | AssignmentPEOCreatedBy | CREATED_BY | — | — |
| 22 | AssignmentPEOCreationDate | CREATION_DATE | — | — |
| 23 | AssignmentPEODateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentPEODefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentPEODutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 28 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 29 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | AssignmentPEOEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 31 | AssignmentPEOEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 32 | AssignmentPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 33 | AssignmentPEOExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 34 | AssignmentPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 35 | AssignmentPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 36 | AssignmentPEOFrequency | FREQUENCY | — | — |
| 37 | AssignmentPEOFullPartTime | FULL_PART_TIME | — | — |
| 38 | AssignmentPEOGradeId | GRADE_ID | — | — |
| 39 | AssignmentPEOGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 40 | AssignmentPEOHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 41 | AssignmentPEOIdFlexNum | ID_FLEX_NUM | — | — |
| 42 | AssignmentPEOInternalBuilding | INTERNAL_BUILDING | — | — |
| 43 | AssignmentPEOInternalFloor | INTERNAL_FLOOR | — | — |
| 44 | AssignmentPEOInternalLocation | INTERNAL_LOCATION | — | — |
| 45 | AssignmentPEOInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 46 | AssignmentPEOInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 47 | AssignmentPEOJobId | JOB_ID | — | — |
| 48 | AssignmentPEOJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 49 | AssignmentPEOLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 50 | AssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | AssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | AssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 54 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 55 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 56 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 57 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 58 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 59 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 60 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 61 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 63 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 64 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 65 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 66 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 67 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 68 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 69 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 70 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 71 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 72 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 73 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 74 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 75 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 76 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 77 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 78 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 79 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 80 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 81 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 82 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 83 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 84 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 85 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 86 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 87 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 88 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 89 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 90 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 91 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 92 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 93 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 94 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 95 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 96 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 97 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 98 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 99 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 100 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 101 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 102 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 103 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 104 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 105 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 106 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 107 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 108 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 109 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | UserPEOCreatedBy | CREATED_BY | — | — |
| 3 | UserPEOCreationDate | CREATION_DATE | — | — |
| 4 | UserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 5 | UserPEOEndDate | END_DATE | — | — |
| 6 | UserPEOExternalId | EXTERNAL_ID | — | — |
| 7 | UserPEOHrTerminated | HR_TERMINATED | — | — |
| 8 | UserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | UserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | UserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | UserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 12 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | UserPEOPartyId | PARTY_ID | — | — |
| 14 | UserPEOPersonId | PERSON_ID | — | — |
| 15 | UserPEOStartDate | START_DATE | — | — |
| 16 | UserPEOSuspended | SUSPENDED | — | — |
| 17 | UserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 18 | UserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 19 | UserPEOUserGuid | USER_GUID | — | — |
| 20 | UserPEOUserId | USER_ID | — | — |
| 21 | UserPEOUserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 22 | UserPEOUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
