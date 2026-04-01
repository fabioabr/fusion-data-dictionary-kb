---
id: DOC-OTHER-PVO-PerfObligationLinDistsPVO
doc_type: system-doc
title: "PerfObligationLinDistsPVO — PVO Cross-Module"
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
  - PerfObligationLinDistsPVO
  - perfobligationlindistspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerfObligationLinDistsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Perf Obligation Lin Dists. Acessa as tabelas: GL_LEDGERS, PER_PERSON_NAMES_F_V, PER_USERS (+11).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.PerfObligationLinDistsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 547 | 14 | 1 | 97 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos
- [[per_users|PER_USERS]] — 16 atributos
- [[vrm_accounting_events|VRM_ACCOUNTING_EVENTS]] — 55 atributos (4 BICC)
- [[vrm_billing_line_details|VRM_BILLING_LINE_DETAILS]] — 38 atributos (4 BICC)
- [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]] — 66 atributos (2 BICC)
- [[vrm_fmv_lines|VRM_FMV_LINES]] — 9 atributos
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 3 atributos
- [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]] — 100 atributos (30 BICC)
- [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]] — 105 atributos (36 BICC)
- [[vrm_perf_obligation_lin_dists|VRM_PERF_OBLIGATION_LIN_DISTS]] — 67 atributos (1 PKs, 13 BICC)
- [[vrm_pol_billing_events|VRM_POL_BILLING_EVENTS]] — 46 atributos (1 BICC)
- [[vrm_pricing_lines|VRM_PRICING_LINES]] — 11 atributos (7 BICC)
- [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]] — 5 atributos

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | GlLedgersCreatedBy | CREATED_BY | — | — |
| 3 | GlLedgersCreationDate | CREATION_DATE | — | — |
| 4 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 5 | GlLedgersName | NAME | — | — |
| 6 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHeadPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | CustContHeadPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | CustContHeadPersonCreatedByPersonId | PERSON_ID | — | — |
| 4 | CustContHeadPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | CustContHeadPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | CustContHeadPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | CustContHeadPersonUpdatedByPersonId | PERSON_ID | — | — |
| 8 | CustContHeadPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 9 | CustomerContractHeadersPEOCreatedBy | DISPLAY_NAME | — | — |
| 10 | CustomerContractHeadersPEOLastUpdatedBy | DISPLAY_NAME | — | — |
| 11 | PerfObligPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 12 | PerfObligPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | PerfObligPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | PerfObligPersonCreatedByPersonId | PERSON_ID | — | — |
| 15 | PerfObligPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | PerfObligPersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 17 | PerfObligPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | PerfObligPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | PerfObligPersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | PerfObligPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHeadUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CustContHeadUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | CustContHeadUserCreatedByUserId | USER_ID | — | — |
| 4 | CustContHeadUserCreatedByUsername | USERNAME | — | — |
| 5 | CustContHeadUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | CustContHeadUserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | CustContHeadUserUpdatedByUserId | USER_ID | — | — |
| 8 | CustContHeadUserUpdatedByUsername | USERNAME | — | — |
| 9 | PerfObligUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PerfObligUserCreatedByPersonId | PERSON_ID | — | — |
| 11 | PerfObligUserCreatedByUserId | USER_ID | — | — |
| 12 | PerfObligUserCreatedByUsername | USERNAME | — | — |
| 13 | PerfObligUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PerfObligUserUpdatedByPersonId | PERSON_ID | — | — |
| 15 | PerfObligUserUpdatedByUserId | USER_ID | — | — |
| 16 | PerfObligUserUpdatedByUsername | USERNAME | — | — |

