---
id: DOC-OTHER-PVO-DisbursementHeaderExtractPVO
doc_type: system-doc
title: "DisbursementHeaderExtractPVO — PVO Cross-Module"
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
  - DisbursementHeaderExtractPVO
  - disbursementheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DisbursementHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Disbursement Header Extract. Acessa as tabelas: AP_CHECKS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.DisbursementHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 158 | 1 | 1 | 101 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[ap_checks_all|AP_CHECKS_ALL]] — 158 atributos (1 PKs, 101 BICC)

---

## ⚙️ Atributos

### [[ap_checks_all|AP_CHECKS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApChecksAllActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 2 | ApChecksAllAddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 3 | ApChecksAllAddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 4 | ApChecksAllAddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 5 | ApChecksAllAddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 6 | ApChecksAllAddressStyle | ADDRESS_STYLE | — | ✅ |
| 7 | ApChecksAllAmount | AMOUNT | — | ✅ |
| 8 | ApChecksAllAnticipatedValueDate | ANTICIPATED_VALUE_DATE | — | ✅ |
| 9 | ApChecksAllAttribute1 | ATTRIBUTE1 | — | — |
| 10 | ApChecksAllAttribute10 | ATTRIBUTE10 | — | — |
| 11 | ApChecksAllAttribute11 | ATTRIBUTE11 | — | — |
| 12 | ApChecksAllAttribute12 | ATTRIBUTE12 | — | — |
| 13 | ApChecksAllAttribute13 | ATTRIBUTE13 | — | — |
| 14 | ApChecksAllAttribute14 | ATTRIBUTE14 | — | — |
| 15 | ApChecksAllAttribute15 | ATTRIBUTE15 | — | — |
| 16 | ApChecksAllAttribute2 | ATTRIBUTE2 | — | — |
| 17 | ApChecksAllAttribute3 | ATTRIBUTE3 | — | — |
| 18 | ApChecksAllAttribute4 | ATTRIBUTE4 | — | — |
| 19 | ApChecksAllAttribute5 | ATTRIBUTE5 | — | — |
| 20 | ApChecksAllAttribute6 | ATTRIBUTE6 | — | — |
| 21 | ApChecksAllAttribute7 | ATTRIBUTE7 | — | — |
| 22 | ApChecksAllAttribute8 | ATTRIBUTE8 | — | — |
| 23 | ApChecksAllAttribute9 | ATTRIBUTE9 | — | — |
| 24 | ApChecksAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | ApChecksAllAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | ApChecksAllAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | ApChecksAllAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | ApChecksAllAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | ApChecksAllAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | ApChecksAllAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 31 | ApChecksAllAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | ApChecksAllAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | ApChecksAllAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | ApChecksAllAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | ApChecksAllBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 36 | ApChecksAllBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 37 | ApChecksAllBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 38 | ApChecksAllBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 39 | ApChecksAllBankNum | BANK_NUM | — | ✅ |
| 40 | ApChecksAllBaseAmount | BASE_AMOUNT | — | ✅ |
| 41 | ApChecksAllCeBankAcctUseId | CE_BANK_ACCT_USE_ID | — | ✅ |
| 42 | ApChecksAllCheckDate | CHECK_DATE | — | ✅ |
| 43 | ApChecksAllCheckFormatId | CHECK_FORMAT_ID | — | ✅ |
| 44 | ApChecksAllCheckId | CHECK_ID | 🔑 | ✅ |
| 45 | ApChecksAllCheckNumber | CHECK_NUMBER | — | ✅ |
| 46 | ApChecksAllCheckStockId | CHECK_STOCK_ID | — | ✅ |
| 47 | ApChecksAllCheckVoucherNum | CHECK_VOUCHER_NUM | — | ✅ |
| 48 | ApChecksAllCheckrunId | CHECKRUN_ID | — | ✅ |
| 49 | ApChecksAllCheckrunName | CHECKRUN_NAME | — | ✅ |
| 50 | ApChecksAllCity | CITY | — | ✅ |
| 51 | ApChecksAllClearedAmount | CLEARED_AMOUNT | — | ✅ |
| 52 | ApChecksAllClearedBaseAmount | CLEARED_BASE_AMOUNT | — | ✅ |
| 53 | ApChecksAllClearedChargesAmount | CLEARED_CHARGES_AMOUNT | — | ✅ |
| 54 | ApChecksAllClearedChargesBaseAmount | CLEARED_CHARGES_BASE_AMOUNT | — | ✅ |
| 55 | ApChecksAllClearedDate | CLEARED_DATE | — | ✅ |
| 56 | ApChecksAllClearedErrorAmount | CLEARED_ERROR_AMOUNT | — | ✅ |
| 57 | ApChecksAllClearedErrorBaseAmount | CLEARED_ERROR_BASE_AMOUNT | — | ✅ |
| 58 | ApChecksAllClearedExchangeDate | CLEARED_EXCHANGE_DATE | — | ✅ |
| 59 | ApChecksAllClearedExchangeRate | CLEARED_EXCHANGE_RATE | — | ✅ |
| 60 | ApChecksAllClearedExchangeRateType | CLEARED_EXCHANGE_RATE_TYPE | — | ✅ |
| 61 | ApChecksAllCompletedPmtsGroupId | COMPLETED_PMTS_GROUP_ID | — | ✅ |
| 62 | ApChecksAllCountry | COUNTRY | — | ✅ |
| 63 | ApChecksAllCounty | COUNTY | — | ✅ |
| 64 | ApChecksAllCreatedBy | CREATED_BY | — | ✅ |
| 65 | ApChecksAllCreationDate | CREATION_DATE | — | ✅ |
| 66 | ApChecksAllCurrencyCode | CURRENCY_CODE | — | ✅ |
| 67 | ApChecksAllDescription | DESCRIPTION | — | ✅ |
| 68 | ApChecksAllDocCategoryCode | DOC_CATEGORY_CODE | — | ✅ |
| 69 | ApChecksAllDocSequenceId | DOC_SEQUENCE_ID | — | ✅ |
| 70 | ApChecksAllDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 71 | ApChecksAllEmployeeAddressCode | EMPLOYEE_ADDRESS_CODE | — | ✅ |
| 72 | ApChecksAllExchangeDate | EXCHANGE_DATE | — | ✅ |
| 73 | ApChecksAllExchangeRate | EXCHANGE_RATE | — | ✅ |
| 74 | ApChecksAllExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 75 | ApChecksAllExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | ✅ |
| 76 | ApChecksAllFuturePayDueDate | FUTURE_PAY_DUE_DATE | — | ✅ |
| 77 | ApChecksAllGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 78 | ApChecksAllGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 79 | ApChecksAllGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 80 | ApChecksAllGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 81 | ApChecksAllGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 82 | ApChecksAllGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 83 | ApChecksAllGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 84 | ApChecksAllGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 85 | ApChecksAllGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 86 | ApChecksAllGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 87 | ApChecksAllGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 88 | ApChecksAllGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 89 | ApChecksAllGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 90 | ApChecksAllGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 91 | ApChecksAllGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 92 | ApChecksAllGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 93 | ApChecksAllGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 94 | ApChecksAllGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 95 | ApChecksAllGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 96 | ApChecksAllGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 97 | ApChecksAllGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 98 | ApChecksAllGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 99 | ApChecksAllGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 100 | ApChecksAllGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 101 | ApChecksAllGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 102 | ApChecksAllGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 103 | ApChecksAllGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 104 | ApChecksAllGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 105 | ApChecksAllGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 106 | ApChecksAllGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 107 | ApChecksAllGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 108 | ApChecksAllIbanNumber | IBAN_NUMBER | — | ✅ |
| 109 | ApChecksAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 110 | ApChecksAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 111 | ApChecksAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 112 | ApChecksAllLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 113 | ApChecksAllLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | ✅ |
| 114 | ApChecksAllMaturityExchangeDate | MATURITY_EXCHANGE_DATE | — | ✅ |
| 115 | ApChecksAllMaturityExchangeRate | MATURITY_EXCHANGE_RATE | — | ✅ |
| 116 | ApChecksAllMaturityExchangeRateType | MATURITY_EXCHANGE_RATE_TYPE | — | ✅ |
| 117 | ApChecksAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | ApChecksAllOrgId | ORG_ID | — | ✅ |
| 119 | ApChecksAllPartyId | PARTY_ID | — | ✅ |
| 120 | ApChecksAllPartySiteId | PARTY_SITE_ID | — | ✅ |
| 121 | ApChecksAllPaymentDocumentId | PAYMENT_DOCUMENT_ID | — | ✅ |
| 122 | ApChecksAllPaymentId | PAYMENT_ID | — | ✅ |
| 123 | ApChecksAllPaymentInstructionId | PAYMENT_INSTRUCTION_ID | — | ✅ |
| 124 | ApChecksAllPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 125 | ApChecksAllPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | ✅ |
| 126 | ApChecksAllPaymentProfileId | PAYMENT_PROFILE_ID | — | ✅ |
| 127 | ApChecksAllPaymentTypeFlag | PAYMENT_TYPE_FLAG | — | ✅ |
| 128 | ApChecksAllPositivePayStatusCode | POSITIVE_PAY_STATUS_CODE | — | ✅ |
| 129 | ApChecksAllProvince | PROVINCE | — | ✅ |
| 130 | ApChecksAllReconFlag | RECON_FLAG | — | ✅ |
| 131 | ApChecksAllReconciliationBatchId | RECONCILIATION_BATCH_ID | — | ✅ |
| 132 | ApChecksAllRelationshipId | RELATIONSHIP_ID | — | ✅ |
| 133 | ApChecksAllReleasedBy | RELEASED_BY | — | ✅ |
| 134 | ApChecksAllReleasedDate | RELEASED_DATE | — | ✅ |
| 135 | ApChecksAllRemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 136 | ApChecksAllRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 137 | ApChecksAllRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 138 | ApChecksAllRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 139 | ApChecksAllRequestId | REQUEST_ID | — | ✅ |
| 140 | ApChecksAllSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 141 | ApChecksAllStampDutyAmt | STAMP_DUTY_AMT | — | ✅ |
| 142 | ApChecksAllStampDutyBaseAmt | STAMP_DUTY_BASE_AMT | — | ✅ |
| 143 | ApChecksAllState | STATE | — | ✅ |
| 144 | ApChecksAllStatusLookupCode | STATUS_LOOKUP_CODE | — | ✅ |
| 145 | ApChecksAllStoppedBy | STOPPED_BY | — | ✅ |
| 146 | ApChecksAllStoppedDate | STOPPED_DATE | — | ✅ |
| 147 | ApChecksAllTransferPriority | TRANSFER_PRIORITY | — | ✅ |
| 148 | ApChecksAllTreasuryPayDate | TREASURY_PAY_DATE | — | ✅ |
| 149 | ApChecksAllTreasuryPayNumber | TREASURY_PAY_NUMBER | — | ✅ |
| 150 | ApChecksAllUssglTransactionCode | USSGL_TRANSACTION_CODE | — | ✅ |
| 151 | ApChecksAllUssglTrxCodeContext | USSGL_TRX_CODE_CONTEXT | — | ✅ |
| 152 | ApChecksAllVendorId | VENDOR_ID | — | ✅ |
| 153 | ApChecksAllVendorName | VENDOR_NAME | — | ✅ |
| 154 | ApChecksAllVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 155 | ApChecksAllVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 156 | ApChecksAllVoidDate | VOID_DATE | — | ✅ |
| 157 | ApChecksAllXCurrRateType | X_CURR_RATE_TYPE | — | ✅ |
| 158 | ApChecksAllZip | ZIP | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
