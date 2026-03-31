---
id: DOC-OTHER-PVO-DebriefLinesExtractPVO
doc_type: system-doc
title: "DebriefLinesExtractPVO — PVO Cross-Module"
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
  - DebriefLinesExtractPVO
  - debrieflinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DebriefLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Debrief Lines Extract. Acessa as tabelas: RCL_DEBRIEF_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RclBiccExtractAM.DebriefLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 1 | 38 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[rcl_debrief_lines|RCL_DEBRIEF_LINES]] — 79 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[rcl_debrief_lines|RCL_DEBRIEF_LINES]]

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
| 42 | BillToPartyId | BILL_TO_PARTY_ID | — | ✅ |
| 43 | BillToPartySiteId | BILL_TO_PARTY_SITE_ID | — | ✅ |
| 44 | CreatedBy | CREATED_BY | — | ✅ |
| 45 | CreationDate | CREATION_DATE | — | ✅ |
| 46 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 47 | CustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 48 | DebriefHeaderId | DEBRIEF_HEADER_ID | — | ✅ |
| 49 | DebriefLineId | DEBRIEF_LINE_ID | 🔑 | ✅ |
| 50 | ErrorText | ERROR_TEXT | — | ✅ |
| 51 | ExpenseAmount | EXPENSE_AMOUNT | — | ✅ |
| 52 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 53 | ItemRevision | ITEM_REVISION | — | ✅ |
| 54 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 55 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 56 | LaborEndDate | LABOR_END_DATE | — | ✅ |
| 57 | LaborStartDate | LABOR_START_DATE | — | ✅ |
| 58 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 60 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 61 | LineStatusCode | LINE_STATUS_CODE | — | ✅ |
| 62 | LineType | LINE_TYPE | — | ✅ |
| 63 | LotNumber | LOT_NUMBER | — | ✅ |
| 64 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 65 | OrderLineId | ORDER_LINE_ID | — | ✅ |
| 66 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 67 | ParentInstanceId | PARENT_INSTANCE_ID | — | ✅ |
| 68 | PartyId | PARTY_ID | — | ✅ |
| 69 | Quantity | QUANTITY | — | ✅ |
| 70 | ReasonCode | REASON_CODE | — | ✅ |
| 71 | RequestId | REQUEST_ID | — | ✅ |
| 72 | ReservationId | RESERVATION_ID | — | ✅ |
| 73 | SerialNumber | SERIAL_NUMBER | — | ✅ |
| 74 | ServiceActivityId | SERVICE_ACTIVITY_ID | — | ✅ |
| 75 | SourceId | SOURCE_ID | — | ✅ |
| 76 | SourceType | SOURCE_TYPE | — | ✅ |
| 77 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 78 | UomCode | UOM_CODE | — | ✅ |
| 79 | UseCommonInventoryFlag | USE_COMMON_INVENTORY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