### [[vrm_accounting_events|VRM_ACCOUNTING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationLinDistsEOAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | VrmAccountingEventsAccountingDate | ACCOUNTING_DATE | — | — |
| 3 | VrmAccountingEventsAccountingEventSeqNumber | ACCOUNTING_EVENT_SEQ_NUMBER | — | — |
| 4 | VrmAccountingEventsAccountingEventTypeCode | ACCOUNTING_EVENT_TYPE_CODE | — | — |
| 5 | VrmAccountingEventsAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 6 | VrmAccountingEventsAmount | AMOUNT | — | ✅ |
| 7 | VrmAccountingEventsAttribute102 | ATTRIBUTE10 | — | — |
| 8 | VrmAccountingEventsAttribute112 | ATTRIBUTE1 | — | — |
| 9 | VrmAccountingEventsAttribute113 | ATTRIBUTE11 | — | — |
| 10 | VrmAccountingEventsAttribute122 | ATTRIBUTE12 | — | — |
| 11 | VrmAccountingEventsAttribute132 | ATTRIBUTE13 | — | — |
| 12 | VrmAccountingEventsAttribute142 | ATTRIBUTE14 | — | — |
| 13 | VrmAccountingEventsAttribute152 | ATTRIBUTE15 | — | — |
| 14 | VrmAccountingEventsAttribute162 | ATTRIBUTE16 | — | — |
| 15 | VrmAccountingEventsAttribute172 | ATTRIBUTE17 | — | — |
| 16 | VrmAccountingEventsAttribute182 | ATTRIBUTE18 | — | — |
| 17 | VrmAccountingEventsAttribute192 | ATTRIBUTE19 | — | — |
| 18 | VrmAccountingEventsAttribute202 | ATTRIBUTE20 | — | — |
| 19 | VrmAccountingEventsAttribute22 | ATTRIBUTE2 | — | — |
| 20 | VrmAccountingEventsAttribute32 | ATTRIBUTE3 | — | — |
| 21 | VrmAccountingEventsAttribute42 | ATTRIBUTE4 | — | — |
| 22 | VrmAccountingEventsAttribute52 | ATTRIBUTE5 | — | — |
| 23 | VrmAccountingEventsAttribute62 | ATTRIBUTE6 | — | — |
| 24 | VrmAccountingEventsAttribute72 | ATTRIBUTE7 | — | — |
| 25 | VrmAccountingEventsAttribute82 | ATTRIBUTE8 | — | — |
| 26 | VrmAccountingEventsAttribute92 | ATTRIBUTE9 | — | — |
| 27 | VrmAccountingEventsAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 28 | VrmAccountingEventsAttributeDate12 | ATTRIBUTE_DATE1 | — | — |
| 29 | VrmAccountingEventsAttributeDate22 | ATTRIBUTE_DATE2 | — | — |
| 30 | VrmAccountingEventsAttributeDate32 | ATTRIBUTE_DATE3 | — | — |
| 31 | VrmAccountingEventsAttributeDate42 | ATTRIBUTE_DATE4 | — | — |
| 32 | VrmAccountingEventsAttributeDate52 | ATTRIBUTE_DATE5 | — | — |
| 33 | VrmAccountingEventsAttributeNumber12 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | VrmAccountingEventsAttributeNumber22 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | VrmAccountingEventsAttributeNumber32 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | VrmAccountingEventsAttributeNumber42 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | VrmAccountingEventsAttributeNumber52 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | VrmAccountingEventsContractActivityGroupId | CONTRACT_ACTIVITY_GROUP_ID | — | — |
| 39 | VrmAccountingEventsCreatedBy2 | CREATED_BY | — | — |
| 40 | VrmAccountingEventsCreatedFrom2 | CREATED_FROM | — | — |
| 41 | VrmAccountingEventsCreationDate2 | CREATION_DATE | — | — |
| 42 | VrmAccountingEventsLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 43 | VrmAccountingEventsLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 44 | VrmAccountingEventsLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 45 | VrmAccountingEventsObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 46 | VrmAccountingEventsPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 47 | VrmAccountingEventsPerfObligationLineId2 | PERF_OBLIGATION_LINE_ID | — | — |
| 48 | VrmAccountingEventsPobFirstBeFlag | POB_FIRST_BE_FLAG | — | — |
| 49 | VrmAccountingEventsPobLastSeFlag | POB_LAST_SE_FLAG | — | — |
| 50 | VrmAccountingEventsProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 51 | VrmAccountingEventsProcessedRequestId2 | PROCESSED_REQUEST_ID | — | — |
| 52 | VrmAccountingEventsReferenceEventId | REFERENCE_EVENT_ID | — | — |
| 53 | VrmAccountingEventsRequestId2 | REQUEST_ID | — | — |
| 54 | VrmAccountingEventsReversedFlag | REVERSED_FLAG | — | — |
| 55 | VrmAccountingEventsReversedRequestId | REVERSED_REQUEST_ID | — | — |

### [[vrm_billing_line_details|VRM_BILLING_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingLineDetailsPEOBillAccountingDate | BILL_ACCOUNTING_DATE | — | — |
| 2 | BillingLineDetailsPEOBillAcctdAmount | BILL_ACCTD_AMOUNT | — | ✅ |
| 3 | BillingLineDetailsPEOBillAmount | BILL_AMOUNT | — | ✅ |
| 4 | BillingLineDetailsPEOBillDate | BILL_DATE | — | — |
| 5 | BillingLineDetailsPEOBillId | BILL_ID | — | — |
| 6 | BillingLineDetailsPEOBillLineId | BILL_LINE_ID | — | — |
| 7 | BillingLineDetailsPEOBillLineNumber | BILL_LINE_NUMBER | — | — |
| 8 | BillingLineDetailsPEOBillNumber | BILL_NUMBER | — | — |
| 9 | BillingLineDetailsPEOBillQuantity | BILL_QUANTITY | — | ✅ |
| 10 | BillingLineDetailsPEOBillSubLineId | BILL_SUB_LINE_ID | — | — |
| 11 | BillingLineDetailsPEOBillingApplication | BILLING_APPLICATION | — | — |
| 12 | BillingLineDetailsPEOBillingDataProcessedStatus | BILLING_DATA_PROCESSED_STATUS | — | — |
| 13 | BillingLineDetailsPEOBillingLineDetailId | BILLING_LINE_DETAIL_ID | — | — |
| 14 | BillingLineDetailsPEOCreatedBy | CREATED_BY | — | — |
| 15 | BillingLineDetailsPEOCreationDate | CREATION_DATE | — | — |
| 16 | BillingLineDetailsPEODocLineIdChar1 | DOC_LINE_ID_CHAR_1 | — | — |
| 17 | BillingLineDetailsPEODocLineIdChar2 | DOC_LINE_ID_CHAR_2 | — | — |
| 18 | BillingLineDetailsPEODocLineIdChar3 | DOC_LINE_ID_CHAR_3 | — | — |
| 19 | BillingLineDetailsPEODocLineIdChar4 | DOC_LINE_ID_CHAR_4 | — | — |
| 20 | BillingLineDetailsPEODocLineIdChar5 | DOC_LINE_ID_CHAR_5 | — | — |
| 21 | BillingLineDetailsPEODocLineIdInt1 | DOC_LINE_ID_INT_1 | — | — |
| 22 | BillingLineDetailsPEODocLineIdInt2 | DOC_LINE_ID_INT_2 | — | — |
| 23 | BillingLineDetailsPEODocLineIdInt3 | DOC_LINE_ID_INT_3 | — | — |
| 24 | BillingLineDetailsPEODocLineIdInt4 | DOC_LINE_ID_INT_4 | — | — |
| 25 | BillingLineDetailsPEODocLineIdInt5 | DOC_LINE_ID_INT_5 | — | — |
| 26 | BillingLineDetailsPEODocumentLineId | DOCUMENT_LINE_ID | — | — |
| 27 | BillingLineDetailsPEODocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 28 | BillingLineDetailsPEOExchangeRate | EXCHANGE_RATE | — | — |
| 29 | BillingLineDetailsPEOExchangeRateDate | EXCHANGE_RATE_DATE | — | — |
| 30 | BillingLineDetailsPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 31 | BillingLineDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | BillingLineDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | BillingLineDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | BillingLineDetailsPEOLoadRequestId | LOAD_REQUEST_ID | — | — |
| 35 | BillingLineDetailsPEOSourceDocumentDate | SOURCE_DOCUMENT_DATE | — | — |
| 36 | BillingLineDetailsPEOSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 37 | BillingLineDetailsPEOSourceDocumentNumber | SOURCE_DOCUMENT_NUMBER | — | — |
| 38 | BillingLineDetailsPEOSourceSystem | SOURCE_SYSTEM | — | — |

