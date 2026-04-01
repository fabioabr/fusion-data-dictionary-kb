---
id: DOC-OTHER-PVO-AssessmentResultPVO
doc_type: system-doc
title: "AssessmentResultPVO — PVO Cross-Module"
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
  - AssessmentResultPVO
  - assessmentresultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentResultPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assessment Result. Acessa as tabelas: GRC_ACTV_ACTIVITY_TL, GRC_ACTV_RESPONSE_TL, GRC_ASMT_ASSESSMENT_B (+9).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.AssessmentResultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 181 | 12 | 2 | 49 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[grc_actv_activity_tl|GRC_ACTV_ACTIVITY_TL]] — 11 atributos (4 BICC)
- [[grc_actv_response_tl|GRC_ACTV_RESPONSE_TL]] — 11 atributos (3 BICC)
- [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]] — 34 atributos (1 BICC)
- [[grc_asmt_issue_result_v|GRC_ASMT_ISSUE_RESULT_V]] — 17 atributos (3 BICC)
- [[grc_asmt_result_v|GRC_ASMT_RESULT_V]] — 32 atributos (2 PKs, 17 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (10 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[grc_actv_activity_tl|GRC_ACTV_ACTIVITY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityPEOActivityCode | ACTIVITY_CODE | — | ✅ |
| 2 | ActivityPEOBindKey | BIND_KEY | — | — |
| 3 | ActivityPEOCreatedBy | CREATED_BY | — | — |
| 4 | ActivityPEOCreationDate | CREATION_DATE | — | — |
| 5 | ActivityPEODescription | DESCRIPTION | — | ✅ |
| 6 | ActivityPEOLanguage | LANGUAGE | — | — |
| 7 | ActivityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActivityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActivityPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ActivityPEOName | NAME | — | ✅ |
| 11 | ActivityPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_actv_response_tl|GRC_ACTV_RESPONSE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResponsePEOBindKey | BIND_KEY | — | — |
| 2 | ResponsePEOCreatedBy | CREATED_BY | — | — |
| 3 | ResponsePEOCreationDate | CREATION_DATE | — | — |
| 4 | ResponsePEODescription | DESCRIPTION | — | ✅ |
| 5 | ResponsePEOLanguage | LANGUAGE | — | — |
| 6 | ResponsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ResponsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ResponsePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ResponsePEOName | NAME | — | ✅ |
| 10 | ResponsePEOResponseCode | RESPONSE_CODE | — | — |
| 11 | ResponsePEOSourceLang | SOURCE_LANG | — | — |

### [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentBasePEOAsmtPlanEffseq | ASMT_PLAN_EFFSEQ | — | — |
| 2 | AssessmentBasePEOAsmtPlanId | ASMT_PLAN_ID | — | — |
| 3 | AssessmentBasePEOAssessmentCategoryCode | ASSESSMENT_CATEGORY_CODE | — | — |
| 4 | AssessmentBasePEOAssessmentId | ASSESSMENT_ID | — | — |
| 5 | AssessmentBasePEOAssessmentInitiateDate | ASSESSMENT_INITIATE_DATE | — | — |
| 6 | AssessmentBasePEOBusEntityAsmtCode | BUS_ENTITY_ASMT_CODE | — | — |
| 7 | AssessmentBasePEOBusEntityAuditTestCode | BUS_ENTITY_AUDIT_TEST_CODE | — | — |
| 8 | AssessmentBasePEOCompensatingSelectionCode | COMPENSATING_SELECTION_CODE | — | — |
| 9 | AssessmentBasePEOCreatedBy | CREATED_BY | — | — |
| 10 | AssessmentBasePEOCreationDate | CREATION_DATE | — | — |
| 11 | AssessmentBasePEOKeySelectionCode | KEY_SELECTION_CODE | — | — |
| 12 | AssessmentBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 13 | AssessmentBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | AssessmentBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | AssessmentBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | AssessmentBasePEOMitigatingSelectionCode | MITIGATING_SELECTION_CODE | — | — |
| 17 | AssessmentBasePEOMonitoringSelectionCode | MONITORING_SELECTION_CODE | — | — |
| 18 | AssessmentBasePEONoSelectionCode | NO_SELECTION_CODE | — | — |
| 19 | AssessmentBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | AssessmentBasePEOOtherSelectionCode | OTHER_SELECTION_CODE | — | — |
| 21 | AssessmentBasePEOOwner | OWNER | — | — |
| 22 | AssessmentBasePEOPerspItemId | PERSP_ITEM_ID | — | — |
| 23 | AssessmentBasePEOPerspTreeEffseq | PERSP_TREE_EFFSEQ | — | — |
| 24 | AssessmentBasePEOPerspTreeId | PERSP_TREE_ID | — | — |
| 25 | AssessmentBasePEOPrimaryControlsCode | PRIMARY_CONTROLS_CODE | — | — |
| 26 | AssessmentBasePEORedundantSelectionCode | REDUNDANT_SELECTION_CODE | — | — |
| 27 | AssessmentBasePEOResultsEntryCompletionDate | RESULTS_ENTRY_COMPLETION_DATE | — | — |
| 28 | AssessmentBasePEOResultsEntryDueDate | RESULTS_ENTRY_DUE_DATE | — | — |
| 29 | AssessmentBasePEOResultsEntryStartDate | RESULTS_ENTRY_START_DATE | — | — |
| 30 | AssessmentBasePEORootObjectTypeCode | ROOT_OBJECT_TYPE_CODE | — | — |
| 31 | AssessmentBasePEOStateCode | STATE_CODE | — | — |
| 32 | AssessmentBasePEOStateDate | STATE_DATE | — | — |
| 33 | AssessmentBasePEOSubordinateControlsCode | SUBORDINATE_CONTROLS_CODE | — | — |
| 34 | AssessmentBasePEOSurveyPrefixName | SURVEY_PREFIX_NAME | — | — |

### [[grc_asmt_issue_result_v|GRC_ASMT_ISSUE_RESULT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentIssueResultPEOAssessmentResultId | ASSESSMENT_RESULT_ID | — | ✅ |
| 2 | AssessmentIssueResultPEOAssociationId | ASSOCIATION_ID | — | — |
| 3 | AssessmentIssueResultPEOChildObjectTypeId | CHILD_OBJECT_TYPE_ID | — | — |
| 4 | AssessmentIssueResultPEOCreatedBy | CREATED_BY | — | — |
| 5 | AssessmentIssueResultPEOCreationDate | CREATION_DATE | — | — |
| 6 | AssessmentIssueResultPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | AssessmentIssueResultPEOIssueId | ISSUE_ID | — | ✅ |
| 8 | AssessmentIssueResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AssessmentIssueResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AssessmentIssueResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AssessmentIssueResultPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 12 | AssessmentIssueResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | AssessmentIssueResultPEORevisionDate | REVISION_DATE | — | — |
| 14 | AssessmentIssueResultPEORevisionNumber | REVISION_NUMBER | — | — |
| 15 | AssessmentIssueResultPEORiskAnalysisId | RISK_ANALYSIS_ID | — | — |
| 16 | AssessmentIssueResultPEORiskEvaluationId | RISK_EVALUATION_ID | — | — |
| 17 | AssessmentIssueResultPEOTreatmentId | TREATMENT_ID | — | — |

### [[grc_asmt_result_v|GRC_ASMT_RESULT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentResultBasePEOActivityCode | ACTIVITY_CODE | — | — |
| 2 | AssessmentResultBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 3 | AssessmentResultBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 4 | AssessmentResultBasePEOApprovedDate | APPROVED_DATE | — | ✅ |
| 5 | AssessmentResultBasePEOAssessedBy | ASSESSED_BY | — | ✅ |
| 6 | AssessmentResultBasePEOAssessedDate | ASSESSED_DATE | — | ✅ |
| 7 | AssessmentResultBasePEOAssessmentId | ASSESSMENT_ID | — | — |
| 8 | AssessmentResultBasePEOAssociationId | ASSOCIATION_ID | — | — |
| 9 | AssessmentResultBasePEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 10 | AssessmentResultBasePEOCreatedBy | CREATED_BY | — | — |
| 11 | AssessmentResultBasePEOCreationDate | CREATION_DATE | — | — |
| 12 | AssessmentResultBasePEODueDate | DUE_DATE | — | ✅ |
| 13 | AssessmentResultBasePEOFlexObjectTypeKey | FLEX_OBJECT_TYPE_KEY | — | — |
| 14 | AssessmentResultBasePEOFlexTemplateModuleId | FLEX_TEMPLATE_MODULE_ID | — | — |
| 15 | AssessmentResultBasePEOLastStateCode | LAST_STATE_CODE | — | ✅ |
| 16 | AssessmentResultBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AssessmentResultBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | AssessmentResultBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | AssessmentResultBasePEOObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 20 | AssessmentResultBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | AssessmentResultBasePEOResponseCode | RESPONSE_CODE | — | ✅ |
| 22 | AssessmentResultBasePEOResultId | RESULT_ID | 🔑 | ✅ |
| 23 | AssessmentResultBasePEOResultSummary | RESULT_SUMMARY | — | ✅ |
| 24 | AssessmentResultBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 25 | AssessmentResultBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 26 | AssessmentResultBasePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 27 | AssessmentResultBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 28 | AssessmentResultBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 29 | AssessmentResultBasePEOStateCode | STATE_CODE | — | ✅ |
| 30 | AssessmentResultBasePEOStateDate | STATE_DATE | — | — |
| 31 | AssessmentResultBasePEOStatus | STATUS | — | ✅ |
| 32 | AssessmentResultBasePEOSurveyId | SURVEY_ID | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCScSecurityPEOAccessorId | ACCESSOR_ID | — | ✅ |
| 2 | FRCScSecurityPEOAccessorType | ACCESSOR_TYPE | — | — |
| 3 | FRCScSecurityPEOId | ID | — | — |
| 4 | FRCScSecurityPEOIsApprover | IS_APPROVER | — | ✅ |
| 5 | FRCScSecurityPEOIsAssessor | IS_ASSESSOR | — | ✅ |
| 6 | FRCScSecurityPEOIsEditor | IS_EDITOR | — | ✅ |
| 7 | FRCScSecurityPEOIsIssueOwner | IS_ISSUE_OWNER | — | ✅ |
| 8 | FRCScSecurityPEOIsIssueValidator | IS_ISSUE_VALIDATOR | — | ✅ |
| 9 | FRCScSecurityPEOIsManager | IS_MANAGER | — | ✅ |
| 10 | FRCScSecurityPEOIsOwner | IS_OWNER | — | ✅ |
| 11 | FRCScSecurityPEOIsReviewer | IS_REVIEWER | — | ✅ |
| 12 | FRCScSecurityPEOIsViewer | IS_VIEWER | — | ✅ |
| 13 | FRCScSecurityPEORoleBitmap | ROLE_BITMAP | — | — |
| 14 | FRCScSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 15 | FRCScSecurityPEOSecurableType | SECURABLE_TYPE | — | — |

### [[gtg_sc_group_vl|GTG_SC_GROUP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecurityGroupPEOGroupId | GROUP_ID | — | ✅ |
| 2 | SecurityGroupPEOName | NAME | — | ✅ |
| 3 | SecurityGroupPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 4 | SecurityGroupPEORoleType | ROLE_TYPE | — | ✅ |
| 5 | SecurityGroupPEOSecurableType | SECURABLE_TYPE | — | ✅ |

### [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScSecurityPrivPEOId | ID | — | — |
| 2 | ScSecurityPrivPEOPrivilegeCode | PRIVILEGE_CODE | — | — |
| 3 | ScSecurityPrivPEORoleType | ROLE_TYPE | — | ✅ |
| 4 | ScSecurityPrivPEOSecurableType | SECURABLE_TYPE | — | — |

### [[gtg_sc_user_group|GTG_SC_USER_GROUP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScSecurityUserGroupPEOCreatedBy | CREATED_BY | — | — |
| 2 | ScSecurityUserGroupPEOCrtnDt | CREATION_DATE | — | — |
| 3 | ScSecurityUserGroupPEOGroupId | GROUP_ID | — | — |
| 4 | ScSecurityUserGroupPEOId | ID | — | — |
| 5 | ScSecurityUserGroupPEOIsOrphan | IS_ORPHAN | — | ✅ |
| 6 | ScSecurityUserGroupPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 7 | ScSecurityUserGroupPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 8 | ScSecurityUserGroupPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 9 | ScSecurityUserGroupPEOUserId | USER_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsRsPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | AsRsPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AsRsPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AsRsPersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | AsRsPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | AsRsPersonAssessedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | AsRsPersonAssessedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | AsRsPersonAssessedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | AsRsPersonAssessedByPersonId | PERSON_ID | — | — |
| 10 | AsRsPersonAssessedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | AsRsPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | AsRsPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | AsRsPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | AsRsPersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | AsRsPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | AsRsPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | AsRsPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | AsRsPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | AsRsPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | AsRsPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsRsApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | AsRsApprovedByPersonId | PERSON_ID | — | — |
| 3 | AsRsApprovedByUserGuid | USER_GUID | — | — |
| 4 | AsRsApprovedByUserId | USER_ID | — | — |
| 5 | AsRsApprovedByUsername | USERNAME | — | — |
| 6 | AsRsAssessedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | AsRsAssessedByPersonId | PERSON_ID | — | — |
| 8 | AsRsAssessedByUserGuid | USER_GUID | — | — |
| 9 | AsRsAssessedByUserId | USER_ID | — | — |
| 10 | AsRsAssessedByUsername | USERNAME | — | — |
| 11 | AsRsReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AsRsReviewedByPersonId | PERSON_ID | — | — |
| 13 | AsRsReviewedByUserGuid | USER_GUID | — | — |
| 14 | AsRsReviewedByUserId | USER_ID | — | — |
| 15 | AsRsReviewedByUsername | USERNAME | — | — |
| 16 | AsRsUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | AsRsUpdatedByPersonId | PERSON_ID | — | — |
| 18 | AsRsUpdatedByUserGuid | USER_GUID | — | — |
| 19 | AsRsUpdatedByUserId | USER_ID | — | — |
| 20 | AsRsUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
