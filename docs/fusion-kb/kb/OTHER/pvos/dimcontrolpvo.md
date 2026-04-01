---
id: DOC-OTHER-PVO-DimControlPVO
doc_type: system-doc
title: "DimControlPVO — PVO Cross-Module"
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
  - DimControlPVO
  - dimcontrolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DimControlPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dim Control. Acessa as tabelas: GRC_CONTROL_B, GRC_CONTROL_TL, GRC_CTRL_ASSERTION_V (+7).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.DimControlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 129 | 10 | 1 | 50 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[grc_control_b|GRC_CONTROL_B]] — 36 atributos (1 PKs, 21 BICC)
- [[grc_control_tl|GRC_CONTROL_TL]] — 11 atributos (2 BICC)
- [[grc_ctrl_assertion_v|GRC_CTRL_ASSERTION_V]] — 6 atributos (5 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (11 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[grc_control_b|GRC_CONTROL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBasePEOAccessType | ACCESS_TYPE | — | — |
| 2 | ControlBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 3 | ControlBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 4 | ControlBasePEOApprovedDate | APPROVED_DATE | — | ✅ |
| 5 | ControlBasePEOAssessmentFlag | ASSESSMENT_FLAG | — | ✅ |
| 6 | ControlBasePEOAuditTestingFlag | AUDIT_TESTING_FLAG | — | ✅ |
| 7 | ControlBasePEOControlAudit | CONTROL_AUDIT | — | ✅ |
| 8 | ControlBasePEOControlCost | CONTROL_COST | — | ✅ |
| 9 | ControlBasePEOControlCostCurrency | CONTROL_COST_CURRENCY | — | — |
| 10 | ControlBasePEOControlFrequency | CONTROL_FREQUENCY | — | ✅ |
| 11 | ControlBasePEOControlId | CONTROL_ID | 🔑 | ✅ |
| 12 | ControlBasePEOControlKey | CONTROL_KEY | — | — |
| 13 | ControlBasePEOControlMethod | CONTROL_METHOD | — | ✅ |
| 14 | ControlBasePEOControlType | CONTROL_TYPE | — | ✅ |
| 15 | ControlBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | ControlBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | ControlBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 18 | ControlBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 19 | ControlBasePEOEnforcementType | ENFORCEMENT_TYPE | — | ✅ |
| 20 | ControlBasePEOFlexObjectTypeId | FLEX_OBJECT_TYPE_ID | — | — |
| 21 | ControlBasePEOFlxPerspItemId | FLX_PERSP_ITEM_ID | — | — |
| 22 | ControlBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 23 | ControlBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | ControlBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | ControlBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | ControlBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ControlBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 28 | ControlBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 29 | ControlBasePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 30 | ControlBasePEORevisionDate | REVISION_DATE | — | — |
| 31 | ControlBasePEORevisionNumber | REVISION_NUMBER | — | ✅ |
| 32 | ControlBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 33 | ControlBasePEOStartDate | START_DATE | — | — |
| 34 | ControlBasePEOStateCode | STATE_CODE | — | ✅ |
| 35 | ControlBasePEOStateDate | STATE_DATE | — | — |
| 36 | ControlBasePEOStatus | STATUS | — | ✅ |

### [[grc_control_tl|GRC_CONTROL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlTranslationPEOControlId | CONTROL_ID | — | — |
| 2 | ControlTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ControlTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ControlTranslationPEODescription | DESCRIPTION | — | — |
| 5 | ControlTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | — |
| 6 | ControlTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ControlTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ControlTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ControlTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ControlTranslationPEOName | NAME | — | ✅ |
| 11 | ControlTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_ctrl_assertion_v|GRC_CTRL_ASSERTION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlAssertionPEOCompleteness | COMPLETENESS | — | ✅ |
| 2 | ControlAssertionPEOControlId | CONTROL_ID | — | — |
| 3 | ControlAssertionPEOExistenceOccurrence | EXISTENCE_OCCURRENCE | — | ✅ |
| 4 | ControlAssertionPEOPresentationDisclosure | PRESENTATION_DISCLOSURE | — | ✅ |
| 5 | ControlAssertionPEORightsObligation | RIGHTS_OBLIGATION | — | ✅ |
| 6 | ControlAssertionPEOValuationAllocation | VALUATION_ALLOCATION | — | ✅ |

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
| 13 | FRCScSecurityPEORoleBitmap | ROLE_BITMAP | — | ✅ |
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
| 1 | CtrlPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CtrlPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CtrlPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CtrlPersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | CtrlPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | CtrlPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | CtrlPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CtrlPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | CtrlPersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | CtrlPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | CtrlPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | CtrlPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | CtrlPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | CtrlPersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | CtrlPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | CtrlPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | CtrlPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | CtrlPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | CtrlPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | CtrlPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CtrlApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CtrlApprovedByPersonId | PERSON_ID | — | — |
| 3 | CtrlApprovedByUserGuid | USER_GUID | — | — |
| 4 | CtrlApprovedByUserId | USER_ID | — | — |
| 5 | CtrlApprovedByUsername | USERNAME | — | — |
| 6 | CtrlCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | CtrlCreatedByPersonId | PERSON_ID | — | — |
| 8 | CtrlCreatedByUserGuid | USER_GUID | — | — |
| 9 | CtrlCreatedByUserId | USER_ID | — | — |
| 10 | CtrlCreatedByUsername | USERNAME | — | — |
| 11 | CtrlReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CtrlReviewedByPersonId | PERSON_ID | — | — |
| 13 | CtrlReviewedByUserGuid | USER_GUID | — | — |
| 14 | CtrlReviewedByUserId | USER_ID | — | — |
| 15 | CtrlReviewedByUsername | USERNAME | — | — |
| 16 | CtrlUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | CtrlUpdatedByPersonId | PERSON_ID | — | — |
| 18 | CtrlUpdatedByUserGuid | USER_GUID | — | — |
| 19 | CtrlUpdatedByUserId | USER_ID | — | — |
| 20 | CtrlUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
