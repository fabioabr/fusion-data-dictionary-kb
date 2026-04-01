---
id: DOC-OTHER-PVO-IncidentTransactionResultDetailsPVO
doc_type: system-doc
title: "IncidentTransactionResultDetailsPVO — PVO Cross-Module"
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
  - IncidentTransactionResultDetailsPVO
  - incidenttransactionresultdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IncidentTransactionResultDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Incident Transaction Result Details. Acessa as tabelas: GRC_CTRL_INCIDENTS, GTG_OTBI_CTRL_DYN_COLS, GTG_SC_AC_RESULT_ACCESS_V (+6).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.IncidentTransactionResultDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 166 | 9 | 3 | 63 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[grc_ctrl_incidents|GRC_CTRL_INCIDENTS]] — 70 atributos (3 PKs, 48 BICC)
- [[gtg_otbi_ctrl_dyn_cols|GTG_OTBI_CTRL_DYN_COLS]] — 34 atributos
- [[gtg_sc_ac_result_access_v|GTG_SC_AC_RESULT_ACCESS_V]] — 4 atributos
- [[gtg_sc_ac_result_security_v|GTG_SC_AC_RESULT_SECURITY_V]] — 10 atributos (5 BICC)
- [[gtg_sc_group_vl|GTG_SC_GROUP_VL]] — 5 atributos (4 BICC)
- [[gtg_sc_securable_to_priv|GTG_SC_SECURABLE_TO_PRIV]] — 4 atributos (1 BICC)
- [[gtg_sc_user_group|GTG_SC_USER_GROUP]] — 9 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 15 atributos (3 BICC)
- [[per_users|PER_USERS]] — 15 atributos

---

## ⚙️ Atributos

