---
id: DOC-OTHER-PVO-ServiceRequestAnalyticsPVOUnsecured
doc_type: system-doc
title: "ServiceRequestAnalyticsPVOUnsecured — PVO Cross-Module"
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
  - ServiceRequestAnalyticsPVOUnsecured
  - servicerequestanalyticspvounsecured
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ServiceRequestAnalyticsPVOUnsecured

## 📌 Visão Geral

View Object para extração BICC de dados de Service Request Analytics Unsecured. Acessa as tabelas: HZ_PARTIES, SVC_CHANNEL_VIA, SVC_SERVICE_PROFILES (+1).

**Caminho:** `FscmTopModelAM.ServiceRequestAM.ServiceRequestAnalyticsPVOUnsecured`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 4 | 1 | 16 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 14 atributos
- [[svc_channel_via|SVC_CHANNEL_VIA]] — 3 atributos
- [[svc_service_profiles|SVC_SERVICE_PROFILES]] — 8 atributos
- [[svc_service_requests|SVC_SERVICE_REQUESTS]] — 71 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LastUpdatedByPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | LastUpdatedByPEOPartyId | PARTY_ID | — | — |
| 3 | LastUpdatedByPEOPartyName | PARTY_NAME | — | — |
| 4 | PrimaryContactPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PrimaryContactPartyPEOPartyId | PARTY_ID | — | — |
| 6 | PrimaryContactPartyPEOPartyName | PARTY_NAME | — | — |
| 7 | ReportedByPartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 8 | ReportedByPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReportedByPartyPEOPartyId | PARTY_ID | — | — |
| 10 | ReportedByPartyPEOPartyName | PARTY_NAME | — | — |
| 11 | ResolvedByPartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 12 | ResolvedByPartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ResolvedByPartyPEOPartyId | PARTY_ID | — | — |
| 14 | ResolvedByPartyPEOPartyName | PARTY_NAME | — | — |

### [[svc_channel_via|SVC_CHANNEL_VIA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChannelViaPEOChannelId | CHANNEL_ID | — | — |
| 2 | ChannelViaPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | ChannelViaPEOViaId | VIA_ID | — | — |

### [[svc_service_profiles|SVC_SERVICE_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SvcProfilePEOBillToCustomerAccountId | BILL_TO_CUST_ACCOUNT_ID | — | — |
| 2 | SvcProfilePEOBillToCustomerId | BILL_TO_CUST_ID | — | — |
| 3 | SvcProfilePEOBillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | — |
| 4 | SvcProfilePEOCustomerPartyId | CUSTOMER_PARTY_ID | — | — |
| 5 | SvcProfilePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | SvcProfilePEOPartySiteId | PARTY_SITE_ID | — | — |
| 7 | SvcProfilePEOPrimaryContactPartyId | PRIMARY_CONTACT_PARTY_ID | — | — |
| 8 | SvcProfilePEOServiceProfileId | SERVICE_PROFILE_ID | — | — |

