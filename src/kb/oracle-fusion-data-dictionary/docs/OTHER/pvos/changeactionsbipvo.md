---
id: DOC-OTHER-PVO-ChangeActionsBIPVO
doc_type: system-doc
title: "ChangeActionsBIPVO — PVO Cross-Module"
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
  - ChangeActionsBIPVO
  - changeactionsbipvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeActionsBIPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Actions BI. Acessa as tabelas: EGO_CHANGE_ACTIONS_VL, EGO_CHANGE_LINES_B, EGO_CHANGE_LINES_TL (+4).

**Caminho:** `FscmTopModelAM.ChangeObjectsAM.ChangeActionsBIPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 273 | 7 | 1 | 51 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_actions_vl|EGO_CHANGE_ACTIONS_VL]] — 32 atributos (1 PKs, 7 BICC)
- [[ego_change_lines_b|EGO_CHANGE_LINES_B]] — 90 atributos (20 BICC)
- [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]] — 12 atributos (4 BICC)
- [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]] — 94 atributos (14 BICC)
- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 13 atributos (4 BICC)
- [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]] — 30 atributos (2 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 2 atributos

---

## ⚙️ Atributos

### [[ego_change_actions_vl|EGO_CHANGE_ACTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeActionsActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ChangeActionsActionType | ACTION_TYPE | — | ✅ |
| 3 | ChangeActionsAssigneeId | ASSIGNEE_ID | — | — |
| 4 | ChangeActionsCreatedBy | CREATED_BY | — | ✅ |
| 5 | ChangeActionsCreationDate | CREATION_DATE | — | ✅ |
| 6 | ChangeActionsDescription | DESCRIPTION | — | ✅ |
| 7 | ChangeActionsImplementationReqId | IMPLEMENTATION_REQ_ID | — | — |
| 8 | ChangeActionsJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | ChangeActionsJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | ChangeActionsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ChangeActionsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ChangeActionsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ChangeActionsLocalOrganizationId | LOCAL_ORGANIZATION_ID | — | — |
| 14 | ChangeActionsObjectId1 | OBJECT_ID1 | — | — |
| 15 | ChangeActionsObjectId2 | OBJECT_ID2 | — | — |
| 16 | ChangeActionsObjectId3 | OBJECT_ID3 | — | — |
| 17 | ChangeActionsObjectId4 | OBJECT_ID4 | — | — |
| 18 | ChangeActionsObjectId5 | OBJECT_ID5 | — | — |
| 19 | ChangeActionsObjectName | OBJECT_NAME | — | — |
| 20 | ChangeActionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ChangeActionsOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 22 | ChangeActionsParentActionId | PARENT_ACTION_ID | — | — |
| 23 | ChangeActionsParentStatusCode | PARENT_STATUS_CODE | — | — |
| 24 | ChangeActionsPartyIdList | PARTY_ID_LIST | — | — |
| 25 | ChangeActionsPriorityCode | PRIORITY_CODE | — | — |
| 26 | ChangeActionsProgramAppName | PROGRAM_APP_NAME | — | — |
| 27 | ChangeActionsProgramName | PROGRAM_NAME | — | — |
| 28 | ChangeActionsRequestId | REQUEST_ID | — | — |
| 29 | ChangeActionsResponseByDate | RESPONSE_BY_DATE | — | — |
| 30 | ChangeActionsStatusCode | STATUS_CODE | — | ✅ |
| 31 | ChangeActionsWfProcessInstanceId | WF_PROCESS_INSTANCE_ID | — | — |
| 32 | ChangeActionsWfProcessTemplate | WF_PROCESS_TEMPLATE | — | — |

### [[ego_change_lines_b|EGO_CHANGE_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineBaseAssignedBy | ASSIGNED_BY | — | — |
| 2 | ChangeLineBaseAssignedDate | ASSIGNED_DATE | — | ✅ |
| 3 | ChangeLineBaseAssigneeId2 | ASSIGNEE_ID | — | — |
| 4 | ChangeLineBaseAttribute101 | ATTRIBUTE10 | — | — |
| 5 | ChangeLineBaseAttribute110 | ATTRIBUTE1 | — | — |
| 6 | ChangeLineBaseAttribute111 | ATTRIBUTE11 | — | — |
| 7 | ChangeLineBaseAttribute121 | ATTRIBUTE12 | — | — |
| 8 | ChangeLineBaseAttribute131 | ATTRIBUTE13 | — | — |
| 9 | ChangeLineBaseAttribute141 | ATTRIBUTE14 | — | — |
| 10 | ChangeLineBaseAttribute151 | ATTRIBUTE15 | — | — |
| 11 | ChangeLineBaseAttribute161 | ATTRIBUTE16 | — | — |
| 12 | ChangeLineBaseAttribute171 | ATTRIBUTE17 | — | — |
| 13 | ChangeLineBaseAttribute181 | ATTRIBUTE18 | — | — |
| 14 | ChangeLineBaseAttribute191 | ATTRIBUTE19 | — | — |
| 15 | ChangeLineBaseAttribute201 | ATTRIBUTE20 | — | — |
| 16 | ChangeLineBaseAttribute210 | ATTRIBUTE2 | — | — |
| 17 | ChangeLineBaseAttribute211 | ATTRIBUTE21 | — | — |
| 18 | ChangeLineBaseAttribute221 | ATTRIBUTE22 | — | — |
| 19 | ChangeLineBaseAttribute231 | ATTRIBUTE23 | — | — |
| 20 | ChangeLineBaseAttribute241 | ATTRIBUTE24 | — | — |
| 21 | ChangeLineBaseAttribute251 | ATTRIBUTE25 | — | — |
| 22 | ChangeLineBaseAttribute261 | ATTRIBUTE26 | — | — |
| 23 | ChangeLineBaseAttribute271 | ATTRIBUTE27 | — | — |
| 24 | ChangeLineBaseAttribute281 | ATTRIBUTE28 | — | — |
| 25 | ChangeLineBaseAttribute291 | ATTRIBUTE29 | — | — |
| 26 | ChangeLineBaseAttribute301 | ATTRIBUTE30 | — | — |
| 27 | ChangeLineBaseAttribute31 | ATTRIBUTE3 | — | — |
| 28 | ChangeLineBaseAttribute41 | ATTRIBUTE4 | — | — |
| 29 | ChangeLineBaseAttribute51 | ATTRIBUTE5 | — | — |
| 30 | ChangeLineBaseAttribute61 | ATTRIBUTE6 | — | — |
| 31 | ChangeLineBaseAttribute71 | ATTRIBUTE7 | — | — |
| 32 | ChangeLineBaseAttribute81 | ATTRIBUTE8 | — | — |
| 33 | ChangeLineBaseAttribute91 | ATTRIBUTE9 | — | — |
| 34 | ChangeLineBaseAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 35 | ChangeLineBaseAttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 36 | ChangeLineBaseAttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 37 | ChangeLineBaseAttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 38 | ChangeLineBaseAttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 39 | ChangeLineBaseAttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 40 | ChangeLineBaseAttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 41 | ChangeLineBaseAttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 42 | ChangeLineBaseAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 43 | ChangeLineBaseAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 44 | ChangeLineBaseAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 45 | ChangeLineBaseAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 46 | ChangeLineBaseAttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 47 | ChangeLineBaseAttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 48 | ChangeLineBaseAttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 49 | ChangeLineBaseAttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 50 | ChangeLineBaseAttributeTimestamp11 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 51 | ChangeLineBaseAttributeTimestamp21 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 52 | ChangeLineBaseAttributeTimestamp31 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 53 | ChangeLineBaseAttributeTimestamp41 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 54 | ChangeLineBaseAttributeTimestamp51 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 55 | ChangeLineBaseCancelationDate | CANCELATION_DATE | — | — |
| 56 | ChangeLineBaseChangeId2 | CHANGE_ID | — | — |
| 57 | ChangeLineBaseChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 58 | ChangeLineBaseCompleteBeforeStatusCode | COMPLETE_BEFORE_STATUS_CODE | — | ✅ |
| 59 | ChangeLineBaseCreatedBy3 | CREATED_BY | — | ✅ |
| 60 | ChangeLineBaseCreationDate3 | CREATION_DATE | — | ✅ |
| 61 | ChangeLineBaseEffectivityOnApprovalFlag | EFFECTIVITY_ON_APPROVAL_FLAG | — | ✅ |
| 62 | ChangeLineBaseImplementationDate1 | IMPLEMENTATION_DATE | — | ✅ |
| 63 | ChangeLineBaseJobDefinitionName2 | JOB_DEFINITION_NAME | — | — |
| 64 | ChangeLineBaseJobDefinitionPackage2 | JOB_DEFINITION_PACKAGE | — | — |
| 65 | ChangeLineBaseLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 66 | ChangeLineBaseLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 67 | ChangeLineBaseLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 68 | ChangeLineBaseLifecycleStateId | LIFECYCLE_STATE_ID | — | — |
| 69 | ChangeLineBaseLineTypeId | LINE_TYPE_ID | — | — |
| 70 | ChangeLineBaseNeedByDate1 | NEED_BY_DATE | — | ✅ |
| 71 | ChangeLineBaseNewItemRevision | NEW_ITEM_REVISION | — | ✅ |
| 72 | ChangeLineBaseNewItemRevisionId | NEW_ITEM_REVISION_ID | — | — |
| 73 | ChangeLineBaseNewRevisionReason | NEW_REVISION_REASON | — | ✅ |
| 74 | ChangeLineBaseObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 75 | ChangeLineBaseOrganizationId1 | ORGANIZATION_ID | — | ✅ |
| 76 | ChangeLineBasePk1Value | PK1_VALUE | — | ✅ |
| 77 | ChangeLineBasePk2Value | PK2_VALUE | — | ✅ |
| 78 | ChangeLineBasePk3Value | PK3_VALUE | — | — |
| 79 | ChangeLineBasePk4Value | PK4_VALUE | — | — |
| 80 | ChangeLineBasePk5Value | PK5_VALUE | — | — |
| 81 | ChangeLineBaseProgramAppName2 | PROGRAM_APP_NAME | — | — |
| 82 | ChangeLineBaseProgramName2 | PROGRAM_NAME | — | — |
| 83 | ChangeLineBaseRequestId2 | REQUEST_ID | — | — |
| 84 | ChangeLineBaseRequiredFlag | REQUIRED_FLAG | — | ✅ |
| 85 | ChangeLineBaseScheduledDate | SCHEDULED_DATE | — | ✅ |
| 86 | ChangeLineBaseSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 87 | ChangeLineBaseStartAfterStatusCode | START_AFTER_STATUS_CODE | — | ✅ |
| 88 | ChangeLineBaseStatusCode2 | STATUS_CODE | — | ✅ |
| 89 | ChangeLineBaseStatusType1 | STATUS_TYPE | — | — |
| 90 | ChangeLineBaseSubjectInternalName | SUBJECT_INTERNAL_NAME | — | ✅ |

### [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineTLCancelComments | CANCEL_COMMENTS | — | — |
| 2 | ChangeLineTLChangeLineId1 | CHANGE_LINE_ID | — | — |
| 3 | ChangeLineTLCreatedBy4 | CREATED_BY | — | — |
| 4 | ChangeLineTLCreationDate4 | CREATION_DATE | — | — |
| 5 | ChangeLineTLDescription2 | DESCRIPTION | — | ✅ |
| 6 | ChangeLineTLLanguage1 | LANGUAGE | — | ✅ |
| 7 | ChangeLineTLLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 8 | ChangeLineTLLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 9 | ChangeLineTLLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 10 | ChangeLineTLName | NAME | — | ✅ |
| 11 | ChangeLineTLObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 12 | ChangeLineTLSourceLang1 | SOURCE_LANG | — | — |

### [[ego_engineering_changes_b|EGO_ENGINEERING_CHANGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectBaseApprovalDate | APPROVAL_DATE | — | ✅ |
| 2 | ChangeObjectBaseApprovalRequestDate | APPROVAL_REQUEST_DATE | — | ✅ |
| 3 | ChangeObjectBaseApprovalStatusType | APPROVAL_STATUS_TYPE | — | — |
| 4 | ChangeObjectBaseAssigneeId1 | ASSIGNEE_ID | — | — |
| 5 | ChangeObjectBaseAssigneeRoleId | ASSIGNEE_ROLE_ID | — | ✅ |
| 6 | ChangeObjectBaseAttribute1 | ATTRIBUTE1 | — | — |
| 7 | ChangeObjectBaseAttribute10 | ATTRIBUTE10 | — | — |
| 8 | ChangeObjectBaseAttribute11 | ATTRIBUTE11 | — | — |
| 9 | ChangeObjectBaseAttribute12 | ATTRIBUTE12 | — | — |
| 10 | ChangeObjectBaseAttribute13 | ATTRIBUTE13 | — | — |
| 11 | ChangeObjectBaseAttribute14 | ATTRIBUTE14 | — | — |
| 12 | ChangeObjectBaseAttribute15 | ATTRIBUTE15 | — | — |
| 13 | ChangeObjectBaseAttribute16 | ATTRIBUTE16 | — | — |
| 14 | ChangeObjectBaseAttribute17 | ATTRIBUTE17 | — | — |
| 15 | ChangeObjectBaseAttribute18 | ATTRIBUTE18 | — | — |
| 16 | ChangeObjectBaseAttribute19 | ATTRIBUTE19 | — | — |
| 17 | ChangeObjectBaseAttribute2 | ATTRIBUTE2 | — | — |
| 18 | ChangeObjectBaseAttribute20 | ATTRIBUTE20 | — | — |
| 19 | ChangeObjectBaseAttribute21 | ATTRIBUTE21 | — | — |
| 20 | ChangeObjectBaseAttribute22 | ATTRIBUTE22 | — | — |
| 21 | ChangeObjectBaseAttribute23 | ATTRIBUTE23 | — | — |
| 22 | ChangeObjectBaseAttribute24 | ATTRIBUTE24 | — | — |
| 23 | ChangeObjectBaseAttribute25 | ATTRIBUTE25 | — | — |
| 24 | ChangeObjectBaseAttribute26 | ATTRIBUTE26 | — | — |
| 25 | ChangeObjectBaseAttribute27 | ATTRIBUTE27 | — | — |
| 26 | ChangeObjectBaseAttribute28 | ATTRIBUTE28 | — | — |
| 27 | ChangeObjectBaseAttribute29 | ATTRIBUTE29 | — | — |
| 28 | ChangeObjectBaseAttribute3 | ATTRIBUTE3 | — | — |
| 29 | ChangeObjectBaseAttribute30 | ATTRIBUTE30 | — | — |
| 30 | ChangeObjectBaseAttribute4 | ATTRIBUTE4 | — | — |
| 31 | ChangeObjectBaseAttribute5 | ATTRIBUTE5 | — | — |
| 32 | ChangeObjectBaseAttribute6 | ATTRIBUTE6 | — | — |
| 33 | ChangeObjectBaseAttribute7 | ATTRIBUTE7 | — | — |
| 34 | ChangeObjectBaseAttribute8 | ATTRIBUTE8 | — | — |
| 35 | ChangeObjectBaseAttribute9 | ATTRIBUTE9 | — | — |
| 36 | ChangeObjectBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | ChangeObjectBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | ChangeObjectBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | ChangeObjectBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | ChangeObjectBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | ChangeObjectBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | ChangeObjectBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 43 | ChangeObjectBaseAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 44 | ChangeObjectBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 45 | ChangeObjectBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 46 | ChangeObjectBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 47 | ChangeObjectBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 48 | ChangeObjectBaseAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 49 | ChangeObjectBaseAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 50 | ChangeObjectBaseAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 51 | ChangeObjectBaseAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 52 | ChangeObjectBaseAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 53 | ChangeObjectBaseAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 54 | ChangeObjectBaseAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 55 | ChangeObjectBaseAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 56 | ChangeObjectBaseAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 57 | ChangeObjectBaseBaseChangeMgmtTypeCode | BASE_CHANGE_MGMT_TYPE_CODE | — | — |
| 58 | ChangeObjectBaseCancellationDate | CANCELLATION_DATE | — | ✅ |
| 59 | ChangeObjectBaseChangeId | CHANGE_ID | — | ✅ |
| 60 | ChangeObjectBaseChangeNotice | CHANGE_NOTICE | — | ✅ |
| 61 | ChangeObjectBaseChangeTypeId | CHANGE_TYPE_ID | — | — |
| 62 | ChangeObjectBaseCreatedBy1 | CREATED_BY | — | ✅ |
| 63 | ChangeObjectBaseCreationDate1 | CREATION_DATE | — | ✅ |
| 64 | ChangeObjectBaseCustomerId | CUSTOMER_ID | — | — |
| 65 | ChangeObjectBaseHierarchyId | HIERARCHY_ID | — | — |
| 66 | ChangeObjectBaseImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 67 | ChangeObjectBaseImplementationReqId1 | IMPLEMENTATION_REQ_ID | — | — |
| 68 | ChangeObjectBaseInitiationDate | INITIATION_DATE | — | ✅ |
| 69 | ChangeObjectBaseInternalUseOnly | INTERNAL_USE_ONLY | — | — |
| 70 | ChangeObjectBaseJobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 71 | ChangeObjectBaseJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 72 | ChangeObjectBaseLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 73 | ChangeObjectBaseLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 74 | ChangeObjectBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 75 | ChangeObjectBaseManufacturerId | MANUFACTURER_ID | — | — |
| 76 | ChangeObjectBaseNeedByDate | NEED_BY_DATE | — | ✅ |
| 77 | ChangeObjectBaseObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 78 | ChangeObjectBaseOrganizationId | ORGANIZATION_ID | — | — |
| 79 | ChangeObjectBasePriorityCode1 | PRIORITY_CODE | — | — |
| 80 | ChangeObjectBaseProgramAppName1 | PROGRAM_APP_NAME | — | — |
| 81 | ChangeObjectBaseProgramName1 | PROGRAM_NAME | — | — |
| 82 | ChangeObjectBasePromoteStatusCode | PROMOTE_STATUS_CODE | — | — |
| 83 | ChangeObjectBaseReasonCode | REASON_CODE | — | — |
| 84 | ChangeObjectBaseRequestId1 | REQUEST_ID | — | — |
| 85 | ChangeObjectBaseRequestorId | REQUESTOR_ID | — | — |
| 86 | ChangeObjectBaseSourceCode | SOURCE_CODE | — | — |
| 87 | ChangeObjectBaseSourceId | SOURCE_ID | — | — |
| 88 | ChangeObjectBaseSourceName | SOURCE_NAME | — | — |
| 89 | ChangeObjectBaseSourceTypeCode | SOURCE_TYPE_CODE | — | — |
| 90 | ChangeObjectBaseStatusCode1 | STATUS_CODE | — | ✅ |
| 91 | ChangeObjectBaseStatusType | STATUS_TYPE | — | ✅ |
| 92 | ChangeObjectBaseSupplierId | SUPPLIER_ID | — | — |
| 93 | ChangeObjectBaseWfProcessInstanceId1 | WF_PROCESS_INSTANCE_ID | — | — |
| 94 | ChangeObjectBaseWfProcessTemplate1 | WF_PROCESS_TEMPLATE | — | — |

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectTLCancellationComments | CANCELLATION_COMMENTS | — | — |
| 2 | ChangeObjectTLChangeId1 | CHANGE_ID | — | — |
| 3 | ChangeObjectTLChangeName | CHANGE_NAME | — | ✅ |
| 4 | ChangeObjectTLCreatedBy2 | CREATED_BY | — | — |
| 5 | ChangeObjectTLCreationDate2 | CREATION_DATE | — | — |
| 6 | ChangeObjectTLDescription1 | DESCRIPTION | — | ✅ |
| 7 | ChangeObjectTLLanguage | LANGUAGE | — | ✅ |
| 8 | ChangeObjectTLLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 9 | ChangeObjectTLLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 10 | ChangeObjectTLLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 11 | ChangeObjectTLObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 12 | ChangeObjectTLResolution | RESOLUTION | — | — |
| 13 | ChangeObjectTLSourceLang | SOURCE_LANG | — | — |

### [[ego_item_associations|EGO_ITEM_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemSupplierAssociationAcdType | ACD_TYPE | — | — |
| 2 | ItemSupplierAssociationAssociationId | ASSOCIATION_ID | — | — |
| 3 | ItemSupplierAssociationChangeBitMap | CHANGE_BIT_MAP | — | — |
| 4 | ItemSupplierAssociationChangeLineId2 | CHANGE_LINE_ID | — | — |
| 5 | ItemSupplierAssociationCreatedBy5 | CREATED_BY | — | — |
| 6 | ItemSupplierAssociationCreationDate5 | CREATION_DATE | — | — |
| 7 | ItemSupplierAssociationImplementationDate2 | IMPLEMENTATION_DATE | — | — |
| 8 | ItemSupplierAssociationInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 9 | ItemSupplierAssociationJobDefinitionName3 | JOB_DEFINITION_NAME | — | — |
| 10 | ItemSupplierAssociationJobDefinitionPackage3 | JOB_DEFINITION_PACKAGE | — | — |
| 11 | ItemSupplierAssociationLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 12 | ItemSupplierAssociationLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 13 | ItemSupplierAssociationLastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 14 | ItemSupplierAssociationObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 15 | ItemSupplierAssociationOrganizationId2 | ORGANIZATION_ID | — | — |
| 16 | ItemSupplierAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 17 | ItemSupplierAssociationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 18 | ItemSupplierAssociationPEOSupplierId | SUPPLIER_ID | — | — |
| 19 | ItemSupplierAssociationPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 20 | ItemSupplierAssociationPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 21 | ItemSupplierAssociationProgramAppName3 | PROGRAM_APP_NAME | — | — |
| 22 | ItemSupplierAssociationProgramName3 | PROGRAM_NAME | — | — |
| 23 | ItemSupplierAssociationRequestId3 | REQUEST_ID | — | — |
| 24 | ItemSupplierAssociationStatusCode3 | STATUS_CODE | — | — |
| 25 | ItemSupplierAssociationStyleItemId | STYLE_ITEM_ID | — | — |
| 26 | ItemSupplierAssociationSupplierId | SUPPLIER_ID | — | — |
| 27 | ItemSupplierAssociationSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 28 | ItemSupplierAssociationVersionEndDate | VERSION_END_DATE | — | — |
| 29 | ItemSupplierAssociationVersionId | VERSION_ID | — | — |
| 30 | VersionStartDate | VERSION_START_DATE | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountCustAccountId | CUST_ACCOUNT_ID | — | — |
| 2 | CustomerAccountPartyId | PARTY_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
