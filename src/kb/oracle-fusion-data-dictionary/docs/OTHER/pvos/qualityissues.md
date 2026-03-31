---
id: DOC-OTHER-PVO-QualityIssues
doc_type: system-doc
title: "QualityIssues — PVO Cross-Module"
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
  - QualityIssues
  - qualityissues
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityIssues

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Issues. Acessa as tabelas: ENQ_ISSUES_B, ENQ_ISSUES_TL, ENQ_ISSUE_WORKFLOW_DATES_V (+4).

**Caminho:** `FscmTopModelAM.QualityIssuesAnalyticsAM.QualityIssues`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 185 | 7 | 1 | 57 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[enq_issues_b|ENQ_ISSUES_B]] — 23 atributos (1 PKs, 23 BICC)
- [[enq_issues_tl|ENQ_ISSUES_TL]] — 7 atributos (7 BICC)
- [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]] — 4 atributos (4 BICC)
- [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]] — 15 atributos (15 BICC)
- [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]] — 5 atributos (5 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 BICC)
- [[per_users|PER_USERS]] — 22 atributos (1 BICC)

---

## ⚙️ Atributos

### [[enq_issues_b|ENQ_ISSUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignedTo | ASSIGNED_TO | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | CustomerId | CUSTOMER_ID | — | ✅ |
| 5 | Disposition | DISPOSITION | — | ✅ |
| 6 | Downtime | DOWNTIME | — | ✅ |
| 7 | ExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 8 | IsBaActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 9 | IsBaIssueId | ISSUE_ID | 🔑 | ✅ |
| 10 | IsBaIssueNumber | ISSUE_NUMBER | — | ✅ |
| 11 | IsBaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | IsBaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | IsBaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | IsBaLikelihoodOfRecurrence | LIKELIHOOD_OF_RECURRENCE | — | ✅ |
| 15 | IsBaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | IsBaOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | IsBaQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 18 | IsBaReportedBy | REPORTED_BY | — | ✅ |
| 19 | IsBaReportedDate | REPORTED_DATE | — | ✅ |
| 20 | IsBaSeverity | SEVERITY | — | ✅ |
| 21 | IsBaSource | SOURCE | — | ✅ |
| 22 | IsBaSupplierId | SUPPLIER_ID | — | ✅ |
| 23 | IsBaWorkflowStatusId | WORKFLOW_STATUS_ID | — | ✅ |

### [[enq_issues_tl|ENQ_ISSUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IsTlDescription | DESCRIPTION | — | ✅ |
| 2 | IsTlDispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 3 | IsTlIssueId | ISSUE_ID | — | ✅ |
| 4 | IsTlLanguage | LANGUAGE | — | ✅ |
| 5 | IsTlName | NAME | — | ✅ |
| 6 | IsTlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | IsTlSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IsDaApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | IsDaObjectPk1 | OBJECT_PK1 | — | ✅ |
| 3 | IsDaWorkflowCompletiondate | WORKFLOW_END_DATE | — | ✅ |
| 4 | IsDaWorkflowStartdate | WORKFLOW_START_DATE | — | ✅ |

### [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TypeBCode | CODE | — | ✅ |
| 2 | TypeBCreatedBy | CREATED_BY | — | ✅ |
| 3 | TypeBCreationDate | CREATION_DATE | — | ✅ |
| 4 | TypeBDisplayOrder | DISPLAY_ORDER | — | ✅ |
| 5 | TypeBInstantiationAllowed | INSTANTIATION_ALLOWED | — | ✅ |
| 6 | TypeBIsActive | IS_ACTIVE | — | ✅ |
| 7 | TypeBIsSeeded | IS_SEEDED | — | ✅ |
| 8 | TypeBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TypeBLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TypeBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TypeBObjectType | OBJECT_TYPE | — | ✅ |
| 12 | TypeBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | TypeBParentQualityTypeId | PARENT_QUALITY_TYPE_ID | — | ✅ |
| 14 | TypeBQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 15 | TypeBSource | SOURCE | — | ✅ |

