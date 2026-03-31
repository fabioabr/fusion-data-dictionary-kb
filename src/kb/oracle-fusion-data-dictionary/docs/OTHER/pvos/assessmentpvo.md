---
id: DOC-OTHER-PVO-AssessmentPVO
doc_type: system-doc
title: "AssessmentPVO — PVO Cross-Module"
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
  - AssessmentPVO
  - assessmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assessment. Acessa as tabelas: GRC_ASMT_ASSESSMENT_B, GRC_ASMT_ASSESSMENT_TL, GRC_ASMT_PLAN_B (+10).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.AssessmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 181 | 13 | 1 | 51 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]] — 38 atributos (1 PKs, 20 BICC)
- [[grc_asmt_assessment_tl|GRC_ASMT_ASSESSMENT_TL]] — 10 atributos (3 BICC)
- [[grc_asmt_plan_b|GRC_ASMT_PLAN_B]] — 40 atributos (2 BICC)
- [[grc_asmt_plan_tl|GRC_ASMT_PLAN_TL]] — 10 atributos (3 BICC)
- [[grc_asmt_template_b|GRC_ASMT_TEMPLATE_B]] — 27 atributos (2 BICC)
- [[grc_asmt_template_tl|GRC_ASMT_TEMPLATE_TL]] — 10 atributos (3 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (10 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos

---

## ⚙️ Atributos

### [[grc_asmt_assessment_b|GRC_ASMT_ASSESSMENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentBasePEOAllowDuplication | ALLOW_DUPLICATION | — | — |
| 2 | AssessmentBasePEOAsmtPlanEffseq | ASMT_PLAN_EFFSEQ | — | — |
| 3 | AssessmentBasePEOAsmtPlanId | ASMT_PLAN_ID | — | — |
| 4 | AssessmentBasePEOAssessmentCategoryCode | ASSESSMENT_CATEGORY_CODE | — | ✅ |
| 5 | AssessmentBasePEOAssessmentId | ASSESSMENT_ID | 🔑 | ✅ |
| 6 | AssessmentBasePEOAssessmentInitiateDate | ASSESSMENT_INITIATE_DATE | — | ✅ |
| 7 | AssessmentBasePEOBusEntityAsmtCode | BUS_ENTITY_ASMT_CODE | — | — |
| 8 | AssessmentBasePEOBusEntityAuditTestCode | BUS_ENTITY_AUDIT_TEST_CODE | — | — |
| 9 | AssessmentBasePEOCompensatingSelectionCode | COMPENSATING_SELECTION_CODE | — | ✅ |
| 10 | AssessmentBasePEOCreatedBy | CREATED_BY | — | — |
| 11 | AssessmentBasePEOCreationDate | CREATION_DATE | — | — |
| 12 | AssessmentBasePEODuplication | DUPLICATION | — | — |
| 13 | AssessmentBasePEOIsSurvMndtry | IS_SURVEY_MANDATORY | — | — |
| 14 | AssessmentBasePEOKeySelectionCode | KEY_SELECTION_CODE | — | ✅ |
| 15 | AssessmentBasePEOLastStateCode | LAST_STATE_CODE | — | ✅ |
| 16 | AssessmentBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | AssessmentBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | AssessmentBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | AssessmentBasePEOMitigatingSelectionCode | MITIGATING_SELECTION_CODE | — | ✅ |
| 20 | AssessmentBasePEOMonitoringSelectionCode | MONITORING_SELECTION_CODE | — | — |
| 21 | AssessmentBasePEONoSelectionCode | NO_SELECTION_CODE | — | ✅ |
| 22 | AssessmentBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AssessmentBasePEOOtherSelectionCode | OTHER_SELECTION_CODE | — | ✅ |
| 24 | AssessmentBasePEOOwner | OWNER | — | — |
| 25 | AssessmentBasePEOPerspAssociated | PERSPECTIVE_ASSOCIATED | — | — |
| 26 | AssessmentBasePEOPerspItemId | PERSP_ITEM_ID | — | — |
| 27 | AssessmentBasePEOPerspTreeEffseq | PERSP_TREE_EFFSEQ | — | — |
| 28 | AssessmentBasePEOPerspTreeId | PERSP_TREE_ID | — | — |
| 29 | AssessmentBasePEOPrimaryControlsCode | PRIMARY_CONTROLS_CODE | — | ✅ |
| 30 | AssessmentBasePEORedundantSelectionCode | REDUNDANT_SELECTION_CODE | — | ✅ |
| 31 | AssessmentBasePEOResultsEntryCompletionDate | RESULTS_ENTRY_COMPLETION_DATE | — | ✅ |
| 32 | AssessmentBasePEOResultsEntryDueDate | RESULTS_ENTRY_DUE_DATE | — | ✅ |
| 33 | AssessmentBasePEOResultsEntryStartDate | RESULTS_ENTRY_START_DATE | — | ✅ |
| 34 | AssessmentBasePEORootObjectTypeCode | ROOT_OBJECT_TYPE_CODE | — | ✅ |
| 35 | AssessmentBasePEOStateCode | STATE_CODE | — | ✅ |
| 36 | AssessmentBasePEOStateDate | STATE_DATE | — | — |
| 37 | AssessmentBasePEOSubordinateControlsCode | SUBORDINATE_CONTROLS_CODE | — | ✅ |
| 38 | AssessmentBasePEOSurveyPrefixName | SURVEY_PREFIX_NAME | — | ✅ |

### [[grc_asmt_assessment_tl|GRC_ASMT_ASSESSMENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentTranslationPEOAssessmentId | ASSESSMENT_ID | — | — |
| 2 | AssessmentTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | AssessmentTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | AssessmentTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | AssessmentTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | AssessmentTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssessmentTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AssessmentTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AssessmentTranslationPEOName | NAME | — | ✅ |
| 10 | AssessmentTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_asmt_plan_b|GRC_ASMT_PLAN_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentPlanBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | AssessmentPlanBasePEOApprovedBy | APPROVED_BY | — | — |
| 3 | AssessmentPlanBasePEOApprovedDate | APPROVED_DATE | — | — |
| 4 | AssessmentPlanBasePEOAsmtPlanId | ASMT_PLAN_ID | — | — |
| 5 | AssessmentPlanBasePEOAsmtTemplateEffseq | ASMT_TEMPLATE_EFFSEQ | — | — |
| 6 | AssessmentPlanBasePEOAsmtTemplateId | ASMT_TEMPLATE_ID | — | — |
| 7 | AssessmentPlanBasePEOAssessedBy | ASSESSED_BY | — | — |
| 8 | AssessmentPlanBasePEOAssessedDate | ASSESSED_DATE | — | — |
| 9 | AssessmentPlanBasePEOAssessmentCategoryCode | ASSESSMENT_CATEGORY_CODE | — | — |
| 10 | AssessmentPlanBasePEOBusEntityAsmtCode | BUS_ENTITY_ASMT_CODE | — | — |
| 11 | AssessmentPlanBasePEOBusEntityAuditTestCode | BUS_ENTITY_AUDIT_TEST_CODE | — | — |
| 12 | AssessmentPlanBasePEOCompensatingSelectionCode | COMPENSATING_SELECTION_CODE | — | — |
| 13 | AssessmentPlanBasePEOCreatedBy | CREATED_BY | — | — |
| 14 | AssessmentPlanBasePEOCreationDate | CREATION_DATE | — | — |
| 15 | AssessmentPlanBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 16 | AssessmentPlanBasePEOKeySelectionCode | KEY_SELECTION_CODE | — | — |
| 17 | AssessmentPlanBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 18 | AssessmentPlanBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | AssessmentPlanBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | AssessmentPlanBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | AssessmentPlanBasePEOMitigatingSelectionCode | MITIGATING_SELECTION_CODE | — | — |
| 22 | AssessmentPlanBasePEOMonitoringSelectionCode | MONITORING_SELECTION_CODE | — | — |
| 23 | AssessmentPlanBasePEONoSelectionCode | NO_SELECTION_CODE | — | — |
| 24 | AssessmentPlanBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | AssessmentPlanBasePEOOtherSelectionCode | OTHER_SELECTION_CODE | — | — |
| 26 | AssessmentPlanBasePEOPerspItemId | PERSP_ITEM_ID | — | — |
| 27 | AssessmentPlanBasePEOPerspTreeId | PERSP_TREE_ID | — | — |
| 28 | AssessmentPlanBasePEOPrimaryControlsCode | PRIMARY_CONTROLS_CODE | — | — |
| 29 | AssessmentPlanBasePEORedundantSelectionCode | REDUNDANT_SELECTION_CODE | — | — |
| 30 | AssessmentPlanBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 31 | AssessmentPlanBasePEOReviewedBy | REVIEWED_BY | — | — |
| 32 | AssessmentPlanBasePEOReviewedDate | REVIEWED_DATE | — | — |
| 33 | AssessmentPlanBasePEORevisionDate | REVISION_DATE | — | — |
| 34 | AssessmentPlanBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 35 | AssessmentPlanBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 36 | AssessmentPlanBasePEOStartDate | START_DATE | — | — |
| 37 | AssessmentPlanBasePEOStateCode | STATE_CODE | — | — |
| 38 | AssessmentPlanBasePEOStateDate | STATE_DATE | — | — |
| 39 | AssessmentPlanBasePEOStatus | STATUS | — | ✅ |
| 40 | AssessmentPlanBasePEOSubordinateControlsCode | SUBORDINATE_CONTROLS_CODE | — | — |

### [[grc_asmt_plan_tl|GRC_ASMT_PLAN_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentPlanTranslationPEOAsmtPlanId | ASMT_PLAN_ID | — | — |
| 2 | AssessmentPlanTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | AssessmentPlanTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | AssessmentPlanTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | ✅ |
| 5 | AssessmentPlanTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | AssessmentPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssessmentPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AssessmentPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AssessmentPlanTranslationPEOName | NAME | — | ✅ |
| 10 | AssessmentPlanTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_asmt_template_b|GRC_ASMT_TEMPLATE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentTemplateBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | AssessmentTemplateBasePEOApprovedBy | APPROVED_BY | — | — |
| 3 | AssessmentTemplateBasePEOApprovedDate | APPROVED_DATE | — | — |
| 4 | AssessmentTemplateBasePEOAsmtTemplateId | ASMT_TEMPLATE_ID | — | — |
| 5 | AssessmentTemplateBasePEOAssessedBy | ASSESSED_BY | — | — |
| 6 | AssessmentTemplateBasePEOAssessedDate | ASSESSED_DATE | — | — |
| 7 | AssessmentTemplateBasePEOAssessmentTypeCode | ASSESSMENT_TYPE_CODE | — | ✅ |
| 8 | AssessmentTemplateBasePEOCreatedBy | CREATED_BY | — | — |
| 9 | AssessmentTemplateBasePEOCreationDate | CREATION_DATE | — | — |
| 10 | AssessmentTemplateBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 11 | AssessmentTemplateBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 12 | AssessmentTemplateBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | AssessmentTemplateBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | AssessmentTemplateBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | AssessmentTemplateBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AssessmentTemplateBasePEOPerspTypeCode | PERSP_TYPE_CODE | — | — |
| 17 | AssessmentTemplateBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 18 | AssessmentTemplateBasePEOReviewedBy | REVIEWED_BY | — | — |
| 19 | AssessmentTemplateBasePEOReviewedDate | REVIEWED_DATE | — | — |
| 20 | AssessmentTemplateBasePEORevisionDate | REVISION_DATE | — | — |
| 21 | AssessmentTemplateBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 22 | AssessmentTemplateBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 23 | AssessmentTemplateBasePEORootObjectTypeCode | ROOT_OBJECT_TYPE_CODE | — | — |
| 24 | AssessmentTemplateBasePEOStartDate | START_DATE | — | — |
| 25 | AssessmentTemplateBasePEOStateCode | STATE_CODE | — | — |
| 26 | AssessmentTemplateBasePEOStateDate | STATE_DATE | — | — |
| 27 | AssessmentTemplateBasePEOStatus | STATUS | — | — |

### [[grc_asmt_template_tl|GRC_ASMT_TEMPLATE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentTemplateTranslationPEOAsmtTemplateId | ASMT_TEMPLATE_ID | — | — |
| 2 | AssessmentTemplateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | AssessmentTemplateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | AssessmentTemplateTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | ✅ |
| 5 | AssessmentTemplateTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | AssessmentTemplateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssessmentTemplateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AssessmentTemplateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AssessmentTemplateTranslationPEOName | NAME | — | ✅ |
| 10 | AssessmentTemplateTranslationPEOSourceLang | SOURCE_LANG | — | — |

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
| 1 | AsPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | AsmtPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 3 | AsmtPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AsmtPersonUpdatedByPersonId | PERSON_ID | — | — |
| 5 | AsmtPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | AsmtUpdatedByPersonId | PERSON_ID | — | — |
| 3 | AsmtUpdatedByUserGuid | USER_GUID | — | — |
| 4 | AsmtUpdatedByUserId | USER_ID | — | — |
| 5 | AsmtUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