### [[svc_service_requests|SVC_SERVICE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountPartyId | ACCOUNT_PARTY_ID | — | — |
| 2 | AssetId | ASSET_ID | — | — |
| 3 | AssigneeResourceId | ASSIGNEE_RESOURCE_ID | — | — |
| 4 | BUOrgId | BU_ORG_ID | — | — |
| 5 | CaseId | CASE_ID | — | — |
| 6 | CatalogId | CATALOG_ID | — | — |
| 7 | CategoryId | CATEGORY_ID | — | ✅ |
| 8 | ChannelTypeCd | CHANNEL_TYPE_CD | — | ✅ |
| 9 | ClosedDate | CLOSED_DATE | — | ✅ |
| 10 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 11 | CreatedBy | CREATED_BY | — | — |
| 12 | CreatedByPartyId | CREATED_BY_PARTY_ID | — | — |
| 13 | CreationDate | CREATION_DATE | — | ✅ |
| 14 | CriticalFlag | CRITICAL_FLAG | — | ✅ |
| 15 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 16 | CurrencyCode | CURRENCY_CODE | — | — |
| 17 | DeletedFlag | DELETED_FLAG | — | — |
| 18 | FirstTransferDate | FIRST_TRANSFER_DATE | — | — |
| 19 | IBAssetId | IB_ASSET_ID | — | — |
| 20 | InitQueueAssignDate | INIT_QUEUE_ASSIGN_DATE | — | — |
| 21 | InitResourceAssignDate | INIT_RESOURCE_ASSIGN_DATE | — | — |
| 22 | InternalPriorityCd | INTERNAL_PRIORITY_CD | — | — |
| 23 | InventoryItemId | INVENTORY_ITEM_ID | — | — |
| 24 | InventoryOrgId | INVENTORY_ORG_ID | — | — |
| 25 | LanguageCd | LANGUAGE_CD | — | — |
| 26 | LastQueueAssignDate | LAST_QUEUE_ASSIGN_DATE | — | — |
| 27 | LastReopenDate | LAST_REOPEN_DATE | — | — |
| 28 | LastResolvedDate | LAST_RESOLVED_DATE | — | ✅ |
| 29 | LastResourceAssignDate | LAST_RESOURCE_ASSIGN_DATE | — | — |
| 30 | LastTransferDate | LAST_TRANSFER_DATE | — | — |
| 31 | LastTransferredBy | LAST_TRANSFERRED_BY | — | — |
| 32 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | LastUpdatedByPartyId | LAST_UPDATED_BY_PARTY_ID | — | — |
| 36 | LoyMemberId | LOY_MEMBER_ID | — | — |
| 37 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | OpenDate | OPEN_DATE | — | — |
| 39 | OwnerTypeCd | OWNER_TYPE_CD | — | ✅ |
| 40 | PartnerAccountPartyId | PARTNER_ACCOUNT_PARTY_ID | — | — |
| 41 | PrimaryContactPartyId | PRIMARY_CONTACT_PARTY_ID | — | — |
| 42 | PrimaryContactPersonId | PRIMARY_CONTACT_PERSON_ID | — | — |
| 43 | ProblemCd | PROBLEM_CD | — | ✅ |
| 44 | ProblemDesc | PROBLEM_DESC | — | — |
| 45 | ProdGroupId | PROD_GROUP_ID | — | — |
| 46 | QueueId | QUEUE_ID | — | — |
| 47 | ReferenceObjectId | REF_OBJ_ID | — | — |
| 48 | ReferenceObjectPuid | REF_OBJ_PUID | — | — |
| 49 | ReferenceObjectType | REF_OBJ_TYPE | — | — |
| 50 | ReportedByPartyId | REPORTED_BY_PARTY_ID | — | — |
| 51 | ResolutionCd | RESOLUTION_CD | — | ✅ |
| 52 | ResolveDescription | RESOLVE_DESC | — | — |
| 53 | ResolveOutcomeCd | RESOLVE_OUTCOME_CD | — | — |
| 54 | ResolvedBy | RESOLVED_BY | — | — |
| 55 | ResolvedByPartyId | RESOLVED_BY_PARTY_ID | — | — |
| 56 | ServiceProfileId | SERVICE_PROFILE_ID | — | — |
| 57 | SeverityCd | SEVERITY_CD | — | ✅ |
| 58 | SourceCd | SOURCE_CD | — | — |
| 59 | SrCreatedBy | SR_CREATED_BY | — | — |
| 60 | SrId | SR_ID | 🔑 | ✅ |
| 61 | SrLastUpdateDate | SR_LAST_UPDATE_DATE | — | ✅ |
| 62 | SrLastUpdateLogin | SR_LAST_UPDATE_LOGIN | — | — |
| 63 | SrLastUpdatedBy | SR_LAST_UPDATED_BY | — | — |
| 64 | SrNumber | SR_NUMBER | — | ✅ |
| 65 | StatusCd | STATUS_CD | — | ✅ |
| 66 | StatusTypeCd | STATUS_TYPE_CD | — | — |
| 67 | StripeCd | STRIPE_CD | — | — |
| 68 | Title | TITLE | — | ✅ |
| 69 | TransferCount | TRANSFER_COUNT | — | — |
| 70 | TransferNote | TRANSFER_NOTE | — | — |
| 71 | TransferReasonCd | TRANSFER_REASON_CD | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
