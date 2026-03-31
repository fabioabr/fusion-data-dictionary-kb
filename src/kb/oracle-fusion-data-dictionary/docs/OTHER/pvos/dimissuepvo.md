---
id: DOC-OTHER-PVO-DimIssuePVO
doc_type: system-doc
title: "DimIssuePVO — PVO Cross-Module"
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
  - DimIssuePVO
  - dimissuepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DimIssuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dim Issue. Acessa as tabelas: GRC_COMMENT, GRC_ISSU_ISSUE_B, GRC_ISSU_ISSUE_TL (+8).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.DimIssuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 241 | 11 | 1 | 67 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[grc_comment|GRC_COMMENT]] — 13 atributos (5 BICC)
- [[grc_issu_issue_b|GRC_ISSU_ISSUE_B]] — 119 atributos (1 PKs, 27 BICC)
- [[grc_issu_issue_tl|GRC_ISSU_ISSUE_TL]] — 11 atributos (3 BICC)
- [[gtg_frc_rec_origin_otbi_v|GTG_FRC_REC_ORIGIN_OTBI_V]] — 12 atributos (9 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[gtg_sc_frc_security_v|GTG_SC_FRC_SECURITY_V]] — 15 atributos (11 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 25 atributos (5 BICC)
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
| 5 | CommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CommentsPEOObjectEffectiveSequence | OBJECT_EFFECTIVE_SEQUENCE | — | — |
| 9 | CommentsPEOObjectId | OBJECT_ID | — | — |
| 10 | CommentsPEOObjectStateCode | OBJECT_STATE_CODE | — | ✅ |
| 11 | CommentsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 12 | CommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CommentsPEOUserComment | USER_COMMENT | — | ✅ |

### [[grc_issu_issue_b|GRC_ISSU_ISSUE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueBasePEOAction | ACTION | — | — |
| 2 | IssueBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | ✅ |
| 3 | IssueBasePEOApprovedBy | APPROVED_BY | — | ✅ |
| 4 | IssueBasePEOApprovedDate | APPROVED_DATE | — | — |
| 5 | IssueBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | IssueBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | IssueBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | IssueBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 9 | IssueBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 10 | IssueBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 11 | IssueBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 12 | IssueBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 13 | IssueBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 14 | IssueBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 15 | IssueBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 16 | IssueBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 17 | IssueBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 18 | IssueBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 19 | IssueBasePEOAttributeChar21 | ATTRIBUTE_CHAR21 | — | — |
| 20 | IssueBasePEOAttributeChar22 | ATTRIBUTE_CHAR22 | — | — |
| 21 | IssueBasePEOAttributeChar23 | ATTRIBUTE_CHAR23 | — | — |
| 22 | IssueBasePEOAttributeChar24 | ATTRIBUTE_CHAR24 | — | — |
| 23 | IssueBasePEOAttributeChar25 | ATTRIBUTE_CHAR25 | — | — |
| 24 | IssueBasePEOAttributeChar26 | ATTRIBUTE_CHAR26 | — | — |
| 25 | IssueBasePEOAttributeChar27 | ATTRIBUTE_CHAR27 | — | — |
| 26 | IssueBasePEOAttributeChar28 | ATTRIBUTE_CHAR28 | — | — |
| 27 | IssueBasePEOAttributeChar29 | ATTRIBUTE_CHAR29 | — | — |
| 28 | IssueBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 29 | IssueBasePEOAttributeChar30 | ATTRIBUTE_CHAR30 | — | — |
| 30 | IssueBasePEOAttributeChar31 | ATTRIBUTE_CHAR31 | — | — |
| 31 | IssueBasePEOAttributeChar32 | ATTRIBUTE_CHAR32 | — | — |
| 32 | IssueBasePEOAttributeChar33 | ATTRIBUTE_CHAR33 | — | — |
| 33 | IssueBasePEOAttributeChar34 | ATTRIBUTE_CHAR34 | — | — |
| 34 | IssueBasePEOAttributeChar35 | ATTRIBUTE_CHAR35 | — | — |
| 35 | IssueBasePEOAttributeChar36 | ATTRIBUTE_CHAR36 | — | — |
| 36 | IssueBasePEOAttributeChar37 | ATTRIBUTE_CHAR37 | — | — |
| 37 | IssueBasePEOAttributeChar38 | ATTRIBUTE_CHAR38 | — | — |
| 38 | IssueBasePEOAttributeChar39 | ATTRIBUTE_CHAR39 | — | — |
| 39 | IssueBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 40 | IssueBasePEOAttributeChar40 | ATTRIBUTE_CHAR40 | — | — |
| 41 | IssueBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 42 | IssueBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 43 | IssueBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 44 | IssueBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 45 | IssueBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 46 | IssueBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 47 | IssueBasePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 48 | IssueBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 49 | IssueBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 50 | IssueBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 51 | IssueBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 52 | IssueBasePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 53 | IssueBasePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 54 | IssueBasePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 55 | IssueBasePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 56 | IssueBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 57 | IssueBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 58 | IssueBasePEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 59 | IssueBasePEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 60 | IssueBasePEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 61 | IssueBasePEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 62 | IssueBasePEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 63 | IssueBasePEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 64 | IssueBasePEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 65 | IssueBasePEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 66 | IssueBasePEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 67 | IssueBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 68 | IssueBasePEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 69 | IssueBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 70 | IssueBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 71 | IssueBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 72 | IssueBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 73 | IssueBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 74 | IssueBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 75 | IssueBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 76 | IssueBasePEOCategoryCode | CATEGORY_CODE | — | — |
| 77 | IssueBasePEOClosedDate | CLOSED_DATE | — | ✅ |
| 78 | IssueBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 79 | IssueBasePEOCreationDate | CREATION_DATE | — | — |
| 80 | IssueBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 81 | IssueBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 82 | IssueBasePEOFlxPerspItemId | FLX_PERSP_ITEM_ID | — | — |
| 83 | IssueBasePEOHoldDate | HOLD_DATE | — | ✅ |
| 84 | IssueBasePEOImpactCost | IMPACT_COST | — | ✅ |
| 85 | IssueBasePEOIncidentFlag | INCIDENT_FLAG | — | — |
| 86 | IssueBasePEOIsCommon | IS_COMMON | — | — |
| 87 | IssueBasePEOIssueDate | ISSUE_DATE | — | ✅ |
| 88 | IssueBasePEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 89 | IssueBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 90 | IssueBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 91 | IssueBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 92 | IssueBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 93 | IssueBasePEOLikelihoodCode | LIKELIHOOD_CODE | — | ✅ |
| 94 | IssueBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | IssueBasePEOOpenDate | OPEN_DATE | — | ✅ |
| 96 | IssueBasePEOOriginObjectId | ORIGIN_OBJECT_ID | — | ✅ |
| 97 | IssueBasePEOOriginObjectTypeCode | ORIGIN_OBJECT_TYPE_CODE | — | ✅ |
| 98 | IssueBasePEOOriginator | ORIGINATOR | — | ✅ |
| 99 | IssueBasePEOOriginatorUser | ORIGINATOR_USER | — | — |
| 100 | IssueBasePEOReasonCode | REASON_CODE | — | — |
| 101 | IssueBasePEORemedDate | REMED_DATE | — | ✅ |
| 102 | IssueBasePEORemedFlag | REMED_FLAG | — | ✅ |
| 103 | IssueBasePEORemediationCost | REMEDIATION_COST | — | ✅ |
| 104 | IssueBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 105 | IssueBasePEOReviewedBy | REVIEWED_BY | — | ✅ |
| 106 | IssueBasePEOReviewedDate | REVIEWED_DATE | — | — |
| 107 | IssueBasePEORevisionDate | REVISION_DATE | — | ✅ |
| 108 | IssueBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 109 | IssueBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 110 | IssueBasePEOSeverity | SEVERITY | — | ✅ |
| 111 | IssueBasePEOSource | SOURCE | — | — |
| 112 | IssueBasePEOStartDate | START_DATE | — | ✅ |
| 113 | IssueBasePEOStateCode | STATE_CODE | — | ✅ |
| 114 | IssueBasePEOStateDate | STATE_DATE | — | — |
| 115 | IssueBasePEOStatus | STATUS | — | ✅ |
| 116 | IssueBasePEOType | TYPE | — | ✅ |
| 117 | IssueBasePEOValidDate | VALID_DATE | — | ✅ |
| 118 | IssueBasePEOValidatedBy | VALIDATED_BY | — | — |
| 119 | IssueBasePEOValidatedDate | VALIDATED_DATE | — | — |

### [[grc_issu_issue_tl|GRC_ISSU_ISSUE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | IssueTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | IssueTranslationPEODescription | DESCRIPTION | — | — |
| 4 | IssueTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | IssueTranslationPEOIssueId | ISSUE_ID | — | — |
| 6 | IssueTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | IssueTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IssueTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | IssueTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | IssueTranslationPEOName | NAME | — | ✅ |
| 11 | IssueTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_frc_rec_origin_otbi_v|GTG_FRC_REC_ORIGIN_OTBI_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecordOfOriginPEOAnalysisDate | ANALYSIS_DATE | — | ✅ |
| 2 | RecordOfOriginPEOAsmtctrlName | ASSESSMENT_CTRLNAME | — | ✅ |
| 3 | RecordOfOriginPEOAsmtprocName | ASSESSMENT_PROCNAME | — | ✅ |
| 4 | RecordOfOriginPEOAsmtrskName | ASSESSMENT_RSKNAME | — | ✅ |
| 5 | RecordOfOriginPEOControlName | CONTROL_NAME | — | ✅ |
| 6 | RecordOfOriginPEOIssueId | ISSUE_ID | — | — |
| 7 | RecordOfOriginPEOOrigObjTypeCode | ORIGIN_OBJECT_TYPE_CODE | — | — |
| 8 | RecordOfOriginPEOOrigObjectId | ORIGIN_OBJECT_ID | — | — |
| 9 | RecordOfOriginPEOProcessName | PROCESS_NAME | — | ✅ |
| 10 | RecordOfOriginPEORiskEvalDate | RISK_EVALUATION_DATE | — | ✅ |
| 11 | RecordOfOriginPEORiskName | RISK_NAME | — | ✅ |
| 12 | RecordOfOriginPEORsktrtmntplnName | RISKTREATMENT_PLANNAME | — | ✅ |

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
| 1 | IssuePersonApprovedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | IssuePersonApprovedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | IssuePersonApprovedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | IssuePersonApprovedByPersonId | PERSON_ID | — | — |
| 5 | IssuePersonApprovedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | IssuePersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | IssuePersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | IssuePersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | IssuePersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | IssuePersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | IssuePersonReviewedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | IssuePersonReviewedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | IssuePersonReviewedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | IssuePersonReviewedByPersonId | PERSON_ID | — | — |
| 15 | IssuePersonReviewedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | IssuePersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | IssuePersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | IssuePersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | IssuePersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | IssuePersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 21 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 22 | PersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | PersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 24 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 25 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CreatedByPersonId | PERSON_ID | — | — |
| 3 | CreatedByUserGuid | USER_GUID | — | — |
| 4 | CreatedByUserId | USER_ID | — | — |
| 5 | CreatedByUsername | USERNAME | — | — |
| 6 | IssueApprovedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | IssueApprovedByPersonId | PERSON_ID | — | — |
| 8 | IssueApprovedByUserGuid | USER_GUID | — | — |
| 9 | IssueApprovedByUserId | USER_ID | — | — |
| 10 | IssueApprovedByUsername | USERNAME | — | — |
| 11 | IssueCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | IssueCreatedByPersonId | PERSON_ID | — | — |
| 13 | IssueCreatedByUserGuid | USER_GUID | — | — |
| 14 | IssueCreatedByUserId | USER_ID | — | — |
| 15 | IssueCreatedByUsername | USERNAME | — | — |
| 16 | IssueReviewedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | IssueReviewedByPersonId | PERSON_ID | — | — |
| 18 | IssueReviewedByUserGuid | USER_GUID | — | — |
| 19 | IssueReviewedByUserId | USER_ID | — | — |
| 20 | IssueReviewedByUsername | USERNAME | — | — |
| 21 | IssueUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | IssueUpdatedByPersonId | PERSON_ID | — | — |
| 23 | IssueUpdatedByUserGuid | USER_GUID | — | — |
| 24 | IssueUpdatedByUserId | USER_ID | — | — |
| 25 | IssueUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