### [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHdrPEOCustomerContractDate | CUSTOMER_CONTRACT_DATE | — | — |
| 2 | CustomerContractHeadersPEOAllocationPendingReason | ALLOCATION_PENDING_REASON | — | — |
| 3 | CustomerContractHeadersPEOAllocationRequestId | ALLOCATION_REQUEST_ID | — | — |
| 4 | CustomerContractHeadersPEOAllocationStatus | ALLOCATION_STATUS | — | — |
| 5 | CustomerContractHeadersPEOAllocationType | ALLOCATION_TYPE | — | — |
| 6 | CustomerContractHeadersPEOAttribute101 | ATTRIBUTE10 | — | — |
| 7 | CustomerContractHeadersPEOAttribute110 | ATTRIBUTE1 | — | — |
| 8 | CustomerContractHeadersPEOAttribute111 | ATTRIBUTE11 | — | — |
| 9 | CustomerContractHeadersPEOAttribute121 | ATTRIBUTE12 | — | — |
| 10 | CustomerContractHeadersPEOAttribute131 | ATTRIBUTE13 | — | — |
| 11 | CustomerContractHeadersPEOAttribute141 | ATTRIBUTE14 | — | — |
| 12 | CustomerContractHeadersPEOAttribute151 | ATTRIBUTE15 | — | — |
| 13 | CustomerContractHeadersPEOAttribute161 | ATTRIBUTE16 | — | — |
| 14 | CustomerContractHeadersPEOAttribute171 | ATTRIBUTE17 | — | — |
| 15 | CustomerContractHeadersPEOAttribute181 | ATTRIBUTE18 | — | — |
| 16 | CustomerContractHeadersPEOAttribute191 | ATTRIBUTE19 | — | — |
| 17 | CustomerContractHeadersPEOAttribute201 | ATTRIBUTE20 | — | — |
| 18 | CustomerContractHeadersPEOAttribute21 | ATTRIBUTE2 | — | — |
| 19 | CustomerContractHeadersPEOAttribute31 | ATTRIBUTE3 | — | — |
| 20 | CustomerContractHeadersPEOAttribute41 | ATTRIBUTE4 | — | — |
| 21 | CustomerContractHeadersPEOAttribute51 | ATTRIBUTE5 | — | — |
| 22 | CustomerContractHeadersPEOAttribute61 | ATTRIBUTE6 | — | — |
| 23 | CustomerContractHeadersPEOAttribute71 | ATTRIBUTE7 | — | — |
| 24 | CustomerContractHeadersPEOAttribute81 | ATTRIBUTE8 | — | — |
| 25 | CustomerContractHeadersPEOAttribute91 | ATTRIBUTE9 | — | — |
| 26 | CustomerContractHeadersPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 27 | CustomerContractHeadersPEOAttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 28 | CustomerContractHeadersPEOAttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 29 | CustomerContractHeadersPEOAttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 30 | CustomerContractHeadersPEOAttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 31 | CustomerContractHeadersPEOAttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 32 | CustomerContractHeadersPEOAttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CustomerContractHeadersPEOAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 34 | CustomerContractHeadersPEOAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 35 | CustomerContractHeadersPEOAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 36 | CustomerContractHeadersPEOAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 37 | CustomerContractHeadersPEOComments1 | COMMENTS | — | — |
| 38 | CustomerContractHeadersPEOContrCurTotalBilledAmt1 | CONTR_CUR_TOTAL_BILLED_AMT | — | — |
| 39 | CustomerContractHeadersPEOContrCurTotalRecogRevAmt1 | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 40 | CustomerContractHeadersPEOContrCurTransactionPrice | CONTR_CUR_TRANSACTION_PRICE | — | — |
| 41 | CustomerContractHeadersPEOContractClassificationCode | CONTRACT_CLASSIFICATION_CODE | — | — |
| 42 | CustomerContractHeadersPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 43 | CustomerContractHeadersPEOContractHashCode | CONTRACT_HASH_CODE | — | — |
| 44 | CustomerContractHeadersPEOContractPaymentAmount | CONTRACT_PAYMENT_AMOUNT | — | — |
| 45 | CustomerContractHeadersPEOContractRuleId | CONTRACT_RULE_ID | — | — |
| 46 | CustomerContractHeadersPEOCreatedFrom1 | CREATED_FROM | — | — |
| 47 | CustomerContractHeadersPEOCreationDate1 | CREATION_DATE | — | — |
| 48 | CustomerContractHeadersPEOCustomerContractFreezeDate | CUSTOMER_CONTRACT_FREEZE_DATE | — | — |
| 49 | CustomerContractHeadersPEOCustomerContractHeaderId1 | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 50 | CustomerContractHeadersPEOCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | — |
| 51 | CustomerContractHeadersPEOEffectivityPeriodId | EFFECTIVITY_PERIOD_ID | — | — |
| 52 | CustomerContractHeadersPEOExchangeRate1 | EXCHANGE_RATE | — | — |
| 53 | CustomerContractHeadersPEOExchangeRateDate1 | EXCHANGE_RATE_DATE | — | — |
| 54 | CustomerContractHeadersPEOExchangeRateType1 | EXCHANGE_RATE_TYPE | — | — |
| 55 | CustomerContractHeadersPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 56 | CustomerContractHeadersPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 57 | CustomerContractHeadersPEOLedgerId | LEDGER_ID | — | — |
| 58 | CustomerContractHeadersPEOLegalEntityId1 | LEGAL_ENTITY_ID | — | — |
| 59 | CustomerContractHeadersPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 60 | CustomerContractHeadersPEOPaymentConfirmFlag | PAYMENT_CONFIRM_FLAG | — | — |
| 61 | CustomerContractHeadersPEOProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 62 | CustomerContractHeadersPEOReference | REFERENCE | — | — |
| 63 | CustomerContractHeadersPEORequestId1 | REQUEST_ID | — | — |
| 64 | CustomerContractHeadersPEOReviewStatus | REVIEW_STATUS | — | — |
| 65 | CustomerContractHeadersPEOSingleObligationFlag | SINGLE_OBLIGATION_FLAG | — | — |
| 66 | CustomerContractHeadersPEOStandaloneSalesFlag | STANDALONE_SALES_FLAG | — | — |

