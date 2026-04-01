---
id: DOC-OTHER-PVO-ContractHeaderLinesRefP
doc_type: system-doc
title: "ContractHeaderLinesRefP — PVO Cross-Module"
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
  - ContractHeaderLinesRefP
  - contractheaderlinesrefp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractHeaderLinesRefP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Header Lines Ref P. Acessa as tabelas: EGP_CATEGORIES_B, EGP_CATEGORIES_TL, EGP_SYSTEM_ITEMS_B_V (+33).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractHeaderLinesRefP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1287 | 36 | 2 | 104 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_b|EGP_CATEGORIES_B]] — 26 atributos (1 BICC)
- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 11 atributos (1 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 323 atributos (1 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 14 atributos (1 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 3 atributos
- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 16 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 3 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 8 atributos
- [[gms_sponsor_accts_v|GMS_SPONSOR_ACCTS_V]] — 3 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 17 atributos (3 BICC)
- [[hr_organization_v|HR_ORGANIZATION_V]] — 6 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 17 atributos (5 BICC)
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 14 atributos (3 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 25 atributos
- [[hz_parties|HZ_PARTIES]] — 274 atributos (2 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 172 atributos (2 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 5 atributos (1 BICC)
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 3 atributos
- [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]] — 38 atributos (5 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 105 atributos (27 BICC)
- [[okc_k_headers_tl|OKC_K_HEADERS_TL]] — 15 atributos (3 BICC)
- [[okc_k_inv_rev_summary_v|OKC_K_INV_REV_SUMMARY_V]] — 4 atributos
- [[okc_k_lines_b|OKC_K_LINES_B]] — 96 atributos (2 PKs, 24 BICC)
- [[okc_k_lines_tl|OKC_K_LINES_TL]] — 18 atributos (3 BICC)
- [[okc_line_types_vl|OKC_LINE_TYPES_VL]] — 3 atributos (2 BICC)
- [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]] — 19 atributos (8 BICC)
- [[pjb_clin_internal_attributes|PJB_CLIN_INTERNAL_ATTRIBUTES]] — 12 atributos (3 BICC)
- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 3 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos (1 BICC)
- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 3 atributos (1 BICC)
- [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]] — 2 atributos (1 BICC)
- [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]] — 3 atributos (1 BICC)
- [[qsc_pricebook_headers_vl|QSC_PRICEBOOK_HEADERS_VL]] — 6 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 6 atributos (2 BICC)
- [[zx_exemptions_v|ZX_EXEMPTIONS_V]] — 8 atributos

---

## ⚙️ Atributos

### [[egp_categories_b|EGP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineCategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ContractLineCategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | ContractLineCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 4 | ContractLineCategoryPEOCreatedBy | CREATED_BY | — | — |
| 5 | ContractLineCategoryPEOCreationDate | CREATION_DATE | — | — |
| 6 | ContractLineCategoryPEODescription | DESCRIPTION | — | — |
| 7 | ContractLineCategoryPEODisableDate | DISABLE_DATE | — | — |
| 8 | ContractLineCategoryPEOEnabledFlag | ENABLED_FLAG | — | — |
| 9 | ContractLineCategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | ContractLineCategoryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | ContractLineCategoryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ContractLineCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ContractLineCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ContractLineCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ContractLineCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ContractLineCategoryPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | ContractLineCategoryPEOProgramName | PROGRAM_NAME | — | — |
| 18 | ContractLineCategoryPEORequestId | REQUEST_ID | — | — |
| 19 | ContractLineCategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 20 | ContractLineCategoryPEOStructureId | STRUCTURE_ID | — | — |
| 21 | ContractLineCategoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 22 | ContractLineCategoryPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 23 | ContractLineCategoryPEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 24 | ContractLineCategoryPEOTotalProdId | TOTAL_PROD_ID | — | — |
| 25 | ContractLineCategoryPEOWebStatus | WEB_STATUS | — | — |
| 26 | ContractLineCategoryPEOWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineCategoryTLPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ContractLineCategoryTLPEOCategoryName | CATEGORY_NAME | — | — |
| 3 | ContractLineCategoryTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | ContractLineCategoryTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | ContractLineCategoryTLPEODescription | DESCRIPTION | — | — |
| 6 | ContractLineCategoryTLPEOLanguage | LANGUAGE | — | — |
| 7 | ContractLineCategoryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContractLineCategoryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContractLineCategoryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContractLineCategoryTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ContractLineCategoryTLPEOSourceLang | SOURCE_LANG | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractItemPEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | ContractItemPEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 3 | ContractItemPEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 4 | ContractItemPEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 5 | ContractItemPEOAcdType | ACD_TYPE | — | — |
| 6 | ContractItemPEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 7 | ContractItemPEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 8 | ContractItemPEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 9 | ContractItemPEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | — |
| 10 | ContractItemPEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | — |
| 11 | ContractItemPEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 12 | ContractItemPEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 13 | ContractItemPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 14 | ContractItemPEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 15 | ContractItemPEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 16 | ContractItemPEOAssetClass | ASSET_CLASS | — | — |
| 17 | ContractItemPEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 18 | ContractItemPEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | — |
| 19 | ContractItemPEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 20 | ContractItemPEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 21 | ContractItemPEOAtpFlag | ATP_FLAG | — | — |
| 22 | ContractItemPEOAtpRuleId | ATP_RULE_ID | — | — |
| 23 | ContractItemPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 24 | ContractItemPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 25 | ContractItemPEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 26 | ContractItemPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 27 | ContractItemPEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 28 | ContractItemPEOBaseItemId | BASE_ITEM_ID | — | — |
| 29 | ContractItemPEOBomItemType | BOM_ITEM_TYPE | — | — |
| 30 | ContractItemPEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 31 | ContractItemPEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 32 | ContractItemPEOBuyerId | BUYER_ID | — | — |
| 33 | ContractItemPEOCarryingCost | CARRYING_COST | — | — |
| 34 | ContractItemPEOCasNumber | CAS_NUMBER | — | — |
| 35 | ContractItemPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 36 | ContractItemPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 37 | ContractItemPEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 38 | ContractItemPEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 39 | ContractItemPEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 40 | ContractItemPEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 41 | ContractItemPEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 42 | ContractItemPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 43 | ContractItemPEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 44 | ContractItemPEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 45 | ContractItemPEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 46 | ContractItemPEOConfigMatch | CONFIG_MATCH | — | — |
| 47 | ContractItemPEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 48 | ContractItemPEOConfigOrgs | CONFIG_ORGS | — | — |
| 49 | ContractItemPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 50 | ContractItemPEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 51 | ContractItemPEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 52 | ContractItemPEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 53 | ContractItemPEOContractItemTypeCode | CONTRACT_ITEM_TYPE_CODE | — | — |
| 54 | ContractItemPEOConvergence | CONVERGENCE | — | — |
| 55 | ContractItemPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 56 | ContractItemPEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 57 | ContractItemPEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 58 | ContractItemPEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 59 | ContractItemPEOCreatedBy | CREATED_BY | — | — |
| 60 | ContractItemPEOCreationDate | CREATION_DATE | — | — |
| 61 | ContractItemPEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 62 | ContractItemPEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 63 | ContractItemPEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 64 | ContractItemPEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 65 | ContractItemPEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 66 | ContractItemPEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 67 | ContractItemPEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 68 | ContractItemPEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 69 | ContractItemPEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 70 | ContractItemPEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 71 | ContractItemPEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 72 | ContractItemPEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 73 | ContractItemPEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 74 | ContractItemPEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 75 | ContractItemPEODefaultGrade | DEFAULT_GRADE | — | — |
| 76 | ContractItemPEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 77 | ContractItemPEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 78 | ContractItemPEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 79 | ContractItemPEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 80 | ContractItemPEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 81 | ContractItemPEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 82 | ContractItemPEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 83 | ContractItemPEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 84 | ContractItemPEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 85 | ContractItemPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 86 | ContractItemPEODivergence | DIVERGENCE | — | — |
| 87 | ContractItemPEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 88 | ContractItemPEODqRequiredFlag | DQ_REQUIRED_FLAG | — | — |
| 89 | ContractItemPEODqSemanticKey | DQ_SEMANTIC_KEY | — | — |
| 90 | ContractItemPEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 91 | ContractItemPEODualUomControl | DUAL_UOM_CONTROL | — | — |
| 92 | ContractItemPEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 93 | ContractItemPEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 94 | ContractItemPEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 95 | ContractItemPEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 96 | ContractItemPEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 97 | ContractItemPEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 98 | ContractItemPEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 99 | ContractItemPEOEamItemType | EAM_ITEM_TYPE | — | — |
| 100 | ContractItemPEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 101 | ContractItemPEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 102 | ContractItemPEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 103 | ContractItemPEOEnabledFlag | ENABLED_FLAG | — | — |
| 104 | ContractItemPEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 105 | ContractItemPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 106 | ContractItemPEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 107 | ContractItemPEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 108 | ContractItemPEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 109 | ContractItemPEOEventFlag | EVENT_FLAG | — | — |
| 110 | ContractItemPEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 111 | ContractItemPEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 112 | ContractItemPEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 113 | ContractItemPEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 114 | ContractItemPEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 115 | ContractItemPEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 116 | ContractItemPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 117 | ContractItemPEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 118 | ContractItemPEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 119 | ContractItemPEOForecastHorizon | FORECAST_HORIZON | — | — |
| 120 | ContractItemPEOFullLeadTime | FULL_LEAD_TIME | — | — |
| 121 | ContractItemPEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 122 | ContractItemPEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 123 | ContractItemPEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 124 | ContractItemPEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 125 | ContractItemPEOHoldDays | HOLD_DAYS | — | — |
| 126 | ContractItemPEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 127 | ContractItemPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 128 | ContractItemPEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 129 | ContractItemPEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 130 | ContractItemPEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 131 | ContractItemPEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 132 | ContractItemPEOInternalVolume | INTERNAL_VOLUME | — | — |
| 133 | ContractItemPEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 134 | ContractItemPEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 135 | ContractItemPEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 136 | ContractItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 137 | ContractItemPEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 138 | ContractItemPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 139 | ContractItemPEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 140 | ContractItemPEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 141 | ContractItemPEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 142 | ContractItemPEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 143 | ContractItemPEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 144 | ContractItemPEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 145 | ContractItemPEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 146 | ContractItemPEOItemNumber | ITEM_NUMBER | — | — |
| 147 | ContractItemPEOItemType | ITEM_TYPE | — | — |
| 148 | ContractItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 149 | ContractItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 150 | ContractItemPEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 151 | ContractItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 152 | ContractItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 153 | ContractItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 154 | ContractItemPEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 155 | ContractItemPEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 156 | ContractItemPEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 157 | ContractItemPEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 158 | ContractItemPEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 159 | ContractItemPEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 160 | ContractItemPEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 161 | ContractItemPEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 162 | ContractItemPEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 163 | ContractItemPEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 164 | ContractItemPEOMarketPrice | MARKET_PRICE | — | — |
| 165 | ContractItemPEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 166 | ContractItemPEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 167 | ContractItemPEOMaturityDays | MATURITY_DAYS | — | — |
| 168 | ContractItemPEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 169 | ContractItemPEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 170 | ContractItemPEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 171 | ContractItemPEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 172 | ContractItemPEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 173 | ContractItemPEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 174 | ContractItemPEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 175 | ContractItemPEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 176 | ContractItemPEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 177 | ContractItemPEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 178 | ContractItemPEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 179 | ContractItemPEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 180 | ContractItemPEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 181 | ContractItemPEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 182 | ContractItemPEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 183 | ContractItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 184 | ContractItemPEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 185 | ContractItemPEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 186 | ContractItemPEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 187 | ContractItemPEOOrderCost | ORDER_COST | — | — |
| 188 | ContractItemPEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 189 | ContractItemPEOOrganizationId | ORGANIZATION_ID | — | — |
| 190 | ContractItemPEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 191 | ContractItemPEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 192 | ContractItemPEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 193 | ContractItemPEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 194 | ContractItemPEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 195 | ContractItemPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 196 | ContractItemPEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 197 | ContractItemPEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 198 | ContractItemPEOPickingRuleId | PICKING_RULE_ID | — | — |
| 199 | ContractItemPEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 200 | ContractItemPEOPlannerCode | PLANNER_CODE | — | — |
| 201 | ContractItemPEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 202 | ContractItemPEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 203 | ContractItemPEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 204 | ContractItemPEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 205 | ContractItemPEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 206 | ContractItemPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 207 | ContractItemPEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 208 | ContractItemPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 209 | ContractItemPEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 210 | ContractItemPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 211 | ContractItemPEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 212 | ContractItemPEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 213 | ContractItemPEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 214 | ContractItemPEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 215 | ContractItemPEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 216 | ContractItemPEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 217 | ContractItemPEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 218 | ContractItemPEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 219 | ContractItemPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 220 | ContractItemPEOProgramName | PROGRAM_NAME | — | — |
| 221 | ContractItemPEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 222 | ContractItemPEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 223 | ContractItemPEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 224 | ContractItemPEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 225 | ContractItemPEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 226 | ContractItemPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 227 | ContractItemPEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 228 | ContractItemPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 229 | ContractItemPEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 230 | ContractItemPEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 231 | ContractItemPEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 232 | ContractItemPEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 233 | ContractItemPEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 234 | ContractItemPEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 235 | ContractItemPEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 236 | ContractItemPEORepairProgram | REPAIR_PROGRAM | — | — |
| 237 | ContractItemPEORepairYield | REPAIR_YIELD | — | — |
| 238 | ContractItemPEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 239 | ContractItemPEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 240 | ContractItemPEORequestId | REQUEST_ID | — | — |
| 241 | ContractItemPEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | — |
| 242 | ContractItemPEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | — |
| 243 | ContractItemPEOReservableType | RESERVABLE_TYPE | — | — |
| 244 | ContractItemPEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 245 | ContractItemPEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 246 | ContractItemPEORetestInterval | RETEST_INTERVAL | — | — |
| 247 | ContractItemPEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 248 | ContractItemPEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 249 | ContractItemPEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 250 | ContractItemPEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 251 | ContractItemPEORoundingFactor | ROUNDING_FACTOR | — | — |
| 252 | ContractItemPEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 253 | ContractItemPEOSalesAccount | SALES_ACCOUNT | — | — |
| 254 | ContractItemPEOSalesProductSubType | SALES_PRODUCT_SUB_TYPE | — | — |
| 255 | ContractItemPEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 256 | ContractItemPEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 257 | ContractItemPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 258 | ContractItemPEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 259 | ContractItemPEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 260 | ContractItemPEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 261 | ContractItemPEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 262 | ContractItemPEOServiceDuration | SERVICE_DURATION | — | — |
| 263 | ContractItemPEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 264 | ContractItemPEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | — |
| 265 | ContractItemPEOServiceStartDelay | SERVICE_START_DELAY | — | — |
| 266 | ContractItemPEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | — |
| 267 | ContractItemPEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 268 | ContractItemPEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 269 | ContractItemPEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 270 | ContractItemPEOShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 271 | ContractItemPEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 272 | ContractItemPEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 273 | ContractItemPEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 274 | ContractItemPEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 275 | ContractItemPEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 276 | ContractItemPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 277 | ContractItemPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 278 | ContractItemPEOSourceType | SOURCE_TYPE | — | — |
| 279 | ContractItemPEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 280 | ContractItemPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 281 | ContractItemPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 282 | ContractItemPEOStartUponMilestoneCode | START_UPON_MILESTONE_CODE | — | — |
| 283 | ContractItemPEOStdLotSize | STD_LOT_SIZE | — | — |
| 284 | ContractItemPEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 285 | ContractItemPEOStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 286 | ContractItemPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 287 | ContractItemPEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 288 | ContractItemPEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 289 | ContractItemPEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 290 | ContractItemPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 291 | ContractItemPEOTaxCode | TAX_CODE | — | — |
| 292 | ContractItemPEOTaxableFlag | TAXABLE_FLAG | — | — |
| 293 | ContractItemPEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 294 | ContractItemPEOThreadId | THREAD_ID | — | — |
| 295 | ContractItemPEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 296 | ContractItemPEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 297 | ContractItemPEOUnNumberId | UN_NUMBER_ID | — | — |
| 298 | ContractItemPEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 299 | ContractItemPEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 300 | ContractItemPEOUnitHeight | UNIT_HEIGHT | — | — |
| 301 | ContractItemPEOUnitLength | UNIT_LENGTH | — | — |
| 302 | ContractItemPEOUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 303 | ContractItemPEOUnitVolume | UNIT_VOLUME | — | — |
| 304 | ContractItemPEOUnitWeight | UNIT_WEIGHT | — | — |
| 305 | ContractItemPEOUnitWidth | UNIT_WIDTH | — | — |
| 306 | ContractItemPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 307 | ContractItemPEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 308 | ContractItemPEOVersionEndDate | VERSION_END_DATE | — | — |
| 309 | ContractItemPEOVersionId | VERSION_ID | — | — |
| 310 | ContractItemPEOVersionStartDate | VERSION_START_DATE | — | — |
| 311 | ContractItemPEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 312 | ContractItemPEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 313 | ContractItemPEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 314 | ContractItemPEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 315 | ContractItemPEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 316 | ContractItemPEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 317 | ContractItemPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 318 | ContractItemPEOWebStatus | WEB_STATUS | — | — |
| 319 | ContractItemPEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 320 | ContractItemPEOWhUpdateDate | WH_UPDATE_DATE | — | — |
| 321 | ContractItemPEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 322 | ContractItemPEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 323 | ContractItemPEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractItemTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ContractItemTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ContractItemTranslationPEODescription | DESCRIPTION | — | — |
| 4 | ContractItemTranslationPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | — |
| 5 | ContractItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | ContractItemTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ContractItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContractItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContractItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContractItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | — |
| 11 | ContractItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ContractItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 13 | ContractItemTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 14 | ContractItemTranslationPEOTemplateName | TEMPLATE_NAME | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineEgpSysItemPEODescription | DESCRIPTION | — | — |
| 2 | ContractLineEgpSysItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | ContractLineEgpSysItemPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 2 | CancelReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 3 | CancelReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 4 | CancelReasonSetIdAssignmentSetId | SET_ID | — | — |
| 5 | CloseReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 6 | CloseReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 7 | CloseReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 8 | CloseReasonSetIdAssignmentSetId | SET_ID | — | — |
| 9 | HdrTaxClassPEODetRefGpName | REFERENCE_GROUP_NAME | — | — |
| 10 | HdrTaxClassPEODetType | DETERMINANT_TYPE | — | — |
| 11 | HdrTaxClassPEODetValue | DETERMINANT_VALUE | — | — |
| 12 | HdrTaxClassPEOSetId | SET_ID | — | ✅ |
| 13 | HoldReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 14 | HoldReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 15 | HoldReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 16 | HoldReasonSetIdAssignmentSetId | SET_ID | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrBusinessUnitId | BU_ID | — | — |
| 2 | HdrBusinessUnitPEOLedgerId | PRIMARY_LEDGER_ID | — | — |
| 3 | HdrBusinessUnitPEOName | BU_NAME | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderInvConvRatePEOConversionType | CONVERSION_TYPE | — | — |
| 2 | ContractHeaderInvConvRatePEODescription | DESCRIPTION | — | — |
| 3 | ContractHeaderInvConvRatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ContractHeaderInvConvRatePEOUserConversionType | USER_CONVERSION_TYPE | — | — |
| 5 | ContractHeaderRevConvRatePEOConversionType | CONVERSION_TYPE | — | — |
| 6 | ContractHeaderRevConvRatePEODescription | DESCRIPTION | — | — |
| 7 | ContractHeaderRevConvRatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ContractHeaderRevConvRatePEOUserConversionType | USER_CONVERSION_TYPE | — | — |

### [[gms_sponsor_accts_v|GMS_SPONSOR_ACCTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctId | CUST_ACCT_ID | — | — |
| 2 | LocNumber | LOC_NUMBER | — | — |
| 3 | SponsorId | SPONSOR_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrganizationInformationPEOOrgInformationContext | ORG_INFORMATION_CONTEXT | — | — |
| 4 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrvdrBusinessUnitTrnsltnPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PrvdrBusinessUnitTrnsltnPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PrvdrBusinessUnitTrnsltnPEOLanguage | LANGUAGE | — | — |
| 4 | PrvdrBusinessUnitTrnsltnPEOName | NAME | — | ✅ |
| 5 | PrvdrBusinessUnitTrnsltnPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PrvdrBusinessUnitTrnsltnPEOOrganizationId | ORGANIZATION_ID | — | — |
| 7 | RcvrBusinessUnitTrnsltnPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RcvrBusinessUnitTrnsltnPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RcvrBusinessUnitTrnsltnPEOLanguage | LANGUAGE | — | — |
| 10 | RcvrBusinessUnitTrnsltnPEOName | NAME | — | ✅ |
| 11 | RcvrBusinessUnitTrnsltnPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RcvrBusinessUnitTrnsltnPEOOrganizationId | ORGANIZATION_ID | — | — |
| 13 | RcvrExpenditureOrgTrnsltnPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | RcvrExpenditureOrgTrnsltnPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 15 | RcvrExpenditureOrgTrnsltnPEOLanguage | LANGUAGE | — | — |
| 16 | RcvrExpenditureOrgTrnsltnPEOName | NAME | — | ✅ |
| 17 | RcvrExpenditureOrgTrnsltnPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderOwingOrgPEOClassCode | CLASSIFICATION_CODE | — | — |
| 2 | ContractHeaderOwingOrgPEOEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContractHeaderOwingOrgPEOEffStrtDate | EFFECTIVE_START_DATE | — | — |
| 4 | ContractHeaderOwingOrgPEOName | NAME | — | ✅ |
| 5 | ContractHeaderOwingOrgPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 6 | ContractHeaderOwingOrgPEOOrgId | ORGANIZATION_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderBillToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 2 | ContractHeaderBillToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 3 | ContractHeaderBillToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 4 | ContractHeaderShipToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 5 | ContractHeaderShipToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 6 | ContractHeaderShipToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 7 | ContractHeaderSoldToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 8 | ContractHeaderSoldToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 9 | ContractHeaderSoldToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 10 | ContractLineBillToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 11 | ContractLineBillToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 12 | ContractLineBillToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 13 | ContractLineShipToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 14 | ContractLineShipToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 15 | ContractLineShipToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 16 | CustAccountId | CUST_ACCOUNT_ID | — | — |
| 17 | CustAccountPartyId | PARTY_ID | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderBillToSitePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 2 | ContractHeaderBillToSitePEOSiteUseCode | SITE_USE_CODE | — | — |
| 3 | ContractHeaderBillToSitePEOSiteUseId | SITE_USE_ID | — | — |
| 4 | ContractHeaderShipToSitePEOLocation | LOCATION | — | ✅ |
| 5 | ContractHeaderShipToSitePEOSiteUseCode | SITE_USE_CODE | — | — |
| 6 | ContractHeaderShipToSitePEOSiteUseIdSiteUseId | SITE_USE_ID | — | — |
| 7 | ContractLineBillToSitePEOLocation | LOCATION | — | ✅ |
| 8 | ContractLineBillToSitePEOSiteUseCode | SITE_USE_CODE | — | — |
| 9 | ContractLineBillToSitePEOSiteUseId | SITE_USE_ID | — | — |
| 10 | ContractLineShipToSitePEOLocation | LOCATION | — | ✅ |
| 11 | ContractLineShipToSitePEOSiteUseCode | SITE_USE_CODE | — | — |
| 12 | ContractLineShipToSitePEOSiteUseId | SITE_USE_ID | — | — |
| 13 | HdrSoldToSitePEOLocation | LOCATION | — | — |
| 14 | HdrSoldToSitePEOSiteUseId | SITE_USE_ID | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrBillToAddress1 | ADDRESS1 | — | — |
| 2 | HdrBillToAddress2 | ADDRESS2 | — | — |
| 3 | HdrBillToAddress3 | ADDRESS3 | — | — |
| 4 | HdrBillToAddress4 | ADDRESS4 | — | — |
| 5 | HdrBillToLocationId | LOCATION_ID | — | — |
| 6 | HdrShipToAddress1 | ADDRESS1 | — | — |
| 7 | HdrShipToAddress2 | ADDRESS2 | — | — |
| 8 | HdrShipToAddress3 | ADDRESS3 | — | — |
| 9 | HdrShipToAddress4 | ADDRESS4 | — | — |
| 10 | HdrShipToLocationId | LOCATION_ID | — | — |
| 11 | HdrSoldToAddress1 | ADDRESS1 | — | — |
| 12 | HdrSoldToAddress2 | ADDRESS2 | — | — |
| 13 | HdrSoldToAddress3 | ADDRESS3 | — | — |
| 14 | HdrSoldToAddress4 | ADDRESS4 | — | — |
| 15 | HdrSoldToLocationId | LOCATION_ID | — | — |
| 16 | LnBillToAddress1 | ADDRESS1 | — | — |
| 17 | LnBillToAddress2 | ADDRESS2 | — | — |
| 18 | LnBillToAddress3 | ADDRESS3 | — | — |
| 19 | LnBillToAddress4 | ADDRESS4 | — | — |
| 20 | LnBillToLocationId | LOCATION_ID | — | — |
| 21 | LnShipToAddress1 | ADDRESS1 | — | — |
| 22 | LnShipToAddress2 | ADDRESS2 | — | — |
| 23 | LnShipToAddress3 | ADDRESS3 | — | — |
| 24 | LnShipToAddress4 | ADDRESS4 | — | — |
| 25 | LnShipToLocationId | LOCATION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrSupplierAddress1 | ADDRESS1 | — | — |
| 2 | HdrSupplierAddress2 | ADDRESS2 | — | — |
| 3 | HdrSupplierAddress3 | ADDRESS3 | — | — |
| 4 | HdrSupplierAddress4 | ADDRESS4 | — | — |
| 5 | HdrSupplierAnalysisFy | ANALYSIS_FY | — | — |
| 6 | HdrSupplierAttribute1 | ATTRIBUTE1 | — | — |
| 7 | HdrSupplierAttribute10 | ATTRIBUTE10 | — | — |
| 8 | HdrSupplierAttribute11 | ATTRIBUTE11 | — | — |
| 9 | HdrSupplierAttribute12 | ATTRIBUTE12 | — | — |
| 10 | HdrSupplierAttribute13 | ATTRIBUTE13 | — | — |
| 11 | HdrSupplierAttribute14 | ATTRIBUTE14 | — | — |
| 12 | HdrSupplierAttribute15 | ATTRIBUTE15 | — | — |
| 13 | HdrSupplierAttribute16 | ATTRIBUTE16 | — | — |
| 14 | HdrSupplierAttribute17 | ATTRIBUTE17 | — | — |
| 15 | HdrSupplierAttribute18 | ATTRIBUTE18 | — | — |
| 16 | HdrSupplierAttribute19 | ATTRIBUTE19 | — | — |
| 17 | HdrSupplierAttribute2 | ATTRIBUTE2 | — | — |
| 18 | HdrSupplierAttribute20 | ATTRIBUTE20 | — | — |
| 19 | HdrSupplierAttribute21 | ATTRIBUTE21 | — | — |
| 20 | HdrSupplierAttribute22 | ATTRIBUTE22 | — | — |
| 21 | HdrSupplierAttribute23 | ATTRIBUTE23 | — | — |
| 22 | HdrSupplierAttribute24 | ATTRIBUTE24 | — | — |
| 23 | HdrSupplierAttribute25 | ATTRIBUTE25 | — | — |
| 24 | HdrSupplierAttribute26 | ATTRIBUTE26 | — | — |
| 25 | HdrSupplierAttribute27 | ATTRIBUTE27 | — | — |
| 26 | HdrSupplierAttribute28 | ATTRIBUTE28 | — | — |
| 27 | HdrSupplierAttribute29 | ATTRIBUTE29 | — | — |
| 28 | HdrSupplierAttribute3 | ATTRIBUTE3 | — | — |
| 29 | HdrSupplierAttribute30 | ATTRIBUTE30 | — | — |
| 30 | HdrSupplierAttribute4 | ATTRIBUTE4 | — | — |
| 31 | HdrSupplierAttribute5 | ATTRIBUTE5 | — | — |
| 32 | HdrSupplierAttribute6 | ATTRIBUTE6 | — | — |
| 33 | HdrSupplierAttribute7 | ATTRIBUTE7 | — | — |
| 34 | HdrSupplierAttribute8 | ATTRIBUTE8 | — | — |
| 35 | HdrSupplierAttribute9 | ATTRIBUTE9 | — | — |
| 36 | HdrSupplierAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | HdrSupplierAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | HdrSupplierAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | HdrSupplierAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | HdrSupplierAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | HdrSupplierAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | HdrSupplierAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | HdrSupplierAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | HdrSupplierAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | HdrSupplierAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | HdrSupplierAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | HdrSupplierAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | HdrSupplierAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | HdrSupplierAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | HdrSupplierAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | HdrSupplierAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | HdrSupplierAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | HdrSupplierAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | HdrSupplierAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | HdrSupplierAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | HdrSupplierAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | HdrSupplierAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | HdrSupplierAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | HdrSupplierAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | HdrSupplierAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | HdrSupplierCategoryCode | CATEGORY_CODE | — | — |
| 62 | HdrSupplierCeoName | CEO_NAME | — | — |
| 63 | HdrSupplierCertReasonCode | CERT_REASON_CODE | — | — |
| 64 | HdrSupplierCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | HdrSupplierCity | CITY | — | — |
| 66 | HdrSupplierComments | COMMENTS | — | — |
| 67 | HdrSupplierCountry | COUNTRY | — | — |
| 68 | HdrSupplierCounty | COUNTY | — | — |
| 69 | HdrSupplierCreatedBy | CREATED_BY | — | — |
| 70 | HdrSupplierCreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | HdrSupplierCreationDate | CREATION_DATE | — | — |
| 72 | HdrSupplierCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | HdrSupplierDateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | HdrSupplierDunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | HdrSupplierEmailAddress | EMAIL_ADDRESS | — | — |
| 76 | HdrSupplierEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | HdrSupplierFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | HdrSupplierGender | GENDER | — | — |
| 79 | HdrSupplierGroupType | GROUP_TYPE | — | — |
| 80 | HdrSupplierGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | HdrSupplierHomeCountry | HOME_COUNTRY | — | — |
| 82 | HdrSupplierHqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | HdrSupplierIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | HdrSupplierIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | HdrSupplierInternalFlag | INTERNAL_FLAG | — | — |
| 86 | HdrSupplierJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | HdrSupplierLanguageName | LANGUAGE_NAME | — | — |
| 88 | HdrSupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | HdrSupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 90 | HdrSupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 91 | HdrSupplierMaritalStatus | MARITAL_STATUS | — | — |
| 92 | HdrSupplierMissionStatement | MISSION_STATEMENT | — | — |
| 93 | HdrSupplierNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | HdrSupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | HdrSupplierOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | HdrSupplierPartyId | PARTY_ID | — | — |
| 97 | HdrSupplierPartyName | PARTY_NAME | — | — |
| 98 | HdrSupplierPartyNumber | PARTY_NUMBER | — | — |
| 99 | HdrSupplierPartyType | PARTY_TYPE | — | — |
| 100 | HdrSupplierPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 101 | HdrSupplierPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | HdrSupplierPersonFirstName | PERSON_FIRST_NAME | — | — |
| 103 | HdrSupplierPersonLastName | PERSON_LAST_NAME | — | — |
| 104 | HdrSupplierPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | HdrSupplierPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 106 | HdrSupplierPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | HdrSupplierPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | HdrSupplierPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | HdrSupplierPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | HdrSupplierPersonTitle | PERSON_TITLE | — | — |
| 111 | HdrSupplierPostalCode | POSTAL_CODE | — | — |
| 112 | HdrSupplierPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 113 | HdrSupplierPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 114 | HdrSupplierPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 115 | HdrSupplierPreferredName | PREFERRED_NAME | — | — |
| 116 | HdrSupplierPreferredNameId | PREFERRED_NAME_ID | — | — |
| 117 | HdrSupplierPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 118 | HdrSupplierPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 119 | HdrSupplierPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 120 | HdrSupplierPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 121 | HdrSupplierPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 122 | HdrSupplierPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 123 | HdrSupplierPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 124 | HdrSupplierPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 125 | HdrSupplierPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 126 | HdrSupplierProvince | PROVINCE | — | — |
| 127 | HdrSupplierSalutation | SALUTATION | — | — |
| 128 | HdrSupplierSicCode | SIC_CODE | — | — |
| 129 | HdrSupplierSicCodeType | SIC_CODE_TYPE | — | — |
| 130 | HdrSupplierState | STATE | — | — |
| 131 | HdrSupplierStatus | STATUS | — | — |
| 132 | HdrSupplierThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 133 | HdrSupplierTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 134 | HdrSupplierUrl | URL | — | — |
| 135 | HdrSupplierUserGuid | USER_GUID | — | — |
| 136 | HdrSupplierValidatedFlag | VALIDATED_FLAG | — | — |
| 137 | HdrSupplierYearEstablished | YEAR_ESTABLISHED | — | — |
| 138 | LineSupplierAddress1 | ADDRESS1 | — | — |
| 139 | LineSupplierAddress2 | ADDRESS2 | — | — |
| 140 | LineSupplierAddress3 | ADDRESS3 | — | — |
| 141 | LineSupplierAddress4 | ADDRESS4 | — | — |
| 142 | LineSupplierAnalysisFy | ANALYSIS_FY | — | — |
| 143 | LineSupplierAttribute1 | ATTRIBUTE1 | — | — |
| 144 | LineSupplierAttribute10 | ATTRIBUTE10 | — | — |
| 145 | LineSupplierAttribute11 | ATTRIBUTE11 | — | — |
| 146 | LineSupplierAttribute12 | ATTRIBUTE12 | — | — |
| 147 | LineSupplierAttribute13 | ATTRIBUTE13 | — | — |
| 148 | LineSupplierAttribute14 | ATTRIBUTE14 | — | — |
| 149 | LineSupplierAttribute15 | ATTRIBUTE15 | — | — |
| 150 | LineSupplierAttribute16 | ATTRIBUTE16 | — | — |
| 151 | LineSupplierAttribute17 | ATTRIBUTE17 | — | — |
| 152 | LineSupplierAttribute18 | ATTRIBUTE18 | — | — |
| 153 | LineSupplierAttribute19 | ATTRIBUTE19 | — | — |
| 154 | LineSupplierAttribute2 | ATTRIBUTE2 | — | — |
| 155 | LineSupplierAttribute20 | ATTRIBUTE20 | — | — |
| 156 | LineSupplierAttribute21 | ATTRIBUTE21 | — | — |
| 157 | LineSupplierAttribute22 | ATTRIBUTE22 | — | — |
| 158 | LineSupplierAttribute23 | ATTRIBUTE23 | — | — |
| 159 | LineSupplierAttribute24 | ATTRIBUTE24 | — | — |
| 160 | LineSupplierAttribute25 | ATTRIBUTE25 | — | — |
| 161 | LineSupplierAttribute26 | ATTRIBUTE26 | — | — |
| 162 | LineSupplierAttribute27 | ATTRIBUTE27 | — | — |
| 163 | LineSupplierAttribute28 | ATTRIBUTE28 | — | — |
| 164 | LineSupplierAttribute29 | ATTRIBUTE29 | — | — |
| 165 | LineSupplierAttribute3 | ATTRIBUTE3 | — | — |
| 166 | LineSupplierAttribute30 | ATTRIBUTE30 | — | — |
| 167 | LineSupplierAttribute4 | ATTRIBUTE4 | — | — |
| 168 | LineSupplierAttribute5 | ATTRIBUTE5 | — | — |
| 169 | LineSupplierAttribute6 | ATTRIBUTE6 | — | — |
| 170 | LineSupplierAttribute7 | ATTRIBUTE7 | — | — |
| 171 | LineSupplierAttribute8 | ATTRIBUTE8 | — | — |
| 172 | LineSupplierAttribute9 | ATTRIBUTE9 | — | — |
| 173 | LineSupplierAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 174 | LineSupplierAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 175 | LineSupplierAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 176 | LineSupplierAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 177 | LineSupplierAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 178 | LineSupplierAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 179 | LineSupplierAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 180 | LineSupplierAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 181 | LineSupplierAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 182 | LineSupplierAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 183 | LineSupplierAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 184 | LineSupplierAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 185 | LineSupplierAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 186 | LineSupplierAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 187 | LineSupplierAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 188 | LineSupplierAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 189 | LineSupplierAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 190 | LineSupplierAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 191 | LineSupplierAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 192 | LineSupplierAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 193 | LineSupplierAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 194 | LineSupplierAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 195 | LineSupplierAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 196 | LineSupplierAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 197 | LineSupplierAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 198 | LineSupplierCategoryCode | CATEGORY_CODE | — | — |
| 199 | LineSupplierCeoName | CEO_NAME | — | — |
| 200 | LineSupplierCertReasonCode | CERT_REASON_CODE | — | — |
| 201 | LineSupplierCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 202 | LineSupplierCity | CITY | — | — |
| 203 | LineSupplierComments | COMMENTS | — | — |
| 204 | LineSupplierCountry | COUNTRY | — | — |
| 205 | LineSupplierCounty | COUNTY | — | — |
| 206 | LineSupplierCreatedBy | CREATED_BY | — | — |
| 207 | LineSupplierCreatedByModule | CREATED_BY_MODULE | — | — |
| 208 | LineSupplierCreationDate | CREATION_DATE | — | — |
| 209 | LineSupplierCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 210 | LineSupplierDateOfBirth | DATE_OF_BIRTH | — | — |
| 211 | LineSupplierDunsNumberC | DUNS_NUMBER_C | — | — |
| 212 | LineSupplierEmailAddress | EMAIL_ADDRESS | — | — |
| 213 | LineSupplierEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 214 | LineSupplierFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 215 | LineSupplierGender | GENDER | — | — |
| 216 | LineSupplierGroupType | GROUP_TYPE | — | — |
| 217 | LineSupplierGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 218 | LineSupplierHomeCountry | HOME_COUNTRY | — | — |
| 219 | LineSupplierHqBranchInd | HQ_BRANCH_IND | — | — |
| 220 | LineSupplierIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 221 | LineSupplierIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 222 | LineSupplierInternalFlag | INTERNAL_FLAG | — | — |
| 223 | LineSupplierJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 224 | LineSupplierLanguageName | LANGUAGE_NAME | — | — |
| 225 | LineSupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 226 | LineSupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 227 | LineSupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 228 | LineSupplierMaritalStatus | MARITAL_STATUS | — | — |
| 229 | LineSupplierMissionStatement | MISSION_STATEMENT | — | — |
| 230 | LineSupplierNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 231 | LineSupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 232 | LineSupplierOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 233 | LineSupplierPartyId | PARTY_ID | — | — |
| 234 | LineSupplierPartyName | PARTY_NAME | — | — |
| 235 | LineSupplierPartyNumber | PARTY_NUMBER | — | — |
| 236 | LineSupplierPartyType | PARTY_TYPE | — | — |
| 237 | LineSupplierPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 238 | LineSupplierPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 239 | LineSupplierPersonFirstName | PERSON_FIRST_NAME | — | — |
| 240 | LineSupplierPersonLastName | PERSON_LAST_NAME | — | — |
| 241 | LineSupplierPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 242 | LineSupplierPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 243 | LineSupplierPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 244 | LineSupplierPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 245 | LineSupplierPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 246 | LineSupplierPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 247 | LineSupplierPersonTitle | PERSON_TITLE | — | — |
| 248 | LineSupplierPostalCode | POSTAL_CODE | — | — |
| 249 | LineSupplierPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 250 | LineSupplierPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 251 | LineSupplierPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 252 | LineSupplierPreferredName | PREFERRED_NAME | — | — |
| 253 | LineSupplierPreferredNameId | PREFERRED_NAME_ID | — | — |
| 254 | LineSupplierPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 255 | LineSupplierPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 256 | LineSupplierPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 257 | LineSupplierPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 258 | LineSupplierPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 259 | LineSupplierPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 260 | LineSupplierPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 261 | LineSupplierPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 262 | LineSupplierPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 263 | LineSupplierProvince | PROVINCE | — | — |
| 264 | LineSupplierSalutation | SALUTATION | — | — |
| 265 | LineSupplierSicCode | SIC_CODE | — | — |
| 266 | LineSupplierSicCodeType | SIC_CODE_TYPE | — | — |
| 267 | LineSupplierState | STATE | — | — |
| 268 | LineSupplierStatus | STATUS | — | — |
| 269 | LineSupplierThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 270 | LineSupplierTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 271 | LineSupplierUrl | URL | — | — |
| 272 | LineSupplierUserGuid | USER_GUID | — | — |
| 273 | LineSupplierValidatedFlag | VALIDATED_FLAG | — | — |
| 274 | LineSupplierYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrSupplierSiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | HdrSupplierSiteAddressee | ADDRESSEE | — | — |
| 3 | HdrSupplierSiteAttribute1 | ATTRIBUTE1 | — | — |
| 4 | HdrSupplierSiteAttribute10 | ATTRIBUTE10 | — | — |
| 5 | HdrSupplierSiteAttribute11 | ATTRIBUTE11 | — | — |
| 6 | HdrSupplierSiteAttribute12 | ATTRIBUTE12 | — | — |
| 7 | HdrSupplierSiteAttribute13 | ATTRIBUTE13 | — | — |
| 8 | HdrSupplierSiteAttribute14 | ATTRIBUTE14 | — | — |
| 9 | HdrSupplierSiteAttribute15 | ATTRIBUTE15 | — | — |
| 10 | HdrSupplierSiteAttribute16 | ATTRIBUTE16 | — | — |
| 11 | HdrSupplierSiteAttribute17 | ATTRIBUTE17 | — | — |
| 12 | HdrSupplierSiteAttribute18 | ATTRIBUTE18 | — | — |
| 13 | HdrSupplierSiteAttribute19 | ATTRIBUTE19 | — | — |
| 14 | HdrSupplierSiteAttribute2 | ATTRIBUTE2 | — | — |
| 15 | HdrSupplierSiteAttribute20 | ATTRIBUTE20 | — | — |
| 16 | HdrSupplierSiteAttribute21 | ATTRIBUTE21 | — | — |
| 17 | HdrSupplierSiteAttribute22 | ATTRIBUTE22 | — | — |
| 18 | HdrSupplierSiteAttribute23 | ATTRIBUTE23 | — | — |
| 19 | HdrSupplierSiteAttribute24 | ATTRIBUTE24 | — | — |
| 20 | HdrSupplierSiteAttribute25 | ATTRIBUTE25 | — | — |
| 21 | HdrSupplierSiteAttribute26 | ATTRIBUTE26 | — | — |
| 22 | HdrSupplierSiteAttribute27 | ATTRIBUTE27 | — | — |
| 23 | HdrSupplierSiteAttribute28 | ATTRIBUTE28 | — | — |
| 24 | HdrSupplierSiteAttribute29 | ATTRIBUTE29 | — | — |
| 25 | HdrSupplierSiteAttribute3 | ATTRIBUTE3 | — | — |
| 26 | HdrSupplierSiteAttribute30 | ATTRIBUTE30 | — | — |
| 27 | HdrSupplierSiteAttribute4 | ATTRIBUTE4 | — | — |
| 28 | HdrSupplierSiteAttribute5 | ATTRIBUTE5 | — | — |
| 29 | HdrSupplierSiteAttribute6 | ATTRIBUTE6 | — | — |
| 30 | HdrSupplierSiteAttribute7 | ATTRIBUTE7 | — | — |
| 31 | HdrSupplierSiteAttribute8 | ATTRIBUTE8 | — | — |
| 32 | HdrSupplierSiteAttribute9 | ATTRIBUTE9 | — | — |
| 33 | HdrSupplierSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | HdrSupplierSiteAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | HdrSupplierSiteAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 36 | HdrSupplierSiteAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 37 | HdrSupplierSiteAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 38 | HdrSupplierSiteAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | HdrSupplierSiteAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | HdrSupplierSiteAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | HdrSupplierSiteAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | HdrSupplierSiteAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 43 | HdrSupplierSiteAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 44 | HdrSupplierSiteAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 45 | HdrSupplierSiteAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 46 | HdrSupplierSiteAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | HdrSupplierSiteAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | HdrSupplierSiteAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 49 | HdrSupplierSiteAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 50 | HdrSupplierSiteAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 51 | HdrSupplierSiteAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 52 | HdrSupplierSiteAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 53 | HdrSupplierSiteAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 54 | HdrSupplierSiteAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 55 | HdrSupplierSiteAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 56 | HdrSupplierSiteAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 57 | HdrSupplierSiteAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 58 | HdrSupplierSiteComments | COMMENTS | — | — |
| 59 | HdrSupplierSiteCreatedBy | CREATED_BY | — | — |
| 60 | HdrSupplierSiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 61 | HdrSupplierSiteCreationDate | CREATION_DATE | — | — |
| 62 | HdrSupplierSiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 63 | HdrSupplierSiteEndDateActive | END_DATE_ACTIVE | — | — |
| 64 | HdrSupplierSiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 65 | HdrSupplierSiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 66 | HdrSupplierSiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 67 | HdrSupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 68 | HdrSupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 69 | HdrSupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 70 | HdrSupplierSiteLocationId | LOCATION_ID | — | — |
| 71 | HdrSupplierSiteMailstop | MAILSTOP | — | — |
| 72 | HdrSupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | HdrSupplierSiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 74 | HdrSupplierSiteOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 75 | HdrSupplierSitePartyId | PARTY_ID | — | — |
| 76 | HdrSupplierSitePartyNameDba | PARTY_NAME_DBA | — | — |
| 77 | HdrSupplierSitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 78 | HdrSupplierSitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 79 | HdrSupplierSitePartySiteId | PARTY_SITE_ID | — | — |
| 80 | HdrSupplierSitePartySiteName | PARTY_SITE_NAME | — | — |
| 81 | HdrSupplierSitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 82 | HdrSupplierSitePartySiteType | PARTY_SITE_TYPE | — | — |
| 83 | HdrSupplierSitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 84 | HdrSupplierSiteRelationshipId | RELATIONSHIP_ID | — | — |
| 85 | HdrSupplierSiteStartDateActive | START_DATE_ACTIVE | — | — |
| 86 | HdrSupplierSiteStatus | STATUS | — | — |
| 87 | LineSupplierSiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 88 | LineSupplierSiteAddressee | ADDRESSEE | — | — |
| 89 | LineSupplierSiteAttribute1 | ATTRIBUTE1 | — | — |
| 90 | LineSupplierSiteAttribute10 | ATTRIBUTE10 | — | — |
| 91 | LineSupplierSiteAttribute11 | ATTRIBUTE11 | — | — |
| 92 | LineSupplierSiteAttribute12 | ATTRIBUTE12 | — | — |
| 93 | LineSupplierSiteAttribute13 | ATTRIBUTE13 | — | — |
| 94 | LineSupplierSiteAttribute14 | ATTRIBUTE14 | — | — |
| 95 | LineSupplierSiteAttribute15 | ATTRIBUTE15 | — | — |
| 96 | LineSupplierSiteAttribute16 | ATTRIBUTE16 | — | — |
| 97 | LineSupplierSiteAttribute17 | ATTRIBUTE17 | — | — |
| 98 | LineSupplierSiteAttribute18 | ATTRIBUTE18 | — | — |
| 99 | LineSupplierSiteAttribute19 | ATTRIBUTE19 | — | — |
| 100 | LineSupplierSiteAttribute2 | ATTRIBUTE2 | — | — |
| 101 | LineSupplierSiteAttribute20 | ATTRIBUTE20 | — | — |
| 102 | LineSupplierSiteAttribute21 | ATTRIBUTE21 | — | — |
| 103 | LineSupplierSiteAttribute22 | ATTRIBUTE22 | — | — |
| 104 | LineSupplierSiteAttribute23 | ATTRIBUTE23 | — | — |
| 105 | LineSupplierSiteAttribute24 | ATTRIBUTE24 | — | — |
| 106 | LineSupplierSiteAttribute25 | ATTRIBUTE25 | — | — |
| 107 | LineSupplierSiteAttribute26 | ATTRIBUTE26 | — | — |
| 108 | LineSupplierSiteAttribute27 | ATTRIBUTE27 | — | — |
| 109 | LineSupplierSiteAttribute28 | ATTRIBUTE28 | — | — |
| 110 | LineSupplierSiteAttribute29 | ATTRIBUTE29 | — | — |
| 111 | LineSupplierSiteAttribute3 | ATTRIBUTE3 | — | — |
| 112 | LineSupplierSiteAttribute30 | ATTRIBUTE30 | — | — |
| 113 | LineSupplierSiteAttribute4 | ATTRIBUTE4 | — | — |
| 114 | LineSupplierSiteAttribute5 | ATTRIBUTE5 | — | — |
| 115 | LineSupplierSiteAttribute6 | ATTRIBUTE6 | — | — |
| 116 | LineSupplierSiteAttribute7 | ATTRIBUTE7 | — | — |
| 117 | LineSupplierSiteAttribute8 | ATTRIBUTE8 | — | — |
| 118 | LineSupplierSiteAttribute9 | ATTRIBUTE9 | — | — |
| 119 | LineSupplierSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 120 | LineSupplierSiteAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 121 | LineSupplierSiteAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 122 | LineSupplierSiteAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 123 | LineSupplierSiteAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 124 | LineSupplierSiteAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 125 | LineSupplierSiteAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 126 | LineSupplierSiteAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 127 | LineSupplierSiteAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 128 | LineSupplierSiteAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 129 | LineSupplierSiteAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 130 | LineSupplierSiteAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 131 | LineSupplierSiteAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 132 | LineSupplierSiteAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 133 | LineSupplierSiteAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 134 | LineSupplierSiteAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 135 | LineSupplierSiteAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 136 | LineSupplierSiteAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 137 | LineSupplierSiteAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 138 | LineSupplierSiteAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 139 | LineSupplierSiteAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 140 | LineSupplierSiteAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 141 | LineSupplierSiteAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 142 | LineSupplierSiteAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 143 | LineSupplierSiteAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 144 | LineSupplierSiteComments | COMMENTS | — | — |
| 145 | LineSupplierSiteCreatedBy | CREATED_BY | — | — |
| 146 | LineSupplierSiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 147 | LineSupplierSiteCreationDate | CREATION_DATE | — | — |
| 148 | LineSupplierSiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 149 | LineSupplierSiteEndDateActive | END_DATE_ACTIVE | — | — |
| 150 | LineSupplierSiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 151 | LineSupplierSiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 152 | LineSupplierSiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 153 | LineSupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 154 | LineSupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 155 | LineSupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 156 | LineSupplierSiteLocationId | LOCATION_ID | — | — |
| 157 | LineSupplierSiteMailstop | MAILSTOP | — | — |
| 158 | LineSupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 159 | LineSupplierSiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 160 | LineSupplierSiteOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 161 | LineSupplierSitePartyId | PARTY_ID | — | — |
| 162 | LineSupplierSitePartyNameDba | PARTY_NAME_DBA | — | — |
| 163 | LineSupplierSitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 164 | LineSupplierSitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 165 | LineSupplierSitePartySiteId | PARTY_SITE_ID | — | — |
| 166 | LineSupplierSitePartySiteName | PARTY_SITE_NAME | — | — |
| 167 | LineSupplierSitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 168 | LineSupplierSitePartySiteType | PARTY_SITE_TYPE | — | — |
| 169 | LineSupplierSitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 170 | LineSupplierSiteRelationshipId | RELATIONSHIP_ID | — | — |
| 171 | LineSupplierSiteStartDateActive | START_DATE_ACTIVE | — | — |
| 172 | LineSupplierSiteStatus | STATUS | — | — |

### [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderInvOrgPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | ContractHeaderInvOrgPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |
| 3 | ContractLineShipInvOrgPEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 4 | ContractLineShipInvOrgPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | ContractLineShipInvOrgPEOOrganizationName | ORGANIZATION_NAME | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineUnitOfMeasurePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ContractLineUnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 3 | ContractLineUnitOfMeasurePEOUomCode | UOM_CODE | — | — |

### [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypePEOAgreementEnabledFlag | AGREEMENT_ENABLED_FLAG | — | — |
| 2 | ContractTypePEOAllowLinesFlag | ALLOW_LINES_FLAG | — | — |
| 3 | ContractTypePEOBillingLimitType | BILLING_LIMIT_TYPE | — | — |
| 4 | ContractTypePEOContractClass | CONTRACT_CLASS | — | — |
| 5 | ContractTypePEOContractGroupId | CONTRACT_GROUP_ID | — | — |
| 6 | ContractTypePEOContractLayoutTemplate | CONTRACT_LAYOUT_TEMPLATE | — | — |
| 7 | ContractTypePEOContractTypeCode | CONTRACT_TYPE_CODE | — | — |
| 8 | ContractTypePEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 9 | ContractTypePEOCreatedBy | CREATED_BY | — | — |
| 10 | ContractTypePEOCreationDate | CREATION_DATE | — | — |
| 11 | ContractTypePEODaysToExpiration | DAYS_TO_EXPIRATION | — | — |
| 12 | ContractTypePEODescription | DESCRIPTION | — | ✅ |
| 13 | ContractTypePEOEnableBillingCtrlFlag | ENABLE_BILLING_CTRL_FLAG | — | — |
| 14 | ContractTypePEOEndDate | END_DATE | — | — |
| 15 | ContractTypePEOIntent | INTENT | — | — |
| 16 | ContractTypePEOInterCompanyFlag | INTER_COMPANY_FLAG | — | ✅ |
| 17 | ContractTypePEOInterProjectFlag | INTER_PROJECT_FLAG | — | ✅ |
| 18 | ContractTypePEOInteractionsEnabledFlag | INTERACTIONS_ENABLED_FLAG | — | — |
| 19 | ContractTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ContractTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ContractTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ContractTypePEOLayoutTemplateId | LAYOUT_TEMPLATE_ID | — | — |
| 23 | ContractTypePEOLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 24 | ContractTypePEOLineClass | LINE_CLASS | — | — |
| 25 | ContractTypePEOName | NAME | — | ✅ |
| 26 | ContractTypePEONotifyBeforeExpFlag | NOTIFY_BEFORE_EXP_FLAG | — | — |
| 27 | ContractTypePEONotifyContactRole | NOTIFY_CONTACT_ROLE | — | — |
| 28 | ContractTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | ContractTypePEOPrimaryBuyerRole | PRIMARY_BUYER_ROLE | — | — |
| 30 | ContractTypePEOQclId | QCL_ID | — | — |
| 31 | ContractTypePEORelatedKEnabledFlag | RELATED_K_ENABLED_FLAG | — | — |
| 32 | ContractTypePEORequesterContactRole | REQUESTER_CONTACT_ROLE | — | — |
| 33 | ContractTypePEORisksEnabledFlag | RISKS_ENABLED_FLAG | — | — |
| 34 | ContractTypePEOSetId | SET_ID | — | — |
| 35 | ContractTypePEOSignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | — |
| 36 | ContractTypePEOStartDate | START_DATE | — | — |
| 37 | ContractTypePEOTermsEnabledFlag | TERMS_ENABLED_FLAG | — | — |
| 38 | ContractTypePEOTermsLayoutTemplate | TERMS_LAYOUT_TEMPLATE | — | — |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHdrCommitmentAmount | COMMITMENT_AMOUNT | — | — |
| 2 | ContractHeaderBasePEOAcctRuleId | ACCT_RULE_ID | — | — |
| 3 | ContractHeaderBasePEOAgreedAmt | AGREED_AMOUNT | — | — |
| 4 | ContractHeaderBasePEOAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | ✅ |
| 5 | ContractHeaderBasePEOApTermsId | AP_TERMS_ID | — | — |
| 6 | ContractHeaderBasePEOArInterfaceYn | AR_INTERFACE_YN | — | — |
| 7 | ContractHeaderBasePEOAssigneeId | ASSIGNEE_ID | — | — |
| 8 | ContractHeaderBasePEOAssigneeType | ASSIGNEE_TYPE | — | — |
| 9 | ContractHeaderBasePEOAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | — |
| 10 | ContractHeaderBasePEOBaseContractYn | BASE_CONTRACT_YN | — | — |
| 11 | ContractHeaderBasePEOBillSequence | BILL_SEQUENCE | — | — |
| 12 | ContractHeaderBasePEOBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 13 | ContractHeaderBasePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 14 | ContractHeaderBasePEOBilledAtSource | BILLED_AT_SOURCE | — | — |
| 15 | ContractHeaderBasePEOBilltoLocationId | BILLTO_LOCATION_ID | — | — |
| 16 | ContractHeaderBasePEOBuyOrSell | BUY_OR_SELL | — | — |
| 17 | ContractHeaderBasePEOCancelledAmount | CANCELLED_AMOUNT | — | — |
| 18 | ContractHeaderBasePEOCarrierId | CARRIER_ID | — | — |
| 19 | ContractHeaderBasePEOCommitmentId | COMMITMENT_ID | — | — |
| 20 | ContractHeaderBasePEOContractNumber | CONTRACT_NUMBER | — | ✅ |
| 21 | ContractHeaderBasePEOContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | — |
| 22 | ContractHeaderBasePEOContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 23 | ContractHeaderBasePEOContributionPercent | CONTRIBUTION_PERCENT | — | — |
| 24 | ContractHeaderBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | ContractHeaderBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | ContractHeaderBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 27 | ContractHeaderBasePEOCustPoNumber | CUST_PO_NUMBER | — | — |
| 28 | ContractHeaderBasePEOCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | — |
| 29 | ContractHeaderBasePEODateApproved | DATE_APPROVED | — | ✅ |
| 30 | ContractHeaderBasePEODateNotified | DATE_NOTIFIED | — | — |
| 31 | ContractHeaderBasePEODateSigned | DATE_SIGNED | — | ✅ |
| 32 | ContractHeaderBasePEODateTerminated | DATE_TERMINATED | — | ✅ |
| 33 | ContractHeaderBasePEODatetimeCancelled | DATETIME_CANCELLED | — | ✅ |
| 34 | ContractHeaderBasePEOEndDate | END_DATE | — | ✅ |
| 35 | ContractHeaderBasePEOEstimatedAmount | ESTIMATED_AMOUNT | — | — |
| 36 | ContractHeaderBasePEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 37 | ContractHeaderBasePEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 38 | ContractHeaderBasePEOFob | FOB | — | — |
| 39 | ContractHeaderBasePEOFreightTerms | FREIGHT_TERMS | — | — |
| 40 | ContractHeaderBasePEOHoldBilling | HOLD_BILLING | — | — |
| 41 | ContractHeaderBasePEOHoldReasonCode | HOLD_REASON_CODE | — | ✅ |
| 42 | ContractHeaderBasePEOHoldReasonCodeSetId | HOLD_REASON_CODE_SET_ID | — | ✅ |
| 43 | ContractHeaderBasePEOHoldUntilDate | HOLD_UNTIL_DATE | — | ✅ |
| 44 | ContractHeaderBasePEOId | ID | — | ✅ |
| 45 | ContractHeaderBasePEOInvConvRateDate | INV_CONV_RATE_DATE | — | — |
| 46 | ContractHeaderBasePEOInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | — |
| 47 | ContractHeaderBasePEOInvConvRateType | INV_CONV_RATE_TYPE | — | — |
| 48 | ContractHeaderBasePEOInvOrganizationId | INV_ORGANIZATION_ID | — | — |
| 49 | ContractHeaderBasePEOInvPrepayTrxTypeId | INV_PREPAY_TRX_TYPE_ID | — | — |
| 50 | ContractHeaderBasePEOInvPrintProfile | INV_PRINT_PROFILE | — | — |
| 51 | ContractHeaderBasePEOInvRuleId | INV_RULE_ID | — | — |
| 52 | ContractHeaderBasePEOInvTrxTypeId | INV_TRX_TYPE_ID | — | — |
| 53 | ContractHeaderBasePEOLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 54 | ContractHeaderBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | ContractHeaderBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | ContractHeaderBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | ContractHeaderBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 58 | ContractHeaderBasePEOLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 59 | ContractHeaderBasePEOMajorVersion | MAJOR_VERSION | — | — |
| 60 | ContractHeaderBasePEONetInvoiceFlag | NET_INVOICE_FLAG | — | ✅ |
| 61 | ContractHeaderBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 62 | ContractHeaderBasePEOOrderId | ORDER_ID | — | — |
| 63 | ContractHeaderBasePEOOrderNumber | ORDER_NUMBER | — | — |
| 64 | ContractHeaderBasePEOOrgId | ORG_ID | — | — |
| 65 | ContractHeaderBasePEOOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 66 | ContractHeaderBasePEOOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 67 | ContractHeaderBasePEOOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 68 | ContractHeaderBasePEOOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 69 | ContractHeaderBasePEOOverallRiskCode | OVERALL_RISK_CODE | — | ✅ |
| 70 | ContractHeaderBasePEOOwningOrgId | OWNING_ORG_ID | — | — |
| 71 | ContractHeaderBasePEOPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | — |
| 72 | ContractHeaderBasePEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 73 | ContractHeaderBasePEOPaymentType | PAYMENT_TYPE | — | — |
| 74 | ContractHeaderBasePEOPriceListId | PRICE_LIST_ID | — | — |
| 75 | ContractHeaderBasePEOPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | — |
| 76 | ContractHeaderBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 77 | ContractHeaderBasePEOProgramName | PROGRAM_NAME | — | — |
| 78 | ContractHeaderBasePEOQclId | QCL_ID | — | — |
| 79 | ContractHeaderBasePEORecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 80 | ContractHeaderBasePEORequestId | REQUEST_ID | — | — |
| 81 | ContractHeaderBasePEORevConvRateType | REV_CONV_RATE_TYPE | — | — |
| 82 | ContractHeaderBasePEOShareWithExternalPartyYn | SHARE_WITH_EXTERNAL_PARTY_YN | — | — |
| 83 | ContractHeaderBasePEOShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 84 | ContractHeaderBasePEOShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 85 | ContractHeaderBasePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 86 | ContractHeaderBasePEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 87 | ContractHeaderBasePEOSoldToAcctId | SOLD_TO_ACCT_ID | — | — |
| 88 | ContractHeaderBasePEOSoldToSiteId | SOLD_TO_SITE_ID | — | — |
| 89 | ContractHeaderBasePEOStartDate | START_DATE | — | ✅ |
| 90 | ContractHeaderBasePEOStsCode | STS_CODE | — | ✅ |
| 91 | ContractHeaderBasePEOSummaryTrxYn | SUMMARY_TRX_YN | — | — |
| 92 | ContractHeaderBasePEOSupplierId | SUPPLIER_ID | — | — |
| 93 | ContractHeaderBasePEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 94 | ContractHeaderBasePEOTaskId | TASK_ID | — | — |
| 95 | ContractHeaderBasePEOTaxAmount | TAX_AMOUNT | — | — |
| 96 | ContractHeaderBasePEOTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | ✅ |
| 97 | ContractHeaderBasePEOTemplateUsed | TEMPLATE_USED | — | — |
| 98 | ContractHeaderBasePEOTemplateYn | TEMPLATE_YN | — | — |
| 99 | ContractHeaderBasePEOTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 100 | ContractHeaderBasePEOTrnCode | TRN_CODE | — | — |
| 101 | ContractHeaderBasePEOTrnCodeSetId | TRN_CODE_SET_ID | — | — |
| 102 | ContractHeaderBasePEOUnderAmendVersionFlag | UNDER_AMEND_VERSION_FLAG | — | — |
| 103 | ContractHeaderBasePEOUserStatusCode | USER_STATUS_CODE | — | — |
| 104 | ContractHeaderBasePEOVersionType | VERSION_TYPE | — | — |
| 105 | ContractId | CONTRACT_ID | — | — |

### [[okc_k_headers_tl|OKC_K_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderTranslationPEOCognomen | COGNOMEN | — | ✅ |
| 2 | ContractHeaderTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ContractHeaderTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ContractHeaderTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ContractHeaderTranslationPEOId | ID | — | — |
| 6 | ContractHeaderTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ContractHeaderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContractHeaderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContractHeaderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContractHeaderTranslationPEOMajorVersion | MAJOR_VERSION | — | — |
| 11 | ContractHeaderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ContractHeaderTranslationPEOShortDescription | SHORT_DESCRIPTION | — | — |
| 13 | ContractHeaderTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 14 | ContractHeaderTranslationPEOVersionDescription | VERSION_DESCRIPTION | — | — |
| 15 | ContractHeaderTranslationPEOVersionType | VERSION_TYPE | — | — |

### [[okc_k_inv_rev_summary_v|OKC_K_INV_REV_SUMMARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OKCInvRevSmryContractId | CONTRACT_ID | — | — |
| 2 | OKCInvRevSmryContractLineId | CONTRACT_LINE_ID | — | — |
| 3 | OKCInvRevSmryInvoiced | INVOICED | — | — |
| 4 | OKCInvRevSmryRevenue | REVENUE | — | — |

### [[okc_k_lines_b|OKC_K_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommitLevelCode | COMMIT_LEVEL_CODE | — | — |
| 2 | ContractLineBasePEOAgreedAmt | AGREED_AMT | — | — |
| 3 | ContractLineBasePEOAgreedQty | AGREED_QTY | — | — |
| 4 | ContractLineBasePEOAgreementAmtLimit | AGREEMENT_AMT_LIMIT | — | — |
| 5 | ContractLineBasePEOAgreementPriceLimit | AGREEMENT_PRICE_LIMIT | — | — |
| 6 | ContractLineBasePEOAgreementPriceOverAllwdYn | AGREEMENT_PRICE_OVER_ALLWD_YN | — | — |
| 7 | ContractLineBasePEOAgreementQtyLimit | AGREEMENT_QTY_LIMIT | — | — |
| 8 | ContractLineBasePEOAgreementUnitPrice | AGREEMENT_UNIT_PRICE | — | — |
| 9 | ContractLineBasePEOAtRiskYn | AT_RISK_YN | — | ✅ |
| 10 | ContractLineBasePEOBillPlanId | BILL_PLAN_ID | — | — |
| 11 | ContractLineBasePEOBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 12 | ContractLineBasePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 13 | ContractLineBasePEOBillableFlag | BILLABLE_FLAG | — | — |
| 14 | ContractLineBasePEOCancelledAmount | CANCELLED_AMOUNT | — | — |
| 15 | ContractLineBasePEOCarrierId | CARRIER_ID | — | — |
| 16 | ContractLineBasePEOChrId | CHR_ID | — | — |
| 17 | ContractLineBasePEOCleId | CLE_ID | — | — |
| 18 | ContractLineBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | ContractLineBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | ContractLineBasePEOCreditedAmount | CREDITED_AMOUNT | — | — |
| 21 | ContractLineBasePEOCurrencyCode | CURRENCY_CODE | — | — |
| 22 | ContractLineBasePEOCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 23 | ContractLineBasePEOCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 24 | ContractLineBasePEOCustomerItemNumber | CUSTOMER_ITEM_NUMBER | — | — |
| 25 | ContractLineBasePEODateCancelled | DATE_CANCELLED | — | ✅ |
| 26 | ContractLineBasePEODateTerminated | DATE_TERMINATED | — | ✅ |
| 27 | ContractLineBasePEODeliveryDate | DELIVERY_DATE | — | — |
| 28 | ContractLineBasePEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 29 | ContractLineBasePEODnzChrId | DNZ_CHR_ID | — | — |
| 30 | ContractLineBasePEOEndDate | END_DATE | — | ✅ |
| 31 | ContractLineBasePEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 32 | ContractLineBasePEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 33 | ContractLineBasePEOFixedPriceServiceYn | FIXED_PRICE_SERVICE_YN | — | — |
| 34 | ContractLineBasePEOFobCode | FOB_CODE | — | — |
| 35 | ContractLineBasePEOFreightTermsCode | FREIGHT_TERMS_CODE | — | — |
| 36 | ContractLineBasePEOHoldReasonCode | HOLD_REASON_CODE | — | ✅ |
| 37 | ContractLineBasePEOHoldUntilDate | HOLD_UNTIL_DATE | — | ✅ |
| 38 | ContractLineBasePEOId | ID | 🔑 | ✅ |
| 39 | ContractLineBasePEOJtotObject1Code | JTOT_OBJECT1_CODE | — | — |
| 40 | ContractLineBasePEOLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 41 | ContractLineBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | ContractLineBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 43 | ContractLineBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | ContractLineBasePEOLineAmount | LINE_AMOUNT | — | — |
| 45 | ContractLineBasePEOLineNumber | LINE_NUMBER | — | ✅ |
| 46 | ContractLineBasePEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 47 | ContractLineBasePEOLineValue | LINE_VALUE | — | — |
| 48 | ContractLineBasePEOMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 49 | ContractLineBasePEOMinReleaseAmt | MIN_RELEASE_AMT | — | — |
| 50 | ContractLineBasePEOMinReleaseQty | MIN_RELEASE_QTY | — | — |
| 51 | ContractLineBasePEONspFlag | NSP_FLAG | — | — |
| 52 | ContractLineBasePEONumOfItem | NUM_OF_ITEM | — | — |
| 53 | ContractLineBasePEOObject1Id1 | OBJECT1_ID1 | — | — |
| 54 | ContractLineBasePEOObject1Id2 | OBJECT1_ID2 | — | — |
| 55 | ContractLineBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | ContractLineBasePEOOrderId | ORDER_ID | — | — |
| 57 | ContractLineBasePEOOrderLineId | ORDER_LINE_ID | — | — |
| 58 | ContractLineBasePEOOrderLineNumber | ORDER_LINE_NUMBER | — | — |
| 59 | ContractLineBasePEOOrderNumber | ORDER_NUMBER | — | — |
| 60 | ContractLineBasePEOOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 61 | ContractLineBasePEOOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 62 | ContractLineBasePEOOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 63 | ContractLineBasePEOOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 64 | ContractLineBasePEOOverridenAmount | OVERRIDEN_AMOUNT | — | — |
| 65 | ContractLineBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 66 | ContractLineBasePEOPercentComplete | PERCENT_COMPLETE | — | — |
| 67 | ContractLineBasePEOPriceUnit | PRICE_UNIT | — | — |
| 68 | ContractLineBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 69 | ContractLineBasePEOProgramName | PROGRAM_NAME | — | — |
| 70 | ContractLineBasePEOPurchasingCategoryId | PURCHASING_CATEGORY_ID | — | — |
| 71 | ContractLineBasePEORecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 72 | ContractLineBasePEORecvLocationId | RECV_LOCATION_ID | — | — |
| 73 | ContractLineBasePEORequestId | REQUEST_ID | — | — |
| 74 | ContractLineBasePEORevenuePlanId | REVENUE_PLAN_ID | — | — |
| 75 | ContractLineBasePEOShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 76 | ContractLineBasePEOShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 77 | ContractLineBasePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 78 | ContractLineBasePEOShiptoLocationId | RECV_LOCATION_ID | — | — |
| 79 | ContractLineBasePEOSourceCodeClass | SOURCE_CODE_CLASS | — | — |
| 80 | ContractLineBasePEOStartDate | START_DATE | — | ✅ |
| 81 | ContractLineBasePEOStsCode | STS_CODE | — | ✅ |
| 82 | ContractLineBasePEOSupplierId | SUPPLIER_ID | — | — |
| 83 | ContractLineBasePEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 84 | ContractLineBasePEOSuppressedAmount | SUPPRESSED_AMOUNT | — | — |
| 85 | ContractLineBasePEOTaxAmount | TAX_AMOUNT | — | — |
| 86 | ContractLineBasePEOTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | ✅ |
| 87 | ContractLineBasePEOTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 88 | ContractLineBasePEOTrnCode | TRN_CODE | — | — |
| 89 | ContractLineBasePEOUnbilledTerminatedAmont | UNBILLED_TERMINATED_AMONT | — | — |
| 90 | ContractLineBasePEOUndefLineTotal | UNDEF_LINE_TOTAL | — | — |
| 91 | ContractLineBasePEOUndefLineValue | UNDEF_LINE_VALUE | — | — |
| 92 | ContractLineBasePEOUndefUnitPrice | UNDEF_UNIT_PRICE | — | — |
| 93 | ContractLineBasePEOUomCode | UOM_CODE | — | ✅ |
| 94 | ContractLineBasePEOVersionType | VERSION_TYPE | — | — |
| 95 | OkcLnBasePEOHoldReasonCodeSetId | HOLD_REASON_CODE_SET_ID | — | — |
| 96 | OkcLnBasePEOTrnCodeSetId | TRN_CODE_SET_ID | — | — |

### [[okc_k_lines_tl|OKC_K_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineTranslationPEOCognomen | COGNOMEN | — | — |
| 2 | ContractLineTranslationPEOComments | COMMENTS | — | — |
| 3 | ContractLineTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | ContractLineTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | ContractLineTranslationPEOId | ID | — | — |
| 6 | ContractLineTranslationPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 7 | ContractLineTranslationPEOItemName | ITEM_NAME | — | ✅ |
| 8 | ContractLineTranslationPEOLanguage | LANGUAGE | — | — |
| 9 | ContractLineTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ContractLineTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ContractLineTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ContractLineTranslationPEOLineDescription | LINE_DESCRIPTION | — | — |
| 13 | ContractLineTranslationPEOLineName | LINE_NAME | — | — |
| 14 | ContractLineTranslationPEOLineReference | LINE_REFERENCE | — | — |
| 15 | ContractLineTranslationPEOMajorVersion | MAJOR_VERSION | — | — |
| 16 | ContractLineTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ContractLineTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 18 | ContractLineTranslationPEOVersionType | VERSION_TYPE | — | — |

### [[okc_line_types_vl|OKC_LINE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLineTypePEODescription | DESCRIPTION | — | ✅ |
| 2 | ContractLineTypePEOLineTypeId | LINE_TYPE_ID | — | — |
| 3 | ContractLineTypePEOName | NAME | — | ✅ |

### [[pjb_bill_plans_vl|PJB_BILL_PLANS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLinePjbBillPlanPEOBillPlanId | BILL_PLAN_ID | — | — |
| 2 | ContractLinePjbBillPlanPEOBillPlanName | BILL_PLAN_NAME | — | ✅ |
| 3 | ContractLinePjbBillPlanPEOInvoiceCurrencyOptCode | INVOICE_CURRENCY_OPT_CODE | — | ✅ |
| 4 | ContractLinePjbBillPlanPEOMajorVersion | MAJOR_VERSION | — | — |
| 5 | ContractLinePjbBillPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | ContractLinePjbBillPlanPEOOnHoldFlag | ON_HOLD_FLAG | — | ✅ |
| 7 | ContractLinePjbRevenuePlanPEBillPlanId | BILL_PLAN_ID | — | — |
| 8 | ContractLinePjbRevenuePlanPEBillPlanName | BILL_PLAN_NAME | — | ✅ |
| 9 | ContractLinePjbRevenuePlanPEMajorVersion | MAJOR_VERSION | — | — |
| 10 | ContractLinePjbRevenuePlanPEObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ContractLinePjbRevenuePlanPEOnHoldFlag | ON_HOLD_FLAG | — | ✅ |
| 12 | DocNumber | DOC_NUMBER | — | ✅ |
| 13 | LocFlag | LOC_FLAG | — | ✅ |
| 14 | PjbBillPlanBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 15 | PjbBillPlanBillToCustAcctId | BILL_TO_CUST_ACCT_ID | — | — |
| 16 | PjbBillPlanBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 17 | PjbBillPlanOrganizationId | ORGANIZATION_ID | — | — |
| 18 | PjbBillPlanPaymentTermId | PAYMENT_TERM_ID | — | — |
| 19 | ReportTypeCode | REPORT_TYPE_CODE | — | ✅ |

### [[pjb_clin_internal_attributes|PJB_CLIN_INTERNAL_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClinInternalAttributesPEOContractLineId | CONTRACT_LINE_ID | — | — |
| 2 | ClinInternalAttributesPEOExpOrgSource | EXP_ORG_SOURCE | — | ✅ |
| 3 | ClinInternalAttributesPEOExpTypeOrigEiFlag | EXP_TYPE_ORIG_EI_FLAG | — | ✅ |
| 4 | ClinInternalAttributesPEOExpenditureOrgId | EXPENDITURE_ORG_ID | — | — |
| 5 | ClinInternalAttributesPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 6 | ClinInternalAttributesPEOMajorVersion | MAJOR_VERSION | — | — |
| 7 | ClinInternalAttributesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ClinInternalAttributesPEOProviderBusinessUnitId | PROVIDER_BUSINESS_UNIT_ID | — | — |
| 9 | ClinInternalAttributesPEORcvrBusinessUnitId | RCVR_BUSINESS_UNIT_ID | — | — |
| 10 | ClinInternalAttributesPEORcvrSetupCode | RCVR_SETUP_CODE | — | ✅ |
| 11 | ClinInternalAttributesPEOReceiverProjectId | RECEIVER_PROJECT_ID | — | — |
| 12 | ClinInternalAttributesPEOReceiverTaskId | RECEIVER_TASK_ID | — | — |

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 2 | ExpenditureTypeTranslationPEOExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 3 | ExpenditureTypeTranslationPEOLanguage | LANGUAGE | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 2 | ProjectBasePEOSegment1 | SEGMENT1 | — | ✅ |

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ProjectTranslationPEOName | NAME | — | ✅ |
| 3 | ProjectTranslationPEOProjectId | PROJECT_ID | — | — |

### [[pjf_proj_elements_b|PJF_PROJ_ELEMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureBasePEOElementNumber | ELEMENT_NUMBER | — | ✅ |
| 2 | TaskStructureBasePEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[pjf_proj_elements_tl|PJF_PROJ_ELEMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStructureTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | TaskStructureTranslationPEOName | NAME | — | ✅ |
| 3 | TaskStructureTranslationPEOProjElementId | PROJ_ELEMENT_ID | — | — |

### [[qsc_pricebook_headers_vl|QSC_PRICEBOOK_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrPriceBookHeaderName | NAME | — | — |
| 2 | HdrPriceBookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | HdrPriceBookPricebookId | PRICEBOOK_ID | — | — |
| 4 | LinePriceBookHeaderName | NAME | — | — |
| 5 | LinePriceBookObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | LinePricebookId | PRICEBOOK_ID | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderLegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | ContractHeaderLegalEntityPEOName | NAME | — | ✅ |
| 3 | ContractHeaderLegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 5 | LegalEntityPEOName | NAME | — | ✅ |
| 6 | LegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zx_exemptions_v|ZX_EXEMPTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OKCHDRTAXEXMPeoMeaning | MEANING | — | — |
| 2 | OKCLnExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 3 | OKCLnTaxExmptMeaning | MEANING | — | — |
| 4 | OkcHdrExemptCertNo | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 5 | OkcHdrExemptReasonCode | EXEMPT_REASON_CODE | — | — |
| 6 | OkcHdrTaxExemptionId | TAX_EXEMPTION_ID | — | — |
| 7 | OkcLnExemptCertNo | EXEMPT_CERTIFICATE_NUMBER | — | — |
| 8 | OkcLnTaxExemptionId | TAX_EXEMPTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
