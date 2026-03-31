---
id: DOC-OTHER-PVO-InvoiceDistributionExtractPVO
doc_type: system-doc
title: "InvoiceDistributionExtractPVO — PVO Cross-Module"
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
  - InvoiceDistributionExtractPVO
  - invoicedistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Distribution Extract. Acessa as tabelas: PJB_INV_LINE_DISTS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.InvoiceDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 1 | 1 | 146 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_inv_line_dists|PJB_INV_LINE_DISTS]] — 146 atributos (1 PKs, 146 BICC)

---

## ⚙️ Atributos

### [[pjb_inv_line_dists|PJB_INV_LINE_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceDistributionPEOAccruedFlag | ACCRUED_FLAG | — | ✅ |
| 2 | InvoiceDistributionPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 3 | InvoiceDistributionPEOBillEmployeeBillingTitle | BILL_EMPLOYEE_BILLING_TITLE | — | ✅ |
| 4 | InvoiceDistributionPEOBillFromDate | BILL_FROM_DATE | — | ✅ |
| 5 | InvoiceDistributionPEOBillJobBillingTitle | BILL_JOB_BILLING_TITLE | — | ✅ |
| 6 | InvoiceDistributionPEOBillJobId | BILL_JOB_ID | — | ✅ |
| 7 | InvoiceDistributionPEOBillPlanId | BILL_PLAN_ID | — | ✅ |
| 8 | InvoiceDistributionPEOBillRate | BILL_RATE | — | ✅ |
| 9 | InvoiceDistributionPEOBillSetNum | BILL_SET_NUM | — | ✅ |
| 10 | InvoiceDistributionPEOBillToDate | BILL_TO_DATE | — | ✅ |
| 11 | InvoiceDistributionPEOBillTransactionTypeCode | BILL_TRANSACTION_TYPE_CODE | — | ✅ |
| 12 | InvoiceDistributionPEOBillTrxId | BILL_TRX_ID | — | ✅ |
| 13 | InvoiceDistributionPEOBillingExtensionId | BILLING_EXTENSION_ID | — | ✅ |
| 14 | InvoiceDistributionPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 15 | InvoiceDistributionPEOCanceledFlag | CANCELED_FLAG | — | ✅ |
| 16 | InvoiceDistributionPEOContCurrBilledAmt | CONT_CURR_BILLED_AMT | — | ✅ |
| 17 | InvoiceDistributionPEOContCurrConcessionAmt | CONT_CURR_CONCESSION_AMT | — | ✅ |
| 18 | InvoiceDistributionPEOContCurrCreditAmt | CONT_CURR_CREDIT_AMT | — | ✅ |
| 19 | InvoiceDistributionPEOContCurrInvDateType | CONT_CURR_INV_DATE_TYPE | — | ✅ |
| 20 | InvoiceDistributionPEOContCurrInvExchgDate | CONT_CURR_INV_EXCHG_DATE | — | ✅ |
| 21 | InvoiceDistributionPEOContCurrInvExchgRate | CONT_CURR_INV_EXCHG_RATE | — | ✅ |
| 22 | InvoiceDistributionPEOContCurrInvRateType | CONT_CURR_INV_RATE_TYPE | — | ✅ |
| 23 | InvoiceDistributionPEOContCurrWriteoffAmt | CONT_CURR_WRITEOFF_AMT | — | ✅ |
| 24 | InvoiceDistributionPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 25 | InvoiceDistributionPEOContractId | CONTRACT_ID | — | ✅ |
| 26 | InvoiceDistributionPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 27 | InvoiceDistributionPEOContractProjectLinkageId | CONTRACT_PROJECT_LINKAGE_ID | — | ✅ |
| 28 | InvoiceDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 29 | InvoiceDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 30 | InvoiceDistributionPEOCreditedDistId | CREDITED_DIST_ID | — | ✅ |
| 31 | InvoiceDistributionPEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | ✅ |
| 32 | InvoiceDistributionPEOCreditedInvoiceLineId | CREDITED_INVOICE_LINE_ID | — | ✅ |
| 33 | InvoiceDistributionPEODocNumber | DOC_NUMBER | — | ✅ |
| 34 | InvoiceDistributionPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 35 | InvoiceDistributionPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 36 | InvoiceDistributionPEOIntendedUse | INTENDED_USE | — | ✅ |
| 37 | InvoiceDistributionPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 38 | InvoiceDistributionPEOInvBilledQuantity | INV_BILLED_QUANTITY | — | ✅ |
| 39 | InvoiceDistributionPEOInvBillingControlId1 | INV_BILLING_CONTROL_ID1 | — | ✅ |
| 40 | InvoiceDistributionPEOInvBillingControlId10 | INV_BILLING_CONTROL_ID10 | — | ✅ |
| 41 | InvoiceDistributionPEOInvBillingControlId11 | INV_BILLING_CONTROL_ID11 | — | ✅ |
| 42 | InvoiceDistributionPEOInvBillingControlId12 | INV_BILLING_CONTROL_ID12 | — | ✅ |
| 43 | InvoiceDistributionPEOInvBillingControlId13 | INV_BILLING_CONTROL_ID13 | — | ✅ |
| 44 | InvoiceDistributionPEOInvBillingControlId14 | INV_BILLING_CONTROL_ID14 | — | ✅ |
| 45 | InvoiceDistributionPEOInvBillingControlId15 | INV_BILLING_CONTROL_ID15 | — | ✅ |
| 46 | InvoiceDistributionPEOInvBillingControlId16 | INV_BILLING_CONTROL_ID16 | — | ✅ |
| 47 | InvoiceDistributionPEOInvBillingControlId17 | INV_BILLING_CONTROL_ID17 | — | ✅ |
| 48 | InvoiceDistributionPEOInvBillingControlId18 | INV_BILLING_CONTROL_ID18 | — | ✅ |
| 49 | InvoiceDistributionPEOInvBillingControlId19 | INV_BILLING_CONTROL_ID19 | — | ✅ |
| 50 | InvoiceDistributionPEOInvBillingControlId2 | INV_BILLING_CONTROL_ID2 | — | ✅ |
| 51 | InvoiceDistributionPEOInvBillingControlId20 | INV_BILLING_CONTROL_ID20 | — | ✅ |
| 52 | InvoiceDistributionPEOInvBillingControlId3 | INV_BILLING_CONTROL_ID3 | — | ✅ |
| 53 | InvoiceDistributionPEOInvBillingControlId4 | INV_BILLING_CONTROL_ID4 | — | ✅ |
| 54 | InvoiceDistributionPEOInvBillingControlId5 | INV_BILLING_CONTROL_ID5 | — | ✅ |
| 55 | InvoiceDistributionPEOInvBillingControlId6 | INV_BILLING_CONTROL_ID6 | — | ✅ |
| 56 | InvoiceDistributionPEOInvBillingControlId7 | INV_BILLING_CONTROL_ID7 | — | ✅ |
| 57 | InvoiceDistributionPEOInvBillingControlId8 | INV_BILLING_CONTROL_ID8 | — | ✅ |
| 58 | InvoiceDistributionPEOInvBillingControlId9 | INV_BILLING_CONTROL_ID9 | — | ✅ |
| 59 | InvoiceDistributionPEOInvBurdenCompileSetId | INV_BURDEN_COMPILE_SET_ID | — | ✅ |
| 60 | InvoiceDistributionPEOInvCurrConcessionAmt | INV_CURR_CONCESSION_AMT | — | ✅ |
| 61 | InvoiceDistributionPEOInvCurrUnitPrice | INV_CURR_UNIT_PRICE | — | ✅ |
| 62 | InvoiceDistributionPEOInvCurrWriteoffAmt | INV_CURR_WRITEOFF_AMT | — | ✅ |
| 63 | InvoiceDistributionPEOInvDiscountReasonCode | INV_DISCOUNT_REASON_CODE | — | ✅ |
| 64 | InvoiceDistributionPEOInvDistributionTypeCode | INV_DISTRIBUTION_TYPE_CODE | — | ✅ |
| 65 | InvoiceDistributionPEOInvIncrementalPercentage | INV_INCREMENTAL_PERCENTAGE | — | ✅ |
| 66 | InvoiceDistributionPEOInvLineDistNum | INV_LINE_DIST_NUM | — | ✅ |
| 67 | InvoiceDistributionPEOInvRejectionReasonCode | INV_REJECTION_REASON_CODE | — | ✅ |
| 68 | InvoiceDistributionPEOInvWarningMsgCode | INV_WARNING_MSG_CODE | — | ✅ |
| 69 | InvoiceDistributionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 70 | InvoiceDistributionPEOInvoiceAmountCalcCode | INVOICE_AMOUNT_CALC_CODE | — | ✅ |
| 71 | InvoiceDistributionPEOInvoiceCurrBilledAmt | INVOICE_CURR_BILLED_AMT | — | ✅ |
| 72 | InvoiceDistributionPEOInvoiceCurrCreditAmt | INVOICE_CURR_CREDIT_AMT | — | ✅ |
| 73 | InvoiceDistributionPEOInvoiceCurrCreditPct | INVOICE_CURR_CREDIT_PCT | — | ✅ |
| 74 | InvoiceDistributionPEOInvoiceCurrDateType | INVOICE_CURR_DATE_TYPE | — | ✅ |
| 75 | InvoiceDistributionPEOInvoiceCurrExchgDate | INVOICE_CURR_EXCHG_DATE | — | ✅ |
| 76 | InvoiceDistributionPEOInvoiceCurrExchgRate | INVOICE_CURR_EXCHG_RATE | — | ✅ |
| 77 | InvoiceDistributionPEOInvoiceCurrRateType | INVOICE_CURR_RATE_TYPE | — | ✅ |
| 78 | InvoiceDistributionPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 79 | InvoiceDistributionPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 80 | InvoiceDistributionPEOInvoiceDenomRateId | INVOICE_DENOM_RATE_ID | — | ✅ |
| 81 | InvoiceDistributionPEOInvoiceDiscountPercentage | INVOICE_DISCOUNT_PERCENTAGE | — | ✅ |
| 82 | InvoiceDistributionPEOInvoiceDistId | INVOICE_DIST_ID | 🔑 | ✅ |
| 83 | InvoiceDistributionPEOInvoiceId | INVOICE_ID | — | ✅ |
| 84 | InvoiceDistributionPEOInvoiceLaborMultiplier | INVOICE_LABOR_MULTIPLIER | — | ✅ |
| 85 | InvoiceDistributionPEOInvoiceLineId | INVOICE_LINE_ID | — | ✅ |
| 86 | InvoiceDistributionPEOInvoiceMarkupPercentage | INVOICE_MARKUP_PERCENTAGE | — | ✅ |
| 87 | InvoiceDistributionPEOInvoiceRateSourceId | INVOICE_RATE_SOURCE_ID | — | ✅ |
| 88 | InvoiceDistributionPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 89 | InvoiceDistributionPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 90 | InvoiceDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 91 | InvoiceDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 92 | InvoiceDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 93 | InvoiceDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 94 | InvoiceDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 95 | InvoiceDistributionPEOLedgerCurrBilledAmt | LEDGER_CURR_BILLED_AMT | — | ✅ |
| 96 | InvoiceDistributionPEOLedgerCurrInvDateType | LEDGER_CURR_INV_DATE_TYPE | — | ✅ |
| 97 | InvoiceDistributionPEOLedgerCurrInvExchgDate | LEDGER_CURR_INV_EXCHG_DATE | — | ✅ |
| 98 | InvoiceDistributionPEOLedgerCurrInvExchgRate | LEDGER_CURR_INV_EXCHG_RATE | — | ✅ |
| 99 | InvoiceDistributionPEOLedgerCurrInvRateType | LEDGER_CURR_INV_RATE_TYPE | — | ✅ |
| 100 | InvoiceDistributionPEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 101 | InvoiceDistributionPEOLinkedProjectId | LINKED_PROJECT_ID | — | ✅ |
| 102 | InvoiceDistributionPEOLinkedTaskId | LINKED_TASK_ID | — | ✅ |
| 103 | InvoiceDistributionPEOLocNumber | LOC_NUMBER | — | ✅ |
| 104 | InvoiceDistributionPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 105 | InvoiceDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 106 | InvoiceDistributionPEOOrgId | ORG_ID | — | ✅ |
| 107 | InvoiceDistributionPEOOutputTaxAmt | OUTPUT_TAX_AMT | — | ✅ |
| 108 | InvoiceDistributionPEOOutputTaxClassCode | OUTPUT_TAX_CLASS_CODE | — | ✅ |
| 109 | InvoiceDistributionPEOOutputTaxExemptFlag | OUTPUT_TAX_EXEMPT_FLAG | — | ✅ |
| 110 | InvoiceDistributionPEOOutputTaxExmtCertNumber | OUTPUT_TAX_EXMT_CERT_NUMBER | — | ✅ |
| 111 | InvoiceDistributionPEOOutputTaxExmtReasonCode | OUTPUT_TAX_EXMT_REASON_CODE | — | ✅ |
| 112 | InvoiceDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | ✅ |
| 113 | InvoiceDistributionPEOProdFcCategId | PROD_FC_CATEG_ID | — | ✅ |
| 114 | InvoiceDistributionPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 115 | InvoiceDistributionPEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 116 | InvoiceDistributionPEOProductType | PRODUCT_TYPE | — | ✅ |
| 117 | InvoiceDistributionPEOProjCurrInvDateType | PROJ_CURR_INV_DATE_TYPE | — | ✅ |
| 118 | InvoiceDistributionPEOProjectCurrBilledAmt | PROJECT_CURR_BILLED_AMT | — | ✅ |
| 119 | InvoiceDistributionPEOProjectCurrInvExchgDate | PROJECT_CURR_INV_EXCHG_DATE | — | ✅ |
| 120 | InvoiceDistributionPEOProjectCurrInvExchgRate | PROJECT_CURR_INV_EXCHG_RATE | — | ✅ |
| 121 | InvoiceDistributionPEOProjectCurrInvRateType | PROJECT_CURR_INV_RATE_TYPE | — | ✅ |
| 122 | InvoiceDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 123 | InvoiceDistributionPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | ✅ |
| 124 | InvoiceDistributionPEORateSourceCode | RATE_SOURCE_CODE | — | ✅ |
| 125 | InvoiceDistributionPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 126 | InvoiceDistributionPEOReadyToAccrualFlag | READY_TO_ACCRUAL_FLAG | — | ✅ |
| 127 | InvoiceDistributionPEORecvrLegalEntityId | RECVR_LEGAL_ENTITY_ID | — | ✅ |
| 128 | InvoiceDistributionPEORequestId | REQUEST_ID | — | ✅ |
| 129 | InvoiceDistributionPEORevenueDate | REVENUE_DATE | — | ✅ |
| 130 | InvoiceDistributionPEOTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 131 | InvoiceDistributionPEOTpInvRulePercentage | TP_INV_RULE_PERCENTAGE | — | ✅ |
| 132 | InvoiceDistributionPEOTpInvSchLinePercentage | TP_INV_SCH_LINE_PERCENTAGE | — | ✅ |
| 133 | InvoiceDistributionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 134 | InvoiceDistributionPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 135 | InvoiceDistributionPEOTransactionProjectId | TRANSACTION_PROJECT_ID | — | ✅ |
| 136 | InvoiceDistributionPEOTransactionTaskId | TRANSACTION_TASK_ID | — | ✅ |
| 137 | InvoiceDistributionPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 138 | InvoiceDistributionPEOTrnsCurrBilledAmt | TRNS_CURR_BILLED_AMT | — | ✅ |
| 139 | InvoiceDistributionPEOTrnsCurrConcessionAmt | TRNS_CURR_CONCESSION_AMT | — | ✅ |
| 140 | InvoiceDistributionPEOTrnsCurrCreditAmt | TRNS_CURR_CREDIT_AMT | — | ✅ |
| 141 | InvoiceDistributionPEOTrnsCurrWriteoffAmt | TRNS_CURR_WRITEOFF_AMT | — | ✅ |
| 142 | InvoiceDistributionPEOTrnsCurrencyCode | TRNS_CURRENCY_CODE | — | ✅ |
| 143 | InvoiceDistributionPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 144 | InvoiceDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | ✅ |
| 145 | InvoiceDistributionPEOUomCode | UOM_CODE | — | ✅ |
| 146 | InvoiceDistributionPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
