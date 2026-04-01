---
id: DOC-OTHER-PVO-ACNCertificationPVO
doc_type: system-doc
title: "ACNCertificationPVO — PVO Cross-Module"
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
  - ACNCertificationPVO
  - acncertificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCertificationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNCertification. Acessa as tabelas: GRC_ACN_CERTIFICATION_VIEW, GRC_ACN_USER_ROLE_INFO_VL, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCertificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 4 | 1 | 46 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_certification_view|GRC_ACN_CERTIFICATION_VIEW]] — 49 atributos (1 PKs, 38 BICC)
- [[grc_acn_user_role_info_vl|GRC_ACN_USER_ROLE_INFO_VL]] — 7 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos (4 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[grc_acn_certification_view|GRC_ACN_CERTIFICATION_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertRolePEOAuditorSubmitBy | AUDITOR_SUBMIT_BY | — | ✅ |
| 2 | ACNCertRolePEOCertRoleId | CERT_ROLE_ID | — | — |
| 3 | ACNCertRolePEOIsIncludedFlag | IS_INCLUDED_FLAG | — | — |
| 4 | ACNCertRolePEOOwnerSubmitBy | OWNER_SUBMIT_BY | — | ✅ |
| 5 | ACNCertRolePEORoleId | ROLE_ID | — | ✅ |
| 6 | ACNCertRolePEORoleName | ROLE_NAME | — | ✅ |
| 7 | ACNCertRolePEORoleName1 | ROLE_NAME1 | — | — |
| 8 | ACNCertRoleSecurityBridgePEOObjectId | OBJECT_ID1 | — | — |
| 9 | ACNCertRoleSecurityBridgePEOUserId | USER_ID1 | — | — |
| 10 | ACNCertRoleUserPEOCertUserRoleId | CERT_USER_ROLE_ID | — | ✅ |
| 11 | ACNCertRoleUserPEOLastDesnBy | LAST_DECISION_BY | — | ✅ |
| 12 | ACNCertRoleUserPEOLastDesnDate | LAST_DECISION_DATE | — | ✅ |
| 13 | ACNCertRoleUserPEOLastUpdatedBy | LAST_UPDATED_BY2 | — | ✅ |
| 14 | ACNCertRoleUserPEOLastUpdtDt | LAST_UPDATE_DATE1 | — | ✅ |
| 15 | ACNCertRoleUserPEOPendingSubmit | PENDING_SUBMIT | — | ✅ |
| 16 | ACNCertRoleUserPEOStatus | STATUS1 | — | ✅ |
| 17 | ACNCertRoleUserPEOUserId | USER_ID | — | ✅ |
| 18 | ACNCertRoleUserPEOUserRoleInfoId | USER_ROLE_INFO_ID | — | — |
| 19 | ACNCertSecurityBridgePEOObjectId | OBJECT_ID | — | — |
| 20 | ACNCertSecurityBridgePEOUserId | USER_ID2 | — | — |
| 21 | ACNCertificationPEOCertificationDescription | CERTIFICATION_DESCRIPTION | — | ✅ |
| 22 | ACNCertificationPEOCertificationId | CERTIFICATION_ID | 🔑 | ✅ |
| 23 | ACNCertificationPEOCertificationName | CERTIFICATION_NAME | — | ✅ |
| 24 | ACNCertificationPEOCloseDate | CLOSE_DATE | — | ✅ |
| 25 | ACNCertificationPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | ACNCertificationPEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | ACNCertificationPEODueDate | DUE_DATE | — | ✅ |
| 28 | ACNCertificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | ACNCertificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ACNCertificationPEOStartDate | START_DATE | — | ✅ |
| 31 | ACNCertificationPEOStatus | STATUS | — | ✅ |
| 32 | ACNCertificationPEOType | TYPE | — | ✅ |
| 33 | ACNRoleInfoPEORoleInfoId | ROLE_INFO_ID | — | — |
| 34 | ACNUserInfoPEOAsgnmntCat | ASSIGNMENT_CATEGORY | — | ✅ |
| 35 | ACNUserInfoPEOAssStatType | ASSIGNMENT_STATUS_TYPE | — | ✅ |
| 36 | ACNUserInfoPEOBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 37 | ACNUserInfoPEOCostCenter | COST_CENTER | — | ✅ |
| 38 | ACNUserInfoPEODepartment | DEPARTMENT | — | ✅ |
| 39 | ACNUserInfoPEOJobCode | JOB_CODE | — | ✅ |
| 40 | ACNUserInfoPEOJobFamily | JOB_FAMILY | — | ✅ |
| 41 | ACNUserInfoPEOJobFunction | JOB_FUNCTION | — | ✅ |
| 42 | ACNUserInfoPEOJobName | JOB_NAME | — | ✅ |
| 43 | ACNUserInfoPEOLocation | LOCATION | — | ✅ |
| 44 | ACNUserInfoPEOLocationCode | LOCATION_CODE | — | ✅ |
| 45 | ACNUserInfoPEOManagerId | MANAGER_ID | — | — |
| 46 | ACNUserInfoPEOMngrDispName | MANAGER_DISPLAY_NAME | — | ✅ |
| 47 | ACNUserInfoPEOPositionName | POSITION_NAME | — | ✅ |
| 48 | ACNUserInfoPEOPstnCode | POSITION_CODE | — | ✅ |
| 49 | ACNUserInfoPEOUserInfoId | USER_INFO_ID | — | — |

### [[grc_acn_user_role_info_vl|GRC_ACN_USER_ROLE_INFO_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNUserRoleInfoVlPEOAssetBook | ASSET_BOOK | — | ✅ |
| 2 | ACNUserRoleInfoVlPEOBusUnit | BUSINESS_UNIT | — | ✅ |
| 3 | ACNUserRoleInfoVlPEODataAccSet | DATA_ACCESS_SET | — | ✅ |
| 4 | ACNUserRoleInfoVlPEOLanguage | LANGUAGE | — | — |
| 5 | ACNUserRoleInfoVlPEOLedger | LEDGER | — | ✅ |
| 6 | ACNUserRoleInfoVlPEORoleId | ROLE_ID | — | — |
| 7 | ACNUserRoleInfoVlPEOUsrRlInId | USER_ROLE_INFO_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | CertPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CertPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CertPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | CertPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | CertPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | CertPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CertPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | CertPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | CertPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | CertRolePersonDecisionByDisName | DISPLAY_NAME | — | ✅ |
| 12 | CertRolePersonDecisionByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | CertRolePersonDecisionByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | CertRolePersonDecisionByPersonId | PERSON_ID | — | — |
| 15 | CertRolePersonDecisionByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | CertRolePersonUpdatedByDisName | DISPLAY_NAME | — | ✅ |
| 17 | CertRolePersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | CertRolePersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | CertRolePersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | CertRolePersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CertCreatedByPersonId | PERSON_ID | — | — |
| 3 | CertCreatedByUserGuid | USER_GUID | — | — |
| 4 | CertCreatedByUserId | USER_ID | — | — |
| 5 | CertCreatedByUsername | USERNAME | — | — |
| 6 | CertRoleUserDecisionByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | CertRoleUserDecisionByPersonId | PERSON_ID | — | — |
| 8 | CertRoleUserDecisionByUserGuid | USER_GUID | — | — |
| 9 | CertRoleUserDecisionByUserId | USER_ID | — | — |
| 10 | CertRoleUserDecisionByUsername | USERNAME | — | — |
| 11 | CertRoleUserUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CertRoleUserUpdatedByPersonId | PERSON_ID | — | — |
| 13 | CertRoleUserUpdatedByUserGuid | USER_GUID | — | — |
| 14 | CertRoleUserUpdatedByUserId | USER_ID | — | — |
| 15 | CertRoleUserUpdatedByUsername | USERNAME | — | — |
| 16 | CertUserUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | CertUserUpdatedByPersonId | PERSON_ID | — | — |
| 18 | CertUserUpdatedByUserGuid | USER_GUID | — | — |
| 19 | CertUserUpdatedByUserId | USER_ID | — | — |
| 20 | CertUserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
