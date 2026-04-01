---
id: DOC-OTHER-PVO-HoldWHInstance
doc_type: system-doc
title: "HoldWHInstance — PVO Cross-Module"
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
  - HoldWHInstance
  - holdwhinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldWHInstance

## 📌 Visão Geral

View Object para extração BICC de dados de Hold WHInstance. Acessa as tabelas: DOO_HEADERS_ALL, DOO_HOLD_INSTANCES.

**Caminho:** `FscmTopModelAM.DooTopAM.HoldWHInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 2 | 1 | 21 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 35 atributos (8 BICC)
- [[doo_hold_instances|DOO_HOLD_INSTANCES]] — 27 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 2 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 3 | HeaderConversionDate | CONVERSION_DATE | — | ✅ |
| 4 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 5 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 6 | HeaderCreatedBy | CREATED_BY | — | — |
| 7 | HeaderCreationDate | CREATION_DATE | — | ✅ |
| 8 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 9 | HeaderHeaderId | HEADER_ID | — | — |
| 10 | HeaderIsEditable | IS_EDITABLE | — | — |
| 11 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | HeaderOnHold | ON_HOLD | — | — |
| 17 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 18 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 19 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 20 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 21 | HeaderOrgId | ORG_ID | — | ✅ |
| 22 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 23 | HeaderOwnerId | OWNER_ID | — | — |
| 24 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 25 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 26 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | ✅ |
| 27 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | ✅ |
| 28 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 29 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 30 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 31 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 32 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 33 | HeaderSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 34 | HeaderStatusCode | STATUS_CODE | — | — |
| 35 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_hold_instances|DOO_HOLD_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldInstanceActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | HoldInstanceApplyDate | APPLY_DATE | — | ✅ |
| 3 | HoldInstanceApplySystem | APPLY_SYSTEM | — | — |
| 4 | HoldInstanceApplyUserId | APPLY_USER_ID | — | — |
| 5 | HoldInstanceCreatedBy | CREATED_BY | — | ✅ |
| 6 | HoldInstanceCreationDate | CREATION_DATE | — | ✅ |
| 7 | HoldInstanceDeletedFlag | DELETED_FLAG | — | — |
| 8 | HoldInstanceHoldCodeId | HOLD_CODE_ID | — | ✅ |
| 9 | HoldInstanceHoldComments | HOLD_COMMENTS | — | — |
| 10 | HoldInstanceHoldReleaseComments | HOLD_RELEASE_COMMENTS | — | — |
| 11 | HoldInstanceHoldRunningTaskFlag | HOLD_RUNNING_TASK_FLAG | — | — |
| 12 | HoldInstanceId | HOLD_INSTANCE_ID | 🔑 | ✅ |
| 13 | HoldInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | HoldInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | HoldInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | HoldInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | HoldInstanceOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 18 | HoldInstancePendingFlag | PENDING_FLAG | — | ✅ |
| 19 | HoldInstanceReleaseDate | RELEASE_DATE | — | ✅ |
| 20 | HoldInstanceReleaseUserId | RELEASE_USER_ID | — | — |
| 21 | HoldInstanceSourceLineId | SOURCE_LINE_ID | — | — |
| 22 | HoldInstanceSourceOrderId | SOURCE_ORDER_ID | — | — |
| 23 | HoldInstanceSourceOrderRevision | SOURCE_ORDER_REVISION | — | — |
| 24 | HoldInstanceSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 25 | HoldInstanceSourceRequestId | SOURCE_REQUEST_ID | — | — |
| 26 | HoldInstanceTransactionEntityId1 | TRANSACTION_ENTITY_ID1 | — | ✅ |
| 27 | HoldInstanceTransactionEntityName1 | TRANSACTION_ENTITY_NAME1 | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
