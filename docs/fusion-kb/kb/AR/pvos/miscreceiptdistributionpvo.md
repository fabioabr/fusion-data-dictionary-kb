---
id: DOC-AR-PVO-MiscReceiptDistributionPVO
doc_type: system-doc
title: "MiscReceiptDistributionPVO — PVO Accounts Receivable"
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
  - MiscReceiptDistributionPVO
  - miscreceiptdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MiscReceiptDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis de recebimentos diversos (miscellaneous receipts), que não estão vinculados a faturas de clientes. Permite contabilizar corretamente receitas financeiras, juros recebidos, reembolsos e outras entradas de caixa não operacionais.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.MiscReceiptDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1077 | 21 | 1 | 80 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 184 atributos (7 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 83 atributos (26 BICC)
- [[ar_collectors|AR_COLLECTORS]] — 11 atributos
- [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]] — 141 atributos (1 PKs, 24 BICC)
- [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]] — 12 atributos (2 BICC)
- [[ar_misc_cash_distributions_all|AR_MISC_CASH_DISTRIBUTIONS_ALL]] — 32 atributos (4 BICC)
- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 25 atributos (2 BICC)
- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 30 atributos (1 BICC)
- [[ce_bank_branches_v|CE_BANK_BRANCHES_V]] — 132 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 36 atributos (4 BICC)
- [[gl_ledgers|GL_LEDGERS]] — 2 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 98 atributos (4 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 7 atributos
- [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]] — 146 atributos
- [[xla_events|XLA_EVENTS]] — 35 atributos (1 BICC)
- [[zx_sco_rates|ZX_SCO_RATES]] — 42 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcptRcptRefIdAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | RcptRcptRefIdAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | RcptRcptRefIdBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | RcptRcptRefIdBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | RcptRcptRefIdBatchDate | BATCH_DATE | — | — |
| 6 | RcptRcptRefIdBatchId | BATCH_ID | — | — |
| 7 | RcptRcptRefIdBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | RcptRcptRefIdClosedDate | CLOSED_DATE | — | — |
| 9 | RcptRcptRefIdControlAmount | CONTROL_AMOUNT | — | — |
| 10 | RcptRcptRefIdControlCount | CONTROL_COUNT | — | — |
| 11 | RcptRcptRefIdCreatedBy | CREATED_BY | — | — |
| 12 | RcptRcptRefIdCreationDate | CREATION_DATE | — | — |
| 13 | RcptRcptRefIdCurrencyCode | CURRENCY_CODE | — | — |
| 14 | RcptRcptRefIdDepositDate | DEPOSIT_DATE | — | — |
| 15 | RcptRcptRefIdExchangeDate | EXCHANGE_DATE | — | — |
| 16 | RcptRcptRefIdExchangeRate | EXCHANGE_RATE | — | — |
| 17 | RcptRcptRefIdExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 18 | RcptRcptRefIdGlDate | GL_DATE | — | — |
| 19 | RcptRcptRefIdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | RcptRcptRefIdLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | RcptRcptRefIdLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | RcptRcptRefIdLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 23 | RcptRcptRefIdLockboxId | LOCKBOX_ID | — | — |
| 24 | RcptRcptRefIdMediaReference | MEDIA_REFERENCE | — | — |
| 25 | RcptRcptRefIdName | NAME | — | — |
| 26 | RcptRcptRefIdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | RcptRcptRefIdOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 28 | RcptRcptRefIdOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 29 | RcptRcptRefIdOrgId | ORG_ID | — | — |
| 30 | RcptRcptRefIdProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | RcptRcptRefIdProgramId | PROGRAM_ID | — | — |
| 32 | RcptRcptRefIdProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | RcptRcptRefIdPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | RcptRcptRefIdReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 35 | RcptRcptRefIdReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 36 | RcptRcptRefIdRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 37 | RcptRcptRefIdRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 38 | RcptRcptRefIdRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 39 | RcptRcptRefIdRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 40 | RcptRcptRefIdRequestId | REQUEST_ID | — | — |
| 41 | RcptRcptRefIdSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 42 | RcptRcptRefIdStatus | STATUS | — | — |
| 43 | RcptRcptRefIdTransmissionId | TRANSMISSION_ID | — | — |
| 44 | RcptRcptRefIdTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | RcptRcptRefIdType | TYPE | — | — |
| 46 | RcptRcptRefIdWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |
| 47 | RcptRcptRmitBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 48 | RcptRcptRmitBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 49 | RcptRcptRmitBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 50 | RcptRcptRmitBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 51 | RcptRcptRmitBatchBatchDate | BATCH_DATE | — | — |
| 52 | RcptRcptRmitBatchBatchId | BATCH_ID | — | — |
| 53 | RcptRcptRmitBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 54 | RcptRcptRmitBatchClosedDate | CLOSED_DATE | — | — |
| 55 | RcptRcptRmitBatchControlAmount | CONTROL_AMOUNT | — | — |
| 56 | RcptRcptRmitBatchControlCount | CONTROL_COUNT | — | — |
| 57 | RcptRcptRmitBatchCreatedBy | CREATED_BY | — | — |
| 58 | RcptRcptRmitBatchCreationDate | CREATION_DATE | — | — |
| 59 | RcptRcptRmitBatchCurrencyCode | CURRENCY_CODE | — | — |
| 60 | RcptRcptRmitBatchDepositDate | DEPOSIT_DATE | — | — |
| 61 | RcptRcptRmitBatchExchangeDate | EXCHANGE_DATE | — | — |
| 62 | RcptRcptRmitBatchExchangeRate | EXCHANGE_RATE | — | — |
| 63 | RcptRcptRmitBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 64 | RcptRcptRmitBatchGlDate | GL_DATE | — | — |
| 65 | RcptRcptRmitBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | RcptRcptRmitBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | RcptRcptRmitBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | RcptRcptRmitBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 69 | RcptRcptRmitBatchLockboxId | LOCKBOX_ID | — | — |
| 70 | RcptRcptRmitBatchMediaReference | MEDIA_REFERENCE | — | — |
| 71 | RcptRcptRmitBatchName | NAME | — | — |
| 72 | RcptRcptRmitBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | RcptRcptRmitBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 74 | RcptRcptRmitBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 75 | RcptRcptRmitBatchOrgId | ORG_ID | — | — |
| 76 | RcptRcptRmitBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 77 | RcptRcptRmitBatchProgramId | PROGRAM_ID | — | — |
| 78 | RcptRcptRmitBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 79 | RcptRcptRmitBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 80 | RcptRcptRmitBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 81 | RcptRcptRmitBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 82 | RcptRcptRmitBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 83 | RcptRcptRmitBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 84 | RcptRcptRmitBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 85 | RcptRcptRmitBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 86 | RcptRcptRmitBatchRequestId | REQUEST_ID | — | — |
| 87 | RcptRcptRmitBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 88 | RcptRcptRmitBatchStatus | STATUS | — | — |
| 89 | RcptRcptRmitBatchTransmissionId | TRANSMISSION_ID | — | — |
| 90 | RcptRcptRmitBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 91 | RcptRcptRmitBatchType | TYPE | — | — |
| 92 | RcptRcptRmitBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |
| 93 | ReceiptBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 94 | ReceiptBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 95 | ReceiptBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 96 | ReceiptBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 97 | ReceiptBatchBatchDate | BATCH_DATE | — | — |
| 98 | ReceiptBatchBatchId | BATCH_ID | — | ✅ |
| 99 | ReceiptBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 100 | ReceiptBatchClosedDate | CLOSED_DATE | — | — |
| 101 | ReceiptBatchControlAmount | CONTROL_AMOUNT | — | — |
| 102 | ReceiptBatchControlCount | CONTROL_COUNT | — | — |
| 103 | ReceiptBatchCreatedBy | CREATED_BY | — | — |
| 104 | ReceiptBatchCreationDate | CREATION_DATE | — | — |
| 105 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 106 | ReceiptBatchDepositDate | DEPOSIT_DATE | — | — |
| 107 | ReceiptBatchExchangeDate | EXCHANGE_DATE | — | — |
| 108 | ReceiptBatchExchangeRate | EXCHANGE_RATE | — | — |
| 109 | ReceiptBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 110 | ReceiptBatchGlDate | GL_DATE | — | — |
| 111 | ReceiptBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 112 | ReceiptBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 113 | ReceiptBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 114 | ReceiptBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 115 | ReceiptBatchLockboxId | LOCKBOX_ID | — | — |
| 116 | ReceiptBatchMediaReference | MEDIA_REFERENCE | — | — |
| 117 | ReceiptBatchName | NAME | — | ✅ |
| 118 | ReceiptBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 119 | ReceiptBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 120 | ReceiptBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 121 | ReceiptBatchOrgId | ORG_ID | — | — |
| 122 | ReceiptBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 123 | ReceiptBatchProgramId | PROGRAM_ID | — | — |
| 124 | ReceiptBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 125 | ReceiptBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 126 | ReceiptBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 127 | ReceiptBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 128 | ReceiptBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 129 | ReceiptBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 130 | ReceiptBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 131 | ReceiptBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 132 | ReceiptBatchRequestId | REQUEST_ID | — | — |
| 133 | ReceiptBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 134 | ReceiptBatchStatus | STATUS | — | ✅ |
| 135 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 136 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 137 | ReceiptBatchType | TYPE | — | — |
| 138 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |
| 139 | RemittanceBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 140 | RemittanceBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 141 | RemittanceBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 142 | RemittanceBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 143 | RemittanceBatchBatchDate | BATCH_DATE | — | — |
| 144 | RemittanceBatchBatchId | BATCH_ID | — | — |
| 145 | RemittanceBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 146 | RemittanceBatchClosedDate | CLOSED_DATE | — | — |
| 147 | RemittanceBatchControlAmount | CONTROL_AMOUNT | — | — |
| 148 | RemittanceBatchControlCount | CONTROL_COUNT | — | — |
| 149 | RemittanceBatchCreatedBy | CREATED_BY | — | — |
| 150 | RemittanceBatchCreationDate | CREATION_DATE | — | — |
| 151 | RemittanceBatchCurrencyCode | CURRENCY_CODE | — | — |
| 152 | RemittanceBatchDepositDate | DEPOSIT_DATE | — | — |
| 153 | RemittanceBatchExchangeDate | EXCHANGE_DATE | — | — |
| 154 | RemittanceBatchExchangeRate | EXCHANGE_RATE | — | — |
| 155 | RemittanceBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 156 | RemittanceBatchGlDate | GL_DATE | — | — |
| 157 | RemittanceBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 158 | RemittanceBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 159 | RemittanceBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 160 | RemittanceBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 161 | RemittanceBatchLockboxId | LOCKBOX_ID | — | — |
| 162 | RemittanceBatchMediaReference | MEDIA_REFERENCE | — | — |
| 163 | RemittanceBatchName | NAME | — | — |
| 164 | RemittanceBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 165 | RemittanceBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 166 | RemittanceBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 167 | RemittanceBatchOrgId | ORG_ID | — | — |
| 168 | RemittanceBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 169 | RemittanceBatchProgramId | PROGRAM_ID | — | — |
| 170 | RemittanceBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 171 | RemittanceBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 172 | RemittanceBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 173 | RemittanceBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 174 | RemittanceBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 175 | RemittanceBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 176 | RemittanceBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 177 | RemittanceBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 178 | RemittanceBatchRequestId | REQUEST_ID | — | — |
| 179 | RemittanceBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 180 | RemittanceBatchStatus | STATUS | — | — |
| 181 | RemittanceBatchTransmissionId | TRANSMISSION_ID | — | — |
| 182 | RemittanceBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 183 | RemittanceBatchType | TYPE | — | — |
| 184 | RemittanceBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptActualValueDate | ACTUAL_VALUE_DATE | — | ✅ |
| 2 | ReceiptAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 3 | ReceiptAmount | AMOUNT | — | — |
| 4 | ReceiptAnticipatedClearingDate | ANTICIPATED_CLEARING_DATE | — | ✅ |
| 5 | ReceiptApplicationNotes | APPLICATION_NOTES | — | — |
| 6 | ReceiptApprovalCode | APPROVAL_CODE | — | — |
| 7 | ReceiptAutoapplyFlag | AUTOAPPLY_FLAG | — | — |
| 8 | ReceiptAutomatchRequestId | AUTOMATCH_REQUEST_ID | — | — |
| 9 | ReceiptAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 10 | ReceiptCashReceiptId | CASH_RECEIPT_ID | — | ✅ |
| 11 | ReceiptCcErrorCode | CC_ERROR_CODE | — | — |
| 12 | ReceiptCcErrorFlag | CC_ERROR_FLAG | — | — |
| 13 | ReceiptCcErrorText | CC_ERROR_TEXT | — | — |
| 14 | ReceiptCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 15 | ReceiptCollectorId | COLLECTOR_ID | — | — |
| 16 | ReceiptComments | COMMENTS | — | ✅ |
| 17 | ReceiptConfirmedFlag | CONFIRMED_FLAG | — | ✅ |
| 18 | ReceiptCreatedBy | CREATED_BY | — | ✅ |
| 19 | ReceiptCreationDate | CREATION_DATE | — | ✅ |
| 20 | ReceiptCurrencyCode | CURRENCY_CODE | — | — |
| 21 | ReceiptCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 22 | ReceiptCustomerBankBranchId | CUSTOMER_BANK_BRANCH_ID | — | — |
| 23 | ReceiptCustomerReceiptReference | CUSTOMER_RECEIPT_REFERENCE | — | ✅ |
| 24 | ReceiptCustomerSiteUseId | CUSTOMER_SITE_USE_ID | — | — |
| 25 | ReceiptDepositDate | DEPOSIT_DATE | — | ✅ |
| 26 | ReceiptDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 27 | ReceiptDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 28 | ReceiptDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 29 | ReceiptExchangeDate | EXCHANGE_DATE | — | ✅ |
| 30 | ReceiptExchangeRate | EXCHANGE_RATE | — | ✅ |
| 31 | ReceiptExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 32 | ReceiptFactorDiscountAmount | FACTOR_DISCOUNT_AMOUNT | — | — |
| 33 | ReceiptIssueDate | ISSUE_DATE | — | — |
| 34 | ReceiptIssuerBankBranchId | ISSUER_BANK_BRANCH_ID | — | — |
| 35 | ReceiptIssuerName | ISSUER_NAME | — | — |
| 36 | ReceiptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ReceiptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ReceiptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | ReceiptLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 40 | ReceiptLogicalGroupReference | LOGICAL_GROUP_REFERENCE | — | — |
| 41 | ReceiptMiscPaymentSource | MISC_PAYMENT_SOURCE | — | ✅ |
| 42 | ReceiptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ReceiptOldCustomerBankAccountId | OLD_CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 44 | ReceiptOldCustomerBankBranchId | OLD_CUSTOMER_BANK_BRANCH_ID | — | — |
| 45 | ReceiptOldIssuerBankBranchId | OLD_ISSUER_BANK_BRANCH_ID | — | — |
| 46 | ReceiptOrgId | ORG_ID | — | — |
| 47 | ReceiptOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 48 | ReceiptPayFromCustomer | PAY_FROM_CUSTOMER | — | — |
| 49 | ReceiptPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 50 | ReceiptPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 51 | ReceiptPostmarkDate | POSTMARK_DATE | — | ✅ |
| 52 | ReceiptProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 53 | ReceiptProgramId | PROGRAM_ID | — | — |
| 54 | ReceiptProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 55 | ReceiptPromiseSource | PROMISE_SOURCE | — | — |
| 56 | ReceiptRecVersionNumber | REC_VERSION_NUMBER | — | — |
| 57 | ReceiptReceiptBatchId | RECEIPT_BATCH_ID | — | — |
| 58 | ReceiptReceiptDate | RECEIPT_DATE | — | ✅ |
| 59 | ReceiptReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 60 | ReceiptReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 61 | ReceiptReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 62 | ReceiptReconFlag | RECON_FLAG | — | — |
| 63 | ReceiptReferenceId | REFERENCE_ID | — | — |
| 64 | ReceiptReferenceType | REFERENCE_TYPE | — | ✅ |
| 65 | ReceiptRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 66 | ReceiptRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 67 | ReceiptRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 68 | ReceiptRequestId | REQUEST_ID | — | — |
| 69 | ReceiptResourceId | RESOURCE_ID | — | — |
| 70 | ReceiptReversalCategory | REVERSAL_CATEGORY | — | ✅ |
| 71 | ReceiptReversalComments | REVERSAL_COMMENTS | — | ✅ |
| 72 | ReceiptReversalDate | REVERSAL_DATE | — | ✅ |
| 73 | ReceiptReversalReasonCode | REVERSAL_REASON_CODE | — | ✅ |
| 74 | ReceiptSelectedForFactoringFlag | SELECTED_FOR_FACTORING_FLAG | — | — |
| 75 | ReceiptSelectedRemittanceBatchId | SELECTED_REMITTANCE_BATCH_ID | — | — |
| 76 | ReceiptSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 77 | ReceiptStatus | STATUS | — | — |
| 78 | ReceiptTaxRate | TAX_RATE | — | ✅ |
| 79 | ReceiptType | TYPE | — | ✅ |
| 80 | ReceiptUniqueReference | UNIQUE_REFERENCE | — | — |
| 81 | ReceiptUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 82 | ReceiptUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |
| 83 | ReceiptVatTaxId | VAT_TAX_ID | — | — |

