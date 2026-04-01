---
id: DOC-OTHER-PVO-RevenueDistributionExtractPVO
doc_type: system-doc
title: "RevenueDistributionExtractPVO — PVO Cross-Module"
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
  - RevenueDistributionExtractPVO
  - revenuedistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevenueDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Revenue Distribution Extract. Acessa as tabelas: PJB_REV_DISTRIBUTIONS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.RevenueDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 1 | 1 | 127 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_rev_distributions|PJB_REV_DISTRIBUTIONS]] — 127 atributos (1 PKs, 127 BICC)

---

## ⚙️ Atributos

### [[pjb_rev_distributions|PJB_REV_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueDistributionPEOBillJobId | BILL_JOB_ID | — | ✅ |
| 2 | RevenueDistributionPEOBillRate | BILL_RATE | — | ✅ |
| 3 | RevenueDistributionPEOBillTransactionTypeCode | BILL_TRANSACTION_TYPE_CODE | — | ✅ |
| 4 | RevenueDistributionPEOBillTrxId | BILL_TRX_ID | — | ✅ |
| 5 | RevenueDistributionPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 6 | RevenueDistributionPEOContCurrRevExchgDate | CONT_CURR_REV_EXCHG_DATE | — | ✅ |
| 7 | RevenueDistributionPEOContCurrRevExchgRate | CONT_CURR_REV_EXCHG_RATE | — | ✅ |
| 8 | RevenueDistributionPEOContCurrRevRateType | CONT_CURR_REV_RATE_TYPE | — | ✅ |
| 9 | RevenueDistributionPEOContCurrRevenueAmt | CONT_CURR_REVENUE_AMT | — | ✅ |
| 10 | RevenueDistributionPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 11 | RevenueDistributionPEOContractId | CONTRACT_ID | — | ✅ |
| 12 | RevenueDistributionPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 13 | RevenueDistributionPEOContractProjectLinkageId | CONTRACT_PROJECT_LINKAGE_ID | — | ✅ |
| 14 | RevenueDistributionPEOContractRateDateType | CONTRACT_RATE_DATE_TYPE | — | ✅ |
| 15 | RevenueDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | RevenueDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | RevenueDistributionPEODenomBurdenCost | DENOM_BURDEN_COST | — | ✅ |
| 18 | RevenueDistributionPEODenomRawCost | DENOM_RAW_COST | — | ✅ |
| 19 | RevenueDistributionPEODocNumber | DOC_NUMBER | — | ✅ |
| 20 | RevenueDistributionPEOEventNum | EVENT_NUM | — | ✅ |
| 21 | RevenueDistributionPEOExportProcessId | EXPORT_PROCESS_ID | — | ✅ |
| 22 | RevenueDistributionPEOGlDate | GL_DATE | — | ✅ |
| 23 | RevenueDistributionPEOGlPeriodName | GL_PERIOD_NAME | — | ✅ |
| 24 | RevenueDistributionPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 25 | RevenueDistributionPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 26 | RevenueDistributionPEOInvLaborRateTypeCode | INV_LABOR_RATE_TYPE_CODE | — | ✅ |
| 27 | RevenueDistributionPEOInvNlRateTypeCode | INV_NL_RATE_TYPE_CODE | — | ✅ |
| 28 | RevenueDistributionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 29 | RevenueDistributionPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 30 | RevenueDistributionPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 31 | RevenueDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 32 | RevenueDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 33 | RevenueDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | RevenueDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | RevenueDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | RevenueDistributionPEOLedgerCurrRevExchgDate | LEDGER_CURR_REV_EXCHG_DATE | — | ✅ |
| 37 | RevenueDistributionPEOLedgerCurrRevExchgRate | LEDGER_CURR_REV_EXCHG_RATE | — | ✅ |
| 38 | RevenueDistributionPEOLedgerCurrRevRateType | LEDGER_CURR_REV_RATE_TYPE | — | ✅ |
| 39 | RevenueDistributionPEOLedgerCurrRevenueAmt | LEDGER_CURR_REVENUE_AMT | — | ✅ |
| 40 | RevenueDistributionPEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 41 | RevenueDistributionPEOLedgerId | LEDGER_ID | — | ✅ |
| 42 | RevenueDistributionPEOLedgerRateDateType | LEDGER_RATE_DATE_TYPE | — | ✅ |
| 43 | RevenueDistributionPEOLineNum | LINE_NUM | — | ✅ |
| 44 | RevenueDistributionPEOLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 45 | RevenueDistributionPEOLinkedProjectId | LINKED_PROJECT_ID | — | ✅ |
| 46 | RevenueDistributionPEOLinkedTaskId | LINKED_TASK_ID | — | ✅ |
| 47 | RevenueDistributionPEOLocNumber | LOC_NUMBER | — | ✅ |
| 48 | RevenueDistributionPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 49 | RevenueDistributionPEONonLaborOrgId | NON_LABOR_ORG_ID | — | ✅ |
| 50 | RevenueDistributionPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 51 | RevenueDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | RevenueDistributionPEOOrgId | ORG_ID | — | ✅ |
| 53 | RevenueDistributionPEOPaDate | PA_DATE | — | ✅ |
| 54 | RevenueDistributionPEOPaPeriodName | PA_PERIOD_NAME | — | ✅ |
| 55 | RevenueDistributionPEOPersonId | PERSON_ID | — | ✅ |
| 56 | RevenueDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | ✅ |
| 57 | RevenueDistributionPEOProjectCurrExchgRate | PROJECT_CURR_EXCHG_RATE | — | ✅ |
| 58 | RevenueDistributionPEOProjectCurrRateType | PROJECT_CURR_RATE_TYPE | — | ✅ |
| 59 | RevenueDistributionPEOProjectCurrRevenueAmt | PROJECT_CURR_REVENUE_AMT | — | ✅ |
| 60 | RevenueDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 61 | RevenueDistributionPEOProjectCurrencyExchgDate | PROJECT_CURRENCY_EXCHG_DATE | — | ✅ |
| 62 | RevenueDistributionPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 63 | RevenueDistributionPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | ✅ |
| 64 | RevenueDistributionPEOQuantity | QUANTITY | — | ✅ |
| 65 | RevenueDistributionPEORbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 66 | RevenueDistributionPEORecvrLegalEntityId | RECVR_LEGAL_ENTITY_ID | — | ✅ |
| 67 | RevenueDistributionPEORequestId | REQUEST_ID | — | ✅ |
| 68 | RevenueDistributionPEORevBillingControlId1 | REV_BILLING_CONTROL_ID1 | — | ✅ |
| 69 | RevenueDistributionPEORevBillingControlId10 | REV_BILLING_CONTROL_ID10 | — | ✅ |
| 70 | RevenueDistributionPEORevBillingControlId11 | REV_BILLING_CONTROL_ID11 | — | ✅ |
| 71 | RevenueDistributionPEORevBillingControlId12 | REV_BILLING_CONTROL_ID12 | — | ✅ |
| 72 | RevenueDistributionPEORevBillingControlId13 | REV_BILLING_CONTROL_ID13 | — | ✅ |
| 73 | RevenueDistributionPEORevBillingControlId14 | REV_BILLING_CONTROL_ID14 | — | ✅ |
| 74 | RevenueDistributionPEORevBillingControlId15 | REV_BILLING_CONTROL_ID15 | — | ✅ |
| 75 | RevenueDistributionPEORevBillingControlId16 | REV_BILLING_CONTROL_ID16 | — | ✅ |
| 76 | RevenueDistributionPEORevBillingControlId17 | REV_BILLING_CONTROL_ID17 | — | ✅ |
| 77 | RevenueDistributionPEORevBillingControlId18 | REV_BILLING_CONTROL_ID18 | — | ✅ |
| 78 | RevenueDistributionPEORevBillingControlId19 | REV_BILLING_CONTROL_ID19 | — | ✅ |
| 79 | RevenueDistributionPEORevBillingControlId2 | REV_BILLING_CONTROL_ID2 | — | ✅ |
| 80 | RevenueDistributionPEORevBillingControlId20 | REV_BILLING_CONTROL_ID20 | — | ✅ |
| 81 | RevenueDistributionPEORevBillingControlId3 | REV_BILLING_CONTROL_ID3 | — | ✅ |
| 82 | RevenueDistributionPEORevBillingControlId4 | REV_BILLING_CONTROL_ID4 | — | ✅ |
| 83 | RevenueDistributionPEORevBillingControlId5 | REV_BILLING_CONTROL_ID5 | — | ✅ |
| 84 | RevenueDistributionPEORevBillingControlId6 | REV_BILLING_CONTROL_ID6 | — | ✅ |
| 85 | RevenueDistributionPEORevBillingControlId7 | REV_BILLING_CONTROL_ID7 | — | ✅ |
| 86 | RevenueDistributionPEORevBillingControlId8 | REV_BILLING_CONTROL_ID8 | — | ✅ |
| 87 | RevenueDistributionPEORevBillingControlId9 | REV_BILLING_CONTROL_ID9 | — | ✅ |
| 88 | RevenueDistributionPEORevBurdenCompileSetId | REV_BURDEN_COMPILE_SET_ID | — | ✅ |
| 89 | RevenueDistributionPEORevDiscountReasonCode | REV_DISCOUNT_REASON_CODE | — | ✅ |
| 90 | RevenueDistributionPEORevDistributionId | REV_DISTRIBUTION_ID | 🔑 | ✅ |
| 91 | RevenueDistributionPEORevIncrementalPercentage | REV_INCREMENTAL_PERCENTAGE | — | ✅ |
| 92 | RevenueDistributionPEORevLaborRateTypeCode | REV_LABOR_RATE_TYPE_CODE | — | ✅ |
| 93 | RevenueDistributionPEORevNlRateTypeCode | REV_NL_RATE_TYPE_CODE | — | ✅ |
| 94 | RevenueDistributionPEORevRateSourceTypeCode | REV_RATE_SOURCE_TYPE_CODE | — | ✅ |
| 95 | RevenueDistributionPEORevRecognzdQuantity | REV_RECOGNZD_QUANTITY | — | ✅ |
| 96 | RevenueDistributionPEORevenueAmountCalcCode | REVENUE_AMOUNT_CALC_CODE | — | ✅ |
| 97 | RevenueDistributionPEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | ✅ |
| 98 | RevenueDistributionPEORevenueCurrAmt | REVENUE_CURR_AMT | — | ✅ |
| 99 | RevenueDistributionPEORevenueCurrDateType | REVENUE_CURR_DATE_TYPE | — | ✅ |
| 100 | RevenueDistributionPEORevenueCurrExchgDate | REVENUE_CURR_EXCHG_DATE | — | ✅ |
| 101 | RevenueDistributionPEORevenueCurrExchgRate | REVENUE_CURR_EXCHG_RATE | — | ✅ |
| 102 | RevenueDistributionPEORevenueCurrRateType | REVENUE_CURR_RATE_TYPE | — | ✅ |
| 103 | RevenueDistributionPEORevenueCurrencyCode | REVENUE_CURRENCY_CODE | — | ✅ |
| 104 | RevenueDistributionPEORevenueDenomRateId | REVENUE_DENOM_RATE_ID | — | ✅ |
| 105 | RevenueDistributionPEORevenueDiscountPercentage | REVENUE_DISCOUNT_PERCENTAGE | — | ✅ |
| 106 | RevenueDistributionPEORevenueLaborMultiplier | REVENUE_LABOR_MULTIPLIER | — | ✅ |
| 107 | RevenueDistributionPEORevenueMarkupPercentage | REVENUE_MARKUP_PERCENTAGE | — | ✅ |
| 108 | RevenueDistributionPEORevenuePlanId | REVENUE_PLAN_ID | — | ✅ |
| 109 | RevenueDistributionPEORevenueRateSourceId | REVENUE_RATE_SOURCE_ID | — | ✅ |
| 110 | RevenueDistributionPEORevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 111 | RevenueDistributionPEOReversedFlag | REVERSED_FLAG | — | ✅ |
| 112 | RevenueDistributionPEOReversedRevDistributionId | REVERSED_REV_DISTRIBUTION_ID | — | ✅ |
| 113 | RevenueDistributionPEOSlaEventId | SLA_EVENT_ID | — | ✅ |
| 114 | RevenueDistributionPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 115 | RevenueDistributionPEOTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 116 | RevenueDistributionPEOTpRevRulePercentage | TP_REV_RULE_PERCENTAGE | — | ✅ |
| 117 | RevenueDistributionPEOTpRevSchLinePercentage | TP_REV_SCH_LINE_PERCENTAGE | — | ✅ |
| 118 | RevenueDistributionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 119 | RevenueDistributionPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 120 | RevenueDistributionPEOTransactionProjectId | TRANSACTION_PROJECT_ID | — | ✅ |
| 121 | RevenueDistributionPEOTransactionTaskId | TRANSACTION_TASK_ID | — | ✅ |
| 122 | RevenueDistributionPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 123 | RevenueDistributionPEOTrnsCurrRevenueAmt | TRNS_CURR_REVENUE_AMT | — | ✅ |
| 124 | RevenueDistributionPEOTrnsCurrUnitPrice | TRNS_CURR_UNIT_PRICE | — | ✅ |
| 125 | RevenueDistributionPEOTrnsCurrencyCode | TRNS_CURRENCY_CODE | — | ✅ |
| 126 | RevenueDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | ✅ |
| 127 | RevenueDistributionPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
