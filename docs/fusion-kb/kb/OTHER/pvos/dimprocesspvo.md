---
id: DOC-OTHER-PVO-DimProcessPVO
doc_type: system-doc
title: "DimProcessPVO — PVO Cross-Module"
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
  - DimProcessPVO
  - dimprocesspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DimProcessPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dim Process. Acessa as tabelas: GRC_PROC_PROCESS_B, GRC_PROC_PROCESS_TL, GTG_SC_FRC_ACCESS_V (+6).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.DimProcessPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 114 | 9 | 1 | 39 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[grc_proc_process_b|GRC_PROC_PROCESS_B]] — 27 atributos (1 PKs, 15 BICC)
- [[grc_proc_process_tl|GRC_PROC_PROCESS_TL]] — 11 atributos (3 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (10 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[grc_proc_process_b|GRC_PROC_PROCESS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | ProcessBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 3 | ProcessBasePEOApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | ProcessBasePEOAssessmentFlag | ASSESSMENT_FLAG | — | ✅ |
| 5 | ProcessBasePEOAuditTestingFlag | AUDIT_TESTING_FLAG | — | ✅ |
| 6 | ProcessBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | ProcessBasePEOCreationDate | CREATION_DATE | — | — |
| 8 | ProcessBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 9 | ProcessBasePEOFlexObjectTypeId | FLEX_OBJECT_TYPE_ID | — | — |
| 10 | ProcessBasePEOFlxPerspItemId | FLX_PERSP_ITEM_ID | — | — |
| 11 | ProcessBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 12 | ProcessBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ProcessBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ProcessBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ProcessBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ProcessBasePEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 17 | ProcessBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 18 | ProcessBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 19 | ProcessBasePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 20 | ProcessBasePEORevisionDate | REVISION_DATE | — | ✅ |
| 21 | ProcessBasePEORevisionNumber | REVISION_NUMBER | — | ✅ |
| 22 | ProcessBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 23 | ProcessBasePEOStartDate | START_DATE | — | — |
| 24 | ProcessBasePEOStateCode | STATE_CODE | — | ✅ |
| 25 | ProcessBasePEOStateDate | STATE_DATE | — | — |
| 26 | ProcessBasePEOStatus | STATUS | — | ✅ |
| 27 | ProcessBasePEOType | TYPE | — | ✅ |

### [[grc_proc_process_tl|GRC_PROC_PROCESS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProcessTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProcessTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ProcessTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | ProcessTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ProcessTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProcessTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProcessTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProcessTranslationPEOName | NAME | — | ✅ |
| 10 | ProcessTranslationPEOProcessId | PROCESS_ID | — | — |
| 11 | ProcessTranslationPEOSourceLang | SOURCE_LANG | — | — |

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
| 1 | ProcPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ProcPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ProcPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ProcPersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | ProcPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | ProcPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | ProcPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ProcPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | ProcPersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | ProcPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | ProcPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | ProcPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | ProcPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | ProcPersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | ProcPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | ProcPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | ProcPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | ProcPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | ProcPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | ProcPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ProcApprovedByPersonId | PERSON_ID | — | — |
| 3 | ProcApprovedByUserGuid | USER_GUID | — | — |
| 4 | ProcApprovedByUserId | USER_ID | — | — |
| 5 | ProcApprovedByUsername | USERNAME | — | — |
| 6 | ProcCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProcCreatedByPersonId | PERSON_ID | — | — |
| 8 | ProcCreatedByUserGuid | USER_GUID | — | — |
| 9 | ProcCreatedByUserId | USER_ID | — | — |
| 10 | ProcCreatedByUsername | USERNAME | — | — |
| 11 | ProcReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProcReviewedByPersonId | PERSON_ID | — | — |
| 13 | ProcReviewedByUserGuid | USER_GUID | — | — |
| 14 | ProcReviewedByUserId | USER_ID | — | — |
| 15 | ProcReviewedByUsername | USERNAME | — | — |
| 16 | ProcUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ProcUpdatedByPersonId | PERSON_ID | — | — |
| 18 | ProcUpdatedByUserGuid | USER_GUID | — | — |
| 19 | ProcUpdatedByUserId | USER_ID | — | — |
| 20 | ProcUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