### [[ar_collectors|AR_COLLECTORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CollectorsAlias | ALIAS | — | — |
| 2 | CollectorsCollectorId | COLLECTOR_ID | — | — |
| 3 | CollectorsDescription | DESCRIPTION | — | — |
| 4 | CollectorsEmployeeId | EMPLOYEE_ID | — | — |
| 5 | CollectorsInactiveDate | INACTIVE_DATE | — | — |
| 6 | CollectorsName | NAME | — | — |
| 7 | CollectorsResourceId | RESOURCE_ID | — | — |
| 8 | CollectorsResourceType | RESOURCE_TYPE | — | — |
| 9 | CollectorsSetId | SET_ID | — | — |
| 10 | CollectorsStatus | STATUS | — | — |
| 11 | CollectorsTelephoneNumber | TELEPHONE_NUMBER | — | — |

### [[ar_distributions_all|AR_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 2 | AdjustmentDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 3 | AdjustmentDistributionActivityBucket | ACTIVITY_BUCKET | — | — |
| 4 | AdjustmentDistributionAmountCr | AMOUNT_CR | — | — |
| 5 | AdjustmentDistributionAmountDr | AMOUNT_DR | — | — |
| 6 | AdjustmentDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | AdjustmentDistributionCreatedBy | CREATED_BY | — | — |
| 8 | AdjustmentDistributionCreationDate | CREATION_DATE | — | — |
| 9 | AdjustmentDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 10 | AdjustmentDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 11 | AdjustmentDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 12 | AdjustmentDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 13 | AdjustmentDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 14 | AdjustmentDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 15 | AdjustmentDistributionFromAmountCr | FROM_AMOUNT_CR | — | — |
| 16 | AdjustmentDistributionFromAmountDr | FROM_AMOUNT_DR | — | — |
| 17 | AdjustmentDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | AdjustmentDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | AdjustmentDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | AdjustmentDistributionLineId | LINE_ID | — | — |
| 21 | AdjustmentDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 22 | AdjustmentDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AdjustmentDistributionOrgId | ORG_ID | — | — |
| 24 | AdjustmentDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 25 | AdjustmentDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 26 | AdjustmentDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 27 | AdjustmentDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 28 | AdjustmentDistributionRefLineId | REF_LINE_ID | — | — |
| 29 | AdjustmentDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 30 | AdjustmentDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 31 | AdjustmentDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 32 | AdjustmentDistributionSourceId | SOURCE_ID | — | — |
| 33 | AdjustmentDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 34 | AdjustmentDistributionSourceTable | SOURCE_TABLE | — | — |
| 35 | AdjustmentDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 36 | AdjustmentDistributionSourceType | SOURCE_TYPE | — | — |
| 37 | AdjustmentDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 38 | AdjustmentDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 39 | AdjustmentDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 40 | AdjustmentDistributionTaxId | TAX_ID | — | — |
| 41 | AdjustmentDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 42 | AdjustmentDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 43 | AdjustmentDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 44 | AdjustmentDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 45 | AdjustmentDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 46 | AdjustmentDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 47 | AdjustmentDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |
| 48 | CashDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | ✅ |
| 49 | CashDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | ✅ |
| 50 | CashDistributionActivityBucket | ACTIVITY_BUCKET | — | ✅ |
| 51 | CashDistributionAmountCr | AMOUNT_CR | — | ✅ |
| 52 | CashDistributionAmountDr | AMOUNT_DR | — | ✅ |
| 53 | CashDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 54 | CashDistributionCreatedBy | CREATED_BY | — | — |
| 55 | CashDistributionCreationDate | CREATION_DATE | — | — |
| 56 | CashDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 57 | CashDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 58 | CashDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 59 | CashDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 60 | CashDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | ✅ |
| 61 | CashDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | ✅ |
| 62 | CashDistributionFromAmountCr | FROM_AMOUNT_CR | — | ✅ |
| 63 | CashDistributionFromAmountDr | FROM_AMOUNT_DR | — | ✅ |
| 64 | CashDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | CashDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | CashDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | CashDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 68 | CashDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | CashDistributionOrgId | ORG_ID | — | — |
| 70 | CashDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | ✅ |
| 71 | CashDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 72 | CashDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 73 | CashDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 74 | CashDistributionRefLineId | REF_LINE_ID | — | — |
| 75 | CashDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 76 | CashDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 77 | CashDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 78 | CashDistributionSourceId | SOURCE_ID | — | ✅ |
| 79 | CashDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 80 | CashDistributionSourceTable | SOURCE_TABLE | — | ✅ |
| 81 | CashDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 82 | CashDistributionSourceType | SOURCE_TYPE | — | ✅ |
| 83 | CashDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 84 | CashDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 85 | CashDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 86 | CashDistributionTaxId | TAX_ID | — | — |
| 87 | CashDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 88 | CashDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | ✅ |
| 89 | CashDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | ✅ |
| 90 | CashDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | ✅ |
| 91 | CashDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | ✅ |
| 92 | CashDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 93 | CashDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |
| 94 | LineId | LINE_ID | 🔑 | ✅ |
| 95 | ReverseDistributionAcctdAmountCr | ACCTD_AMOUNT_CR | — | — |
| 96 | ReverseDistributionAcctdAmountDr | ACCTD_AMOUNT_DR | — | — |
| 97 | ReverseDistributionActivityBucket | ACTIVITY_BUCKET | — | — |
| 98 | ReverseDistributionAmountCr | AMOUNT_CR | — | — |
| 99 | ReverseDistributionAmountDr | AMOUNT_DR | — | — |
| 100 | ReverseDistributionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 101 | ReverseDistributionCreatedBy | CREATED_BY | — | — |
| 102 | ReverseDistributionCreationDate | CREATION_DATE | — | — |
| 103 | ReverseDistributionCurrencyCode | CURRENCY_CODE | — | — |
| 104 | ReverseDistributionCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | — |
| 105 | ReverseDistributionCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 106 | ReverseDistributionCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 107 | ReverseDistributionFromAcctdAmountCr | FROM_ACCTD_AMOUNT_CR | — | — |
| 108 | ReverseDistributionFromAcctdAmountDr | FROM_ACCTD_AMOUNT_DR | — | — |
| 109 | ReverseDistributionFromAmountCr | FROM_AMOUNT_CR | — | — |
| 110 | ReverseDistributionFromAmountDr | FROM_AMOUNT_DR | — | — |
| 111 | ReverseDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 112 | ReverseDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 113 | ReverseDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 114 | ReverseDistributionLineId | LINE_ID | — | — |
| 115 | ReverseDistributionLocationSegmentId | LOCATION_SEGMENT_ID | — | — |
| 116 | ReverseDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 117 | ReverseDistributionOrgId | ORG_ID | — | — |
| 118 | ReverseDistributionRefAccountClass | REF_ACCOUNT_CLASS | — | — |
| 119 | ReverseDistributionRefCustTrxLineGlDistId | REF_CUST_TRX_LINE_GL_DIST_ID | — | — |
| 120 | ReverseDistributionRefCustomerTrxLineId | REF_CUSTOMER_TRX_LINE_ID | — | — |
| 121 | ReverseDistributionRefDistCcid | REF_DIST_CCID | — | — |
| 122 | ReverseDistributionRefLineId | REF_LINE_ID | — | — |
| 123 | ReverseDistributionRefMfDistFlag | REF_MF_DIST_FLAG | — | — |
| 124 | ReverseDistributionReversalFlag | REVERSAL_FLAG | — | — |
| 125 | ReverseDistributionReversedSourceId | REVERSED_SOURCE_ID | — | — |
| 126 | ReverseDistributionSourceId | SOURCE_ID | — | — |
| 127 | ReverseDistributionSourceIdSecondary | SOURCE_ID_SECONDARY | — | — |
| 128 | ReverseDistributionSourceTable | SOURCE_TABLE | — | — |
| 129 | ReverseDistributionSourceTableSecondary | SOURCE_TABLE_SECONDARY | — | — |
| 130 | ReverseDistributionSourceType | SOURCE_TYPE | — | — |
| 131 | ReverseDistributionSourceTypeSecondary | SOURCE_TYPE_SECONDARY | — | — |
| 132 | ReverseDistributionTaxCodeId | TAX_CODE_ID | — | — |
| 133 | ReverseDistributionTaxGroupCodeId | TAX_GROUP_CODE_ID | — | — |
| 134 | ReverseDistributionTaxId | TAX_ID | — | — |
| 135 | ReverseDistributionTaxLinkId | TAX_LINK_ID | — | — |
| 136 | ReverseDistributionTaxableAccountedCr | TAXABLE_ACCOUNTED_CR | — | — |
| 137 | ReverseDistributionTaxableAccountedDr | TAXABLE_ACCOUNTED_DR | — | — |
| 138 | ReverseDistributionTaxableEnteredCr | TAXABLE_ENTERED_CR | — | — |
| 139 | ReverseDistributionTaxableEnteredDr | TAXABLE_ENTERED_DR | — | — |
| 140 | ReverseDistributionThirdPartyId | THIRD_PARTY_ID | — | — |
| 141 | ReverseDistributionThirdPartySubId | THIRD_PARTY_SUB_ID | — | — |

