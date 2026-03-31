---
id: DOC-OTHER-PVO-WorkOrderBIPVOUnsecured
doc_type: system-doc
title: "WorkOrderBIPVOUnsecured — PVO Cross-Module"
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
  - WorkOrderBIPVOUnsecured
  - workorderbipvounsecured
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderBIPVOUnsecured

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order BIUnsecured. Acessa as tabelas: SVC_SERVICE_REQUESTS, SVC_WORK_ORDERS, SVC_WO_STATUS_MAP (+2).

**Caminho:** `FscmTopModelAM.ServiceRequestAM.WorkOrderBIPVOUnsecured`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 108 | 5 | 1 | 24 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[svc_service_requests|SVC_SERVICE_REQUESTS]] — 4 atributos
- [[svc_work_orders|SVC_WORK_ORDERS]] — 72 atributos (1 PKs, 21 BICC)
- [[svc_wo_status_map|SVC_WO_STATUS_MAP]] — 10 atributos
- [[svc_wo_type_map|SVC_WO_TYPE_MAP]] — 11 atributos (2 BICC)
- [[zca_asset|ZCA_ASSET]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[svc_service_requests|SVC_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ServiceRequestUnsecuredPEODeletedFlag | DELETED_FLAG | — | — |
| 2 | ServiceRequestUnsecuredPEOSrId | SR_ID | — | — |
| 3 | SrvReqPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | SrvReqPEOStripeCd | STRIPE_CD | — | — |

### [[svc_work_orders|SVC_WORK_ORDERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountPartyId | ACCOUNT_PARTY_ID | — | — |
| 2 | ActualEndDate | ACTUAL_END_DATE | — | ✅ |
| 3 | ActualStartDate | ACTUAL_START_DATE | — | — |
| 4 | Address1 | ADDRESS1 | — | ✅ |
| 5 | Address2 | ADDRESS2 | — | ✅ |
| 6 | Address3 | ADDRESS3 | — | ✅ |
| 7 | Address4 | ADDRESS4 | — | ✅ |
| 8 | AssigneeResourceId | ASSIGNEE_RESOURCE_ID | — | — |
| 9 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 10 | BookedDate | BOOKED_DATE | — | — |
| 11 | CancelReason | CANCEL_REASON | — | — |
| 12 | CaseNote | CASE_NOTE | — | — |
| 13 | City | CITY | — | ✅ |
| 14 | ContactAltPhoneNumber | CONTACT_ALT_PHONE_NUMBER | — | — |
| 15 | ContactEmail | CONTACT_EMAIL | — | — |
| 16 | ContactLanguageCode | CONTACT_LANGUAGE_CODE | — | — |
| 17 | ContactName | CONTACT_NAME | — | — |
| 18 | ContactPartyId | CONTACT_PARTY_ID | — | — |
| 19 | ContactPhoneNumber | CONTACT_PHONE_NUMBER | — | — |
| 20 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 21 | Country | COUNTRY | — | ✅ |
| 22 | County | COUNTY | — | ✅ |
| 23 | CreatedBy | CREATED_BY | — | — |
| 24 | CreationDate | CREATION_DATE | — | — |
| 25 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 26 | CurrencyCode | CURRENCY_CODE | — | — |
| 27 | DeletedFlag | DELETED_FLAG | — | — |
| 28 | DeliveryWinEndDate | DELIVERY_WIN_END_DATE | — | — |
| 29 | DeliveryWinStartDate | DELIVERY_WIN_START_DATE | — | — |
| 30 | Duration | DURATION | — | ✅ |
| 31 | EstimatedStartDate | ESTIMATED_START_DATE | — | — |
| 32 | FsActivityId | FS_ACTIVITY_ID | — | — |
| 33 | FsContactFlag | FS_CONTACT_FLAG | — | — |
| 34 | FsErrorDetail | FS_ERROR_DETAIL | — | — |
| 35 | FsNote | FS_NOTE | — | — |
| 36 | FsResource | FS_RESOURCE | — | — |
| 37 | IBAssetId | IB_ASSET_ID | — | — |
| 38 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | LastUpdateSourceCd | LAST_UPDATE_SOURCE_CD | — | — |
| 41 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | OpportunityId | OPPORTUNITY_ID | — | — |
| 44 | OverridePartyId | OVERRIDE_PARTY_ID | — | — |
| 45 | OverrideReason | OVERRIDE_REASON | — | — |
| 46 | OverrideStatusCd | OVERRIDE_STATUS_CD | — | — |
| 47 | PostalCode | POSTAL_CODE | — | ✅ |
| 48 | PrimaryAssetId | PRIMARY_ASSET_ID | — | — |
| 49 | Province | PROVINCE | — | ✅ |
| 50 | ReminderTime | REMINDER_TIME | — | — |
| 51 | RequestedByPartyId | REQUESTED_BY_PARTY_ID | — | — |
| 52 | RequestedDate | REQUESTED_DATE | — | ✅ |
| 53 | RequestedTimeSlot | REQUESTED_TIME_SLOT | — | — |
| 54 | RescheduleReason | RESCHEDULE_REASON | — | — |
| 55 | ResolutionDueDate | RESOLUTION_DUE_DATE | — | — |
| 56 | ScheduledDate | SCHEDULED_DATE | — | ✅ |
| 57 | ScheduledTimeSlot | SCHEDULED_TIME_SLOT | — | — |
| 58 | SourceCd | SOURCE_CD | — | — |
| 59 | SrId | SR_ID | — | — |
| 60 | State | STATE | — | ✅ |
| 61 | StripeCd | STRIPE_CD | — | — |
| 62 | TimezoneCode | TIMEZONE_CODE | — | ✅ |
| 63 | Title | TITLE | — | — |
| 64 | TravelTime | TRAVEL_TIME | — | ✅ |
| 65 | WoArea | WO_AREA | — | ✅ |
| 66 | WoId | WO_ID | 🔑 | ✅ |
| 67 | WoIntegrationCd | WO_INTEGRATION_CD | — | — |
| 68 | WoIntegrationMsgCd | WO_INTEGRATION_MSG_CD | — | — |
| 69 | WoIntegrationStatusCd | WO_INTEGRATION_STATUS_CD | — | — |
| 70 | WoNumber | WO_NUMBER | — | ✅ |
| 71 | WoStatusCd | WO_STATUS_CD | — | ✅ |
| 72 | WoTypeId | WO_TYPE_ID | — | — |

### [[svc_wo_status_map|SVC_WO_STATUS_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderStatusMapBIPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderStatusMapBIPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkOrderStatusMapBIPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | WorkOrderStatusMapBIPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | WorkOrderStatusMapBIPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | WorkOrderStatusMapBIPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | WorkOrderStatusMapBIPEOWoIntegrationCd | WO_INTEGRATION_CD | — | — |
| 8 | WorkOrderStatusMapBIPEOWoStatusCatCd | WO_STATUS_CAT_CD | — | — |
| 9 | WorkOrderStatusMapBIPEOWoStatusCd | WO_STATUS_CD | — | — |
| 10 | WorkOrderStatusMapBIPEOWoStatusLookupType | WO_STATUS_LOOKUP_TYPE | — | — |

### [[svc_wo_type_map|SVC_WO_TYPE_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderTypeMapBIPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderTypeMapBIPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkOrderTypeMapBIPEODefaultDuration | DEFAULT_DURATION | — | — |
| 4 | WorkOrderTypeMapBIPEOFsTypeCd | FS_TYPE_CD | — | — |
| 5 | WorkOrderTypeMapBIPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkOrderTypeMapBIPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | WorkOrderTypeMapBIPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | WorkOrderTypeMapBIPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | WorkOrderTypeMapBIPEOWoTypeCd | WO_TYPE_CD | — | ✅ |
| 10 | WorkOrderTypeMapBIPEOWoTypeId | WO_TYPE_ID | — | — |
| 11 | WorkOrderTypeMapBIPEOWoTypeLookupType | WO_TYPE_LOOKUP_TYPE | — | — |

### [[zca_asset|ZCA_ASSET]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOAssetId | ASSET_ID | — | — |
| 2 | AssetPEOCreatedBy | CREATED_BY | — | — |
| 3 | AssetPEOCreationDate | CREATION_DATE | — | — |
| 4 | AssetPEODeleteFlag | DELETE_FLAG | — | — |
| 5 | AssetPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | AssetPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 7 | AssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AssetPEOProdGroupId | PROD_GROUP_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
