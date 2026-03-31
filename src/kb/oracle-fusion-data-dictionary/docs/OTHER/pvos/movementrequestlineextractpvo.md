---
id: DOC-OTHER-PVO-MovementRequestLineExtractPVO
doc_type: system-doc
title: "MovementRequestLineExtractPVO — PVO Cross-Module"
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
  - MovementRequestLineExtractPVO
  - movementrequestlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MovementRequestLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Movement Request Line Extract. Acessa as tabelas: INV_TXN_REQUEST_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.MovementRequestLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 158 | 1 | 1 | 68 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[inv_txn_request_lines|INV_TXN_REQUEST_LINES]] — 158 atributos (1 PKs, 68 BICC)

---

## ⚙️ Atributos

### [[inv_txn_request_lines|INV_TXN_REQUEST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MRLinePEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | MRLinePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | MRLinePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | MRLinePEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | MRLinePEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | MRLinePEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | MRLinePEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | MRLinePEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | MRLinePEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | MRLinePEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | MRLinePEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | MRLinePEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | MRLinePEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | MRLinePEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | MRLinePEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | MRLinePEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | MRLinePEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | MRLinePEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | MRLinePEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | MRLinePEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | MRLinePEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | MRLinePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | MRLinePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | MRLinePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | MRLinePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | MRLinePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | MRLinePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | MRLinePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | MRLinePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 30 | MRLinePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | MRLinePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | MRLinePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | MRLinePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | MRLinePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 35 | MRLinePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 36 | MRLinePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 37 | MRLinePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 38 | MRLinePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 39 | MRLinePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 40 | MRLinePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 41 | MRLinePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 42 | MRLinePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 43 | MRLinePEOBackorderDeliveryDetailId | BACKORDER_DELIVERY_DETAIL_ID | — | ✅ |
| 44 | MRLinePEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 45 | MRLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | MRLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | MRLinePEODateRequired | DATE_REQUIRED | — | ✅ |
| 48 | MRLinePEOFromLocatorId | FROM_LOCATOR_ID | — | ✅ |
| 49 | MRLinePEOFromSubinventoryCode | FROM_SUBINVENTORY_CODE | — | ✅ |
| 50 | MRLinePEOFromSubinventoryId | FROM_SUBINVENTORY_ID | — | ✅ |
| 51 | MRLinePEOGradeCode | GRADE_CODE | — | ✅ |
| 52 | MRLinePEOHeaderId | HEADER_ID | — | ✅ |
| 53 | MRLinePEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 54 | MRLinePEOInvReservedAttribute1 | INV_RESERVED_ATTRIBUTE1 | — | — |
| 55 | MRLinePEOInvReservedAttribute2 | INV_RESERVED_ATTRIBUTE2 | — | — |
| 56 | MRLinePEOInvStripingCategory | INV_STRIPING_CATEGORY | — | — |
| 57 | MRLinePEOInvUserDefAttribute1 | INV_USER_DEF_ATTRIBUTE1 | — | — |
| 58 | MRLinePEOInvUserDefAttribute10 | INV_USER_DEF_ATTRIBUTE10 | — | — |
| 59 | MRLinePEOInvUserDefAttribute2 | INV_USER_DEF_ATTRIBUTE2 | — | — |
| 60 | MRLinePEOInvUserDefAttribute3 | INV_USER_DEF_ATTRIBUTE3 | — | — |
| 61 | MRLinePEOInvUserDefAttribute4 | INV_USER_DEF_ATTRIBUTE4 | — | — |
| 62 | MRLinePEOInvUserDefAttribute5 | INV_USER_DEF_ATTRIBUTE5 | — | — |
| 63 | MRLinePEOInvUserDefAttribute6 | INV_USER_DEF_ATTRIBUTE6 | — | — |
| 64 | MRLinePEOInvUserDefAttribute7 | INV_USER_DEF_ATTRIBUTE7 | — | — |
| 65 | MRLinePEOInvUserDefAttribute8 | INV_USER_DEF_ATTRIBUTE8 | — | — |
| 66 | MRLinePEOInvUserDefAttribute9 | INV_USER_DEF_ATTRIBUTE9 | — | — |
| 67 | MRLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 68 | MRLinePEOJOBDEFINITIONNAME | JOB_DEFINITION_NAME | — | ✅ |
| 69 | MRLinePEOJOBDEFINITIONPACKAGE | JOB_DEFINITION_PACKAGE | — | ✅ |
| 70 | MRLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 71 | MRLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 72 | MRLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 73 | MRLinePEOLineId | LINE_ID | 🔑 | ✅ |
| 74 | MRLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 75 | MRLinePEOLineStatus | LINE_STATUS | — | ✅ |
| 76 | MRLinePEOLotNumber | LOT_NUMBER | — | ✅ |
| 77 | MRLinePEOLpnId | LPN_ID | — | ✅ |
| 78 | MRLinePEOModelQuantity | MODEL_QUANTITY | — | ✅ |
| 79 | MRLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 80 | MRLinePEOOperationSeqNum | OPERATION_SEQ_NUM | — | ✅ |
| 81 | MRLinePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 82 | MRLinePEOPickMethodologyId | PICK_METHODOLOGY_ID | — | ✅ |
| 83 | MRLinePEOPickSlipDate | PICK_SLIP_DATE | — | ✅ |
| 84 | MRLinePEOPickSlipNumber | PICK_SLIP_NUMBER | — | ✅ |
| 85 | MRLinePEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 86 | MRLinePEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 87 | MRLinePEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 88 | MRLinePEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 89 | MRLinePEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 90 | MRLinePEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 91 | MRLinePEOPjcExpenditureOrgId | PJC_EXPENDITURE_ORG_ID | — | — |
| 92 | MRLinePEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 93 | MRLinePEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 94 | MRLinePEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 95 | MRLinePEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 96 | MRLinePEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 97 | MRLinePEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 98 | MRLinePEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 99 | MRLinePEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 100 | MRLinePEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 101 | MRLinePEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 102 | MRLinePEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 103 | MRLinePEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 104 | MRLinePEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 105 | MRLinePEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 106 | MRLinePEOPjcTaskId | PJC_TASK_ID | — | — |
| 107 | MRLinePEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 108 | MRLinePEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 109 | MRLinePEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 110 | MRLinePEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 111 | MRLinePEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 112 | MRLinePEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 113 | MRLinePEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 114 | MRLinePEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 115 | MRLinePEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 116 | MRLinePEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 117 | MRLinePEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 118 | MRLinePEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 119 | MRLinePEOProjectId | PROJECT_ID | — | — |
| 120 | MRLinePEOQuantity | QUANTITY | — | ✅ |
| 121 | MRLinePEOQuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 122 | MRLinePEOQuantityDetailed | QUANTITY_DETAILED | — | ✅ |
| 123 | MRLinePEOReasonId | REASON_ID | — | ✅ |
| 124 | MRLinePEOReferenceDetailId | REFERENCE_DETAIL_ID | — | ✅ |
| 125 | MRLinePEOReferenceId | REFERENCE_ID | — | ✅ |
| 126 | MRLinePEOReferenceName | REFERENCE_NAME | — | ✅ |
| 127 | MRLinePEOReferenceTypeCode | REFERENCE_TYPE_CODE | — | ✅ |
| 128 | MRLinePEORequestId | REQUEST_ID | — | ✅ |
| 129 | MRLinePEORequesterId | REQUESTER_ID | — | ✅ |
| 130 | MRLinePEORequiredQuantity | REQUIRED_QUANTITY | — | ✅ |
| 131 | MRLinePEORevision | REVISION | — | ✅ |
| 132 | MRLinePEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 133 | MRLinePEOSecondaryQuantityDelivered | SECONDARY_QUANTITY_DELIVERED | — | ✅ |
| 134 | MRLinePEOSecondaryQuantityDetailed | SECONDARY_QUANTITY_DETAILED | — | ✅ |
| 135 | MRLinePEOSecondaryRequiredQuantity | SECONDARY_REQUIRED_QUANTITY | — | ✅ |
| 136 | MRLinePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 137 | MRLinePEOSerialNumberEnd | SERIAL_NUMBER_END | — | ✅ |
| 138 | MRLinePEOSerialNumberStart | SERIAL_NUMBER_START | — | ✅ |
| 139 | MRLinePEOShipModelId | SHIP_MODEL_ID | — | ✅ |
| 140 | MRLinePEOShipSetId | SHIP_SET_ID | — | ✅ |
| 141 | MRLinePEOShipSetName | SHIP_SET_NAME | — | ✅ |
| 142 | MRLinePEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 143 | MRLinePEOStatusDate | STATUS_DATE | — | ✅ |
| 144 | MRLinePEOTaskId | TASK_ID | — | — |
| 145 | MRLinePEOToAccountId | TO_ACCOUNT_ID | — | ✅ |
| 146 | MRLinePEOToLocatorId | TO_LOCATOR_ID | — | ✅ |
| 147 | MRLinePEOToOrganizationId | TO_ORGANIZATION_ID | — | ✅ |
| 148 | MRLinePEOToSubinventoryCode | TO_SUBINVENTORY_CODE | — | ✅ |
| 149 | MRLinePEOToSubinventoryId | TO_SUBINVENTORY_ID | — | ✅ |
| 150 | MRLinePEOTransactionHeaderId | TRANSACTION_HEADER_ID | — | ✅ |
| 151 | MRLinePEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | ✅ |
| 152 | MRLinePEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 153 | MRLinePEOTxnSourceId | TXN_SOURCE_ID | — | ✅ |
| 154 | MRLinePEOTxnSourceLineDetailId | TXN_SOURCE_LINE_DETAIL_ID | — | ✅ |
| 155 | MRLinePEOTxnSourceLineId | TXN_SOURCE_LINE_ID | — | ✅ |
| 156 | MRLinePEOUomCode | UOM_CODE | — | ✅ |
| 157 | MRLinePEOWipEntityId | WIP_ENTITY_ID | — | ✅ |
| 158 | MRLinePEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
