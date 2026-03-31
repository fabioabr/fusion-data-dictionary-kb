---
id: DOC-OTHER-PVO-AdvancedAccessControlDetailsRefPVO
doc_type: system-doc
title: "AdvancedAccessControlDetailsRefPVO — PVO Cross-Module"
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
  - AdvancedAccessControlDetailsRefPVO
  - advancedaccesscontroldetailsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdvancedAccessControlDetailsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Advanced Access Control Details Ref. Acessa as tabelas: GRC_COMMENT, GRC_CTRL_CCM_CONTROL_TL, GRC_JOB (+11).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.AdvancedAccessControlDetailsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 233 | 14 | 2 | 71 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[grc_comment|GRC_COMMENT]] — 13 atributos (4 BICC)
- [[grc_ctrl_ccm_control_tl|GRC_CTRL_CCM_CONTROL_TL]] — 12 atributos (4 BICC)
- [[grc_job|GRC_JOB]] — 20 atributos (4 BICC)
- [[grc_otbi_ctrl_ccm_b|GRC_OTBI_CTRL_CCM_B]] — 52 atributos (2 PKs, 41 BICC)
- [[gtg_aac_ctrl_anl_sum|GTG_AAC_CTRL_ANL_SUM]] — 9 atributos
- [[gtg_ctrl_anl_job_inc_sum|GTG_CTRL_ANL_JOB_INC_SUM]] — 14 atributos
- [[gtg_sc_ac_access_v|GTG_SC_AC_ACCESS_V]] — 4 atributos (1 BICC)
- [[gtg_sc_ac_defaults|GTG_SC_AC_DEFAULTS]] — 14 atributos
- [[gtg_sc_ac_security_v|GTG_SC_AC_SECURITY_V]] — 9 atributos (5 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 14 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 18 atributos (2 BICC)
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
| 10 | CommentsPEOObjectStateCode | OBJECT_STATE_CODE | — | — |
| 11 | CommentsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 12 | CommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CommentsPEOUserComment | USER_COMMENT | — | ✅ |

### [[grc_ctrl_ccm_control_tl|GRC_CTRL_CCM_CONTROL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContinuousControlTransPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ContinuousControlTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | ContinuousControlTransPEODescription | DESCRIPTION | — | ✅ |
| 4 | ContinuousControlTransPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | ContinuousControlTransPEOId | ID | — | — |
| 6 | ContinuousControlTransPEOLanguage | LANGUAGE | — | — |
| 7 | ContinuousControlTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContinuousControlTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContinuousControlTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContinuousControlTransPEOName | NAME | — | ✅ |
| 11 | ContinuousControlTransPEORevisionNumber | REVISION_NUMBER | — | — |
| 12 | ContinuousControlTransPEOSourceLang | SOURCE_LANG | — | — |

### [[grc_job|GRC_JOB]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | JobPEOCreationDate | CREATION_DATE | — | — |
| 3 | JobPEODisplayName | DISPLAY_NAME | — | — |
| 4 | JobPEOEndDate | END_DATE | — | — |
| 5 | JobPEOId | ID | — | — |
| 6 | JobPEOIsCancelable | IS_CANCELABLE | — | — |
| 7 | JobPEOJobType | JOB_TYPE | — | — |
| 8 | JobPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | JobPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | JobPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | JobPEOLocaleKey | LOCALE_KEY | — | — |
| 12 | JobPEOName | NAME | — | — |
| 13 | JobPEOParameters | PARAMETERS | — | — |
| 14 | JobPEOResult | RESULT | — | — |
| 15 | JobPEOScheduled | SCHEDULED | — | — |
| 16 | JobPEOScheduledBy | SCHEDULED_BY | — | — |
| 17 | JobPEOScheduledByName | SCHEDULED_BY_NAME | — | ✅ |
| 18 | JobPEOStartDate | START_DATE | — | — |
| 19 | JobPEOStatusId | STATUS_ID | — | ✅ |
| 20 | JobPEOStatusMessage | STATUS_MESSAGE | — | — |

### [[grc_otbi_ctrl_ccm_b|GRC_OTBI_CTRL_CCM_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContinuousControlBasePEOControlLogic | CONTROL_LOGIC | — | ✅ |
| 2 | ContinuousControlBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ContinuousControlBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ContinuousControlBasePEOEffectiveDate | EFFECTIVE_DATE | — | — |
| 5 | ContinuousControlBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 6 | ContinuousControlBasePEOEnforcementType | ENFORCEMENT_TYPE | — | ✅ |
| 7 | ContinuousControlBasePEOEntitlementIds | ENTITLEMENT_IDS | — | — |
| 8 | ContinuousControlBasePEOId | ID | 🔑 | ✅ |
| 9 | ContinuousControlBasePEOIncAttr1 | INC_ATTR_1 | — | ✅ |
| 10 | ContinuousControlBasePEOIncAttr10 | INC_ATTR_10 | — | ✅ |
| 11 | ContinuousControlBasePEOIncAttr11 | INC_ATTR_11 | — | ✅ |
| 12 | ContinuousControlBasePEOIncAttr12 | INC_ATTR_12 | — | ✅ |
| 13 | ContinuousControlBasePEOIncAttr13 | INC_ATTR_13 | — | ✅ |
| 14 | ContinuousControlBasePEOIncAttr14 | INC_ATTR_14 | — | ✅ |
| 15 | ContinuousControlBasePEOIncAttr15 | INC_ATTR_15 | — | ✅ |
| 16 | ContinuousControlBasePEOIncAttr16 | INC_ATTR_16 | — | ✅ |
| 17 | ContinuousControlBasePEOIncAttr17 | INC_ATTR_17 | — | ✅ |
| 18 | ContinuousControlBasePEOIncAttr18 | INC_ATTR_18 | — | ✅ |
| 19 | ContinuousControlBasePEOIncAttr19 | INC_ATTR_19 | — | ✅ |
| 20 | ContinuousControlBasePEOIncAttr2 | INC_ATTR_2 | — | ✅ |
| 21 | ContinuousControlBasePEOIncAttr20 | INC_ATTR_20 | — | ✅ |
| 22 | ContinuousControlBasePEOIncAttr21 | INC_ATTR_21 | — | ✅ |
| 23 | ContinuousControlBasePEOIncAttr22 | INC_ATTR_22 | — | ✅ |
| 24 | ContinuousControlBasePEOIncAttr23 | INC_ATTR_23 | — | ✅ |
| 25 | ContinuousControlBasePEOIncAttr24 | INC_ATTR_24 | — | ✅ |
| 26 | ContinuousControlBasePEOIncAttr25 | INC_ATTR_25 | — | ✅ |
| 27 | ContinuousControlBasePEOIncAttr3 | INC_ATTR_3 | — | ✅ |
| 28 | ContinuousControlBasePEOIncAttr4 | INC_ATTR_4 | — | ✅ |
| 29 | ContinuousControlBasePEOIncAttr5 | INC_ATTR_5 | — | ✅ |
| 30 | ContinuousControlBasePEOIncAttr6 | INC_ATTR_6 | — | ✅ |
| 31 | ContinuousControlBasePEOIncAttr7 | INC_ATTR_7 | — | ✅ |
| 32 | ContinuousControlBasePEOIncAttr8 | INC_ATTR_8 | — | ✅ |
| 33 | ContinuousControlBasePEOIncAttr9 | INC_ATTR_9 | — | ✅ |
| 34 | ContinuousControlBasePEOIncAttrHeader | INC_ATTR_HEADER | — | — |
| 35 | ContinuousControlBasePEOInvestigatorIds | INVESTIGATOR_IDS | — | ✅ |
| 36 | ContinuousControlBasePEOLastRunDate | LAST_RUN_DATE | — | ✅ |
| 37 | ContinuousControlBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | ContinuousControlBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | ContinuousControlBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | ContinuousControlBasePEOLatestJobId | LATEST_JOB_ID | — | — |
| 41 | ContinuousControlBasePEOPriority | PRIORITY | — | ✅ |
| 42 | ContinuousControlBasePEOQuery | QUERY | — | — |
| 43 | ContinuousControlBasePEOQueryName | QUERY_NAME | — | — |
| 44 | ContinuousControlBasePEOResultType | RESULT_TYPE | — | ✅ |
| 45 | ContinuousControlBasePEORevisionDate | REVISION_DATE | — | — |
| 46 | ContinuousControlBasePEORevisionNumber | REVISION_NUMBER | 🔑 | ✅ |
| 47 | ContinuousControlBasePEORunDepJobs | RUN_DEPENDENT_JOBS | — | — |
| 48 | ContinuousControlBasePEOState | STATE | — | — |
| 49 | ContinuousControlBasePEOStateCode | STATE_CODE | — | ✅ |
| 50 | ContinuousControlBasePEOStatus | STATUS | — | ✅ |
| 51 | ContinuousControlBasePEOType | TYPE | — | ✅ |
| 52 | ContinuousControlBasePEOUpdatedByName | UPDATED_BY_NAME | — | — |

### [[gtg_aac_ctrl_anl_sum|GTG_AAC_CTRL_ANL_SUM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GRCAACControlAnlSumPEOAnalyzedRoleCount | ANALYZED_ROLE_COUNT | — | — |
| 2 | GRCAACControlAnlSumPEOAnalyzedUserCount | ANALYZED_USER_COUNT | — | — |
| 3 | GRCAACControlAnlSumPEOControlId | CONTROL_ID | — | — |
| 4 | GRCAACControlAnlSumPEOCreatedBy | CREATED_BY | — | — |
| 5 | GRCAACControlAnlSumPEOCreationDate | CREATION_DATE | — | — |
| 6 | GRCAACControlAnlSumPEOJobId | JOB_ID | — | — |
| 7 | GRCAACControlAnlSumPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | GRCAACControlAnlSumPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | GRCAACControlAnlSumPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |

### [[gtg_ctrl_anl_job_inc_sum|GTG_CTRL_ANL_JOB_INC_SUM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlJobIncidentsPEOAnalysisEndTime | ANALYSIS_END_TIME | — | — |
| 2 | ControlJobIncidentsPEOAnalysisStartTime | ANALYSIS_START_TIME | — | — |
| 3 | ControlJobIncidentsPEOClosedIncidentCount | CLOSED_INCIDENT_COUNT | — | — |
| 4 | ControlJobIncidentsPEOControlId | CONTROL_ID | — | — |
| 5 | ControlJobIncidentsPEOCreatedBy | CREATED_BY | — | — |
| 6 | ControlJobIncidentsPEOCreationDate | CREATION_DATE | — | — |
| 7 | ControlJobIncidentsPEOExistingIncidentCount | EXISTING_INCIDENT_COUNT | — | — |
| 8 | ControlJobIncidentsPEOJobId | JOB_ID | — | — |
| 9 | ControlJobIncidentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | ControlJobIncidentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ControlJobIncidentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ControlJobIncidentsPEONewIncidentCount | NEW_INCIDENT_COUNT | — | — |
| 13 | ControlJobIncidentsPEOTotalIncidentCount | TOTAL_INCIDENT_COUNT | — | — |
| 14 | ControlJobIncidentsPEOUpdatedIncidentCount | UPDATED_INCIDENT_COUNT | — | — |

### [[gtg_sc_ac_access_v|GTG_SC_AC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACSecurityPEOSecId | SECURABLE_ID | — | — |
| 2 | ACSecurityPEOSecType | SECURABLE_TYPE | — | — |
| 3 | ACSecurityPEOStateType | STATE_TYPE | — | — |
| 4 | ACSecurityPEOUserId | USER_ID | — | ✅ |

### [[gtg_sc_ac_defaults|GTG_SC_AC_DEFAULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcScDefaultSecurityPEOAccessorId | ACCESSOR_ID | — | — |
| 2 | AcScDefaultSecurityPEOAccessorType | ACCESSOR_TYPE | — | — |
| 3 | AcScDefaultSecurityPEOCreatedBy | CREATED_BY | — | — |
| 4 | AcScDefaultSecurityPEOCreationDate | CREATION_DATE | — | — |
| 5 | AcScDefaultSecurityPEOId | ID | — | — |
| 6 | AcScDefaultSecurityPEOIsEditor | IS_EDITOR | — | — |
| 7 | AcScDefaultSecurityPEOIsOwner | IS_OWNER | — | — |
| 8 | AcScDefaultSecurityPEOIsViewer | IS_VIEWER | — | — |
| 9 | AcScDefaultSecurityPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | AcScDefaultSecurityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AcScDefaultSecurityPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | AcScDefaultSecurityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | AcScDefaultSecurityPEOSourceSecurableId | SOURCE_SECURABLE_ID | — | — |
| 14 | AcScDefaultSecurityPEOSourceSecurableType | SOURCE_SECURABLE_TYPE | — | — |

### [[gtg_sc_ac_security_v|GTG_SC_AC_SECURITY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcScSecurityPEOAccessorId | ACCESSOR_ID | — | ✅ |
| 2 | AcScSecurityPEOAccessorType | ACCESSOR_TYPE | — | — |
| 3 | AcScSecurityPEOId | ID | — | — |
| 4 | AcScSecurityPEOIsEditor | IS_EDITOR | — | ✅ |
| 5 | AcScSecurityPEOIsOwner | IS_OWNER | — | ✅ |
| 6 | AcScSecurityPEOIsViewer | IS_VIEWER | — | ✅ |
| 7 | AcScSecurityPEORoleBitmap | ROLE_BITMAP | — | ✅ |
| 8 | AcScSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 9 | AcScSecurityPEOSecurableType | SECURABLE_TYPE | — | — |

### [[gtg_sc_group_vl|GTG_SC_GROUP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SecurityGroup2PEOCreatedBy | CREATED_BY | — | — |
| 2 | SecurityGroup2PEOCreationDate | CREATION_DATE | — | — |
| 3 | SecurityGroup2PEOGroupId | GROUP_ID | — | — |
| 4 | SecurityGroup2PEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | SecurityGroup2PEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SecurityGroup2PEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SecurityGroup2PEOName | NAME | — | — |
| 8 | SecurityGroup2PEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SecurityGroup2PEORoleType | ROLE_TYPE | — | — |
| 10 | SecurityGroup2PEOSecurableType | SECURABLE_TYPE | — | — |
| 11 | SecurityGroupPEOGroupId | GROUP_ID | — | ✅ |
| 12 | SecurityGroupPEOName | NAME | — | ✅ |
| 13 | SecurityGroupPEORoleType | ROLE_TYPE | — | ✅ |
| 14 | SecurityGroupPEOSecurableType | SECURABLE_TYPE | — | ✅ |

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
| 1 | ScSecurityUserGroup2PEOCreatedBy | CREATED_BY | — | — |
| 2 | ScSecurityUserGroup2PEOCreationDate | CREATION_DATE | — | — |
| 3 | ScSecurityUserGroup2PEOGroupId | GROUP_ID | — | — |
| 4 | ScSecurityUserGroup2PEOId | ID | — | — |
| 5 | ScSecurityUserGroup2PEOIsOrphan | IS_ORPHAN | — | — |
| 6 | ScSecurityUserGroup2PEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ScSecurityUserGroup2PEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ScSecurityUserGroup2PEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ScSecurityUserGroup2PEOUserId | USER_ID | — | — |
| 10 | ScSecurityUserGroupPEOCreatedBy | CREATED_BY | — | — |
| 11 | ScSecurityUserGroupPEOCrtnDt | CREATION_DATE | — | — |
| 12 | ScSecurityUserGroupPEOGroupId | GROUP_ID | — | — |
| 13 | ScSecurityUserGroupPEOId | ID | — | — |
| 14 | ScSecurityUserGroupPEOIsOrphan | IS_ORPHAN | — | ✅ |
| 15 | ScSecurityUserGroupPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 16 | ScSecurityUserGroupPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 17 | ScSecurityUserGroupPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |
| 18 | ScSecurityUserGroupPEOUserId | USER_ID | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmntPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CmntPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CmntPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CmntPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | CmntPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | CtrlPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | CtrlPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CtrlPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | CtrlPersonCreatedByPersonId | PERSON_ID | — | — |
| 10 | CtrlPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | CtrlPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | CtrlPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | CtrlPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | CtrlPersonUpdatedByPersonId | PERSON_ID | — | — |
| 15 | CtrlPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | InvestPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | InvestPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | InvestPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | InvestPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | InvestPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 21 | JobPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 22 | JobPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | JobPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 24 | JobPersonCreatedByPersonId | PERSON_ID | — | — |
| 25 | JobPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmntCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CmntCreatedByPersonId | PERSON_ID | — | — |
| 3 | CmntCreatedByUserGuid | USER_GUID | — | — |
| 4 | CmntCreatedByUserId | USER_ID | — | — |
| 5 | CmntCreatedByUsername | USERNAME | — | — |
| 6 | CtrlCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | CtrlCreatedByPersonId | PERSON_ID | — | — |
| 8 | CtrlCreatedByUserGuid | USER_GUID | — | — |
| 9 | CtrlCreatedByUserId | USER_ID | — | — |
| 10 | CtrlCreatedByUsername | USERNAME | — | — |
| 11 | CtrlUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CtrlUpdatedByPersonId | PERSON_ID | — | — |
| 13 | CtrlUpdatedByUserGuid | USER_GUID | — | — |
| 14 | CtrlUpdatedByUserId | USER_ID | — | — |
| 15 | CtrlUpdatedByUsername | USERNAME | — | — |
| 16 | InvestUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | InvestUpdatedByPersonId | PERSON_ID | — | — |
| 18 | InvestUpdatedByUserGuid | USER_GUID | — | — |
| 19 | InvestUpdatedByUserId | USER_ID | — | — |
| 20 | InvestUpdatedByUsername | USERNAME | — | — |
| 21 | JobCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | JobCreatedByPersonId | PERSON_ID | — | — |
| 23 | JobCreatedByUserGuid | USER_GUID | — | — |
| 24 | JobCreatedByUserId | USER_ID | — | — |
| 25 | JobCreatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
