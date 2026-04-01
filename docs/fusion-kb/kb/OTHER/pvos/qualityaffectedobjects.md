---
id: DOC-OTHER-PVO-QualityAffectedObjects
doc_type: system-doc
title: "QualityAffectedObjects — PVO Cross-Module"
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
  - QualityAffectedObjects
  - qualityaffectedobjects
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityAffectedObjects

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Affected Objects. Acessa as tabelas: ENQ_ACTIONS_B, ENQ_ACTIONS_TL, ENQ_ACTION_WORKFLOW_DATES_V (+11).

**Caminho:** `FscmTopModelAM.QualityIssuesAnalyticsAM.QualityAffectedObjects`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 300 | 14 | 5 | 136 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[enq_actions_b|ENQ_ACTIONS_B]] — 50 atributos (24 BICC)
- [[enq_actions_tl|ENQ_ACTIONS_TL]] — 13 atributos (13 BICC)
- [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]] — 4 atributos
- [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]] — 19 atributos (1 PKs, 17 BICC)
- [[enq_affected_objects_tl|ENQ_AFFECTED_OBJECTS_TL]] — 5 atributos (5 BICC)
- [[enq_issues_b|ENQ_ISSUES_B]] — 23 atributos (1 PKs, 22 BICC)
- [[enq_issues_tl|ENQ_ISSUES_TL]] — 12 atributos (12 BICC)
- [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]] — 4 atributos (4 BICC)
- [[enq_qlty_type_supp_entities|ENQ_QLTY_TYPE_SUPP_ENTITIES]] — 13 atributos (1 PKs, 12 BICC)
- [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]] — 10 atributos (10 BICC)
- [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]] — 7 atributos (7 BICC)
- [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]] — 9 atributos (9 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 PKs, 1 BICC)
- [[per_users|PER_USERS]] — 22 atributos

---

## ⚙️ Atributos

### [[enq_actions_b|ENQ_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsBasePEOActionAutonumber | ACTION_AUTONUMBER | — | ✅ |
| 2 | ActionsBasePEOActionId | ACTION_ID | — | ✅ |
| 3 | ActionsBasePEOActionType | ACTION_TYPE | — | ✅ |
| 4 | ActionsBasePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 5 | ActionsBasePEOAttributeNumber045 | EXTN_ATTRIBUTE_NUMBER045 | — | — |
| 6 | ActionsBasePEOAttributeNumber046 | EXTN_ATTRIBUTE_NUMBER046 | — | — |
| 7 | ActionsBasePEOAttributeNumber047 | EXTN_ATTRIBUTE_NUMBER047 | — | — |
| 8 | ActionsBasePEOAttributeNumber048 | EXTN_ATTRIBUTE_NUMBER048 | — | — |
| 9 | ActionsBasePEOAttributeNumber049 | EXTN_ATTRIBUTE_NUMBER049 | — | — |
| 10 | ActionsBasePEOAttributeNumber050 | EXTN_ATTRIBUTE_NUMBER050 | — | — |
| 11 | ActionsBasePEOAttributeTimestamp001 | EXTN_ATTRIBUTE_TIMESTAMP001 | — | — |
| 12 | ActionsBasePEOAttributeTimestamp002 | EXTN_ATTRIBUTE_TIMESTAMP002 | — | — |
| 13 | ActionsBasePEOAttributeTimestamp003 | EXTN_ATTRIBUTE_TIMESTAMP003 | — | — |
| 14 | ActionsBasePEOAttributeTimestamp004 | EXTN_ATTRIBUTE_TIMESTAMP004 | — | — |
| 15 | ActionsBasePEOAttributeTimestamp005 | EXTN_ATTRIBUTE_TIMESTAMP005 | — | — |
| 16 | ActionsBasePEOAttributeTimestamp006 | EXTN_ATTRIBUTE_TIMESTAMP006 | — | — |
| 17 | ActionsBasePEOAttributeTimestamp007 | EXTN_ATTRIBUTE_TIMESTAMP007 | — | — |
| 18 | ActionsBasePEOAttributeTimestamp008 | EXTN_ATTRIBUTE_TIMESTAMP008 | — | — |
| 19 | ActionsBasePEOAttributeTimestamp009 | EXTN_ATTRIBUTE_TIMESTAMP009 | — | — |
| 20 | ActionsBasePEOAttributeTimestamp010 | EXTN_ATTRIBUTE_TIMESTAMP010 | — | — |
| 21 | ActionsBasePEOAttributeTimestamp011 | EXTN_ATTRIBUTE_TIMESTAMP011 | — | — |
| 22 | ActionsBasePEOAttributeTimestamp012 | EXTN_ATTRIBUTE_TIMESTAMP012 | — | — |
| 23 | ActionsBasePEOAttributeTimestamp013 | EXTN_ATTRIBUTE_TIMESTAMP013 | — | — |
| 24 | ActionsBasePEOAttributeTimestamp014 | EXTN_ATTRIBUTE_TIMESTAMP014 | — | — |
| 25 | ActionsBasePEOAttributeTimestamp015 | EXTN_ATTRIBUTE_TIMESTAMP015 | — | — |
| 26 | ActionsBasePEOAttributeTimestamp016 | EXTN_ATTRIBUTE_TIMESTAMP016 | — | — |
| 27 | ActionsBasePEOAttributeTimestamp017 | EXTN_ATTRIBUTE_TIMESTAMP017 | — | — |
| 28 | ActionsBasePEOAttributeTimestamp018 | EXTN_ATTRIBUTE_TIMESTAMP018 | — | — |
| 29 | ActionsBasePEOAttributeTimestamp019 | EXTN_ATTRIBUTE_TIMESTAMP019 | — | — |
| 30 | ActionsBasePEOAttributeTimestamp020 | EXTN_ATTRIBUTE_TIMESTAMP020 | — | — |
| 31 | ActionsBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 32 | ActionsBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 33 | ActionsBasePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 34 | ActionsBasePEODateReleased | DATE_RELEASED | — | ✅ |
| 35 | ActionsBasePEODateSubmitted | DATE_SUBMITTED | — | ✅ |
| 36 | ActionsBasePEODisposition | DISPOSITION | — | ✅ |
| 37 | ActionsBasePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 38 | ActionsBasePEOFinalCompletionDate | FINAL_COMPLETION_DATE | — | ✅ |
| 39 | ActionsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ActionsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 41 | ActionsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | ActionsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | ActionsBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 44 | ActionsBasePEOOwner | OWNER | — | ✅ |
| 45 | ActionsBasePEOPriority | PRIORITY | — | ✅ |
| 46 | ActionsBasePEOProductLineId | PRODUCT_LINE_ID | — | ✅ |
| 47 | ActionsBasePEOSource | SOURCE | — | ✅ |
| 48 | ActionsBasePEOStatus | STATUS | — | ✅ |
| 49 | ActionsBasePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 50 | ActionsBasePEOWorkflowId | WORKFLOW_ID | — | ✅ |

