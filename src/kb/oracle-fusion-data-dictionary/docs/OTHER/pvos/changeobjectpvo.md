---
id: DOC-OTHER-PVO-ChangeObjectPVO
doc_type: system-doc
title: "ChangeObjectPVO — PVO Cross-Module"
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
  - ChangeObjectPVO
  - changeobjectpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeObjectPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Object. Acessa as tabelas: EGO_ENGINEERING_CHANGES_B, EGO_ENGINEERING_CHANGES_TL, HZ_CUST_ACCOUNTS.

**Caminho:** `FscmTopModelAM.ChangeObjectsAM.ChangeObjectPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 3 | 1 | 26 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]] — 43 atributos (1 PKs, 23 BICC)
- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 7 atributos (3 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 2 atributos

---

## ⚙️ Atributos

### [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeId | CHANGE_ID | 🔑 | ✅ |
| 2 | ChangeObjectBasePEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 3 | ChangeObjectBasePEOApprovalRequestDate | APPROVAL_REQUEST_DATE | — | ✅ |
| 4 | ChangeObjectBasePEOApprovalStatusType | APPROVAL_STATUS_TYPE | — | ✅ |
| 5 | ChangeObjectBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 6 | ChangeObjectBasePEOAssigneeRoleId | ASSIGNEE_ROLE_ID | — | ✅ |
| 7 | ChangeObjectBasePEOBaseChangeMgmtTypeCode | BASE_CHANGE_MGMT_TYPE_CODE | — | ✅ |
| 8 | ChangeObjectBasePEOCancellationDate | CANCELLATION_DATE | — | ✅ |
| 9 | ChangeObjectBasePEOChangeNotice | CHANGE_NOTICE | — | ✅ |
| 10 | ChangeObjectBasePEOChangeTypeId | CHANGE_TYPE_ID | — | ✅ |
| 11 | ChangeObjectBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | ChangeObjectBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | ChangeObjectBasePEOCustomerId | CUSTOMER_ID | — | — |
| 14 | ChangeObjectBasePEOHierarchyId | HIERARCHY_ID | — | — |
| 15 | ChangeObjectBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 16 | ChangeObjectBasePEOImplementationReqId | IMPLEMENTATION_REQ_ID | — | — |
| 17 | ChangeObjectBasePEOInitiationDate | INITIATION_DATE | — | ✅ |
| 18 | ChangeObjectBasePEOInternalUseOnly | INTERNAL_USE_ONLY | — | — |
| 19 | ChangeObjectBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 20 | ChangeObjectBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 21 | ChangeObjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ChangeObjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | ChangeObjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ChangeObjectBasePEOManufacturerId | MANUFACTURER_ID | — | — |
| 25 | ChangeObjectBasePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 26 | ChangeObjectBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ChangeObjectBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 28 | ChangeObjectBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 29 | ChangeObjectBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 30 | ChangeObjectBasePEOProgramName | PROGRAM_NAME | — | — |
| 31 | ChangeObjectBasePEOPromoteStatusCode | PROMOTE_STATUS_CODE | — | — |
| 32 | ChangeObjectBasePEOReasonCode | REASON_CODE | — | ✅ |
| 33 | ChangeObjectBasePEORequestId | REQUEST_ID | — | — |
| 34 | ChangeObjectBasePEORequestorId | REQUESTOR_ID | — | ✅ |
| 35 | ChangeObjectBasePEOSourceCode | SOURCE_CODE | — | — |
| 36 | ChangeObjectBasePEOSourceId | SOURCE_ID | — | — |
| 37 | ChangeObjectBasePEOSourceName | SOURCE_NAME | — | — |
| 38 | ChangeObjectBasePEOSourceTypeCode | SOURCE_TYPE_CODE | — | — |
| 39 | ChangeObjectBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 40 | ChangeObjectBasePEOStatusType | STATUS_TYPE | — | ✅ |
| 41 | ChangeObjectBasePEOSupplierId | SUPPLIER_ID | — | — |
| 42 | ChangeObjectBasePEOWfProcessInstanceId | WF_PROCESS_INSTANCE_ID | — | — |
| 43 | ChangeObjectBasePEOWfProcessTemplate | WF_PROCESS_TEMPLATE | — | — |

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectTLPEOCancellationComments | CANCELLATION_COMMENTS | — | — |
| 2 | ChangeObjectTLPEOChangeId | CHANGE_ID | — | — |
| 3 | ChangeObjectTLPEOChangeName | CHANGE_NAME | — | ✅ |
| 4 | ChangeObjectTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | ChangeObjectTLPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ChangeObjectTLPEOResolution | RESOLUTION | — | — |
| 7 | ChangeObjectTLPEOSourceLang | SOURCE_LANG | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 2 | CustomerAccountPEOPartyId | PARTY_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