### [[vrm_fmv_lines|VRM_FMV_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceLineFmvLineId | FMV_LINE_ID | — | — |
| 2 | PriceLineFmvLineSetId | FMV_LINE_SET_ID | — | — |
| 3 | PriceLineInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 4 | PriceLineItemType | ITEM_TYPE | — | — |
| 5 | PriceLineItemTypeId | ITEM_TYPE_ID | — | — |
| 6 | PriceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | PriceLinePEOFmvLineId | FMV_LINE_ID | — | — |
| 8 | PriceLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PriceLinePriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | FMVTemplateBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 3 | FMVTemplateBasePEOTemplateId | TEMPLATE_ID | — | — |

### [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PerfObligationsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PerfObligationsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PerfObligationsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PerfObligationsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PerfObligationsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PerfObligationsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PerfObligationsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PerfObligationsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PerfObligationsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PerfObligationsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PerfObligationsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PerfObligationsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PerfObligationsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | PerfObligationsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | PerfObligationsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | PerfObligationsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | PerfObligationsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | PerfObligationsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | PerfObligationsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | PerfObligationsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | PerfObligationsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | PerfObligationsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | PerfObligationsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | PerfObligationsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | PerfObligationsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | PerfObligationsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | PerfObligationsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | PerfObligationsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | PerfObligationsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | PerfObligationsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | PerfObligationsPEOBasePrice | BASE_PRICE | — | ✅ |
| 33 | PerfObligationsPEOBasePricePercentage | BASE_PRICE_PERCENTAGE | — | ✅ |
| 34 | PerfObligationsPEOComments | COMMENTS | — | ✅ |
| 35 | PerfObligationsPEOContrCurCrLiabilityAmt | CONTR_CUR_CR_LIABILITY_AMT | — | — |
| 36 | PerfObligationsPEOContrCurDrAssetAmt | CONTR_CUR_DR_ASSET_AMT | — | — |
| 37 | PerfObligationsPEOContrCurDrDiscountAmt | CONTR_CUR_DR_DISCOUNT_AMT | — | — |
| 38 | PerfObligationsPEOContrCurFmvAmt | CONTR_CUR_FMV_AMT | — | — |
| 39 | PerfObligationsPEOContrCurNetLineAmt | CONTR_CUR_NET_LINE_AMT | — | — |
| 40 | PerfObligationsPEOContrCurTotAllocAmt | CONTR_CUR_TOT_ALLOC_AMT | — | — |
| 41 | PerfObligationsPEOContrCurTotCarveOutAmt | CONTR_CUR_TOT_CARVE_OUT_AMT | — | — |
| 42 | PerfObligationsPEOContrCurTotNetConsiderAmt | CONTR_CUR_TOT_NET_CONSIDER_AMT | — | — |
| 43 | PerfObligationsPEOContrCurTotVarConsiderAmt | CONTR_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 44 | PerfObligationsPEOContrCurTotalBilledAmt | CONTR_CUR_TOTAL_BILLED_AMT | — | — |
| 45 | PerfObligationsPEOContrCurTotalRecogRevAmt | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 46 | PerfObligationsPEOCostAmount | COST_AMOUNT | — | — |
| 47 | PerfObligationsPEOCreatedByUserID | CREATED_BY | — | ✅ |
| 48 | PerfObligationsPEOCreatedFrom | CREATED_FROM | — | — |
| 49 | PerfObligationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 50 | PerfObligationsPEOCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 51 | PerfObligationsPEODiscardFlag | DISCARD_FLAG | — | ✅ |
| 52 | PerfObligationsPEODiscountAmount | DISCOUNT_AMOUNT | — | — |
| 53 | PerfObligationsPEODiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 54 | PerfObligationsPEOExchangeRate | EXCHANGE_RATE | — | — |
| 55 | PerfObligationsPEOExchangeRateDate | EXCHANGE_RATE_DATE | — | — |
| 56 | PerfObligationsPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 57 | PerfObligationsPEOExemptFromAllocationFlag | EXEMPT_FROM_ALLOCATION_FLAG | — | ✅ |
| 58 | PerfObligationsPEOFmvLineId | FMV_LINE_ID | — | ✅ |
| 59 | PerfObligationsPEOFmvTemplateId | FMV_TEMPLATE_ID | — | — |
| 60 | PerfObligationsPEOGrossMarginPercentage | GROSS_MARGIN_PERCENTAGE | — | ✅ |
| 61 | PerfObligationsPEOImplPerfObligTemplateId | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 62 | PerfObligationsPEOInitialPerfEvtCreatedFlag | INITIAL_PERF_EVT_CREATED_FLAG | — | ✅ |
| 63 | PerfObligationsPEOInitialPerfEvtExpectedDate | INITIAL_PERF_EVT_EXPECTED_DATE | — | ✅ |
| 64 | PerfObligationsPEOInitialPerfEvtRecordedFlag | INITIAL_PERF_EVT_RECORDED_FLAG | — | ✅ |
| 65 | PerfObligationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | PerfObligationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | PerfObligationsPEOLastUpdatedByUserID | LAST_UPDATED_BY | — | ✅ |
| 68 | PerfObligationsPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 69 | PerfObligationsPEOListPriceAmount | LIST_PRICE_AMOUNT | — | — |
| 70 | PerfObligationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | PerfObligationsPEOObligCurFmvAmt | OBLIG_CUR_FMV_AMT | — | — |
| 72 | PerfObligationsPEOObligCurNetLineAmt | OBLIG_CUR_NET_LINE_AMT | — | — |
| 73 | PerfObligationsPEOObligCurNetSalesPrice | OBLIG_CUR_NET_SALES_PRICE | — | ✅ |
| 74 | PerfObligationsPEOObligCurTotAllocAmt | OBLIG_CUR_TOT_ALLOC_AMT | — | — |
| 75 | PerfObligationsPEOObligCurTotCarveOutAmt | OBLIG_CUR_TOT_CARVE_OUT_AMT | — | — |
| 76 | PerfObligationsPEOObligCurTotNetConsiderAmt | OBLIG_CUR_TOT_NET_CONSIDER_AMT | — | — |
| 77 | PerfObligationsPEOObligCurTotVarConsiderAmt | OBLIG_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 78 | PerfObligationsPEOObligCurTotalBilledAmt | OBLIG_CUR_TOTAL_BILLED_AMT | — | — |
| 79 | PerfObligationsPEOObligCurTotalRecogRevAmt | OBLIG_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 80 | PerfObligationsPEOObligCurrencyCode | OBLIG_CURRENCY_CODE | — | ✅ |
| 81 | PerfObligationsPEOObligHashCode | OBLIG_HASH_CODE | — | — |
| 82 | PerfObligationsPEOObligPaymentAmount | OBLIG_PAYMENT_AMOUNT | — | — |
| 83 | PerfObligationsPEOObligationReference | OBLIGATION_REFERENCE | — | ✅ |
| 84 | PerfObligationsPEOPerfObligClassificationCode | PERF_OBLIG_CLASSIFICATION_CODE | — | ✅ |
| 85 | PerfObligationsPEOPerfObligFreezeFlag | PERF_OBLIG_FREEZE_FLAG | — | ✅ |
| 86 | PerfObligationsPEOPerfObligationGroupRuleId | PERF_OBLIGATION_GROUP_RULE_ID | — | — |
| 87 | PerfObligationsPEOPerfObligationId | PERF_OBLIGATION_ID | — | ✅ |
| 88 | PerfObligationsPEOPerfObligationNumber | PERF_OBLIGATION_NUMBER | — | ✅ |
| 89 | PerfObligationsPEOPerfObligationTemplateId | PERF_OBLIGATION_TEMPLATE_ID | — | — |
| 90 | PerfObligationsPEOPerfObligationType | PERF_OBLIGATION_TYPE | — | ✅ |
| 91 | PerfObligationsPEOPricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 92 | PerfObligationsPEORemovedFlag | REMOVED_FLAG | — | ✅ |
| 93 | PerfObligationsPEORequestId | REQUEST_ID | — | — |
| 94 | PerfObligationsPEOSatisfactionDate | SATISFACTION_DATE | — | ✅ |
| 95 | PerfObligationsPEOSatisfactionMethod | SATISFACTION_METHOD | — | ✅ |
| 96 | PerfObligationsPEOSatisfactionStatus | SATISFACTION_STATUS | — | ✅ |
| 97 | PerfObligationsPEOSubstantialDistCreatedFlag | SUBSTANTIAL_DIST_CREATED_FLAG | — | — |
| 98 | PerfObligationsPEOUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 99 | PoSspRangeRuleCode | PO_SSP_RANGE_RULE_CODE | — | ✅ |
| 100 | PoSspRuleResultCode | PO_SSP_RULE_RESULT_CODE | — | ✅ |

