---
id: DOC-OTHER-PVO-CustomerContractHeadersPVO
doc_type: system-doc
title: "CustomerContractHeadersPVO — PVO Cross-Module"
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
  - CustomerContractHeadersPVO
  - customercontractheaderspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerContractHeadersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Contract Headers. Acessa as tabelas: GL_LEDGERS, PER_PERSON_NAMES_F_V, PER_USERS (+1).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.CustomerContractHeadersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 4 | 1 | 37 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]] — 80 atributos (1 PKs, 37 BICC)

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
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHeadersAllocationPendingReason | ALLOCATION_PENDING_REASON | — | ✅ |
| 2 | CustContHeadersAllocationRequestId | ALLOCATION_REQUEST_ID | — | — |
| 3 | CustContHeadersAllocationStatus | ALLOCATION_STATUS | — | ✅ |
| 4 | CustContHeadersAllocationType | ALLOCATION_TYPE | — | ✅ |
| 5 | CustContHeadersAttribute1 | ATTRIBUTE1 | — | — |
| 6 | CustContHeadersAttribute10 | ATTRIBUTE10 | — | — |
| 7 | CustContHeadersAttribute11 | ATTRIBUTE11 | — | — |
| 8 | CustContHeadersAttribute12 | ATTRIBUTE12 | — | — |
| 9 | CustContHeadersAttribute13 | ATTRIBUTE13 | — | — |
| 10 | CustContHeadersAttribute14 | ATTRIBUTE14 | — | — |
| 11 | CustContHeadersAttribute15 | ATTRIBUTE15 | — | — |
| 12 | CustContHeadersAttribute16 | ATTRIBUTE16 | — | — |
| 13 | CustContHeadersAttribute17 | ATTRIBUTE17 | — | — |
| 14 | CustContHeadersAttribute18 | ATTRIBUTE18 | — | — |
| 15 | CustContHeadersAttribute19 | ATTRIBUTE19 | — | — |
| 16 | CustContHeadersAttribute2 | ATTRIBUTE2 | — | — |
| 17 | CustContHeadersAttribute20 | ATTRIBUTE20 | — | — |
| 18 | CustContHeadersAttribute3 | ATTRIBUTE3 | — | — |
| 19 | CustContHeadersAttribute4 | ATTRIBUTE4 | — | — |
| 20 | CustContHeadersAttribute5 | ATTRIBUTE5 | — | — |
| 21 | CustContHeadersAttribute6 | ATTRIBUTE6 | — | — |
| 22 | CustContHeadersAttribute7 | ATTRIBUTE7 | — | — |
| 23 | CustContHeadersAttribute8 | ATTRIBUTE8 | — | — |
| 24 | CustContHeadersAttribute9 | ATTRIBUTE9 | — | — |
| 25 | CustContHeadersAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | CustContHeadersAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | CustContHeadersAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | CustContHeadersAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | CustContHeadersAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | CustContHeadersAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | CustContHeadersAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 32 | CustContHeadersAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 33 | CustContHeadersAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 34 | CustContHeadersAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 35 | CustContHeadersAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 36 | CustContHeadersComments | COMMENTS | — | ✅ |
| 37 | CustContHeadersContrCurTotalBilledAmt | CONTR_CUR_TOTAL_BILLED_AMT | — | ✅ |
| 38 | CustContHeadersContrCurTotalRecogRevAmt | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | ✅ |
| 39 | CustContHeadersContrCurTransactionPrice | CONTR_CUR_TRANSACTION_PRICE | — | ✅ |
| 40 | CustContHeadersContractClassificationCode | CONTRACT_CLASSIFICATION_CODE | — | ✅ |
| 41 | CustContHeadersContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 42 | CustContHeadersContractHashCode | CONTRACT_HASH_CODE | — | — |
| 43 | CustContHeadersContractPaymentAmount | CONTRACT_PAYMENT_AMOUNT | — | — |
| 44 | CustContHeadersContractRuleId | CONTRACT_RULE_ID | — | — |
| 45 | CustContHeadersCreatedFrom | CREATED_FROM | — | — |
| 46 | CustContHeadersCreationDate | CREATION_DATE | — | ✅ |
| 47 | CustContHeadersCustomerContractDate | CUSTOMER_CONTRACT_DATE | — | ✅ |
| 48 | CustContHeadersCustomerContractFreezeDate | CUSTOMER_CONTRACT_FREEZE_DATE | — | ✅ |
| 49 | CustContHeadersCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | ✅ |
| 50 | CustContHeadersEffectivityPeriodId | EFFECTIVITY_PERIOD_ID | — | — |
| 51 | CustContHeadersExchangeRate | EXCHANGE_RATE | — | — |
| 52 | CustContHeadersExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 53 | CustContHeadersExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 54 | CustContHeadersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | CustContHeadersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 56 | CustContHeadersLedgerId | LEDGER_ID | — | — |
| 57 | CustContHeadersLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 58 | CustContHeadersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | CustContHeadersPaymentConfirmFlag | PAYMENT_CONFIRM_FLAG | — | ✅ |
| 60 | CustContHeadersProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 61 | CustContHeadersReference | REFERENCE | — | ✅ |
| 62 | CustContHeadersRequestId | REQUEST_ID | — | — |
| 63 | CustContHeadersReviewStatus | REVIEW_STATUS | — | ✅ |
| 64 | CustContHeadersSingleObligationFlag | SINGLE_OBLIGATION_FLAG | — | ✅ |
| 65 | CustContHeadersStandaloneSalesFlag | STANDALONE_SALES_FLAG | — | ✅ |
| 66 | CustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | 🔑 | ✅ |
| 67 | CustomerContractHeadersAdjustmentStatusCode | ADJUSTMENT_STATUS_CODE | — | ✅ |
| 68 | CustomerContractHeadersContrCurModDateAllocAmt | CONTR_CUR_MOD_DATE_ALLOC_AMT | — | ✅ |
| 69 | CustomerContractHeadersContrCurNonexemptTrxPrice | CONTR_CUR_NONEXEMPT_TRX_PRICE | — | ✅ |
| 70 | CustomerContractHeadersContractGroupNumber | CONTRACT_GROUP_NUMBER | — | ✅ |
| 71 | CustomerContractHeadersContractModificationDate | CONTRACT_MODIFICATION_DATE | — | ✅ |
| 72 | CustomerContractHeadersCreatedBy | CREATED_BY | — | ✅ |
| 73 | CustomerContractHeadersExclFromAutoWriteoffFlag | EXCL_FROM_AUTO_WRITEOFF_FLAG | — | ✅ |
| 74 | CustomerContractHeadersFullSatisfactionDate | FULL_SATISFACTION_DATE | — | ✅ |
| 75 | CustomerContractHeadersLastActivityDate | LAST_ACTIVITY_DATE | — | ✅ |
| 76 | CustomerContractHeadersLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 77 | CustomerContractHeadersLatestImmaterialChangeCode | LATEST_IMMATERIAL_CHANGE_CODE | — | ✅ |
| 78 | CustomerContractHeadersLatestRevisionIntentCode | LATEST_REVISION_INTENT_CODE | — | ✅ |
| 79 | CustomerContractHeadersLatestVersionDate | LATEST_VERSION_DATE | — | ✅ |
| 80 | CustomerContractHeadersSatisfactionStatus | SATISFACTION_STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
