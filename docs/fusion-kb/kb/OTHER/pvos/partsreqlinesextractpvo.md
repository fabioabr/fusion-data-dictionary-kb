---
id: DOC-OTHER-PVO-PartsReqLinesExtractPVO
doc_type: system-doc
title: "PartsReqLinesExtractPVO — PVO Cross-Module"
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
  - PartsReqLinesExtractPVO
  - partsreqlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsReqLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Req Lines Extract. Acessa as tabelas: RCL_PARTS_REQ_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RclBiccExtractAM.PartsReqLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 1 | 1 | 30 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]] — 71 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[rcl_parts_req_lines|RCL_PARTS_REQ_LINES]]

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
| 43 | BillToCustAccountId | BILL_TO_CUST_ACCOUNT_ID | — | ✅ |
| 44 | BillToPartyId | BILL_TO_PARTY_ID | — | ✅ |
| 45 | BillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | ✅ |
| 46 | CreatedBy | CREATED_BY | — | ✅ |
| 47 | CreationDate | CREATION_DATE | — | ✅ |
| 48 | DestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | ✅ |
| 49 | DestinationSubinventory | DESTINATION_SUBINVENTORY | — | ✅ |
| 50 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 51 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 55 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 56 | ParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 57 | ParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 58 | Quantity | QUANTITY | — | ✅ |
| 59 | ReqLineLinkId | REQ_LINE_LINK_ID | — | ✅ |
| 60 | RequirementHeaderId | REQUIREMENT_HEADER_ID | — | ✅ |
| 61 | RequirementLineId | REQUIREMENT_LINE_ID | 🔑 | ✅ |
| 62 | ReturnFromPartyId | RETURN_FROM_PARTY_ID | — | ✅ |
| 63 | ReturnFromPartySiteId | RETURN_FROM_PARTY_SITE_ID | — | ✅ |
| 64 | ReturnReasonCode | RETURN_REASON_CODE | — | ✅ |
| 65 | Revision | REVISION | — | ✅ |
| 66 | ServiceActivityId | SERVICE_ACTIVITY_ID | — | ✅ |
| 67 | ShipToAddressType | SHIP_TO_ADDRESS_TYPE | — | ✅ |
| 68 | ShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 69 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 70 | ShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 71 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