### [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationLinesPEOAllocationRequiredFlag | ALLOCATION_REQUIRED_FLAG | — | ✅ |
| 2 | PerfObligationLinesPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PerfObligationLinesPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PerfObligationLinesPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PerfObligationLinesPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PerfObligationLinesPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PerfObligationLinesPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PerfObligationLinesPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PerfObligationLinesPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PerfObligationLinesPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PerfObligationLinesPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PerfObligationLinesPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PerfObligationLinesPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PerfObligationLinesPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PerfObligationLinesPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | PerfObligationLinesPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | PerfObligationLinesPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | PerfObligationLinesPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | PerfObligationLinesPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | PerfObligationLinesPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | PerfObligationLinesPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | PerfObligationLinesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | PerfObligationLinesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | PerfObligationLinesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | PerfObligationLinesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | PerfObligationLinesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | PerfObligationLinesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | PerfObligationLinesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | PerfObligationLinesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | PerfObligationLinesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | PerfObligationLinesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | PerfObligationLinesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | PerfObligationLinesPEOAutomaticConfirmationPeriod | AUTOMATIC_CONFIRMATION_PERIOD | — | — |
| 34 | PerfObligationLinesPEOBuId | BU_ID | — | — |
| 35 | PerfObligationLinesPEOComments | COMMENTS | — | ✅ |
| 36 | PerfObligationLinesPEOContrCurAllocatedAmt | CONTR_CUR_ALLOCATED_AMT | — | — |
| 37 | PerfObligationLinesPEOContrCurBilledAmt | CONTR_CUR_BILLED_AMT | — | — |
| 38 | PerfObligationLinesPEOContrCurCarveOutAmt | CONTR_CUR_CARVE_OUT_AMT | — | — |
| 39 | PerfObligationLinesPEOContrCurFmvAmt | CONTR_CUR_FMV_AMT | — | — |
| 40 | PerfObligationLinesPEOContrCurNetConsiderAmt | CONTR_CUR_NET_CONSIDER_AMT | — | — |
| 41 | PerfObligationLinesPEOContrCurNetLineAmt | CONTR_CUR_NET_LINE_AMT | — | — |
| 42 | PerfObligationLinesPEOContrCurRecogRevAmt | CONTR_CUR_RECOG_REV_AMT | — | — |
| 43 | PerfObligationLinesPEOContrCurVarConsiderAmt | CONTR_CUR_VAR_CONSIDER_AMT | — | — |
| 44 | PerfObligationLinesPEOCreatedBy | CREATED_BY | — | — |
| 45 | PerfObligationLinesPEOCreatedFrom | CREATED_FROM | — | — |
| 46 | PerfObligationLinesPEOCreationDate | CREATION_DATE | — | — |
| 47 | PerfObligationLinesPEOCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 48 | PerfObligationLinesPEODiscardFlag | DISCARD_FLAG | — | ✅ |
| 49 | PerfObligationLinesPEODocumentLineId | DOCUMENT_LINE_ID | — | ✅ |
| 50 | PerfObligationLinesPEOEnteredCurAllocatedAmt | ENTERED_CUR_ALLOCATED_AMT | — | — |
| 51 | PerfObligationLinesPEOEnteredCurBilledAmt | ENTERED_CUR_BILLED_AMT | — | — |
| 52 | PerfObligationLinesPEOEnteredCurCarveOutAmt | ENTERED_CUR_CARVE_OUT_AMT | — | — |
| 53 | PerfObligationLinesPEOEnteredCurFmvAmt | ENTERED_CUR_FMV_AMT | — | — |
| 54 | PerfObligationLinesPEOEnteredCurNetConsiderAmt | ENTERED_CUR_NET_CONSIDER_AMT | — | — |
| 55 | PerfObligationLinesPEOEnteredCurRecogRevAmt | ENTERED_CUR_RECOG_REV_AMT | — | — |
| 56 | PerfObligationLinesPEOEnteredCurVarConsiderAmt | ENTERED_CUR_VAR_CONSIDER_AMT | — | — |
| 57 | PerfObligationLinesPEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 58 | PerfObligationLinesPEOExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 59 | PerfObligationLinesPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 60 | PerfObligationLinesPEOFmvLineId | FMV_LINE_ID | — | ✅ |
| 61 | PerfObligationLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | PerfObligationLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | PerfObligationLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | PerfObligationLinesPEOLatestRevisionIntentCode | LATEST_REVISION_INTENT_CODE | — | ✅ |
| 65 | PerfObligationLinesPEOLatestVersionDate | LATEST_VERSION_DATE | — | ✅ |
| 66 | PerfObligationLinesPEOLedgerId | LEDGER_ID | — | — |
| 67 | PerfObligationLinesPEOLineCurrencyCode | LINE_CURRENCY_CODE | — | ✅ |
| 68 | PerfObligationLinesPEOLineSatisfactionDate | LINE_SATISFACTION_DATE | — | ✅ |
| 69 | PerfObligationLinesPEOLineSatisfactionStatus | LINE_SATISFACTION_STATUS | — | ✅ |
| 70 | PerfObligationLinesPEOLineSource | LINE_SOURCE | — | ✅ |
| 71 | PerfObligationLinesPEOMissingRevInformationFlag | MISSING_REV_INFORMATION_FLAG | — | ✅ |
| 72 | PerfObligationLinesPEOMoveToContrNumber | MOVE_TO_CONTR_NUMBER | — | — |
| 73 | PerfObligationLinesPEOMoveToObligNumber | MOVE_TO_OBLIG_NUMBER | — | — |
| 74 | PerfObligationLinesPEONetLineAmt | NET_LINE_AMT | — | — |
| 75 | PerfObligationLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 76 | PerfObligationLinesPEOParentPerfObligLineId | PARENT_PERF_OBLIG_LINE_ID | — | ✅ |
| 77 | PerfObligationLinesPEOPaymentAmount | PAYMENT_AMOUNT | — | — |
| 78 | PerfObligationLinesPEOPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 79 | PerfObligationLinesPEOPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | ✅ |
| 80 | PerfObligationLinesPEOPerfObligationLineNumber | PERF_OBLIGATION_LINE_NUMBER | — | ✅ |
| 81 | PerfObligationLinesPEOPricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 82 | PerfObligationLinesPEORemovedBy | REMOVED_BY | — | ✅ |
| 83 | PerfObligationLinesPEORemovedDate | REMOVED_DATE | — | ✅ |
| 84 | PerfObligationLinesPEORemovedFlag | REMOVED_FLAG | — | ✅ |
| 85 | PerfObligationLinesPEORemovedRequestId | REMOVED_REQUEST_ID | — | — |
| 86 | PerfObligationLinesPEOReprocessLineEventsFlag | REPROCESS_LINE_EVENTS_FLAG | — | — |
| 87 | PerfObligationLinesPEORequestId | REQUEST_ID | — | — |
| 88 | PerfObligationLinesPEORevRecProcesdDocLineId | REV_REC_PROCESD_DOC_LINE_ID | — | — |
| 89 | PerfObligationLinesPEORevRecProcesdRevEndDate | REV_REC_PROCESD_REV_END_DATE | — | ✅ |
| 90 | PerfObligationLinesPEORevRecProcesdRevRuleDur | REV_REC_PROCESD_REV_RULE_DUR | — | ✅ |
| 91 | PerfObligationLinesPEORevRecProcesdRevRuleId | REV_REC_PROCESD_REV_RULE_ID | — | ✅ |
| 92 | PerfObligationLinesPEORevRecProcesdRevStartDate | REV_REC_PROCESD_REV_START_DATE | — | ✅ |
| 93 | PerfObligationLinesPEORevRecProcessedFlag | REV_REC_PROCESSED_FLAG | — | ✅ |
| 94 | PerfObligationLinesPEORevRecReprocessStatusCode | REV_REC_REPROCESS_STATUS_CODE | — | ✅ |
| 95 | PerfObligationLinesPEORevenueEndDate | REVENUE_END_DATE | — | ✅ |
| 96 | PerfObligationLinesPEORevenueRuleDuration | REVENUE_RULE_DURATION | — | ✅ |
| 97 | PerfObligationLinesPEORevenueRuleId | REVENUE_RULE_ID | — | — |
| 98 | PerfObligationLinesPEORevenueStartDate | REVENUE_START_DATE | — | ✅ |
| 99 | PerfObligationLinesPEOSatisfactionBaseProportion | SATISFACTION_BASE_PROPORTION | — | ✅ |
| 100 | PerfObligationLinesPEOSatisfactionConfirmFlag | SATISFACTION_CONFIRM_FLAG | — | — |
| 101 | PerfObligationLinesPEOSatisfactionMeasurementModel | SATISFACTION_MEASUREMENT_MODEL | — | ✅ |
| 102 | PerfObligationLinesPEOSeCreatedFromSublineFlag | SE_CREATED_FROM_SUBLINE_FLAG | — | — |
| 103 | PerfObligationLinesPEOStandaloneSalesFlag | STANDALONE_SALES_FLAG | — | ✅ |
| 104 | PolSspRangeRuleCode | POL_SSP_RANGE_RULE_CODE | — | ✅ |
| 105 | PolSspRuleResultCode | POL_SSP_RULE_RESULT_CODE | — | ✅ |