### [[ar_distribution_sets_all|AR_DISTRIBUTION_SETS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionSetCreatedBy | CREATED_BY | — | — |
| 2 | DistributionSetCreationDate | CREATION_DATE | — | — |
| 3 | DistributionSetDescription | DESCRIPTION | — | — |
| 4 | DistributionSetDistributionSetId | DISTRIBUTION_SET_ID | — | — |
| 5 | DistributionSetDistributionSetName | DISTRIBUTION_SET_NAME | — | ✅ |
| 6 | DistributionSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DistributionSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DistributionSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DistributionSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DistributionSetOrgId | ORG_ID | — | — |
| 11 | DistributionSetStatus | STATUS | — | — |
| 12 | DistributionSetTotalPercentDistribution | TOTAL_PERCENT_DISTRIBUTION | — | — |

### [[ar_misc_cash_distributions_all|AR_MISC_CASH_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MiscReceiptDistAcctdAmount | ACCTD_AMOUNT | — | — |
| 2 | MiscReceiptDistAmount | AMOUNT | — | — |
| 3 | MiscReceiptDistApplyDate | APPLY_DATE | — | — |
| 4 | MiscReceiptDistCashReceiptHistoryId | CASH_RECEIPT_HISTORY_ID | — | — |
| 5 | MiscReceiptDistCashReceiptId | CASH_RECEIPT_ID | — | — |
| 6 | MiscReceiptDistCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | MiscReceiptDistComments | COMMENTS | — | — |
| 8 | MiscReceiptDistCreatedBy | CREATED_BY | — | — |
| 9 | MiscReceiptDistCreatedFrom | CREATED_FROM | — | — |
| 10 | MiscReceiptDistCreationDate | CREATION_DATE | — | — |
| 11 | MiscReceiptDistEventId | EVENT_ID | — | — |
| 12 | MiscReceiptDistGlDate | GL_DATE | — | ✅ |
| 13 | MiscReceiptDistGlPostedDate | GL_POSTED_DATE | — | — |
| 14 | MiscReceiptDistLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | MiscReceiptDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | MiscReceiptDistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | MiscReceiptDistMiscCashDistributionId | MISC_CASH_DISTRIBUTION_ID | — | — |
| 18 | MiscReceiptDistMrcAcctdAmount | MRC_ACCTD_AMOUNT | — | — |
| 19 | MiscReceiptDistMrcGlPostedDate | MRC_GL_POSTED_DATE | — | — |
| 20 | MiscReceiptDistMrcPostingControlId | MRC_POSTING_CONTROL_ID | — | — |
| 21 | MiscReceiptDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | MiscReceiptDistOrgId | ORG_ID | — | — |
| 23 | MiscReceiptDistPercent | PERCENT | — | ✅ |
| 24 | MiscReceiptDistPostingControlId | POSTING_CONTROL_ID | — | ✅ |
| 25 | MiscReceiptDistProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 26 | MiscReceiptDistProgramId | PROGRAM_ID | — | — |
| 27 | MiscReceiptDistProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 28 | MiscReceiptDistRequestId | REQUEST_ID | — | — |
| 29 | MiscReceiptDistReversalGlDate | REVERSAL_GL_DATE | — | — |
| 30 | MiscReceiptDistSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 31 | MiscReceiptDistUssglTransactionCode | USSGL_TRANSACTION_CODE | — | — |
| 32 | MiscReceiptDistUssglTransactionCodeContext | USSGL_TRANSACTION_CODE_CONTEXT | — | — |

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcptReceivableActAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | — |
| 2 | RcptReceivableActAssetTaxCode | ASSET_TAX_CODE | — | — |
| 3 | RcptReceivableActCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | RcptReceivableActCreatedBy | CREATED_BY | — | — |
| 5 | RcptReceivableActCreationDate | CREATION_DATE | — | — |
| 6 | RcptReceivableActDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | — |
| 7 | RcptReceivableActDescription | DESCRIPTION | — | — |
| 8 | RcptReceivableActEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | RcptReceivableActGlAccountSource | GL_ACCOUNT_SOURCE | — | — |
| 10 | RcptReceivableActInactiveDate | INACTIVE_DATE | — | — |
| 11 | RcptReceivableActLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RcptReceivableActLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RcptReceivableActLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | RcptReceivableActLiabilityTaxCode | LIABILITY_TAX_CODE | — | — |
| 15 | RcptReceivableActName | NAME | — | ✅ |
| 16 | RcptReceivableActObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | RcptReceivableActOrgId | ORG_ID | — | — |
| 18 | RcptReceivableActReceivablesTrxId | RECEIVABLES_TRX_ID | — | — |
| 19 | RcptReceivableActRiskEliminationDays | RISK_ELIMINATION_DAYS | — | — |
| 20 | RcptReceivableActSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 21 | RcptReceivableActStartDateActive | START_DATE_ACTIVE | — | — |
| 22 | RcptReceivableActStatus | STATUS | — | — |
| 23 | RcptReceivableActTaxCodeSource | TAX_CODE_SOURCE | — | — |
| 24 | RcptReceivableActTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | — |
| 25 | RcptReceivableActType | TYPE | — | — |

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccUseApUseEnableFlag | AP_USE_ENABLE_FLAG | — | — |
| 2 | BankAccUseArUseEnableFlag | AR_USE_ENABLE_FLAG | — | — |
| 3 | BankAccUseAuthorizedFlag | AUTHORIZED_FLAG | — | — |
| 4 | BankAccUseBankAccountId | BANK_ACCOUNT_ID | — | — |
| 5 | BankAccUseBankAcctUseId | BANK_ACCT_USE_ID | — | — |
| 6 | BankAccUseCreatedBy | CREATED_BY | — | — |
| 7 | BankAccUseCreationDate | CREATION_DATE | — | — |
| 8 | BankAccUseDefaultAccountFlag | DEFAULT_ACCOUNT_FLAG | — | — |
| 9 | BankAccUseEftScriptName | EFT_SCRIPT_NAME | — | — |
| 10 | BankAccUseEndDate | END_DATE | — | — |
| 11 | BankAccUseFundingLimitCode | FUNDING_LIMIT_CODE | — | — |
| 12 | BankAccUseInvestmentLimitCode | INVESTMENT_LIMIT_CODE | — | — |
| 13 | BankAccUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | BankAccUseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | BankAccUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | BankAccUseLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | BankAccUseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | BankAccUseOrgId | ORG_ID | — | — |
| 19 | BankAccUseOrgPartyId | ORG_PARTY_ID | — | — |
| 20 | BankAccUsePayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | — |
| 21 | BankAccUsePortfolioCode | PORTFOLIO_CODE | — | — |
| 22 | BankAccUsePricingModel | PRICING_MODEL | — | — |
| 23 | BankAccUsePrimaryFlag | PRIMARY_FLAG | — | — |
| 24 | BankAccUseProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 25 | BankAccUseProgramId | PROGRAM_ID | — | — |
| 26 | BankAccUseProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 27 | BankAccUseRequestId | REQUEST_ID | — | — |
| 28 | BankAccUseXtrBankAccountReference | XTR_BANK_ACCOUNT_REFERENCE | — | — |
| 29 | BankAccUseXtrDefaultSettlementFlag | XTR_DEFAULT_SETTLEMENT_FLAG | — | — |
| 30 | BankAccUseXtrUseEnableFlag | XTR_USE_ENABLE_FLAG | — | — |