### [[enq_actions_tl|ENQ_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsTranslationPEOActionId | ACTION_ID | — | ✅ |
| 2 | ActionsTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ActionsTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ActionsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ActionsTranslationPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 6 | ActionsTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | ActionsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ActionsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ActionsTranslationPEOName | NAME | — | ✅ |
| 11 | ActionsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ActionsTranslationPEOResolutionDescription | RESOLUTION_DESCRIPTION | — | ✅ |
| 13 | ActionsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | — |
| 2 | ActionDatesPEOObjectPk1 | OBJECT_PK1 | — | — |
| 3 | ActionDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | — |
| 4 | ActionDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | — |

### [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AffectedObjectsBasePEOAffectedObjectId | AFFECTED_OBJECT_ID | 🔑 | ✅ |
| 2 | AffectedObjectsBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AffectedObjectsBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AffectedObjectsBasePEOImpactType | IMPACT_TYPE | — | ✅ |
| 5 | AffectedObjectsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AffectedObjectsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AffectedObjectsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AffectedObjectsBasePEOObjectId | OBJECT_ID | — | ✅ |
| 9 | AffectedObjectsBasePEOObjectType | OBJECT_TYPE | — | ✅ |
| 10 | AffectedObjectsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AffectedObjectsBasePEOPk1Value | PK1_VALUE | — | ✅ |
| 12 | AffectedObjectsBasePEOPk2Value | PK2_VALUE | — | ✅ |
| 13 | AffectedObjectsBasePEOPk3Value | PK3_VALUE | — | ✅ |
| 14 | AffectedObjectsBasePEOPk4Value | PK4_VALUE | — | ✅ |
| 15 | AffectedObjectsBasePEOPk5Value | PK5_VALUE | — | ✅ |
| 16 | AffectedObjectsBasePEOPk6Value | PK6_VALUE | — | — |
| 17 | AffectedObjectsBasePEOPk7Value | PK7_VALUE | — | — |
| 18 | AffectedObjectsBasePEOStatus | STATUS | — | ✅ |
| 19 | AffectedObjectsBasePEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | ✅ |

### [[enq_affected_objects_tl|ENQ_AFFECTED_OBJECTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AffectedObjectsTranslationEOAffectedObjectId | AFFECTED_OBJECT_ID | — | ✅ |
| 2 | AffectedObjectsTranslationEODescription | DESCRIPTION | — | ✅ |
| 3 | AffectedObjectsTranslationEOLanguage | LANGUAGE | — | ✅ |
| 4 | AffectedObjectsTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 5 | AffectedObjectsTranslationEOSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_issues_b|ENQ_ISSUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueBasePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 2 | IssueBasePEOAssignedTo | ASSIGNED_TO | — | ✅ |
| 3 | IssueBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | IssueBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | IssueBasePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 6 | IssueBasePEODisposition | DISPOSITION | — | ✅ |
| 7 | IssueBasePEODowntime | DOWNTIME | — | ✅ |
| 8 | IssueBasePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 9 | IssueBasePEOIssueId | ISSUE_ID | 🔑 | — |
| 10 | IssueBasePEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 11 | IssueBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | IssueBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | IssueBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | IssueBasePEOLikelihoodOfRecurrence | LIKELIHOOD_OF_RECURRENCE | — | ✅ |
| 15 | IssueBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | IssueBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | IssueBasePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 18 | IssueBasePEOReportedBy | REPORTED_BY | — | ✅ |
| 19 | IssueBasePEOReportedDate | REPORTED_DATE | — | ✅ |
| 20 | IssueBasePEOSeverity | SEVERITY | — | ✅ |
| 21 | IssueBasePEOSource | SOURCE | — | ✅ |
| 22 | IssueBasePEOSupplierId | SUPPLIER_ID | — | ✅ |
| 23 | IssueBasePEOWorkflowStatusId | WORKFLOW_STATUS_ID | — | ✅ |

