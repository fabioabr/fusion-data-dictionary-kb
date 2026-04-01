---
id: DOC-OTHER-PVO-BillingEventPVO
doc_type: system-doc
title: "BillingEventPVO — PVO Cross-Module"
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
  - BillingEventPVO
  - billingeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillingEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Billing Event. Acessa as tabelas: EGP_SYSTEM_ITEMS_B, EGP_SYSTEM_ITEMS_TL_V, HR_ALL_ORGANIZATION_UNITS_F_VL (+14).

**Caminho:** `FscmTopModelAM.BillingEventAM.BillingEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 171 | 17 | 1 | 34 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]] — 3 atributos (1 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 4 atributos
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 4 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 6 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 5 atributos
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 2 atributos (1 BICC)
- [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]] — 2 atributos
- [[okc_k_headers_vl|OKC_K_HEADERS_VL]] — 5 atributos
- [[okc_k_lines_vl|OKC_K_LINES_VL]] — 7 atributos
- [[pjb_assignment_details|PJB_ASSIGNMENT_DETAILS]] — 2 atributos
- [[pjb_billing_assignments|PJB_BILLING_ASSIGNMENTS]] — 1 atributos
- [[pjb_billing_events|PJB_BILLING_EVENTS]] — 107 atributos (1 PKs, 26 BICC)
- [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]] — 4 atributos
- [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]] — 2 atributos (1 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 7 atributos (2 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 8 atributos (2 BICC)
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 2 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranlationPEODescription | DESCRIPTION | — | — |
| 2 | ItemTranlationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ItemTranlationPEOLanguage | LANGUAGE | — | — |
| 4 | ItemTranlationPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventOrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EventOrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | EventOrganizationName | NAME | — | — |
| 4 | EventOrganizationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 3 | EventBusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 4 | EventBusinessUnitPEOLegalEntityId | ORG_INFORMATION2 | — | — |
| 5 | EventBusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 6 | OrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | EventBusinessUnitPEOName | NAME | — | — |
| 4 | Language | LANGUAGE | — | — |
| 5 | OrganizationId | ORGANIZATION_ID | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

### [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypePEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 2 | ContractTypePEOName | NAME | — | — |

### [[okc_k_headers_vl|OKC_K_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderPEOContractNumber | CONTRACT_NUMBER | — | — |
| 2 | ContractHeaderPEOId | ID | — | — |
| 3 | ContractHeaderPEOMajorVersion | MAJOR_VERSION | — | — |
| 4 | ContractHeaderPEOOwningOrgId | OWNING_ORG_ID | — | — |
| 5 | ContractHeaderPEOStsCode | STS_CODE | — | — |

### [[okc_k_lines_vl|OKC_K_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLinePEOId | ID | — | — |
| 2 | ContractLinePEOLineAmount | LINE_AMOUNT | — | — |
| 3 | ContractLinePEOLineDescription | LINE_DESCRIPTION | — | — |
| 4 | ContractLinePEOLineName | LINE_NAME | — | — |
| 5 | ContractLinePEOLineNumber | LINE_NUMBER | — | — |
| 6 | ContractLinePEOMajorVersion | MAJOR_VERSION | — | — |
| 7 | ContractLinePEOStsCode | STS_CODE | — | — |

### [[pjb_assignment_details|PJB_ASSIGNMENT_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDetailPEOAssignmentDetailId | ASSIGNMENT_DETAIL_ID | — | — |
| 2 | AssignmentDetailPEOMajorVersion | MAJOR_VERSION | — | — |

### [[pjb_billing_assignments|PJB_BILLING_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingAssignmentPEOBillingAssignmentId | BILLING_ASSIGNMENT_ID | — | — |

### [[pjb_billing_events|PJB_BILLING_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractEventId | CONTRACT_EVENT_ID | — | — |
| 2 | DefaultEventsInvoicedFlag | INVOICED_FLAG | — | — |
| 3 | DefaultEventsRevenueRecognizedFlag | REVENUE_RECOGNZD_FLAG | — | — |
| 4 | EventId | EVENT_ID | 🔑 | ✅ |
| 5 | EventsAdjustDesc | ADJUST_DESC | — | — |
| 6 | EventsAdjustedEventId | ADJUSTED_EVENT_ID | — | — |
| 7 | EventsAuditAmt1 | AUDIT_AMT1 | — | — |
| 8 | EventsAuditAmt10 | AUDIT_AMT10 | — | — |
| 9 | EventsAuditAmt2 | AUDIT_AMT2 | — | — |
| 10 | EventsAuditAmt3 | AUDIT_AMT3 | — | — |
| 11 | EventsAuditAmt4 | AUDIT_AMT4 | — | — |
| 12 | EventsAuditAmt5 | AUDIT_AMT5 | — | — |
| 13 | EventsAuditAmt6 | AUDIT_AMT6 | — | — |
| 14 | EventsAuditAmt7 | AUDIT_AMT7 | — | — |
| 15 | EventsAuditAmt8 | AUDIT_AMT8 | — | — |
| 16 | EventsAuditAmt9 | AUDIT_AMT9 | — | — |
| 17 | EventsAuditCostPlanTypeId | AUDIT_COST_PLAN_TYPE_ID | — | — |
| 18 | EventsAuditRevPlanTypeId | AUDIT_REV_PLAN_TYPE_ID | — | — |
| 19 | EventsAutomaticFlag | AUTOMATIC_FLAG | — | — |
| 20 | EventsBillCurrOptCode | BILL_CURR_OPT_CODE | — | — |
| 21 | EventsBillHoldFlag | BILL_HOLD_FLAG | — | ✅ |
| 22 | EventsBillTrnsAmount | BILL_TRNS_AMOUNT | — | ✅ |
| 23 | EventsBillTrnsCurrencyCode | BILL_TRNS_CURRENCY_CODE | — | ✅ |
| 24 | EventsBillingAsgmtDetailId | BILLING_ASGMT_DETAIL_ID | — | — |
| 25 | EventsBillingAssignmentId | BILLING_ASSIGNMENT_ID | — | — |
| 26 | EventsBillingExtensionId | BILLING_EXTENSION_ID | — | — |
| 27 | EventsBillingTypeCode | BILLING_TYPE_CODE | — | — |
| 28 | EventsBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 29 | EventsCalcElementCode | CALC_ELEMENT_CODE | — | — |
| 30 | EventsCalculationInvoiceId | CALCULATION_INVOICE_ID | — | — |
| 31 | EventsCallLocation | CALL_LOCATION | — | — |
| 32 | EventsCallProcess | CALL_PROCESS | — | — |
| 33 | EventsCompletionDate | COMPLETION_DATE | — | ✅ |
| 34 | EventsContractCurrAmt | CONTRACT_CURR_AMT | — | ✅ |
| 35 | EventsContractCurrCode | CONTRACT_CURR_CODE | — | — |
| 36 | EventsContractCurrExchgDate | CONTRACT_CURR_EXCHG_DATE | — | — |
| 37 | EventsContractCurrExchgRate | CONTRACT_CURR_EXCHG_RATE | — | — |
| 38 | EventsContractCurrRateType | CONTRACT_CURR_RATE_TYPE | — | — |
| 39 | EventsContractId | CONTRACT_ID | — | — |
| 40 | EventsContractLineId | CONTRACT_LINE_ID | — | — |
| 41 | EventsContractRateDateType | CONTRACT_RATE_DATE_TYPE | — | — |
| 42 | EventsContractTypeId | CONTRACT_TYPE_ID | — | — |
| 43 | EventsCreatedBy | CREATED_BY | — | ✅ |
| 44 | EventsCreatedRequestId | CREATED_REQUEST_ID | — | — |
| 45 | EventsCreationDate | CREATION_DATE | — | ✅ |
| 46 | EventsEventDesc | EVENT_DESC | — | ✅ |
| 47 | EventsEventNum | EVENT_NUM | — | ✅ |
| 48 | EventsEventNumReversed | EVENT_NUM_REVERSED | — | ✅ |
| 49 | EventsEventTypeCode | EVENT_TYPE_CODE | — | — |
| 50 | EventsEventTypeId | EVENT_TYPE_ID | — | ✅ |
| 51 | EventsInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 52 | EventsInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 53 | EventsInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | — |
| 54 | EventsInvoicedAmt | INVOICED_AMT | — | — |
| 55 | EventsInvoicedPercentage | INVOICED_PERCENTAGE | — | — |
| 56 | EventsItemEventFlag | ITEM_EVENT_FLAG | — | ✅ |
| 57 | EventsItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 58 | EventsJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 59 | EventsJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 60 | EventsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | EventsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 62 | EventsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 63 | EventsLedgerCurrencyCode | LEDGER_CURRENCY_CODE | — | — |
| 64 | EventsLedgerInvoiceAmt | LEDGER_INVOICE_AMT | — | — |
| 65 | EventsLedgerRevenueAmt | LEDGER_REVENUE_AMT | — | — |
| 66 | EventsLinkageId | LINKAGE_ID | — | — |
| 67 | EventsLinkedTaskId | LINKED_TASK_ID | — | — |
| 68 | EventsMajorVersion | MAJOR_VERSION | — | — |
| 69 | EventsNonUpdateableFlag | NON_UPDATEABLE_FLAG | — | — |
| 70 | EventsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | EventsOrganizationId | ORGANIZATION_ID | — | ✅ |
| 72 | EventsProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 73 | EventsProjectId | PROJECT_ID | — | — |
| 74 | EventsProjectInvoiceAmt | PROJECT_INVOICE_AMT | — | — |
| 75 | EventsProjectRevenueAmt | PROJECT_REVENUE_AMT | — | — |
| 76 | EventsQuantity | QUANTITY | — | ✅ |
| 77 | EventsQuantityBilled | QUANTITY_BILLED | — | ✅ |
| 78 | EventsQuantityRevRecognzd | QUANTITY_REV_RECOGNZD | — | ✅ |
| 79 | EventsRbsElementId | RBS_ELEMENT_ID | — | — |
| 80 | EventsReference1 | REFERENCE1 | — | — |
| 81 | EventsReference10 | REFERENCE10 | — | — |
| 82 | EventsReference2 | REFERENCE2 | — | — |
| 83 | EventsReference3 | REFERENCE3 | — | — |
| 84 | EventsReference4 | REFERENCE4 | — | — |
| 85 | EventsReference5 | REFERENCE5 | — | — |
| 86 | EventsReference6 | REFERENCE6 | — | — |
| 87 | EventsReference7 | REFERENCE7 | — | — |
| 88 | EventsReference8 | REFERENCE8 | — | — |
| 89 | EventsReference9 | REFERENCE9 | — | — |
| 90 | EventsRequestId | REQUEST_ID | — | — |
| 91 | EventsRevenueAmt | REVENUE_AMT | — | — |
| 92 | EventsRevenueCurrencyCode | REVENUE_CURRENCY_CODE | — | — |
| 93 | EventsRevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | — |
| 94 | EventsRevenueHoldFlag | REVENUE_HOLD_FLAG | — | ✅ |
| 95 | EventsRevenueRecognzdPercentage | REVENUE_RECOGNZD_PERCENTAGE | — | — |
| 96 | EventsReverseAccrualFlag | REVERSE_ACCRUAL_FLAG | — | ✅ |
| 97 | EventsSourceName | SOURCENAME | — | — |
| 98 | EventsSourceRef | SOURCEREF | — | ✅ |
| 99 | EventsTaskId | TASK_ID | — | — |
| 100 | EventsTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 101 | EventsUnitPrice | UNIT_PRICE | — | ✅ |
| 102 | EventsUomCode | UOM_CODE | — | ✅ |
| 103 | InvoiceCurrDateType | INVOICE_CURR_DATE_TYPE | — | — |
| 104 | InvoiceCurrExchgDate | INVOICE_CURR_EXCHG_DATE | — | — |
| 105 | InvoiceCurrExchgRate | INVOICE_CURR_EXCHG_RATE | — | — |
| 106 | InvoiceCurrPotAmt | INVOICE_CURR_POT_AMT | — | — |
| 107 | InvoiceCurrRateType | INVOICE_CURR_RATE_TYPE | — | — |

### [[pjb_billing_extensions|PJB_BILLING_EXTENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillingExtensionPEOBillingExtensionId | BILLING_EXTENSION_ID | — | — |
| 2 | BillingExtensionPEODefaultEventDescription | DEFAULT_EVENT_DESCRIPTION | — | — |
| 3 | BillingExtensionPEOExtensionDesc | EXTENSION_DESC | — | — |
| 4 | BillingExtensionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjf_event_types_vl|PJF_EVENT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTypePEOEventTypeId | EVENT_TYPE_ID | — | — |
| 2 | EventTypePEOEventTypeName | EVENT_TYPE_NAME | — | ✅ |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | EventProjectPEOName | NAME | — | ✅ |
| 3 | EventProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | EventProjectPEOOrgId | ORG_ID | — | — |
| 5 | EventProjectPEOProjectId | PROJECT_ID | — | — |
| 6 | EventProjectPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 7 | EventProjectPEOSegment1 | SEGMENT1 | — | ✅ |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventTaskPEODescription | DESCRIPTION | — | — |
| 2 | EventTaskPEOElementNumber | ELEMENT_NUMBER | — | ✅ |
| 3 | EventTaskPEOName | NAME | — | ✅ |
| 4 | EventTaskPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | EventTaskPEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 6 | LinkTaskPEOElementNumber | ELEMENT_NUMBER | — | — |
| 7 | LinkTaskPEOName | NAME | — | — |
| 8 | LinkTaskPEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRbsPEOAlias | ALIAS | — | — |
| 2 | ProjectRbsPEORbsElementId | RBS_ELEMENT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
