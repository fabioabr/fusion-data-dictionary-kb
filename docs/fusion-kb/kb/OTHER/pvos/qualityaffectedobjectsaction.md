---
id: DOC-OTHER-PVO-QualityAffectedObjectsAction
doc_type: system-doc
title: "QualityAffectedObjectsAction — PVO Cross-Module"
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
  - QualityAffectedObjectsAction
  - qualityaffectedobjectsaction
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityAffectedObjectsAction

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Affected Objects Action. Acessa as tabelas: ENQ_ACTIONS_B, ENQ_ACTIONS_TL, ENQ_ACTION_WORKFLOW_DATES_V (+8).

**Caminho:** `FscmTopModelAM.QualityActionsAnalyticsAM.QualityAffectedObjectsAction`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 261 | 11 | 1 | 13 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[enq_actions_b|ENQ_ACTIONS_B]] — 50 atributos
- [[enq_actions_tl|ENQ_ACTIONS_TL]] — 13 atributos (4 BICC)
- [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]] — 4 atributos (1 BICC)
- [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]] — 19 atributos (1 PKs, 3 BICC)
- [[enq_affected_objects_tl|ENQ_AFFECTED_OBJECTS_TL]] — 5 atributos
- [[enq_qlty_type_supp_entities|ENQ_QLTY_TYPE_SUPP_ENTITIES]] — 13 atributos (1 BICC)
- [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]] — 10 atributos
- [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]] — 7 atributos
- [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]] — 9 atributos (1 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 109 atributos (2 BICC)
- [[per_users|PER_USERS]] — 22 atributos (1 BICC)

---

## ⚙️ Atributos

### [[enq_actions_b|ENQ_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsBasePEOActionAutonumber | ACTION_AUTONUMBER | — | — |
| 2 | ActionsBasePEOActionId | ACTION_ID | — | — |
| 3 | ActionsBasePEOActionType | ACTION_TYPE | — | — |
| 4 | ActionsBasePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | — |
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
| 31 | ActionsBasePEOCreatedBy | CREATED_BY | — | — |
| 32 | ActionsBasePEOCreationDate | CREATION_DATE | — | — |
| 33 | ActionsBasePEOCustomerId | CUSTOMER_ID | — | — |
| 34 | ActionsBasePEODateReleased | DATE_RELEASED | — | — |
| 35 | ActionsBasePEODateSubmitted | DATE_SUBMITTED | — | — |
| 36 | ActionsBasePEODisposition | DISPOSITION | — | — |
| 37 | ActionsBasePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | — |
| 38 | ActionsBasePEOFinalCompletionDate | FINAL_COMPLETION_DATE | — | — |
| 39 | ActionsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 40 | ActionsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | ActionsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | ActionsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ActionsBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 44 | ActionsBasePEOOwner | OWNER | — | — |
| 45 | ActionsBasePEOPriority | PRIORITY | — | — |
| 46 | ActionsBasePEOProductLineId | PRODUCT_LINE_ID | — | — |
| 47 | ActionsBasePEOSource | SOURCE | — | — |
| 48 | ActionsBasePEOStatus | STATUS | — | — |
| 49 | ActionsBasePEOSupplierId | SUPPLIER_ID | — | — |
| 50 | ActionsBasePEOWorkflowId | WORKFLOW_ID | — | — |

### [[enq_actions_tl|ENQ_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ActionsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ActionsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ActionsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ActionsTranslationPEODispositionComment | DISPOSITION_COMMENT | — | ✅ |
| 6 | ActionsTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ActionsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActionsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ActionsTranslationPEOName | NAME | — | ✅ |
| 11 | ActionsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ActionsTranslationPEOResolutionDescription | RESOLUTION_DESCRIPTION | — | — |
| 13 | ActionsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[enq_action_workflow_dates_v|ENQ_ACTION_WORKFLOW_DATES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionDatesPEOApprovalWorkflowStartDate | APPROVAL_WORKFLOW_START_DATE | — | ✅ |
| 2 | ActionDatesPEOObjectPk1 | OBJECT_PK1 | — | — |
| 3 | ActionDatesPEOWorkflowCompletiondate | WORKFLOW_END_DATE | — | — |
| 4 | ActionDatesPEOWorkflowStartdate | WORKFLOW_START_DATE | — | — |

### [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AffectedObjectsBasePEOAffectedObjectId | AFFECTED_OBJECT_ID | 🔑 | ✅ |
| 2 | AffectedObjectsBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | AffectedObjectsBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | AffectedObjectsBasePEOImpactType | IMPACT_TYPE | — | — |
| 5 | AffectedObjectsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AffectedObjectsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AffectedObjectsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AffectedObjectsBasePEOObjectId | OBJECT_ID | — | — |
| 9 | AffectedObjectsBasePEOObjectType | OBJECT_TYPE | — | ✅ |
| 10 | AffectedObjectsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AffectedObjectsBasePEOPk1Value | PK1_VALUE | — | — |
| 12 | AffectedObjectsBasePEOPk2Value | PK2_VALUE | — | — |
| 13 | AffectedObjectsBasePEOPk3Value | PK3_VALUE | — | — |
| 14 | AffectedObjectsBasePEOPk4Value | PK4_VALUE | — | — |
| 15 | AffectedObjectsBasePEOPk5Value | PK5_VALUE | — | — |
| 16 | AffectedObjectsBasePEOPk6Value | PK6_VALUE | — | — |
| 17 | AffectedObjectsBasePEOPk7Value | PK7_VALUE | — | — |
| 18 | AffectedObjectsBasePEOStatus | STATUS | — | — |
| 19 | AffectedObjectsBasePEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | — |

### [[enq_affected_objects_tl|ENQ_AFFECTED_OBJECTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AffectedObjectsTranslationEOAffectedObjectId | AFFECTED_OBJECT_ID | — | — |
| 2 | AffectedObjectsTranslationEODescription | DESCRIPTION | — | — |
| 3 | AffectedObjectsTranslationEOLanguage | LANGUAGE | — | — |
| 4 | AffectedObjectsTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | AffectedObjectsTranslationEOSourceLang | SOURCE_LANG | — | — |

### [[enq_qlty_type_supp_entities|ENQ_QLTY_TYPE_SUPP_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QltyTypeSupEntPEOAssociationType | ASSOCIATION_TYPE | — | — |
| 2 | QltyTypeSupEntPEOCreatedBy | CREATED_BY | — | — |
| 3 | QltyTypeSupEntPEOCreationDate | CREATION_DATE | — | — |
| 4 | QltyTypeSupEntPEOIsRequired | IS_REQUIRED | — | — |
| 5 | QltyTypeSupEntPEOIsSeeded | IS_SEEDED | — | — |
| 6 | QltyTypeSupEntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QltyTypeSupEntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | QltyTypeSupEntPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | QltyTypeSupEntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | QltyTypeSupEntPEOQltyTypeSuppEntityId | QLTY_TYPE_SUPP_ENTITY_ID | — | — |
| 11 | QltyTypeSupEntPEOQualityTypeId | QUALITY_TYPE_ID | — | — |
| 12 | QltyTypeSupEntPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | QltyTypeSupEntPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | — |

### [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypePEOCode | CODE | — | — |
| 2 | QualityTypePEODisplayOrder | DISPLAY_ORDER | — | — |
| 3 | QualityTypePEOInstantiationAllowed | INSTANTIATION_ALLOWED | — | — |
| 4 | QualityTypePEOIsActive | IS_ACTIVE | — | — |
| 5 | QualityTypePEOIsSeeded | IS_SEEDED | — | — |
| 6 | QualityTypePEOObjectType | OBJECT_TYPE | — | — |
| 7 | QualityTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | QualityTypePEOParentQualityTypeId | PARENT_QUALITY_TYPE_ID | — | — |
| 9 | QualityTypePEOQualityTypeId | QUALITY_TYPE_ID | — | — |
| 10 | QualityTypePEOSource | SOURCE | — | — |

### [[enq_quality_types_tl|ENQ_QUALITY_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypeTranslationPEODescription | DESCRIPTION | — | — |
| 2 | QualityTypeTranslationPEOLabel | LABEL | — | — |
| 3 | QualityTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | QualityTypeTranslationPEOName | NAME | — | — |
| 5 | QualityTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | QualityTypeTranslationPEOQualityTypeId | QUALITY_TYPE_ID | — | — |
| 7 | QualityTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QltySupEntPEOCreatedBy | CREATED_BY | — | — |
| 2 | QltySupEntPEOCreationDate | CREATION_DATE | — | — |
| 3 | QltySupEntPEOEntityType | ENTITY_TYPE | — | — |
| 4 | QltySupEntPEOIsSeeded | IS_SEEDED | — | — |
| 5 | QltySupEntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QltySupEntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | QltySupEntPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | QltySupEntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | QltySupEntPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPActionCode | ACTION_CODE | — | — |
| 2 | AssignmentPActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 3 | AssignmentPAllowAsgOverrideFlag | ALLOW_ASG_OVERRIDE_FLAG | — | — |
| 4 | AssignmentPApplicantRank | APPLICANT_RANK | — | — |
| 5 | AssignmentPAssignmentId | ASSIGNMENT_ID | — | — |
| 6 | AssignmentPAssignmentName | ASSIGNMENT_NAME | — | — |
| 7 | AssignmentPAssignmentNumber | ASSIGNMENT_NUMBER | — | — |
| 8 | AssignmentPAssignmentSequence | ASSIGNMENT_SEQUENCE | — | — |
| 9 | AssignmentPAssignmentStatusType | ASSIGNMENT_STATUS_TYPE | — | — |
| 10 | AssignmentPAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 11 | AssignmentPAssignmentType | ASSIGNMENT_TYPE | — | — |
| 12 | AssignmentPAutoEndFlag | AUTO_END_FLAG | — | — |
| 13 | AssignmentPBargainingUnitCode | BARGAINING_UNIT_CODE | — | — |
| 14 | AssignmentPBillingTitle | BILLING_TITLE | — | — |
| 15 | AssignmentPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 16 | AssignmentPBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 17 | AssignmentPCagrGradeDefId | CAGR_GRADE_DEF_ID | — | — |
| 18 | AssignmentPCagrIdFlexNum | CAGR_ID_FLEX_NUM | — | — |
| 19 | AssignmentPCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 20 | AssignmentPContractId | CONTRACT_ID | — | — |
| 21 | AssignmentPCreatedBy | CREATED_BY | — | — |
| 22 | AssignmentPCreationDate | CREATION_DATE | — | — |
| 23 | AssignmentPDateProbationEnd | DATE_PROBATION_END | — | — |
| 24 | AssignmentPDefaultCodeCombId | DEFAULT_CODE_COMB_ID | — | — |
| 25 | AssignmentPDutiesType | DUTIES_TYPE | — | — |
| 26 | AssignmentPEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 27 | AssignmentPEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 28 | AssignmentPEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 29 | AssignmentPEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 30 | AssignmentPEmployeeCategory | EMPLOYEE_CATEGORY | — | — |
| 31 | AssignmentPEmploymentCategory | EMPLOYMENT_CATEGORY | — | — |
| 32 | AssignmentPEstablishmentId | ESTABLISHMENT_ID | — | — |
| 33 | AssignmentPExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | — |
| 34 | AssignmentPFreezeStartDate | FREEZE_START_DATE | — | — |
| 35 | AssignmentPFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 36 | AssignmentPFrequency | FREQUENCY | — | — |
| 37 | AssignmentPFullPartTime | FULL_PART_TIME | — | — |
| 38 | AssignmentPGradeId | GRADE_ID | — | — |
| 39 | AssignmentPGradeLadderPgmId | GRADE_LADDER_PGM_ID | — | — |
| 40 | AssignmentPHourlySalariedCode | HOURLY_SALARIED_CODE | — | — |
| 41 | AssignmentPIdFlexNum | ID_FLEX_NUM | — | — |
| 42 | AssignmentPInternalBuilding | INTERNAL_BUILDING | — | — |
| 43 | AssignmentPInternalFloor | INTERNAL_FLOOR | — | — |
| 44 | AssignmentPInternalLocation | INTERNAL_LOCATION | — | — |
| 45 | AssignmentPInternalMailstop | INTERNAL_MAILSTOP | — | — |
| 46 | AssignmentPInternalOfficeNumber | INTERNAL_OFFICE_NUMBER | — | — |
| 47 | AssignmentPJobId | JOB_ID | — | — |
| 48 | AssignmentPJobPostSourceName | JOB_POST_SOURCE_NAME | — | — |
| 49 | AssignmentPLabourUnionMemberFlag | LABOUR_UNION_MEMBER_FLAG | — | — |
| 50 | AssignmentPLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | AssignmentPLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | AssignmentPLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | AssignmentPLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 54 | AssignmentPLegislationCode | LEGISLATION_CODE | — | — |
| 55 | AssignmentPLinkageType | LINKAGE_TYPE | — | — |
| 56 | AssignmentPLocationId | LOCATION_ID | — | — |
| 57 | AssignmentPManagerFlag | MANAGER_FLAG | — | — |
| 58 | AssignmentPNormalHours | NORMAL_HOURS | — | — |
| 59 | AssignmentPNoticePeriod | NOTICE_PERIOD | — | — |
| 60 | AssignmentPNoticePeriodUom | NOTICE_PERIOD_UOM | — | — |
| 61 | AssignmentPObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | AssignmentPOrganizationId | ORGANIZATION_ID | — | — |
| 63 | AssignmentPParentAssignmentId | PARENT_ASSIGNMENT_ID | — | — |
| 64 | AssignmentPPeopleGroupId | PEOPLE_GROUP_ID | — | — |
| 65 | AssignmentPPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 66 | AssignmentPPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 67 | AssignmentPPersonId | PERSON_ID | — | — |
| 68 | AssignmentPPersonReferredById | PERSON_REFERRED_BY_ID | — | — |
| 69 | AssignmentPPersonTypeId | PERSON_TYPE_ID | — | — |
| 70 | AssignmentPPoHeaderId | PO_HEADER_ID | — | — |
| 71 | AssignmentPPoLineId | PO_LINE_ID | — | — |
| 72 | AssignmentPPositionId | POSITION_ID | — | — |
| 73 | AssignmentPPositionOverrideFlag | POSITION_OVERRIDE_FLAG | — | — |
| 74 | AssignmentPPostingContentId | POSTING_CONTENT_ID | — | — |
| 75 | AssignmentPPrimaryAssignmentFlag | PRIMARY_ASSIGNMENT_FLAG | — | — |
| 76 | AssignmentPPrimaryFlag | PRIMARY_FLAG | — | — |
| 77 | AssignmentPPrimaryWorkRelationFlag | PRIMARY_WORK_RELATION_FLAG | — | — |
| 78 | AssignmentPPrimaryWorkTermsFlag | PRIMARY_WORK_TERMS_FLAG | — | — |
| 79 | AssignmentPProbationPeriod | PROBATION_PERIOD | — | — |
| 80 | AssignmentPProbationUnit | PROBATION_UNIT | — | — |
| 81 | AssignmentPProjectTitle | PROJECT_TITLE | — | — |
| 82 | AssignmentPProjectedAssignmentEnd | PROJECTED_ASSIGNMENT_END | — | — |
| 83 | AssignmentPProjectedStartDate | PROJECTED_START_DATE | — | — |
| 84 | AssignmentPProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 85 | AssignmentPReasonCode | REASON_CODE | — | — |
| 86 | AssignmentPRecordCreator | RECORD_CREATOR | — | — |
| 87 | AssignmentPRecruiterId | RECRUITER_ID | — | — |
| 88 | AssignmentPRecruitmentActivityId | RECRUITMENT_ACTIVITY_ID | — | — |
| 89 | AssignmentPRetirementAge | RETIREMENT_AGE | — | — |
| 90 | AssignmentPRetirementDate | RETIREMENT_DATE | — | — |
| 91 | AssignmentPSalReviewPeriod | SAL_REVIEW_PERIOD | — | — |
| 92 | AssignmentPSalReviewPeriodFrequency | SAL_REVIEW_PERIOD_FREQUENCY | — | — |
| 93 | AssignmentPSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 94 | AssignmentPSoftCodingKeyflexId | SOFT_CODING_KEYFLEX_ID | — | — |
| 95 | AssignmentPSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 96 | AssignmentPSourceType | SOURCE_TYPE | — | — |
| 97 | AssignmentPSpecialCeilingStepId | SPECIAL_CEILING_STEP_ID | — | — |
| 98 | AssignmentPStepEntryDate | STEP_ENTRY_DATE | — | — |
| 99 | AssignmentPSystemPersonType | SYSTEM_PERSON_TYPE | — | — |
| 100 | AssignmentPTaxAddressId | TAX_ADDRESS_ID | — | — |
| 101 | AssignmentPTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 102 | AssignmentPTimeNormalStart | TIME_NORMAL_START | — | — |
| 103 | AssignmentPVacancyId | VACANCY_ID | — | — |
| 104 | AssignmentPVendorAssignmentNumber | VENDOR_ASSIGNMENT_NUMBER | — | — |
| 105 | AssignmentPVendorEmployeeNumber | VENDOR_EMPLOYEE_NUMBER | — | — |
| 106 | AssignmentPVendorId | VENDOR_ID | — | — |
| 107 | AssignmentPVendorSiteId | VENDOR_SITE_ID | — | — |
| 108 | AssignmentPWorkAtHome | WORK_AT_HOME | — | — |
| 109 | AssignmentPWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

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
| 9 | UserPLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
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