### [[enq_issues_tl|ENQ_ISSUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | IssueTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | IssueTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | IssueTranslationPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 5 | IssueTranslationPEOIssueId | ISSUE_ID | — | ✅ |
| 6 | IssueTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | IssueTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | IssueTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | IssueTranslationPEOName | NAME | — | ✅ |
| 11 | IssueTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | IssueTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_issue_workflow_dates_v|ENQ_ISSUE_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | IssueDatesPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 3 | IssueDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | ✅ |
| 4 | IssueDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | ✅ |

### [[enq_qlty_type_supp_entities|ENQ_QLTY_TYPE_SUPP_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QltyTypeSupEntPEOAssociationType | ASSOCIATION_TYPE | — | ✅ |
| 2 | QltyTypeSupEntPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QltyTypeSupEntPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QltyTypeSupEntPEOIsRequired | IS_REQUIRED | — | ✅ |
| 5 | QltyTypeSupEntPEOIsSeeded | IS_SEEDED | — | ✅ |
| 6 | QltyTypeSupEntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QltyTypeSupEntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QltyTypeSupEntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QltyTypeSupEntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QltyTypeSupEntPEOQltyTypeSuppEntityId | QLTY_TYPE_SUPP_ENTITY_ID | 🔑 | — |
| 11 | QltyTypeSupEntPEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 12 | QltyTypeSupEntPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | QltyTypeSupEntPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | ✅ |

### [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypePEOCode | CODE | — | ✅ |
| 2 | QualityTypePEODisplayOrder | DISPLAY_ORDER | — | ✅ |
| 3 | QualityTypePEOInstantiationAllowed | INSTANTIATION_ALLOWED | — | ✅ |
| 4 | QualityTypePEOIsActive | IS_ACTIVE | — | ✅ |
| 5 | QualityTypePEOIsSeeded | IS_SEEDED | — | ✅ |
| 6 | QualityTypePEOObjectType | OBJECT_TYPE | — | ✅ |
| 7 | QualityTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | QualityTypePEOParentQualityTypeId | PARENT_QUALITY_TYPE_ID | — | ✅ |
| 9 | QualityTypePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 10 | QualityTypePEOSource | SOURCE | — | ✅ |

### [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | QualityTypeTranslationPEOLabel | LABEL | — | ✅ |
| 3 | QualityTypeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | QualityTypeTranslationPEOName | NAME | — | ✅ |
| 5 | QualityTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 6 | QualityTypeTranslationPEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 7 | QualityTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QltySupEntPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QltySupEntPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QltySupEntPEOEntityType | ENTITY_TYPE | — | ✅ |
| 4 | QltySupEntPEOIsSeeded | IS_SEEDED | — | ✅ |
| 5 | QltySupEntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QltySupEntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | QltySupEntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | QltySupEntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QltySupEntPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentActionCode | ACTION_CODE | — | — |
| 2 | AssignmentActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentAssignmentId | ASSIGNMENT_ID | 🔑 | — |
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
| 21 | AssignmentCreatedBy | CREATED_BY | — | — |
| 22 | AssignmentCreationDate | CREATION_DATE | — | — |
| 23 | AssignmentDateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentDefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentDutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 28 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 29 | AssignmentEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | — |
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
| 1 | UserPActiveFlag | ACTIVE_FLAG | — | — |
| 2 | UserPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | UserPCreatedBy | CREATED_BY | — | — |
| 4 | UserPCreationDate | CREATION_DATE | — | — |
| 5 | UserPCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | — |
| 6 | UserPEndDate | END_DATE | — | — |
| 7 | UserPExternalId | EXTERNAL_ID | — | — |
| 8 | UserPHrTerminated | HR_TERMINATED | — | — |
| 9 | UserPLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | UserPLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | UserPLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | UserPMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | UserPObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | UserPPartyId | PARTY_ID | — | — |
| 15 | UserPPersonId | PERSON_ID | — | — |
| 16 | UserPStartDate | START_DATE | — | — |
| 17 | UserPSuspended | SUSPENDED | — | — |
| 18 | UserPUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 19 | UserPUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 20 | UserPUserGuid | USER_GUID | — | — |
| 21 | UserPUserId | USER_ID | — | — |
| 22 | UserPUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
