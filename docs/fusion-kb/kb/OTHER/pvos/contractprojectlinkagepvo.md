---
id: DOC-OTHER-PVO-ContractProjectLinkagePVO
doc_type: system-doc
title: "ContractProjectLinkagePVO — PVO Cross-Module"
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
  - ContractProjectLinkagePVO
  - contractprojectlinkagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractProjectLinkagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Project Linkage. Acessa as tabelas: OKC_K_HEADERS_ALL_B, OKC_K_LINES_B, OKC_K_LINES_VL (+3).

**Caminho:** `FscmTopModelAM.ContractProjectLinkAM.ContractProjectLinkagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 354 | 6 | 2 | 32 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 92 atributos (8 BICC)
- [[okc_k_lines_b|OKC_K_LINES_B]] — 80 atributos (7 BICC)
- [[okc_k_lines_vl|OKC_K_LINES_VL]] — 5 atributos
- [[pjb_cntrct_proj_links|PJB_CNTRCT_PROJ_LINKS]] — 19 atributos (2 PKs, 15 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 94 atributos (1 BICC)
- [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]] — 64 atributos (1 BICC)

---

## ⚙️ Atributos

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CHAcctRuleId | ACCT_RULE_ID | — | — |
| 2 | CHAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | — |
| 3 | CHApTermsId | AP_TERMS_ID | — | — |
| 4 | CHArInterfaceYn | AR_INTERFACE_YN | — | — |
| 5 | CHAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | — |
| 6 | CHBillSequence | BILL_SEQUENCE | — | — |
| 7 | CHBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 8 | CHBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 9 | CHBilledAtSource | BILLED_AT_SOURCE | — | — |
| 10 | CHBilltoLocationId | BILLTO_LOCATION_ID | — | — |
| 11 | CHBuyOrSell | BUY_OR_SELL | — | — |
| 12 | CHCancelledAmount | CANCELLED_AMOUNT | — | — |
| 13 | CHCommitmentId | COMMITMENT_ID | — | — |
| 14 | CHContractNumber | CONTRACT_NUMBER | — | — |
| 15 | CHContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | — |
| 16 | CHContractTypeId | CONTRACT_TYPE_ID | — | — |
| 17 | CHContributionPercent | CONTRIBUTION_PERCENT | — | — |
| 18 | CHCreatedBy | CREATED_BY | — | ✅ |
| 19 | CHCreationDate | CREATION_DATE | — | ✅ |
| 20 | CHCurrencyCode | CURRENCY_CODE | — | — |
| 21 | CHCustPoNumber | CUST_PO_NUMBER | — | — |
| 22 | CHCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | — |
| 23 | CHDateApproved | DATE_APPROVED | — | — |
| 24 | CHDateNotified | DATE_NOTIFIED | — | — |
| 25 | CHDateSigned | DATE_SIGNED | — | — |
| 26 | CHDateTerminated | DATE_TERMINATED | — | — |
| 27 | CHDatetimeCancelled | DATETIME_CANCELLED | — | — |
| 28 | CHEndDate | END_DATE | — | — |
| 29 | CHEstimatedAmount | ESTIMATED_AMOUNT | — | — |
| 30 | CHExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 31 | CHExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 32 | CHFob | FOB | — | — |
| 33 | CHFreightTerms | FREIGHT_TERMS | — | — |
| 34 | CHHoldBilling | HOLD_BILLING | — | — |
| 35 | CHHoldReasonCode | HOLD_REASON_CODE | — | — |
| 36 | CHHoldUntilDate | HOLD_UNTIL_DATE | — | — |
| 37 | CHId | ID | — | — |
| 38 | CHInvConvRateDate | INV_CONV_RATE_DATE | — | ✅ |
| 39 | CHInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | — |
| 40 | CHInvConvRateType | INV_CONV_RATE_TYPE | — | ✅ |
| 41 | CHInvOrganizationId | INV_ORGANIZATION_ID | — | — |
| 42 | CHInvPrintProfile | INV_PRINT_PROFILE | — | — |
| 43 | CHInvRuleId | INV_RULE_ID | — | — |
| 44 | CHInvTrxTypeId | INV_TRX_TYPE_ID | — | — |
| 45 | CHLastRevRecogDate | LAST_REV_RECOG_DATE | — | — |
| 46 | CHLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | CHLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | CHLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | CHLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 50 | CHLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 51 | CHMajorVersion | MAJOR_VERSION | — | — |
| 52 | CHNetInvoiceFlag | NET_INVOICE_FLAG | — | — |
| 53 | CHObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | CHOrderId | ORDER_ID | — | — |
| 55 | CHOrderNumber | ORDER_NUMBER | — | — |
| 56 | CHOrgId | ORG_ID | — | ✅ |
| 57 | CHOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 58 | CHOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 59 | CHOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 60 | CHOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | — |
| 61 | CHOverallRiskCode | OVERALL_RISK_CODE | — | — |
| 62 | CHOwningOrgId | OWNING_ORG_ID | — | ✅ |
| 63 | CHPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | — |
| 64 | CHPaymentTermId | PAYMENT_TERM_ID | — | — |
| 65 | CHPaymentType | PAYMENT_TYPE | — | — |
| 66 | CHPriceListId | PRICE_LIST_ID | — | — |
| 67 | CHPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | — |
| 68 | CHProgramAppName | PROGRAM_APP_NAME | — | — |
| 69 | CHProgramName | PROGRAM_NAME | — | — |
| 70 | CHQclId | QCL_ID | — | — |
| 71 | CHRecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 72 | CHRequestId | REQUEST_ID | — | — |
| 73 | CHRevConvRateType | REV_CONV_RATE_TYPE | — | — |
| 74 | CHShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 75 | CHShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 76 | CHShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 77 | CHShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 78 | CHSoldToAcctId | SOLD_TO_ACCT_ID | — | — |
| 79 | CHSoldToSiteId | SOLD_TO_SITE_ID | — | — |
| 80 | CHStartDate | START_DATE | — | — |
| 81 | CHStsCode | STS_CODE | — | — |
| 82 | CHSummaryTrxYn | SUMMARY_TRX_YN | — | — |
| 83 | CHSupplierId | SUPPLIER_ID | — | — |
| 84 | CHSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 85 | CHTaskId | TASK_ID | — | — |
| 86 | CHTaxAmount | TAX_AMOUNT | — | — |
| 87 | CHTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | — |
| 88 | CHTemplateUsed | TEMPLATE_USED | — | — |
| 89 | CHTemplateYn | TEMPLATE_YN | — | — |
| 90 | CHTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 91 | CHTrnCode | TRN_CODE | — | — |
| 92 | CHVersionType | VERSION_TYPE | — | — |

### [[okc_k_lines_b|OKC_K_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CLAtRiskYn | AT_RISK_YN | — | — |
| 2 | CLBillPlanId | BILL_PLAN_ID | — | — |
| 3 | CLBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 4 | CLBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 5 | CLBillableFlag | BILLABLE_FLAG | — | — |
| 6 | CLCancelledAmount | CANCELLED_AMOUNT | — | — |
| 7 | CLChrId | CHR_ID | — | — |
| 8 | CLCleId | CLE_ID | — | — |
| 9 | CLCreatedBy | CREATED_BY | — | — |
| 10 | CLCreationDate | CREATION_DATE | — | — |
| 11 | CLCreditedAmount | CREDITED_AMOUNT | — | — |
| 12 | CLCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | CLCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 14 | CLCustomerItemNumber | CUSTOMER_ITEM_NUMBER | — | — |
| 15 | CLDateCancelled | DATE_CANCELLED | — | — |
| 16 | CLDateTerminated | DATE_TERMINATED | — | — |
| 17 | CLDeliveryDate | DELIVERY_DATE | — | — |
| 18 | CLDisplaySequence | DISPLAY_SEQUENCE | — | — |
| 19 | CLDnzChrId | DNZ_CHR_ID | — | — |
| 20 | CLEndDate | END_DATE | — | — |
| 21 | CLExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 22 | CLExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 23 | CLFobCode | FOB_CODE | — | — |
| 24 | CLFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 25 | CLHoldReasonCode | HOLD_REASON_CODE | — | — |
| 26 | CLHoldUntilDate | HOLD_UNTIL_DATE | — | — |
| 27 | CLId | ID | — | — |
| 28 | CLJtotObject1Code | JTOT_OBJECT1_CODE | — | — |
| 29 | CLLastRevRecogDate | LAST_REV_RECOG_DATE | — | — |
| 30 | CLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | CLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | CLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 33 | CLLineAmount | LINE_AMOUNT | — | ✅ |
| 34 | CLLineNumber | LINE_NUMBER | — | — |
| 35 | CLLineTypeId | LINE_TYPE_ID | — | — |
| 36 | CLLineValue | LINE_VALUE | — | — |
| 37 | CLMajorVersion | MAJOR_VERSION | — | ✅ |
| 38 | CLNspFlag | NSP_FLAG | — | — |
| 39 | CLNumOfItem | NUM_OF_ITEM | — | — |
| 40 | CLObject1Id1 | OBJECT1_ID1 | — | — |
| 41 | CLObject1Id2 | OBJECT1_ID2 | — | — |
| 42 | CLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | CLOrderId | ORDER_ID | — | — |
| 44 | CLOrderLineId | ORDER_LINE_ID | — | — |
| 45 | CLOrderLineNumber | ORDER_LINE_NUMBER | — | — |
| 46 | CLOrderNumber | ORDER_NUMBER | — | — |
| 47 | CLOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 48 | CLOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 49 | CLOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 50 | CLOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | — |
| 51 | CLOverridenAmount | OVERRIDEN_AMOUNT | — | — |
| 52 | CLPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 53 | CLPercentComplete | PERCENT_COMPLETE | — | — |
| 54 | CLPriceUnit | PRICE_UNIT | — | — |
| 55 | CLProgramAppName | PROGRAM_APP_NAME | — | — |
| 56 | CLProgramName | PROGRAM_NAME | — | — |
| 57 | CLPurchasingCategoryId | PURCHASING_CATEGORY_ID | — | — |
| 58 | CLRecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 59 | CLRecvLocationId | RECV_LOCATION_ID | — | — |
| 60 | CLRequestId | REQUEST_ID | — | — |
| 61 | CLRevenuePlanId | REVENUE_PLAN_ID | — | — |
| 62 | CLShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 63 | CLShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 64 | CLShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 65 | CLSourceCodeClass | SOURCE_CODE_CLASS | — | — |
| 66 | CLStartDate | START_DATE | — | ✅ |
| 67 | CLStsCode | STS_CODE | — | ✅ |
| 68 | CLSupplierId | SUPPLIER_ID | — | — |
| 69 | CLSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 70 | CLSuppressedAmount | SUPPRESSED_AMOUNT | — | — |
| 71 | CLTaxAmount | TAX_AMOUNT | — | — |
| 72 | CLTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | — |
| 73 | CLTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 74 | CLTrnCode | TRN_CODE | — | — |
| 75 | CLUnbilledTerminatedAmont | UNBILLED_TERMINATED_AMONT | — | — |
| 76 | CLUndefLineTotal | UNDEF_LINE_TOTAL | — | — |
| 77 | CLUndefLineValue | UNDEF_LINE_VALUE | — | — |
| 78 | CLUndefUnitPrice | UNDEF_UNIT_PRICE | — | — |
| 79 | CLUomCode | UOM_CODE | — | — |
| 80 | CLVersionType | VERSION_TYPE | — | ✅ |

### [[okc_k_lines_vl|OKC_K_LINES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillableContractLinePEOId | ID | — | — |
| 2 | BillableContractLinePEOLineDescription | LINE_DESCRIPTION | — | — |
| 3 | BillableContractLinePEOLineName | LINE_NAME | — | — |
| 4 | BillableContractLinePEOLineNumber | LINE_NUMBER | — | — |
| 5 | BillableContractLinePEOMajorVersion | MAJOR_VERSION | — | — |

### [[pjb_cntrct_proj_links|PJB_CNTRCT_PROJ_LINKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FLActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | FLBillableContractLineId | BILLABLE_CONTRACT_LINE_ID | — | — |
| 3 | FLBillingTypeCode | BILLING_TYPE_CODE | — | — |
| 4 | FLContractId | CONTRACT_ID | — | ✅ |
| 5 | FLContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 6 | FLCreatedBy | CREATED_BY | — | ✅ |
| 7 | FLCreationDate | CREATION_DATE | — | ✅ |
| 8 | FLFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 9 | FLLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 10 | FLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | FLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | FLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | FLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | FLPercentComplete | PERCENT_COMPLETE | — | ✅ |
| 15 | FLProjElementId | PROJ_ELEMENT_ID | — | ✅ |
| 16 | FLProjectId | PROJECT_ID | — | ✅ |
| 17 | FLVersionType | VERSION_TYPE | — | ✅ |
| 18 | LinkId | LINK_ID | 🔑 | ✅ |
| 19 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOActualAsOfDate | ACTUAL_AS_OF_DATE | — | — |
| 2 | ProjectPEOActualDuration | ACTUAL_DURATION | — | — |
| 3 | ProjectPEOActualFinishDate | ACTUAL_FINISH_DATE | — | — |
| 4 | ProjectPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 5 | ProjectPEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | — |
| 6 | ProjectPEOAssetAllocationMethod | ASSET_ALLOCATION_METHOD | — | — |
| 7 | ProjectPEOBaselineAsOfDate | BASELINE_AS_OF_DATE | — | — |
| 8 | ProjectPEOBaselineDuration | BASELINE_DURATION | — | — |
| 9 | ProjectPEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 10 | ProjectPEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 11 | ProjectPEOCapitalEventProcessing | CAPITAL_EVENT_PROCESSING | — | — |
| 12 | ProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 13 | ProjectPEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | — |
| 14 | ProjectPEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | — |
| 15 | ProjectPEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | — |
| 16 | ProjectPEOCintRateSchId | CINT_RATE_SCH_ID | — | — |
| 17 | ProjectPEOCintStopDate | CINT_STOP_DATE | — | — |
| 18 | ProjectPEOClinLinkedCode | CLIN_LINKED_CODE | — | — |
| 19 | ProjectPEOClosedDate | CLOSED_DATE | — | — |
| 20 | ProjectPEOCompletionDate | COMPLETION_DATE | — | — |
| 21 | ProjectPEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 22 | ProjectPEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 23 | ProjectPEOCreatedBy | CREATED_BY | — | — |
| 24 | ProjectPEOCreatedFromProjectId | CREATED_FROM_PROJECT_ID | — | — |
| 25 | ProjectPEOCreationDate | CREATION_DATE | — | — |
| 26 | ProjectPEOCurrencyConvDate | CURRENCY_CONV_DATE | — | — |
| 27 | ProjectPEOCurrencyConvDateTypeCode | CURRENCY_CONV_DATE_TYPE_CODE | — | — |
| 28 | ProjectPEOCurrencyConvRateType | CURRENCY_CONV_RATE_TYPE | — | — |
| 29 | ProjectPEODescription | DESCRIPTION | — | — |
| 30 | ProjectPEOEarlyFinishDate | EARLY_FINISH_DATE | — | — |
| 31 | ProjectPEOEarlyStartDate | EARLY_START_DATE | — | — |
| 32 | ProjectPEOEnabledFlag | ENABLED_FLAG | — | — |
| 33 | ProjectPEOExpectedApprovalDate | EXPECTED_APPROVAL_DATE | — | — |
| 34 | ProjectPEOIcClinLinkedCode | IC_CLIN_LINKED_CODE | — | — |
| 35 | ProjectPEOKpiNotificationEnabled | KPI_NOTIFICATION_ENABLED | — | — |
| 36 | ProjectPEOKpiNotificationIncludeNotes | KPI_NOTIFICATION_INCLUDE_NOTES | — | — |
| 37 | ProjectPEOKpiNotificationRecipients | KPI_NOTIFICATION_RECIPIENTS | — | — |
| 38 | ProjectPEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 39 | ProjectPEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 40 | ProjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | ProjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | ProjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | ProjectPEOLateFinishDate | LATE_FINISH_DATE | — | — |
| 44 | ProjectPEOLateStartDate | LATE_START_DATE | — | — |
| 45 | ProjectPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 46 | ProjectPEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | — |
| 47 | ProjectPEOName | NAME | — | — |
| 48 | ProjectPEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 49 | ProjectPEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 50 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | ProjectPEOOrgId | ORG_ID | — | — |
| 52 | ProjectPEOOutlineLevel | OUTLINE_LEVEL | — | — |
| 53 | ProjectPEOOvrCostIndRateSchId | OVR_COST_IND_RATE_SCH_ID | — | — |
| 54 | ProjectPEOPlanningProjectFlag | PLANNING_PROJECT_FLAG | — | — |
| 55 | ProjectPEOPmProductCode | PM_PRODUCT_CODE | — | — |
| 56 | ProjectPEOPmProjectReference | PM_PROJECT_REFERENCE | — | — |
| 57 | ProjectPEOPriorityCode | PRIORITY_CODE | — | — |
| 58 | ProjectPEOProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 59 | ProjectPEOProgramId | PROGRAM_ID | — | — |
| 60 | ProjectPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 61 | ProjectPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 62 | ProjectPEOProjectId | PROJECT_ID | — | — |
| 63 | ProjectPEOProjectStatusCode | PROJECT_STATUS_CODE | — | — |
| 64 | ProjectPEOProjectTypeId | PROJECT_TYPE_ID | — | — |
| 65 | ProjectPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 66 | ProjectPEOProjectValue | PROJECT_VALUE | — | — |
| 67 | ProjectPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 68 | ProjectPEOPublicSectorFlag | PUBLIC_SECTOR_FLAG | — | — |
| 69 | ProjectPEORequestId | REQUEST_ID | — | — |
| 70 | ProjectPEOScheduledAsOfDate | SCHEDULED_AS_OF_DATE | — | — |
| 71 | ProjectPEOScheduledDuration | SCHEDULED_DURATION | — | — |
| 72 | ProjectPEOScheduledFinishDate | SCHEDULED_FINISH_DATE | — | — |
| 73 | ProjectPEOScheduledStartDate | SCHEDULED_START_DATE | — | — |
| 74 | ProjectPEOSegment1 | SEGMENT1 | — | — |
| 75 | ProjectPEOSegment10 | SEGMENT10 | — | — |
| 76 | ProjectPEOSegment2 | SEGMENT2 | — | — |
| 77 | ProjectPEOSegment3 | SEGMENT3 | — | — |
| 78 | ProjectPEOSegment4 | SEGMENT4 | — | — |
| 79 | ProjectPEOSegment5 | SEGMENT5 | — | — |
| 80 | ProjectPEOSegment6 | SEGMENT6 | — | — |
| 81 | ProjectPEOSegment7 | SEGMENT7 | — | — |
| 82 | ProjectPEOSegment8 | SEGMENT8 | — | — |
| 83 | ProjectPEOSegment9 | SEGMENT9 | — | — |
| 84 | ProjectPEOServiceTypeCode | SERVICE_TYPE_CODE | — | — |
| 85 | ProjectPEOStartDate | START_DATE | — | — |
| 86 | ProjectPEOStructureSharingCode | STRUCTURE_SHARING_CODE | — | — |
| 87 | ProjectPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 88 | ProjectPEOTargetFinishDate | TARGET_FINISH_DATE | — | — |
| 89 | ProjectPEOTargetStartDate | TARGET_START_DATE | — | — |
| 90 | ProjectPEOTemplateEndDateActive | TEMPLATE_END_DATE_ACTIVE | — | — |
| 91 | ProjectPEOTemplateFlag | TEMPLATE_FLAG | — | — |
| 92 | ProjectPEOTemplateStartDateActive | TEMPLATE_START_DATE_ACTIVE | — | — |
| 93 | ProjectPEOVerificationDate | VERIFICATION_DATE | — | — |
| 94 | ProjectPEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjf_proj_elements_vl|PJF_PROJ_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructurePEOAllowCrossChargeFlag | ALLOW_CROSS_CHARGE_FLAG | — | — |
| 2 | TaskStructurePEOBaselineFinishDate | BASELINE_FINISH_DATE | — | — |
| 3 | TaskStructurePEOBaselineStartDate | BASELINE_START_DATE | — | — |
| 4 | TaskStructurePEOBillableFlag | BILLABLE_FLAG | — | — |
| 5 | TaskStructurePEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | — |
| 6 | TaskStructurePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 7 | TaskStructurePEOCcProcessLaborFlag | CC_PROCESS_LABOR_FLAG | — | — |
| 8 | TaskStructurePEOCcProcessNlFlag | CC_PROCESS_NL_FLAG | — | — |
| 9 | TaskStructurePEOChargeableFlag | CHARGEABLE_FLAG | — | — |
| 10 | TaskStructurePEOCintEligibleFlag | CINT_ELIGIBLE_FLAG | — | — |
| 11 | TaskStructurePEOCintStopDate | CINT_STOP_DATE | — | — |
| 12 | TaskStructurePEOClinElementId | CLIN_ELEMENT_ID | — | — |
| 13 | TaskStructurePEOCompletionDate | COMPLETION_DATE | — | — |
| 14 | TaskStructurePEOCostIndRateSchId | COST_IND_RATE_SCH_ID | — | — |
| 15 | TaskStructurePEOCostIndSchFixedDate | COST_IND_SCH_FIXED_DATE | — | — |
| 16 | TaskStructurePEOCreatedBy | CREATED_BY | — | — |
| 17 | TaskStructurePEOCreatedFromSourceId | CREATED_FROM_SOURCE_ID | — | — |
| 18 | TaskStructurePEOCreationDate | CREATION_DATE | — | — |
| 19 | TaskStructurePEOCriticalFlag | CRITICAL_FLAG | — | — |
| 20 | TaskStructurePEODenormDisplaySequence | DENORM_DISPLAY_SEQUENCE | — | — |
| 21 | TaskStructurePEODenormElemVerId | DENORM_ELEM_VER_ID | — | — |
| 22 | TaskStructurePEODenormParentElemVerId | DENORM_PARENT_ELEM_VER_ID | — | — |
| 23 | TaskStructurePEODenormParentElementId | DENORM_PARENT_ELEMENT_ID | — | — |
| 24 | TaskStructurePEODenormParentObjectType | DENORM_PARENT_OBJECT_TYPE | — | — |
| 25 | TaskStructurePEODenormParentStructVerId | DENORM_PARENT_STRUCT_VER_ID | — | — |
| 26 | TaskStructurePEODenormTopElementId | DENORM_TOP_ELEMENT_ID | — | — |
| 27 | TaskStructurePEODenormWbsLevel | DENORM_WBS_LEVEL | — | — |
| 28 | TaskStructurePEODenormWbsNumber | DENORM_WBS_NUMBER | — | — |
| 29 | TaskStructurePEODescription | DESCRIPTION | — | — |
| 30 | TaskStructurePEOElementNumber | ELEMENT_NUMBER | — | — |
| 31 | TaskStructurePEOEtcCalcMethod | ETC_CALC_METHOD | — | — |
| 32 | TaskStructurePEOGenEtcSourceCode | GEN_ETC_SOURCE_CODE | — | — |
| 33 | TaskStructurePEOIcClinElementId | IC_CLIN_ELEMENT_ID | — | — |
| 34 | TaskStructurePEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 35 | TaskStructurePEOLaborTpFixedDate | LABOR_TP_FIXED_DATE | — | — |
| 36 | TaskStructurePEOLaborTpScheduleId | LABOR_TP_SCHEDULE_ID | — | — |
| 37 | TaskStructurePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | TaskStructurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | TaskStructurePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | TaskStructurePEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 41 | TaskStructurePEOLimitToTxnControlsFlag | LIMIT_TO_TXN_CONTROLS_FLAG | — | — |
| 42 | TaskStructurePEOManagerPersonId | MANAGER_PERSON_ID | — | — |
| 43 | TaskStructurePEOMilestoneFlag | MILESTONE_FLAG | — | — |
| 44 | TaskStructurePEOName | NAME | — | — |
| 45 | TaskStructurePEONlTpFixedDate | NL_TP_FIXED_DATE | — | — |
| 46 | TaskStructurePEONlTpScheduleId | NL_TP_SCHEDULE_ID | — | — |
| 47 | TaskStructurePEOObjectType | OBJECT_TYPE | — | — |
| 48 | TaskStructurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | TaskStructurePEOParentStructureId | PARENT_STRUCTURE_ID | — | — |
| 50 | TaskStructurePEOPercentCompCalcMethod | PERCENT_COMP_CALC_METHOD | — | — |
| 51 | TaskStructurePEOPlanningDatesRollupFlag | PLANNING_DATES_ROLLUP_FLAG | — | — |
| 52 | TaskStructurePEOPlanningEndDate | PLANNING_END_DATE | — | — |
| 53 | TaskStructurePEOPlanningStartDate | PLANNING_START_DATE | — | — |
| 54 | TaskStructurePEOPmSourceCode | PM_SOURCE_CODE | — | — |
| 55 | TaskStructurePEOPmSourceReference | PM_SOURCE_REFERENCE | — | — |
| 56 | TaskStructurePEOProjElementId | PROJ_ELEMENT_ID | — | — |
| 57 | TaskStructurePEOProjectId | PROJECT_ID | — | — |
| 58 | TaskStructurePEOReceiveProjectInvoiceFlag | RECEIVE_PROJECT_INVOICE_FLAG | — | — |
| 59 | TaskStructurePEORetirementCostFlag | RETIREMENT_COST_FLAG | — | — |
| 60 | TaskStructurePEOServiceTypeCode | SERVICE_TYPE_CODE | — | — |
| 61 | TaskStructurePEOSiteUseId | SITE_USE_ID | — | — |
| 62 | TaskStructurePEOStartDate | START_DATE | — | — |
| 63 | TaskStructurePEOStructureType | STRUCTURE_TYPE | — | — |
| 64 | TaskStructurePEOWorkTypeId | WORK_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
