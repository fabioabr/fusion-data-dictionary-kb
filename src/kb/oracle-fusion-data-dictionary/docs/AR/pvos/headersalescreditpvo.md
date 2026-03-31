---
id: DOC-AR-PVO-HeaderSalesCreditPVO
doc_type: system-doc
title: "HeaderSalesCreditPVO — PVO Accounts Receivable"
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
  - HeaderSalesCreditPVO
  - headersalescreditpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HeaderSalesCreditPVO

## 📌 Visão Geral

Extrai os créditos de vendas no nível de cabeçalho da transação, vinculando vendedores e percentuais de comissão. Permite calcular comissões, medir performance de vendas e alocar receita por representante comercial.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.HeaderSalesCreditPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 888 | 29 | 1 | 131 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[ar_batches_all|AR_BATCHES_ALL]] — 46 atributos (1 BICC)
- [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]] — 5 atributos (1 BICC)
- [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]] — 35 atributos
- [[ar_lookups|AR_LOOKUPS]] — 4 atributos (1 BICC)
- [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]] — 28 atributos (1 BICC)
- [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]] — 5 atributos (1 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 9 atributos (1 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 12 atributos (2 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 40 atributos (4 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos
- [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]] — 12 atributos
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 6 atributos
- [[hz_locations|HZ_LOCATIONS]] — 26 atributos (20 BICC)
- [[hz_parties|HZ_PARTIES]] — 27 atributos (3 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 12 atributos (3 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 3 atributos (1 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 44 atributos (2 BICC)
- [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]] — 14 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 9 atributos
- [[ra_batches_all|RA_BATCHES_ALL]] — 33 atributos (1 BICC)
- [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]] — 124 atributos (3 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 301 atributos (70 BICC)
- [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]] — 49 atributos (1 PKs, 9 BICC)
- [[ra_rules|RA_RULES]] — 4 atributos (1 BICC)
- [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]] — 3 atributos (1 BICC)
- [[zx_registrations|ZX_REGISTRATIONS]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ar_batches_all|AR_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptBatchAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptBatchAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptBatchBankDepositNumber | BANK_DEPOSIT_NUMBER | — | — |
| 4 | ReceiptBatchBatchAppliedStatus | BATCH_APPLIED_STATUS | — | — |
| 5 | ReceiptBatchBatchDate | BATCH_DATE | — | — |
| 6 | ReceiptBatchBatchId | BATCH_ID | — | — |
| 7 | ReceiptBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 8 | ReceiptBatchClosedDate | CLOSED_DATE | — | — |
| 9 | ReceiptBatchControlAmount | CONTROL_AMOUNT | — | — |
| 10 | ReceiptBatchControlCount | CONTROL_COUNT | — | — |
| 11 | ReceiptBatchCreatedBy | CREATED_BY | — | — |
| 12 | ReceiptBatchCreationDate | CREATION_DATE | — | — |
| 13 | ReceiptBatchCurrencyCode | CURRENCY_CODE | — | — |
| 14 | ReceiptBatchDepositDate | DEPOSIT_DATE | — | — |
| 15 | ReceiptBatchExchangeDate | EXCHANGE_DATE | — | — |
| 16 | ReceiptBatchExchangeRate | EXCHANGE_RATE | — | — |
| 17 | ReceiptBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 18 | ReceiptBatchGlDate | GL_DATE | — | — |
| 19 | ReceiptBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ReceiptBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ReceiptBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ReceiptBatchLockboxBatchName | LOCKBOX_BATCH_NAME | — | — |
| 23 | ReceiptBatchLockboxId | LOCKBOX_ID | — | — |
| 24 | ReceiptBatchMediaReference | MEDIA_REFERENCE | — | — |
| 25 | ReceiptBatchName | NAME | — | — |
| 26 | ReceiptBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | ReceiptBatchOldRemittanceBankBranchId | OLD_REMITTANCE_BANK_BRANCH_ID | — | — |
| 28 | ReceiptBatchOperationRequestId | OPERATION_REQUEST_ID | — | — |
| 29 | ReceiptBatchOrgId | ORG_ID | — | — |
| 30 | ReceiptBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | ReceiptBatchProgramId | PROGRAM_ID | — | — |
| 32 | ReceiptBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | ReceiptBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 34 | ReceiptBatchReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 35 | ReceiptBatchReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 36 | ReceiptBatchRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 37 | ReceiptBatchRemitMethodCode | REMIT_METHOD_CODE | — | — |
| 38 | ReceiptBatchRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 39 | ReceiptBatchRemittanceBankBranchId | REMITTANCE_BANK_BRANCH_ID | — | — |
| 40 | ReceiptBatchRequestId | REQUEST_ID | — | — |
| 41 | ReceiptBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 42 | ReceiptBatchStatus | STATUS | — | — |
| 43 | ReceiptBatchTransmissionId | TRANSMISSION_ID | — | — |
| 44 | ReceiptBatchTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | — |
| 45 | ReceiptBatchType | TYPE | — | — |
| 46 | ReceiptBatchWithRecourseFlag | WITH_RECOURSE_FLAG | — | — |

### [[ar_cash_receipts_all|AR_CASH_RECEIPTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevCashRcptCashReceiptId | CASH_RECEIPT_ID | — | — |
| 2 | RevCashRcptComments | COMMENTS | — | — |
| 3 | RevCashRcptIssuerName | ISSUER_NAME | — | — |
| 4 | RevCashRcptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RevCashRcptReceiptNumber | RECEIPT_NUMBER | — | ✅ |

### [[ar_interest_headers_all|AR_INTEREST_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntrstHdrTrxHdrChargeBeginDate | CHARGE_BEGIN_DATE | — | — |
| 2 | IntrstHdrTrxHdrChargeOnFinanceChargeFlag | CHARGE_ON_FINANCE_CHARGE_FLAG | — | — |
| 3 | IntrstHdrTrxHdrCreditItemsFlag | CREDIT_ITEMS_FLAG | — | — |
| 4 | IntrstHdrTrxHdrCurrencyCode | CURRENCY_CODE | — | — |
| 5 | IntrstHdrTrxHdrDisplayFlag | DISPLAY_FLAG | — | — |
| 6 | IntrstHdrTrxHdrDisputedTransactionsFlag | DISPUTED_TRANSACTIONS_FLAG | — | — |
| 7 | IntrstHdrTrxHdrExchangeRate | EXCHANGE_RATE | — | — |
| 8 | IntrstHdrTrxHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 9 | IntrstHdrTrxHdrFinanceChargeDate | FINANCE_CHARGE_DATE | — | — |
| 10 | IntrstHdrTrxHdrHeaderType | HEADER_TYPE | — | — |
| 11 | IntrstHdrTrxHdrHoldChargedInvoicesFlag | HOLD_CHARGED_INVOICES_FLAG | — | — |
| 12 | IntrstHdrTrxHdrInterestCalculationPeriod | INTEREST_CALCULATION_PERIOD | — | — |
| 13 | IntrstHdrTrxHdrInterestFixedAmount | INTEREST_FIXED_AMOUNT | — | — |
| 14 | IntrstHdrTrxHdrInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 15 | IntrstHdrTrxHdrInterestPeriodDays | INTEREST_PERIOD_DAYS | — | — |
| 16 | IntrstHdrTrxHdrInterestRate | INTEREST_RATE | — | — |
| 17 | IntrstHdrTrxHdrInterestType | INTEREST_TYPE | — | — |
| 18 | IntrstHdrTrxHdrLastAccrueChargeDate | LAST_ACCRUE_CHARGE_DATE | — | — |
| 19 | IntrstHdrTrxHdrLateChargeCalculationTrx | LATE_CHARGE_CALCULATION_TRX | — | — |
| 20 | IntrstHdrTrxHdrMaxInterestCharge | MAX_INTEREST_CHARGE | — | — |
| 21 | IntrstHdrTrxHdrMinFcBalanceAmount | MIN_FC_BALANCE_AMOUNT | — | — |
| 22 | IntrstHdrTrxHdrMinFcBalanceOverdueType | MIN_FC_BALANCE_OVERDUE_TYPE | — | — |
| 23 | IntrstHdrTrxHdrMinFcBalancePercent | MIN_FC_BALANCE_PERCENT | — | — |
| 24 | IntrstHdrTrxHdrMinFcInvoiceAmount | MIN_FC_INVOICE_AMOUNT | — | — |
| 25 | IntrstHdrTrxHdrMinFcInvoiceOverdueType | MIN_FC_INVOICE_OVERDUE_TYPE | — | — |
| 26 | IntrstHdrTrxHdrMinFcInvoicePercent | MIN_FC_INVOICE_PERCENT | — | — |
| 27 | IntrstHdrTrxHdrMinInterestCharge | MIN_INTEREST_CHARGE | — | — |
| 28 | IntrstHdrTrxHdrMultipleInterestRatesFlag | MULTIPLE_INTEREST_RATES_FLAG | — | — |
| 29 | IntrstHdrTrxHdrPaymentGraceDays | PAYMENT_GRACE_DAYS | — | — |
| 30 | IntrstHdrTrxHdrPenaltyFixedAmount | PENALTY_FIXED_AMOUNT | — | — |
| 31 | IntrstHdrTrxHdrPenaltyRate | PENALTY_RATE | — | — |
| 32 | IntrstHdrTrxHdrPenaltyType | PENALTY_TYPE | — | — |
| 33 | IntrstHdrTrxHdrProcessMessage | PROCESS_MESSAGE | — | — |
| 34 | IntrstHdrTrxHdrProcessStatus | PROCESS_STATUS | — | — |
| 35 | IntrstHdrTrxHdrWorkerNum | WORKER_NUM | — | — |

### [[ar_lookups|AR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxClassDescription | DESCRIPTION | — | — |
| 2 | TrxClassLookupCode | LOOKUP_CODE | — | — |
| 3 | TrxClassLookupType | LOOKUP_TYPE | — | — |
| 4 | TrxClassMeaning | MEANING | — | ✅ |

### [[ar_revenue_adjustments_all|AR_REVENUE_ADJUSTMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevAdjAmount | AMOUNT | — | — |
| 2 | RevAdjAmountMode | AMOUNT_MODE | — | — |
| 3 | RevAdjApplicationDate | APPLICATION_DATE | — | — |
| 4 | RevAdjCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 5 | RevAdjFromCategoryId | FROM_CATEGORY_ID | — | — |
| 6 | RevAdjFromCustTrxLineId | FROM_CUST_TRX_LINE_ID | — | — |
| 7 | RevAdjFromInventoryItemId | FROM_INVENTORY_ITEM_ID | — | — |
| 8 | RevAdjFromResourceSalesrepId | FROM_RESOURCE_SALESREP_ID | — | — |
| 9 | RevAdjFromSalesgroupId | FROM_SALESGROUP_ID | — | — |
| 10 | RevAdjGlDate | GL_DATE | — | — |
| 11 | RevAdjLineSelectionMode | LINE_SELECTION_MODE | — | — |
| 12 | RevAdjOrgId | ORG_ID | — | — |
| 13 | RevAdjPercent | PERCENT | — | — |
| 14 | RevAdjProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 15 | RevAdjProgramId | PROGRAM_ID | — | — |
| 16 | RevAdjProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 17 | RevAdjReasonCode | REASON_CODE | — | — |
| 18 | RevAdjRequestId | REQUEST_ID | — | — |
| 19 | RevAdjRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 20 | RevAdjRevenueAdjustmentNumber | REVENUE_ADJUSTMENT_NUMBER | — | ✅ |
| 21 | RevAdjSalesCreditType | SALES_CREDIT_TYPE | — | — |
| 22 | RevAdjStatus | STATUS | — | — |
| 23 | RevAdjToCategoryId | TO_CATEGORY_ID | — | — |
| 24 | RevAdjToCustTrxLineId | TO_CUST_TRX_LINE_ID | — | — |
| 25 | RevAdjToInventoryItemId | TO_INVENTORY_ITEM_ID | — | — |
| 26 | RevAdjToResourceSalesrepId | TO_RESOURCE_SALESREP_ID | — | — |
| 27 | RevAdjToSalesgroupId | TO_SALESGROUP_ID | — | — |
| 28 | RevAdjType | TYPE | — | — |

### [[fnd_document_sequences|FND_DOCUMENT_SEQUENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocSeqHdrAuditTableName | AUDIT_TABLE_NAME | — | — |
| 2 | DocSeqHdrDbSequenceName | DB_SEQUENCE_NAME | — | — |
| 3 | DocSeqHdrDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 4 | DocSeqHdrName | NAME | — | ✅ |
| 5 | DocSeqHdrTableName | TABLE_NAME | — | — |

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryAlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | — |
| 2 | TerritoryCurrencyCode | CURRENCY_CODE | — | — |
| 3 | TerritoryDescription | DESCRIPTION | — | — |
| 4 | TerritoryEuCode | EU_CODE | — | — |
| 5 | TerritoryIsoNumericCode | ISO_NUMERIC_CODE | — | — |
| 6 | TerritoryIsoTerritoryCode | ISO_TERRITORY_CODE | — | — |
| 7 | TerritoryNlsTerritory | NLS_TERRITORY | — | — |
| 8 | TerritoryTerritoryCode | TERRITORY_CODE | — | — |
| 9 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

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

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonRevSalesOrgEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | NonRevSalesOrgEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | NonRevSalesOrgLanguage | LANGUAGE | — | — |
| 4 | NonRevSalesOrgName | NAME | — | ✅ |
| 5 | NonRevSalesOrgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | NonRevSalesOrgOrganizationId | ORGANIZATION_ID | — | — |
| 7 | RevSalesOrgEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RevSalesOrgEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RevSalesOrgLanguage | LANGUAGE | — | — |
| 10 | RevSalesOrgName | NAME | — | ✅ |
| 11 | RevSalesOrgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RevSalesOrgOrganizationId | ORGANIZATION_ID | — | — |

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
| 32 | PayingCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 33 | PayingCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 34 | PayingCustAcctPartyId | PARTY_ID | — | — |
| 35 | ShipToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 36 | ShipToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 37 | ShipToCustAcctPartyId | PARTY_ID | — | — |
| 38 | SoldToCustAcctAccountName | ACCOUNT_NAME | — | ✅ |
| 39 | SoldToCustAcctCustAccountId | CUST_ACCOUNT_ID | — | — |
| 40 | SoldToCustAcctPartyId | PARTY_ID | — | — |

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 2 | BillToContactCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |

### [[hz_cust_acct_sites_all|HZ_CUST_ACCT_SITES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | PayingSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 3 | PayingSitePartySiteId | PARTY_SITE_ID | — | — |
| 4 | RmtToAddrSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 5 | RmtToAddrSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 6 | RmtToAddrSitePartySiteId | PARTY_SITE_ID | — | — |
| 7 | ShipToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 8 | ShipToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 9 | ShipToSitePartySiteId | PARTY_SITE_ID | — | — |
| 10 | SoldToSiteCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 11 | SoldToSiteLanguage | ACCT_SITE_LANGUAGE | — | — |
| 12 | SoldToSitePartySiteId | PARTY_SITE_ID | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 2 | PayingSiteUseSiteUseId | SITE_USE_ID | — | — |
| 3 | ShipToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 4 | ShipToSiteUseSiteUseId | SITE_USE_ID | — | — |
| 5 | SoldToSiteUseCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 6 | SoldToSiteUseSiteUseId | SITE_USE_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RmtLocationAddress1 | ADDRESS1 | — | ✅ |
| 2 | RmtLocationAddress2 | ADDRESS2 | — | ✅ |
| 3 | RmtLocationAddress3 | ADDRESS3 | — | ✅ |
| 4 | RmtLocationAddress4 | ADDRESS4 | — | ✅ |
| 5 | RmtLocationCity | CITY | — | ✅ |
| 6 | RmtLocationCountry | COUNTRY | — | ✅ |
| 7 | RmtLocationCounty | COUNTY | — | ✅ |
| 8 | RmtLocationDescription | DESCRIPTION | — | — |
| 9 | RmtLocationLocationId | LOCATION_ID | — | — |
| 10 | RmtLocationPosition | POSITION | — | — |
| 11 | RmtLocationPostalCode | POSTAL_CODE | — | ✅ |
| 12 | RmtLocationProvince | PROVINCE | — | ✅ |
| 13 | RmtLocationState | STATE | — | ✅ |
| 14 | ShipToAddrLocationAddress1 | ADDRESS1 | — | ✅ |
| 15 | ShipToAddrLocationAddress2 | ADDRESS2 | — | ✅ |
| 16 | ShipToAddrLocationAddress3 | ADDRESS3 | — | ✅ |
| 17 | ShipToAddrLocationAddress4 | ADDRESS4 | — | ✅ |
| 18 | ShipToAddrLocationCity | CITY | — | ✅ |
| 19 | ShipToAddrLocationCountry | COUNTRY | — | ✅ |
| 20 | ShipToAddrLocationCounty | COUNTY | — | ✅ |
| 21 | ShipToAddrLocationDescription | DESCRIPTION | — | — |
| 22 | ShipToAddrLocationLocationId | LOCATION_ID | — | — |
| 23 | ShipToAddrLocationPosition | POSITION | — | — |
| 24 | ShipToAddrLocationPostalCode | POSTAL_CODE | — | ✅ |
| 25 | ShipToAddrLocationProvince | PROVINCE | — | ✅ |
| 26 | ShipToAddrLocationState | STATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactPartyPartyId | PARTY_ID | — | — |
| 2 | BillToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 3 | BillToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 4 | BillToContactPartyPartyType | PARTY_TYPE | — | — |
| 5 | BillToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 6 | BillToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 7 | BillToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 8 | BillToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 9 | BillToContactPartyPersonTitle | PERSON_TITLE | — | — |
| 10 | ShipToContactPartyPartyId | PARTY_ID | — | — |
| 11 | ShipToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 12 | ShipToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 13 | ShipToContactPartyPartyType | PARTY_TYPE | — | — |
| 14 | ShipToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 15 | ShipToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 16 | ShipToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 17 | ShipToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 18 | ShipToContactPartyPersonTitle | PERSON_TITLE | — | — |
| 19 | SoldToContactPartyPartyId | PARTY_ID | — | — |
| 20 | SoldToContactPartyPartyName | PARTY_NAME | — | ✅ |
| 21 | SoldToContactPartyPartyNumber | PARTY_NUMBER | — | — |
| 22 | SoldToContactPartyPartyType | PARTY_TYPE | — | — |
| 23 | SoldToContactPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 24 | SoldToContactPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 25 | SoldToContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 26 | SoldToContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 27 | SoldToContactPartyPersonTitle | PERSON_TITLE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayingPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 2 | PayingPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 3 | RmtPartySiteLocationId | LOCATION_ID | — | — |
| 4 | RmtPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 5 | RmtPartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 6 | ShipToAddrPartySiteLocationId | LOCATION_ID | — | — |
| 7 | ShipToAddrPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 8 | ShipToAddrPartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 9 | ShipToPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 10 | ShipToPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 11 | SoldToPartySitePartySiteId | PARTY_SITE_ID | — | — |
| 12 | SoldToPartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[hz_party_site_uses|HZ_PARTY_SITE_USES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShipToPartySiteUseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | ShipToPartySiteUseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 3 | ShipToPartySiteUsePartySiteUseId | PARTY_SITE_USE_ID | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IbyExtBankAccountsAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | IbyExtBankAccountsAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | IbyExtBankAccountsAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | IbyExtBankAccountsBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | IbyExtBankAccountsBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | IbyExtBankAccountsBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | IbyExtBankAccountsBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | IbyExtBankAccountsBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | IbyExtBankAccountsBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | IbyExtBankAccountsBankAccountNum | BANK_ACCOUNT_NUM | — | ✅ |
| 11 | IbyExtBankAccountsBankAccountNumElectronic | BANK_ACCOUNT_NUM_ELECTRONIC | — | — |
| 12 | IbyExtBankAccountsBankAccountNumHash1 | BANK_ACCOUNT_NUM_HASH1 | — | — |
| 13 | IbyExtBankAccountsBankAccountNumHash2 | BANK_ACCOUNT_NUM_HASH2 | — | — |
| 14 | IbyExtBankAccountsBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 15 | IbyExtBankAccountsBankId | BANK_ID | — | — |
| 16 | IbyExtBankAccountsBranchId | BRANCH_ID | — | — |
| 17 | IbyExtBankAccountsCheckDigits | CHECK_DIGITS | — | — |
| 18 | IbyExtBankAccountsCountryCode | COUNTRY_CODE | — | — |
| 19 | IbyExtBankAccountsCurrencyCode | CURRENCY_CODE | — | — |
| 20 | IbyExtBankAccountsDescription | DESCRIPTION | — | — |
| 21 | IbyExtBankAccountsEncrypted | ENCRYPTED | — | — |
| 22 | IbyExtBankAccountsEndDate | END_DATE | — | — |
| 23 | IbyExtBankAccountsExchangeRate | EXCHANGE_RATE | — | — |
| 24 | IbyExtBankAccountsExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 25 | IbyExtBankAccountsExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 26 | IbyExtBankAccountsExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 27 | IbyExtBankAccountsForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 28 | IbyExtBankAccountsHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 29 | IbyExtBankAccountsIban | IBAN | — | — |
| 30 | IbyExtBankAccountsIbanHash1 | IBAN_HASH1 | — | — |
| 31 | IbyExtBankAccountsIbanHash2 | IBAN_HASH2 | — | — |
| 32 | IbyExtBankAccountsIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 33 | IbyExtBankAccountsMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | — |
| 34 | IbyExtBankAccountsMaskedIban | MASKED_IBAN | — | — |
| 35 | IbyExtBankAccountsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | IbyExtBankAccountsPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 37 | IbyExtBankAccountsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 38 | IbyExtBankAccountsProgramId | PROGRAM_ID | — | — |
| 39 | IbyExtBankAccountsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 40 | IbyExtBankAccountsRequestId | REQUEST_ID | — | — |
| 41 | IbyExtBankAccountsSaltVersion | SALT_VERSION | — | — |
| 42 | IbyExtBankAccountsSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 43 | IbyExtBankAccountsShortAcctName | SHORT_ACCT_NAME | — | — |
| 44 | IbyExtBankAccountsStartDate | START_DATE | — | — |

### [[iby_fndcpt_tx_extensions|IBY_FNDCPT_TX_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxExtnHdrAdditionalInfo | ADDITIONAL_INFO | — | — |
| 2 | TrxExtnHdrEncrypted | ENCRYPTED | — | — |
| 3 | TrxExtnHdrInstrSecCodeLength | INSTR_SEC_CODE_LENGTH | — | — |
| 4 | TrxExtnHdrInstrumentSecurityCode | INSTRUMENT_SECURITY_CODE | — | — |
| 5 | TrxExtnHdrPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 6 | TrxExtnHdrPaymentSystemOrderNumber | PAYMENT_SYSTEM_ORDER_NUMBER | — | ✅ |
| 7 | TrxExtnHdrPoLineNumber | PO_LINE_NUMBER | — | — |
| 8 | TrxExtnHdrPoNumber | PO_NUMBER | — | — |
| 9 | TrxExtnHdrTrxnExtensionId | TRXN_EXTENSION_ID | — | — |
| 10 | TrxExtnHdrTrxnRefNumber1 | TRXN_REF_NUMBER1 | — | — |
| 11 | TrxExtnHdrTrxnRefNumber2 | TRXN_REF_NUMBER2 | — | — |
| 12 | TrxExtnHdrVoiceAuthorizationCode | VOICE_AUTHORIZATION_CODE | — | — |
| 13 | TrxExtnHdrVoiceAuthorizationDate | VOICE_AUTHORIZATION_DATE | — | — |
| 14 | TrxExtnHdrVoiceAuthorizationFlag | VOICE_AUTHORIZATION_FLAG | — | — |

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
| 2 | UserCreatedByUserGuid | USER_GUID | — | — |
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 8 | UserUpdatedByUserId | USER_ID | — | — |
| 9 | UserUpdatedByUsername | USERNAME | — | — |

### [[ra_batches_all|RA_BATCHES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchBatchDate | BATCH_DATE | — | — |
| 2 | TransactionBatchBatchId | BATCH_ID | — | — |
| 3 | TransactionBatchBatchProcessStatus | BATCH_PROCESS_STATUS | — | — |
| 4 | TransactionBatchBatchSourceId | BATCH_SOURCE_ID | — | — |
| 5 | TransactionBatchBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 6 | TransactionBatchComments | COMMENTS | — | — |
| 7 | TransactionBatchControlAmount | CONTROL_AMOUNT | — | — |
| 8 | TransactionBatchControlCount | CONTROL_COUNT | — | — |
| 9 | TransactionBatchCreatedBy | CREATED_BY | — | — |
| 10 | TransactionBatchCreationDate | CREATION_DATE | — | — |
| 11 | TransactionBatchCurrencyCode | CURRENCY_CODE | — | — |
| 12 | TransactionBatchExchangeDate | EXCHANGE_DATE | — | — |
| 13 | TransactionBatchExchangeRate | EXCHANGE_RATE | — | — |
| 14 | TransactionBatchExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 15 | TransactionBatchGlDate | GL_DATE | — | — |
| 16 | TransactionBatchIssueDate | ISSUE_DATE | — | — |
| 17 | TransactionBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | TransactionBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | TransactionBatchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | TransactionBatchMaturityDate | MATURITY_DATE | — | — |
| 21 | TransactionBatchName | NAME | — | — |
| 22 | TransactionBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | TransactionBatchOrgId | ORG_ID | — | — |
| 24 | TransactionBatchProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 25 | TransactionBatchProgramId | PROGRAM_ID | — | — |
| 26 | TransactionBatchProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 27 | TransactionBatchPurgedChildrenFlag | PURGED_CHILDREN_FLAG | — | — |
| 28 | TransactionBatchRequestId | REQUEST_ID | — | — |
| 29 | TransactionBatchSelectionCriteriaId | SELECTION_CRITERIA_ID | — | — |
| 30 | TransactionBatchSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 31 | TransactionBatchSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 32 | TransactionBatchStatus | STATUS | — | — |
| 33 | TransactionBatchType | TYPE | — | — |

### [[ra_batch_sources_all|RA_BATCH_SOURCES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionBatchSourceAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 2 | TransactionBatchSourceAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 3 | TransactionBatchSourceAgreementRule | AGREEMENT_RULE | — | — |
| 4 | TransactionBatchSourceAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 5 | TransactionBatchSourceAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 6 | TransactionBatchSourceAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 7 | TransactionBatchSourceAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 8 | TransactionBatchSourceBatchSourceId | BATCH_SOURCE_ID | — | — |
| 9 | TransactionBatchSourceBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 10 | TransactionBatchSourceBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 11 | TransactionBatchSourceBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 12 | TransactionBatchSourceBillContactRule | BILL_CONTACT_RULE | — | — |
| 13 | TransactionBatchSourceBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 14 | TransactionBatchSourceCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 15 | TransactionBatchSourceCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 16 | TransactionBatchSourceCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 17 | TransactionBatchSourceCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 18 | TransactionBatchSourceCreatedBy | CREATED_BY | — | — |
| 19 | TransactionBatchSourceCreationDate | CREATION_DATE | — | — |
| 20 | TransactionBatchSourceCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 21 | TransactionBatchSourceCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 22 | TransactionBatchSourceCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 23 | TransactionBatchSourceDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 24 | TransactionBatchSourceDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 25 | TransactionBatchSourceDefaultReference | DEFAULT_REFERENCE | — | — |
| 26 | TransactionBatchSourceDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 27 | TransactionBatchSourceDescription | DESCRIPTION | — | — |
| 28 | TransactionBatchSourceEndDate | END_DATE | — | — |
| 29 | TransactionBatchSourceFobPointRule | FOB_POINT_RULE | — | — |
| 30 | TransactionBatchSourceGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 31 | TransactionBatchSourceGroupingRuleId | GROUPING_RULE_ID | — | — |
| 32 | TransactionBatchSourceInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 33 | TransactionBatchSourceInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 34 | TransactionBatchSourceInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 35 | TransactionBatchSourceInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 36 | TransactionBatchSourceLastBatchNum | LAST_BATCH_NUM | — | — |
| 37 | TransactionBatchSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | TransactionBatchSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | TransactionBatchSourceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | TransactionBatchSourceLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 41 | TransactionBatchSourceMemoLineRule | MEMO_LINE_RULE | — | — |
| 42 | TransactionBatchSourceMemoReasonRule | MEMO_REASON_RULE | — | — |
| 43 | TransactionBatchSourceName | NAME | — | ✅ |
| 44 | TransactionBatchSourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | TransactionBatchSourceParentAccountingFlexfieldRule | ACCOUNTING_FLEXFIELD_RULE | — | — |
| 46 | TransactionBatchSourceParentAccountingRuleRule | ACCOUNTING_RULE_RULE | — | — |
| 47 | TransactionBatchSourceParentAgreementRule | AGREEMENT_RULE | — | — |
| 48 | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | ALLOW_DUPLICATE_TRX_NUM_FLAG | — | — |
| 49 | TransactionBatchSourceParentAllowSalesCreditFlag | ALLOW_SALES_CREDIT_FLAG | — | — |
| 50 | TransactionBatchSourceParentAutoBatchNumberingFlag | AUTO_BATCH_NUMBERING_FLAG | — | — |
| 51 | TransactionBatchSourceParentAutoTrxNumberingFlag | AUTO_TRX_NUMBERING_FLAG | — | — |
| 52 | TransactionBatchSourceParentBatchSourceId | BATCH_SOURCE_ID | — | — |
| 53 | TransactionBatchSourceParentBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 54 | TransactionBatchSourceParentBatchSourceType | BATCH_SOURCE_TYPE | — | — |
| 55 | TransactionBatchSourceParentBillAddressRule | BILL_ADDRESS_RULE | — | — |
| 56 | TransactionBatchSourceParentBillContactRule | BILL_CONTACT_RULE | — | — |
| 57 | TransactionBatchSourceParentBillCustomerRule | BILL_CUSTOMER_RULE | — | — |
| 58 | TransactionBatchSourceParentCmBatchSourceSeqId | CM_BATCH_SOURCE_SEQ_ID | — | — |
| 59 | TransactionBatchSourceParentCopyDocNumberFlag | COPY_DOC_NUMBER_FLAG | — | — |
| 60 | TransactionBatchSourceParentCopyInvTidffToCmFlag | COPY_INV_TIDFF_TO_CM_FLAG | — | — |
| 61 | TransactionBatchSourceParentCreateClearingFlag | CREATE_CLEARING_FLAG | — | — |
| 62 | TransactionBatchSourceParentCreatedBy | CREATED_BY | — | — |
| 63 | TransactionBatchSourceParentCreationDate | CREATION_DATE | — | — |
| 64 | TransactionBatchSourceParentCreditMemoBatchSourceId | CREDIT_MEMO_BATCH_SOURCE_ID | — | — |
| 65 | TransactionBatchSourceParentCustTrxTypeRule | CUST_TRX_TYPE_RULE | — | — |
| 66 | TransactionBatchSourceParentCustomerBankAccountRule | CUSTOMER_BANK_ACCOUNT_RULE | — | — |
| 67 | TransactionBatchSourceParentDefaultInvTrxType | DEFAULT_INV_TRX_TYPE | — | — |
| 68 | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | DEFAULT_INV_TRX_TYPE_SEQ_ID | — | — |
| 69 | TransactionBatchSourceParentDefaultReference | DEFAULT_REFERENCE | — | — |
| 70 | TransactionBatchSourceParentDeriveDateFlag | DERIVE_DATE_FLAG | — | — |
| 71 | TransactionBatchSourceParentDescription | DESCRIPTION | — | — |
| 72 | TransactionBatchSourceParentEndDate | END_DATE | — | — |
| 73 | TransactionBatchSourceParentFobPointRule | FOB_POINT_RULE | — | — |
| 74 | TransactionBatchSourceParentGlDatePeriodRule | GL_DATE_PERIOD_RULE | — | — |
| 75 | TransactionBatchSourceParentGroupingRuleId | GROUPING_RULE_ID | — | — |
| 76 | TransactionBatchSourceParentInvalidLinesRule | INVALID_LINES_RULE | — | — |
| 77 | TransactionBatchSourceParentInvalidTaxRateRule | INVALID_TAX_RATE_RULE | — | — |
| 78 | TransactionBatchSourceParentInventoryItemRule | INVENTORY_ITEM_RULE | — | — |
| 79 | TransactionBatchSourceParentInvoicingRuleRule | INVOICING_RULE_RULE | — | — |
| 80 | TransactionBatchSourceParentLastBatchNum | LAST_BATCH_NUM | — | — |
| 81 | TransactionBatchSourceParentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | TransactionBatchSourceParentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | TransactionBatchSourceParentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 84 | TransactionBatchSourceParentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 85 | TransactionBatchSourceParentMemoLineRule | MEMO_LINE_RULE | — | — |
| 86 | TransactionBatchSourceParentMemoReasonRule | MEMO_REASON_RULE | — | — |
| 87 | TransactionBatchSourceParentName | NAME | — | — |
| 88 | TransactionBatchSourceParentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | TransactionBatchSourceParentReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 90 | TransactionBatchSourceParentReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 91 | TransactionBatchSourceParentRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 92 | TransactionBatchSourceParentRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 93 | TransactionBatchSourceParentSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 94 | TransactionBatchSourceParentSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 95 | TransactionBatchSourceParentSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 96 | TransactionBatchSourceParentSalespersonRule | SALESPERSON_RULE | — | — |
| 97 | TransactionBatchSourceParentSetId | SET_ID | — | — |
| 98 | TransactionBatchSourceParentShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 99 | TransactionBatchSourceParentShipContactRule | SHIP_CONTACT_RULE | — | — |
| 100 | TransactionBatchSourceParentShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 101 | TransactionBatchSourceParentShipViaRule | SHIP_VIA_RULE | — | — |
| 102 | TransactionBatchSourceParentSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 103 | TransactionBatchSourceParentStartDate | START_DATE | — | — |
| 104 | TransactionBatchSourceParentStatus | STATUS | — | — |
| 105 | TransactionBatchSourceParentTermRule | TERM_RULE | — | — |
| 106 | TransactionBatchSourceParentUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |
| 107 | TransactionBatchSourceReceiptHandlingOption | RECEIPT_HANDLING_OPTION | — | — |
| 108 | TransactionBatchSourceReceiptMethodRule | RECEIPT_METHOD_RULE | — | — |
| 109 | TransactionBatchSourceRelatedDocumentRule | RELATED_DOCUMENT_RULE | — | — |
| 110 | TransactionBatchSourceRevAccAllocationRule | REV_ACC_ALLOCATION_RULE | — | — |
| 111 | TransactionBatchSourceSalesCreditRule | SALES_CREDIT_RULE | — | — |
| 112 | TransactionBatchSourceSalesCreditTypeRule | SALES_CREDIT_TYPE_RULE | — | — |
| 113 | TransactionBatchSourceSalesTerritoryRule | SALES_TERRITORY_RULE | — | — |
| 114 | TransactionBatchSourceSalespersonRule | SALESPERSON_RULE | — | — |
| 115 | TransactionBatchSourceSetId | SET_ID | — | — |
| 116 | TransactionBatchSourceShipAddressRule | SHIP_ADDRESS_RULE | — | — |
| 117 | TransactionBatchSourceShipContactRule | SHIP_CONTACT_RULE | — | — |
| 118 | TransactionBatchSourceShipCustomerRule | SHIP_CUSTOMER_RULE | — | — |
| 119 | TransactionBatchSourceShipViaRule | SHIP_VIA_RULE | — | — |
| 120 | TransactionBatchSourceSoldCustomerRule | SOLD_CUSTOMER_RULE | — | — |
| 121 | TransactionBatchSourceStartDate | START_DATE | — | — |
| 122 | TransactionBatchSourceStatus | STATUS | — | — |
| 123 | TransactionBatchSourceTermRule | TERM_RULE | — | — |
| 124 | TransactionBatchSourceUnitOfMeasureRule | UNIT_OF_MEASURE_RULE | — | — |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 2 | RelCustTrxHdrCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 3 | RelCustTrxHdrTrxNumber | TRX_NUMBER | — | ✅ |
| 4 | TransactionHeaderAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 5 | TransactionHeaderAgreementId | AGREEMENT_ID | — | — |
| 6 | TransactionHeaderApplicationId | APPLICATION_ID | — | — |
| 7 | TransactionHeaderApprovalCode | APPROVAL_CODE | — | — |
| 8 | TransactionHeaderAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 9 | TransactionHeaderBatchId | BATCH_ID | — | — |
| 10 | TransactionHeaderBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 11 | TransactionHeaderBillTemplateId | BILL_TEMPLATE_ID | — | ✅ |
| 12 | TransactionHeaderBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 13 | TransactionHeaderBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 14 | TransactionHeaderBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 15 | TransactionHeaderBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 16 | TransactionHeaderBillingDate | BILLING_DATE | — | ✅ |
| 17 | TransactionHeaderBrAmount | BR_AMOUNT | — | — |
| 18 | TransactionHeaderBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 19 | TransactionHeaderBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 20 | TransactionHeaderCcErrorCode | CC_ERROR_CODE | — | — |
| 21 | TransactionHeaderCcErrorFlag | CC_ERROR_FLAG | — | — |
| 22 | TransactionHeaderCcErrorText | CC_ERROR_TEXT | — | — |
| 23 | TransactionHeaderComments | COMMENTS | — | ✅ |
| 24 | TransactionHeaderCompleteFlag | COMPLETE_FLAG | — | ✅ |
| 25 | TransactionHeaderContractId | CONTRACT_ID | — | — |
| 26 | TransactionHeaderCreatedBy | CREATED_BY | — | ✅ |
| 27 | TransactionHeaderCreatedFrom | CREATED_FROM | — | ✅ |
| 28 | TransactionHeaderCreationDate | CREATION_DATE | — | ✅ |
| 29 | TransactionHeaderCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | ✅ |
| 30 | TransactionHeaderCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | ✅ |
| 31 | TransactionHeaderCtReference | CT_REFERENCE | — | ✅ |
| 32 | TransactionHeaderCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 33 | TransactionHeaderCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 34 | TransactionHeaderCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 35 | TransactionHeaderCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | ✅ |
| 36 | TransactionHeaderCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 37 | TransactionHeaderDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | ✅ |
| 38 | TransactionHeaderDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 39 | TransactionHeaderDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 40 | TransactionHeaderDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 41 | TransactionHeaderDelContactEmailAddress | DEL_CONTACT_EMAIL_ADDRESS | — | — |
| 42 | TransactionHeaderDeliveryMethodCode | DELIVERY_METHOD_CODE | — | — |
| 43 | TransactionHeaderDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 44 | TransactionHeaderDocSequenceValue | DOC_SEQUENCE_VALUE | — | ✅ |
| 45 | TransactionHeaderDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 46 | TransactionHeaderDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 47 | TransactionHeaderDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 48 | TransactionHeaderDraweeId | DRAWEE_ID | — | — |
| 49 | TransactionHeaderDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 50 | TransactionHeaderEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 51 | TransactionHeaderEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 52 | TransactionHeaderEndDateCommitment | END_DATE_COMMITMENT | — | ✅ |
| 53 | TransactionHeaderExchangeDate | EXCHANGE_DATE | — | ✅ |
| 54 | TransactionHeaderExchangeRate | EXCHANGE_RATE | — | ✅ |
| 55 | TransactionHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 56 | TransactionHeaderFinanceCharges | FINANCE_CHARGES | — | ✅ |
| 57 | TransactionHeaderFobPoint | FOB_POINT | — | ✅ |
| 58 | TransactionHeaderInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 59 | TransactionHeaderIntercompanyFlag | INTERCOMPANY_FLAG | — | ✅ |
| 60 | TransactionHeaderInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 61 | TransactionHeaderInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | ✅ |
| 62 | TransactionHeaderInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | ✅ |
| 63 | TransactionHeaderInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | ✅ |
| 64 | TransactionHeaderInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | ✅ |
| 65 | TransactionHeaderInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | ✅ |
| 66 | TransactionHeaderInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | ✅ |
| 67 | TransactionHeaderInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | ✅ |
| 68 | TransactionHeaderInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | ✅ |
| 69 | TransactionHeaderInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | ✅ |
| 70 | TransactionHeaderInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | ✅ |
| 71 | TransactionHeaderInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | ✅ |
| 72 | TransactionHeaderInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | ✅ |
| 73 | TransactionHeaderInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | ✅ |
| 74 | TransactionHeaderInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | ✅ |
| 75 | TransactionHeaderInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | ✅ |
| 76 | TransactionHeaderInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | ✅ |
| 77 | TransactionHeaderInternalNotes | INTERNAL_NOTES | — | ✅ |
| 78 | TransactionHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 79 | TransactionHeaderInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 80 | TransactionHeaderLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | ✅ |
| 81 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 84 | TransactionHeaderLateChargesAssessed | LATE_CHARGES_ASSESSED | — | ✅ |
| 85 | TransactionHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 86 | TransactionHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 87 | TransactionHeaderOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 88 | TransactionHeaderOrgId | ORG_ID | — | — |
| 89 | TransactionHeaderOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | ✅ |
| 90 | TransactionHeaderOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 91 | TransactionHeaderPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 92 | TransactionHeaderPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 93 | TransactionHeaderPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 94 | TransactionHeaderPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 95 | TransactionHeaderPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 96 | TransactionHeaderPostRequestId | POST_REQUEST_ID | — | — |
| 97 | TransactionHeaderPostingControlId | POSTING_CONTROL_ID | — | — |
| 98 | TransactionHeaderPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 99 | TransactionHeaderPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 100 | TransactionHeaderPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 101 | TransactionHeaderPrintingCount | PRINTING_COUNT | — | ✅ |
| 102 | TransactionHeaderPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 103 | TransactionHeaderPrintingOption | PRINTING_OPTION | — | ✅ |
| 104 | TransactionHeaderPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | ✅ |
| 105 | TransactionHeaderPrintingPending | PRINTING_PENDING | — | ✅ |
| 106 | TransactionHeaderProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 107 | TransactionHeaderProgramId | PROGRAM_ID | — | — |
| 108 | TransactionHeaderProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 109 | TransactionHeaderPurchaseOrder | PURCHASE_ORDER | — | ✅ |
| 110 | TransactionHeaderPurchaseOrderDate | PURCHASE_ORDER_DATE | — | ✅ |
| 111 | TransactionHeaderPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | ✅ |
| 112 | TransactionHeaderRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 113 | TransactionHeaderReasonCode | REASON_CODE | — | ✅ |
| 114 | TransactionHeaderReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 115 | TransactionHeaderRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 116 | TransactionHeaderRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 117 | TransactionHeaderRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 118 | TransactionHeaderRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 119 | TransactionHeaderRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 120 | TransactionHeaderRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 121 | TransactionHeaderRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 122 | TransactionHeaderRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 123 | TransactionHeaderRequestId | REQUEST_ID | — | — |
| 124 | TransactionHeaderRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | ✅ |
| 125 | TransactionHeaderRevRecApplication | REV_REC_APPLICATION | — | ✅ |
| 126 | TransactionHeaderReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 127 | TransactionHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 128 | TransactionHeaderShipDateActual | SHIP_DATE_ACTUAL | — | ✅ |
| 129 | TransactionHeaderShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 130 | TransactionHeaderShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 131 | TransactionHeaderShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 132 | TransactionHeaderShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 133 | TransactionHeaderShipVia | SHIP_VIA | — | ✅ |
| 134 | TransactionHeaderShipmentId | SHIPMENT_ID | — | — |
| 135 | TransactionHeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 136 | TransactionHeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 137 | TransactionHeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 138 | TransactionHeaderSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 139 | TransactionHeaderSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 140 | TransactionHeaderSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 141 | TransactionHeaderSpecialInstructions | SPECIAL_INSTRUCTIONS | — | ✅ |
| 142 | TransactionHeaderStartDateCommitment | START_DATE_COMMITMENT | — | ✅ |
| 143 | TransactionHeaderStatusTrx | STATUS_TRX | — | ✅ |
| 144 | TransactionHeaderTermDueDate | TERM_DUE_DATE | — | ✅ |
| 145 | TransactionHeaderTermId | TERM_ID | — | — |
| 146 | TransactionHeaderTerritoryId | TERRITORY_ID | — | — |
| 147 | TransactionHeaderTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 148 | TransactionHeaderTrxClass | TRX_CLASS | — | ✅ |
| 149 | TransactionHeaderTrxDate | TRX_DATE | — | ✅ |
| 150 | TransactionHeaderTrxNumber | TRX_NUMBER | — | ✅ |
| 151 | TransactionHeaderUpgradeMethod | UPGRADE_METHOD | — | — |
| 152 | TransactionHeaderUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 153 | TransactionHeaderWaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 154 | TransactionHeaderWhUpdateDate | WH_UPDATE_DATE | — | — |
| 155 | TrxHeaderPrevAddressVerificationCode | ADDRESS_VERIFICATION_CODE | — | — |
| 156 | TrxHeaderPrevAgreementId | AGREEMENT_ID | — | — |
| 157 | TrxHeaderPrevApplicationId | APPLICATION_ID | — | — |
| 158 | TrxHeaderPrevApprovalCode | APPROVAL_CODE | — | — |
| 159 | TrxHeaderPrevAxAccountedFlag | AX_ACCOUNTED_FLAG | — | — |
| 160 | TrxHeaderPrevBatchId | BATCH_ID | — | — |
| 161 | TrxHeaderPrevBatchSourceSeqId | BATCH_SOURCE_SEQ_ID | — | — |
| 162 | TrxHeaderPrevBillTemplateId | BILL_TEMPLATE_ID | — | — |
| 163 | TrxHeaderPrevBillToAddressId | BILL_TO_ADDRESS_ID | — | — |
| 164 | TrxHeaderPrevBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 165 | TrxHeaderPrevBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 166 | TrxHeaderPrevBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 167 | TrxHeaderPrevBillingDate | BILLING_DATE | — | — |
| 168 | TrxHeaderPrevBrAmount | BR_AMOUNT | — | — |
| 169 | TrxHeaderPrevBrOnHoldFlag | BR_ON_HOLD_FLAG | — | — |
| 170 | TrxHeaderPrevBrUnpaidFlag | BR_UNPAID_FLAG | — | — |
| 171 | TrxHeaderPrevCcErrorCode | CC_ERROR_CODE | — | — |
| 172 | TrxHeaderPrevCcErrorFlag | CC_ERROR_FLAG | — | — |
| 173 | TrxHeaderPrevCcErrorText | CC_ERROR_TEXT | — | — |
| 174 | TrxHeaderPrevComments | COMMENTS | — | — |
| 175 | TrxHeaderPrevCompleteFlag | COMPLETE_FLAG | — | — |
| 176 | TrxHeaderPrevContractId | CONTRACT_ID | — | — |
| 177 | TrxHeaderPrevCreatedBy | CREATED_BY | — | — |
| 178 | TrxHeaderPrevCreatedFrom | CREATED_FROM | — | — |
| 179 | TrxHeaderPrevCreationDate | CREATION_DATE | — | — |
| 180 | TrxHeaderPrevCreditMethodForInstallments | CREDIT_METHOD_FOR_INSTALLMENTS | — | — |
| 181 | TrxHeaderPrevCreditMethodForRules | CREDIT_METHOD_FOR_RULES | — | — |
| 182 | TrxHeaderPrevCtReference | CT_REFERENCE | — | — |
| 183 | TrxHeaderPrevCustTrxTypeSeqId | CUST_TRX_TYPE_SEQ_ID | — | — |
| 184 | TrxHeaderPrevCustomerBankAccountId | CUSTOMER_BANK_ACCOUNT_ID | — | — |
| 185 | TrxHeaderPrevCustomerReference | CUSTOMER_REFERENCE | — | — |
| 186 | TrxHeaderPrevCustomerReferenceDate | CUSTOMER_REFERENCE_DATE | — | — |
| 187 | TrxHeaderPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 188 | TrxHeaderPrevDefaultTaxExemptFlag | DEFAULT_TAX_EXEMPT_FLAG | — | — |
| 189 | TrxHeaderPrevDefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 190 | TrxHeaderPrevDefaultUssglTransactionCode | DEFAULT_USSGL_TRANSACTION_CODE | — | — |
| 191 | TrxHeaderPrevDefaultUssglTrxCodeContext | DEFAULT_USSGL_TRX_CODE_CONTEXT | — | — |
| 192 | TrxHeaderPrevDocSequenceId | DOC_SEQUENCE_ID | — | — |
| 193 | TrxHeaderPrevDocSequenceValue | DOC_SEQUENCE_VALUE | — | — |
| 194 | TrxHeaderPrevDocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 195 | TrxHeaderPrevDraweeBankAccountId | DRAWEE_BANK_ACCOUNT_ID | — | — |
| 196 | TrxHeaderPrevDraweeContactId | DRAWEE_CONTACT_ID | — | — |
| 197 | TrxHeaderPrevDraweeId | DRAWEE_ID | — | — |
| 198 | TrxHeaderPrevDraweeSiteUseId | DRAWEE_SITE_USE_ID | — | — |
| 199 | TrxHeaderPrevEdiProcessedFlag | EDI_PROCESSED_FLAG | — | — |
| 200 | TrxHeaderPrevEdiProcessedStatus | EDI_PROCESSED_STATUS | — | — |
| 201 | TrxHeaderPrevEndDateCommitment | END_DATE_COMMITMENT | — | — |
| 202 | TrxHeaderPrevExchangeDate | EXCHANGE_DATE | — | — |
| 203 | TrxHeaderPrevExchangeRate | EXCHANGE_RATE | — | — |
| 204 | TrxHeaderPrevExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 205 | TrxHeaderPrevFinanceCharges | FINANCE_CHARGES | — | — |
| 206 | TrxHeaderPrevFobPoint | FOB_POINT | — | — |
| 207 | TrxHeaderPrevInitialCustomerTrxId | INITIAL_CUSTOMER_TRX_ID | — | — |
| 208 | TrxHeaderPrevIntercompanyFlag | INTERCOMPANY_FLAG | — | — |
| 209 | TrxHeaderPrevInterestHeaderId | INTEREST_HEADER_ID | — | — |
| 210 | TrxHeaderPrevInterfaceHeaderAttribute1 | INTERFACE_HEADER_ATTRIBUTE1 | — | — |
| 211 | TrxHeaderPrevInterfaceHeaderAttribute10 | INTERFACE_HEADER_ATTRIBUTE10 | — | — |
| 212 | TrxHeaderPrevInterfaceHeaderAttribute11 | INTERFACE_HEADER_ATTRIBUTE11 | — | — |
| 213 | TrxHeaderPrevInterfaceHeaderAttribute12 | INTERFACE_HEADER_ATTRIBUTE12 | — | — |
| 214 | TrxHeaderPrevInterfaceHeaderAttribute13 | INTERFACE_HEADER_ATTRIBUTE13 | — | — |
| 215 | TrxHeaderPrevInterfaceHeaderAttribute14 | INTERFACE_HEADER_ATTRIBUTE14 | — | — |
| 216 | TrxHeaderPrevInterfaceHeaderAttribute15 | INTERFACE_HEADER_ATTRIBUTE15 | — | — |
| 217 | TrxHeaderPrevInterfaceHeaderAttribute2 | INTERFACE_HEADER_ATTRIBUTE2 | — | — |
| 218 | TrxHeaderPrevInterfaceHeaderAttribute3 | INTERFACE_HEADER_ATTRIBUTE3 | — | — |
| 219 | TrxHeaderPrevInterfaceHeaderAttribute4 | INTERFACE_HEADER_ATTRIBUTE4 | — | — |
| 220 | TrxHeaderPrevInterfaceHeaderAttribute5 | INTERFACE_HEADER_ATTRIBUTE5 | — | — |
| 221 | TrxHeaderPrevInterfaceHeaderAttribute6 | INTERFACE_HEADER_ATTRIBUTE6 | — | — |
| 222 | TrxHeaderPrevInterfaceHeaderAttribute7 | INTERFACE_HEADER_ATTRIBUTE7 | — | — |
| 223 | TrxHeaderPrevInterfaceHeaderAttribute8 | INTERFACE_HEADER_ATTRIBUTE8 | — | — |
| 224 | TrxHeaderPrevInterfaceHeaderAttribute9 | INTERFACE_HEADER_ATTRIBUTE9 | — | — |
| 225 | TrxHeaderPrevInterfaceHeaderContext | INTERFACE_HEADER_CONTEXT | — | — |
| 226 | TrxHeaderPrevInternalNotes | INTERNAL_NOTES | — | — |
| 227 | TrxHeaderPrevInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 228 | TrxHeaderPrevInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 229 | TrxHeaderPrevLastPrintedSequenceNum | LAST_PRINTED_SEQUENCE_NUM | — | — |
| 230 | TrxHeaderPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 231 | TrxHeaderPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 232 | TrxHeaderPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 233 | TrxHeaderPrevLateChargesAssessed | LATE_CHARGES_ASSESSED | — | — |
| 234 | TrxHeaderPrevLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 235 | TrxHeaderPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 236 | TrxHeaderPrevOldTrxNumber | OLD_TRX_NUMBER | — | — |
| 237 | TrxHeaderPrevOrgId | ORG_ID | — | — |
| 238 | TrxHeaderPrevOrigSystemBatchName | ORIG_SYSTEM_BATCH_NAME | — | — |
| 239 | TrxHeaderPrevOverrideRemitAccountFlag | OVERRIDE_REMIT_ACCOUNT_FLAG | — | — |
| 240 | TrxHeaderPrevPayingCustomerId | PAYING_CUSTOMER_ID | — | — |
| 241 | TrxHeaderPrevPayingSiteUseId | PAYING_SITE_USE_ID | — | — |
| 242 | TrxHeaderPrevPaymentAttributes | PAYMENT_ATTRIBUTES | — | — |
| 243 | TrxHeaderPrevPaymentServerOrderNum | PAYMENT_SERVER_ORDER_NUM | — | — |
| 244 | TrxHeaderPrevPaymentTrxnExtensionId | PAYMENT_TRXN_EXTENSION_ID | — | — |
| 245 | TrxHeaderPrevPostRequestId | POST_REQUEST_ID | — | — |
| 246 | TrxHeaderPrevPostingControlId | POSTING_CONTROL_ID | — | — |
| 247 | TrxHeaderPrevPrepaymentFlag | PREPAYMENT_FLAG | — | — |
| 248 | TrxHeaderPrevPreviousCustomerTrxId | PREVIOUS_CUSTOMER_TRX_ID | — | — |
| 249 | TrxHeaderPrevPrimaryResourceSalesrepId | PRIMARY_RESOURCE_SALESREP_ID | — | — |
| 250 | TrxHeaderPrevPrintingCount | PRINTING_COUNT | — | — |
| 251 | TrxHeaderPrevPrintingLastPrinted | PRINTING_LAST_PRINTED | — | — |
| 252 | TrxHeaderPrevPrintingOption | PRINTING_OPTION | — | — |
| 253 | TrxHeaderPrevPrintingOriginalDate | PRINTING_ORIGINAL_DATE | — | — |
| 254 | TrxHeaderPrevPrintingPending | PRINTING_PENDING | — | — |
| 255 | TrxHeaderPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 256 | TrxHeaderPrevProgramId | PROGRAM_ID | — | — |
| 257 | TrxHeaderPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 258 | TrxHeaderPrevPurchaseOrder | PURCHASE_ORDER | — | — |
| 259 | TrxHeaderPrevPurchaseOrderDate | PURCHASE_ORDER_DATE | — | — |
| 260 | TrxHeaderPrevPurchaseOrderRevision | PURCHASE_ORDER_REVISION | — | — |
| 261 | TrxHeaderPrevRaPostLoopNumber | RA_POST_LOOP_NUMBER | — | — |
| 262 | TrxHeaderPrevReasonCode | REASON_CODE | — | — |
| 263 | TrxHeaderPrevReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 264 | TrxHeaderPrevRecurredFromTrxNumber | RECURRED_FROM_TRX_NUMBER | — | — |
| 265 | TrxHeaderPrevRelatedBatchSourceSeqId | RELATED_BATCH_SOURCE_SEQ_ID | — | — |
| 266 | TrxHeaderPrevRelatedCustomerTrxId | RELATED_CUSTOMER_TRX_ID | — | — |
| 267 | TrxHeaderPrevRemitBankAcctUseId | REMIT_BANK_ACCT_USE_ID | — | — |
| 268 | TrxHeaderPrevRemitToAddressId | REMIT_TO_ADDRESS_ID | — | — |
| 269 | TrxHeaderPrevRemitToAddressSeqId | REMIT_TO_ADDRESS_SEQ_ID | — | — |
| 270 | TrxHeaderPrevRemittanceBankAccountId | REMITTANCE_BANK_ACCOUNT_ID | — | — |
| 271 | TrxHeaderPrevRemittanceBatchId | REMITTANCE_BATCH_ID | — | — |
| 272 | TrxHeaderPrevRequestId | REQUEST_ID | — | — |
| 273 | TrxHeaderPrevRequiresManualScheduling | REQUIRES_MANUAL_SCHEDULING | — | — |
| 274 | TrxHeaderPrevReversedCashReceiptId | REVERSED_CASH_RECEIPT_ID | — | — |
| 275 | TrxHeaderPrevSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 276 | TrxHeaderPrevShipDateActual | SHIP_DATE_ACTUAL | — | — |
| 277 | TrxHeaderPrevShipToAddressId | SHIP_TO_ADDRESS_ID | — | — |
| 278 | TrxHeaderPrevShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 279 | TrxHeaderPrevShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 280 | TrxHeaderPrevShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 281 | TrxHeaderPrevShipVia | SHIP_VIA | — | — |
| 282 | TrxHeaderPrevShipmentId | SHIPMENT_ID | — | — |
| 283 | TrxHeaderPrevSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 284 | TrxHeaderPrevSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 285 | TrxHeaderPrevSoldToSiteUseId | SOLD_TO_SITE_USE_ID | — | — |
| 286 | TrxHeaderPrevSourceDocumentId | SOURCE_DOCUMENT_ID | — | — |
| 287 | TrxHeaderPrevSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 288 | TrxHeaderPrevSpecialInstructions | SPECIAL_INSTRUCTIONS | — | — |
| 289 | TrxHeaderPrevStartDateCommitment | START_DATE_COMMITMENT | — | — |
| 290 | TrxHeaderPrevStatusTrx | STATUS_TRX | — | — |
| 291 | TrxHeaderPrevTermDueDate | TERM_DUE_DATE | — | — |
| 292 | TrxHeaderPrevTermId | TERM_ID | — | — |
| 293 | TrxHeaderPrevTerritoryId | TERRITORY_ID | — | — |
| 294 | TrxHeaderPrevTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 295 | TrxHeaderPrevTrxClass | TRX_CLASS | — | — |
| 296 | TrxHeaderPrevTrxDate | TRX_DATE | — | — |
| 297 | TrxHeaderPrevTrxNumber | TRX_NUMBER | — | ✅ |
| 298 | TrxHeaderPrevUpgradeMethod | UPGRADE_METHOD | — | — |
| 299 | TrxHeaderPrevUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 300 | TrxHeaderPrevWaybillNumber | WAYBILL_NUMBER | — | — |
| 301 | TrxHeaderPrevWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_cust_trx_line_salesreps_all|RA_CUST_TRX_LINE_SALESREPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | 🔑 | ✅ |
| 2 | SalesCreditCreatedBy | CREATED_BY | — | — |
| 3 | SalesCreditCreationDate | CREATION_DATE | — | — |
| 4 | SalesCreditCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 5 | SalesCreditCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 6 | SalesCreditLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SalesCreditLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SalesCreditLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SalesCreditNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | ✅ |
| 10 | SalesCreditNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | ✅ |
| 11 | SalesCreditNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 12 | SalesCreditObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | SalesCreditOrgId | ORG_ID | — | — |
| 14 | SalesCreditOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 15 | SalesCreditPrevCreatedBy | CREATED_BY | — | — |
| 16 | SalesCreditPrevCreationDate | CREATION_DATE | — | — |
| 17 | SalesCreditPrevCustTrxLineSalesrepId | CUST_TRX_LINE_SALESREP_ID | — | — |
| 18 | SalesCreditPrevCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 19 | SalesCreditPrevCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 20 | SalesCreditPrevLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | SalesCreditPrevLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | SalesCreditPrevLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | SalesCreditPrevNonRevenueAmountSplit | NON_REVENUE_AMOUNT_SPLIT | — | — |
| 24 | SalesCreditPrevNonRevenuePercentSplit | NON_REVENUE_PERCENT_SPLIT | — | — |
| 25 | SalesCreditPrevNonRevenueSalesgroupId | NON_REVENUE_SALESGROUP_ID | — | — |
| 26 | SalesCreditPrevObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | SalesCreditPrevOrgId | ORG_ID | — | — |
| 28 | SalesCreditPrevOriginalLineSalesrepId | ORIGINAL_LINE_SALESREP_ID | — | — |
| 29 | SalesCreditPrevPrevCustTrxLineSalesrepId | PREV_CUST_TRX_LINE_SALESREP_ID | — | — |
| 30 | SalesCreditPrevProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 31 | SalesCreditPrevProgramId | PROGRAM_ID | — | — |
| 32 | SalesCreditPrevProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 33 | SalesCreditPrevRequestId | REQUEST_ID | — | — |
| 34 | SalesCreditPrevResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 35 | SalesCreditPrevRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 36 | SalesCreditPrevRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | — |
| 37 | SalesCreditPrevRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | — |
| 38 | SalesCreditPrevRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 39 | SalesCreditPrevWhUpdateDate | WH_UPDATE_DATE | — | — |
| 40 | SalesCreditProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 41 | SalesCreditProgramId | PROGRAM_ID | — | — |
| 42 | SalesCreditProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 43 | SalesCreditRequestId | REQUEST_ID | — | — |
| 44 | SalesCreditResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 45 | SalesCreditRevenueAdjustmentId | REVENUE_ADJUSTMENT_ID | — | — |
| 46 | SalesCreditRevenueAmountSplit | REVENUE_AMOUNT_SPLIT | — | ✅ |
| 47 | SalesCreditRevenuePercentSplit | REVENUE_PERCENT_SPLIT | — | ✅ |
| 48 | SalesCreditRevenueSalesgroupId | REVENUE_SALESGROUP_ID | — | — |
| 49 | SalesCreditWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvDistRuleDescription | DESCRIPTION | — | — |
| 2 | InvDistRuleName | NAME | — | ✅ |
| 3 | InvDistRuleRuleId | RULE_ID | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zx_fc_user_defined_v|ZX_FC_USER_DEFINED_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UsrDfndFiscClsClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | UsrDfndFiscClsClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 3 | UsrDfndFiscClsCountryCode | COUNTRY_CODE | — | — |

### [[zx_registrations|ZX_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FirstPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | FirstPartyRegistrationId | REGISTRATION_ID | — | — |
| 3 | FirstPartyRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 4 | ThirdPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | ThirdPartyRegistrationId | REGISTRATION_ID | — | — |
| 6 | ThirdPartyRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