### [[ce_bank_branches_v|CE_BANK_BRANCHES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 2 | CustomerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 3 | CustomerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 4 | CustomerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 5 | CustomerBankBranchBankBranchName | BANK_BRANCH_NAME | — | ✅ |
| 6 | CustomerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 7 | CustomerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 8 | CustomerBankBranchBankCode | BANK_CODE | — | — |
| 9 | CustomerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 10 | CustomerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 11 | CustomerBankBranchBankName | BANK_NAME | — | — |
| 12 | CustomerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 13 | CustomerBankBranchBankNumber | BANK_NUMBER | — | — |
| 14 | CustomerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 15 | CustomerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 16 | CustomerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 17 | CustomerBankBranchCity | CITY | — | — |
| 18 | CustomerBankBranchCountry | COUNTRY | — | — |
| 19 | CustomerBankBranchCountryName | COUNTRY_NAME | — | — |
| 20 | CustomerBankBranchDescription | DESCRIPTION | — | — |
| 21 | CustomerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 22 | CustomerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 23 | CustomerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 24 | CustomerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 25 | CustomerBankBranchEndDate | END_DATE | — | — |
| 26 | CustomerBankBranchPkId | PK_ID | — | — |
| 27 | CustomerBankBranchProvince | PROVINCE | — | — |
| 28 | CustomerBankBranchRfc | RFC | — | — |
| 29 | CustomerBankBranchRowId | ROW_ID | — | — |
| 30 | CustomerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 31 | CustomerBankBranchStartDate | START_DATE | — | — |
| 32 | CustomerBankBranchState | STATE | — | — |
| 33 | CustomerBankBranchZip | ZIP | — | — |
| 34 | IssuerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 35 | IssuerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 36 | IssuerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 37 | IssuerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 38 | IssuerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 39 | IssuerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 40 | IssuerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 41 | IssuerBankBranchBankCode | BANK_CODE | — | — |
| 42 | IssuerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 43 | IssuerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 44 | IssuerBankBranchBankName | BANK_NAME | — | — |
| 45 | IssuerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 46 | IssuerBankBranchBankNumber | BANK_NUMBER | — | — |
| 47 | IssuerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 48 | IssuerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 49 | IssuerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 50 | IssuerBankBranchCity | CITY | — | — |
| 51 | IssuerBankBranchCountry | COUNTRY | — | — |
| 52 | IssuerBankBranchCountryName | COUNTRY_NAME | — | — |
| 53 | IssuerBankBranchDescription | DESCRIPTION | — | — |
| 54 | IssuerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 55 | IssuerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 56 | IssuerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 57 | IssuerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 58 | IssuerBankBranchEndDate | END_DATE | — | — |
| 59 | IssuerBankBranchPkId | PK_ID | — | — |
| 60 | IssuerBankBranchProvince | PROVINCE | — | — |
| 61 | IssuerBankBranchRfc | RFC | — | — |
| 62 | IssuerBankBranchRowId | ROW_ID | — | — |
| 63 | IssuerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 64 | IssuerBankBranchStartDate | START_DATE | — | — |
| 65 | IssuerBankBranchState | STATE | — | — |
| 66 | IssuerBankBranchZip | ZIP | — | — |
| 67 | OldCustomerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 68 | OldCustomerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 69 | OldCustomerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 70 | OldCustomerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 71 | OldCustomerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 72 | OldCustomerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 73 | OldCustomerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 74 | OldCustomerBankBranchBankCode | BANK_CODE | — | — |
| 75 | OldCustomerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 76 | OldCustomerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 77 | OldCustomerBankBranchBankName | BANK_NAME | — | — |
| 78 | OldCustomerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 79 | OldCustomerBankBranchBankNumber | BANK_NUMBER | — | — |
| 80 | OldCustomerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 81 | OldCustomerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 82 | OldCustomerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 83 | OldCustomerBankBranchCity | CITY | — | — |
| 84 | OldCustomerBankBranchCountry | COUNTRY | — | — |
| 85 | OldCustomerBankBranchCountryName | COUNTRY_NAME | — | — |
| 86 | OldCustomerBankBranchDescription | DESCRIPTION | — | — |
| 87 | OldCustomerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 88 | OldCustomerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 89 | OldCustomerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 90 | OldCustomerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 91 | OldCustomerBankBranchEndDate | END_DATE | — | — |
| 92 | OldCustomerBankBranchPkId | PK_ID | — | — |
| 93 | OldCustomerBankBranchProvince | PROVINCE | — | — |
| 94 | OldCustomerBankBranchRfc | RFC | — | — |
| 95 | OldCustomerBankBranchRowId | ROW_ID | — | — |
| 96 | OldCustomerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 97 | OldCustomerBankBranchStartDate | START_DATE | — | — |
| 98 | OldCustomerBankBranchState | STATE | — | — |
| 99 | OldCustomerBankBranchZip | ZIP | — | — |
| 100 | OldIssuerBankBranchAddressLine1 | ADDRESS_LINE1 | — | — |
| 101 | OldIssuerBankBranchAddressLine2 | ADDRESS_LINE2 | — | — |
| 102 | OldIssuerBankBranchAddressLine3 | ADDRESS_LINE3 | — | — |
| 103 | OldIssuerBankBranchAddressLine4 | ADDRESS_LINE4 | — | — |
| 104 | OldIssuerBankBranchBankBranchName | BANK_BRANCH_NAME | — | — |
| 105 | OldIssuerBankBranchBankBranchNameAlt | BANK_BRANCH_NAME_ALT | — | — |
| 106 | OldIssuerBankBranchBankBranchType | BANK_BRANCH_TYPE | — | — |
| 107 | OldIssuerBankBranchBankCode | BANK_CODE | — | — |
| 108 | OldIssuerBankBranchBankHomeCountry | BANK_HOME_COUNTRY | — | — |
| 109 | OldIssuerBankBranchBankInstitutionType | BANK_INSTITUTION_TYPE | — | — |
| 110 | OldIssuerBankBranchBankName | BANK_NAME | — | — |
| 111 | OldIssuerBankBranchBankNameAlt | BANK_NAME_ALT | — | — |
| 112 | OldIssuerBankBranchBankNumber | BANK_NUMBER | — | — |
| 113 | OldIssuerBankBranchBankPartyId | BANK_PARTY_ID | — | — |
| 114 | OldIssuerBankBranchBranchNumber | BRANCH_NUMBER | — | — |
| 115 | OldIssuerBankBranchBranchPartyId | BRANCH_PARTY_ID | — | — |
| 116 | OldIssuerBankBranchCity | CITY | — | — |
| 117 | OldIssuerBankBranchCountry | COUNTRY | — | — |
| 118 | OldIssuerBankBranchCountryName | COUNTRY_NAME | — | — |
| 119 | OldIssuerBankBranchDescription | DESCRIPTION | — | — |
| 120 | OldIssuerBankBranchEdiIdNumber | EDI_ID_NUMBER | — | — |
| 121 | OldIssuerBankBranchEdiLocation | EDI_LOCATION | — | — |
| 122 | OldIssuerBankBranchEftSwiftCode | EFT_SWIFT_CODE | — | — |
| 123 | OldIssuerBankBranchEftUserNumber | EFT_USER_NUMBER | — | — |
| 124 | OldIssuerBankBranchEndDate | END_DATE | — | — |
| 125 | OldIssuerBankBranchPkId | PK_ID | — | — |
| 126 | OldIssuerBankBranchProvince | PROVINCE | — | — |
| 127 | OldIssuerBankBranchRfc | RFC | — | — |
| 128 | OldIssuerBankBranchRowId | ROW_ID | — | — |
| 129 | OldIssuerBankBranchShortBankName | SHORT_BANK_NAME | — | — |
| 130 | OldIssuerBankBranchStartDate | START_DATE | — | — |
| 131 | OldIssuerBankBranchState | STATE | — | — |
| 132 | OldIssuerBankBranchZip | ZIP | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqName | NAME | — | ✅ |
| 5 | DocSeqTableName | TABLE_NAME | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DailyConversionTypeConversionType | CONVERSION_TYPE | — | — |
| 2 | DailyConversionTypeCreatedBy | CREATED_BY | — | — |
| 3 | DailyConversionTypeCreationDate | CREATION_DATE | — | — |
| 4 | DailyConversionTypeDescription | DESCRIPTION | — | — |
| 5 | DailyConversionTypeEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | DailyConversionTypeEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | DailyConversionTypeFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | DailyConversionTypeFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | DailyConversionTypeFemScenario | FEM_SCENARIO | — | — |
| 10 | DailyConversionTypeFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | DailyConversionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | DailyConversionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | DailyConversionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | DailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DailyConversionTypePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | DailyConversionTypeSecurityFlag | SECURITY_FLAG | — | — |
| 17 | DailyConversionTypeUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 18 | DailyConversionTypeUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |
| 19 | ReceiptDailyRateConversionType | CONVERSION_TYPE | — | — |
| 20 | ReceiptDailyRateCreatedBy | CREATED_BY | — | — |
| 21 | ReceiptDailyRateCreationDate | CREATION_DATE | — | — |
| 22 | ReceiptDailyRateDescription | DESCRIPTION | — | — |
| 23 | ReceiptDailyRateEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 24 | ReceiptDailyRateEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 25 | ReceiptDailyRateFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 26 | ReceiptDailyRateFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 27 | ReceiptDailyRateFemScenario | FEM_SCENARIO | — | — |
| 28 | ReceiptDailyRateFemTimeframe | FEM_TIMEFRAME | — | — |
| 29 | ReceiptDailyRateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | ReceiptDailyRateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | ReceiptDailyRateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | ReceiptDailyRateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | ReceiptDailyRatePivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 34 | ReceiptDailyRateSecurityFlag | SECURITY_FLAG | — | — |
| 35 | ReceiptDailyRateUserConversionType | USER_CONVERSION_TYPE | — | ✅ |
| 36 | ReceiptDailyRateUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | LedgersLedgerId | LEDGER_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustAcctAccountName | ACCOUNT_NAME | — | — |
| 3 | CustAcctAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | CustAcctArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | CustAcctAutopayFlag | AUTOPAY_FLAG | — | — |
| 6 | CustAcctComments | COMMENTS | — | — |
| 7 | CustAcctCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | CustAcctCreatedBy | CREATED_BY | — | — |
| 9 | CustAcctCreatedByModule | CREATED_BY_MODULE | — | — |
| 10 | CustAcctCreationDate | CREATION_DATE | — | — |
| 11 | CustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 12 | CustAcctCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 13 | CustAcctCustomerType | CUSTOMER_TYPE | — | — |
| 14 | CustAcctDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 15 | CustAcctDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 16 | CustAcctHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 17 | CustAcctHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 18 | CustAcctLastBatchId | LAST_BATCH_ID | — | — |
| 19 | CustAcctLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CustAcctLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | CustAcctLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | CustAcctNpaNumber | NPA_NUMBER | — | — |
| 23 | CustAcctOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 24 | CustAcctPartyId | PARTY_ID | — | — |
| 25 | CustAcctSellingPartyId | SELLING_PARTY_ID | — | — |
| 26 | CustAcctSourceCode | SOURCE_CODE | — | — |
| 27 | CustAcctStatus | STATUS | — | — |
| 28 | CustAcctStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 29 | CustAcctTaxCode | TAX_CODE | — | — |
| 30 | CustAcctTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 31 | CustAcctTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtBankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | ExtBankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | ExtBankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | ExtBankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | ExtBankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | ExtBankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | ExtBankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | ExtBankAccountBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | ExtBankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | ExtBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 11 | ExtBankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | ExtBankAccountBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 13 | ExtBankAccountBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 14 | ExtBankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 15 | ExtBankAccountBankId | BANK_ID | — | — |
| 16 | ExtBankAccountBranchId | BRANCH_ID | — | — |
| 17 | ExtBankAccountCheckDigits | CHECK_DIGITS | — | — |
| 18 | ExtBankAccountCountryCode | COUNTRY_CODE | — | — |
| 19 | ExtBankAccountCreatedBy | CREATED_BY | — | — |
| 20 | ExtBankAccountCreationDate | CREATION_DATE | — | — |
| 21 | ExtBankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 22 | ExtBankAccountDescription | DESCRIPTION | — | — |
| 23 | ExtBankAccountEncrypted | ENCRYPTED | — | — |
| 24 | ExtBankAccountEndDate | END_DATE | — | — |
| 25 | ExtBankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 26 | ExtBankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 27 | ExtBankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 28 | ExtBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 29 | ExtBankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 30 | ExtBankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 31 | ExtBankAccountIban | IBAN | — | — |
| 32 | ExtBankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 33 | ExtBankAccountIbanHash2 | IBAN_HASH2 | — | — |
| 34 | ExtBankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 35 | ExtBankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | ExtBankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | ExtBankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | ExtBankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 39 | ExtBankAccountMaskedIban | MASKED_IBAN | — | — |
| 40 | ExtBankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | ExtBankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 42 | ExtBankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 43 | ExtBankAccountProgramId | PROGRAM_ID | — | — |
| 44 | ExtBankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 45 | ExtBankAccountRequestId | REQUEST_ID | — | — |
| 46 | ExtBankAccountSaltVersion | SALT_VERSION | — | — |
| 47 | ExtBankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 48 | ExtBankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 49 | ExtBankAccountStartDate | START_DATE | — | — |
| 50 | OldCustBankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 51 | OldCustBankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 52 | OldCustBankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 53 | OldCustBankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 54 | OldCustBankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 55 | OldCustBankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 56 | OldCustBankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 57 | OldCustBankAccountBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 58 | OldCustBankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 59 | OldCustBankAccountBankAccountNum | BANK_ACCOUNT_NUM | — | — |
| 60 | OldCustBankAccountBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 61 | OldCustBankAccountBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 62 | OldCustBankAccountBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 63 | OldCustBankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 64 | OldCustBankAccountBankId | BANK_ID | — | — |
| 65 | OldCustBankAccountBranchId | BRANCH_ID | — | — |
| 66 | OldCustBankAccountCheckDigits | CHECK_DIGITS | — | — |
| 67 | OldCustBankAccountCountryCode | COUNTRY_CODE | — | — |
| 68 | OldCustBankAccountCreatedBy | CREATED_BY | — | — |
| 69 | OldCustBankAccountCreationDate | CREATION_DATE | — | — |
| 70 | OldCustBankAccountCurrencyCode | CURRENCY_CODE | — | — |
| 71 | OldCustBankAccountDescription | DESCRIPTION | — | — |
| 72 | OldCustBankAccountEncrypted | ENCRYPTED | — | — |
| 73 | OldCustBankAccountEndDate | END_DATE | — | — |
| 74 | OldCustBankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 75 | OldCustBankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 76 | OldCustBankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 77 | OldCustBankAccountExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 78 | OldCustBankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 79 | OldCustBankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 80 | OldCustBankAccountIban | IBAN | — | — |
| 81 | OldCustBankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 82 | OldCustBankAccountIbanHash2 | IBAN_HASH2 | — | — |
| 83 | OldCustBankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 84 | OldCustBankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | OldCustBankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | OldCustBankAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | OldCustBankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 88 | OldCustBankAccountMaskedIban | MASKED_IBAN | — | — |
| 89 | OldCustBankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 90 | OldCustBankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 91 | OldCustBankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 92 | OldCustBankAccountProgramId | PROGRAM_ID | — | — |
| 93 | OldCustBankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 94 | OldCustBankAccountRequestId | REQUEST_ID | — | — |
| 95 | OldCustBankAccountSaltVersion | SALT_VERSION | — | — |
| 96 | OldCustBankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 97 | OldCustBankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 98 | OldCustBankAccountStartDate | START_DATE | — | — |

