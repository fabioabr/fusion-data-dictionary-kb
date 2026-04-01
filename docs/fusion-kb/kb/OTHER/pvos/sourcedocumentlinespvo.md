---
id: DOC-OTHER-PVO-SourceDocumentLinesPVO
doc_type: system-doc
title: "SourceDocumentLinesPVO — PVO Cross-Module"
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
  - SourceDocumentLinesPVO
  - sourcedocumentlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceDocumentLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Source Document Lines. Acessa as tabelas: FND_APPLICATION_VL, HZ_CUST_ACCOUNTS, HZ_CUST_SITE_USES_ALL (+2).

**Caminho:** `FscmTopModelAM.FinVrmRCSharedPublicModelAM.SourceDocumentLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 511 | 5 | 1 | 37 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_application_vl|FND_APPLICATION_VL]] — 3 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 64 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 168 atributos
- [[vrm_source_documents|VRM_SOURCE_DOCUMENTS]] — 98 atributos (9 BICC)
- [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]] — 178 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[fnd_application_vl|FND_APPLICATION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | ApplicationPEOApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | ApplicationPEOApplicationShortName | APPLICATION_SHORT_NAME | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipToCustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | ShipToCustomerAccountAccountName | ACCOUNT_NAME | — | — |
| 3 | ShipToCustomerAccountAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | ShipToCustomerAccountAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | — |
| 5 | ShipToCustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 6 | ShipToCustomerAccountAutopayFlag | AUTOPAY_FLAG | — | — |
| 7 | ShipToCustomerAccountComments | COMMENTS | — | — |
| 8 | ShipToCustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 9 | ShipToCustomerAccountCreatedBy | CREATED_BY | — | — |
| 10 | ShipToCustomerAccountCreatedByModule | CREATED_BY_MODULE | — | — |
| 11 | ShipToCustomerAccountCreationDate | CREATION_DATE | — | — |
| 12 | ShipToCustomerAccountCustAccountId | CUST_ACCOUNT_ID | — | — |
| 13 | ShipToCustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 14 | ShipToCustomerAccountCustomerType | CUSTOMER_TYPE | — | — |
| 15 | ShipToCustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 16 | ShipToCustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 17 | ShipToCustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 18 | ShipToCustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 19 | ShipToCustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 20 | ShipToCustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 21 | ShipToCustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | ShipToCustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | ShipToCustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 24 | ShipToCustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 25 | ShipToCustomerAccountPartyId | PARTY_ID | — | — |
| 26 | ShipToCustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 27 | ShipToCustomerAccountSourceCode | SOURCE_CODE | — | — |
| 28 | ShipToCustomerAccountStatus | STATUS | — | — |
| 29 | ShipToCustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 30 | ShipToCustomerAccountTaxCode | TAX_CODE | — | — |
| 31 | ShipToCustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 32 | ShipToCustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 33 | ShipToLineCustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 34 | ShipToLineCustomerAccountAccountName | ACCOUNT_NAME | — | — |
| 35 | ShipToLineCustomerAccountAccountNumber | ACCOUNT_NUMBER | — | — |
| 36 | ShipToLineCustomerAccountAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | — |
| 37 | ShipToLineCustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 38 | ShipToLineCustomerAccountAutopayFlag | AUTOPAY_FLAG | — | — |
| 39 | ShipToLineCustomerAccountComments | COMMENTS | — | — |
| 40 | ShipToLineCustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 41 | ShipToLineCustomerAccountCreatedBy | CREATED_BY | — | — |
| 42 | ShipToLineCustomerAccountCreatedByModule | CREATED_BY_MODULE | — | — |
| 43 | ShipToLineCustomerAccountCreationDate | CREATION_DATE | — | — |
| 44 | ShipToLineCustomerAccountCustAccountId | CUST_ACCOUNT_ID | — | — |
| 45 | ShipToLineCustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 46 | ShipToLineCustomerAccountCustomerType | CUSTOMER_TYPE | — | — |
| 47 | ShipToLineCustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 48 | ShipToLineCustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 49 | ShipToLineCustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 50 | ShipToLineCustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 51 | ShipToLineCustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 52 | ShipToLineCustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 53 | ShipToLineCustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | ShipToLineCustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | ShipToLineCustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 56 | ShipToLineCustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 57 | ShipToLineCustomerAccountPartyId | PARTY_ID | — | — |
| 58 | ShipToLineCustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 59 | ShipToLineCustomerAccountSourceCode | SOURCE_CODE | — | — |
| 60 | ShipToLineCustomerAccountStatus | STATUS | — | — |
| 61 | ShipToLineCustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 62 | ShipToLineCustomerAccountTaxCode | TAX_CODE | — | — |
| 63 | ShipToLineCustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 64 | ShipToLineCustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToCustomerAccountSiteUseBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 2 | BillToCustomerAccountSiteUseCreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | BillToCustomerAccountSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 4 | BillToCustomerAccountSiteUseEndDate | END_DATE | — | — |
| 5 | BillToCustomerAccountSiteUseFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 6 | BillToCustomerAccountSiteUseGsaIndicator | GSA_INDICATOR | — | — |
| 7 | BillToCustomerAccountSiteUseLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 8 | BillToCustomerAccountSiteUseLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 9 | BillToCustomerAccountSiteUseLocation | LOCATION | — | — |
| 10 | BillToCustomerAccountSiteUseOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 11 | BillToCustomerAccountSiteUsePaymentTermId | PAYMENT_TERM_ID | — | — |
| 12 | BillToCustomerAccountSiteUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 13 | BillToCustomerAccountSiteUseSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 14 | BillToCustomerAccountSiteUseSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 15 | BillToCustomerAccountSiteUseSetId | SET_ID | — | — |
| 16 | BillToCustomerAccountSiteUseSicCode | SIC_CODE | — | — |
| 17 | BillToCustomerAccountSiteUseSiteUseCode | SITE_USE_CODE | — | — |
| 18 | BillToCustomerAccountSiteUseSiteUseId | SITE_USE_ID | — | — |
| 19 | BillToCustomerAccountSiteUseSortPriority | SORT_PRIORITY | — | — |
| 20 | BillToCustomerAccountSiteUseStartDate | START_DATE | — | — |
| 21 | BillToCustomerAccountSiteUseStatus | STATUS | — | — |
| 22 | BillToCustomerAccountSiteUseTaxClassification | TAX_CLASSIFICATION | — | — |
| 23 | BillToCustomerAccountSiteUseTaxCode | TAX_CODE | — | — |
| 24 | BillToCustomerAccountSiteUseTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 25 | BillToCustomerAccountSiteUseTaxReference | TAX_REFERENCE | — | — |
| 26 | BillToCustomerAccountSiteUseTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 27 | BillToCustomerAccountSiteUseTerritoryId | TERRITORY_ID | — | — |
| 28 | BillToLineCustAcctSiteUseAttribute1 | ATTRIBUTE1 | — | — |
| 29 | BillToLineCustAcctSiteUseAttribute10 | ATTRIBUTE10 | — | — |
| 30 | BillToLineCustAcctSiteUseAttribute11 | ATTRIBUTE11 | — | — |
| 31 | BillToLineCustAcctSiteUseAttribute12 | ATTRIBUTE12 | — | — |
| 32 | BillToLineCustAcctSiteUseAttribute13 | ATTRIBUTE13 | — | — |
| 33 | BillToLineCustAcctSiteUseAttribute14 | ATTRIBUTE14 | — | — |
| 34 | BillToLineCustAcctSiteUseAttribute15 | ATTRIBUTE15 | — | — |
| 35 | BillToLineCustAcctSiteUseAttribute16 | ATTRIBUTE16 | — | — |
| 36 | BillToLineCustAcctSiteUseAttribute17 | ATTRIBUTE17 | — | — |
| 37 | BillToLineCustAcctSiteUseAttribute18 | ATTRIBUTE18 | — | — |
| 38 | BillToLineCustAcctSiteUseAttribute19 | ATTRIBUTE19 | — | — |
| 39 | BillToLineCustAcctSiteUseAttribute2 | ATTRIBUTE2 | — | — |
| 40 | BillToLineCustAcctSiteUseAttribute20 | ATTRIBUTE20 | — | — |
| 41 | BillToLineCustAcctSiteUseAttribute21 | ATTRIBUTE21 | — | — |
| 42 | BillToLineCustAcctSiteUseAttribute22 | ATTRIBUTE22 | — | — |
| 43 | BillToLineCustAcctSiteUseAttribute23 | ATTRIBUTE23 | — | — |
| 44 | BillToLineCustAcctSiteUseAttribute24 | ATTRIBUTE24 | — | — |
| 45 | BillToLineCustAcctSiteUseAttribute25 | ATTRIBUTE25 | — | — |
| 46 | BillToLineCustAcctSiteUseAttribute26 | ATTRIBUTE26 | — | — |
| 47 | BillToLineCustAcctSiteUseAttribute27 | ATTRIBUTE27 | — | — |
| 48 | BillToLineCustAcctSiteUseAttribute28 | ATTRIBUTE28 | — | — |
| 49 | BillToLineCustAcctSiteUseAttribute29 | ATTRIBUTE29 | — | — |
| 50 | BillToLineCustAcctSiteUseAttribute3 | ATTRIBUTE3 | — | — |
| 51 | BillToLineCustAcctSiteUseAttribute30 | ATTRIBUTE30 | — | — |
| 52 | BillToLineCustAcctSiteUseAttribute4 | ATTRIBUTE4 | — | — |
| 53 | BillToLineCustAcctSiteUseAttribute5 | ATTRIBUTE5 | — | — |
| 54 | BillToLineCustAcctSiteUseAttribute6 | ATTRIBUTE6 | — | — |
| 55 | BillToLineCustAcctSiteUseAttribute7 | ATTRIBUTE7 | — | — |
| 56 | BillToLineCustAcctSiteUseAttribute8 | ATTRIBUTE8 | — | — |
| 57 | BillToLineCustAcctSiteUseAttribute9 | ATTRIBUTE9 | — | — |
| 58 | BillToLineCustAcctSiteUseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 59 | BillToLineCustAcctSiteUseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 60 | BillToLineCustAcctSiteUseAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 61 | BillToLineCustAcctSiteUseAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 62 | BillToLineCustAcctSiteUseAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 63 | BillToLineCustAcctSiteUseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 64 | BillToLineCustAcctSiteUseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 65 | BillToLineCustAcctSiteUseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 66 | BillToLineCustAcctSiteUseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 67 | BillToLineCustAcctSiteUseAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 68 | BillToLineCustAcctSiteUseAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 69 | BillToLineCustAcctSiteUseAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 70 | BillToLineCustAcctSiteUseAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 71 | BillToLineCustAcctSiteUseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 72 | BillToLineCustAcctSiteUseAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 73 | BillToLineCustAcctSiteUseAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 74 | BillToLineCustAcctSiteUseAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 75 | BillToLineCustAcctSiteUseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 76 | BillToLineCustAcctSiteUseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 77 | BillToLineCustAcctSiteUseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 78 | BillToLineCustAcctSiteUseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 79 | BillToLineCustAcctSiteUseAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 80 | BillToLineCustAcctSiteUseAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 81 | BillToLineCustAcctSiteUseAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 82 | BillToLineCustAcctSiteUseAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 83 | BillToLineCustAcctSiteUseBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 84 | BillToLineCustAcctSiteUseCreatedBy | CREATED_BY | — | — |
| 85 | BillToLineCustAcctSiteUseCreatedByModule | CREATED_BY_MODULE | — | — |
| 86 | BillToLineCustAcctSiteUseCreationDate | CREATION_DATE | — | — |
| 87 | BillToLineCustAcctSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 88 | BillToLineCustAcctSiteUseEndDate | END_DATE | — | — |
| 89 | BillToLineCustAcctSiteUseFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 90 | BillToLineCustAcctSiteUseGsaIndicator | GSA_INDICATOR | — | — |
| 91 | BillToLineCustAcctSiteUseLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 92 | BillToLineCustAcctSiteUseLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 93 | BillToLineCustAcctSiteUseLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 94 | BillToLineCustAcctSiteUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 95 | BillToLineCustAcctSiteUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 96 | BillToLineCustAcctSiteUseLocation | LOCATION | — | — |
| 97 | BillToLineCustAcctSiteUseOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 98 | BillToLineCustAcctSiteUsePaymentTermId | PAYMENT_TERM_ID | — | — |
| 99 | BillToLineCustAcctSiteUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 100 | BillToLineCustAcctSiteUseSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 101 | BillToLineCustAcctSiteUseSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 102 | BillToLineCustAcctSiteUseSetId | SET_ID | — | — |
| 103 | BillToLineCustAcctSiteUseSicCode | SIC_CODE | — | — |
| 104 | BillToLineCustAcctSiteUseSiteUseCode | SITE_USE_CODE | — | — |
| 105 | BillToLineCustAcctSiteUseSiteUseId | SITE_USE_ID | — | — |
| 106 | BillToLineCustAcctSiteUseSortPriority | SORT_PRIORITY | — | — |
| 107 | BillToLineCustAcctSiteUseStartDate | START_DATE | — | — |
| 108 | BillToLineCustAcctSiteUseStatus | STATUS | — | — |
| 109 | BillToLineCustAcctSiteUseTaxClassification | TAX_CLASSIFICATION | — | — |
| 110 | BillToLineCustAcctSiteUseTaxCode | TAX_CODE | — | — |
| 111 | BillToLineCustAcctSiteUseTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 112 | BillToLineCustAcctSiteUseTaxReference | TAX_REFERENCE | — | — |
| 113 | BillToLineCustAcctSiteUseTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 114 | BillToLineCustAcctSiteUseTerritoryId | TERRITORY_ID | — | — |
| 115 | ShipToCustomerAccountSiteUseBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 116 | ShipToCustomerAccountSiteUseCreatedByModule | CREATED_BY_MODULE | — | — |
| 117 | ShipToCustomerAccountSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 118 | ShipToCustomerAccountSiteUseEndDate | END_DATE | — | — |
| 119 | ShipToCustomerAccountSiteUseFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 120 | ShipToCustomerAccountSiteUseGsaIndicator | GSA_INDICATOR | — | — |
| 121 | ShipToCustomerAccountSiteUseLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 122 | ShipToCustomerAccountSiteUseLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 123 | ShipToCustomerAccountSiteUseLocation | LOCATION | — | — |
| 124 | ShipToCustomerAccountSiteUseOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 125 | ShipToCustomerAccountSiteUsePaymentTermId | PAYMENT_TERM_ID | — | — |
| 126 | ShipToCustomerAccountSiteUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 127 | ShipToCustomerAccountSiteUseSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 128 | ShipToCustomerAccountSiteUseSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 129 | ShipToCustomerAccountSiteUseSetId | SET_ID | — | — |
| 130 | ShipToCustomerAccountSiteUseSicCode | SIC_CODE | — | — |
| 131 | ShipToCustomerAccountSiteUseSiteUseCode | SITE_USE_CODE | — | — |
| 132 | ShipToCustomerAccountSiteUseSiteUseId | SITE_USE_ID | — | — |
| 133 | ShipToCustomerAccountSiteUseSortPriority | SORT_PRIORITY | — | — |
| 134 | ShipToCustomerAccountSiteUseStartDate | START_DATE | — | — |
| 135 | ShipToCustomerAccountSiteUseStatus | STATUS | — | — |
| 136 | ShipToCustomerAccountSiteUseTaxClassification | TAX_CLASSIFICATION | — | — |
| 137 | ShipToCustomerAccountSiteUseTaxCode | TAX_CODE | — | — |
| 138 | ShipToCustomerAccountSiteUseTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 139 | ShipToCustomerAccountSiteUseTaxReference | TAX_REFERENCE | — | — |
| 140 | ShipToCustomerAccountSiteUseTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 141 | ShipToCustomerAccountSiteUseTerritoryId | TERRITORY_ID | — | — |
| 142 | ShipToLineCustAccountSiteUseBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 143 | ShipToLineCustAccountSiteUseCreatedByModule | CREATED_BY_MODULE | — | — |
| 144 | ShipToLineCustAccountSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 145 | ShipToLineCustAccountSiteUseEndDate | END_DATE | — | — |
| 146 | ShipToLineCustAccountSiteUseFinchrgReceivablesTrxId | FINCHRG_RECEIVABLES_TRX_ID | — | — |
| 147 | ShipToLineCustAccountSiteUseGsaIndicator | GSA_INDICATOR | — | — |
| 148 | ShipToLineCustAccountSiteUseLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 149 | ShipToLineCustAccountSiteUseLastUnaccrueChargeDate | LAST_UNACCRUE_CHARGE_DATE | — | — |
| 150 | ShipToLineCustAccountSiteUseLocation | LOCATION | — | — |
| 151 | ShipToLineCustAccountSiteUseOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 152 | ShipToLineCustAccountSiteUsePaymentTermId | PAYMENT_TERM_ID | — | — |
| 153 | ShipToLineCustAccountSiteUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 154 | ShipToLineCustAccountSiteUseSecondLastAccrueChargeDate | SECOND_LAST_ACCRUE_CHARGE_DATE | — | — |
| 155 | ShipToLineCustAccountSiteUseSecondLastUnaccrueChrgDate | SECOND_LAST_UNACCRUE_CHRG_DATE | — | — |
| 156 | ShipToLineCustAccountSiteUseSetId | SET_ID | — | — |
| 157 | ShipToLineCustAccountSiteUseSicCode | SIC_CODE | — | — |
| 158 | ShipToLineCustAccountSiteUseSiteUseCode | SITE_USE_CODE | — | — |
| 159 | ShipToLineCustAccountSiteUseSiteUseId | SITE_USE_ID | — | — |
| 160 | ShipToLineCustAccountSiteUseSortPriority | SORT_PRIORITY | — | — |
| 161 | ShipToLineCustAccountSiteUseStartDate | START_DATE | — | — |
| 162 | ShipToLineCustAccountSiteUseStatus | STATUS | — | — |
| 163 | ShipToLineCustAccountSiteUseTaxClassification | TAX_CLASSIFICATION | — | — |
| 164 | ShipToLineCustAccountSiteUseTaxCode | TAX_CODE | — | — |
| 165 | ShipToLineCustAccountSiteUseTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 166 | ShipToLineCustAccountSiteUseTaxReference | TAX_REFERENCE | — | — |
| 167 | ShipToLineCustAccountSiteUseTaxRoundingRule | TAX_ROUNDING_RULE | — | — |
| 168 | ShipToLineCustAccountSiteUseTerritoryId | TERRITORY_ID | — | — |

### [[vrm_source_documents|VRM_SOURCE_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocumentsAccountingEffectFlag | ACCOUNTING_EFFECT_FLAG | — | — |
| 2 | SourceDocumentsAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 3 | SourceDocumentsAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 4 | SourceDocumentsApplicationId | APPLICATION_ID | — | — |
| 5 | SourceDocumentsBillToCountry | BILL_TO_COUNTRY | — | — |
| 6 | SourceDocumentsBillToCustClassification | BILL_TO_CUST_CLASSIFICATION | — | — |
| 7 | SourceDocumentsBillToCustSiteName | BILL_TO_CUST_SITE_NAME | — | — |
| 8 | SourceDocumentsBillToCustomerCity | BILL_TO_CUSTOMER_CITY | — | — |
| 9 | SourceDocumentsBillToCustomerCounty | BILL_TO_CUSTOMER_COUNTY | — | — |
| 10 | SourceDocumentsBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 11 | SourceDocumentsBillToCustomerName | BILL_TO_CUSTOMER_NAME | — | — |
| 12 | SourceDocumentsBillToCustomerNum | BILL_TO_CUSTOMER_NUM | — | — |
| 13 | SourceDocumentsBillToCustomerPartyId | BILL_TO_CUSTOMER_PARTY_ID | — | — |
| 14 | SourceDocumentsBillToCustomerPartyName | BILL_TO_CUSTOMER_PARTY_NAME | — | — |
| 15 | SourceDocumentsBillToCustomerPartyNum | BILL_TO_CUSTOMER_PARTY_NUM | — | — |
| 16 | SourceDocumentsBillToCustomerPostalCode | BILL_TO_CUSTOMER_POSTAL_CODE | — | — |
| 17 | SourceDocumentsBillToCustomerSiteId | BILL_TO_CUSTOMER_SITE_ID | — | — |
| 18 | SourceDocumentsBillToCustomerState | BILL_TO_CUSTOMER_STATE | — | — |
| 19 | SourceDocumentsCancelledFlag | CANCELLED_FLAG | — | — |
| 20 | SourceDocumentsCreatedBy | CREATED_BY | — | — |
| 21 | SourceDocumentsCreationDate | CREATION_DATE | — | — |
| 22 | SourceDocumentsCurrencyCode | CURRENCY_CODE | — | ✅ |
| 23 | SourceDocumentsCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 24 | SourceDocumentsCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | — |
| 25 | SourceDocumentsDataTransErrorMessage | DATA_TRANS_ERROR_MESSAGE | — | — |
| 26 | SourceDocumentsDataTransformationStatus | DATA_TRANSFORMATION_STATUS | — | — |
| 27 | SourceDocumentsDocIdChar1 | DOC_ID_CHAR_1 | — | — |
| 28 | SourceDocumentsDocIdChar2 | DOC_ID_CHAR_2 | — | — |
| 29 | SourceDocumentsDocIdChar3 | DOC_ID_CHAR_3 | — | — |
| 30 | SourceDocumentsDocIdChar4 | DOC_ID_CHAR_4 | — | — |
| 31 | SourceDocumentsDocIdChar5 | DOC_ID_CHAR_5 | — | — |
| 32 | SourceDocumentsDocIdInt1 | DOC_ID_INT_1 | — | — |
| 33 | SourceDocumentsDocIdInt2 | DOC_ID_INT_2 | — | — |
| 34 | SourceDocumentsDocIdInt3 | DOC_ID_INT_3 | — | — |
| 35 | SourceDocumentsDocIdInt4 | DOC_ID_INT_4 | — | — |
| 36 | SourceDocumentsDocIdInt5 | DOC_ID_INT_5 | — | — |
| 37 | SourceDocumentsDocumentCreationDate | DOCUMENT_CREATION_DATE | — | — |
| 38 | SourceDocumentsDocumentDate | DOCUMENT_DATE | — | ✅ |
| 39 | SourceDocumentsDocumentId | DOCUMENT_ID | — | — |
| 40 | SourceDocumentsDocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 41 | SourceDocumentsDocumentType | DOCUMENT_TYPE | — | — |
| 42 | SourceDocumentsDocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 43 | SourceDocumentsDocumentUpdateDate | DOCUMENT_UPDATE_DATE | — | — |
| 44 | SourceDocumentsExchangeDate | EXCHANGE_DATE | — | — |
| 45 | SourceDocumentsExchangeRate | EXCHANGE_RATE | — | — |
| 46 | SourceDocumentsExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 47 | SourceDocumentsInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 48 | SourceDocumentsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | SourceDocumentsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | SourceDocumentsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | SourceDocumentsLedgerId | LEDGER_ID | — | — |
| 52 | SourceDocumentsLedgerName | LEDGER_NAME | — | — |
| 53 | SourceDocumentsLegalEntityAddress | LEGAL_ENTITY_ADDRESS | — | — |
| 54 | SourceDocumentsLegalEntityCountry | LEGAL_ENTITY_COUNTRY | — | — |
| 55 | SourceDocumentsLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 56 | SourceDocumentsLegalEntityName | LEGAL_ENTITY_NAME | — | — |
| 57 | SourceDocumentsLoadRequestId | LOAD_REQUEST_ID | — | — |
| 58 | SourceDocumentsMeaFlag | MEA_FLAG | — | — |
| 59 | SourceDocumentsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 60 | SourceDocumentsOpenFlag | OPEN_FLAG | — | — |
| 61 | SourceDocumentsOrgId | ORG_ID | — | — |
| 62 | SourceDocumentsOrganizationName | ORGANIZATION_NAME | — | — |
| 63 | SourceDocumentsOrigSysBillToCustRef | ORIG_SYS_BILL_TO_CUST_REF | — | — |
| 64 | SourceDocumentsOrigSysBillToCustSiteRef | ORIG_SYS_BILL_TO_CUST_SITE_REF | — | — |
| 65 | SourceDocumentsOrigSysShipToCustRef | ORIG_SYS_SHIP_TO_CUST_REF | — | — |
| 66 | SourceDocumentsOrigSysShipToCustSiteRef | ORIG_SYS_SHIP_TO_CUST_SITE_REF | — | — |
| 67 | SourceDocumentsPaymentTermId | PAYMENT_TERM_ID | — | — |
| 68 | SourceDocumentsPaymentTermName | PAYMENT_TERM_NAME | — | ✅ |
| 69 | SourceDocumentsQuoteNumber | QUOTE_NUMBER | — | — |
| 70 | SourceDocumentsRequestId | REQUEST_ID | — | — |
| 71 | SourceDocumentsReturnReasonCode | RETURN_REASON_CODE | — | — |
| 72 | SourceDocumentsSalesAgreementNumber | SALES_AGREEMENT_NUMBER | — | ✅ |
| 73 | SourceDocumentsSalesrepId | SALESREP_ID | — | — |
| 74 | SourceDocumentsSalesrepName | SALESREP_NAME | — | — |
| 75 | SourceDocumentsShipToCountry | SHIP_TO_COUNTRY | — | — |
| 76 | SourceDocumentsShipToCustSiteName | SHIP_TO_CUST_SITE_NAME | — | — |
| 77 | SourceDocumentsShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 78 | SourceDocumentsShipToCustomerName | SHIP_TO_CUSTOMER_NAME | — | — |
| 79 | SourceDocumentsShipToCustomerNum | SHIP_TO_CUSTOMER_NUM | — | — |
| 80 | SourceDocumentsShipToCustomerSiteId | SHIP_TO_CUSTOMER_SITE_ID | — | — |
| 81 | SourceDocumentsSourceBillToCustAddress | SOURCE_BILL_TO_CUST_ADDRESS | — | — |
| 82 | SourceDocumentsSourceBillToCustName | SOURCE_BILL_TO_CUST_NAME | — | — |
| 83 | SourceDocumentsSourceBillToCustNum | SOURCE_BILL_TO_CUST_NUM | — | — |
| 84 | SourceDocumentsSourceBillToCustSiteNum | SOURCE_BILL_TO_CUST_SITE_NUM | — | — |
| 85 | SourceDocumentsSourceExchangeRateType | SOURCE_EXCHANGE_RATE_TYPE | — | — |
| 86 | SourceDocumentsSourceLegalEntityName | SOURCE_LEGAL_ENTITY_NAME | — | — |
| 87 | SourceDocumentsSourceOrgId | SOURCE_ORG_ID | — | — |
| 88 | SourceDocumentsSourceOrganizationName | SOURCE_ORGANIZATION_NAME | — | — |
| 89 | SourceDocumentsSourcePaymentTermName | SOURCE_PAYMENT_TERM_NAME | — | — |
| 90 | SourceDocumentsSourceSalesrepName | SOURCE_SALESREP_NAME | — | — |
| 91 | SourceDocumentsSourceShipToCustAddress | SOURCE_SHIP_TO_CUST_ADDRESS | — | — |
| 92 | SourceDocumentsSourceShipToCustName | SOURCE_SHIP_TO_CUST_NAME | — | — |
| 93 | SourceDocumentsSourceShipToCustNum | SOURCE_SHIP_TO_CUST_NUM | — | — |
| 94 | SourceDocumentsSourceShipToCustSiteNum | SOURCE_SHIP_TO_CUST_SITE_NUM | — | — |
| 95 | SourceDocumentsSourceSystem | SOURCE_SYSTEM | — | ✅ |
| 96 | SourceDocumentsSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 97 | SourceDocumentsSrcAttributeChar1 | SRC_ATTRIBUTE_CHAR1 | — | — |
| 98 | SourceDocumentsSrcAttributeChar4 | SRC_ATTRIBUTE_CHAR4 | — | — |

### [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocLinesAcceptedBy | ACCEPTED_BY | — | — |
| 2 | SourceDocLinesAcceptedQuantity | ACCEPTED_QUANTITY | — | — |
| 3 | SourceDocLinesAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 4 | SourceDocLinesAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 5 | SourceDocLinesAccountingRuleName | ACCOUNTING_RULE_NAME | — | ✅ |
| 6 | SourceDocLinesActualArrivalDate | ACTUAL_ARRIVAL_DATE | — | — |
| 7 | SourceDocLinesActualFulfillmentDate | ACTUAL_FULFILLMENT_DATE | — | — |
| 8 | SourceDocLinesActualShipmentDate | ACTUAL_SHIPMENT_DATE | — | — |
| 9 | SourceDocLinesAddToContractActionCode | ADD_TO_CONTRACT_ACTION_CODE | — | ✅ |
| 10 | SourceDocLinesAddToContractFlag | ADD_TO_CONTRACT_FLAG | — | ✅ |
| 11 | SourceDocLinesApplicationId | APPLICATION_ID | — | — |
| 12 | SourceDocLinesBasePrice | BASE_PRICE | — | — |
| 13 | SourceDocLinesBillToCountry | BILL_TO_COUNTRY | — | — |
| 14 | SourceDocLinesBillToCustClassification | BILL_TO_CUST_CLASSIFICATION | — | — |
| 15 | SourceDocLinesBillToCustSiteName | BILL_TO_CUST_SITE_NAME | — | — |
| 16 | SourceDocLinesBillToCustomerCity | BILL_TO_CUSTOMER_CITY | — | — |
| 17 | SourceDocLinesBillToCustomerCounty | BILL_TO_CUSTOMER_COUNTY | — | — |
| 18 | SourceDocLinesBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 19 | SourceDocLinesBillToCustomerName | BILL_TO_CUSTOMER_NAME | — | — |
| 20 | SourceDocLinesBillToCustomerNum | BILL_TO_CUSTOMER_NUM | — | — |
| 21 | SourceDocLinesBillToCustomerPartyId | BILL_TO_CUSTOMER_PARTY_ID | — | — |
| 22 | SourceDocLinesBillToCustomerPartyName | BILL_TO_CUSTOMER_PARTY_NAME | — | — |
| 23 | SourceDocLinesBillToCustomerPartyNum | BILL_TO_CUSTOMER_PARTY_NUM | — | — |
| 24 | SourceDocLinesBillToCustomerPostalCode | BILL_TO_CUSTOMER_POSTAL_CODE | — | — |
| 25 | SourceDocLinesBillToCustomerSiteId | BILL_TO_CUSTOMER_SITE_ID | — | — |
| 26 | SourceDocLinesBillToCustomerState | BILL_TO_CUSTOMER_STATE | — | — |
| 27 | SourceDocLinesCancelledFlag | CANCELLED_FLAG | — | — |
| 28 | SourceDocLinesComments | COMMENTS | — | ✅ |
| 29 | SourceDocLinesContingencyId | CONTINGENCY_ID | — | — |
| 30 | SourceDocLinesCostAmount | COST_AMOUNT | — | — |
| 31 | SourceDocLinesCreatedBy | CREATED_BY | — | — |
| 32 | SourceDocLinesCreationDate | CREATION_DATE | — | — |
| 33 | SourceDocLinesCreditInvoiceLineId | CREDIT_INVOICE_LINE_ID | — | — |
| 34 | SourceDocLinesCustPoNumber | CUST_PO_NUMBER | — | — |
| 35 | SourceDocLinesDataTransErrorMessage | DATA_TRANS_ERROR_MESSAGE | — | — |
| 36 | SourceDocLinesDataTransformationStatus | DATA_TRANSFORMATION_STATUS | — | ✅ |
| 37 | SourceDocLinesDeliveredFlag | DELIVERED_FLAG | — | — |
| 38 | SourceDocLinesDeliveryDate | DELIVERY_DATE | — | ✅ |
| 39 | SourceDocLinesDeliveryStatus | DELIVERY_STATUS | — | ✅ |
| 40 | SourceDocLinesDiscountAmount | DISCOUNT_AMOUNT | — | — |
| 41 | SourceDocLinesDiscountPercentage | DISCOUNT_PERCENTAGE | — | — |
| 42 | SourceDocLinesDocIdChar1 | DOC_ID_CHAR_1 | — | — |
| 43 | SourceDocLinesDocIdChar2 | DOC_ID_CHAR_2 | — | — |
| 44 | SourceDocLinesDocIdChar3 | DOC_ID_CHAR_3 | — | — |
| 45 | SourceDocLinesDocIdChar4 | DOC_ID_CHAR_4 | — | — |
| 46 | SourceDocLinesDocIdChar5 | DOC_ID_CHAR_5 | — | — |
| 47 | SourceDocLinesDocIdInt1 | DOC_ID_INT_1 | — | — |
| 48 | SourceDocLinesDocIdInt2 | DOC_ID_INT_2 | — | — |
| 49 | SourceDocLinesDocIdInt3 | DOC_ID_INT_3 | — | — |
| 50 | SourceDocLinesDocIdInt4 | DOC_ID_INT_4 | — | — |
| 51 | SourceDocLinesDocIdInt5 | DOC_ID_INT_5 | — | — |
| 52 | SourceDocLinesDocLineIdChar1 | DOC_LINE_ID_CHAR_1 | — | — |
| 53 | SourceDocLinesDocLineIdChar2 | DOC_LINE_ID_CHAR_2 | — | — |
| 54 | SourceDocLinesDocLineIdChar3 | DOC_LINE_ID_CHAR_3 | — | — |
| 55 | SourceDocLinesDocLineIdChar4 | DOC_LINE_ID_CHAR_4 | — | — |
| 56 | SourceDocLinesDocLineIdChar5 | DOC_LINE_ID_CHAR_5 | — | — |
| 57 | SourceDocLinesDocLineIdInt1 | DOC_LINE_ID_INT_1 | — | — |
| 58 | SourceDocLinesDocLineIdInt2 | DOC_LINE_ID_INT_2 | — | — |
| 59 | SourceDocLinesDocLineIdInt3 | DOC_LINE_ID_INT_3 | — | — |
| 60 | SourceDocLinesDocLineIdInt4 | DOC_LINE_ID_INT_4 | — | — |
| 61 | SourceDocLinesDocLineIdInt5 | DOC_LINE_ID_INT_5 | — | — |
| 62 | SourceDocLinesDocumentDate | DOCUMENT_DATE | — | ✅ |
| 63 | SourceDocLinesDocumentId | DOCUMENT_ID | — | — |
| 64 | SourceDocLinesDocumentLineId | DOCUMENT_LINE_ID | 🔑 | ✅ |
| 65 | SourceDocLinesDocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 66 | SourceDocLinesFobPointCode | FOB_POINT_CODE | — | — |
| 67 | SourceDocLinesFrieghtTermsCode | FRIEGHT_TERMS_CODE | — | — |
| 68 | SourceDocLinesFulfilledFlag | FULFILLED_FLAG | — | — |
| 69 | SourceDocLinesFulfillmentDate | FULFILLMENT_DATE | — | — |
| 70 | SourceDocLinesGrossMarginPercent | GROSS_MARGIN_PERCENT | — | — |
| 71 | SourceDocLinesImmaterialChangeCode | IMMATERIAL_CHANGE_CODE | — | ✅ |
| 72 | SourceDocLinesInventoryOrgCode | INVENTORY_ORG_CODE | — | — |
| 73 | SourceDocLinesInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 74 | SourceDocLinesInvoicedFlag | INVOICED_FLAG | — | — |
| 75 | SourceDocLinesItemDescription | ITEM_DESCRIPTION | — | — |
| 76 | SourceDocLinesItemId | ITEM_ID | — | — |
| 77 | SourceDocLinesItemNumber | ITEM_NUMBER | — | — |
| 78 | SourceDocLinesLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 79 | SourceDocLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 80 | SourceDocLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 81 | SourceDocLinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 82 | SourceDocLinesLineAmount | LINE_AMOUNT | — | — |
| 83 | SourceDocLinesLineCreationDate | LINE_CREATION_DATE | — | — |
| 84 | SourceDocLinesLineLastUpdateDate | LINE_LAST_UPDATE_DATE | — | ✅ |
| 85 | SourceDocLinesLineNum | LINE_NUM | — | ✅ |
| 86 | SourceDocLinesLineNumber | LINE_NUMBER | — | — |
| 87 | SourceDocLinesLineType | LINE_TYPE | — | ✅ |
| 88 | SourceDocLinesLoadRequestId | LOAD_REQUEST_ID | — | — |
| 89 | SourceDocLinesManualReviewRequiredFlag | MANUAL_REVIEW_REQUIRED_FLAG | — | ✅ |
| 90 | SourceDocLinesMemoLineId | MEMO_LINE_ID | — | — |
| 91 | SourceDocLinesMemoLineName | MEMO_LINE_NAME | — | — |
| 92 | SourceDocLinesMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 93 | SourceDocLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 94 | SourceDocLinesOpenFlag | OPEN_FLAG | — | — |
| 95 | SourceDocLinesOrigSysBillToCustRef | ORIG_SYS_BILL_TO_CUST_REF | — | — |
| 96 | SourceDocLinesOrigSysBillToCustSiteRef | ORIG_SYS_BILL_TO_CUST_SITE_REF | — | — |
| 97 | SourceDocLinesOrigSysShipToCustRef | ORIG_SYS_SHIP_TO_CUST_REF | — | — |
| 98 | SourceDocLinesOrigSysShipToCustSiteRef | ORIG_SYS_SHIP_TO_CUST_SITE_REF | — | — |
| 99 | SourceDocLinesOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 100 | SourceDocLinesPaymentAmount | PAYMENT_AMOUNT | — | — |
| 101 | SourceDocLinesPaymentTermId | PAYMENT_TERM_ID | — | — |
| 102 | SourceDocLinesPaymentTermName | PAYMENT_TERM_NAME | — | — |
| 103 | SourceDocLinesProjectId | PROJECT_ID | — | — |
| 104 | SourceDocLinesQuantity | QUANTITY | — | — |
| 105 | SourceDocLinesQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 106 | SourceDocLinesQuantityFulfilled | QUANTITY_FULFILLED | — | — |
| 107 | SourceDocLinesQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 108 | SourceDocLinesQuantityOrdered | QUANTITY_ORDERED | — | — |
| 109 | SourceDocLinesQuantityShipped | QUANTITY_SHIPPED | — | — |
| 110 | SourceDocLinesRecurLineCopyNum | RECUR_LINE_COPY_NUM | — | ✅ |
| 111 | SourceDocLinesRecurringFlag | RECURRING_FLAG | — | ✅ |
| 112 | SourceDocLinesRecurringFrequency | RECURRING_FREQUENCY | — | ✅ |
| 113 | SourceDocLinesRecurringPatternCode | RECURRING_PATTERN_CODE | — | ✅ |
| 114 | SourceDocLinesReferenceCustomerTrxLineId | REFERENCE_CUSTOMER_TRX_LINE_ID | — | — |
| 115 | SourceDocLinesReferenceDocLineIdChar1 | REFERENCE_DOC_LINE_ID_CHAR_1 | — | — |
| 116 | SourceDocLinesReferenceDocLineIdChar2 | REFERENCE_DOC_LINE_ID_CHAR_2 | — | — |
| 117 | SourceDocLinesReferenceDocLineIdChar3 | REFERENCE_DOC_LINE_ID_CHAR_3 | — | — |
| 118 | SourceDocLinesReferenceDocLineIdChar4 | REFERENCE_DOC_LINE_ID_CHAR_4 | — | — |
| 119 | SourceDocLinesReferenceDocLineIdChar5 | REFERENCE_DOC_LINE_ID_CHAR_5 | — | — |
| 120 | SourceDocLinesReferenceDocLineIdInt1 | REFERENCE_DOC_LINE_ID_INT_1 | — | — |
| 121 | SourceDocLinesReferenceDocLineIdInt2 | REFERENCE_DOC_LINE_ID_INT_2 | — | — |
| 122 | SourceDocLinesReferenceDocLineIdInt3 | REFERENCE_DOC_LINE_ID_INT_3 | — | — |
| 123 | SourceDocLinesReferenceDocLineIdInt4 | REFERENCE_DOC_LINE_ID_INT_4 | — | — |
| 124 | SourceDocLinesReferenceDocLineIdInt5 | REFERENCE_DOC_LINE_ID_INT_5 | — | — |
| 125 | SourceDocLinesRequestId | REQUEST_ID | — | — |
| 126 | SourceDocLinesReturnReasonCode | RETURN_REASON_CODE | — | — |
| 127 | SourceDocLinesRevenueReversalMethod | REVENUE_REVERSAL_METHOD | — | — |
| 128 | SourceDocLinesRevisionIntentTypeCode | REVISION_INTENT_TYPE_CODE | — | ✅ |
| 129 | SourceDocLinesRevrecComments | REVREC_COMMENTS | — | — |
| 130 | SourceDocLinesRevrecEventCode | REVREC_EVENT_CODE | — | — |
| 131 | SourceDocLinesRevrecExpirationDays | REVREC_EXPIRATION_DAYS | — | — |
| 132 | SourceDocLinesRevrecImplicitFlag | REVREC_IMPLICIT_FLAG | — | — |
| 133 | SourceDocLinesRevrecReferenceDocument | REVREC_REFERENCE_DOCUMENT | — | — |
| 134 | SourceDocLinesRevrecSignature | REVREC_SIGNATURE | — | — |
| 135 | SourceDocLinesRevrecSignatureDate | REVREC_SIGNATURE_DATE | — | — |
| 136 | SourceDocLinesRuleEndDate | RULE_END_DATE | — | — |
| 137 | SourceDocLinesRuleStartDate | RULE_START_DATE | — | ✅ |
| 138 | SourceDocLinesSalesrepId | SALESREP_ID | — | — |
| 139 | SourceDocLinesSalesrepName | SALESREP_NAME | — | — |
| 140 | SourceDocLinesSatisfactionMeasurementModel | SATISFACTION_MEASUREMENT_MODEL | — | ✅ |
| 141 | SourceDocLinesScheduledStatusCode | SCHEDULED_STATUS_CODE | — | — |
| 142 | SourceDocLinesShipToCountry | SHIP_TO_COUNTRY | — | — |
| 143 | SourceDocLinesShipToCustSiteName | SHIP_TO_CUST_SITE_NAME | — | — |
| 144 | SourceDocLinesShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 145 | SourceDocLinesShipToCustomerName | SHIP_TO_CUSTOMER_NAME | — | — |
| 146 | SourceDocLinesShipToCustomerNum | SHIP_TO_CUSTOMER_NUM | — | — |
| 147 | SourceDocLinesShipToCustomerSiteId | SHIP_TO_CUSTOMER_SITE_ID | — | — |
| 148 | SourceDocLinesShippableFlag | SHIPPABLE_FLAG | — | — |
| 149 | SourceDocLinesShippingInterfacedFlag | SHIPPING_INTERFACED_FLAG | — | — |
| 150 | SourceDocLinesSourceAccountingRuleName | SOURCE_ACCOUNTING_RULE_NAME | — | — |
| 151 | SourceDocLinesSourceBillToCustAddress | SOURCE_BILL_TO_CUST_ADDRESS | — | — |
| 152 | SourceDocLinesSourceBillToCustName | SOURCE_BILL_TO_CUST_NAME | — | — |
| 153 | SourceDocLinesSourceBillToCustNum | SOURCE_BILL_TO_CUST_NUM | — | — |
| 154 | SourceDocLinesSourceBillToCustSiteNum | SOURCE_BILL_TO_CUST_SITE_NUM | — | — |
| 155 | SourceDocLinesSourceInventoryOrgCode | SOURCE_INVENTORY_ORG_CODE | — | — |
| 156 | SourceDocLinesSourceInventoryOrgId | SOURCE_INVENTORY_ORG_ID | — | — |
| 157 | SourceDocLinesSourceItemNumber | SOURCE_ITEM_NUMBER | — | — |
| 158 | SourceDocLinesSourceMemoLineName | SOURCE_MEMO_LINE_NAME | — | — |
| 159 | SourceDocLinesSourceOrgId | SOURCE_ORG_ID | — | — |
| 160 | SourceDocLinesSourcePaymentTermName | SOURCE_PAYMENT_TERM_NAME | — | — |
| 161 | SourceDocLinesSourceSalesrepName | SOURCE_SALESREP_NAME | — | — |
| 162 | SourceDocLinesSourceShipToCustAddress | SOURCE_SHIP_TO_CUST_ADDRESS | — | — |
| 163 | SourceDocLinesSourceShipToCustName | SOURCE_SHIP_TO_CUST_NAME | — | — |
| 164 | SourceDocLinesSourceShipToCustNum | SOURCE_SHIP_TO_CUST_NUM | — | — |
| 165 | SourceDocLinesSourceShipToCustSiteNum | SOURCE_SHIP_TO_CUST_SITE_NUM | — | — |
| 166 | SourceDocLinesSourceTypeCode | SOURCE_TYPE_CODE | — | — |
| 167 | SourceDocLinesSourceUomCode | SOURCE_UOM_CODE | — | — |
| 168 | SourceDocLinesSrcAttributeChar4 | SRC_ATTRIBUTE_CHAR4 | — | — |
| 169 | SourceDocLinesTaskId | TASK_ID | — | — |
| 170 | SourceDocLinesTerminationDate | TERMINATION_DATE | — | ✅ |
| 171 | SourceDocLinesUnitListPctBasePrice | UNIT_LIST_PCT_BASE_PRICE | — | — |
| 172 | SourceDocLinesUnitListPrice | UNIT_LIST_PRICE | — | — |
| 173 | SourceDocLinesUnitSellingPctBasePrice | UNIT_SELLING_PCT_BASE_PRICE | — | — |
| 174 | SourceDocLinesUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 175 | SourceDocLinesUnitSsp | UNIT_SSP | — | — |
| 176 | SourceDocLinesUomCode | UOM_CODE | — | ✅ |
| 177 | SourceDocLinesVersionFlag | VERSION_FLAG | — | ✅ |
| 178 | SourceDocLinesVersionNumber | VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
