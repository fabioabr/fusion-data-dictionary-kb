---
id: DOC-OTHER-PVO-PartsReqHeadersExtractPVO
doc_type: system-doc
title: "PartsReqHeadersExtractPVO — PVO Cross-Module"
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
  - PartsReqHeadersExtractPVO
  - partsreqheadersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsReqHeadersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Req Headers Extract. Acessa as tabelas: RCL_PARTS_REQ_HEADERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RclBiccExtractAM.PartsReqHeadersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 23 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[rcl_parts_req_headers|RCL_PARTS_REQ_HEADERS]] — 64 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[rcl_parts_req_headers|RCL_PARTS_REQ_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | BillToCustAccountId | BILL_TO_CUST_ACCOUNT_ID | — | ✅ |
| 43 | BillToPartyId | BILL_TO_PARTY_ID | — | ✅ |
| 44 | BillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | ✅ |
| 45 | BuOrgId | BU_ORG_ID | — | ✅ |
| 46 | CreatedBy | CREATED_BY | — | ✅ |
| 47 | CreationDate | CREATION_DATE | — | ✅ |
| 48 | DestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 49 | DestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 53 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | ParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 56 | ParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 57 | ParentEntityNumber | PARENT_ENTITY_NUMBER | — | ✅ |
| 58 | PurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 59 | RequirementHeaderId | REQUIREMENT_HEADER_ID | 🔑 | ✅ |
| 60 | ShipToAddressType | SHIP_TO_ADDRESS_TYPE | — | ✅ |
| 61 | ShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 62 | ShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 63 | SoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 64 | TechnicianPartyId | TECHNICIAN_PARTY_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
