---
id: DOC-OTHER-PVO-ItemFact
doc_type: system-doc
title: "ItemFact — PVO Cross-Module"
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
  - ItemFact
  - itemfact
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemFact

## 📌 Visão Geral

View Object para extração BICC de dados de Item Fact. Acessa as tabelas: EGP_ITEM_CATEGORIES, EGP_ITEM_REVISIONS_B_V, EGP_ITEM_REVISIONS_TL_V (+3).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemFact`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 401 | 6 | 2 | 29 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_categories|EGP_ITEM_CATEGORIES]] — 15 atributos (3 BICC)
- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 27 atributos (6 BICC)
- [[egp_item_revisions_tl_v|EGP_ITEM_REVISIONS_TL_V]] — 10 atributos (3 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 333 atributos (2 PKs, 13 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 12 atributos (4 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos

---

## ⚙️ Atributos

### [[egp_item_categories|EGP_ITEM_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryId | CATEGORY_ID | — | ✅ |
| 2 | CategorySetId | CATEGORY_SET_ID | — | ✅ |
| 3 | ItemCategoryPEOCreatedBy | CREATED_BY | — | — |
| 4 | ItemCategoryPEOCreationDate | CREATION_DATE | — | — |
| 5 | ItemCategoryPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 6 | ItemCategoryPEOItemCategoryAssignmentId | ITEM_CATEGORY_ASSIGNMENT_ID | — | — |
| 7 | ItemCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ItemCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ItemCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ItemCategoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ItemCategoryPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 13 | ItemCategoryPEOProgramName | PROGRAM_NAME | — | — |
| 14 | ItemCategoryPEORequestId | REQUEST_ID | — | — |
| 15 | ItemCategoryPEOSequenceNumber | SEQUENCE_NUMBER | — | — |

### [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromRevisionPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromRevisionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 3 | CreatedFromRevisionPEORevision | REVISION | — | — |
| 4 | CreatedFromRevisionPEORevisionId | REVISION_ID | — | — |
| 5 | ItemRevisionBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 6 | ItemRevisionBasePEOCreatedBy | CREATED_BY | — | — |
| 7 | ItemRevisionBasePEOCreationDate | CREATION_DATE | — | — |
| 8 | ItemRevisionBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 9 | ItemRevisionBasePEODescription | DESCRIPTION | — | — |
| 10 | ItemRevisionBasePEOEcnInitiationDate | ECN_INITIATION_DATE | — | — |
| 11 | ItemRevisionBasePEOEffectivityDate | EFFECTIVITY_DATE | — | ✅ |
| 12 | ItemRevisionBasePEOEndEffectivityDate | END_EFFECTIVITY_DATE | — | ✅ |
| 13 | ItemRevisionBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 14 | ItemRevisionBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 15 | ItemRevisionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 16 | ItemRevisionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 17 | ItemRevisionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | ItemRevisionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | ItemRevisionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | ItemRevisionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ItemRevisionBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 22 | ItemRevisionBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 23 | ItemRevisionBasePEOProgramName | PROGRAM_NAME | — | — |
| 24 | ItemRevisionBasePEORequestId | REQUEST_ID | — | — |
| 25 | ItemRevisionBasePEORevision | REVISION | — | ✅ |
| 26 | ItemRevisionBasePEORevisionId | REVISION_ID | — | — |
| 27 | ItemRevisionBasePEORevisionReason | REVISION_REASON | — | ✅ |

### [[egp_item_revisions_tl_v|EGP_ITEM_REVISIONS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRevisionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ItemRevisionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ItemRevisionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemRevisionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ItemRevisionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ItemRevisionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ItemRevisionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ItemRevisionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ItemRevisionTranslationPEORevisionId | REVISION_ID | — | — |
| 10 | ItemRevisionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 2 | ItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 3 | ItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 4 | ItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 5 | ItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 6 | ItemBasePEOAcdType | ACD_TYPE | — | ✅ |
| 7 | ItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 8 | ItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 9 | ItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 10 | ItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 11 | ItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 12 | ItemBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 13 | ItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 14 | ItemBasePEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 15 | ItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 16 | ItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 17 | ItemBasePEOAtpFlag | ATP_FLAG | — | — |
| 18 | ItemBasePEOAtpRuleId | ATP_RULE_ID | — | — |
| 19 | ItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 20 | ItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 21 | ItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 22 | ItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 23 | ItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 24 | ItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 25 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 26 | ItemBasePEOBomItemType | BOM_ITEM_TYPE | — | — |
| 27 | ItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 28 | ItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 29 | ItemBasePEOBuyerId | BUYER_ID | — | — |
| 30 | ItemBasePEOCarryingCost | CARRYING_COST | — | — |
| 31 | ItemBasePEOCasNumber | CAS_NUMBER | — | — |
| 32 | ItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 33 | ItemBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 34 | ItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 35 | ItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 36 | ItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 37 | ItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 38 | ItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 39 | ItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 40 | ItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 41 | ItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 42 | ItemBasePEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 43 | ItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | — |
| 44 | ItemBasePEOConfigMatch | CONFIG_MATCH | — | — |
| 45 | ItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 46 | ItemBasePEOConfigOrgs | CONFIG_ORGS | — | — |
| 47 | ItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 48 | ItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 49 | ItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 50 | ItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 51 | ItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 52 | ItemBasePEOConvergence | CONVERGENCE | — | — |
| 53 | ItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 54 | ItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 55 | ItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 56 | ItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | — |
| 57 | ItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | — |
| 58 | ItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 59 | ItemBasePEOCreatedBy | CREATED_BY | — | — |
| 60 | ItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | — |
| 61 | ItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | — |
| 62 | ItemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 63 | ItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 64 | ItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 65 | ItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 66 | ItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 67 | ItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 68 | ItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 69 | ItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 70 | ItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 71 | ItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 72 | ItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 73 | ItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 74 | ItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 75 | ItemBasePEODaysOfCover | DAYS_OF_COVER | — | — |
| 76 | ItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 77 | ItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 78 | ItemBasePEODefaultGrade | DEFAULT_GRADE | — | — |
| 79 | ItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 80 | ItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 81 | ItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 82 | ItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 83 | ItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 84 | ItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 85 | ItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 86 | ItemBasePEODemandPeriod | DEMAND_PERIOD | — | — |
| 87 | ItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 88 | ItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 89 | ItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 90 | ItemBasePEODivergence | DIVERGENCE | — | — |
| 91 | ItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 92 | ItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 93 | ItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | ✅ |
| 94 | ItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 95 | ItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 96 | ItemBasePEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 97 | ItemBasePEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 98 | ItemBasePEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 99 | ItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 100 | ItemBasePEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 101 | ItemBasePEOEamItemType | EAM_ITEM_TYPE | — | — |
| 102 | ItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 103 | ItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 104 | ItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 105 | ItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | — |
| 106 | ItemBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 107 | ItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 108 | ItemBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 109 | ItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 110 | ItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 111 | ItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 112 | ItemBasePEOEventFlag | EVENT_FLAG | — | — |
| 113 | ItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 114 | ItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 115 | ItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 116 | ItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 117 | ItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 118 | ItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 119 | ItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 120 | ItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 121 | ItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 122 | ItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 123 | ItemBasePEOForecastHorizon | FORECAST_HORIZON | — | — |
| 124 | ItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | — |
| 125 | ItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 126 | ItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 127 | ItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | — |
| 128 | ItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 129 | ItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 130 | ItemBasePEOHoldDays | HOLD_DAYS | — | — |
| 131 | ItemBasePEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 132 | ItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 133 | ItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 134 | ItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 135 | ItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 136 | ItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 137 | ItemBasePEOInternalVolume | INTERNAL_VOLUME | — | — |
| 138 | ItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 139 | ItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 140 | ItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 141 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 142 | ItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 143 | ItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 144 | ItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 145 | ItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 146 | ItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 147 | ItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 148 | ItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 149 | ItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 150 | ItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 151 | ItemBasePEOItemDefinitionOrgId | ITEM_DEFINITION_ORG_ID | — | — |
| 152 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 153 | ItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | — |
| 154 | ItemBasePEOItemType | ITEM_TYPE | — | — |
| 155 | ItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 156 | ItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 157 | ItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 158 | ItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 159 | ItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 160 | ItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 161 | ItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 162 | ItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 163 | ItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 164 | ItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 165 | ItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 166 | ItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 167 | ItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 168 | ItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 169 | ItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 170 | ItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 171 | ItemBasePEOMarketPrice | MARKET_PRICE | — | — |
| 172 | ItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 173 | ItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 174 | ItemBasePEOMaturityDays | MATURITY_DAYS | — | — |
| 175 | ItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 176 | ItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 177 | ItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 178 | ItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 179 | ItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 180 | ItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 181 | ItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 182 | ItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 183 | ItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 184 | ItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 185 | ItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 186 | ItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 187 | ItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 188 | ItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 189 | ItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 190 | ItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 191 | ItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | ✅ |
| 192 | ItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 193 | ItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 194 | ItemBasePEOOrderCost | ORDER_COST | — | — |
| 195 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | — |
| 196 | ItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 197 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 198 | ItemBasePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 199 | ItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | — |
| 200 | ItemBasePEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 201 | ItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 202 | ItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 203 | ItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 204 | ItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 205 | ItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 206 | ItemBasePEOPackagingStringId | PACKAGING_STRING_ID | — | — |
| 207 | ItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 208 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | — |
| 209 | ItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 210 | ItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 211 | ItemBasePEOPickingRuleId | PICKING_RULE_ID | — | — |
| 212 | ItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 213 | ItemBasePEOPlannerCode | PLANNER_CODE | — | — |
| 214 | ItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 215 | ItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 216 | ItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 217 | ItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 218 | ItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 219 | ItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 220 | ItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 221 | ItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 222 | ItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 223 | ItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 224 | ItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 225 | ItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 226 | ItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 227 | ItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 228 | ItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 229 | ItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 230 | ItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 231 | ItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 232 | ItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 233 | ItemBasePEOProgramName | PROGRAM_NAME | — | — |
| 234 | ItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 235 | ItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 236 | ItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 237 | ItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 238 | ItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 239 | ItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 240 | ItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 241 | ItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 242 | ItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 243 | ItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 244 | ItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 245 | ItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 246 | ItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 247 | ItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 248 | ItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 249 | ItemBasePEORepairProgram | REPAIR_PROGRAM | — | — |
| 250 | ItemBasePEORepairTransactionCode | REPAIR_TRANSACTION_CODE | — | — |
| 251 | ItemBasePEORepairYield | REPAIR_YIELD | — | — |
| 252 | ItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 253 | ItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 254 | ItemBasePEORequestId | REQUEST_ID | — | — |
| 255 | ItemBasePEOReservableType | RESERVABLE_TYPE | — | — |
| 256 | ItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 257 | ItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 258 | ItemBasePEORetestInterval | RETEST_INTERVAL | — | — |
| 259 | ItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 260 | ItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 261 | ItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 262 | ItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 263 | ItemBasePEORoundingFactor | ROUNDING_FACTOR | — | — |
| 264 | ItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 265 | ItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 266 | ItemBasePEOSalesAccount | SALES_ACCOUNT | — | — |
| 267 | ItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 268 | ItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 269 | ItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 270 | ItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 271 | ItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 272 | ItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 273 | ItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 274 | ItemBasePEOServiceDuration | SERVICE_DURATION | — | — |
| 275 | ItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 276 | ItemBasePEOServiceStartingDelay | SERVICE_START_DELAY | — | — |
| 277 | ItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 278 | ItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 279 | ItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 280 | ItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 281 | ItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 282 | ItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 283 | ItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 284 | ItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 285 | ItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 286 | ItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 287 | ItemBasePEOSourceType | SOURCE_TYPE | — | — |
| 288 | ItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 289 | ItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 290 | ItemBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 291 | ItemBasePEOStdLotSize | STD_LOT_SIZE | — | — |
| 292 | ItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 293 | ItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 294 | ItemBasePEOStyleItemId | STYLE_ITEM_ID | — | — |
| 295 | ItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 296 | ItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 297 | ItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 298 | ItemBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 299 | ItemBasePEOTaxCode | TAX_CODE | — | — |
| 300 | ItemBasePEOTaxableFlag | TAXABLE_FLAG | — | — |
| 301 | ItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 302 | ItemBasePEOTemplateName | ITEM_NUMBER | — | — |
| 303 | ItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 304 | ItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 305 | ItemBasePEOUnNumberId | UN_NUMBER_ID | — | — |
| 306 | ItemBasePEOUnderCompletionToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | — |
| 307 | ItemBasePEOUnderCompletionToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | — |
| 308 | ItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 309 | ItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 310 | ItemBasePEOUnitHeight | UNIT_HEIGHT | — | — |
| 311 | ItemBasePEOUnitLength | UNIT_LENGTH | — | — |
| 312 | ItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 313 | ItemBasePEOUnitVolume | UNIT_VOLUME | — | — |
| 314 | ItemBasePEOUnitWeight | UNIT_WEIGHT | — | — |
| 315 | ItemBasePEOUnitWidth | UNIT_WIDTH | — | — |
| 316 | ItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 317 | ItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 318 | ItemBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 319 | ItemBasePEOVersionId | VERSION_ID | — | — |
| 320 | ItemBasePEOVersionStartDate | VERSION_START_DATE | — | — |
| 321 | ItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 322 | ItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 323 | ItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 324 | ItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 325 | ItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 326 | ItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 327 | ItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 328 | ItemBasePEOWebStatus | WEB_STATUS | — | — |
| 329 | ItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 330 | ItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 331 | ItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 332 | ItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |
| 333 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ItemTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 5 | ItemTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | ItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 10 | ItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ItemTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromItemPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | CreatedFromItemPEOItemNumber | ITEM_NUMBER | — | — |
| 4 | CreatedFromItemPEOOrganizationId | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
