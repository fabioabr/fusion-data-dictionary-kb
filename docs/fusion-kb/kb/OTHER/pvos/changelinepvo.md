---
id: DOC-OTHER-PVO-ChangeLinePVO
doc_type: system-doc
title: "ChangeLinePVO — PVO Cross-Module"
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
  - ChangeLinePVO
  - changelinepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLinePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Line. Acessa as tabelas: EGO_CHANGE_LINES_B, EGO_CHANGE_LINES_TL, EGO_ENGINEERING_CHANGES_B (+3).

**Caminho:** `FscmTopModelAM.ChangeObjectsAM.ChangeLinePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 111 | 6 | 7 | 104 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_lines_b|EGO_CHANGE_LINES_B]] — 39 atributos (1 PKs, 38 BICC)
- [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]] — 12 atributos (1 PKs, 12 BICC)
- [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]] — 42 atributos (1 PKs, 38 BICC)
- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 7 atributos (1 PKs, 7 BICC)
- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 9 atributos (3 PKs, 9 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 2 atributos

---

## ⚙️ Atributos

### [[ego_change_lines_b|EGO_CHANGE_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineBasePEOAssignedBy | ASSIGNED_BY | — | — |
| 2 | ChangeLineBasePEOAssignedDate | ASSIGNED_DATE | — | ✅ |
| 3 | ChangeLineBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 4 | ChangeLineBasePEOCancelationDate | CANCELATION_DATE | — | ✅ |
| 5 | ChangeLineBasePEOChangeId | CHANGE_ID | — | ✅ |
| 6 | ChangeLineBasePEOCompleteBeforeStatusCode | COMPLETE_BEFORE_STATUS_CODE | — | ✅ |
| 7 | ChangeLineBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ChangeLineBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ChangeLineBasePEOEffectivityOnApprovalFlag | EFFECTIVITY_ON_APPROVAL_FLAG | — | ✅ |
| 10 | ChangeLineBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 11 | ChangeLineBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 12 | ChangeLineBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 13 | ChangeLineBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ChangeLineBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ChangeLineBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ChangeLineBasePEOLifecycleStateId | LIFECYCLE_STATE_ID | — | ✅ |
| 17 | ChangeLineBasePEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 18 | ChangeLineBasePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 19 | ChangeLineBasePEONewItemRevision | NEW_ITEM_REVISION | — | ✅ |
| 20 | ChangeLineBasePEONewItemRevisionId | NEW_ITEM_REVISION_ID | — | ✅ |
| 21 | ChangeLineBasePEONewRevisionReason | NEW_REVISION_REASON | — | ✅ |
| 22 | ChangeLineBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | ChangeLineBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 24 | ChangeLineBasePEOPk1Value | PK1_VALUE | — | ✅ |
| 25 | ChangeLineBasePEOPk2Value | PK2_VALUE | — | ✅ |
| 26 | ChangeLineBasePEOPk3Value | PK3_VALUE | — | ✅ |
| 27 | ChangeLineBasePEOPk4Value | PK4_VALUE | — | ✅ |
| 28 | ChangeLineBasePEOPk5Value | PK5_VALUE | — | ✅ |
| 29 | ChangeLineBasePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 30 | ChangeLineBasePEOProgramName | PROGRAM_NAME | — | ✅ |
| 31 | ChangeLineBasePEORequestId | REQUEST_ID | — | ✅ |
| 32 | ChangeLineBasePEORequiredFlag | REQUIRED_FLAG | — | ✅ |
| 33 | ChangeLineBasePEOScheduledDate | SCHEDULED_DATE | — | ✅ |
| 34 | ChangeLineBasePEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 35 | ChangeLineBasePEOStartAfterStatusCode | START_AFTER_STATUS_CODE | — | ✅ |
| 36 | ChangeLineBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 37 | ChangeLineBasePEOStatusType | STATUS_TYPE | — | ✅ |
| 38 | ChangeLineBasePEOSubjectInternalName | SUBJECT_INTERNAL_NAME | — | ✅ |
| 39 | ChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |

### [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineTLPEOCancelComments | CANCEL_COMMENTS | — | ✅ |
| 2 | ChangeLineTLPEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 3 | ChangeLineTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ChangeLineTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ChangeLineTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | ChangeLineTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ChangeLineTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ChangeLineTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ChangeLineTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ChangeLineTLPEOName | NAME | — | ✅ |
| 11 | ChangeLineTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ChangeLineTLPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectBasePEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | ChangeObjectBasePEOApprovalRequestDate | APPROVAL_REQUEST_DATE | — | ✅ |
| 3 | ChangeObjectBasePEOApprovalStatusType | APPROVAL_STATUS_TYPE | — | ✅ |
| 4 | ChangeObjectBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 5 | ChangeObjectBasePEOAssigneeRoleId | ASSIGNEE_ROLE_ID | — | ✅ |
| 6 | ChangeObjectBasePEOBaseChangeMgmtTypeCode | BASE_CHANGE_MGMT_TYPE_CODE | — | ✅ |
| 7 | ChangeObjectBasePEOCancellationDate | CANCELLATION_DATE | — | ✅ |
| 8 | ChangeObjectBasePEOChangeId | CHANGE_ID | 🔑 | ✅ |
| 9 | ChangeObjectBasePEOChangeNotice | CHANGE_NOTICE | — | ✅ |
| 10 | ChangeObjectBasePEOChangeTypeId | CHANGE_TYPE_ID | — | ✅ |
| 11 | ChangeObjectBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | ChangeObjectBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | ChangeObjectBasePEOCustomerId | CUSTOMER_ID | — | — |
| 14 | ChangeObjectBasePEOHierarchyId | HIERARCHY_ID | — | ✅ |
| 15 | ChangeObjectBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 16 | ChangeObjectBasePEOImplementationReqId | IMPLEMENTATION_REQ_ID | — | ✅ |
| 17 | ChangeObjectBasePEOInitiationDate | INITIATION_DATE | — | ✅ |
| 18 | ChangeObjectBasePEOInternalUseOnly | INTERNAL_USE_ONLY | — | ✅ |
| 19 | ChangeObjectBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 20 | ChangeObjectBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 21 | ChangeObjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ChangeObjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ChangeObjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ChangeObjectBasePEOManufacturerId | MANUFACTURER_ID | — | — |
| 25 | ChangeObjectBasePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 26 | ChangeObjectBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 27 | ChangeObjectBasePEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 28 | ChangeObjectBasePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 29 | ChangeObjectBasePEOProgramName | PROGRAM_NAME | — | ✅ |
| 30 | ChangeObjectBasePEOPromoteStatusCode | PROMOTE_STATUS_CODE | — | ✅ |
| 31 | ChangeObjectBasePEOReasonCode | REASON_CODE | — | ✅ |
| 32 | ChangeObjectBasePEORequestId | REQUEST_ID | — | ✅ |
| 33 | ChangeObjectBasePEORequestorId | REQUESTOR_ID | — | ✅ |
| 34 | ChangeObjectBasePEOSourceCode | SOURCE_CODE | — | — |
| 35 | ChangeObjectBasePEOSourceId | SOURCE_ID | — | ✅ |
| 36 | ChangeObjectBasePEOSourceName | SOURCE_NAME | — | ✅ |
| 37 | ChangeObjectBasePEOSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 38 | ChangeObjectBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 39 | ChangeObjectBasePEOStatusType | STATUS_TYPE | — | ✅ |
| 40 | ChangeObjectBasePEOSupplierId | SUPPLIER_ID | — | — |
| 41 | ChangeObjectBasePEOWfProcessInstanceId | WF_PROCESS_INSTANCE_ID | — | ✅ |
| 42 | ChangeObjectBasePEOWfProcessTemplate | WF_PROCESS_TEMPLATE | — | ✅ |

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectTLPEOCancellationComments | CANCELLATION_COMMENTS | — | ✅ |
| 2 | ChangeObjectTLPEOChangeId | CHANGE_ID | — | ✅ |
| 3 | ChangeObjectTLPEOChangeName | CHANGE_NAME | — | ✅ |
| 4 | ChangeObjectTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | ChangeObjectTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ChangeObjectTLPEOResolution | RESOLUTION | — | ✅ |
| 7 | ChangeObjectTLPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAssociationPEOAcdType | ACD_TYPE | 🔑 | ✅ |
| 2 | ItemSupplierAssociationPEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 3 | ItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 4 | ItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 5 | ItemSupplierAssociationPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 6 | ItemSupplierAssociationPEOStatusCode | STATUS_CODE | — | ✅ |
| 7 | ItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | 🔑 | ✅ |
| 8 | ItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | 🔑 | ✅ |
| 9 | ItemSupplierAssociationPEOVersionId | VERSION_ID | — | ✅ |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 2 | CustomerAccountPEOPartyId | PARTY_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
