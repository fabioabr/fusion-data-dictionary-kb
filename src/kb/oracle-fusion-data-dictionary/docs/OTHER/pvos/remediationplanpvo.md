---
id: DOC-OTHER-PVO-RemediationPlanPVO
doc_type: system-doc
title: "RemediationPlanPVO — PVO Cross-Module"
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
  - RemediationPlanPVO
  - remediationplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RemediationPlanPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Remediation Plan. Acessa as tabelas: GRC_COMMENT, GRC_ISSU_RMPLAN_B, GRC_ISSU_RMPLAN_TL (+7).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RemediationPlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 215 | 10 | 1 | 44 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[grc_comment|GRC_COMMENT]] — 15 atributos (3 BICC)
- [[grc_issu_rmplan_b|GRC_ISSU_RMPLAN_B]] — 103 atributos (1 PKs, 19 BICC)
- [[grc_issu_rmplan_tl|GRC_ISSU_RMPLAN_TL]] — 11 atributos (2 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (10 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 25 atributos (3 BICC)
- [[per_users|PER_USERS]] — 25 atributos

---

## ⚙️ Atributos

### [[grc_comment|GRC_COMMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CommentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CommentsPEODelegated | DELEGATED | — | — |
| 4 | CommentsPEOId | ID | — | — |
| 5 | CommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | CommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CommentsPEONextStateCode | NEXT_STATE_CODE | — | — |
| 9 | CommentsPEOObjectEffectiveSequence | OBJECT_EFFECTIVE_SEQUENCE | — | — |
| 10 | CommentsPEOObjectId | OBJECT_ID | — | — |
| 11 | CommentsPEOObjectStateCode | OBJECT_STATE_CODE | — | — |
| 12 | CommentsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 13 | CommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CommentsPEORvwAprvAction | REVIEW_APPROVE_ACTION | — | — |
| 15 | CommentsPEOUserComment | USER_COMMENT | — | ✅ |

### [[grc_issu_rmplan_b|GRC_ISSU_RMPLAN_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RemediationPlanBasePEOAction | ACTION | — | ✅ |
| 2 | RemediationPlanBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | ✅ |
| 3 | RemediationPlanBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 4 | RemediationPlanBasePEOApprovedDate | APPROVED_DATE | — | — |
| 5 | RemediationPlanBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | RemediationPlanBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | RemediationPlanBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | RemediationPlanBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 9 | RemediationPlanBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 10 | RemediationPlanBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 11 | RemediationPlanBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 12 | RemediationPlanBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 13 | RemediationPlanBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 14 | RemediationPlanBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 15 | RemediationPlanBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 16 | RemediationPlanBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 17 | RemediationPlanBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 18 | RemediationPlanBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 19 | RemediationPlanBasePEOAttributeChar21 | ATTRIBUTE_CHAR21 | — | — |
| 20 | RemediationPlanBasePEOAttributeChar22 | ATTRIBUTE_CHAR22 | — | — |
| 21 | RemediationPlanBasePEOAttributeChar23 | ATTRIBUTE_CHAR23 | — | — |
| 22 | RemediationPlanBasePEOAttributeChar24 | ATTRIBUTE_CHAR24 | — | — |
| 23 | RemediationPlanBasePEOAttributeChar25 | ATTRIBUTE_CHAR25 | — | — |
| 24 | RemediationPlanBasePEOAttributeChar26 | ATTRIBUTE_CHAR26 | — | — |
| 25 | RemediationPlanBasePEOAttributeChar27 | ATTRIBUTE_CHAR27 | — | — |
| 26 | RemediationPlanBasePEOAttributeChar28 | ATTRIBUTE_CHAR28 | — | — |
| 27 | RemediationPlanBasePEOAttributeChar29 | ATTRIBUTE_CHAR29 | — | — |
| 28 | RemediationPlanBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 29 | RemediationPlanBasePEOAttributeChar30 | ATTRIBUTE_CHAR30 | — | — |
| 30 | RemediationPlanBasePEOAttributeChar31 | ATTRIBUTE_CHAR31 | — | — |
| 31 | RemediationPlanBasePEOAttributeChar32 | ATTRIBUTE_CHAR32 | — | — |
| 32 | RemediationPlanBasePEOAttributeChar33 | ATTRIBUTE_CHAR33 | — | — |
| 33 | RemediationPlanBasePEOAttributeChar34 | ATTRIBUTE_CHAR34 | — | — |
| 34 | RemediationPlanBasePEOAttributeChar35 | ATTRIBUTE_CHAR35 | — | — |
| 35 | RemediationPlanBasePEOAttributeChar36 | ATTRIBUTE_CHAR36 | — | — |
| 36 | RemediationPlanBasePEOAttributeChar37 | ATTRIBUTE_CHAR37 | — | — |
| 37 | RemediationPlanBasePEOAttributeChar38 | ATTRIBUTE_CHAR38 | — | — |
| 38 | RemediationPlanBasePEOAttributeChar39 | ATTRIBUTE_CHAR39 | — | — |
| 39 | RemediationPlanBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 40 | RemediationPlanBasePEOAttributeChar40 | ATTRIBUTE_CHAR40 | — | — |
| 41 | RemediationPlanBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 42 | RemediationPlanBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 43 | RemediationPlanBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 44 | RemediationPlanBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 45 | RemediationPlanBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 46 | RemediationPlanBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 47 | RemediationPlanBasePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 48 | RemediationPlanBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 49 | RemediationPlanBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 50 | RemediationPlanBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 51 | RemediationPlanBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 52 | RemediationPlanBasePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 53 | RemediationPlanBasePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 54 | RemediationPlanBasePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 55 | RemediationPlanBasePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 56 | RemediationPlanBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 57 | RemediationPlanBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 58 | RemediationPlanBasePEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 59 | RemediationPlanBasePEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 60 | RemediationPlanBasePEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 61 | RemediationPlanBasePEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 62 | RemediationPlanBasePEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 63 | RemediationPlanBasePEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 64 | RemediationPlanBasePEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 65 | RemediationPlanBasePEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 66 | RemediationPlanBasePEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 67 | RemediationPlanBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 68 | RemediationPlanBasePEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 69 | RemediationPlanBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 70 | RemediationPlanBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 71 | RemediationPlanBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 72 | RemediationPlanBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 73 | RemediationPlanBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 74 | RemediationPlanBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 75 | RemediationPlanBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 76 | RemediationPlanBasePEOCategoryCode | CATEGORY_CODE | — | — |
| 77 | RemediationPlanBasePEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 78 | RemediationPlanBasePEOCreatedBy | CREATED_BY | — | — |
| 79 | RemediationPlanBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 80 | RemediationPlanBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 81 | RemediationPlanBasePEODueDate | DUE_DATE | — | ✅ |
| 82 | RemediationPlanBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 83 | RemediationPlanBasePEOEstimatedCompletionDate | ESTIMATED_COMPLETION_DATE | — | ✅ |
| 84 | RemediationPlanBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 85 | RemediationPlanBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 86 | RemediationPlanBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 87 | RemediationPlanBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 88 | RemediationPlanBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | RemediationPlanBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 90 | RemediationPlanBasePEOProgressCode | PROGRESS_CODE | — | ✅ |
| 91 | RemediationPlanBasePEORemedCost | REMED_COST | — | — |
| 92 | RemediationPlanBasePEORemedPlanId | REMED_PLAN_ID | 🔑 | ✅ |
| 93 | RemediationPlanBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 94 | RemediationPlanBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 95 | RemediationPlanBasePEOReviewedDate | REVIEWED_DATE | — | ✅ |
| 96 | RemediationPlanBasePEORevisionDate | REVISION_DATE | — | — |
| 97 | RemediationPlanBasePEORevisionNumber | REVISION_NUMBER | — | ✅ |
| 98 | RemediationPlanBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 99 | RemediationPlanBasePEOStartDate | START_DATE | — | ✅ |
| 100 | RemediationPlanBasePEOStateCode | STATE_CODE | — | ✅ |
| 101 | RemediationPlanBasePEOStateDate | STATE_DATE | — | — |
| 102 | RemediationPlanBasePEOStatus | STATUS | — | ✅ |
| 103 | RemediationPlanBasePEOType | TYPE | — | — |

### [[grc_issu_rmplan_tl|GRC_ISSU_RMPLAN_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RemediationPlanTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | RemediationPlanTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RemediationPlanTransPEODescription | DESCRIPTION | — | — |
| 4 | RemediationPlanTransPEODetailedDescription | DETAILED_DESCRIPTION | — | — |
| 5 | RemediationPlanTransPEOLanguage | LANGUAGE | — | — |
| 6 | RemediationPlanTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RemediationPlanTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RemediationPlanTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RemediationPlanTransPEOName | NAME | — | ✅ |
| 10 | RemediationPlanTransPEORemedPlanId | REMED_PLAN_ID | — | — |
| 11 | RemediationPlanTransPEOSourceLang | SOURCE_LANG | — | — |

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
| 1 | CmntPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | CmntPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CmntPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CmntPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | CmntPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | RmPnPersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | RmPnPersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RmPnPersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RmPnPersonApprovedByPersonId | PERSON_ID | — | — |
| 10 | RmPnPersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | RmPnPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 12 | RmPnPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | RmPnPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | RmPnPersonCreatedByPersonId | PERSON_ID | — | — |
| 15 | RmPnPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | RmPnPersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | RmPnPersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | RmPnPersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | RmPnPersonReviewedByPersonId | PERSON_ID | — | — |
| 20 | RmPnPersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 21 | RmPnPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 22 | RmPnPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | RmPnPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 24 | RmPnPersonUpdatedByPersonId | PERSON_ID | — | — |
| 25 | RmPnPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmntCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CmntCreatedByPersonId | PERSON_ID | — | — |
| 3 | CmntCreatedByUserGuid | USER_GUID | — | — |
| 4 | CmntCreatedByUserId | USER_ID | — | — |
| 5 | CmntCreatedByUsername | USERNAME | — | — |
| 6 | RmPnApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RmPnApprovedByPersonId | PERSON_ID | — | — |
| 8 | RmPnApprovedByUserGuid | USER_GUID | — | — |
| 9 | RmPnApprovedByUserId | USER_ID | — | — |
| 10 | RmPnApprovedByUsername | USERNAME | — | — |
| 11 | RmPnCreatdByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RmPnCreatedByPersonId | PERSON_ID | — | — |
| 13 | RmPnCreatedByUserGuid | USER_GUID | — | — |
| 14 | RmPnCreatedByUserId | USER_ID | — | — |
| 15 | RmPnCreatedByUsername | USERNAME | — | — |
| 16 | RmPnReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | RmPnReviewedByPersonId | PERSON_ID | — | — |
| 18 | RmPnReviewedByUserGuid | USER_GUID | — | — |
| 19 | RmPnReviewedByUserId | USER_ID | — | — |
| 20 | RmPnReviewedByUsername | USERNAME | — | — |
| 21 | RmPnUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | RmPnUpdatedByPersonId | PERSON_ID | — | — |
| 23 | RmPnUpdatedByUserGuid | USER_GUID | — | — |
| 24 | RmPnUpdatedByUserId | USER_ID | — | — |
| 25 | RmPnUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
