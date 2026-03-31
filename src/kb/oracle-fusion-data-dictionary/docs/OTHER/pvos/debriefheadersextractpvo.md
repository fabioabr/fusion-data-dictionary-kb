---
id: DOC-OTHER-PVO-DebriefHeadersExtractPVO
doc_type: system-doc
title: "DebriefHeadersExtractPVO — PVO Cross-Module"
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
  - DebriefHeadersExtractPVO
  - debriefheadersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DebriefHeadersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Debrief Headers Extract. Acessa as tabelas: RCL_DEBRIEF_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RclBiccExtractAM.DebriefHeadersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 1 | 1 | 64 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[rcl_debrief_headers|RCL_DEBRIEF_HEADERS]] — 105 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[rcl_debrief_headers|RCL_DEBRIEF_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 6 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 7 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 8 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 9 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 10 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 11 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 12 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 13 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 14 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 15 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 16 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 17 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 18 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 19 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 20 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 21 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 22 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | BillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | ✅ |
| 44 | BuOrgId | BU_ORG_ID | — | ✅ |
| 45 | CostOrganizationId | COST_ORGANIZATION_ID | — | ✅ |
| 46 | CreatedBy | CREATED_BY | — | ✅ |
| 47 | CreationDate | CREATION_DATE | — | ✅ |
| 48 | CustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 49 | DebriefHeaderId | DEBRIEF_HEADER_ID | 🔑 | ✅ |
| 50 | DebriefNumber | DEBRIEF_NUMBER | — | ✅ |
| 51 | DebriefStatusCode | DEBRIEF_STATUS_CODE | — | ✅ |
| 52 | EstimateStatus | ESTIMATE_STATUS | — | ✅ |
| 53 | FreezePriceFlag | FREEZE_PRICE_FLAG | — | ✅ |
| 54 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 55 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 56 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 58 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 59 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 60 | ParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 61 | ParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 62 | ParentEntityName | PARENT_ENTITY_NAME | — | ✅ |
| 63 | PartyId | PARTY_ID | — | ✅ |
| 64 | PjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 65 | PjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 66 | PjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 67 | PjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 68 | PjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 69 | PjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 70 | PjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 71 | PjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 72 | PjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 73 | PjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 74 | PjcProjectNumber | PJC_PROJECT_NUMBER | — | ✅ |
| 75 | PjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 76 | PjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 77 | PjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 78 | PjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 79 | PjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 80 | PjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 81 | PjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 82 | PjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 83 | PjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 84 | PjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 85 | PjcTaskId | PJC_TASK_ID | — | ✅ |
| 86 | PjcTaskNumber | PJC_TASK_NUMBER | — | ✅ |
| 87 | PjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 88 | PjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 89 | PjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 90 | PjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 91 | PjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 92 | PjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 93 | PjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 94 | PjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 95 | PjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 96 | PjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 97 | PjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 98 | ProductItemId | PRODUCT_ITEM_ID | — | ✅ |
| 99 | ProductSerialNumber | PRODUCT_SERIAL_NUMBER | — | ✅ |
| 100 | PurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 101 | RequestId | REQUEST_ID | — | ✅ |
| 102 | ShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 103 | TechnicianPartyId | TECHNICIAN_PARTY_ID | — | ✅ |
| 104 | WieWoId | WIE_WO_ID | — | ✅ |
| 105 | WorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
