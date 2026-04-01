---
id: DOC-OTHER-PVO-QualityRelationships
doc_type: system-doc
title: "QualityRelationships — PVO Cross-Module"
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
  - QualityRelationships
  - qualityrelationships
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityRelationships

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Relationships. Acessa as tabelas: ACA_CS_REL_RULES, ENQ_ISSUES_VL, ENQ_ISSUE_RELATIONSHIP_V (+3).

**Caminho:** `FscmTopModelAM.QualityIssuesAnalyticsAM.QualityRelationships`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 225 | 6 | 1 | 98 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[aca_cs_rel_rules|ACA_CS_REL_RULES]] — 12 atributos (12 BICC)
- [[enq_issues_vl|ENQ_ISSUES_VL]] — 52 atributos (52 BICC)
- [[enq_issue_relationship_v|ENQ_ISSUE_RELATIONSHIP_V]] — 27 atributos (1 PKs, 27 BICC)
- [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]] — 4 atributos (4 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 108 atributos (2 BICC)
- [[per_users|PER_USERS]] — 22 atributos (1 BICC)

---

## ⚙️ Atributos

### [[aca_cs_rel_rules|ACA_CS_REL_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipRulesPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RelationshipRulesPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RelationshipRulesPEODestObjToStatusCode | DEST_OBJ_TO_STATUS_CODE | — | ✅ |
| 4 | RelationshipRulesPEODestObjType | DEST_OBJ_TYPE | — | ✅ |
| 5 | RelationshipRulesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RelationshipRulesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RelationshipRulesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RelationshipRulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RelationshipRulesPEORelationshipId | RELATIONSHIP_ID | — | ✅ |
| 10 | RelationshipRulesPEORelationshipRuleId | RELATIONSHIP_RULE_ID | — | ✅ |
| 11 | RelationshipRulesPEOSrcObjToStatusCode | SRC_OBJ_TO_STATUS_CODE | — | ✅ |
| 12 | RelationshipRulesPEOSrcObjType | SRC_OBJ_TYPE | — | ✅ |

### [[enq_issues_vl|ENQ_ISSUES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedIssuePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 2 | DerivedIssuePEOAssignedTo | ASSIGNED_TO | — | ✅ |
| 3 | DerivedIssuePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | DerivedIssuePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | DerivedIssuePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 6 | DerivedIssuePEODescription | DESCRIPTION | — | ✅ |
| 7 | DerivedIssuePEODisposition | DISPOSITION | — | ✅ |
| 8 | DerivedIssuePEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 9 | DerivedIssuePEODowntime | DOWNTIME | — | ✅ |
| 10 | DerivedIssuePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 11 | DerivedIssuePEOIssueId | ISSUE_ID | — | ✅ |
| 12 | DerivedIssuePEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 13 | DerivedIssuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | DerivedIssuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | DerivedIssuePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | DerivedIssuePEOLikelihoodOfRecurrence | LIKELIHOOD_OF_RECURRENCE | — | ✅ |
| 17 | DerivedIssuePEOName | NAME | — | ✅ |
| 18 | DerivedIssuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | DerivedIssuePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 20 | DerivedIssuePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 21 | DerivedIssuePEOReportedBy | REPORTED_BY | — | ✅ |
| 22 | DerivedIssuePEOReportedDate | REPORTED_DATE | — | ✅ |
| 23 | DerivedIssuePEOSeverity | SEVERITY | — | ✅ |
| 24 | DerivedIssuePEOSource | SOURCE | — | ✅ |
| 25 | DerivedIssuePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 26 | DerivedIssuePEOWorkflowStatusId | WORKFLOW_STATUS_ID | — | ✅ |
| 27 | DrivingIssueExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 28 | DrivingIssuePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 29 | DrivingIssuePEOAssignedTo | ASSIGNED_TO | — | ✅ |
| 30 | DrivingIssuePEOCreatedBy | CREATED_BY | — | ✅ |
| 31 | DrivingIssuePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 32 | DrivingIssuePEODescription | DESCRIPTION | — | ✅ |
| 33 | DrivingIssuePEODisposition | DISPOSITION | — | ✅ |
| 34 | DrivingIssuePEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 35 | DrivingIssuePEODowntime | DOWNTIME | — | ✅ |
| 36 | DrivingIssuePEOIssueId | ISSUE_ID | — | ✅ |
| 37 | DrivingIssuePEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 38 | DrivingIssuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | DrivingIssuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | DrivingIssuePEOLastUpdatedDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | DrivingIssuePEOLikelihoodOfRecurrence | LIKELIHOOD_OF_RECURRENCE | — | ✅ |
| 42 | DrivingIssuePEOName | NAME | — | ✅ |
| 43 | DrivingIssuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | DrivingIssuePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 45 | DrivingIssuePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 46 | DrivingIssuePEOReportedBy | REPORTED_BY | — | ✅ |
| 47 | DrivingIssuePEOReportedDate | REPORTED_DATE | — | ✅ |
| 48 | DrivingIssuePEOSeverity | SEVERITY | — | ✅ |
| 49 | DrivingIssuePEOSource | SOURCE | — | ✅ |
| 50 | DrivingIssuePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 51 | DrivingIssuePEOWorkflowStatusId | WORKFLOW_STATUS_ID | — | ✅ |
| 52 | DrivingIssuePEOcreationDate | CREATION_DATE | — | ✅ |

### [[enq_issue_relationship_v|ENQ_ISSUE_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueRelationshipPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | IssueRelationshipPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | IssueRelationshipPEODerivedActionId | DERIVED_ACTION_ID | — | ✅ |
| 4 | IssueRelationshipPEODerivedChangeId | DERIVED_CHANGE_ID | — | ✅ |
| 5 | IssueRelationshipPEODerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 6 | IssueRelationshipPEODerivedConceptId | DERIVED_CONCEPT_ID | — | ✅ |
| 7 | IssueRelationshipPEODerivedIdeaId | DERIVED_IDEA_ID | — | ✅ |
| 8 | IssueRelationshipPEODerivedItemId | DERIVED_ITEM_ID | — | ✅ |
| 9 | IssueRelationshipPEODerivedItemId1 | DERIVED_ITEM_ID1 | — | ✅ |
| 10 | IssueRelationshipPEODerivedProposalId | DERIVED_PROPOSAL_ID | — | ✅ |
| 11 | IssueRelationshipPEODerivedRequirementId | DERIVED_REQUIREMENT_ID | — | ✅ |
| 12 | IssueRelationshipPEODerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 13 | IssueRelationshipPEODestObjId | DEST_OBJ_ID | — | ✅ |
| 14 | IssueRelationshipPEODestObjPk2value | DEST_OBJ_PK2VALUE | — | ✅ |
| 15 | IssueRelationshipPEODestObjType | DEST_OBJ_TYPE | — | ✅ |
| 16 | IssueRelationshipPEODirectionType | DIRECTION_TYPE | — | ✅ |
| 17 | IssueRelationshipPEOFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 18 | IssueRelationshipPEOFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 19 | IssueRelationshipPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | IssueRelationshipPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | IssueRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | IssueRelationshipPEORelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 23 | IssueRelationshipPEORelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 24 | IssueRelationshipPEOSrcObjId | SRC_OBJ_ID | — | ✅ |
| 25 | IssueRelationshipPEOSrcObjPk2value | SRC_OBJ_PK2VALUE | — | ✅ |
| 26 | IssueRelationshipPEOSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 27 | IssueRelationshipPEOTargetType | TARGET_TYPE | — | ✅ |

### [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | IssueDatesPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 3 | IssueDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | ✅ |
| 4 | IssueDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | ✅ |

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
| 52 | AssignmentPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 53 | AssignmentPEOLegislationCode | LEGISLATION_CODE | — | — |
| 54 | AssignmentPEOLinkageType | LINKAGE_TYPE | — | — |
| 55 | AssignmentPEOLocationId | LOCATION_ID | — | — |
| 56 | AssignmentPEOManagerFlag | MANAGER_FLAG | — | — |
| 57 | AssignmentPEONormalHours | NORMAL_HOURS | — | — |
| 58 | AssignmentPEONoticePeriod | NOTICE_PERIOD | — | — |
| 59 | AssignmentPEONoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 60 | AssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | AssignmentPEOOrganizationId | ORGANIZATION_ID | — | — |
| 62 | AssignmentPEOParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 63 | AssignmentPEOPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 64 | AssignmentPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 65 | AssignmentPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 66 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 67 | AssignmentPEOPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 68 | AssignmentPEOPersonTypeId | PERSON_TYPE_ID | — | — |
| 69 | AssignmentPEOPoHeaderId | PO_HEADER_ID | — | — |
| 70 | AssignmentPEOPoLineId | PO_LINE_ID | — | — |
| 71 | AssignmentPEOPositionId | POSITION_ID | — | — |
| 72 | AssignmentPEOPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 73 | AssignmentPEOPostingContentId | POSTING_CONTENT_ID | — | — |
| 74 | AssignmentPEOPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 75 | AssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 76 | AssignmentPEOPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 77 | AssignmentPEOPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 78 | AssignmentPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 79 | AssignmentPEOProbationUnit | PROBATION_UNIT | — | — |
| 80 | AssignmentPEOProjectTitle | PROJECT_TITLE | — | — |
| 81 | AssignmentPEOProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 82 | AssignmentPEOProjectedStartDate | PROJECTED_START_DATE | — | — |
| 83 | AssignmentPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 84 | AssignmentPEOReasonCode | REASON_CODE | — | — |
| 85 | AssignmentPEORecordCreator | RECORD_CREATOR | — | — |
| 86 | AssignmentPEORecruiterId | RECRUITER_ID | — | — |
| 87 | AssignmentPEORecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 88 | AssignmentPEORetirementAge | RETIREMENT_AGE | — | — |
| 89 | AssignmentPEORetirementDate | RETIREMENT_DATE | — | — |
| 90 | AssignmentPEOSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 91 | AssignmentPEOSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 92 | AssignmentPEOSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 93 | AssignmentPEOSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 94 | AssignmentPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 95 | AssignmentPEOSourceType | SOURCE_TYPE | — | — |
| 96 | AssignmentPEOSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 97 | AssignmentPEOStepEntryDate | STEP_ENTRY_DATE | — | — |
| 98 | AssignmentPEOSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 99 | AssignmentPEOTaxAddressId | TAX_ADDRESS_ID | — | — |
| 100 | AssignmentPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 101 | AssignmentPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 102 | AssignmentPEOVacancyId | VACANCY_ID | — | — |
| 103 | AssignmentPEOVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 104 | AssignmentPEOVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 105 | AssignmentPEOVendorId | VENDOR_ID | — | — |
| 106 | AssignmentPEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 107 | AssignmentPEOWorkAtHome | WORK_AT_HOME | — | — |
| 108 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | UserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | UserPEOCreatedBy | CREATED_BY | — | — |
| 4 | UserPEOCreationDate | CREATION_DATE | — | — |
| 5 | UserPEOCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | UserPEOEndDate | END_DATE | — | — |
| 7 | UserPEOExternalId | EXTERNAL_ID | — | — |
| 8 | UserPEOHrTerminated | HR_TERMINATED | — | — |
| 9 | UserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | UserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | UserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | UserPEOMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | UserPEOPartyId | PARTY_ID | — | — |
| 15 | UserPEOPersonId | PERSON_ID | — | — |
| 16 | UserPEOStartDate | START_DATE | — | — |
| 17 | UserPEOSuspended | SUSPENDED | — | — |
| 18 | UserPEOUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | UserPEOUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | UserPEOUserGuid | USER_GUID | — | — |
| 21 | UserPEOUserId | USER_ID | — | — |
| 22 | UserPEOUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
