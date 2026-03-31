---
id: DOC-OTHER-PVO-ReceivingParameterExtractPVO
doc_type: system-doc
title: "ReceivingParameterExtractPVO — PVO Cross-Module"
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
  - ReceivingParameterExtractPVO
  - receivingparameterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingParameterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receiving Parameter Extract. Acessa as tabelas: RCV_PARAMETERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RcvBiccExtractAM.ReceivingParameterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 1 | 1 | 41 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[rcv_parameters|RCV_PARAMETERS]] — 61 atributos (1 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[rcv_parameters|RCV_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdvancedPricing | ADVANCED_PRICING | — | ✅ |
| 2 | AllowRoutingOverride | ALLOW_ROUTING_OVERRIDE | — | ✅ |
| 3 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 4 | AllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 5 | BlindReceivingFlag | BLIND_RECEIVING_FLAG | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 9 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 10 | EnforceRmaLotNum | ENFORCE_RMA_LOT_NUM | — | ✅ |
| 11 | EnforceRmaSerialNum | ENFORCE_RMA_SERIAL_NUM | — | ✅ |
| 12 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 13 | GlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 14 | GlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 15 | GlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 16 | GlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 17 | GlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 18 | GlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 19 | GlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 20 | GlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 21 | GlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 22 | GlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 23 | GlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 24 | GlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 25 | GlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 26 | GlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 27 | GlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 28 | GlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 29 | GlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 30 | GlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 31 | GlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 32 | GlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 33 | GlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 34 | IncludeClosedPoReceipt | INCLUDE_CLOSED_PO_RECEIPT | — | ✅ |
| 35 | InspectionMethod | INSPECTION_METHOD | — | ✅ |
| 36 | IntfDropshipsToShipping | INTF_DROPSHIPS_TO_SHIPPING | — | ✅ |
| 37 | IntfReturnsToShipping | INTF_RETURNS_TO_SHIPPING | — | ✅ |
| 38 | IntfRmasToShipping | INTF_RMAS_TO_SHIPPING | — | ✅ |
| 39 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 40 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 41 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 43 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | MaintainSpQuantity | MAINTAIN_SP_QUANTITY | — | ✅ |
| 45 | MaintainStandardPack | MAINTAIN_STANDARD_PACK | — | ✅ |
| 46 | ManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | ✅ |
| 47 | NextReceiptNum | NEXT_RECEIPT_NUM | — | ✅ |
| 48 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 49 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 50 | PrintReceiptTraveler | PRINT_RECEIPT_TRAVELER | — | ✅ |
| 51 | ProcessAsnLinesTogether | PROCESS_ASN_LINES_TOGETHER | — | ✅ |
| 52 | PublishTxnEvents | PUBLISH_TXN_EVENTS | — | ✅ |
| 53 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 54 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 55 | ReceiptAsnExistsCode | RECEIPT_ASN_EXISTS_CODE | — | ✅ |
| 56 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 57 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 58 | RequestId | REQUEST_ID | — | ✅ |
| 59 | RmaReceiptRoutingId | RMA_RECEIPT_ROUTING_ID | — | ✅ |
| 60 | TransportationExecution | TRANSPORTATION_EXECUTION | — | ✅ |
| 61 | UserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
