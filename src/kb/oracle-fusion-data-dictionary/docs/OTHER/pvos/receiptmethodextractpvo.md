---
id: DOC-OTHER-PVO-ReceiptMethodExtractPVO
doc_type: system-doc
title: "ReceiptMethodExtractPVO — PVO Cross-Module"
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
  - ReceiptMethodExtractPVO
  - receiptmethodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptMethodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receipt Method Extract. Acessa as tabelas: AR_RECEIPT_CLASSES, AR_RECEIPT_METHODS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceiptMethodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 128 | 2 | 1 | 44 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[ar_receipt_classes|AR_RECEIPT_CLASSES]] — 62 atributos (15 BICC)
- [[ar_receipt_methods|AR_RECEIPT_METHODS]] — 66 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[ar_receipt_classes|AR_RECEIPT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArReceiptClassAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ArReceiptClassAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ArReceiptClassAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ArReceiptClassAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ArReceiptClassAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ArReceiptClassAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ArReceiptClassAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ArReceiptClassAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ArReceiptClassAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ArReceiptClassAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ArReceiptClassAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ArReceiptClassAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ArReceiptClassAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ArReceiptClassAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ArReceiptClassAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ArReceiptClassAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ArReceiptClassBillOfExchangeFlag | BILL_OF_EXCHANGE_FLAG | — | ✅ |
| 18 | ArReceiptClassClearFlag | CLEAR_FLAG | — | ✅ |
| 19 | ArReceiptClassConfirmFlag | CONFIRM_FLAG | — | ✅ |
| 20 | ArReceiptClassCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArReceiptClassCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArReceiptClassCreationMethodCode | CREATION_METHOD_CODE | — | ✅ |
| 23 | ArReceiptClassCreationStatus | CREATION_STATUS | — | ✅ |
| 24 | ArReceiptClassGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 25 | ArReceiptClassGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 26 | ArReceiptClassGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 27 | ArReceiptClassGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 28 | ArReceiptClassGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 29 | ArReceiptClassGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 30 | ArReceiptClassGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 31 | ArReceiptClassGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 32 | ArReceiptClassGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 33 | ArReceiptClassGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 34 | ArReceiptClassGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 35 | ArReceiptClassGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 36 | ArReceiptClassGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 37 | ArReceiptClassGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 38 | ArReceiptClassGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 39 | ArReceiptClassGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 40 | ArReceiptClassGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 41 | ArReceiptClassGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 42 | ArReceiptClassGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 43 | ArReceiptClassGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 44 | ArReceiptClassGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 45 | ArReceiptClassGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 46 | ArReceiptClassGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 47 | ArReceiptClassGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 48 | ArReceiptClassGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 49 | ArReceiptClassGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 50 | ArReceiptClassGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 51 | ArReceiptClassGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 52 | ArReceiptClassGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 53 | ArReceiptClassGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 54 | ArReceiptClassGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 55 | ArReceiptClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | ArReceiptClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 57 | ArReceiptClassLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 58 | ArReceiptClassName | NAME | — | ✅ |
| 59 | ArReceiptClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 60 | ArReceiptClassReceiptClassId | RECEIPT_CLASS_ID | — | ✅ |
| 61 | ArReceiptClassRemitFlag | REMIT_FLAG | — | ✅ |
| 62 | RemitMethodCode | REMIT_METHOD_CODE | — | ✅ |

### [[ar_receipt_methods|AR_RECEIPT_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArReceiptMethodAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ArReceiptMethodAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ArReceiptMethodAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ArReceiptMethodAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ArReceiptMethodAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ArReceiptMethodAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ArReceiptMethodAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ArReceiptMethodAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ArReceiptMethodAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ArReceiptMethodAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ArReceiptMethodAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ArReceiptMethodAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ArReceiptMethodAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ArReceiptMethodAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ArReceiptMethodAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ArReceiptMethodAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ArReceiptMethodAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | ✅ |
| 18 | ArReceiptMethodAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | ✅ |
| 19 | ArReceiptMethodBrCustTrxTypeId | BR_CUST_TRX_TYPE_ID | — | ✅ |
| 20 | ArReceiptMethodBrInheritInvNumFlag | BR_INHERIT_INV_NUM_FLAG | — | ✅ |
| 21 | ArReceiptMethodBrMaxAcctdAmount | BR_MAX_ACCTD_AMOUNT | — | ✅ |
| 22 | ArReceiptMethodBrMinAcctdAmount | BR_MIN_ACCTD_AMOUNT | — | ✅ |
| 23 | ArReceiptMethodCreatedBy | CREATED_BY | — | ✅ |
| 24 | ArReceiptMethodCreationDate | CREATION_DATE | — | ✅ |
| 25 | ArReceiptMethodDmInheritReceiptNumFlag | DM_INHERIT_RECEIPT_NUM_FLAG | — | ✅ |
| 26 | ArReceiptMethodEndDate | END_DATE | — | ✅ |
| 27 | ArReceiptMethodGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 28 | ArReceiptMethodGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 29 | ArReceiptMethodGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 30 | ArReceiptMethodGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 31 | ArReceiptMethodGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 32 | ArReceiptMethodGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 33 | ArReceiptMethodGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 34 | ArReceiptMethodGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 35 | ArReceiptMethodGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 36 | ArReceiptMethodGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 37 | ArReceiptMethodGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 38 | ArReceiptMethodGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 39 | ArReceiptMethodGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 40 | ArReceiptMethodGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 41 | ArReceiptMethodGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 42 | ArReceiptMethodGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 43 | ArReceiptMethodGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 44 | ArReceiptMethodGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 45 | ArReceiptMethodGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 46 | ArReceiptMethodGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 47 | ArReceiptMethodGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 48 | ArReceiptMethodIso20022DirectDebitFlag | ISO20022_DIRECT_DEBIT_FLAG | — | ✅ |
| 49 | ArReceiptMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | ArReceiptMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | ArReceiptMethodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | ArReceiptMethodLeadDays | LEAD_DAYS | — | ✅ |
| 53 | ArReceiptMethodMaturityDateRuleCode | MATURITY_DATE_RULE_CODE | — | ✅ |
| 54 | ArReceiptMethodMerchantId | MERCHANT_ID | — | ✅ |
| 55 | ArReceiptMethodMerchantRef | MERCHANT_REF | — | ✅ |
| 56 | ArReceiptMethodName | NAME | — | ✅ |
| 57 | ArReceiptMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 58 | ArReceiptMethodPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | ✅ |
| 59 | ArReceiptMethodPaymentTypeCode | PAYMENT_TYPE_CODE | — | ✅ |
| 60 | ArReceiptMethodPrintedName | PRINTED_NAME | — | ✅ |
| 61 | ArReceiptMethodReceiptClassId | RECEIPT_CLASS_ID | — | ✅ |
| 62 | ArReceiptMethodReceiptCreationRuleCode | RECEIPT_CREATION_RULE_CODE | — | ✅ |
| 63 | ArReceiptMethodReceiptInheritInvNumFlag | RECEIPT_INHERIT_INV_NUM_FLAG | — | ✅ |
| 64 | ArReceiptMethodReceiptMethodId | RECEIPT_METHOD_ID | 🔑 | ✅ |
| 65 | ArReceiptMethodSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 66 | ArReceiptMethodStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