### [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TypeTLanguage | LANGUAGE | — | ✅ |
| 2 | TypeTlDescription | DESCRIPTION | — | ✅ |
| 3 | TypeTlLabel | LABEL | — | ✅ |
| 4 | TypeTlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 5 | TypeTlQualityTypeIdQualityTypeId | QUALITY_TYPE_ID | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentActionCode | ACTION_CODE | — | — |
| 2 | AssignmentActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 16 | AssignmentBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 17 | AssignmentCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentContractId | CONTRACT_ID | — | — |
| 21 | AssignmentCreatedBy1 | CREATED_BY | — | — |
| 22 | AssignmentCreationDate1 | CREATION_DATE | — | — |
| 23 | AssignmentDateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentDefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentDutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 28 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 29 | AssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | AssignmentEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 31 | AssignmentEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 32 | AssignmentEstablishmentId | ESTABLISHMENT_ID | — | — |
| 33 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 34 | AssignmentFreezeStartDate | FREEZE_START_DATE | — | — |
| 35 | AssignmentFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 36 | AssignmentFrequency | FREQUENCY | — | — |
| 37 | AssignmentFullPartTime | FULL_PART_TIME | — | — |
| 38 | AssignmentGradeId | GRADE_ID | — | — |
| 39 | AssignmentGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 40 | AssignmentHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 41 | AssignmentIdFlexNum | ID_FLEX_NUM | — | — |
| 42 | AssignmentInternalBuilding | INTERNAL_BUILDING | — | — |
| 43 | AssignmentInternalFloor | INTERNAL_FLOOR | — | — |
| 44 | AssignmentInternalLocation | INTERNAL_LOCATION | — | — |
| 45 | AssignmentInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 46 | AssignmentInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 47 | AssignmentJobId | JOB_ID | — | — |
| 48 | AssignmentJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 49 | AssignmentLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 50 | AssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | AssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | AssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 54 | AssignmentLegislationCode | LEGISLATION_CODE | — | — |
| 55 | AssignmentLinkageType | LINKAGE_TYPE | — | — |
| 56 | AssignmentLocationId | LOCATION_ID | — | — |
| 57 | AssignmentManagerFlag | MANAGER_FLAG | — | — |
| 58 | AssignmentNormalHours | NORMAL_HOURS | — | — |
| 59 | AssignmentNoticePeriod | NOTICE_PERIOD | — | — |
| 60 | AssignmentNoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 61 | AssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | AssignmentOrganizationId | ORGANIZATION_ID | — | — |
| 63 | AssignmentParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 64 | AssignmentPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 65 | AssignmentPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 66 | AssignmentPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 67 | AssignmentPersonId | PERSON_ID | — | — |
| 68 | AssignmentPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 69 | AssignmentPersonTypeId | PERSON_TYPE_ID | — | — |
| 70 | AssignmentPoHeaderId | PO_HEADER_ID | — | — |
| 71 | AssignmentPoLineId | PO_LINE_ID | — | — |
| 72 | AssignmentPositionId | POSITION_ID | — | — |
| 73 | AssignmentPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 74 | AssignmentPostingContentId | POSTING_CONTENT_ID | — | — |
| 75 | AssignmentPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 76 | AssignmentPrimaryFlag | PRIMARY_FLAG | — | — |
| 77 | AssignmentPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 78 | AssignmentPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 79 | AssignmentProbationPeriod | PROBATION_PERIOD | — | — |
| 80 | AssignmentProbationUnit | PROBATION_UNIT | — | — |
| 81 | AssignmentProjectTitle | PROJECT_TITLE | — | — |
| 82 | AssignmentProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 83 | AssignmentProjectedStartDate | PROJECTED_START_DATE | — | — |
| 84 | AssignmentProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 85 | AssignmentReasonCode | REASON_CODE | — | — |
| 86 | AssignmentRecordCreator | RECORD_CREATOR | — | — |
| 87 | AssignmentRecruiterId | RECRUITER_ID | — | — |
| 88 | AssignmentRecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 89 | AssignmentRetirementAge | RETIREMENT_AGE | — | — |
| 90 | AssignmentRetirementDate | RETIREMENT_DATE | — | — |
| 91 | AssignmentSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 92 | AssignmentSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 93 | AssignmentSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 94 | AssignmentSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 95 | AssignmentSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 96 | AssignmentSourceType | SOURCE_TYPE | — | — |
| 97 | AssignmentSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 98 | AssignmentStepEntryDate | STEP_ENTRY_DATE | — | — |
| 99 | AssignmentSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 100 | AssignmentTaxAddressId | TAX_ADDRESS_ID | — | — |
| 101 | AssignmentTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 102 | AssignmentTimeNormalStart | TIME_NORMAL_START | — | — |
| 103 | AssignmentVacancyId | VACANCY_ID | — | — |
| 104 | AssignmentVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 105 | AssignmentVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 106 | AssignmentVendorId | VENDOR_ID | — | — |
| 107 | AssignmentVendorSiteId | VENDOR_SITE_ID | — | — |
| 108 | AssignmentWorkAtHome | WORK_AT_HOME | — | — |
| 109 | AssignmentWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserActiveFlag | ACTIVE_FLAG | — | — |
| 2 | UserBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | UserCreatedBy1 | CREATED_BY | — | — |
| 4 | UserCreationDate1 | CREATION_DATE | — | — |
| 5 | UserCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | UserEndDate | END_DATE | — | — |
| 7 | UserExternalId | EXTERNAL_ID | — | — |
| 8 | UserHrTerminated | HR_TERMINATED | — | — |
| 9 | UserLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | UserLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | UserLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | UserMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | UserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | UserPartyId | PARTY_ID | — | — |
| 15 | UserPersonId | PERSON_ID | — | — |
| 16 | UserStartDate | START_DATE | — | — |
| 17 | UserSuspended | SUSPENDED | — | — |
| 18 | UserUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | UserUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | UserUserGuid | USER_GUID | — | — |
| 21 | UserUserId | USER_ID | — | — |
| 22 | UserUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