### [[vrm_perf_obligation_lin_dists|VRM_PERF_OBLIGATION_LIN_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationLinDistsEOAccountClass | ACCOUNT_CLASS | — | ✅ |
| 2 | PerfObligationLinDistsEOAccountingDate | ACCOUNTING_DATE | — | ✅ |
| 3 | PerfObligationLinDistsEOAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 4 | PerfObligationLinDistsEOAmount | AMOUNT | — | ✅ |
| 5 | PerfObligationLinDistsEOApplicationId | APPLICATION_ID | — | — |
| 6 | PerfObligationLinDistsEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | PerfObligationLinDistsEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | PerfObligationLinDistsEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | PerfObligationLinDistsEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | PerfObligationLinDistsEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | PerfObligationLinDistsEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | PerfObligationLinDistsEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | PerfObligationLinDistsEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | PerfObligationLinDistsEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | PerfObligationLinDistsEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | PerfObligationLinDistsEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | PerfObligationLinDistsEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | PerfObligationLinDistsEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | PerfObligationLinDistsEOAttribute3 | ATTRIBUTE3 | — | — |
| 20 | PerfObligationLinDistsEOAttribute4 | ATTRIBUTE4 | — | — |
| 21 | PerfObligationLinDistsEOAttribute5 | ATTRIBUTE5 | — | — |
| 22 | PerfObligationLinDistsEOAttribute6 | ATTRIBUTE6 | — | — |
| 23 | PerfObligationLinDistsEOAttribute7 | ATTRIBUTE7 | — | — |
| 24 | PerfObligationLinDistsEOAttribute8 | ATTRIBUTE8 | — | — |
| 25 | PerfObligationLinDistsEOAttribute9 | ATTRIBUTE9 | — | — |
| 26 | PerfObligationLinDistsEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | PerfObligationLinDistsEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 28 | PerfObligationLinDistsEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | PerfObligationLinDistsEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | PerfObligationLinDistsEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | PerfObligationLinDistsEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | PerfObligationLinDistsEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | PerfObligationLinDistsEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 34 | PerfObligationLinDistsEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 35 | PerfObligationLinDistsEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 36 | PerfObligationLinDistsEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 37 | PerfObligationLinDistsEOBuId | BU_ID | — | — |
| 38 | PerfObligationLinDistsEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 39 | PerfObligationLinDistsEOCogsRequestId | COGS_REQUEST_ID | — | — |
| 40 | PerfObligationLinDistsEOConcatenatedSegments | CONCATENATED_SEGMENTS | — | — |
| 41 | PerfObligationLinDistsEOCreatedBy | CREATED_BY | — | — |
| 42 | PerfObligationLinDistsEOCreatedFrom | CREATED_FROM | — | — |
| 43 | PerfObligationLinDistsEOCreationDate | CREATION_DATE | — | — |
| 44 | PerfObligationLinDistsEOCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 45 | PerfObligationLinDistsEOEventId | EVENT_ID | — | — |
| 46 | PerfObligationLinDistsEOExchangeRate | EXCHANGE_RATE | — | ✅ |
| 47 | PerfObligationLinDistsEOExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 48 | PerfObligationLinDistsEOExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 49 | PerfObligationLinDistsEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | PerfObligationLinDistsEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | PerfObligationLinDistsEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | PerfObligationLinDistsEOLedgerId | LEDGER_ID | — | — |
| 53 | PerfObligationLinDistsEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | PerfObligationLinDistsEOOriginalAccountingDate | ORIGINAL_ACCOUNTING_DATE | — | ✅ |
| 55 | PerfObligationLinDistsEOPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 56 | PerfObligationLinDistsEOPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | — |
| 57 | PerfObligationLinDistsEOPerfObligationLineSplitId | PERF_OBLIGATION_LINE_SPLIT_ID | — | — |
| 58 | PerfObligationLinDistsEOPolBillingEventId | POL_BILLING_EVENT_ID | — | — |
| 59 | PerfObligationLinDistsEOPolEventType | POL_EVENT_TYPE | — | — |
| 60 | PerfObligationLinDistsEOPolSatisfactionEventId | POL_SATISFACTION_EVENT_ID | — | — |
| 61 | PerfObligationLinDistsEOPostedToSlaDate | POSTED_TO_SLA_DATE | — | ✅ |
| 62 | PerfObligationLinDistsEOPostedToSlaFlag | POSTED_TO_SLA_FLAG | — | ✅ |
| 63 | PerfObligationLinDistsEOPostingControlId | POSTING_CONTROL_ID | — | — |
| 64 | PerfObligationLinDistsEORequestId | REQUEST_ID | — | — |
| 65 | PerfObligationLinDistsEOTransferToGlFlag | TRANSFER_TO_GL_FLAG | — | ✅ |
| 66 | PerfObligationLineDistId | PERF_OBLIGATION_LINE_DIST_ID | 🔑 | ✅ |
| 67 | VrmAccountingEventsAccountingEventId | ACCOUNTING_EVENT_ID | — | — |

