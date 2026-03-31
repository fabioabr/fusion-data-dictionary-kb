---
id: DOC-OTHER-PVO-TransactionBatchSourceExtractPVO
doc_type: system-doc
title: "TransactionBatchSourceExtractPVO — PVO Cross-Module"
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
  - TransactionBatchSourceExtractPVO
  - transactionbatchsourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionBatchSourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Batch Source Extract. Acessa as tabelas: RA_BATCH_SOURCES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransactionBatchSourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 111 | 1 | 1 | 64 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 111 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaBatchSourceAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | ✅ |
| 2 | RaBatchSourceAccountingRuleRule | ACCOUNTING_RULE_RULE | — | ✅ |
| 3 | RaBatchSourceAgreementRule | AGREEMENT_RULE | — | ✅ |
| 4 | RaBatchSourceAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | ✅ |
| 5 | RaBatchSourceAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | ✅ |
| 6 | RaBatchSourceAttribute1 | ATTRIBUTE1 | — | — |
| 7 | RaBatchSourceAttribute10 | ATTRIBUTE10 | — | — |
| 8 | RaBatchSourceAttribute11 | ATTRIBUTE11 | — | — |
| 9 | RaBatchSourceAttribute12 | ATTRIBUTE12 | — | — |
| 10 | RaBatchSourceAttribute13 | ATTRIBUTE13 | — | — |
| 11 | RaBatchSourceAttribute14 | ATTRIBUTE14 | — | — |
| 12 | RaBatchSourceAttribute15 | ATTRIBUTE15 | — | — |
| 13 | RaBatchSourceAttribute2 | ATTRIBUTE2 | — | — |
| 14 | RaBatchSourceAttribute3 | ATTRIBUTE3 | — | — |
| 15 | RaBatchSourceAttribute4 | ATTRIBUTE4 | — | — |
| 16 | RaBatchSourceAttribute5 | ATTRIBUTE5 | — | — |
| 17 | RaBatchSourceAttribute6 | ATTRIBUTE6 | — | — |
| 18 | RaBatchSourceAttribute7 | ATTRIBUTE7 | — | — |
| 19 | RaBatchSourceAttribute8 | ATTRIBUTE8 | — | — |
| 20 | RaBatchSourceAttribute9 | ATTRIBUTE9 | — | — |
| 21 | RaBatchSourceAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | RaBatchSourceAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | ✅ |
| 23 | RaBatchSourceAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | ✅ |
| 24 | RaBatchSourceBatchSourceId | BATCH_SOURCE_ID | — | ✅ |
| 25 | RaBatchSourceBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | 🔑 | ✅ |
| 26 | RaBatchSourceBatchSourceType | BATCH_SOURCE_TYPE | — | ✅ |
| 27 | RaBatchSourceBillAddressRule | BILL_ADDRESS_RULE | — | ✅ |
| 28 | RaBatchSourceBillContactRule | BILL_CONTACT_RULE | — | ✅ |
| 29 | RaBatchSourceBillCustomerRule | BILL_CUSTOMER_RULE | — | ✅ |
| 30 | RaBatchSourceCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | ✅ |
| 31 | RaBatchSourceControlTrxCompletionFlag | CONTROL_TRX_COMPLETION_FLAG | — | ✅ |
| 32 | RaBatchSourceCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | ✅ |
| 33 | RaBatchSourceCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | ✅ |
| 34 | RaBatchSourceCreateClearingFlag | CREATE_CLEARING_FLAG | — | ✅ |
| 35 | RaBatchSourceCreatedBy | CREATED_BY | — | ✅ |
| 36 | RaBatchSourceCreationDate | CREATION_DATE | — | ✅ |
| 37 | RaBatchSourceCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | ✅ |
| 38 | RaBatchSourceCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | ✅ |
| 39 | RaBatchSourceCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | ✅ |
| 40 | RaBatchSourceDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | ✅ |
| 41 | RaBatchSourceDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | ✅ |
| 42 | RaBatchSourceDefaultReference | DEFAULT_REFERENCE | — | ✅ |
| 43 | RaBatchSourceDeriveDateFlag | DERIVE_DATE_FLAG | — | ✅ |
| 44 | RaBatchSourceDescription | DESCRIPTION | — | ✅ |
| 45 | RaBatchSourceEndDate | END_DATE | — | ✅ |
| 46 | RaBatchSourceFobPointRule | FOB_POINT_RULE | — | ✅ |
| 47 | RaBatchSourceGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | ✅ |
| 48 | RaBatchSourceGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 49 | RaBatchSourceGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 50 | RaBatchSourceGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 51 | RaBatchSourceGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 52 | RaBatchSourceGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 53 | RaBatchSourceGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 54 | RaBatchSourceGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 55 | RaBatchSourceGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 56 | RaBatchSourceGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 57 | RaBatchSourceGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 58 | RaBatchSourceGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 59 | RaBatchSourceGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 60 | RaBatchSourceGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 61 | RaBatchSourceGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 62 | RaBatchSourceGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 63 | RaBatchSourceGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 64 | RaBatchSourceGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 65 | RaBatchSourceGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 66 | RaBatchSourceGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 67 | RaBatchSourceGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 68 | RaBatchSourceGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 69 | RaBatchSourceGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 70 | RaBatchSourceGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 71 | RaBatchSourceGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 72 | RaBatchSourceGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 73 | RaBatchSourceGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 74 | RaBatchSourceGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 75 | RaBatchSourceGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 76 | RaBatchSourceGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 77 | RaBatchSourceGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 78 | RaBatchSourceGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 79 | RaBatchSourceGroupingRuleId | GROUPING_RULE_ID | — | ✅ |
| 80 | RaBatchSourceInvalidLinesRule | INVALID_LINES_RULE | — | ✅ |
| 81 | RaBatchSourceInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | ✅ |
| 82 | RaBatchSourceInventoryItemRule | INVENTORY_ITEM_RULE | — | ✅ |
| 83 | RaBatchSourceInvoicingRuleRule | INVOICING_RULE_RULE | — | ✅ |
| 84 | RaBatchSourceLastBatchNum | LAST_BATCH_NUM | — | ✅ |
| 85 | RaBatchSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 86 | RaBatchSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 87 | RaBatchSourceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 88 | RaBatchSourceLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 89 | RaBatchSourceMemoLineRule | MEMO_LINE_RULE | — | ✅ |
| 90 | RaBatchSourceMemoReasonRule | MEMO_REASON_RULE | — | ✅ |
| 91 | RaBatchSourceName | NAME | — | ✅ |
| 92 | RaBatchSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 93 | RaBatchSourceReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | ✅ |
| 94 | RaBatchSourceReceiptMethodRule | RECEIPT_METHOD_RULE | — | ✅ |
| 95 | RaBatchSourceRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | ✅ |
| 96 | RaBatchSourceRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | ✅ |
| 97 | RaBatchSourceSalesCreditRule | SALES_CREDIT_RULE | — | ✅ |
| 98 | RaBatchSourceSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | ✅ |
| 99 | RaBatchSourceSalesTerritoryRule | SALES_TERRITORY_RULE | — | ✅ |
| 100 | RaBatchSourceSalespersonRule | SALESPERSON_RULE | — | ✅ |
| 101 | RaBatchSourceSetId | SET_ID | — | ✅ |
| 102 | RaBatchSourceShipAddressRule | SHIP_ADDRESS_RULE | — | ✅ |
| 103 | RaBatchSourceShipContactRule | SHIP_CONTACT_RULE | — | ✅ |
| 104 | RaBatchSourceShipCustomerRule | SHIP_CUSTOMER_RULE | — | ✅ |
| 105 | RaBatchSourceShipViaRule | SHIP_VIA_RULE | — | ✅ |
| 106 | RaBatchSourceSoldCustomerRule | SOLD_CUSTOMER_RULE | — | ✅ |
| 107 | RaBatchSourceStartDate | START_DATE | — | ✅ |
| 108 | RaBatchSourceStatus | STATUS | — | ✅ |
| 109 | RaBatchSourceTermRule | TERM_RULE | — | ✅ |
| 110 | RaBatchSourceUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | ✅ |
| 111 | RaBatchSourceUsageCategoryCode | USAGE_CATEGORY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
