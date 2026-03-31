---
id: DOC-OTHER-PVO-MovementRequestHeaderExtractPVO
doc_type: system-doc
title: "MovementRequestHeaderExtractPVO — PVO Cross-Module"
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
  - MovementRequestHeaderExtractPVO
  - movementrequestheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MovementRequestHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Movement Request Header Extract. Acessa as tabelas: INV_TXN_REQUEST_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.MovementRequestHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 1 | 1 | 28 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[inv_txn_request_headers|INV_TXN_REQUEST_HEADERS]] — 69 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[inv_txn_request_headers|INV_TXN_REQUEST_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MRHeaderPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | MRHeaderPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | MRHeaderPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | MRHeaderPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | MRHeaderPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | MRHeaderPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | MRHeaderPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | MRHeaderPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | MRHeaderPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | MRHeaderPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | MRHeaderPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | MRHeaderPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | MRHeaderPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | MRHeaderPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | MRHeaderPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | MRHeaderPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | MRHeaderPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | MRHeaderPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | MRHeaderPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | MRHeaderPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | MRHeaderPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | MRHeaderPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | MRHeaderPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | MRHeaderPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | MRHeaderPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | MRHeaderPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | MRHeaderPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | MRHeaderPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | MRHeaderPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | MRHeaderPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | MRHeaderPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | MRHeaderPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | MRHeaderPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | MRHeaderPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | MRHeaderPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | MRHeaderPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | MRHeaderPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | MRHeaderPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | MRHeaderPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | MRHeaderPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | MRHeaderPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | MRHeaderPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | MRHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 44 | MRHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 45 | MRHeaderPEODateRequired | DATE_REQUIRED | — | ✅ |
| 46 | MRHeaderPEODescription | DESCRIPTION | — | ✅ |
| 47 | MRHeaderPEOFreightCode | FREIGHT_CODE | — | ✅ |
| 48 | MRHeaderPEOFromSubinventoryCode | FROM_SUBINVENTORY_CODE | — | ✅ |
| 49 | MRHeaderPEOGroupingRuleId | GROUPING_RULE_ID | — | ✅ |
| 50 | MRHeaderPEOHeaderId | HEADER_ID | 🔑 | ✅ |
| 51 | MRHeaderPEOHeaderStatus | HEADER_STATUS | — | ✅ |
| 52 | MRHeaderPEOJOBDEFINITIONNAME | JOB_DEFINITION_NAME | — | ✅ |
| 53 | MRHeaderPEOJOBDEFINITIONPACKAGE | JOB_DEFINITION_PACKAGE | — | ✅ |
| 54 | MRHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | MRHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | MRHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | MRHeaderPEOMOVEORDERTYPE | MOVE_ORDER_TYPE | — | ✅ |
| 58 | MRHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 59 | MRHeaderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 60 | MRHeaderPEOReferenceDetailId | REFERENCE_DETAIL_ID | — | ✅ |
| 61 | MRHeaderPEOReferenceId | REFERENCE_ID | — | ✅ |
| 62 | MRHeaderPEORequestId | REQUEST_ID | — | ✅ |
| 63 | MRHeaderPEORequestNumber | REQUEST_NUMBER | — | ✅ |
| 64 | MRHeaderPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 65 | MRHeaderPEOShipmentMethod | SHIPMENT_METHOD | — | ✅ |
| 66 | MRHeaderPEOStatusDate | STATUS_DATE | — | ✅ |
| 67 | MRHeaderPEOToAccountId | TO_ACCOUNT_ID | — | ✅ |
| 68 | MRHeaderPEOToSubinventoryCode | TO_SUBINVENTORY_CODE | — | ✅ |
| 69 | MRHeaderPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
