---
id: DOC-AR-PVO-RevenueDistributionPVO
doc_type: system-doc
title: "RevenueDistributionPVO — PVO Accounts Receivable"
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
  - RevenueDistributionPVO
  - revenuedistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RevenueDistributionPVO

## 📌 Visão Geral

Extrai as distribuições de receita vinculadas a projetos, contratos e itens de faturamento, com regras de reconhecimento e períodos. Essencial para reconhecimento de receita em cenários complexos (projetos, contratos de longo prazo, serviços recorrentes).

**Caminho:** `FscmTopModelAM.RevenueDistributionAM.RevenueDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 200 | 23 | 1 | 84 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_categories|EGP_ITEM_CATEGORIES]] — 4 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos (1 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 4 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 6 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 4 atributos (1 BICC)
- [[okc_k_headers_vl|OKC_K_HEADERS_VL]] — 6 atributos
- [[okc_k_lines_vl|OKC_K_LINES_VL]] — 6 atributos
- [[pjb_billing_events|PJB_BILLING_EVENTS]] — 2 atributos
- [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]] — 3 atributos (1 BICC)
- [[pjb_rev_distributions|PJB_REV_DISTRIBUTIONS]] — 126 atributos (1 PKs, 77 BICC)
- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 5 atributos
- [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]] — 2 atributos
- [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]] — 3 atributos
- [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]] — 2 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 4 atributos
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 4 atributos
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 2 atributos
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 4 atributos
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 2 atributos
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 2 atributos (1 BICC)
- [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]] — 2 atributos (1 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[egp_item_categories|EGP_ITEM_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ItemCategoryPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ItemCategoryPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | ItemCategoryPEOOrganizationId | ORGANIZATION_ID | — | — |

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

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOName | BU_NAME | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContCurrRevRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 2 | ContCurrRevRateTypePEODescription | DESCRIPTION | — | — |
| 3 | LedgerCurrRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 4 | LedgerCurrRateTypePEODescription | DESCRIPTION | — | — |
| 5 | ProjCurrRateTypePEOConversionType | CONVERSION_TYPE | — | — |
| 6 | ProjCurrRateTypePEODescription | DESCRIPTION | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | NonLaborOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | NonLaborOrganizationDPEOName | NAME | — | ✅ |
| 4 | NonLaborOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[okc_k_headers_vl|OKC_K_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderPEOContractNumber | CONTRACT_NUMBER | — | — |
| 2 | ContractHeaderPEODescription | DESCRIPTION | — | — |
| 3 | ContractHeaderPEOId | ID | — | — |
| 4 | ContractHeaderPEOMajorVersion | MAJOR_VERSION | — | — |
| 5 | ContractHeaderPEOOwningOrgId | OWNING_ORG_ID | — | — |
| 6 | LegalEntityId | LEGAL_ENTITY_ID | — | — |

### [[okc_k_lines_vl|OKC_K_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLinePEOBillPlanId | BILL_PLAN_ID | — | — |
| 2 | ContractLinePEOId | ID | — | — |
| 3 | ContractLinePEOLineName | LINE_NAME | — | — |
| 4 | ContractLinePEOLineNumber | LINE_NUMBER | — | — |
| 5 | ContractLinePEOMajorVersion | MAJOR_VERSION | — | — |
| 6 | ContractLinePEOStsCode | STS_CODE | — | — |

### [[pjb_billing_events|PJB_BILLING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingEventsPEOEventId1 | EVENT_ID | — | — |
| 2 | BillingEventsPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenuePlanBillPlanPEOBillPlanId | BILL_PLAN_ID | — | — |
| 2 | RevenuePlanBillPlanPEOBillPlanName | BILL_PLAN_NAME | — | ✅ |
| 3 | RevenuePlanBillPlanPEOMajorVersion | MAJOR_VERSION | — | — |

### [[pjb_rev_distributions|PJB_REV_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevDistributionId | REV_DISTRIBUTION_ID | 🔑 | ✅ |
| 2 | RevenueDistributionPEOBillJobId | BILL_JOB_ID | — | — |
| 3 | RevenueDistributionPEOBillRate | BILL_RATE | — | ✅ |
| 4 | RevenueDistributionPEOBillTransactionTypeCode | BILL_TRANSACTION_TYPE_CODE | — | ✅ |
| 5 | RevenueDistributionPEOBillTrxId | BILL_TRX_ID | — | — |
| 6 | RevenueDistributionPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 7 | RevenueDistributionPEOContCurrRevExchgDate | CONT_CURR_REV_EXCHG_DATE | — | ✅ |
| 8 | RevenueDistributionPEOContCurrRevExchgRate | CONT_CURR_REV_EXCHG_RATE | — | ✅ |
| 9 | RevenueDistributionPEOContCurrRevRateType | CONT_CURR_REV_RATE_TYPE | — | ✅ |
| 10 | RevenueDistributionPEOContCurrRevenueAmt | CONT_CURR_REVENUE_AMT | — | ✅ |
| 11 | RevenueDistributionPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 12 | RevenueDistributionPEOContractId | CONTRACT_ID | — | ✅ |
| 13 | RevenueDistributionPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 14 | RevenueDistributionPEOContractProjectLinkageId | CONTRACT_PROJECT_LINKAGE_ID | — | — |
| 15 | RevenueDistributionPEOContractRateDateType | CONTRACT_RATE_DATE_TYPE | — | ✅ |
| 16 | RevenueDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 17 | RevenueDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | RevenueDistributionPEODenomBurdenCost | DENOM_BURDEN_COST | — | — |
| 19 | RevenueDistributionPEODenomRawCost | DENOM_RAW_COST | — | — |
| 20 | RevenueDistributionPEODocNumber | DOC_NUMBER | — | — |
| 21 | RevenueDistributionPEOEventNum | EVENT_NUM | — | ✅ |
| 22 | RevenueDistributionPEOExportProcessId | EXPORT_PROCESS_ID | — | ✅ |
| 23 | RevenueDistributionPEOGlDate | GL_DATE | — | ✅ |
| 24 | RevenueDistributionPEOGlPeriodName | GL_PERIOD_NAME | — | — |
| 25 | RevenueDistributionPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 26 | RevenueDistributionPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 27 | RevenueDistributionPEOInvLaborRateTypeCode | INV_LABOR_RATE_TYPE_CODE | — | ✅ |
| 28 | RevenueDistributionPEOInvNlRateTypeCode | INV_NL_RATE_TYPE_CODE | — | ✅ |
| 29 | RevenueDistributionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 30 | RevenueDistributionPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 31 | RevenueDistributionPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 32 | RevenueDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 33 | RevenueDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 34 | RevenueDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | RevenueDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | RevenueDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | RevenueDistributionPEOLedgerCurrRevExchgDate | LEDGER_CURR_REV_EXCHG_DATE | — | ✅ |
| 38 | RevenueDistributionPEOLedgerCurrRevExchgRate | LEDGER_CURR_REV_EXCHG_RATE | — | ✅ |
| 39 | RevenueDistributionPEOLedgerCurrRevRateType | LEDGER_CURR_REV_RATE_TYPE | — | ✅ |
| 40 | RevenueDistributionPEOLedgerCurrRevenueAmt | LEDGER_CURR_REVENUE_AMT | — | ✅ |
| 41 | RevenueDistributionPEOLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | ✅ |
| 42 | RevenueDistributionPEOLedgerId | LEDGER_ID | — | ✅ |
| 43 | RevenueDistributionPEOLedgerRateDateType | LEDGER_RATE_DATE_TYPE | — | ✅ |
| 44 | RevenueDistributionPEOLineNum | LINE_NUM | — | ✅ |
| 45 | RevenueDistributionPEOLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 46 | RevenueDistributionPEOLinkedProjectId | LINKED_PROJECT_ID | — | ✅ |
| 47 | RevenueDistributionPEOLinkedTaskId | LINKED_TASK_ID | — | ✅ |
| 48 | RevenueDistributionPEOLocNumber | LOC_NUMBER | — | — |
| 49 | RevenueDistributionPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 50 | RevenueDistributionPEONonLaborOrgId | NON_LABOR_ORG_ID | — | — |
| 51 | RevenueDistributionPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 52 | RevenueDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 53 | RevenueDistributionPEOOrgId | ORG_ID | — | ✅ |
| 54 | RevenueDistributionPEOPaDate | PA_DATE | — | ✅ |
| 55 | RevenueDistributionPEOPaPeriodName | PA_PERIOD_NAME | — | ✅ |
| 56 | RevenueDistributionPEOPersonId | PERSON_ID | — | — |
| 57 | RevenueDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 58 | RevenueDistributionPEOProjectCurrExchgRate | PROJECT_CURR_EXCHG_RATE | — | ✅ |
| 59 | RevenueDistributionPEOProjectCurrRateType | PROJECT_CURR_RATE_TYPE | — | ✅ |
| 60 | RevenueDistributionPEOProjectCurrRevenueAmt | PROJECT_CURR_REVENUE_AMT | — | ✅ |
| 61 | RevenueDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 62 | RevenueDistributionPEOProjectCurrencyExchgDate | PROJECT_CURRENCY_EXCHG_DATE | — | ✅ |
| 63 | RevenueDistributionPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 64 | RevenueDistributionPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 65 | RevenueDistributionPEOQuantity | QUANTITY | — | ✅ |
| 66 | RevenueDistributionPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 67 | RevenueDistributionPEORecvrLegalEntityId | RECVR_LEGAL_ENTITY_ID | — | — |
| 68 | RevenueDistributionPEORequestId | REQUEST_ID | — | — |
| 69 | RevenueDistributionPEORevBillingControlId1 | REV_BILLING_CONTROL_ID1 | — | — |
| 70 | RevenueDistributionPEORevBillingControlId10 | REV_BILLING_CONTROL_ID10 | — | — |
| 71 | RevenueDistributionPEORevBillingControlId11 | REV_BILLING_CONTROL_ID11 | — | — |
| 72 | RevenueDistributionPEORevBillingControlId12 | REV_BILLING_CONTROL_ID12 | — | — |
| 73 | RevenueDistributionPEORevBillingControlId13 | REV_BILLING_CONTROL_ID13 | — | — |
| 74 | RevenueDistributionPEORevBillingControlId14 | REV_BILLING_CONTROL_ID14 | — | — |
| 75 | RevenueDistributionPEORevBillingControlId15 | REV_BILLING_CONTROL_ID15 | — | — |
| 76 | RevenueDistributionPEORevBillingControlId16 | REV_BILLING_CONTROL_ID16 | — | — |
| 77 | RevenueDistributionPEORevBillingControlId17 | REV_BILLING_CONTROL_ID17 | — | — |
| 78 | RevenueDistributionPEORevBillingControlId18 | REV_BILLING_CONTROL_ID18 | — | — |
| 79 | RevenueDistributionPEORevBillingControlId19 | REV_BILLING_CONTROL_ID19 | — | — |
| 80 | RevenueDistributionPEORevBillingControlId2 | REV_BILLING_CONTROL_ID2 | — | — |
| 81 | RevenueDistributionPEORevBillingControlId20 | REV_BILLING_CONTROL_ID20 | — | — |
| 82 | RevenueDistributionPEORevBillingControlId3 | REV_BILLING_CONTROL_ID3 | — | — |
| 83 | RevenueDistributionPEORevBillingControlId4 | REV_BILLING_CONTROL_ID4 | — | — |
| 84 | RevenueDistributionPEORevBillingControlId5 | REV_BILLING_CONTROL_ID5 | — | — |
| 85 | RevenueDistributionPEORevBillingControlId6 | REV_BILLING_CONTROL_ID6 | — | — |
| 86 | RevenueDistributionPEORevBillingControlId7 | REV_BILLING_CONTROL_ID7 | — | — |
| 87 | RevenueDistributionPEORevBillingControlId8 | REV_BILLING_CONTROL_ID8 | — | — |
| 88 | RevenueDistributionPEORevBillingControlId9 | REV_BILLING_CONTROL_ID9 | — | — |
| 89 | RevenueDistributionPEORevBurdenCompileSetId | REV_BURDEN_COMPILE_SET_ID | — | — |
| 90 | RevenueDistributionPEORevDiscountReasonCode | REV_DISCOUNT_REASON_CODE | — | ✅ |
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
| 104 | RevenueDistributionPEORevenueDenomRateId | REVENUE_DENOM_RATE_ID | — | — |
| 105 | RevenueDistributionPEORevenueDiscountPercentage | REVENUE_DISCOUNT_PERCENTAGE | — | ✅ |
| 106 | RevenueDistributionPEORevenueLaborMultiplier | REVENUE_LABOR_MULTIPLIER | — | ✅ |
| 107 | RevenueDistributionPEORevenueMarkupPercentage | REVENUE_MARKUP_PERCENTAGE | — | ✅ |
| 108 | RevenueDistributionPEORevenuePlanId | REVENUE_PLAN_ID | — | — |
| 109 | RevenueDistributionPEORevenueRateSourceId | REVENUE_RATE_SOURCE_ID | — | — |
| 110 | RevenueDistributionPEOReversedFlag | REVERSED_FLAG | — | ✅ |
| 111 | RevenueDistributionPEOReversedRevDistributionId | REVERSED_REV_DISTRIBUTION_ID | — | ✅ |
| 112 | RevenueDistributionPEOSlaEventId | SLA_EVENT_ID | — | — |
| 113 | RevenueDistributionPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | — |
| 114 | RevenueDistributionPEOTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 115 | RevenueDistributionPEOTpRevRulePercentage | TP_REV_RULE_PERCENTAGE | — | ✅ |
| 116 | RevenueDistributionPEOTpRevSchLinePercentage | TP_REV_SCH_LINE_PERCENTAGE | — | ✅ |
| 117 | RevenueDistributionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 118 | RevenueDistributionPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 119 | RevenueDistributionPEOTransactionProjectId | TRANSACTION_PROJECT_ID | — | — |
| 120 | RevenueDistributionPEOTransactionTaskId | TRANSACTION_TASK_ID | — | ✅ |
| 121 | RevenueDistributionPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 122 | RevenueDistributionPEOTrnsCurrRevenueAmt | TRNS_CURR_REVENUE_AMT | — | ✅ |
| 123 | RevenueDistributionPEOTrnsCurrUnitPrice | TRNS_CURR_UNIT_PRICE | — | ✅ |
| 124 | RevenueDistributionPEOTrnsCurrencyCode | TRNS_CURRENCY_CODE | — | — |
| 125 | RevenueDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 126 | RevenueDistributionPEOUomCode | UOM_CODE | — | ✅ |

### [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureItemPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 2 | ProjectExpenditureItemPEOExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 3 | ProjectExpenditureItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | ProjectExpenditureItemPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | — |
| 5 | ProjectExpenditureItemPEOVendorId | VENDOR_ID | — | — |

### [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypePEOEventTypeId | EVENT_TYPE_ID | — | — |
| 2 | EventTypePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |

### [[pjf_exp_types_vl|PJF_EXP_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpenditureTypePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 3 | ExpenditureTypePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |

### [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceBasePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | — |
| 2 | NonLaborResourceBasePEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |

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
| 1 | LinkProjectPEOName | NAME | — | — |
| 2 | LinkProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | LinkProjectPEOProjectId | PROJECT_ID | — | — |
| 4 | LinkProjectPEOSegment1 | SEGMENT1 | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransTaskPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | TransTaskPEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinkTaskStructurePEOElementNumber | ELEMENT_NUMBER | — | — |
| 2 | LinkTaskStructurePEOName | NAME | — | — |
| 3 | LinkTaskStructurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | LinkTaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementPEOAlias | ALIAS | — | — |
| 2 | RBSElementPEORbsElementId | RBS_ELEMENT_ID | — | — |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementNamePEOName | NAME | — | ✅ |
| 2 | RBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SystemLinkageFunctionPEOFunction | FUNCTION | — | — |
| 2 | SystemLinkageFunctionPEOMeaning | MEANING | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
