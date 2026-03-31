---
id: DOC-AP-PVO-InvoiceDistributionPVO
doc_type: system-doc
title: "InvoiceDistributionPVO — PVO Accounts Payable"
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
  - InvoiceDistributionPVO
  - invoicedistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceDistributionPVO

## 📌 Visão Geral

Extrai as distribuições contábeis das faturas de fornecedores, incluindo centro de custo, projeto, conta contábil, valores e classificação fiscal. Essencial para contabilização precisa do contas a pagar, análise de despesas por centro de custo e rastreabilidade contábil.

**Caminho:** `FscmTopModelAM.InvoiceDistributionAM.InvoiceDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 376 | 28 | 1 | 168 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos (1 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 4 atributos (1 BICC)
- [[fnd_messages_vl|FND_MESSAGES_VL]] — 3 atributos (2 BICC)
- [[fun_ic_cust_supp_map|FUN_IC_CUST_SUPP_MAP]] — 2 atributos (2 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 6 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 3 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 5 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 8 atributos (1 BICC)
- [[okc_k_headers_vl|OKC_K_HEADERS_VL]] — 6 atributos (4 BICC)
- [[okc_k_lines_vl|OKC_K_LINES_VL]] — 5 atributos (4 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (4 BICC)
- [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]] — 2 atributos
- [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]] — 3 atributos (1 BICC)
- [[pjb_invoice_formats|PJB_INVOICE_FORMATS]] — 2 atributos (1 BICC)
- [[pjb_invoice_headers|PJB_INVOICE_HEADERS]] — 62 atributos (42 BICC)
- [[pjb_invoice_lines|PJB_INVOICE_LINES]] — 68 atributos (19 BICC)
- [[pjb_inv_line_dists|PJB_INV_LINE_DISTS]] — 142 atributos (1 PKs, 77 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 6 atributos (1 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 10 atributos (1 BICC)
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 2 atributos
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 2 atributos
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (1 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos (1 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 4 atributos (2 BICC)
- [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]] — 3 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 2 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[fnd_messages_vl|FND_MESSAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrfrRejReasonCodeMessagePEOApplicationId | APPLICATION_ID | — | — |
| 2 | TrfrRejReasonCodeMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 3 | TrfrRejReasonCodeMessagePEOMessageText | MESSAGE_TEXT | — | ✅ |

### [[fun_ic_cust_supp_map|FUN_IC_CUST_SUPP_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunIcCustSuppMapPEOCustSuppMapId | CUST_SUPP_MAP_ID | — | ✅ |
| 2 | FunIcCustSuppMapPEOVendorId | VENDOR_ID | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContCurrInvRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 2 | ContCurrInvRateTypePEODescription | DESCRIPTION | — | — |
| 3 | LedgerCurrInvRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 4 | LedgerCurrInvRateTypePEODescription | DESCRIPTION | — | — |
| 5 | ProjCurrInvRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 6 | ProjCurrInvRateTypePEODescription | DESCRIPTION | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpOrgDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ExpOrgDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ExpOrgDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | BUPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 3 | EffectiveEndDate4 | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate3 | EFFECTIVE_START_DATE | — | — |
| 5 | OrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPEOName | NAME | — | — |
| 2 | EffectiveEndDate5 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate4 | EFFECTIVE_START_DATE | — | — |
| 4 | Language | LANGUAGE | — | — |
| 5 | OrganizationId | ORGANIZATION_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToCustomerAccountPEOAccountName | ACCOUNT_NAME | — | — |
| 2 | BillToCustomerAccountPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 3 | BillToCustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 4 | BillToCustomerAccountPEOPartyId | PARTY_ID | — | — |
| 5 | ShipToCustomerAccountPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 6 | ShipToCustomerAccountPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 7 | ShipToCustomerAccountPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 8 | ShipToCustomerAccountPEOPartyId | PARTY_ID | — | — |

### [[okc_k_headers_vl|OKC_K_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderPEOContractNumber | CONTRACT_NUMBER | — | ✅ |
| 2 | ContractHeaderPEODescription | DESCRIPTION | — | ✅ |
| 3 | ContractHeaderPEOId | ID | — | ✅ |
| 4 | ContractHeaderPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 5 | ContractHeaderPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 6 | ContractHeaderPEOOwningOrgId | OWNING_ORG_ID | — | — |

### [[okc_k_lines_vl|OKC_K_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLinePEOId | ID | — | ✅ |
| 2 | ContractLinePEOLineName | LINE_NAME | — | ✅ |
| 3 | ContractLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 4 | ContractLinePEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 5 | ContractLinePEOStsCode | STS_CODE | — | — |

### [[per_jobs_f_vl|PER_JOBS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JobDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | JobDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | JobDPEOJobId | JOB_ID | — | — |
| 4 | JobDPEOName | NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 5 | PersonNameDPEO1DisplayName | DISPLAY_NAME | — | ✅ |
| 6 | PersonNameDPEODisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonNameId1 | PERSON_NAME_ID | — | — |

### [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingExtensionPEOBillingExtensionId | BILLING_EXTENSION_ID | — | — |
| 2 | BillingExtensionPEOBillingExtensionName | BILLING_EXTENSION_NAME | — | — |

### [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillPlanPEOBillPlanId | BILL_PLAN_ID | — | — |
| 2 | BillPlanPEOBillPlanName | BILL_PLAN_NAME | — | ✅ |
| 3 | BillPlanPEOMajorVersion | MAJOR_VERSION | — | — |

### [[pjb_invoice_formats|PJB_INVOICE_FORMATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceFormatPEOInvoiceFormatId | INVOICE_FORMAT_ID | — | — |
| 2 | InvoiceFormatPEOName | NAME | — | ✅ |

### [[pjb_invoice_headers|PJB_INVOICE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditedInvoicePEOInvoiceId | INVOICE_ID | — | — |
| 2 | CreditedInvoicePEOInvoiceNum | INVOICE_NUM | — | ✅ |
| 3 | InvoiceHeaderPEOAcctdCurrencyCode | ACCTD_CURRENCY_CODE | — | — |
| 4 | InvoiceHeaderPEOAcctdExchgRate | ACCTD_EXCHG_RATE | — | ✅ |
| 5 | InvoiceHeaderPEOAcctdRateDate | ACCTD_RATE_DATE | — | ✅ |
| 6 | InvoiceHeaderPEOAcctdRateType | ACCTD_RATE_TYPE | — | ✅ |
| 7 | InvoiceHeaderPEOApprovedByPersonId | APPROVED_BY_PERSON_ID | — | ✅ |
| 8 | InvoiceHeaderPEOApprovedDate | APPROVED_DATE | — | ✅ |
| 9 | InvoiceHeaderPEOBillFromDate | BILL_FROM_DATE | — | ✅ |
| 10 | InvoiceHeaderPEOBillSetNum | BILL_SET_NUM | — | ✅ |
| 11 | InvoiceHeaderPEOBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 12 | InvoiceHeaderPEOBillToCustAcctId | BILL_TO_CUST_ACCT_ID | — | — |
| 13 | InvoiceHeaderPEOBillToDate | BILL_TO_DATE | — | ✅ |
| 14 | InvoiceHeaderPEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 15 | InvoiceHeaderPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 16 | InvoiceHeaderPEOCancelledFlag | CANCELLED_FLAG | — | ✅ |
| 17 | InvoiceHeaderPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | — |
| 18 | InvoiceHeaderPEOContractId | CONTRACT_ID | — | — |
| 19 | InvoiceHeaderPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 20 | InvoiceHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | InvoiceHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | InvoiceHeaderPEOCreditMemoReasonCode | CREDIT_MEMO_REASON_CODE | — | ✅ |
| 23 | InvoiceHeaderPEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | — |
| 24 | InvoiceHeaderPEODocNumber | DOC_NUMBER | — | — |
| 25 | InvoiceHeaderPEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 26 | InvoiceHeaderPEOExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 27 | InvoiceHeaderPEOExportProcessId | EXPORT_PROCESS_ID | — | ✅ |
| 28 | InvoiceHeaderPEOGenerationErrorFlag | GENERATION_ERROR_FLAG | — | ✅ |
| 29 | InvoiceHeaderPEOGlDate | GL_DATE | — | ✅ |
| 30 | InvoiceHeaderPEOGlPeriodName | GL_PERIOD_NAME | — | — |
| 31 | InvoiceHeaderPEOInApTransferStatusCode | IN_AP_TRANSFER_STATUS_CODE | — | ✅ |
| 32 | InvoiceHeaderPEOInvoiceComment | INVOICE_COMMENT | — | ✅ |
| 33 | InvoiceHeaderPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 34 | InvoiceHeaderPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 35 | InvoiceHeaderPEOInvoiceId | INVOICE_ID | — | ✅ |
| 36 | InvoiceHeaderPEOInvoiceInstructions | INVOICE_INSTRUCTIONS | — | ✅ |
| 37 | InvoiceHeaderPEOInvoiceNum | INVOICE_NUM | — | ✅ |
| 38 | InvoiceHeaderPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 39 | InvoiceHeaderPEOInvoiceTypeCode | INVOICE_TYPE_CODE | — | ✅ |
| 40 | InvoiceHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 41 | InvoiceHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 42 | InvoiceHeaderPEOLang | LANG | — | ✅ |
| 43 | InvoiceHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | InvoiceHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | InvoiceHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | InvoiceHeaderPEOLocNumber | LOC_NUMBER | — | — |
| 47 | InvoiceHeaderPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 48 | InvoiceHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | InvoiceHeaderPEOOrgId | ORG_ID | — | — |
| 50 | InvoiceHeaderPEOPaDate | PA_DATE | — | ✅ |
| 51 | InvoiceHeaderPEOPaPeriodName | PA_PERIOD_NAME | — | ✅ |
| 52 | InvoiceHeaderPEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 53 | InvoiceHeaderPEOPurgeFlag | PURGE_FLAG | — | ✅ |
| 54 | InvoiceHeaderPEORaInvoiceNumber | RA_INVOICE_NUMBER | — | ✅ |
| 55 | InvoiceHeaderPEOReleasedByPersonId | RELEASED_BY_PERSON_ID | — | ✅ |
| 56 | InvoiceHeaderPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 57 | InvoiceHeaderPEORequestId | REQUEST_ID | — | — |
| 58 | InvoiceHeaderPEOSystemReference | SYSTEM_REFERENCE | — | ✅ |
| 59 | InvoiceHeaderPEOTaxationCountry | TAXATION_COUNTRY | — | ✅ |
| 60 | InvoiceHeaderPEOTransferRejectReasonCode | TRANSFER_REJECT_REASON_CODE | — | — |
| 61 | InvoiceHeaderPEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 62 | InvoiceHeaderPEOTransferredDate | TRANSFERRED_DATE | — | ✅ |

### [[pjb_invoice_lines|PJB_INVOICE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditedInvoiceLinePEOInvoiceLineId | INVOICE_LINE_ID | — | ✅ |
| 2 | CreditedInvoiceLinePEOInvoiceLineNum | INVOICE_LINE_NUM | — | ✅ |
| 3 | CreditedInvoiceLinePEOInvoiceNum | INVOICE_NUM | — | — |
| 4 | InvoiceLinePEOAcctdCurrencyAmt | ACCTD_CURRENCY_AMT | — | — |
| 5 | InvoiceLinePEOAcctdCurrencyCode | ACCTD_CURRENCY_CODE | — | — |
| 6 | InvoiceLinePEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 7 | InvoiceLinePEOBillPlanId | BILL_PLAN_ID | — | — |
| 8 | InvoiceLinePEOBillSetNum | BILL_SET_NUM | — | — |
| 9 | InvoiceLinePEOContractCurrCreditAmt | CONTRACT_CURR_CREDIT_AMT | — | — |
| 10 | InvoiceLinePEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | — |
| 11 | InvoiceLinePEOContractCurrencyInvAmt | CONTRACT_CURRENCY_INV_AMT | — | — |
| 12 | InvoiceLinePEOContractId | CONTRACT_ID | — | — |
| 13 | InvoiceLinePEOContractLineId | CONTRACT_LINE_ID | — | — |
| 14 | InvoiceLinePEOCreatedBy | CREATED_BY | — | — |
| 15 | InvoiceLinePEOCreationDate | CREATION_DATE | — | — |
| 16 | InvoiceLinePEOCreditProcessedFlag | CREDIT_PROCESSED_FLAG | — | ✅ |
| 17 | InvoiceLinePEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | — |
| 18 | InvoiceLinePEOCreditedInvoiceLineId | CREDITED_INVOICE_LINE_ID | — | — |
| 19 | InvoiceLinePEODocNumber | DOC_NUMBER | — | — |
| 20 | InvoiceLinePEOExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 21 | InvoiceLinePEOExpenditureOrgId | EXPENDITURE_ORG_ID | — | — |
| 22 | InvoiceLinePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 23 | InvoiceLinePEOInApTransferStatusCode | IN_AP_TRANSFER_STATUS_CODE | — | — |
| 24 | InvoiceLinePEOIntendedUse | INTENDED_USE | — | — |
| 25 | InvoiceLinePEOInvBilledQuantity | INV_BILLED_QUANTITY | — | — |
| 26 | InvoiceLinePEOInvCurrLineAmt | INV_CURR_LINE_AMT | — | ✅ |
| 27 | InvoiceLinePEOInvCurrUnitPrice | INV_CURR_UNIT_PRICE | — | — |
| 28 | InvoiceLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 29 | InvoiceLinePEOInvoiceCurrCreditAmt | INVOICE_CURR_CREDIT_AMT | — | — |
| 30 | InvoiceLinePEOInvoiceCurrCreditPct | INVOICE_CURR_CREDIT_PCT | — | ✅ |
| 31 | InvoiceLinePEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 32 | InvoiceLinePEOInvoiceFormatId | INVOICE_FORMAT_ID | — | — |
| 33 | InvoiceLinePEOInvoiceId | INVOICE_ID | — | ✅ |
| 34 | InvoiceLinePEOInvoiceLineDesc | INVOICE_LINE_DESC | — | ✅ |
| 35 | InvoiceLinePEOInvoiceLineId | INVOICE_LINE_ID | — | ✅ |
| 36 | InvoiceLinePEOInvoiceLineNum | INVOICE_LINE_NUM | — | ✅ |
| 37 | InvoiceLinePEOInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 38 | InvoiceLinePEOInvoiceNum | INVOICE_NUM | — | — |
| 39 | InvoiceLinePEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 40 | InvoiceLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 41 | InvoiceLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 42 | InvoiceLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | InvoiceLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | InvoiceLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | InvoiceLinePEOLocNumber | LOC_NUMBER | — | — |
| 46 | InvoiceLinePEOMajorVersion | MAJOR_VERSION | — | — |
| 47 | InvoiceLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | InvoiceLinePEOOutputTaxAmt | OUTPUT_TAX_AMT | — | ✅ |
| 49 | InvoiceLinePEOOutputTaxClassCode | OUTPUT_TAX_CLASS_CODE | — | — |
| 50 | InvoiceLinePEOOutputTaxExemptFlag | OUTPUT_TAX_EXEMPT_FLAG | — | — |
| 51 | InvoiceLinePEOOutputTaxExmtCertNumber | OUTPUT_TAX_EXMT_CERT_NUMBER | — | — |
| 52 | InvoiceLinePEOOutputTaxExmtReasonCode | OUTPUT_TAX_EXMT_REASON_CODE | — | — |
| 53 | InvoiceLinePEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 54 | InvoiceLinePEOProductCategory | PRODUCT_CATEGORY | — | — |
| 55 | InvoiceLinePEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 56 | InvoiceLinePEOProductType | PRODUCT_TYPE | — | ✅ |
| 57 | InvoiceLinePEORecalcExtnFlag | RECALC_EXTN_FLAG | — | ✅ |
| 58 | InvoiceLinePEOReceiverProjectId | RECEIVER_PROJECT_ID | — | ✅ |
| 59 | InvoiceLinePEOReceiverTaskId | RECEIVER_TASK_ID | — | — |
| 60 | InvoiceLinePEORequestId | REQUEST_ID | — | — |
| 61 | InvoiceLinePEOShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 62 | InvoiceLinePEOShipToCustAcctId | SHIP_TO_CUST_ACCT_ID | — | — |
| 63 | InvoiceLinePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 64 | InvoiceLinePEOTranslatedText | TRANSLATED_TEXT | — | ✅ |
| 65 | InvoiceLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 66 | InvoiceLinePEOUomCode | UOM_CODE | — | — |
| 67 | InvoiceLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 68 | InvoiceLinePEOWriteOffFlag | WRITE_OFF_FLAG | — | ✅ |

### [[pjb_inv_line_dists|PJB_INV_LINE_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceDistId | INVOICE_DIST_ID | 🔑 | ✅ |
| 2 | InvoiceDistributionPEOAccruedFlag | ACCRUED_FLAG | — | ✅ |
| 3 | InvoiceDistributionPEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 4 | InvoiceDistributionPEOBillEmployeeBillingTitle | BILL_EMPLOYEE_BILLING_TITLE | — | ✅ |
| 5 | InvoiceDistributionPEOBillFromDate | BILL_FROM_DATE | — | — |
| 6 | InvoiceDistributionPEOBillJobBillingTitle | BILL_JOB_BILLING_TITLE | — | ✅ |
| 7 | InvoiceDistributionPEOBillJobId | BILL_JOB_ID | — | ✅ |
| 8 | InvoiceDistributionPEOBillPlanId | BILL_PLAN_ID | — | — |
| 9 | InvoiceDistributionPEOBillRate | BILL_RATE | — | ✅ |
| 10 | InvoiceDistributionPEOBillSetNum | BILL_SET_NUM | — | — |
| 11 | InvoiceDistributionPEOBillToDate | BILL_TO_DATE | — | — |
| 12 | InvoiceDistributionPEOBillTransactionTypeCode | BILL_TRANSACTION_TYPE_CODE | — | ✅ |
| 13 | InvoiceDistributionPEOBillTrxId | BILL_TRX_ID | — | — |
| 14 | InvoiceDistributionPEOBillingExtensionId | BILLING_EXTENSION_ID | — | — |
| 15 | InvoiceDistributionPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 16 | InvoiceDistributionPEOCanceledFlag | CANCELED_FLAG | — | — |
| 17 | InvoiceDistributionPEOContCurrBilledAmt | CONT_CURR_BILLED_AMT | — | ✅ |
| 18 | InvoiceDistributionPEOContCurrConcessionAmt | CONT_CURR_CONCESSION_AMT | — | ✅ |
| 19 | InvoiceDistributionPEOContCurrCreditAmt | CONT_CURR_CREDIT_AMT | — | ✅ |
| 20 | InvoiceDistributionPEOContCurrInvDateType | CONT_CURR_INV_DATE_TYPE | — | ✅ |
| 21 | InvoiceDistributionPEOContCurrInvExchgDate | CONT_CURR_INV_EXCHG_DATE | — | ✅ |
| 22 | InvoiceDistributionPEOContCurrInvExchgRate | CONT_CURR_INV_EXCHG_RATE | — | ✅ |
| 23 | InvoiceDistributionPEOContCurrInvRateType | CONT_CURR_INV_RATE_TYPE | — | ✅ |
| 24 | InvoiceDistributionPEOContCurrWriteoffAmt | CONT_CURR_WRITEOFF_AMT | — | — |
| 25 | InvoiceDistributionPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 26 | InvoiceDistributionPEOContractId | CONTRACT_ID | — | ✅ |
| 27 | InvoiceDistributionPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 28 | InvoiceDistributionPEOContractProjectLinkageId | CONTRACT_PROJECT_LINKAGE_ID | — | — |
| 29 | InvoiceDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 30 | InvoiceDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 31 | InvoiceDistributionPEOCreditedDistId | CREDITED_DIST_ID | — | ✅ |
| 32 | InvoiceDistributionPEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | ✅ |
| 33 | InvoiceDistributionPEOCreditedInvoiceLineId | CREDITED_INVOICE_LINE_ID | — | — |
| 34 | InvoiceDistributionPEODocNumber | DOC_NUMBER | — | — |
| 35 | InvoiceDistributionPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 36 | InvoiceDistributionPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 37 | InvoiceDistributionPEOIntendedUse | INTENDED_USE | — | — |
| 38 | InvoiceDistributionPEOInvBilledQuantity | INV_BILLED_QUANTITY | — | ✅ |
| 39 | InvoiceDistributionPEOInvBillingControlId1 | INV_BILLING_CONTROL_ID1 | — | — |
| 40 | InvoiceDistributionPEOInvBillingControlId10 | INV_BILLING_CONTROL_ID10 | — | — |
| 41 | InvoiceDistributionPEOInvBillingControlId11 | INV_BILLING_CONTROL_ID11 | — | — |
| 42 | InvoiceDistributionPEOInvBillingControlId12 | INV_BILLING_CONTROL_ID12 | — | — |
| 43 | InvoiceDistributionPEOInvBillingControlId13 | INV_BILLING_CONTROL_ID13 | — | — |
| 44 | InvoiceDistributionPEOInvBillingControlId14 | INV_BILLING_CONTROL_ID14 | — | — |
| 45 | InvoiceDistributionPEOInvBillingControlId15 | INV_BILLING_CONTROL_ID15 | — | — |
| 46 | InvoiceDistributionPEOInvBillingControlId16 | INV_BILLING_CONTROL_ID16 | — | — |
| 47 | InvoiceDistributionPEOInvBillingControlId17 | INV_BILLING_CONTROL_ID17 | — | — |
| 48 | InvoiceDistributionPEOInvBillingControlId18 | INV_BILLING_CONTROL_ID18 | — | — |
| 49 | InvoiceDistributionPEOInvBillingControlId19 | INV_BILLING_CONTROL_ID19 | — | — |
| 50 | InvoiceDistributionPEOInvBillingControlId2 | INV_BILLING_CONTROL_ID2 | — | — |
| 51 | InvoiceDistributionPEOInvBillingControlId20 | INV_BILLING_CONTROL_ID20 | — | — |
| 52 | InvoiceDistributionPEOInvBillingControlId3 | INV_BILLING_CONTROL_ID3 | — | — |
| 53 | InvoiceDistributionPEOInvBillingControlId4 | INV_BILLING_CONTROL_ID4 | — | — |
| 54 | InvoiceDistributionPEOInvBillingControlId5 | INV_BILLING_CONTROL_ID5 | — | — |
| 55 | InvoiceDistributionPEOInvBillingControlId6 | INV_BILLING_CONTROL_ID6 | — | — |
| 56 | InvoiceDistributionPEOInvBillingControlId7 | INV_BILLING_CONTROL_ID7 | — | — |
| 57 | InvoiceDistributionPEOInvBillingControlId8 | INV_BILLING_CONTROL_ID8 | — | — |
| 58 | InvoiceDistributionPEOInvBillingControlId9 | INV_BILLING_CONTROL_ID9 | — | — |
| 59 | InvoiceDistributionPEOInvBurdenCompileSetId | INV_BURDEN_COMPILE_SET_ID | — | — |
| 60 | InvoiceDistributionPEOInvCurrConcessionAmt | INV_CURR_CONCESSION_AMT | — | ✅ |
| 61 | InvoiceDistributionPEOInvCurrUnitPrice | INV_CURR_UNIT_PRICE | — | ✅ |
| 62 | InvoiceDistributionPEOInvCurrWriteoffAmt | INV_CURR_WRITEOFF_AMT | — | — |
| 63 | InvoiceDistributionPEOInvDiscountReasonCode | INV_DISCOUNT_REASON_CODE | — | ✅ |
| 64 | InvoiceDistributionPEOInvDistributionTypeCode | INV_DISTRIBUTION_TYPE_CODE | — | ✅ |
| 65 | InvoiceDistributionPEOInvIncrementalPercentage | INV_INCREMENTAL_PERCENTAGE | — | ✅ |
| 66 | InvoiceDistributionPEOInvLineDistNum | INV_LINE_DIST_NUM | — | ✅ |
| 67 | InvoiceDistributionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 68 | InvoiceDistributionPEOInvoiceAmountCalcCode | INVOICE_AMOUNT_CALC_CODE | — | ✅ |
| 69 | InvoiceDistributionPEOInvoiceCurrBilledAmt | INVOICE_CURR_BILLED_AMT | — | ✅ |
| 70 | InvoiceDistributionPEOInvoiceCurrCreditAmt | INVOICE_CURR_CREDIT_AMT | — | ✅ |
| 71 | InvoiceDistributionPEOInvoiceCurrCreditPct | INVOICE_CURR_CREDIT_PCT | — | — |
| 72 | InvoiceDistributionPEOInvoiceCurrDateType | INVOICE_CURR_DATE_TYPE | — | ✅ |
| 73 | InvoiceDistributionPEOInvoiceCurrExchgDate | INVOICE_CURR_EXCHG_DATE | — | ✅ |
| 74 | InvoiceDistributionPEOInvoiceCurrExchgRate | INVOICE_CURR_EXCHG_RATE | — | ✅ |
| 75 | InvoiceDistributionPEOInvoiceCurrRateType | INVOICE_CURR_RATE_TYPE | — | ✅ |
| 76 | InvoiceDistributionPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 77 | InvoiceDistributionPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 78 | InvoiceDistributionPEOInvoiceDenomRateId | INVOICE_DENOM_RATE_ID | — | — |
| 79 | InvoiceDistributionPEOInvoiceDiscountPercentage | INVOICE_DISCOUNT_PERCENTAGE | — | ✅ |
| 80 | InvoiceDistributionPEOInvoiceId | INVOICE_ID | — | ✅ |
| 81 | InvoiceDistributionPEOInvoiceLaborMultiplier | INVOICE_LABOR_MULTIPLIER | — | — |
| 82 | InvoiceDistributionPEOInvoiceLineId | INVOICE_LINE_ID | — | — |
| 83 | InvoiceDistributionPEOInvoiceMarkupPercentage | INVOICE_MARKUP_PERCENTAGE | — | ✅ |
| 84 | InvoiceDistributionPEOInvoiceRateSourceId | INVOICE_RATE_SOURCE_ID | — | — |
| 85 | InvoiceDistributionPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 86 | InvoiceDistributionPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 87 | InvoiceDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 88 | InvoiceDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 89 | InvoiceDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 90 | InvoiceDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 91 | InvoiceDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 92 | InvoiceDistributionPEOLedgerCurrBilledAmt | LEDGER_CURR_BILLED_AMT | — | ✅ |
| 93 | InvoiceDistributionPEOLedgerCurrInvDateType | LEDGER_CURR_INV_DATE_TYPE | — | ✅ |
| 94 | InvoiceDistributionPEOLedgerCurrInvExchgDate | LEDGER_CURR_INV_EXCHG_DATE | — | ✅ |
| 95 | InvoiceDistributionPEOLedgerCurrInvExchgRate | LEDGER_CURR_INV_EXCHG_RATE | — | ✅ |
| 96 | InvoiceDistributionPEOLedgerCurrInvRateType | LEDGER_CURR_INV_RATE_TYPE | — | ✅ |
| 97 | InvoiceDistributionPEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 98 | InvoiceDistributionPEOLinkedProjectId | LINKED_PROJECT_ID | — | ✅ |
| 99 | InvoiceDistributionPEOLinkedTaskId | LINKED_TASK_ID | — | ✅ |
| 100 | InvoiceDistributionPEOLocNumber | LOC_NUMBER | — | — |
| 101 | InvoiceDistributionPEOMajorVersion | MAJOR_VERSION | — | — |
| 102 | InvoiceDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 103 | InvoiceDistributionPEOOrgId | ORG_ID | — | ✅ |
| 104 | InvoiceDistributionPEOOutputTaxAmt | OUTPUT_TAX_AMT | — | — |
| 105 | InvoiceDistributionPEOOutputTaxClassCode | OUTPUT_TAX_CLASS_CODE | — | — |
| 106 | InvoiceDistributionPEOOutputTaxExemptFlag | OUTPUT_TAX_EXEMPT_FLAG | — | — |
| 107 | InvoiceDistributionPEOOutputTaxExmtCertNumber | OUTPUT_TAX_EXMT_CERT_NUMBER | — | — |
| 108 | InvoiceDistributionPEOOutputTaxExmtReasonCode | OUTPUT_TAX_EXMT_REASON_CODE | — | — |
| 109 | InvoiceDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 110 | InvoiceDistributionPEOProductCategory | PRODUCT_CATEGORY | — | — |
| 111 | InvoiceDistributionPEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 112 | InvoiceDistributionPEOProductType | PRODUCT_TYPE | — | — |
| 113 | InvoiceDistributionPEOProjCurrInvDateType | PROJ_CURR_INV_DATE_TYPE | — | ✅ |
| 114 | InvoiceDistributionPEOProjectCurrBilledAmt | PROJECT_CURR_BILLED_AMT | — | ✅ |
| 115 | InvoiceDistributionPEOProjectCurrInvExchgDate | PROJECT_CURR_INV_EXCHG_DATE | — | ✅ |
| 116 | InvoiceDistributionPEOProjectCurrInvExchgRate | PROJECT_CURR_INV_EXCHG_RATE | — | ✅ |
| 117 | InvoiceDistributionPEOProjectCurrInvRateType | PROJECT_CURR_INV_RATE_TYPE | — | ✅ |
| 118 | InvoiceDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 119 | InvoiceDistributionPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 120 | InvoiceDistributionPEORateSourceCode | RATE_SOURCE_CODE | — | ✅ |
| 121 | InvoiceDistributionPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 122 | InvoiceDistributionPEOReadyToAccrualFlag | READY_TO_ACCRUAL_FLAG | — | ✅ |
| 123 | InvoiceDistributionPEORecvrLegalEntityId | RECVR_LEGAL_ENTITY_ID | — | — |
| 124 | InvoiceDistributionPEORequestId | REQUEST_ID | — | — |
| 125 | InvoiceDistributionPEORevenueDate | REVENUE_DATE | — | ✅ |
| 126 | InvoiceDistributionPEOTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 127 | InvoiceDistributionPEOTpInvRulePercentage | TP_INV_RULE_PERCENTAGE | — | ✅ |
| 128 | InvoiceDistributionPEOTpInvSchLinePercentage | TP_INV_SCH_LINE_PERCENTAGE | — | ✅ |
| 129 | InvoiceDistributionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 130 | InvoiceDistributionPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 131 | InvoiceDistributionPEOTransactionProjectId | TRANSACTION_PROJECT_ID | — | ✅ |
| 132 | InvoiceDistributionPEOTransactionTaskId | TRANSACTION_TASK_ID | — | ✅ |
| 133 | InvoiceDistributionPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 134 | InvoiceDistributionPEOTrnsCurrBilledAmt | TRNS_CURR_BILLED_AMT | — | ✅ |
| 135 | InvoiceDistributionPEOTrnsCurrConcessionAmt | TRNS_CURR_CONCESSION_AMT | — | ✅ |
| 136 | InvoiceDistributionPEOTrnsCurrCreditAmt | TRNS_CURR_CREDIT_AMT | — | ✅ |
| 137 | InvoiceDistributionPEOTrnsCurrWriteoffAmt | TRNS_CURR_WRITEOFF_AMT | — | — |
| 138 | InvoiceDistributionPEOTrnsCurrencyCode | TRNS_CURRENCY_CODE | — | — |
| 139 | InvoiceDistributionPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 140 | InvoiceDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 141 | InvoiceDistributionPEOUomCode | UOM_CODE | — | ✅ |
| 142 | InvoiceDistributionPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | TransProjectPEOOrgId | ORG_ID | — | — |
| 3 | TransProjectPEOProjectId | PROJECT_ID | — | — |
| 4 | TransProjectPEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinkedProjectPEOName | NAME | — | — |
| 2 | LinkedProjectPEOProjectId | PROJECT_ID | — | — |
| 3 | LinkedProjectPEOSegment1 | SEGMENT1 | — | — |
| 4 | RcvrProjectPEOName | NAME | — | ✅ |
| 5 | RcvrProjectPEOProjectId | PROJECT_ID | — | — |
| 6 | RcvrProjectPEOSegment1 | SEGMENT1 | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinkTaskStructurePEOElementNumber | ELEMENT_NUMBER | — | — |
| 2 | LinkTaskStructurePEOName | NAME | — | — |
| 3 | LinkTaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 4 | RcvrTaskStructurePEOElementNumber | ELEMENT_NUMBER | — | — |
| 5 | RcvrTaskStructurePEOName | NAME | — | ✅ |
| 6 | RcvrTaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 7 | TransTaskStructurePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 8 | TransTaskStructurePEOElementNumber | ELEMENT_NUMBER | — | — |
| 9 | TransTaskStructurePEOName | NAME | — | — |
| 10 | TransTaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementPEOAlias | ALIAS | — | — |
| 2 | RBSElementPEORbsElementId | RBS_ELEMENT_ID | — | — |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementNamePEOName | NAME | — | — |
| 2 | RBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentTermPEOName | NAME | — | ✅ |
| 2 | PaymentTermPEOTermId | TERM_ID | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrvdrLePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | PrvdrLePEOName | NAME | — | ✅ |
| 3 | RcvrLePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 4 | RcvrLePEOName | NAME | — | ✅ |

### [[zx_fc_product_categories_v|ZX_FC_PRODUCT_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductCategoriesPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | ProductCategoriesPEOClassificationId | CLASSIFICATION_ID | — | — |
| 3 | ProductCategoriesPEOClassificationName | CLASSIFICATION_NAME | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