### [[grc_ctrl_incidents|GRC_CTRL_INCIDENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncidentResultDetailsPEOAccessPathGrouping | ACCESS_PATH_GROUPING | — | ✅ |
| 2 | IncidentResultDetailsPEOAccessPathGroupingVal | ACCESS_PATH_GROUPING_VAL | — | ✅ |
| 3 | IncidentResultDetailsPEOAccessPathId | ACCESS_PATH_ID | — | — |
| 4 | IncidentResultDetailsPEOAccessPathIds | ACCESS_PATH_IDS | — | — |
| 5 | IncidentResultDetailsPEOAccessPathInfo | ACCESS_PATH_INFO | — | ✅ |
| 6 | IncidentResultDetailsPEOAccessPointName | ACCESS_POINT_NAME | — | — |
| 7 | IncidentResultDetailsPEOApprovers | APPROVERS | — | — |
| 8 | IncidentResultDetailsPEOClosedBy | CLOSED_BY | — | — |
| 9 | IncidentResultDetailsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 10 | IncidentResultDetailsPEOConflictingAccPointId | CONFLICTING_ACC_POINT_ID | — | — |
| 11 | IncidentResultDetailsPEOConflictingAccPointName | CONFLICTING_ACC_POINT_NAME | — | ✅ |
| 12 | IncidentResultDetailsPEOConflictingAccPointType | CONFLICTING_ACC_POINT_TYPE | — | — |
| 13 | IncidentResultDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | IncidentResultDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | IncidentResultDetailsPEOCtrlVersion | CTRL_VERSION | 🔑 | ✅ |
| 16 | IncidentResultDetailsPEODatasourceIds | DATASOURCE_IDS | — | — |
| 17 | IncidentResultDetailsPEODatasourceNames | DATASOURCE_NAMES | — | — |
| 18 | IncidentResultDetailsPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 19 | IncidentResultDetailsPEOEntitlement | ENTITLEMENT | — | ✅ |
| 20 | IncidentResultDetailsPEOErpUserId | ERP_USER_ID | — | — |
| 21 | IncidentResultDetailsPEOErpUserName | ERP_USER_NAME | — | ✅ |
| 22 | IncidentResultDetailsPEOFirstName | FIRST_NAME | — | ✅ |
| 23 | IncidentResultDetailsPEOGrccControlId | GRCC_CONTROL_ID | — | — |
| 24 | IncidentResultDetailsPEOId | ID | 🔑 | ✅ |
| 25 | IncidentResultDetailsPEOIncAttr1 | INC_ATTR_1 | — | ✅ |
| 26 | IncidentResultDetailsPEOIncAttr10 | INC_ATTR_10 | — | ✅ |
| 27 | IncidentResultDetailsPEOIncAttr11 | INC_ATTR_11 | — | ✅ |
| 28 | IncidentResultDetailsPEOIncAttr12 | INC_ATTR_12 | — | ✅ |
| 29 | IncidentResultDetailsPEOIncAttr13 | INC_ATTR_13 | — | ✅ |
| 30 | IncidentResultDetailsPEOIncAttr14 | INC_ATTR_14 | — | ✅ |
| 31 | IncidentResultDetailsPEOIncAttr15 | INC_ATTR_15 | — | ✅ |
| 32 | IncidentResultDetailsPEOIncAttr16 | INC_ATTR_16 | — | ✅ |
| 33 | IncidentResultDetailsPEOIncAttr17 | INC_ATTR_17 | — | ✅ |
| 34 | IncidentResultDetailsPEOIncAttr18 | INC_ATTR_18 | — | ✅ |
| 35 | IncidentResultDetailsPEOIncAttr19 | INC_ATTR_19 | — | ✅ |
| 36 | IncidentResultDetailsPEOIncAttr2 | INC_ATTR_2 | — | ✅ |
| 37 | IncidentResultDetailsPEOIncAttr20 | INC_ATTR_20 | — | ✅ |
| 38 | IncidentResultDetailsPEOIncAttr21 | INC_ATTR_21 | — | ✅ |
| 39 | IncidentResultDetailsPEOIncAttr22 | INC_ATTR_22 | — | ✅ |
| 40 | IncidentResultDetailsPEOIncAttr23 | INC_ATTR_23 | — | ✅ |
| 41 | IncidentResultDetailsPEOIncAttr24 | INC_ATTR_24 | — | ✅ |
| 42 | IncidentResultDetailsPEOIncAttr25 | INC_ATTR_25 | — | ✅ |
| 43 | IncidentResultDetailsPEOIncAttr3 | INC_ATTR_3 | — | ✅ |
| 44 | IncidentResultDetailsPEOIncAttr4 | INC_ATTR_4 | — | ✅ |
| 45 | IncidentResultDetailsPEOIncAttr5 | INC_ATTR_5 | — | ✅ |
| 46 | IncidentResultDetailsPEOIncAttr6 | INC_ATTR_6 | — | ✅ |
| 47 | IncidentResultDetailsPEOIncAttr7 | INC_ATTR_7 | — | ✅ |
| 48 | IncidentResultDetailsPEOIncAttr8 | INC_ATTR_8 | — | ✅ |
| 49 | IncidentResultDetailsPEOIncAttr9 | INC_ATTR_9 | — | ✅ |
| 50 | IncidentResultDetailsPEOIncAttrValues | INC_ATTR_VALUES | — | — |
| 51 | IncidentResultDetailsPEOIncidentVersion | INCIDENT_VERSION | 🔑 | ✅ |
| 52 | IncidentResultDetailsPEOInvUserIds | INV_USER_IDS | — | — |
| 53 | IncidentResultDetailsPEOInvestigators | INVESTIGATORS | — | ✅ |
| 54 | IncidentResultDetailsPEOIsAttr2Num | IS_ATTR2_NUM | — | ✅ |
| 55 | IncidentResultDetailsPEOLastName | LAST_NAME | — | ✅ |
| 56 | IncidentResultDetailsPEOLastRunDate | LAST_RUN_DATE | — | — |
| 57 | IncidentResultDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | IncidentResultDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 59 | IncidentResultDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 60 | IncidentResultDetailsPEOLocaleKey | LOCALE_KEY | — | — |
| 61 | IncidentResultDetailsPEOOrigKeypath | ORIG_KEYPATH | — | — |
| 62 | IncidentResultDetailsPEOPathExpression | PATH_EXPRESSION | — | — |
| 63 | IncidentResultDetailsPEOPriority | PRIORITY | — | ✅ |
| 64 | IncidentResultDetailsPEOReviewers | REVIEWERS | — | — |
| 65 | IncidentResultDetailsPEORevisionDate | REVISION_DATE | — | — |
| 66 | IncidentResultDetailsPEORole | ROLE | — | ✅ |
| 67 | IncidentResultDetailsPEORoleGrouping | ROLE_GROUPING | — | — |
| 68 | IncidentResultDetailsPEOStateCode | STATE_CODE | — | ✅ |
| 69 | IncidentResultDetailsPEOStatus | STATUS | — | ✅ |
| 70 | IncidentResultDetailsPEOType | TYPE | — | ✅ |