### [[vrm_pol_billing_events|VRM_POL_BILLING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PolBillingEventsAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PolBillingEventsAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PolBillingEventsAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PolBillingEventsAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PolBillingEventsAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PolBillingEventsAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PolBillingEventsAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PolBillingEventsAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PolBillingEventsAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PolBillingEventsAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PolBillingEventsAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PolBillingEventsAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PolBillingEventsAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PolBillingEventsAttribute3 | ATTRIBUTE3 | — | — |
| 15 | PolBillingEventsAttribute4 | ATTRIBUTE4 | — | — |
| 16 | PolBillingEventsAttribute5 | ATTRIBUTE5 | — | — |
| 17 | PolBillingEventsAttribute6 | ATTRIBUTE6 | — | — |
| 18 | PolBillingEventsAttribute7 | ATTRIBUTE7 | — | — |
| 19 | PolBillingEventsAttribute8 | ATTRIBUTE8 | — | — |
| 20 | PolBillingEventsAttribute9 | ATTRIBUTE9 | — | — |
| 21 | PolBillingEventsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | PolBillingEventsAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | PolBillingEventsAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | PolBillingEventsAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | PolBillingEventsAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | PolBillingEventsAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | PolBillingEventsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | PolBillingEventsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | PolBillingEventsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | PolBillingEventsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | PolBillingEventsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | PolBillingEventsBatchNumber | BATCH_NUMBER | — | — |
| 33 | PolBillingEventsBillingDataJobRequestId | BILLING_DATA_JOB_REQUEST_ID | — | — |
| 34 | PolBillingEventsBillingLineDetailId | BILLING_LINE_DETAIL_ID | — | — |
| 35 | PolBillingEventsCreatedBy | CREATED_BY | — | — |
| 36 | PolBillingEventsCreatedFrom | CREATED_FROM | — | — |
| 37 | PolBillingEventsCreationDate | CREATION_DATE | — | — |
| 38 | PolBillingEventsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | PolBillingEventsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | PolBillingEventsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | PolBillingEventsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | PolBillingEventsPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | — |
| 43 | PolBillingEventsPolBillingEventId | POL_BILLING_EVENT_ID | — | — |
| 44 | PolBillingEventsProcessedFlag | PROCESSED_FLAG | — | — |
| 45 | PolBillingEventsProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 46 | PolBillingEventsRequestId | REQUEST_ID | — | — |

