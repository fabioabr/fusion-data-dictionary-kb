---
id: DOC-OTHER-PVO-IncidentAccessResultDetailsPVO
doc_type: system-doc
title: "IncidentAccessResultDetailsPVO — PVO Cross-Module"
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
  - IncidentAccessResultDetailsPVO
  - incidentaccessresultdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IncidentAccessResultDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Incident Access Result Details. Acessa as tabelas: GRC_CTRL_AAC_INCIDENTS, GRC_OTBI_INTRA_ROLE, GTG_SC_AC_RESULT_ACCESS_V (+6).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.IncidentAccessResultDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 147 | 9 | 3 | 77 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[grc_ctrl_aac_incidents|GRC_CTRL_AAC_INCIDENTS]] — 77 atributos (3 PKs, 54 BICC)
- [[grc_otbi_intra_role|GRC_OTBI_INTRA_ROLE]] — 8 atributos (8 BICC)
- [[gtg_sc_ac_result_access_v|GTG_SC_AC_RESULT_ACCESS_V]] — 4 atributos
- [[gtg_sc_ac_result_security_v|GTG_SC_AC_RESULT_SECURITY_V]] — 10 atributos (5 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 15 atributos (3 BICC)
- [[per_users|PER_USERS]] — 15 atributos

---

## ⚙️ Atributos

### [[grc_ctrl_aac_incidents|GRC_CTRL_AAC_INCIDENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncidentAccRsltDtlsPEOAccPathGrpg | ACCESS_PATH_GROUPING | — | ✅ |
| 2 | IncidentAccRsltDtlsPEOAccPathGrpgVal | ACCESS_PATH_GROUPING_VAL | — | ✅ |
| 3 | IncidentAccRsltDtlsPEOAccessPathId | ACCESS_PATH_ID | — | — |
| 4 | IncidentAccRsltDtlsPEOAccessPathIds | ACCESS_PATH_IDS | — | — |
| 5 | IncidentAccRsltDtlsPEOAccessPathInfo | ACCESS_PATH_INFO | — | ✅ |
| 6 | IncidentAccRsltDtlsPEOAccessPointName | ACCESS_POINT_NAME | — | — |
| 7 | IncidentAccRsltDtlsPEOAlInUsrId | ALL_INV_USER_IDS | — | — |
| 8 | IncidentAccRsltDtlsPEOAllAprvrs | ALL_APPROVERS | — | — |
| 9 | IncidentAccRsltDtlsPEOAllInstgrs | ALL_INVESTIGATORS | — | — |
| 10 | IncidentAccRsltDtlsPEOAllRvwrs | ALL_REVIEWERS | — | — |
| 11 | IncidentAccRsltDtlsPEOApprovers | APPROVERS | — | — |
| 12 | IncidentAccRsltDtlsPEOAtchmnt | ATTACHMENT | — | — |
| 13 | IncidentAccRsltDtlsPEOClosedBy | CLOSED_BY | — | — |
| 14 | IncidentAccRsltDtlsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 15 | IncidentAccRsltDtlsPEOCnfltgAccPntId | CONFLICTING_ACC_POINT_ID | — | — |
| 16 | IncidentAccRsltDtlsPEOCnfltgAccPntNam | CONFLICTING_ACC_POINT_NAME | — | ✅ |
| 17 | IncidentAccRsltDtlsPEOCnfltgAccPntTyp | CONFLICTING_ACC_POINT_TYPE | — | ✅ |
| 18 | IncidentAccRsltDtlsPEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | IncidentAccRsltDtlsPEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | IncidentAccRsltDtlsPEOCtrlVersion | CTRL_VERSION | 🔑 | ✅ |
| 21 | IncidentAccRsltDtlsPEODatasourceIds | DATASOURCE_IDS | — | — |
| 22 | IncidentAccRsltDtlsPEODatasourceNames | DATASOURCE_NAMES | — | — |
| 23 | IncidentAccRsltDtlsPEOEffectiveSeq | EFFECTIVE_SEQUENCE | — | — |
| 24 | IncidentAccRsltDtlsPEOEntitlement | ENTITLEMENT | — | ✅ |
| 25 | IncidentAccRsltDtlsPEOErpUserId | ERP_USER_ID | — | ✅ |
| 26 | IncidentAccRsltDtlsPEOErpUserName | ERP_USER_NAME | — | ✅ |
| 27 | IncidentAccRsltDtlsPEOFirstName | FIRST_NAME | — | ✅ |
| 28 | IncidentAccRsltDtlsPEOGrccControlId | GRCC_CONTROL_ID | — | — |
| 29 | IncidentAccRsltDtlsPEOId | ID | 🔑 | ✅ |
| 30 | IncidentAccRsltDtlsPEOIncAttr1 | INC_ATTR_1 | — | ✅ |
| 31 | IncidentAccRsltDtlsPEOIncAttr10 | INC_ATTR_10 | — | ✅ |
| 32 | IncidentAccRsltDtlsPEOIncAttr11 | INC_ATTR_11 | — | ✅ |
| 33 | IncidentAccRsltDtlsPEOIncAttr12 | INC_ATTR_12 | — | ✅ |
| 34 | IncidentAccRsltDtlsPEOIncAttr13 | INC_ATTR_13 | — | ✅ |
| 35 | IncidentAccRsltDtlsPEOIncAttr14 | INC_ATTR_14 | — | ✅ |
| 36 | IncidentAccRsltDtlsPEOIncAttr15 | INC_ATTR_15 | — | ✅ |
| 37 | IncidentAccRsltDtlsPEOIncAttr16 | INC_ATTR_16 | — | ✅ |
| 38 | IncidentAccRsltDtlsPEOIncAttr17 | INC_ATTR_17 | — | ✅ |
| 39 | IncidentAccRsltDtlsPEOIncAttr18 | INC_ATTR_18 | — | ✅ |
| 40 | IncidentAccRsltDtlsPEOIncAttr19 | INC_ATTR_19 | — | ✅ |
| 41 | IncidentAccRsltDtlsPEOIncAttr2 | INC_ATTR_2 | — | ✅ |
| 42 | IncidentAccRsltDtlsPEOIncAttr20 | INC_ATTR_20 | — | ✅ |
| 43 | IncidentAccRsltDtlsPEOIncAttr21 | INC_ATTR_21 | — | ✅ |
| 44 | IncidentAccRsltDtlsPEOIncAttr22 | INC_ATTR_22 | — | ✅ |
| 45 | IncidentAccRsltDtlsPEOIncAttr23 | INC_ATTR_23 | — | ✅ |
| 46 | IncidentAccRsltDtlsPEOIncAttr24 | INC_ATTR_24 | — | ✅ |
| 47 | IncidentAccRsltDtlsPEOIncAttr25 | INC_ATTR_25 | — | ✅ |
| 48 | IncidentAccRsltDtlsPEOIncAttr3 | INC_ATTR_3 | — | ✅ |
| 49 | IncidentAccRsltDtlsPEOIncAttr4 | INC_ATTR_4 | — | ✅ |
| 50 | IncidentAccRsltDtlsPEOIncAttr5 | INC_ATTR_5 | — | ✅ |
| 51 | IncidentAccRsltDtlsPEOIncAttr6 | INC_ATTR_6 | — | ✅ |
| 52 | IncidentAccRsltDtlsPEOIncAttr7 | INC_ATTR_7 | — | ✅ |
| 53 | IncidentAccRsltDtlsPEOIncAttr8 | INC_ATTR_8 | — | ✅ |
| 54 | IncidentAccRsltDtlsPEOIncAttr9 | INC_ATTR_9 | — | ✅ |
| 55 | IncidentAccRsltDtlsPEOIncAttrValues | INC_ATTR_VALUES | — | — |
| 56 | IncidentAccRsltDtlsPEOIncInfCd | INCIDENT_INFO_CODE | — | ✅ |
| 57 | IncidentAccRsltDtlsPEOIncidentVersion | INCIDENT_VERSION | 🔑 | ✅ |
| 58 | IncidentAccRsltDtlsPEOInvUserIds | INV_USER_IDS | — | ✅ |
| 59 | IncidentAccRsltDtlsPEOInvestigators | INVESTIGATORS | — | ✅ |
| 60 | IncidentAccRsltDtlsPEOIsAttr2Num | IS_ATTR2_NUM | — | ✅ |
| 61 | IncidentAccRsltDtlsPEOLastName | LAST_NAME | — | ✅ |
| 62 | IncidentAccRsltDtlsPEOLastRunDate | LAST_RUN_DATE | — | — |
| 63 | IncidentAccRsltDtlsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | IncidentAccRsltDtlsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | IncidentAccRsltDtlsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 66 | IncidentAccRsltDtlsPEOLocaleKey | LOCALE_KEY | — | — |
| 67 | IncidentAccRsltDtlsPEOOrigKeypath | ORIG_KEYPATH | — | — |
| 68 | IncidentAccRsltDtlsPEOPathExpression | PATH_EXPRESSION | — | — |
| 69 | IncidentAccRsltDtlsPEOPriority | PRIORITY | — | ✅ |
| 70 | IncidentAccRsltDtlsPEOReviewers | REVIEWERS | — | — |
| 71 | IncidentAccRsltDtlsPEORevisionDate | REVISION_DATE | — | — |
| 72 | IncidentAccRsltDtlsPEORole | ROLE | — | ✅ |
| 73 | IncidentAccRsltDtlsPEORoleGrouping | ROLE_GROUPING | — | ✅ |
| 74 | IncidentAccRsltDtlsPEORoleId | ROLE_ID | — | ✅ |
| 75 | IncidentAccRsltDtlsPEOStateCode | STATE_CODE | — | ✅ |
| 76 | IncidentAccRsltDtlsPEOStatus | STATUS | — | ✅ |
| 77 | IncidentAccRsltDtlsPEOType | TYPE | — | ✅ |

### [[grc_otbi_intra_role|GRC_OTBI_INTRA_ROLE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessViolationsPEOAccPathGrpg | ACCESS_PATH_GROUPING | — | ✅ |
| 2 | AccessViolationsPEOAccPntName | ACCESS_POINT_NAME | — | ✅ |
| 3 | AccessViolationsPEOEntlmnt | ENTITLEMENT | — | ✅ |
| 4 | AccessViolationsPEOIncId | INCIDENT_ID | — | ✅ |
| 5 | AccessViolationsPEOIncInfoCd | INCIDENT_INFO_CODE | — | ✅ |
| 6 | AccessViolationsPEORoleId | ROLE_ID | — | ✅ |
| 7 | AccessViolationsPEORoleName | ROLE_NAME | — | ✅ |
| 8 | AccessViolationsPEOStatus | STATUS | — | ✅ |

### [[gtg_sc_ac_result_access_v|GTG_SC_AC_RESULT_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACSecurityPEOSecId | SECURABLE_ID | — | — |
| 2 | ACSecurityPEOSecType | SECURABLE_TYPE | — | — |
| 3 | ACSecurityPEOStateType | STATE_TYPE | — | — |
| 4 | ACSecurityPEOUserId | USER_ID | — | — |

### [[gtg_sc_ac_result_security_v|GTG_SC_AC_RESULT_SECURITY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACIncidentSecurityPEOAccessorType | ACCESSOR_TYPE | — | — |
| 2 | ACIncidentSecurityPEOAcsrId | ACCESSOR_ID | — | ✅ |
| 3 | ACIncidentSecurityPEOIsEditor | IS_EDITOR | — | ✅ |
| 4 | ACIncidentSecurityPEOIsOwner | IS_OWNER | — | ✅ |
| 5 | ACIncidentSecurityPEOIsViewer | IS_VIEWER | — | ✅ |
| 6 | ACIncidentSecurityPEORoleBitmap | ROLE_BITMAP | — | ✅ |
| 7 | ACIncidentSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 8 | ACIncidentSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 9 | ACIncidentSecurityPEOSourceSecurableId | SOURCE_SECURABLE_ID | — | — |
| 10 | ACIncidentSecurityPEOSourceSecurableType | SOURCE_SECURABLE_TYPE | — | — |

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
| 1 | IncPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | IncPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | IncPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | IncPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | IncPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | IncPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | IncPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | IncPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | IncPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | IncPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | InvestPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 12 | InvestPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | InvestPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | InvestPersonUpdatedByPersonId | PERSON_ID | — | — |
| 15 | InvestPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | IncCreatedByPersonId | PERSON_ID | — | — |
| 3 | IncCreatedByUserGuid | USER_GUID | — | — |
| 4 | IncCreatedByUserId | USER_ID | — | — |
| 5 | IncCreatedByUsername | USERNAME | — | — |
| 6 | IncUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | IncUpdatedByPersonId | PERSON_ID | — | — |
| 8 | IncUpdatedByUserGuid | USER_GUID | — | — |
| 9 | IncUpdatedByUserId | USER_ID | — | — |
| 10 | IncUpdatedByUsername | USERNAME | — | — |
| 11 | InvestUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | InvestUpdatedByPersonId | PERSON_ID | — | — |
| 13 | InvestUpdatedByUserGuid | USER_GUID | — | — |
| 14 | InvestUpdatedByUserId | USER_ID | — | — |
| 15 | InvestUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
