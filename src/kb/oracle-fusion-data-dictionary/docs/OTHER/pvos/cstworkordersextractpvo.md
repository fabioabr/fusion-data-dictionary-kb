---
id: DOC-OTHER-PVO-CstWorkOrdersExtractPVO
doc_type: system-doc
title: "CstWorkOrdersExtractPVO — PVO Cross-Module"
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
  - CstWorkOrdersExtractPVO
  - cstworkordersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWorkOrdersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Work Orders Extract. Acessa as tabelas: CST_WORK_ORDERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWorkOrdersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 1 | 1 | 26 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[cst_work_orders|CST_WORK_ORDERS]] — 58 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[cst_work_orders|CST_WORK_ORDERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrdersPEOClosedDate | CLOSED_DATE | — | ✅ |
| 2 | CstWorkOrdersPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 3 | CstWorkOrdersPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | ✅ |
| 4 | CstWorkOrdersPEOContractMfgPoLineLocId | CONTRACT_MFG_PO_LINE_LOC_ID | — | ✅ |
| 5 | CstWorkOrdersPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 6 | CstWorkOrdersPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstWorkOrdersPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstWorkOrdersPEOCstWorkOrderId | CST_WORK_ORDER_ID | 🔑 | ✅ |
| 9 | CstWorkOrdersPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 10 | CstWorkOrdersPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 11 | CstWorkOrdersPEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 12 | CstWorkOrdersPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 13 | CstWorkOrdersPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 14 | CstWorkOrdersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | CstWorkOrdersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | CstWorkOrdersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | CstWorkOrdersPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 18 | CstWorkOrdersPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 19 | CstWorkOrdersPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 20 | CstWorkOrdersPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 21 | CstWorkOrdersPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 22 | CstWorkOrdersPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 23 | CstWorkOrdersPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 24 | CstWorkOrdersPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 25 | CstWorkOrdersPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 26 | CstWorkOrdersPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 27 | CstWorkOrdersPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 28 | CstWorkOrdersPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 29 | CstWorkOrdersPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 30 | CstWorkOrdersPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 31 | CstWorkOrdersPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 32 | CstWorkOrdersPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 33 | CstWorkOrdersPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 34 | CstWorkOrdersPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 35 | CstWorkOrdersPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 36 | CstWorkOrdersPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 37 | CstWorkOrdersPEOPjcTaskId | PJC_TASK_ID | — | — |
| 38 | CstWorkOrdersPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 39 | CstWorkOrdersPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 40 | CstWorkOrdersPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 41 | CstWorkOrdersPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 42 | CstWorkOrdersPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 43 | CstWorkOrdersPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 44 | CstWorkOrdersPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 45 | CstWorkOrdersPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 46 | CstWorkOrdersPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 47 | CstWorkOrdersPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 48 | CstWorkOrdersPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 49 | CstWorkOrdersPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 50 | CstWorkOrdersPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 51 | CstWorkOrdersPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 52 | CstWorkOrdersPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 53 | CstWorkOrdersPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 54 | CstWorkOrdersPEOWorkOrderLessFlag | WORK_ORDER_LESS_FLAG | — | ✅ |
| 55 | CstWorkOrdersPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 56 | CstWorkOrdersPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 57 | CstWorkOrdersPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 58 | CstWorkOrdersPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
