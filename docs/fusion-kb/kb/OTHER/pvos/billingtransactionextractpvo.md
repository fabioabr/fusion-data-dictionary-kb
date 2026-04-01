---
id: DOC-OTHER-PVO-BillingTransactionExtractPVO
doc_type: system-doc
title: "BillingTransactionExtractPVO — PVO Cross-Module"
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
  - BillingTransactionExtractPVO
  - billingtransactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingTransactionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Transaction Extract. Acessa as tabelas: PJB_BILL_TRXS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.BillingTransactionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 265 | 1 | 1 | 235 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_bill_trxs|PJB_BILL_TRXS]] — 265 atributos (1 PKs, 235 BICC)

---

## ⚙️ Atributos

### [[pjb_bill_trxs|PJB_BILL_TRXS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjbBillTransactionsAmendmentFlag | AMENDMENT_FLAG | — | ✅ |
| 2 | PjbBillTransactionsApplicableFlag | APPLICABLE_FLAG | — | ✅ |
| 3 | PjbBillTransactionsAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | PjbBillTransactionsAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | PjbBillTransactionsAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | PjbBillTransactionsAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | PjbBillTransactionsAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | PjbBillTransactionsAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | PjbBillTransactionsAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | PjbBillTransactionsAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | PjbBillTransactionsAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | PjbBillTransactionsAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | PjbBillTransactionsAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | PjbBillTransactionsAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | PjbBillTransactionsAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | PjbBillTransactionsAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | PjbBillTransactionsAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | PjbBillTransactionsAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | PjbBillTransactionsAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | PjbBillTransactionsAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | PjbBillTransactionsAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | PjbBillTransactionsAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | PjbBillTransactionsAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | PjbBillTransactionsAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | PjbBillTransactionsAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | PjbBillTransactionsAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | PjbBillTransactionsAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | PjbBillTransactionsAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | PjbBillTransactionsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | PjbBillTransactionsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 31 | PjbBillTransactionsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 32 | PjbBillTransactionsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 33 | PjbBillTransactionsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 34 | PjbBillTransactionsBillEmployeeBillingTitle | BILL_EMPLOYEE_BILLING_TITLE | — | ✅ |
| 35 | PjbBillTransactionsBillFromDate | BILL_FROM_DATE | — | ✅ |
| 36 | PjbBillTransactionsBillJobBillingTitle | BILL_JOB_BILLING_TITLE | — | ✅ |
| 37 | PjbBillTransactionsBillJobId | BILL_JOB_ID | — | ✅ |
| 38 | PjbBillTransactionsBillPlanId | BILL_PLAN_ID | — | ✅ |
| 39 | PjbBillTransactionsBillRate | BILL_RATE | — | ✅ |
| 40 | PjbBillTransactionsBillToDate | BILL_TO_DATE | — | ✅ |
| 41 | PjbBillTransactionsBillTransactionTypeCode | BILL_TRANSACTION_TYPE_CODE | — | ✅ |
| 42 | PjbBillTransactionsBillTrxId | BILL_TRX_ID | 🔑 | ✅ |
| 43 | PjbBillTransactionsBillingExtensionId | BILLING_EXTENSION_ID | — | ✅ |
| 44 | PjbBillTransactionsBillingResourceId | BILLING_RESOURCE_ID | — | ✅ |
| 45 | PjbBillTransactionsBillingStatusCode | BILLING_STATUS_CODE | — | ✅ |
| 46 | PjbBillTransactionsBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 47 | PjbBillTransactionsConcessionPercentage | CONCESSION_PERCENTAGE | — | ✅ |
| 48 | PjbBillTransactionsContCurrBilledAmt | CONT_CURR_BILLED_AMT | — | ✅ |
| 49 | PjbBillTransactionsContCurrConcessionAmt | CONT_CURR_CONCESSION_AMT | — | ✅ |
| 50 | PjbBillTransactionsContCurrInvCreditAmt | CONT_CURR_INV_CREDIT_AMT | — | ✅ |
| 51 | PjbBillTransactionsContCurrInvDateType | CONT_CURR_INV_DATE_TYPE | — | ✅ |
| 52 | PjbBillTransactionsContCurrInvEligibleAmt | CONT_CURR_INV_ELIGIBLE_AMT | — | ✅ |
| 53 | PjbBillTransactionsContCurrInvExchgDate | CONT_CURR_INV_EXCHG_DATE | — | ✅ |
| 54 | PjbBillTransactionsContCurrInvExchgRate | CONT_CURR_INV_EXCHG_RATE | — | ✅ |
| 55 | PjbBillTransactionsContCurrInvOvrrideId | CONT_CURR_INV_OVRRIDE_ID | — | ✅ |
| 56 | PjbBillTransactionsContCurrInvQualifiedAmt | CONT_CURR_INV_QUALIFIED_AMT | — | ✅ |
| 57 | PjbBillTransactionsContCurrInvRateType | CONT_CURR_INV_RATE_TYPE | — | ✅ |
| 58 | PjbBillTransactionsContCurrInvTxnAmt | CONT_CURR_INV_TXN_AMT | — | ✅ |
| 59 | PjbBillTransactionsContCurrRevCreditAmt | CONT_CURR_REV_CREDIT_AMT | — | ✅ |
| 60 | PjbBillTransactionsContCurrRevEligibleAmt | CONT_CURR_REV_ELIGIBLE_AMT | — | ✅ |
| 61 | PjbBillTransactionsContCurrRevExchgDate | CONT_CURR_REV_EXCHG_DATE | — | ✅ |
| 62 | PjbBillTransactionsContCurrRevExchgRate | CONT_CURR_REV_EXCHG_RATE | — | ✅ |
| 63 | PjbBillTransactionsContCurrRevOvrrideId | CONT_CURR_REV_OVRRIDE_ID | — | ✅ |
| 64 | PjbBillTransactionsContCurrRevQualifiedAmt | CONT_CURR_REV_QUALIFIED_AMT | — | ✅ |
| 65 | PjbBillTransactionsContCurrRevRateType | CONT_CURR_REV_RATE_TYPE | — | ✅ |
| 66 | PjbBillTransactionsContCurrRevRecognzedAmt | CONT_CURR_REV_RECOGNZED_AMT | — | ✅ |
| 67 | PjbBillTransactionsContCurrRevTxnAmt | CONT_CURR_REV_TXN_AMT | — | ✅ |
| 68 | PjbBillTransactionsContCurrWriteoffAmt | CONT_CURR_WRITEOFF_AMT | — | ✅ |
| 69 | PjbBillTransactionsContractContributionPct | CONTRACT_CONTRIBUTION_PCT | — | ✅ |
| 70 | PjbBillTransactionsContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 71 | PjbBillTransactionsContractId | CONTRACT_ID | — | ✅ |
| 72 | PjbBillTransactionsContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 73 | PjbBillTransactionsContractProjectLinkageId | CONTRACT_PROJECT_LINKAGE_ID | — | ✅ |
| 74 | PjbBillTransactionsCreatedBy | CREATED_BY | — | ✅ |
| 75 | PjbBillTransactionsCreatedByProcess | CREATED_BY_PROCESS | — | ✅ |
| 76 | PjbBillTransactionsCreationDate | CREATION_DATE | — | ✅ |
| 77 | PjbBillTransactionsDerivedBillRate | DERIVED_BILL_RATE | — | ✅ |
| 78 | PjbBillTransactionsDerivedDiscountPercentage | DERIVED_DISCOUNT_PERCENTAGE | — | ✅ |
| 79 | PjbBillTransactionsDerivedLaborMultiplier | DERIVED_LABOR_MULTIPLIER | — | ✅ |
| 80 | PjbBillTransactionsDerivedMarkupPercentage | DERIVED_MARKUP_PERCENTAGE | — | ✅ |
| 81 | PjbBillTransactionsDerivedTrnsCurrTxnAmt | DERIVED_TRNS_CURR_TXN_AMT | — | ✅ |
| 82 | PjbBillTransactionsDocNumber | DOC_NUMBER | — | ✅ |
| 83 | PjbBillTransactionsEventId | EVENT_ID | — | ✅ |
| 84 | PjbBillTransactionsExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 85 | PjbBillTransactionsGroupOnWorkTypeFlag | GROUP_ON_WORK_TYPE_FLAG | — | ✅ |
| 86 | PjbBillTransactionsIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 87 | PjbBillTransactionsIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 88 | PjbBillTransactionsInvAdjEligibilityFlag | INV_ADJ_ELIGIBILITY_FLAG | — | ✅ |
| 89 | PjbBillTransactionsInvBilledQuantity | INV_BILLED_QUANTITY | — | ✅ |
| 90 | PjbBillTransactionsInvBillingControlId1 | INV_BILLING_CONTROL_ID1 | — | ✅ |
| 91 | PjbBillTransactionsInvBillingControlId10 | INV_BILLING_CONTROL_ID10 | — | ✅ |
| 92 | PjbBillTransactionsInvBillingControlId11 | INV_BILLING_CONTROL_ID11 | — | ✅ |
| 93 | PjbBillTransactionsInvBillingControlId12 | INV_BILLING_CONTROL_ID12 | — | ✅ |
| 94 | PjbBillTransactionsInvBillingControlId13 | INV_BILLING_CONTROL_ID13 | — | ✅ |
| 95 | PjbBillTransactionsInvBillingControlId14 | INV_BILLING_CONTROL_ID14 | — | ✅ |
| 96 | PjbBillTransactionsInvBillingControlId15 | INV_BILLING_CONTROL_ID15 | — | ✅ |
| 97 | PjbBillTransactionsInvBillingControlId16 | INV_BILLING_CONTROL_ID16 | — | ✅ |
| 98 | PjbBillTransactionsInvBillingControlId17 | INV_BILLING_CONTROL_ID17 | — | ✅ |
| 99 | PjbBillTransactionsInvBillingControlId18 | INV_BILLING_CONTROL_ID18 | — | ✅ |
| 100 | PjbBillTransactionsInvBillingControlId19 | INV_BILLING_CONTROL_ID19 | — | ✅ |
| 101 | PjbBillTransactionsInvBillingControlId2 | INV_BILLING_CONTROL_ID2 | — | ✅ |
| 102 | PjbBillTransactionsInvBillingControlId20 | INV_BILLING_CONTROL_ID20 | — | ✅ |
| 103 | PjbBillTransactionsInvBillingControlId3 | INV_BILLING_CONTROL_ID3 | — | ✅ |
| 104 | PjbBillTransactionsInvBillingControlId4 | INV_BILLING_CONTROL_ID4 | — | ✅ |
| 105 | PjbBillTransactionsInvBillingControlId5 | INV_BILLING_CONTROL_ID5 | — | ✅ |
| 106 | PjbBillTransactionsInvBillingControlId6 | INV_BILLING_CONTROL_ID6 | — | ✅ |
| 107 | PjbBillTransactionsInvBillingControlId7 | INV_BILLING_CONTROL_ID7 | — | ✅ |
| 108 | PjbBillTransactionsInvBillingControlId8 | INV_BILLING_CONTROL_ID8 | — | ✅ |
| 109 | PjbBillTransactionsInvBillingControlId9 | INV_BILLING_CONTROL_ID9 | — | ✅ |
| 110 | PjbBillTransactionsInvBurdenCompileSetId | INV_BURDEN_COMPILE_SET_ID | — | ✅ |
| 111 | PjbBillTransactionsInvCreditedPercent | INV_CREDITED_PERCENT | — | ✅ |
| 112 | PjbBillTransactionsInvCreditedQuantity | INV_CREDITED_QUANTITY | — | ✅ |
| 113 | PjbBillTransactionsInvCurrBilledAmt | INV_CURR_BILLED_AMT | — | ✅ |
| 114 | PjbBillTransactionsInvCurrConcessionAmt | INV_CURR_CONCESSION_AMT | — | ✅ |
| 115 | PjbBillTransactionsInvCurrConvOvrrideId | INV_CURR_CONV_OVRRIDE_ID | — | ✅ |
| 116 | PjbBillTransactionsInvCurrCreditAmt | INV_CURR_CREDIT_AMT | — | ✅ |
| 117 | PjbBillTransactionsInvCurrEligibleAmt | INV_CURR_ELIGIBLE_AMT | — | ✅ |
| 118 | PjbBillTransactionsInvCurrQualifiedAmt | INV_CURR_QUALIFIED_AMT | — | ✅ |
| 119 | PjbBillTransactionsInvCurrTxnAmt | INV_CURR_TXN_AMT | — | ✅ |
| 120 | PjbBillTransactionsInvCurrWriteoffAmt | INV_CURR_WRITEOFF_AMT | — | ✅ |
| 121 | PjbBillTransactionsInvDiscountReasonCode | INV_DISCOUNT_REASON_CODE | — | ✅ |
| 122 | PjbBillTransactionsInvFromDate | INV_FROM_DATE | — | ✅ |
| 123 | PjbBillTransactionsInvGroupAttributeDesc | INV_GROUP_ATTRIBUTE_DESC | — | ✅ |
| 124 | PjbBillTransactionsInvGroupAttributeValues | INV_GROUP_ATTRIBUTE_VALUES | — | ✅ |
| 125 | PjbBillTransactionsInvIncrementalPercentage | INV_INCREMENTAL_PERCENTAGE | — | ✅ |
| 126 | PjbBillTransactionsInvLineDescription | INV_LINE_DESCRIPTION | — | ✅ |
| 127 | PjbBillTransactionsInvQualifiedQuantity | INV_QUALIFIED_QUANTITY | — | ✅ |
| 128 | PjbBillTransactionsInvQuantity | INV_QUANTITY | — | ✅ |
| 129 | PjbBillTransactionsInvRejectionReasonCode | INV_REJECTION_REASON_CODE | — | ✅ |
| 130 | PjbBillTransactionsInvToDate | INV_TO_DATE | — | ✅ |
| 131 | PjbBillTransactionsInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 132 | PjbBillTransactionsInvoiceActiveFlag | INVOICE_ACTIVE_FLAG | — | ✅ |
| 133 | PjbBillTransactionsInvoiceAmountCalcCode | INVOICE_AMOUNT_CALC_CODE | — | ✅ |
| 134 | PjbBillTransactionsInvoiceBilledPercentage | INVOICE_BILLED_PERCENTAGE | — | ✅ |
| 135 | PjbBillTransactionsInvoiceCurrDateType | INVOICE_CURR_DATE_TYPE | — | ✅ |
| 136 | PjbBillTransactionsInvoiceCurrExchgDate | INVOICE_CURR_EXCHG_DATE | — | ✅ |
| 137 | PjbBillTransactionsInvoiceCurrExchgRate | INVOICE_CURR_EXCHG_RATE | — | ✅ |
| 138 | PjbBillTransactionsInvoiceCurrRateType | INVOICE_CURR_RATE_TYPE | — | ✅ |
| 139 | PjbBillTransactionsInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 140 | PjbBillTransactionsInvoiceDate | INVOICE_DATE | — | ✅ |
| 141 | PjbBillTransactionsInvoiceDenomRateId | INVOICE_DENOM_RATE_ID | — | ✅ |
| 142 | PjbBillTransactionsInvoiceDenormRateId | INVOICE_DENORM_RATE_ID | — | ✅ |
| 143 | PjbBillTransactionsInvoiceDiscountPercentage | INVOICE_DISCOUNT_PERCENTAGE | — | ✅ |
| 144 | PjbBillTransactionsInvoiceDistributedFlag | INVOICE_DISTRIBUTED_FLAG | — | ✅ |
| 145 | PjbBillTransactionsInvoiceLaborMultiplier | INVOICE_LABOR_MULTIPLIER | — | ✅ |
| 146 | PjbBillTransactionsInvoiceMarkupPercentage | INVOICE_MARKUP_PERCENTAGE | — | ✅ |
| 147 | PjbBillTransactionsInvoiceNetZeroAdjFlag | INVOICE_NET_ZERO_ADJ_FLAG | — | ✅ |
| 148 | PjbBillTransactionsInvoiceRateSourceId | INVOICE_RATE_SOURCE_ID | — | ✅ |
| 149 | PjbBillTransactionsInvoiceRecalcFlag | INVOICE_RECALC_FLAG | — | ✅ |
| 150 | PjbBillTransactionsInvoiceWarningMsgCode | INVOICE_WARNING_MSG_CODE | — | ✅ |
| 151 | PjbBillTransactionsItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 152 | PjbBillTransactionsJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 153 | PjbBillTransactionsJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 154 | PjbBillTransactionsLastInvLineDistNum | LAST_INV_LINE_DIST_NUM | — | ✅ |
| 155 | PjbBillTransactionsLastRevLineNum | LAST_REV_LINE_NUM | — | ✅ |
| 156 | PjbBillTransactionsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 157 | PjbBillTransactionsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 158 | PjbBillTransactionsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 159 | PjbBillTransactionsLatestInvoiceDistId | LATEST_INVOICE_DIST_ID | — | ✅ |
| 160 | PjbBillTransactionsLinkedProjectId | LINKED_PROJECT_ID | — | ✅ |
| 161 | PjbBillTransactionsLinkedTaskId | LINKED_TASK_ID | — | ✅ |
| 162 | PjbBillTransactionsLocNumber | LOC_NUMBER | — | ✅ |
| 163 | PjbBillTransactionsMajorVersion | MAJOR_VERSION | — | ✅ |
| 164 | PjbBillTransactionsManualFlag | MANUAL_FLAG | — | ✅ |
| 165 | PjbBillTransactionsMigrationFlag | MIGRATION_FLAG | — | ✅ |
| 166 | PjbBillTransactionsNetCreditFlag | NET_CREDIT_FLAG | — | ✅ |
| 167 | PjbBillTransactionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 168 | PjbBillTransactionsOrgId | ORG_ID | — | ✅ |
| 169 | PjbBillTransactionsOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 170 | PjbBillTransactionsOriginalInvoiceId | ORIGINAL_INVOICE_ID | — | ✅ |
| 171 | PjbBillTransactionsOriginalInvoiceLineId | ORIGINAL_INVOICE_LINE_ID | — | ✅ |
| 172 | PjbBillTransactionsOriginalWorkTypeId | ORIGINAL_WORK_TYPE_ID | — | ✅ |
| 173 | PjbBillTransactionsOutputTaxClassCode | OUTPUT_TAX_CLASS_CODE | — | ✅ |
| 174 | PjbBillTransactionsPreprocessStatusFlag | PREPROCESS_STATUS_FLAG | — | ✅ |
| 175 | PjbBillTransactionsPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | ✅ |
| 176 | PjbBillTransactionsRateSourceCode | RATE_SOURCE_CODE | — | ✅ |
| 177 | PjbBillTransactionsRbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 178 | PjbBillTransactionsRecvrLegalEntityId | RECVR_LEGAL_ENTITY_ID | — | ✅ |
| 179 | PjbBillTransactionsRequestId | REQUEST_ID | — | ✅ |
| 180 | PjbBillTransactionsRevAdjEligibilityFlag | REV_ADJ_ELIGIBILITY_FLAG | — | ✅ |
| 181 | PjbBillTransactionsRevBillingControlId1 | REV_BILLING_CONTROL_ID1 | — | ✅ |
| 182 | PjbBillTransactionsRevBillingControlId10 | REV_BILLING_CONTROL_ID10 | — | ✅ |
| 183 | PjbBillTransactionsRevBillingControlId11 | REV_BILLING_CONTROL_ID11 | — | ✅ |
| 184 | PjbBillTransactionsRevBillingControlId12 | REV_BILLING_CONTROL_ID12 | — | ✅ |
| 185 | PjbBillTransactionsRevBillingControlId13 | REV_BILLING_CONTROL_ID13 | — | ✅ |
| 186 | PjbBillTransactionsRevBillingControlId14 | REV_BILLING_CONTROL_ID14 | — | ✅ |
| 187 | PjbBillTransactionsRevBillingControlId15 | REV_BILLING_CONTROL_ID15 | — | ✅ |
| 188 | PjbBillTransactionsRevBillingControlId16 | REV_BILLING_CONTROL_ID16 | — | ✅ |
| 189 | PjbBillTransactionsRevBillingControlId17 | REV_BILLING_CONTROL_ID17 | — | ✅ |
| 190 | PjbBillTransactionsRevBillingControlId18 | REV_BILLING_CONTROL_ID18 | — | ✅ |
| 191 | PjbBillTransactionsRevBillingControlId19 | REV_BILLING_CONTROL_ID19 | — | ✅ |
| 192 | PjbBillTransactionsRevBillingControlId2 | REV_BILLING_CONTROL_ID2 | — | ✅ |
| 193 | PjbBillTransactionsRevBillingControlId20 | REV_BILLING_CONTROL_ID20 | — | ✅ |
| 194 | PjbBillTransactionsRevBillingControlId3 | REV_BILLING_CONTROL_ID3 | — | ✅ |
| 195 | PjbBillTransactionsRevBillingControlId4 | REV_BILLING_CONTROL_ID4 | — | ✅ |
| 196 | PjbBillTransactionsRevBillingControlId5 | REV_BILLING_CONTROL_ID5 | — | ✅ |
| 197 | PjbBillTransactionsRevBillingControlId6 | REV_BILLING_CONTROL_ID6 | — | ✅ |
| 198 | PjbBillTransactionsRevBillingControlId7 | REV_BILLING_CONTROL_ID7 | — | ✅ |
| 199 | PjbBillTransactionsRevBillingControlId8 | REV_BILLING_CONTROL_ID8 | — | ✅ |
| 200 | PjbBillTransactionsRevBillingControlId9 | REV_BILLING_CONTROL_ID9 | — | ✅ |
| 201 | PjbBillTransactionsRevBurdenCompileSetId | REV_BURDEN_COMPILE_SET_ID | — | ✅ |
| 202 | PjbBillTransactionsRevCurrConvOvrrideId | REV_CURR_CONV_OVRRIDE_ID | — | ✅ |
| 203 | PjbBillTransactionsRevCurrCreditAmt | REV_CURR_CREDIT_AMT | — | ✅ |
| 204 | PjbBillTransactionsRevCurrEligibleAmt | REV_CURR_ELIGIBLE_AMT | — | ✅ |
| 205 | PjbBillTransactionsRevCurrQualifiedAmt | REV_CURR_QUALIFIED_AMT | — | ✅ |
| 206 | PjbBillTransactionsRevCurrRecognzdAmt | REV_CURR_RECOGNZD_AMT | — | ✅ |
| 207 | PjbBillTransactionsRevCurrTxnAmt | REV_CURR_TXN_AMT | — | ✅ |
| 208 | PjbBillTransactionsRevDiscountReasonCode | REV_DISCOUNT_REASON_CODE | — | ✅ |
| 209 | PjbBillTransactionsRevFromDate | REV_FROM_DATE | — | ✅ |
| 210 | PjbBillTransactionsRevIncrementalPercentage | REV_INCREMENTAL_PERCENTAGE | — | ✅ |
| 211 | PjbBillTransactionsRevQualifiedQuantity | REV_QUALIFIED_QUANTITY | — | ✅ |
| 212 | PjbBillTransactionsRevQuantity | REV_QUANTITY | — | ✅ |
| 213 | PjbBillTransactionsRevRecognzdQuantity | REV_RECOGNZD_QUANTITY | — | ✅ |
| 214 | PjbBillTransactionsRevRejectionReasonCode | REV_REJECTION_REASON_CODE | — | ✅ |
| 215 | PjbBillTransactionsRevToDate | REV_TO_DATE | — | ✅ |
| 216 | PjbBillTransactionsRevenueActiveFlag | REVENUE_ACTIVE_FLAG | — | ✅ |
| 217 | PjbBillTransactionsRevenueAmountCalcCode | REVENUE_AMOUNT_CALC_CODE | — | ✅ |
| 218 | PjbBillTransactionsRevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 219 | PjbBillTransactionsRevenueClassificationCode | REVENUE_CLASSIFICATION_CODE | — | ✅ |
| 220 | PjbBillTransactionsRevenueDate | REVENUE_DATE | — | ✅ |
| 221 | PjbBillTransactionsRevenueDenomRateId | REVENUE_DENOM_RATE_ID | — | ✅ |
| 222 | PjbBillTransactionsRevenueDenormRateId | REVENUE_DENORM_RATE_ID | — | ✅ |
| 223 | PjbBillTransactionsRevenueDiscountPercentage | REVENUE_DISCOUNT_PERCENTAGE | — | ✅ |
| 224 | PjbBillTransactionsRevenueLaborMultiplier | REVENUE_LABOR_MULTIPLIER | — | ✅ |
| 225 | PjbBillTransactionsRevenueMarkupPercentage | REVENUE_MARKUP_PERCENTAGE | — | ✅ |
| 226 | PjbBillTransactionsRevenueNetZeroAdjFlag | REVENUE_NET_ZERO_ADJ_FLAG | — | ✅ |
| 227 | PjbBillTransactionsRevenuePlanId | REVENUE_PLAN_ID | — | ✅ |
| 228 | PjbBillTransactionsRevenueRateSourceId | REVENUE_RATE_SOURCE_ID | — | ✅ |
| 229 | PjbBillTransactionsRevenueRecalcFlag | REVENUE_RECALC_FLAG | — | ✅ |
| 230 | PjbBillTransactionsRevenueRecognzdFlag | REVENUE_RECOGNZD_FLAG | — | ✅ |
| 231 | PjbBillTransactionsRevenueRecogzdPercentage | REVENUE_RECOGZD_PERCENTAGE | — | ✅ |
| 232 | PjbBillTransactionsRevenueWarningMsgCode | REVENUE_WARNING_MSG_CODE | — | ✅ |
| 233 | PjbBillTransactionsSourceReferenceId | SOURCE_REFERENCE_ID | — | ✅ |
| 234 | PjbBillTransactionsSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 235 | PjbBillTransactionsTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 236 | PjbBillTransactionsTpInvRulePercentage | TP_INV_RULE_PERCENTAGE | — | ✅ |
| 237 | PjbBillTransactionsTpInvSchLinePercentage | TP_INV_SCH_LINE_PERCENTAGE | — | ✅ |
| 238 | PjbBillTransactionsTpRevRulePercentage | TP_REV_RULE_PERCENTAGE | — | ✅ |
| 239 | PjbBillTransactionsTpRevSchLinePercentage | TP_REV_SCH_LINE_PERCENTAGE | — | ✅ |
| 240 | PjbBillTransactionsTransactionDate | TRANSACTION_DATE | — | ✅ |
| 241 | PjbBillTransactionsTransactionId | TRANSACTION_ID | — | ✅ |
| 242 | PjbBillTransactionsTransactionProjectId | TRANSACTION_PROJECT_ID | — | ✅ |
| 243 | PjbBillTransactionsTransactionTaskId | TRANSACTION_TASK_ID | — | ✅ |
| 244 | PjbBillTransactionsTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 245 | PjbBillTransactionsTrnsCurrBilledAmt | TRNS_CURR_BILLED_AMT | — | ✅ |
| 246 | PjbBillTransactionsTrnsCurrConcessionAmt | TRNS_CURR_CONCESSION_AMT | — | ✅ |
| 247 | PjbBillTransactionsTrnsCurrInvCreditAmt | TRNS_CURR_INV_CREDIT_AMT | — | ✅ |
| 248 | PjbBillTransactionsTrnsCurrInvEligibleAmt | TRNS_CURR_INV_ELIGIBLE_AMT | — | ✅ |
| 249 | PjbBillTransactionsTrnsCurrInvQualifiedAmt | TRNS_CURR_INV_QUALIFIED_AMT | — | ✅ |
| 250 | PjbBillTransactionsTrnsCurrInvTxnAmt | TRNS_CURR_INV_TXN_AMT | — | ✅ |
| 251 | PjbBillTransactionsTrnsCurrInvUnitPrice | TRNS_CURR_INV_UNIT_PRICE | — | ✅ |
| 252 | PjbBillTransactionsTrnsCurrRevCreditAmt | TRNS_CURR_REV_CREDIT_AMT | — | ✅ |
| 253 | PjbBillTransactionsTrnsCurrRevEligibleAmt | TRNS_CURR_REV_ELIGIBLE_AMT | — | ✅ |
| 254 | PjbBillTransactionsTrnsCurrRevQualifiedAmt | TRNS_CURR_REV_QUALIFIED_AMT | — | ✅ |
| 255 | PjbBillTransactionsTrnsCurrRevRecognzedAmt | TRNS_CURR_REV_RECOGNZED_AMT | — | ✅ |
| 256 | PjbBillTransactionsTrnsCurrRevTxnAmt | TRNS_CURR_REV_TXN_AMT | — | ✅ |
| 257 | PjbBillTransactionsTrnsCurrRevUnitPrice | TRNS_CURR_REV_UNIT_PRICE | — | ✅ |
| 258 | PjbBillTransactionsTrnsCurrWipAmt | TRNS_CURR_WIP_AMT | — | ✅ |
| 259 | PjbBillTransactionsTrnsCurrWriteoffAmt | TRNS_CURR_WRITEOFF_AMT | — | ✅ |
| 260 | PjbBillTransactionsTrnsCurrencyCode | TRNS_CURRENCY_CODE | — | ✅ |
| 261 | PjbBillTransactionsTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | ✅ |
| 262 | PjbBillTransactionsUomCode | UOM_CODE | — | ✅ |
| 263 | PjbBillTransactionsUserAdjustedFlag | USER_ADJUSTED_FLAG | — | ✅ |
| 264 | PjbBillTransactionsWorkTypeId | WORK_TYPE_ID | — | ✅ |
| 265 | PjbBillTransactionsWriteoffPercentage | WRITEOFF_PERCENTAGE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
