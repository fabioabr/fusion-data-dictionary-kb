---
id: DOC-OTHER-PVO-QualityActionRelationship
doc_type: system-doc
title: "QualityActionRelationship — PVO Cross-Module"
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
  - QualityActionRelationship
  - qualityactionrelationship
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityActionRelationship

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Action Relationship. Acessa as tabelas: ACA_CS_REL_RULES, ENQ_ACTIONS_VL, ENQ_ACTION_RELATIONSHIP_V (+3).

**Caminho:** `FscmTopModelAM.QualityActionsAnalyticsAM.QualityActionRelationship`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 231 | 6 | 1 | 101 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[aca_cs_rel_rules|ACA_CS_REL_RULES]] — 12 atributos (12 BICC)
- [[enq_actions_vl|ENQ_ACTIONS_VL]] — 56 atributos (56 BICC)
- [[enq_action_relationship_v|ENQ_ACTION_RELATIONSHIP_V]] — 28 atributos (1 PKs, 28 BICC)
- [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]] — 4 atributos (2 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 BICC)
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

### [[enq_actions_vl|ENQ_ACTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedActionPEOActionAutonumber | ACTION_AUTONUMBER | — | ✅ |
| 2 | DerivedActionPEOActionId | ACTION_ID | — | ✅ |
| 3 | DerivedActionPEOActionType | ACTION_TYPE | — | ✅ |
| 4 | DerivedActionPEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 5 | DerivedActionPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | DerivedActionPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | DerivedActionPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 8 | DerivedActionPEODateReleased | DATE_RELEASED | — | ✅ |
| 9 | DerivedActionPEODateSubmitted | DATE_SUBMITTED | — | ✅ |
| 10 | DerivedActionPEODescription | DESCRIPTION | — | ✅ |
| 11 | DerivedActionPEODisposition | DISPOSITION | — | ✅ |
| 12 | DerivedActionPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 13 | DerivedActionPEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 14 | DerivedActionPEOFinalCompletionDate | FINAL_COMPLETION_DATE | — | ✅ |
| 15 | DerivedActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | DerivedActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | DerivedActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | DerivedActionPEOName | NAME | — | ✅ |
| 19 | DerivedActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | DerivedActionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 21 | DerivedActionPEOOwner | OWNER | — | ✅ |
| 22 | DerivedActionPEOPriority | PRIORITY | — | ✅ |
| 23 | DerivedActionPEOProductLineId | PRODUCT_LINE_ID | — | ✅ |
| 24 | DerivedActionPEOResolutionDescription | RESOLUTION_DESCRIPTION | — | ✅ |
| 25 | DerivedActionPEOSource | SOURCE | — | ✅ |
| 26 | DerivedActionPEOStatus | STATUS | — | ✅ |
| 27 | DerivedActionPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 28 | DerivedActionPEOWorkflowId | WORKFLOW_ID | — | ✅ |
| 29 | DrivingActionPEOActionAutonumber | ACTION_AUTONUMBER | — | ✅ |
| 30 | DrivingActionPEOActionId | ACTION_ID | — | ✅ |
| 31 | DrivingActionPEOActionType | ACTION_TYPE | — | ✅ |
| 32 | DrivingActionPEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 33 | DrivingActionPEOCreatedBy | CREATED_BY | — | ✅ |
| 34 | DrivingActionPEOCreationDate | CREATION_DATE | — | ✅ |
| 35 | DrivingActionPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 36 | DrivingActionPEODateReleased | DATE_RELEASED | — | ✅ |
| 37 | DrivingActionPEODateSubmitted | DATE_SUBMITTED | — | ✅ |
| 38 | DrivingActionPEODescription | DESCRIPTION | — | ✅ |
| 39 | DrivingActionPEODisposition | DISPOSITION | — | ✅ |
| 40 | DrivingActionPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 41 | DrivingActionPEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 42 | DrivingActionPEOFinalCompletionDate | FINAL_COMPLETION_DATE | — | ✅ |
| 43 | DrivingActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | DrivingActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | DrivingActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | DrivingActionPEOName | NAME | — | ✅ |
| 47 | DrivingActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 48 | DrivingActionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 49 | DrivingActionPEOOwner | OWNER | — | ✅ |
| 50 | DrivingActionPEOPriority | PRIORITY | — | ✅ |
| 51 | DrivingActionPEOProductLineId | PRODUCT_LINE_ID | — | ✅ |
| 52 | DrivingActionPEOResolutionDescription | RESOLUTION_DESCRIPTION | — | ✅ |
| 53 | DrivingActionPEOSource | SOURCE | — | ✅ |
| 54 | DrivingActionPEOStatus | STATUS | — | ✅ |
| 55 | DrivingActionPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 56 | DrivingActionPEOWorkflowId | WORKFLOW_ID | — | ✅ |

### [[enq_action_relationship_v|ENQ_ACTION_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionRelationshipPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ActionRelationshipPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ActionRelationshipPEODerivedActionId | DERIVED_ACTION_ID | — | ✅ |
| 4 | ActionRelationshipPEODerivedChangeId | DERIVED_CHANGE_ID | — | ✅ |
| 5 | ActionRelationshipPEODerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 6 | ActionRelationshipPEODerivedConceptId | DERIVED_CONCEPT_ID | — | ✅ |
| 7 | ActionRelationshipPEODerivedIdeaId | DERIVED_IDEA_ID | — | ✅ |
| 8 | ActionRelationshipPEODerivedIssueId | DERIVED_ISSUE_ID | — | ✅ |
| 9 | ActionRelationshipPEODerivedItemId | DERIVED_ITEM_ID | — | ✅ |
| 10 | ActionRelationshipPEODerivedItemId1 | DERIVED_ITEM_ID1 | — | ✅ |
| 11 | ActionRelationshipPEODerivedProposalId | DERIVED_PROPOSAL_ID | — | ✅ |
| 12 | ActionRelationshipPEODerivedRequirementId | DERIVED_REQUIREMENT_ID | — | ✅ |
| 13 | ActionRelationshipPEODerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 14 | ActionRelationshipPEODestObjId | DEST_OBJ_ID | — | ✅ |
| 15 | ActionRelationshipPEODestObjPk2value | DEST_OBJ_PK2VALUE | — | ✅ |
| 16 | ActionRelationshipPEODestObjType | DEST_OBJ_TYPE | — | ✅ |
| 17 | ActionRelationshipPEODirectionType | DIRECTION_TYPE | — | ✅ |
| 18 | ActionRelationshipPEOFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 19 | ActionRelationshipPEOFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 20 | ActionRelationshipPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | ActionRelationshipPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | ActionRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ActionRelationshipPEORelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 24 | ActionRelationshipPEORelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 25 | ActionRelationshipPEOSrcObjId | SRC_OBJ_ID | — | ✅ |
| 26 | ActionRelationshipPEOSrcObjPk2value | SRC_OBJ_PK2VALUE | — | ✅ |
| 27 | ActionRelationshipPEOSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 28 | ActionRelationshipPEOTargetType | TARGET_TYPE | — | ✅ |

### [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | ActionDatesPEOObjectPk1 | OBJECT_PK1 | — | — |
| 3 | ActionDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | — |
| 4 | ActionDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | ✅ |

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
