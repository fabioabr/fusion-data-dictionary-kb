---
id: DOC-AP-PVO-InvoicePaymentSchedulePVO
doc_type: system-doc
title: "InvoicePaymentSchedulePVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - InvoicePaymentSchedulePVO
  - invoicepaymentschedulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoicePaymentSchedulePVO

## 📌 Visão Geral

Extrai os cronogramas de pagamento das faturas de fornecedores, incluindo datas de vencimento, valores das parcelas, condições de pagamento e dados bancários. Essencial para projeção de fluxo de caixa, planejamento de tesouraria e gestão de vencimentos.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.InvoicePaymentSchedulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 117 | 8 | 2 | 78 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 43 atributos (26 BICC)
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 43 atributos (2 PKs, 38 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 7 atributos (3 BICC)
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 8 atributos (6 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 11 atributos (2 BICC)
- [[zx_condition_groups_vl|ZX_CONDITION_GROUPS_VL]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderAcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | ✅ |
| 2 | InvoiceHeaderBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 3 | InvoiceHeaderBudgetDate | BUDGET_DATE | — | ✅ |
| 4 | InvoiceHeaderCancelledDate | CANCELLED_DATE | — | ✅ |
| 5 | InvoiceHeaderCorrectionPeriod | CORRECTION_PERIOD | — | — |
| 6 | InvoiceHeaderCorrectionYear | CORRECTION_YEAR | — | — |
| 7 | InvoiceHeaderCreationDate | CREATION_DATE | — | ✅ |
| 8 | InvoiceHeaderDescription | DESCRIPTION | — | ✅ |
| 9 | InvoiceHeaderDocCategoryCode | DOC_CATEGORY_CODE | — | — |
| 10 | InvoiceHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 11 | InvoiceHeaderEmployeeAddressCode | EMPLOYEE_ADDRESS_CODE | — | — |
| 12 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 13 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 14 | InvoiceHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 15 | InvoiceHeaderExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 16 | InvoiceHeaderExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 17 | InvoiceHeaderExpenditureType | EXPENDITURE_TYPE | — | — |
| 18 | InvoiceHeaderFundsStatus | FUNDS_STATUS | — | ✅ |
| 19 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 20 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | ✅ |
| 21 | InvoiceHeaderInvoiceId | INVOICE_ID | — | — |
| 22 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | ✅ |
| 23 | InvoiceHeaderInvoiceReceivedDate | INVOICE_RECEIVED_DATE | — | ✅ |
| 24 | InvoiceHeaderInvoiceTypeLookupCode | INVOICE_TYPE_LOOKUP_CODE | — | ✅ |
| 25 | InvoiceHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | InvoiceHeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 27 | InvoiceHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | InvoiceHeaderOrgId | ORG_ID | — | ✅ |
| 29 | InvoiceHeaderPartyId | PARTY_ID | — | ✅ |
| 30 | InvoiceHeaderPaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 31 | InvoiceHeaderPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 32 | InvoiceHeaderPaymentMethodLookupCode | PAYMENT_METHOD_LOOKUP_CODE | — | — |
| 33 | InvoiceHeaderPaymentReasonComments | PAYMENT_REASON_COMMENTS | — | ✅ |
| 34 | InvoiceHeaderPaymentStatusFlag | PAYMENT_STATUS_FLAG | — | — |
| 35 | InvoiceHeaderProjectId | PROJECT_ID | — | — |
| 36 | InvoiceHeaderRequesterId | REQUESTER_ID | — | — |
| 37 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 38 | InvoiceHeaderSource | SOURCE | — | ✅ |
| 39 | InvoiceHeaderTermsId | TERMS_ID | — | ✅ |
| 40 | InvoiceHeaderVendorContactId | VENDOR_CONTACT_ID | — | — |
| 41 | InvoiceHeaderVendorId | VENDOR_ID | — | — |
| 42 | InvoiceHeaderVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 43 | InvoiceHeaderWfapprovalStatus | WFAPPROVAL_STATUS | — | ✅ |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DiscountAPR | APR_DISCOUNT_RATE | — | — |
| 2 | DiscountOffersTransNameType | ASSIGNMENT_TYPE_CODE | — | — |
| 3 | DiscountOffersTranslationName | CAMPAIGN_NAME | — | — |
| 4 | InvoiceHeaderRelationshipId | RELATIONSHIP_ID | — | ✅ |
| 5 | InvoiceHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 6 | InvoiceHeaderRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 7 | InvoiceHeaderRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 8 | InvoiceHeaderRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 9 | InvoiceId | INVOICE_ID | 🔑 | ✅ |
| 10 | PaymentNum | PAYMENT_NUM | 🔑 | ✅ |
| 11 | PaymentScheduleAmountRemaining | AMOUNT_REMAINING | — | ✅ |
| 12 | PaymentScheduleCreatedBy | CREATED_BY | — | ✅ |
| 13 | PaymentScheduleCreationDate | CREATION_DATE | — | ✅ |
| 14 | PaymentScheduleDiscountAmountAvailable | DISCOUNT_AMOUNT_AVAILABLE | — | ✅ |
| 15 | PaymentScheduleDiscountAmountRemaining | DISCOUNT_AMOUNT_REMAINING | — | ✅ |
| 16 | PaymentScheduleDiscountDate | DISCOUNT_DATE | — | ✅ |
| 17 | PaymentScheduleDueDate | DUE_DATE | — | ✅ |
| 18 | PaymentScheduleExternalBankAccountId | EXTERNAL_BANK_ACCOUNT_ID | — | ✅ |
| 19 | PaymentScheduleGrossAmount | GROSS_AMOUNT | — | ✅ |
| 20 | PaymentScheduleHoldDate | HOLD_DATE | — | ✅ |
| 21 | PaymentScheduleHoldFlag | HOLD_FLAG | — | ✅ |
| 22 | PaymentScheduleIbyHoldReason | IBY_HOLD_REASON | — | ✅ |
| 23 | PaymentScheduleInvCurrGrossAmount | INV_CURR_GROSS_AMOUNT | — | ✅ |
| 24 | PaymentScheduleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | PaymentScheduleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | PaymentScheduleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | PaymentScheduleOrgId | ORG_ID | — | — |
| 28 | PaymentSchedulePaymentCrossRate | PAYMENT_CROSS_RATE | — | ✅ |
| 29 | PaymentSchedulePaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 30 | PaymentSchedulePaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 31 | PaymentSchedulePaymentStatusFlag | PAYMENT_STATUS_FLAG | — | ✅ |
| 32 | PaymentScheduleRelationshipId | RELATIONSHIP_ID | — | ✅ |
| 33 | PaymentScheduleRemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 34 | PaymentScheduleRemitToAddressName | REMIT_TO_ADDRESS_NAME | — | ✅ |
| 35 | PaymentScheduleRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 36 | PaymentScheduleRemitToSupplierName | REMIT_TO_SUPPLIER_NAME | — | ✅ |
| 37 | PaymentScheduleRemittanceMessage1 | REMITTANCE_MESSAGE1 | — | ✅ |
| 38 | PaymentScheduleRemittanceMessage2 | REMITTANCE_MESSAGE2 | — | ✅ |
| 39 | PaymentScheduleRemittanceMessage3 | REMITTANCE_MESSAGE3 | — | ✅ |
| 40 | PaymentScheduleSecondDiscAmtAvailable | SECOND_DISC_AMT_AVAILABLE | — | ✅ |
| 41 | PaymentScheduleSecondDiscountDate | SECOND_DISCOUNT_DATE | — | ✅ |
| 42 | PaymentScheduleThirdDiscAmtAvailable | THIRD_DISC_AMT_AVAILABLE | — | ✅ |
| 43 | PaymentScheduleThirdDiscountDate | THIRD_DISCOUNT_DATE | — | ✅ |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PartyPartyId | PARTY_ID | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtBnkAcctCheckDigits | CHECK_DIGITS | — | ✅ |
| 2 | ExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 3 | ExtBnkAcctMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | ✅ |
| 4 | ExtBnkAcctObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | InvExtBnkAcctExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 6 | InvExtBnkAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InvExtBnkAcctObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | PayDelcodeMeaning | MEANING | — | ✅ |
| 3 | PayDelcodePaymentCode | PAYMENT_CODE | — | ✅ |
| 4 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 5 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PayReacodeMeaning | MEANING | — | ✅ |
| 7 | PayReacodePaymentCode | PAYMENT_CODE | — | ✅ |
| 8 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 9 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 10 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 11 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[zx_condition_groups_vl|ZX_CONDITION_GROUPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwtTaxGroupConditionGroupId | CONDITION_GROUP_ID | — | ✅ |
| 2 | AwtTaxGroupConditionGroupName | CONDITION_GROUP_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