### [[vrm_pricing_lines|VRM_PRICING_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingLinesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 2 | PricingLinesItemType | ITEM_TYPE | — | — |
| 3 | PricingLinesItemTypeId | ITEM_TYPE_ID | — | — |
| 4 | PricingLinesLatestPeriodActionCode | LATEST_PERIOD_ACTION_CODE | — | ✅ |
| 5 | PricingLinesLatestReversalDays | LATEST_REVERSAL_DAYS | — | ✅ |
| 6 | PricingLinesRevisedRecurPatternCode | REVISED_RECUR_PATTERN_CODE | — | ✅ |
| 7 | PricingLinesRevisedRecurringAmount | REVISED_RECURRING_AMOUNT | — | — |
| 8 | PricingLinesRevisedRecurringFlag | REVISED_RECURRING_FLAG | — | ✅ |
| 9 | PricingLinesRevisedRecurringFrequency | REVISED_RECURRING_FREQUENCY | — | ✅ |
| 10 | PricingLinesRevisedTerminationDate | REVISED_TERMINATION_DATE | — | ✅ |
| 11 | PricingLinesTotalReversalDays | TOTAL_REVERSAL_DAYS | — | ✅ |

### [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocLinesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 2 | SourceDocLinesInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 3 | SourceDocLinesItemId | ITEM_ID | — | — |
| 4 | SourceDocLinesMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 5 | SourceDocLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
