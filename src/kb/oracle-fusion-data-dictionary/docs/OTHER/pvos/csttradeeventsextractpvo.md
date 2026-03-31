---
id: DOC-OTHER-PVO-CstTradeEventsExtractPVO
doc_type: system-doc
title: "CstTradeEventsExtractPVO — PVO Cross-Module"
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
  - CstTradeEventsExtractPVO
  - csttradeeventsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTradeEventsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Trade Events Extract. Acessa as tabelas: CST_TRADE_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTradeEventsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 138 | 1 | 1 | 106 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[cst_trade_events|CST_TRADE_EVENTS]] — 138 atributos (1 PKs, 106 BICC)

---

## ⚙️ Atributos

### [[cst_trade_events|CST_TRADE_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTradeEventsPEOAccrualTradeEventId | ACCRUAL_TRADE_EVENT_ID | — | ✅ |
| 2 | CstTradeEventsPEOAccrualTransactionId | ACCRUAL_TRANSACTION_ID | — | ✅ |
| 3 | CstTradeEventsPEOAgreementHeaderId | AGREEMENT_HEADER_ID | — | ✅ |
| 4 | CstTradeEventsPEOAgreementNumber | AGREEMENT_NUMBER | — | ✅ |
| 5 | CstTradeEventsPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 6 | CstTradeEventsPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 7 | CstTradeEventsPEOBillToBuId | BILL_TO_BU_ID | — | ✅ |
| 8 | CstTradeEventsPEOBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 9 | CstTradeEventsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 10 | CstTradeEventsPEOCallbackStatus | CALLBACK_STATUS | — | ✅ |
| 11 | CstTradeEventsPEOCmrTransactionTypeCode | CMR_TRANSACTION_TYPE_CODE | — | ✅ |
| 12 | CstTradeEventsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 13 | CstTradeEventsPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 14 | CstTradeEventsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 15 | CstTradeEventsPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | CstTradeEventsPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | CstTradeEventsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 18 | CstTradeEventsPEOCustodyInventoryOrgId | CUSTODY_INVENTORY_ORG_ID | — | ✅ |
| 19 | CstTradeEventsPEODefaultTaxCountry | DEFAULT_TAX_COUNTRY | — | ✅ |
| 20 | CstTradeEventsPEODocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 21 | CstTradeEventsPEODooFullfillLineId | DOO_FULLFILL_LINE_ID | — | ✅ |
| 22 | CstTradeEventsPEODooSplitFulfillLineId | DOO_SPLIT_FULFILL_LINE_ID | — | ✅ |
| 23 | CstTradeEventsPEOErrorCode | ERROR_CODE | — | ✅ |
| 24 | CstTradeEventsPEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | ✅ |
| 25 | CstTradeEventsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 26 | CstTradeEventsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 27 | CstTradeEventsPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 28 | CstTradeEventsPEOFtrId | FTR_ID | — | ✅ |
| 29 | CstTradeEventsPEOIntendUseClassifId | INTEND_USE_CLASSIF_ID | — | ✅ |
| 30 | CstTradeEventsPEOIntercompanyInvoicingFlag | INTERCOMPANY_INVOICING_FLAG | — | ✅ |
| 31 | CstTradeEventsPEOInvStripingCategory | INV_STRIPING_CATEGORY | — | ✅ |
| 32 | CstTradeEventsPEOInvTransactionId | INV_TRANSACTION_ID | — | ✅ |
| 33 | CstTradeEventsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 34 | CstTradeEventsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 35 | CstTradeEventsPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 36 | CstTradeEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | CstTradeEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | CstTradeEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | CstTradeEventsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 40 | CstTradeEventsPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 41 | CstTradeEventsPEOManualReceiptReqdFlag | MANUAL_RECEIPT_REQD_FLAG | — | ✅ |
| 42 | CstTradeEventsPEOOwnershipChangeDocNumber | OWNERSHIP_CHANGE_DOC_NUMBER | — | ✅ |
| 43 | CstTradeEventsPEOOwnershipChangeDocType | OWNERSHIP_CHANGE_DOC_TYPE | — | ✅ |
| 44 | CstTradeEventsPEOOwnershipChangeEventType | OWNERSHIP_CHANGE_EVENT_TYPE | — | ✅ |
| 45 | CstTradeEventsPEOOwnershipChangeSystemRef | OWNERSHIP_CHANGE_SYSTEM_REF | — | ✅ |
| 46 | CstTradeEventsPEOOwnershipChangeTxnId | OWNERSHIP_CHANGE_TXN_ID | — | ✅ |
| 47 | CstTradeEventsPEOParentOwnerChangeEventType | PARENT_OWNER_CHANGE_EVENT_TYPE | — | ✅ |
| 48 | CstTradeEventsPEOParentOwnerChangeSystemRef | PARENT_OWNER_CHANGE_SYSTEM_REF | — | ✅ |
| 49 | CstTradeEventsPEOParentOwnershipChangeTxnId | PARENT_OWNERSHIP_CHANGE_TXN_ID | — | ✅ |
| 50 | CstTradeEventsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 51 | CstTradeEventsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 52 | CstTradeEventsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 53 | CstTradeEventsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 54 | CstTradeEventsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 55 | CstTradeEventsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 56 | CstTradeEventsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 57 | CstTradeEventsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 58 | CstTradeEventsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 59 | CstTradeEventsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 60 | CstTradeEventsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 61 | CstTradeEventsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 62 | CstTradeEventsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 63 | CstTradeEventsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 64 | CstTradeEventsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 65 | CstTradeEventsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 66 | CstTradeEventsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 67 | CstTradeEventsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 68 | CstTradeEventsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 69 | CstTradeEventsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 70 | CstTradeEventsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 71 | CstTradeEventsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 72 | CstTradeEventsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 73 | CstTradeEventsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 74 | CstTradeEventsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 75 | CstTradeEventsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 76 | CstTradeEventsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 77 | CstTradeEventsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 78 | CstTradeEventsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 79 | CstTradeEventsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 80 | CstTradeEventsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 81 | CstTradeEventsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 82 | CstTradeEventsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 83 | CstTradeEventsPEOPricingOption | PRICING_OPTION | — | ✅ |
| 84 | CstTradeEventsPEOPrimaryQty | PRIMARY_QTY | — | ✅ |
| 85 | CstTradeEventsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 86 | CstTradeEventsPEOPriorBuId | PRIOR_BU_ID | — | ✅ |
| 87 | CstTradeEventsPEOPriorInventoryOrgId | PRIOR_INVENTORY_ORG_ID | — | ✅ |
| 88 | CstTradeEventsPEOPriorTradeEventId | PRIOR_TRADE_EVENT_ID | — | ✅ |
| 89 | CstTradeEventsPEOPriorTransactionId | PRIOR_TRANSACTION_ID | — | ✅ |
| 90 | CstTradeEventsPEOProcessByCaFlag | PROCESS_BY_CA_FLAG | — | ✅ |
| 91 | CstTradeEventsPEOProcessByRaFlag | PROCESS_BY_RA_FLAG | — | ✅ |
| 92 | CstTradeEventsPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 93 | CstTradeEventsPEOProductFiscClassif | PRODUCT_FISC_CLASSIF | — | ✅ |
| 94 | CstTradeEventsPEOProjectId | PROJECT_ID | — | ✅ |
| 95 | CstTradeEventsPEOPtrId | PTR_ID | — | ✅ |
| 96 | CstTradeEventsPEOPtrInstanceId | PTR_INSTANCE_ID | — | ✅ |
| 97 | CstTradeEventsPEOQppTxnGroupsUpdatedFlag | QPP_TXN_GROUPS_UPDATED_FLAG | — | ✅ |
| 98 | CstTradeEventsPEORcvTransactionId | RCV_TRANSACTION_ID | — | ✅ |
| 99 | CstTradeEventsPEOReturnBuId | RETURN_BU_ID | — | ✅ |
| 100 | CstTradeEventsPEOReturnInvOrgId | RETURN_INV_ORG_ID | — | ✅ |
| 101 | CstTradeEventsPEORootOwnershipChangeTxnId | ROOT_OWNERSHIP_CHANGE_TXN_ID | — | ✅ |
| 102 | CstTradeEventsPEOSecondaryTransactionQty | SECONDARY_TRANSACTION_QTY | — | ✅ |
| 103 | CstTradeEventsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 104 | CstTradeEventsPEOShippingBuId | SHIPPING_BU_ID | — | ✅ |
| 105 | CstTradeEventsPEOShippingInvOrgId | SHIPPING_INV_ORG_ID | — | ✅ |
| 106 | CstTradeEventsPEOSoNeededFlag | SO_NEEDED_FLAG | — | ✅ |
| 107 | CstTradeEventsPEOSourceDocQuantity | SOURCE_DOC_QUANTITY | — | ✅ |
| 108 | CstTradeEventsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 109 | CstTradeEventsPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 110 | CstTradeEventsPEOSuccessorBuId | SUCCESSOR_BU_ID | — | ✅ |
| 111 | CstTradeEventsPEOSuccessorInvOrgId | SUCCESSOR_INV_ORG_ID | — | ✅ |
| 112 | CstTradeEventsPEOTaskId | TASK_ID | — | ✅ |
| 113 | CstTradeEventsPEOTaxCalculatedFlag | TAX_CALCULATED_FLAG | — | ✅ |
| 114 | CstTradeEventsPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 115 | CstTradeEventsPEOTrackProfitFlag | TRACK_PROFIT_FLAG | — | ✅ |
| 116 | CstTradeEventsPEOTradeEventId | TRADE_EVENT_ID | 🔑 | ✅ |
| 117 | CstTradeEventsPEOTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 118 | CstTradeEventsPEOTransactionCreationDate | TRANSACTION_CREATION_DATE | — | ✅ |
| 119 | CstTradeEventsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 120 | CstTradeEventsPEOTransactionEventId | TRANSACTION_EVENT_ID | — | ✅ |
| 121 | CstTradeEventsPEOTransactionQty | TRANSACTION_QTY | — | ✅ |
| 122 | CstTradeEventsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 123 | CstTradeEventsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 124 | CstTradeEventsPEOTransferOrderDistId | TRANSFER_ORDER_DIST_ID | — | ✅ |
| 125 | CstTradeEventsPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 126 | CstTradeEventsPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 127 | CstTradeEventsPEOTxnAmountCurrencyCode | TXN_AMOUNT_CURRENCY_CODE | — | ✅ |
| 128 | CstTradeEventsPEOTxnDocumentSourceSystem | TXN_DOCUMENT_SOURCE_SYSTEM | — | ✅ |
| 129 | CstTradeEventsPEOTxnSourceDocLine | TXN_SOURCE_DOC_LINE | — | ✅ |
| 130 | CstTradeEventsPEOTxnSourceDocLineDetail | TXN_SOURCE_DOC_LINE_DETAIL | — | ✅ |
| 131 | CstTradeEventsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 132 | CstTradeEventsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 133 | CstTradeEventsPEOTxnSourceRefDocLine | TXN_SOURCE_REF_DOC_LINE | — | ✅ |
| 134 | CstTradeEventsPEOTxnSourceRefDocLineDetail | TXN_SOURCE_REF_DOC_LINE_DETAIL | — | ✅ |
| 135 | CstTradeEventsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 136 | CstTradeEventsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 137 | CstTradeEventsPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 138 | CstTradeEventsPEOWshDeliveryDetailId | WSH_DELIVERY_DETAIL_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