### [[gtg_otbi_ctrl_dyn_cols|GTG_OTBI_CTRL_DYN_COLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACRsltDrillColPEOControlId | CONTROL_ID | — | — |
| 2 | ACRsltDrillColPEOCreatedBy | CREATED_BY | — | — |
| 3 | ACRsltDrillColPEOCreationDate | CREATION_DATE | — | — |
| 4 | ACRsltDrillColPEOId | ID | — | — |
| 5 | ACRsltDrillColPEOIncAttrKey1 | INC_ATTR_KEY_1 | — | — |
| 6 | ACRsltDrillColPEOIncAttrKey10 | INC_ATTR_KEY_10 | — | — |
| 7 | ACRsltDrillColPEOIncAttrKey11 | INC_ATTR_KEY_11 | — | — |
| 8 | ACRsltDrillColPEOIncAttrKey12 | INC_ATTR_KEY_12 | — | — |
| 9 | ACRsltDrillColPEOIncAttrKey13 | INC_ATTR_KEY_13 | — | — |
| 10 | ACRsltDrillColPEOIncAttrKey14 | INC_ATTR_KEY_14 | — | — |
| 11 | ACRsltDrillColPEOIncAttrKey15 | INC_ATTR_KEY_15 | — | — |
| 12 | ACRsltDrillColPEOIncAttrKey16 | INC_ATTR_KEY_16 | — | — |
| 13 | ACRsltDrillColPEOIncAttrKey17 | INC_ATTR_KEY_17 | — | — |
| 14 | ACRsltDrillColPEOIncAttrKey18 | INC_ATTR_KEY_18 | — | — |
| 15 | ACRsltDrillColPEOIncAttrKey19 | INC_ATTR_KEY_19 | — | — |
| 16 | ACRsltDrillColPEOIncAttrKey2 | INC_ATTR_KEY_2 | — | — |
| 17 | ACRsltDrillColPEOIncAttrKey20 | INC_ATTR_KEY_20 | — | — |
| 18 | ACRsltDrillColPEOIncAttrKey21 | INC_ATTR_KEY_21 | — | — |
| 19 | ACRsltDrillColPEOIncAttrKey22 | INC_ATTR_KEY_22 | — | — |
| 20 | ACRsltDrillColPEOIncAttrKey23 | INC_ATTR_KEY_23 | — | — |
| 21 | ACRsltDrillColPEOIncAttrKey24 | INC_ATTR_KEY_24 | — | — |
| 22 | ACRsltDrillColPEOIncAttrKey25 | INC_ATTR_KEY_25 | — | — |
| 23 | ACRsltDrillColPEOIncAttrKey4 | INC_ATTR_KEY_4 | — | — |
| 24 | ACRsltDrillColPEOIncAttrKey5 | INC_ATTR_KEY_5 | — | — |
| 25 | ACRsltDrillColPEOIncAttrKey6 | INC_ATTR_KEY_6 | — | — |
| 26 | ACRsltDrillColPEOIncAttrKey7 | INC_ATTR_KEY_7 | — | — |
| 27 | ACRsltDrillColPEOIncAttrKey8 | INC_ATTR_KEY_8 | — | — |
| 28 | ACRsltDrillColPEOIncAttrKey9 | INC_ATTR_KEY_9 | — | — |
| 29 | ACRsltDrillColPEOLastUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 30 | ACRsltDrillColPEOLastUpdtdBy | LAST_UPDATED_BY | — | — |
| 31 | ACRsltDrillColPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 32 | ACRsltDrillColPEORowNum | ROW_NUM | — | — |
| 33 | ACRsltDrillColPEORsltCols | RESULT_COLUMNS | — | — |
| 34 | ACRsltDrillColPEOncAttrKey3 | INC_ATTR_KEY_3 | — | — |

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
