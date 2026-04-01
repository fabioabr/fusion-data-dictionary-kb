---
id: DOC-AR-PVO-CreditMemoApplicationPVO
doc_type: system-doc
title: "CreditMemoApplicationPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CreditMemoApplicationPVO
  - creditmemoapplicationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CreditMemoApplicationPVO

## 📌 Visão Geral

Extrai as aplicações de notas de crédito a transações de recebíveis, incluindo valores aplicados, saldo remanescente e regras de aplicação. Permite acompanhar a compensação de créditos concedidos contra faturas em aberto e o impacto no saldo de clientes.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.CreditMemoApplicationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 421 | 15 | 1 | 53 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_rule_sets|AR_APP_RULE_SETS]] — 6 atributos (1 BICC)
- [[ar_cons_inv_all|AR_CONS_INV_ALL]] — 8 atributos (1 BICC)
- [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]] — 93 atributos (2 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 20 atributos (1 BICC)
- [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]] — 84 atributos (1 PKs, 26 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 3 atributos (1 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 14 atributos (9 BICC)
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 154 atributos (10 BICC)
- [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]] — 4 atributos (2 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos
- [[xla_events|XLA_EVENTS]] — 11 atributos

---

## ⚙️ Atributos

### [[ar_app_rule_sets|AR_APP_RULE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppRuleSetDescription | DESCRIPTION | — | — |
| 2 | AppRuleSetFreezeFlag | FREEZE_FLAG | — | — |
| 3 | AppRuleSetModuleId | MODULE_ID | — | — |
| 4 | AppRuleSetRuleSetId | RULE_SET_ID | — | — |
| 5 | AppRuleSetRuleSetName | RULE_SET_NAME | — | ✅ |
| 6 | AppRuleSetRuleSource | RULE_SOURCE | — | — |

### [[ar_cons_inv_all|AR_CONS_INV_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsBillConcurrentRequestId | CONCURRENT_REQUEST_ID | — | — |
| 2 | ConsBillConsBillingNumber | CONS_BILLING_NUMBER | — | ✅ |
| 3 | ConsBillConsInvId | CONS_INV_ID | — | — |
| 4 | ConsBillConsInvType | CONS_INV_TYPE | — | — |
| 5 | ConsBillCustomerId | CUSTOMER_ID | — | — |
| 6 | ConsBillSiteUseId | SITE_USE_ID | — | — |
| 7 | ConsBillStatus | STATUS | — | — |
| 8 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[ar_payment_schedules_all|AR_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentScheduleAppliedAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 2 | PaymentScheduleAppliedActiveClaimFlag | ACTIVE_CLAIM_FLAG | — | — |
| 3 | PaymentScheduleAppliedActualDateClosed | ACTUAL_DATE_CLOSED | — | — |
| 4 | PaymentScheduleAppliedAdjustmentAmountLast | ADJUSTMENT_AMOUNT_LAST | — | — |
| 5 | PaymentScheduleAppliedAdjustmentDateLast | ADJUSTMENT_DATE_LAST | — | — |
| 6 | PaymentScheduleAppliedAdjustmentGlDateLast | ADJUSTMENT_GL_DATE_LAST | — | — |
| 7 | PaymentScheduleAppliedAdjustmentIdLast | ADJUSTMENT_ID_LAST | — | — |
| 8 | PaymentScheduleAppliedAmountAdjusted | AMOUNT_ADJUSTED | — | — |
| 9 | PaymentScheduleAppliedAmountAdjustedPending | AMOUNT_ADJUSTED_PENDING | — | — |
| 10 | PaymentScheduleAppliedAmountApplied | AMOUNT_APPLIED | — | — |
| 11 | PaymentScheduleAppliedAmountCredited | AMOUNT_CREDITED | — | — |
| 12 | PaymentScheduleAppliedAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 13 | PaymentScheduleAppliedAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 14 | PaymentScheduleAppliedAmountInDispute | AMOUNT_IN_DISPUTE | — | — |
| 15 | PaymentScheduleAppliedAmountLineItemsOriginal | AMOUNT_LINE_ITEMS_ORIGINAL | — | — |
| 16 | PaymentScheduleAppliedAmountLineItemsRemaining | AMOUNT_LINE_ITEMS_REMAINING | — | — |
| 17 | PaymentScheduleAppliedAmountOnAccount | AMOUNT_ON_ACCOUNT | — | — |
| 18 | PaymentScheduleAppliedAmountOtherAccount | AMOUNT_OTHER_ACCOUNT | — | — |
| 19 | PaymentScheduleAppliedAssociatedCashReceiptId | ASSOCIATED_CASH_RECEIPT_ID | — | — |
| 20 | PaymentScheduleAppliedBrAmountAssigned | BR_AMOUNT_ASSIGNED | — | — |
| 21 | PaymentScheduleAppliedCallDateLast | CALL_DATE_LAST | — | — |
| 22 | PaymentScheduleAppliedCashAppliedAmountLast | CASH_APPLIED_AMOUNT_LAST | — | — |
| 23 | PaymentScheduleAppliedCashAppliedDateLast | CASH_APPLIED_DATE_LAST | — | — |
| 24 | PaymentScheduleAppliedCashAppliedIdLast | CASH_APPLIED_ID_LAST | — | — |
| 25 | PaymentScheduleAppliedCashAppliedStatusLast | CASH_APPLIED_STATUS_LAST | — | — |
| 26 | PaymentScheduleAppliedCashGlDateLast | CASH_GL_DATE_LAST | — | — |
| 27 | PaymentScheduleAppliedCashReceiptAmountLast | CASH_RECEIPT_AMOUNT_LAST | — | — |
| 28 | PaymentScheduleAppliedCashReceiptDateLast | CASH_RECEIPT_DATE_LAST | — | — |
| 29 | PaymentScheduleAppliedCashReceiptId | CASH_RECEIPT_ID | — | — |
| 30 | PaymentScheduleAppliedCashReceiptIdLast | CASH_RECEIPT_ID_LAST | — | — |
| 31 | PaymentScheduleAppliedCashReceiptStatusLast | CASH_RECEIPT_STATUS_LAST | — | — |
| 32 | PaymentScheduleAppliedCollectorLast | COLLECTOR_LAST | — | — |
| 33 | PaymentScheduleAppliedConsInvId | CONS_INV_ID | — | — |
| 34 | PaymentScheduleAppliedConsInvIdRev | CONS_INV_ID_REV | — | — |
| 35 | PaymentScheduleAppliedCreatedBy | CREATED_BY | — | — |
| 36 | PaymentScheduleAppliedCreationDate | CREATION_DATE | — | — |
| 37 | PaymentScheduleAppliedCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 38 | PaymentScheduleAppliedCustomerId | CUSTOMER_ID | — | — |
| 39 | PaymentScheduleAppliedCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 40 | PaymentScheduleAppliedCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 41 | PaymentScheduleAppliedDiscountDate | DISCOUNT_DATE | — | — |
| 42 | PaymentScheduleAppliedDiscountOriginal | DISCOUNT_ORIGINAL | — | — |
| 43 | PaymentScheduleAppliedDiscountRemaining | DISCOUNT_REMAINING | — | — |
| 44 | PaymentScheduleAppliedDiscountTakenEarned | DISCOUNT_TAKEN_EARNED | — | — |
| 45 | PaymentScheduleAppliedDiscountTakenUnearned | DISCOUNT_TAKEN_UNEARNED | — | — |
| 46 | PaymentScheduleAppliedDisputeDate | DISPUTE_DATE | — | — |
| 47 | PaymentScheduleAppliedDueDate | DUE_DATE | — | ✅ |
| 48 | PaymentScheduleAppliedDunningLevelOverrideDate | DUNNING_LEVEL_OVERRIDE_DATE | — | — |
| 49 | PaymentScheduleAppliedExchangeDate | EXCHANGE_DATE | — | — |
| 50 | PaymentScheduleAppliedExchangeRate | EXCHANGE_RATE | — | — |
| 51 | PaymentScheduleAppliedExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 52 | PaymentScheduleAppliedExcludeFromConsBillFlag | EXCLUDE_FROM_CONS_BILL_FLAG | — | — |
| 53 | PaymentScheduleAppliedExcludeFromDunningFlag | EXCLUDE_FROM_DUNNING_FLAG | — | — |
| 54 | PaymentScheduleAppliedFollowUpCodeLast | FOLLOW_UP_CODE_LAST | — | — |
| 55 | PaymentScheduleAppliedFollowUpDateLast | FOLLOW_UP_DATE_LAST | — | — |
| 56 | PaymentScheduleAppliedFreightOriginal | FREIGHT_ORIGINAL | — | — |
| 57 | PaymentScheduleAppliedFreightRemaining | FREIGHT_REMAINING | — | — |
| 58 | PaymentScheduleAppliedGlDate | GL_DATE | — | — |
| 59 | PaymentScheduleAppliedGlDateClosed | GL_DATE_CLOSED | — | — |
| 60 | PaymentScheduleAppliedInCollection | IN_COLLECTION | — | — |
| 61 | PaymentScheduleAppliedInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 62 | PaymentScheduleAppliedLastChargeDate | LAST_CHARGE_DATE | — | — |
| 63 | PaymentScheduleAppliedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | PaymentScheduleAppliedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | PaymentScheduleAppliedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | PaymentScheduleAppliedNumberOfDueDates | NUMBER_OF_DUE_DATES | — | — |
| 67 | PaymentScheduleAppliedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | PaymentScheduleAppliedOrgId | ORG_ID | — | — |
| 69 | PaymentScheduleAppliedPaymentApproval | PAYMENT_APPROVAL | — | — |
| 70 | PaymentScheduleAppliedPaymentScheduleClass | CLASS | — | — |
| 71 | PaymentScheduleAppliedPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 72 | PaymentScheduleAppliedProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | PaymentScheduleAppliedProgramId | PROGRAM_ID | — | — |
| 74 | PaymentScheduleAppliedProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | PaymentScheduleAppliedPromiseAmountLast | PROMISE_AMOUNT_LAST | — | — |
| 76 | PaymentScheduleAppliedPromiseDateLast | PROMISE_DATE_LAST | — | — |
| 77 | PaymentScheduleAppliedReceiptConfirmedFlag | RECEIPT_CONFIRMED_FLAG | — | — |
| 78 | PaymentScheduleAppliedReceivablesChargesCharged | RECEIVABLES_CHARGES_CHARGED | — | — |
| 79 | PaymentScheduleAppliedReceivablesChargesRemaining | RECEIVABLES_CHARGES_REMAINING | — | — |
| 80 | PaymentScheduleAppliedRequestId | REQUEST_ID | — | — |
| 81 | PaymentScheduleAppliedReservedType | RESERVED_TYPE | — | — |
| 82 | PaymentScheduleAppliedReservedValue | RESERVED_VALUE | — | — |
| 83 | PaymentScheduleAppliedReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 84 | PaymentScheduleAppliedSecondLastChargeDate | SECOND_LAST_CHARGE_DATE | — | — |
| 85 | PaymentScheduleAppliedSelectedForReceiptBatchId | SELECTED_FOR_RECEIPT_BATCH_ID | — | — |
| 86 | PaymentScheduleAppliedStagedDunningLevel | STAGED_DUNNING_LEVEL | — | — |
| 87 | PaymentScheduleAppliedStatus | STATUS | — | — |
| 88 | PaymentScheduleAppliedTaxOriginal | TAX_ORIGINAL | — | — |
| 89 | PaymentScheduleAppliedTaxRemaining | TAX_REMAINING | — | — |
| 90 | PaymentScheduleAppliedTermId | TERM_ID | — | — |
| 91 | PaymentScheduleAppliedTermsSequenceNumber | TERMS_SEQUENCE_NUMBER | — | — |
| 92 | PaymentScheduleAppliedTrxDate | TRX_DATE | — | — |
| 93 | PaymentScheduleAppliedTrxNumber | TRX_NUMBER | — | — |

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RecvTrxActAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 3 | RecvTrxActAssetTaxCode | ASSET_TAX_CODE | — | — |
| 4 | RecvTrxActCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | RecvTrxActDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 6 | RecvTrxActDescription | DESCRIPTION | — | — |
| 7 | RecvTrxActEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | RecvTrxActGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 9 | RecvTrxActInactiveDate | INACTIVE_DATE | — | — |
| 10 | RecvTrxActLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 11 | RecvTrxActName | NAME | — | ✅ |
| 12 | RecvTrxActOrgId | ORG_ID | — | — |
| 13 | RecvTrxActReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 14 | RecvTrxActRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 15 | RecvTrxActSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 16 | RecvTrxActStartDateActive | START_DATE_ACTIVE | — | — |
| 17 | RecvTrxActStatus | STATUS | — | — |
| 18 | RecvTrxActTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 19 | RecvTrxActTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 20 | RecvTrxActType | TYPE | — | — |

### [[ar_receivable_applications_all|AR_RECEIVABLE_APPLICATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceivableApplicationAcctdAmountAppliedFrom | ACCTD_AMOUNT_APPLIED_FROM | — | ✅ |
| 2 | ReceivableApplicationAcctdAmountAppliedTo | ACCTD_AMOUNT_APPLIED_TO | — | ✅ |
| 3 | ReceivableApplicationAcctdEarnedDiscountTaken | ACCTD_EARNED_DISCOUNT_TAKEN | — | — |
| 4 | ReceivableApplicationAcctdUnearnedDiscountTaken | ACCTD_UNEARNED_DISCOUNT_TAKEN | — | — |
| 5 | ReceivableApplicationAmountApplied | AMOUNT_APPLIED | — | ✅ |
| 6 | ReceivableApplicationAmountAppliedFrom | AMOUNT_APPLIED_FROM | — | ✅ |
| 7 | ReceivableApplicationApplicationRefId | APPLICATION_REF_ID | — | — |
| 8 | ReceivableApplicationApplicationRefNum | APPLICATION_REF_NUM | — | — |
| 9 | ReceivableApplicationApplicationRefReason | APPLICATION_REF_REASON | — | — |
| 10 | ReceivableApplicationApplicationRefType | APPLICATION_REF_TYPE | — | — |
| 11 | ReceivableApplicationApplicationRule | APPLICATION_RULE | — | — |
| 12 | ReceivableApplicationApplicationType | APPLICATION_TYPE | — | ✅ |
| 13 | ReceivableApplicationAppliedCustomerTrxId | APPLIED_CUSTOMER_TRX_ID | — | — |
| 14 | ReceivableApplicationAppliedCustomerTrxLineId | APPLIED_CUSTOMER_TRX_LINE_ID | — | — |
| 15 | ReceivableApplicationAppliedPaymentScheduleId | APPLIED_PAYMENT_SCHEDULE_ID | — | — |
| 16 | ReceivableApplicationAppliedRecAppId | APPLIED_REC_APP_ID | — | — |
| 17 | ReceivableApplicationApplyDate | APPLY_DATE | — | ✅ |
| 18 | ReceivableApplicationCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 19 | ReceivableApplicationCashReceiptId | CASH_RECEIPT_ID | — | — |
| 20 | ReceivableApplicationChargebackCustomerTrxId | CHARGEBACK_CUSTOMER_TRX_ID | — | — |
| 21 | ReceivableApplicationChargesEdiscounted | CHARGES_EDISCOUNTED | — | — |
| 22 | ReceivableApplicationChargesUediscounted | CHARGES_UEDISCOUNTED | — | — |
| 23 | ReceivableApplicationCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 24 | ReceivableApplicationComments | COMMENTS | — | ✅ |
| 25 | ReceivableApplicationConfirmedFlag | CONFIRMED_FLAG | — | — |
| 26 | ReceivableApplicationConsInvId | CONS_INV_ID | — | — |
| 27 | ReceivableApplicationConsInvIdTo | CONS_INV_ID_TO | — | — |
| 28 | ReceivableApplicationCreatedBy | CREATED_BY | — | ✅ |
| 29 | ReceivableApplicationCreationDate | CREATION_DATE | — | ✅ |
| 30 | ReceivableApplicationCustomerReason | CUSTOMER_REASON | — | ✅ |
| 31 | ReceivableApplicationCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 32 | ReceivableApplicationCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 33 | ReceivableApplicationDaysLate | DAYS_LATE | — | — |
| 34 | ReceivableApplicationDisplay | DISPLAY | — | ✅ |
| 35 | ReceivableApplicationEarnedDiscountCcid | EARNED_DISCOUNT_CCID | — | — |
| 36 | ReceivableApplicationEarnedDiscountTaken | EARNED_DISCOUNT_TAKEN | — | — |
| 37 | ReceivableApplicationEdiscTaxAcctRule | EDISC_TAX_ACCT_RULE | — | — |
| 38 | ReceivableApplicationEventId | EVENT_ID | — | ✅ |
| 39 | ReceivableApplicationExceptionReasonCode | EXCEPTION_REASON_CODE | — | — |
| 40 | ReceivableApplicationFreightApplied | FREIGHT_APPLIED | — | ✅ |
| 41 | ReceivableApplicationFreightEdiscounted | FREIGHT_EDISCOUNTED | — | — |
| 42 | ReceivableApplicationFreightUediscounted | FREIGHT_UEDISCOUNTED | — | — |
| 43 | ReceivableApplicationGlDate | GL_DATE | — | ✅ |
| 44 | ReceivableApplicationGlPostedDate | GL_POSTED_DATE | — | ✅ |
| 45 | ReceivableApplicationId | RECEIVABLE_APPLICATION_ID | 🔑 | ✅ |
| 46 | ReceivableApplicationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | ReceivableApplicationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | ReceivableApplicationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | ReceivableApplicationLineApplied | LINE_APPLIED | — | — |
| 50 | ReceivableApplicationLineEdiscounted | LINE_EDISCOUNTED | — | — |
| 51 | ReceivableApplicationLineUediscounted | LINE_UEDISCOUNTED | — | — |
| 52 | ReceivableApplicationLinkToCustomerTrxId | LINK_TO_CUSTOMER_TRX_ID | — | — |
| 53 | ReceivableApplicationLinkToTrxHistId | LINK_TO_TRX_HIST_ID | — | — |
| 54 | ReceivableApplicationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | ReceivableApplicationOnAccountCustomer | ON_ACCOUNT_CUSTOMER | — | — |
| 56 | ReceivableApplicationOrgId | ORG_ID | — | — |
| 57 | ReceivableApplicationPaymentScheduleId | PAYMENT_SCHEDULE_ID | — | — |
| 58 | ReceivableApplicationPaymentSetId | PAYMENT_SET_ID | — | — |
| 59 | ReceivableApplicationPostable | POSTABLE | — | ✅ |
| 60 | ReceivableApplicationPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 61 | ReceivableApplicationProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 62 | ReceivableApplicationProgramId | PROGRAM_ID | — | — |
| 63 | ReceivableApplicationProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 64 | ReceivableApplicationReceivablesChargesApplied | RECEIVABLES_CHARGES_APPLIED | — | ✅ |
| 65 | ReceivableApplicationReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 66 | ReceivableApplicationRequestId | REQUEST_ID | — | — |
| 67 | ReceivableApplicationReversalGlDate | REVERSAL_GL_DATE | — | ✅ |
| 68 | ReceivableApplicationRuleSetId | RULE_SET_ID | — | — |
| 69 | ReceivableApplicationSecondaryApplicationRefId | SECONDARY_APPLICATION_REF_ID | — | — |
| 70 | ReceivableApplicationSecondaryApplicationRefNum | SECONDARY_APPLICATION_REF_NUM | — | — |
| 71 | ReceivableApplicationSecondaryApplicationRefType | SECONDARY_APPLICATION_REF_TYPE | — | — |
| 72 | ReceivableApplicationSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 73 | ReceivableApplicationStatus | STATUS | — | — |
| 74 | ReceivableApplicationTaxApplied | TAX_APPLIED | — | ✅ |
| 75 | ReceivableApplicationTaxCode | TAX_CODE | — | ✅ |
| 76 | ReceivableApplicationTaxEdiscounted | TAX_EDISCOUNTED | — | — |
| 77 | ReceivableApplicationTaxUediscounted | TAX_UEDISCOUNTED | — | — |
| 78 | ReceivableApplicationTransToReceiptRate | TRANS_TO_RECEIPT_RATE | — | ✅ |
| 79 | ReceivableApplicationUnearnedDiscountCcid | UNEARNED_DISCOUNT_CCID | — | — |
| 80 | ReceivableApplicationUnearnedDiscountTaken | UNEARNED_DISCOUNT_TAKEN | — | — |
| 81 | ReceivableApplicationUnediscTaxAcctRule | UNEDISC_TAX_ACCT_RULE | — | — |
| 82 | ReceivableApplicationUpgradeMethod | UPGRADE_METHOD | — | — |
| 83 | ReceivableApplicationUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 84 | ReceivableApplicationUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |
| 3 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |

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
| 1 | UserCreatedByPersonId | PERSON_ID | — | — |
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 6 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchSourcePEOBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 2 | TransactionBatchSourcePEOName | NAME | — | ✅ |
| 3 | TransactionBatchSourcePEOObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AppliedTransactionHeaderCustomerTrxId1 | CUSTOMER_TRX_ID | — | — |
| 2 | AppliedTransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 3 | AppliedTransactionHeaderObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 4 | AppliedTransactionHeaderTermDueDate | TERM_DUE_DATE | — | — |
| 5 | AppliedTransactionHeaderTrxClass | TRX_CLASS | — | ✅ |
| 6 | AppliedTransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 7 | CustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 8 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 9 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 10 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 11 | TransactionHeaderReasonCode | REASON_CODE | — | ✅ |
| 12 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 13 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 14 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditMemoLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 2 | CreditMemoLineDescription | DESCRIPTION | — | — |
| 3 | CreditMemoLineLineNumber | LINE_NUMBER | — | ✅ |
| 4 | CreditMemoLineLineType | LINE_TYPE | — | ✅ |
| 5 | CreditMemoLineObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 6 | CreditMemoLineQuantityCredited | QUANTITY_CREDITED | — | ✅ |
| 7 | CreditMemoLineQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 8 | CreditMemoLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 9 | CreditMemoLineReasonCode | REASON_CODE | — | ✅ |
| 10 | CreditMemoLineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 11 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 12 | TrxLineAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 13 | TrxLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 14 | TrxLineAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 15 | TrxLineAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 16 | TrxLineAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 17 | TrxLineAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 18 | TrxLineAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 19 | TrxLineAssessableValue | ASSESSABLE_VALUE | — | — |
| 20 | TrxLineAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 21 | TrxLineAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 22 | TrxLineAutotax | AUTOTAX | — | — |
| 23 | TrxLineBrAdjustmentId | BR_ADJUSTMENT_ID | — | — |
| 24 | TrxLineBrRefCustomerTrxId | BR_REF_CUSTOMER_TRX_ID | — | — |
| 25 | TrxLineBrRefPaymentScheduleId | BR_REF_PAYMENT_SCHEDULE_ID | — | — |
| 26 | TrxLineChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 27 | TrxLineChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 28 | TrxLineContractLineId | CONTRACT_LINE_ID | — | — |
| 29 | TrxLineCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 30 | TrxLineCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 31 | TrxLineDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 32 | TrxLineDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 33 | TrxLineDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 34 | TrxLineDescription | DESCRIPTION | — | — |
| 35 | TrxLineExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 36 | TrxLineExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 37 | TrxLineFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 38 | TrxLineFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 39 | TrxLineFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 40 | TrxLineFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 41 | TrxLineFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 42 | TrxLineFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 43 | TrxLineFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 44 | TrxLineGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 45 | TrxLineGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 46 | TrxLineHistoricalFlag | HISTORICAL_FLAG | — | — |
| 47 | TrxLineInitialCustomerTrxLineId | INITIAL_CUSTOMER_TRX_LINE_ID | — | — |
| 48 | TrxLineInterestLineId | INTEREST_LINE_ID | — | — |
| 49 | TrxLineInterfaceLineAttribute1 | INTERFACE_LINE_ATTRIBUTE1 | — | — |
| 50 | TrxLineInterfaceLineAttribute10 | INTERFACE_LINE_ATTRIBUTE10 | — | — |
| 51 | TrxLineInterfaceLineAttribute11 | INTERFACE_LINE_ATTRIBUTE11 | — | — |
| 52 | TrxLineInterfaceLineAttribute12 | INTERFACE_LINE_ATTRIBUTE12 | — | — |
| 53 | TrxLineInterfaceLineAttribute13 | INTERFACE_LINE_ATTRIBUTE13 | — | — |
| 54 | TrxLineInterfaceLineAttribute14 | INTERFACE_LINE_ATTRIBUTE14 | — | — |
| 55 | TrxLineInterfaceLineAttribute15 | INTERFACE_LINE_ATTRIBUTE15 | — | — |
| 56 | TrxLineInterfaceLineAttribute2 | INTERFACE_LINE_ATTRIBUTE2 | — | — |
| 57 | TrxLineInterfaceLineAttribute3 | INTERFACE_LINE_ATTRIBUTE3 | — | — |
| 58 | TrxLineInterfaceLineAttribute4 | INTERFACE_LINE_ATTRIBUTE4 | — | — |
| 59 | TrxLineInterfaceLineAttribute5 | INTERFACE_LINE_ATTRIBUTE5 | — | — |
| 60 | TrxLineInterfaceLineAttribute6 | INTERFACE_LINE_ATTRIBUTE6 | — | — |
| 61 | TrxLineInterfaceLineAttribute7 | INTERFACE_LINE_ATTRIBUTE7 | — | — |
| 62 | TrxLineInterfaceLineAttribute8 | INTERFACE_LINE_ATTRIBUTE8 | — | — |
| 63 | TrxLineInterfaceLineAttribute9 | INTERFACE_LINE_ATTRIBUTE9 | — | — |
| 64 | TrxLineInterfaceLineContext | INTERFACE_LINE_CONTEXT | — | — |
| 65 | TrxLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 66 | TrxLineInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 67 | TrxLineItemContext | ITEM_CONTEXT | — | — |
| 68 | TrxLineItemExceptionRateId | ITEM_EXCEPTION_RATE_ID | — | — |
| 69 | TrxLineLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 70 | TrxLineLineIntendedUse | LINE_INTENDED_USE | — | — |
| 71 | TrxLineLineNumber | LINE_NUMBER | — | ✅ |
| 72 | TrxLineLineRecoverable | LINE_RECOVERABLE | — | — |
| 73 | TrxLineLineType | LINE_TYPE | — | ✅ |
| 74 | TrxLineLinkToCustTrxLineId | LINK_TO_CUST_TRX_LINE_ID | — | — |
| 75 | TrxLineLinkToParentlineAttribute1 | LINK_TO_PARENTLINE_ATTRIBUTE1 | — | — |
| 76 | TrxLineLinkToParentlineAttribute10 | LINK_TO_PARENTLINE_ATTRIBUTE10 | — | — |
| 77 | TrxLineLinkToParentlineAttribute11 | LINK_TO_PARENTLINE_ATTRIBUTE11 | — | — |
| 78 | TrxLineLinkToParentlineAttribute12 | LINK_TO_PARENTLINE_ATTRIBUTE12 | — | — |
| 79 | TrxLineLinkToParentlineAttribute13 | LINK_TO_PARENTLINE_ATTRIBUTE13 | — | — |
| 80 | TrxLineLinkToParentlineAttribute14 | LINK_TO_PARENTLINE_ATTRIBUTE14 | — | — |
| 81 | TrxLineLinkToParentlineAttribute15 | LINK_TO_PARENTLINE_ATTRIBUTE15 | — | — |
| 82 | TrxLineLinkToParentlineAttribute2 | LINK_TO_PARENTLINE_ATTRIBUTE2 | — | — |
| 83 | TrxLineLinkToParentlineAttribute3 | LINK_TO_PARENTLINE_ATTRIBUTE3 | — | — |
| 84 | TrxLineLinkToParentlineAttribute4 | LINK_TO_PARENTLINE_ATTRIBUTE4 | — | — |
| 85 | TrxLineLinkToParentlineAttribute5 | LINK_TO_PARENTLINE_ATTRIBUTE5 | — | — |
| 86 | TrxLineLinkToParentlineAttribute6 | LINK_TO_PARENTLINE_ATTRIBUTE6 | — | — |
| 87 | TrxLineLinkToParentlineAttribute7 | LINK_TO_PARENTLINE_ATTRIBUTE7 | — | — |
| 88 | TrxLineLinkToParentlineAttribute8 | LINK_TO_PARENTLINE_ATTRIBUTE8 | — | — |
| 89 | TrxLineLinkToParentlineAttribute9 | LINK_TO_PARENTLINE_ATTRIBUTE9 | — | — |
| 90 | TrxLineLinkToParentlineContext | LINK_TO_PARENTLINE_CONTEXT | — | — |
| 91 | TrxLineLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 92 | TrxLineMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 93 | TrxLineMovementId | MOVEMENT_ID | — | — |
| 94 | TrxLineMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 95 | TrxLineOrgId | ORG_ID | — | — |
| 96 | TrxLineOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 97 | TrxLinePaymentSetId | PAYMENT_SET_ID | — | — |
| 98 | TrxLinePaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 99 | TrxLinePreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 100 | TrxLinePreviousCustomerTrxLineId | PREVIOUS_CUSTOMER_TRX_LINE_ID | — | — |
| 101 | TrxLineProductCategory | PRODUCT_CATEGORY | — | — |
| 102 | TrxLineProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 103 | TrxLineProductType | PRODUCT_TYPE | — | — |
| 104 | TrxLineProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 105 | TrxLineProgramId | PROGRAM_ID | — | — |
| 106 | TrxLineProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 107 | TrxLineQuantityCredited | QUANTITY_CREDITED | — | — |
| 108 | TrxLineQuantityInvoiced | QUANTITY_INVOICED | — | ✅ |
| 109 | TrxLineQuantityOrdered | QUANTITY_ORDERED | — | — |
| 110 | TrxLineReasonCode | REASON_CODE | — | — |
| 111 | TrxLineRequestId | REQUEST_ID | — | — |
| 112 | TrxLineRevenueAmount | REVENUE_AMOUNT | — | — |
| 113 | TrxLineRuleEndDate | RULE_END_DATE | — | — |
| 114 | TrxLineRuleStartDate | RULE_START_DATE | — | — |
| 115 | TrxLineSalesOrder | SALES_ORDER | — | — |
| 116 | TrxLineSalesOrderDate | SALES_ORDER_DATE | — | — |
| 117 | TrxLineSalesOrderLine | SALES_ORDER_LINE | — | — |
| 118 | TrxLineSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 119 | TrxLineSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 120 | TrxLineSalesTaxId | SALES_TAX_ID | — | — |
| 121 | TrxLineSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 122 | TrxLineShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 123 | TrxLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 124 | TrxLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 125 | TrxLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 126 | TrxLineSourceDataKey1 | SOURCE_DATA_KEY1 | — | — |
| 127 | TrxLineSourceDataKey2 | SOURCE_DATA_KEY2 | — | — |
| 128 | TrxLineSourceDataKey3 | SOURCE_DATA_KEY3 | — | — |
| 129 | TrxLineSourceDataKey4 | SOURCE_DATA_KEY4 | — | — |
| 130 | TrxLineSourceDataKey5 | SOURCE_DATA_KEY5 | — | — |
| 131 | TrxLineSourceDocumentLineId | SOURCE_DOCUMENT_LINE_ID | — | — |
| 132 | TrxLineSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 133 | TrxLineTaxAction | TAX_ACTION | — | — |
| 134 | TrxLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 135 | TrxLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 136 | TrxLineTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 137 | TrxLineTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 138 | TrxLineTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 139 | TrxLineTaxLineId | TAX_LINE_ID | — | — |
| 140 | TrxLineTaxPrecedence | TAX_PRECEDENCE | — | — |
| 141 | TrxLineTaxRate | TAX_RATE | — | — |
| 142 | TrxLineTaxRecoverable | TAX_RECOVERABLE | — | — |
| 143 | TrxLineTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 144 | TrxLineTaxableAmount | TAXABLE_AMOUNT | — | — |
| 145 | TrxLineTaxableFlag | TAXABLE_FLAG | — | — |
| 146 | TrxLineTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 147 | TrxLineTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 148 | TrxLineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 149 | TrxLineUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 150 | TrxLineUomCode | UOM_CODE | — | — |
| 151 | TrxLineUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 152 | TrxLineVatTaxId | VAT_TAX_ID | — | — |
| 153 | TrxLineWarehouseId | WAREHOUSE_ID | — | — |
| 154 | TrxLineWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_cust_trx_types_all|RA_CUST_TRX_TYPES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 2 | TransactionTypeDescription | DESCRIPTION | — | ✅ |
| 3 | TransactionTypeName | NAME | — | ✅ |
| 4 | TransactionTypeObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermTranslationPEOName | NAME | — | — |
| 2 | PaymentTermTranslationPEOTermId | TERM_ID | — | — |

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | — |
| 2 | EventEventDate | EVENT_DATE | — | — |
| 3 | EventEventId | EVENT_ID | — | — |
| 4 | EventEventNumber | EVENT_NUMBER | — | — |
| 5 | EventEventStatusCode | EVENT_STATUS_CODE | — | — |
| 6 | EventEventTypeCode | EVENT_TYPE_CODE | — | — |
| 7 | EventHasWarningsFlag | HAS_WARNINGS_FLAG | — | — |
| 8 | EventOnHoldFlag | ON_HOLD_FLAG | — | — |
| 9 | EventProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 10 | EventTransactionDate | TRANSACTION_DATE | — | — |
| 11 | EventUpgValidFlag | UPG_VALID_FLAG | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