### [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtnAdditionalInfo | ADDITIONAL_INFO | — | — |
| 2 | TrxExtnEncrypted | ENCRYPTED | — | — |
| 3 | TrxExtnInstrSecCodeLength | INSTR_SEC_CODE_LENGTH | — | — |
| 4 | TrxExtnInstrumentSecurityCode | INSTRUMENT_SECURITY_CODE | — | — |
| 5 | TrxExtnPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 6 | TrxExtnPaymentSystemOrderNumber | PAYMENT_SYSTEM_ORDER_NUMBER | — | ✅ |
| 7 | TrxExtnPoLineNumber | PO_LINE_NUMBER | — | — |
| 8 | TrxExtnPoNumber | PO_NUMBER | — | — |
| 9 | TrxExtnTrxnExtensionId | TRXN_EXTENSION_ID | — | — |
| 10 | TrxExtnTrxnRefNumber1 | TRXN_REF_NUMBER1 | — | — |
| 11 | TrxExtnTrxnRefNumber2 | TRXN_REF_NUMBER2 | — | — |
| 12 | TrxExtnVoiceAuthorizationCode | VOICE_AUTHORIZATION_CODE | — | — |
| 13 | TrxExtnVoiceAuthorizationDate | VOICE_AUTHORIZATION_DATE | — | — |
| 14 | TrxExtnVoiceAuthorizationFlag | VOICE_AUTHORIZATION_FLAG | — | — |

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
| 1 | UserCreatedByUserGuid | USER_GUID | — | — |
| 2 | UserCreatedByUserId | USER_ID | — | — |
| 3 | UserCreatedByUsername | USERNAME | — | — |
| 4 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 5 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 6 | UserUpdatedByUserId | USER_ID | — | — |
| 7 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_customer_trx_lines_all|RA_CUSTOMER_TRX_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxLineRefCustAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 2 | TrxLineRefCustAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 3 | TrxLineRefCustAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 4 | TrxLineRefCustAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 5 | TrxLineRefCustAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 6 | TrxLineRefCustAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 7 | TrxLineRefCustAssessableValue | ASSESSABLE_VALUE | — | — |
| 8 | TrxLineRefCustAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 9 | TrxLineRefCustAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 10 | TrxLineRefCustAutotax | AUTOTAX | — | — |
| 11 | TrxLineRefCustChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 12 | TrxLineRefCustChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 13 | TrxLineRefCustCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 14 | TrxLineRefCustDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 15 | TrxLineRefCustDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 16 | TrxLineRefCustDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 17 | TrxLineRefCustDescription | DESCRIPTION | — | — |
| 18 | TrxLineRefCustExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 19 | TrxLineRefCustExtendedAmount | EXTENDED_AMOUNT | — | — |
| 20 | TrxLineRefCustFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 21 | TrxLineRefCustFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 22 | TrxLineRefCustFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 23 | TrxLineRefCustFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 24 | TrxLineRefCustFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 25 | TrxLineRefCustFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 26 | TrxLineRefCustFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 27 | TrxLineRefCustGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 28 | TrxLineRefCustGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 29 | TrxLineRefCustHistoricalFlag | HISTORICAL_FLAG | — | — |
| 30 | TrxLineRefCustInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 31 | TrxLineRefCustItemContext | ITEM_CONTEXT | — | — |
| 32 | TrxLineRefCustLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 33 | TrxLineRefCustLineIntendedUse | LINE_INTENDED_USE | — | — |
| 34 | TrxLineRefCustLineNumber | LINE_NUMBER | — | — |
| 35 | TrxLineRefCustLineRecoverable | LINE_RECOVERABLE | — | — |
| 36 | TrxLineRefCustLineType | LINE_TYPE | — | — |
| 37 | TrxLineRefCustMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 38 | TrxLineRefCustOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 39 | TrxLineRefCustProductCategory | PRODUCT_CATEGORY | — | — |
| 40 | TrxLineRefCustProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 41 | TrxLineRefCustProductType | PRODUCT_TYPE | — | — |
| 42 | TrxLineRefCustProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 43 | TrxLineRefCustQuantityCredited | QUANTITY_CREDITED | — | — |
| 44 | TrxLineRefCustQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 45 | TrxLineRefCustQuantityOrdered | QUANTITY_ORDERED | — | — |
| 46 | TrxLineRefCustReasonCode | REASON_CODE | — | — |
| 47 | TrxLineRefCustRevenueAmount | REVENUE_AMOUNT | — | — |
| 48 | TrxLineRefCustRuleEndDate | RULE_END_DATE | — | — |
| 49 | TrxLineRefCustRuleStartDate | RULE_START_DATE | — | — |
| 50 | TrxLineRefCustSalesOrder | SALES_ORDER | — | — |
| 51 | TrxLineRefCustSalesOrderDate | SALES_ORDER_DATE | — | — |
| 52 | TrxLineRefCustSalesOrderLine | SALES_ORDER_LINE | — | — |
| 53 | TrxLineRefCustSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 54 | TrxLineRefCustSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 55 | TrxLineRefCustSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 56 | TrxLineRefCustTaxAction | TAX_ACTION | — | — |
| 57 | TrxLineRefCustTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 58 | TrxLineRefCustTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 59 | TrxLineRefCustTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 60 | TrxLineRefCustTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 61 | TrxLineRefCustTaxPrecedence | TAX_PRECEDENCE | — | — |
| 62 | TrxLineRefCustTaxRate | TAX_RATE | — | — |
| 63 | TrxLineRefCustTaxRecoverable | TAX_RECOVERABLE | — | — |
| 64 | TrxLineRefCustTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 65 | TrxLineRefCustTaxableAmount | TAXABLE_AMOUNT | — | — |
| 66 | TrxLineRefCustTaxableFlag | TAXABLE_FLAG | — | — |
| 67 | TrxLineRefCustTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 68 | TrxLineRefCustTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 69 | TrxLineRefCustUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 70 | TrxLineRefCustUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 71 | TrxLineRefCustUomCode | UOM_CODE | — | — |
| 72 | TrxLineRefCustUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 73 | TrxLineRefCustWhUpdateDate | WH_UPDATE_DATE | — | — |
| 74 | TrxLineTaxlinkAccountingRuleDuration | ACCOUNTING_RULE_DURATION | — | — |
| 75 | TrxLineTaxlinkAcctdAmountDueOriginal | ACCTD_AMOUNT_DUE_ORIGINAL | — | — |
| 76 | TrxLineTaxlinkAcctdAmountDueRemaining | ACCTD_AMOUNT_DUE_REMAINING | — | — |
| 77 | TrxLineTaxlinkAmountDueOriginal | AMOUNT_DUE_ORIGINAL | — | — |
| 78 | TrxLineTaxlinkAmountDueRemaining | AMOUNT_DUE_REMAINING | — | — |
| 79 | TrxLineTaxlinkAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 80 | TrxLineTaxlinkAssessableValue | ASSESSABLE_VALUE | — | — |
| 81 | TrxLineTaxlinkAutoruleCompleteFlag | AUTORULE_COMPLETE_FLAG | — | — |
| 82 | TrxLineTaxlinkAutoruleDurationProcessed | AUTORULE_DURATION_PROCESSED | — | — |
| 83 | TrxLineTaxlinkAutotax | AUTOTAX | — | — |
| 84 | TrxLineTaxlinkChrgAcctdAmountRemaining | CHRG_ACCTD_AMOUNT_REMAINING | — | — |
| 85 | TrxLineTaxlinkChrgAmountRemaining | CHRG_AMOUNT_REMAINING | — | — |
| 86 | TrxLineTaxlinkCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 87 | TrxLineTaxlinkDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 88 | TrxLineTaxlinkDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 89 | TrxLineTaxlinkDeferralExclusionFlag | DEFERRAL_EXCLUSION_FLAG | — | — |
| 90 | TrxLineTaxlinkDescription | DESCRIPTION | — | — |
| 91 | TrxLineTaxlinkExtendedAcctdAmount | EXTENDED_ACCTD_AMOUNT | — | — |
| 92 | TrxLineTaxlinkExtendedAmount | EXTENDED_AMOUNT | — | — |
| 93 | TrxLineTaxlinkFairMarketValueAmount | FAIR_MARKET_VALUE_AMOUNT | — | — |
| 94 | TrxLineTaxlinkFrtAdjAcctdRemaining | FRT_ADJ_ACCTD_REMAINING | — | — |
| 95 | TrxLineTaxlinkFrtAdjRemaining | FRT_ADJ_REMAINING | — | — |
| 96 | TrxLineTaxlinkFrtEdAcctdAmount | FRT_ED_ACCTD_AMOUNT | — | — |
| 97 | TrxLineTaxlinkFrtEdAmount | FRT_ED_AMOUNT | — | — |
| 98 | TrxLineTaxlinkFrtUnedAcctdAmount | FRT_UNED_ACCTD_AMOUNT | — | — |
| 99 | TrxLineTaxlinkFrtUnedAmount | FRT_UNED_AMOUNT | — | — |
| 100 | TrxLineTaxlinkGrossExtendedAmount | GROSS_EXTENDED_AMOUNT | — | — |
| 101 | TrxLineTaxlinkGrossUnitSellingPrice | GROSS_UNIT_SELLING_PRICE | — | — |
| 102 | TrxLineTaxlinkHistoricalFlag | HISTORICAL_FLAG | — | — |
| 103 | TrxLineTaxlinkInvoicedLineAcctgLevel | INVOICED_LINE_ACCTG_LEVEL | — | — |
| 104 | TrxLineTaxlinkItemContext | ITEM_CONTEXT | — | — |
| 105 | TrxLineTaxlinkLastPeriodToCredit | LAST_PERIOD_TO_CREDIT | — | — |
| 106 | TrxLineTaxlinkLineIntendedUse | LINE_INTENDED_USE | — | — |
| 107 | TrxLineTaxlinkLineNumber | LINE_NUMBER | — | — |
| 108 | TrxLineTaxlinkLineRecoverable | LINE_RECOVERABLE | — | — |
| 109 | TrxLineTaxlinkLineType | LINE_TYPE | — | — |
| 110 | TrxLineTaxlinkMrcExtendedAcctdAmount | MRC_EXTENDED_ACCTD_AMOUNT | — | — |
| 111 | TrxLineTaxlinkOverrideAutoAccountingFlag | OVERRIDE_AUTO_ACCOUNTING_FLAG | — | — |
| 112 | TrxLineTaxlinkProductCategory | PRODUCT_CATEGORY | — | — |
| 113 | TrxLineTaxlinkProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 114 | TrxLineTaxlinkProductType | PRODUCT_TYPE | — | — |
| 115 | TrxLineTaxlinkProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 116 | TrxLineTaxlinkQuantityCredited | QUANTITY_CREDITED | — | — |
| 117 | TrxLineTaxlinkQuantityInvoiced | QUANTITY_INVOICED | — | — |
| 118 | TrxLineTaxlinkQuantityOrdered | QUANTITY_ORDERED | — | — |
| 119 | TrxLineTaxlinkReasonCode | REASON_CODE | — | — |
| 120 | TrxLineTaxlinkRevenueAmount | REVENUE_AMOUNT | — | — |
| 121 | TrxLineTaxlinkRuleEndDate | RULE_END_DATE | — | — |
| 122 | TrxLineTaxlinkRuleStartDate | RULE_START_DATE | — | — |
| 123 | TrxLineTaxlinkSalesOrder | SALES_ORDER | — | — |
| 124 | TrxLineTaxlinkSalesOrderDate | SALES_ORDER_DATE | — | — |
| 125 | TrxLineTaxlinkSalesOrderLine | SALES_ORDER_LINE | — | — |
| 126 | TrxLineTaxlinkSalesOrderRevision | SALES_ORDER_REVISION | — | — |
| 127 | TrxLineTaxlinkSalesOrderSource | SALES_ORDER_SOURCE | — | — |
| 128 | TrxLineTaxlinkSourceDocumentLineNumber | SOURCE_DOCUMENT_LINE_NUMBER | — | — |
| 129 | TrxLineTaxlinkTaxAction | TAX_ACTION | — | — |
| 130 | TrxLineTaxlinkTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 131 | TrxLineTaxlinkTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 132 | TrxLineTaxlinkTaxExemptNumber | TAX_EXEMPT_NUMBER | — | — |
| 133 | TrxLineTaxlinkTaxExemptReasonCode | TAX_EXEMPT_REASON_CODE | — | — |
| 134 | TrxLineTaxlinkTaxPrecedence | TAX_PRECEDENCE | — | — |
| 135 | TrxLineTaxlinkTaxRate | TAX_RATE | — | — |
| 136 | TrxLineTaxlinkTaxRecoverable | TAX_RECOVERABLE | — | — |
| 137 | TrxLineTaxlinkTaxVendorReturnCode | TAX_VENDOR_RETURN_CODE | — | — |
| 138 | TrxLineTaxlinkTaxableAmount | TAXABLE_AMOUNT | — | — |
| 139 | TrxLineTaxlinkTaxableFlag | TAXABLE_FLAG | — | — |
| 140 | TrxLineTaxlinkTranslatedDescription | TRANSLATED_DESCRIPTION | — | — |
| 141 | TrxLineTaxlinkTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 142 | TrxLineTaxlinkUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 143 | TrxLineTaxlinkUnitStandardPrice | UNIT_STANDARD_PRICE | — | — |
| 144 | TrxLineTaxlinkUomCode | UOM_CODE | — | — |
| 145 | TrxLineTaxlinkUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 146 | TrxLineTaxlinkWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[xla_events|XLA_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventApplicationId | APPLICATION_ID | — | — |
| 2 | EventBudgetaryControlFlag | BUDGETARY_CONTROL_FLAG | — | — |
| 3 | EventCreatedBy | CREATED_BY | — | — |
| 4 | EventCreationDate | CREATION_DATE | — | — |
| 5 | EventEntityId | ENTITY_ID | — | — |
| 6 | EventEventDate | EVENT_DATE | — | — |
| 7 | EventEventId | EVENT_ID | — | — |
| 8 | EventEventNumber | EVENT_NUMBER | — | — |
| 9 | EventEventStatusCode | EVENT_STATUS_CODE | — | — |
| 10 | EventEventTypeCode | EVENT_TYPE_CODE | — | — |
| 11 | EventHasWarningsFlag | HAS_WARNINGS_FLAG | — | — |
| 12 | EventLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | EventLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | EventLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | EventMergeEventSetId | MERGE_EVENT_SET_ID | — | — |
| 16 | EventObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | EventOnHoldFlag | ON_HOLD_FLAG | — | — |
| 18 | EventProcessStatusCode | PROCESS_STATUS_CODE | — | — |
| 19 | EventReferenceChar1 | REFERENCE_CHAR_1 | — | — |
| 20 | EventReferenceChar2 | REFERENCE_CHAR_2 | — | — |
| 21 | EventReferenceChar3 | REFERENCE_CHAR_3 | — | — |
| 22 | EventReferenceChar4 | REFERENCE_CHAR_4 | — | — |
| 23 | EventReferenceDate1 | REFERENCE_DATE_1 | — | — |
| 24 | EventReferenceDate2 | REFERENCE_DATE_2 | — | — |
| 25 | EventReferenceDate3 | REFERENCE_DATE_3 | — | — |
| 26 | EventReferenceDate4 | REFERENCE_DATE_4 | — | — |
| 27 | EventReferenceNum1 | REFERENCE_NUM_1 | — | — |
| 28 | EventReferenceNum2 | REFERENCE_NUM_2 | — | — |
| 29 | EventReferenceNum3 | REFERENCE_NUM_3 | — | — |
| 30 | EventReferenceNum4 | REFERENCE_NUM_4 | — | — |
| 31 | EventRequestId | REQUEST_ID | — | — |
| 32 | EventTransactionDate | TRANSACTION_DATE | — | — |
| 33 | EventUpgBatchId | UPG_BATCH_ID | — | — |
| 34 | EventUpgSourceApplicationId | UPG_SOURCE_APPLICATION_ID | — | — |
| 35 | EventUpgValidFlag | UPG_VALID_FLAG | — | — |

### [[zx_sco_rates|ZX_SCO_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRtScoActiveFlag | ACTIVE_FLAG | — | — |
| 2 | TaxRtScoAdjForAdhocAmtCode | ADJ_FOR_ADHOC_AMT_CODE | — | — |
| 3 | TaxRtScoAllowAdhocTaxRateFlag | ALLOW_ADHOC_TAX_RATE_FLAG | — | — |
| 4 | TaxRtScoAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | — |
| 5 | TaxRtScoAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | — |
| 6 | TaxRtScoDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | — |
| 7 | TaxRtScoDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | — |
| 8 | TaxRtScoDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | — |
| 9 | TaxRtScoDefaultRateFlag | DEFAULT_RATE_FLAG | — | — |
| 10 | TaxRtScoDefaultRecRateCode | DEFAULT_REC_RATE_CODE | — | — |
| 11 | TaxRtScoDefaultRecTypeCode | DEFAULT_REC_TYPE_CODE | — | — |
| 12 | TaxRtScoDescription | DESCRIPTION | — | — |
| 13 | TaxRtScoEffectiveFrom | EFFECTIVE_FROM | — | — |
| 14 | TaxRtScoEffectiveTo | EFFECTIVE_TO | — | — |
| 15 | TaxRtScoInclusiveTaxFlag | INCLUSIVE_TAX_FLAG | — | — |
| 16 | TaxRtScoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TaxRtScoOffsetStatusCode | OFFSET_STATUS_CODE | — | — |
| 18 | TaxRtScoOffsetTax | OFFSET_TAX | — | — |
| 19 | TaxRtScoOffsetTaxRateCode | OFFSET_TAX_RATE_CODE | — | — |
| 20 | TaxRtScoPercentageRate | PERCENTAGE_RATE | — | — |
| 21 | TaxRtScoProgramAppName | PROGRAM_APP_NAME | — | — |
| 22 | TaxRtScoProgramName | PROGRAM_NAME | — | — |
| 23 | TaxRtScoQuantityRate | QUANTITY_RATE | — | — |
| 24 | TaxRtScoRateTypeCode | RATE_TYPE_CODE | — | — |
| 25 | TaxRtScoRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 26 | TaxRtScoRecoveryRuleCode | RECOVERY_RULE_CODE | — | — |
| 27 | TaxRtScoRecoveryTypeCode | RECOVERY_TYPE_CODE | — | — |
| 28 | TaxRtScoScheduleBasedRateFlag | SCHEDULE_BASED_RATE_FLAG | — | — |
| 29 | TaxRtScoSdeffFrom | SDEFF_FROM | — | — |
| 30 | TaxRtScoSdeffTo | SDEFF_TO | — | — |
| 31 | TaxRtScoTax | TAX | — | — |
| 32 | TaxRtScoTaxClass | TAX_CLASS | — | — |
| 33 | TaxRtScoTaxInclusiveOverrideFlag | TAX_INCLUSIVE_OVERRIDE_FLAG | — | — |
| 34 | TaxRtScoTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 35 | TaxRtScoTaxRateCode | TAX_RATE_CODE | — | — |
| 36 | TaxRtScoTaxRateId | TAX_RATE_ID | — | — |
| 37 | TaxRtScoTaxRateName | TAX_RATE_NAME | — | ✅ |
| 38 | TaxRtScoTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 39 | TaxRtScoTaxStatusCode | TAX_STATUS_CODE | — | — |
| 40 | TaxRtScoTaxableBasisFormulaCode | TAXABLE_BASIS_FORMULA_CODE | — | — |
| 41 | TaxRtScoUomCode | UOM_CODE | — | — |
| 42 | TaxRtScoVatTransactionTypeCode | VAT_TRANSACTION_TYPE_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
