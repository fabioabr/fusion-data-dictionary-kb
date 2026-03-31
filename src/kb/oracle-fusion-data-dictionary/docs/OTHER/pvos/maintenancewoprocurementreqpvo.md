---
id: DOC-OTHER-PVO-MaintenanceWOProcurementReqPVO
doc_type: system-doc
title: "MaintenanceWOProcurementReqPVO — PVO Cross-Module"
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
  - MaintenanceWOProcurementReqPVO
  - maintenancewoprocurementreqpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWOProcurementReqPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance WOProcurement Req. Acessa as tabelas: EGP_CATEGORIES_VL, EGP_SYSTEM_ITEMS_B_V, POR_REQUISITION_HEADERS_ALL (+6).

**Caminho:** `FscmTopModelAM.WorkOrderAM.MaintenanceWOProcurementReqPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 759 | 9 | 1 | 47 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_vl|EGP_CATEGORIES_VL]] — 21 atributos (3 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 308 atributos (8 BICC)
- [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]] — 49 atributos (6 BICC)
- [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]] — 177 atributos (23 BICC)
- [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]] — 38 atributos (1 PKs, 4 BICC)
- [[po_line_types_vl|PO_LINE_TYPES_VL]] — 23 atributos (1 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 96 atributos (1 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 43 atributos (1 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 4 atributos

---

## ⚙️ Atributos

### [[egp_categories_vl|EGP_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryPEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | CategoryPEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | CategoryPEOCategoryId | CATEGORY_ID | — | ✅ |
| 4 | CategoryPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 5 | CategoryPEOCreatedBy | CREATED_BY | — | — |
| 6 | CategoryPEOCreationDate | CREATION_DATE | — | — |
| 7 | CategoryPEODescription | DESCRIPTION | — | — |
| 8 | CategoryPEOEnabledFlag | ENABLED_FLAG | — | — |
| 9 | CategoryPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | CategoryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | CategoryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | CategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | CategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | CategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | CategoryPEORequestId | REQUEST_ID | — | — |
| 17 | CategoryPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 18 | CategoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 19 | CategoryPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 20 | CategoryPEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 21 | CategoryPEOWebStatus | WEB_STATUS | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | InventoryItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | InventoryItemBasePEOAcdType | ACD_TYPE | — | — |
| 4 | InventoryItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 5 | InventoryItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 6 | InventoryItemBasePEOAllowMaintenanceAssetFlag | ALLOW_MAINTENANCE_ASSET_FLAG | — | — |
| 7 | InventoryItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 8 | InventoryItemBasePEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | — |
| 9 | InventoryItemBasePEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | — |
| 10 | InventoryItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 11 | InventoryItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 12 | InventoryItemBasePEOApprovalStatus | APPROVAL_STATUS | — | — |
| 13 | InventoryItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 14 | InventoryItemBasePEOAssetClass | ASSET_CLASS | — | — |
| 15 | InventoryItemBasePEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | — |
| 16 | InventoryItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 17 | InventoryItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 18 | InventoryItemBasePEOAtpFlag | ATP_FLAG | — | — |
| 19 | InventoryItemBasePEOAtpRuleId | ATP_RULE_ID | — | — |
| 20 | InventoryItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 21 | InventoryItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 22 | InventoryItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 23 | InventoryItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 24 | InventoryItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 25 | InventoryItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 26 | InventoryItemBasePEOBomItemType | BOM_ITEM_TYPE | — | — |
| 27 | InventoryItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 28 | InventoryItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 29 | InventoryItemBasePEOCarryingCost | CARRYING_COST | — | — |
| 30 | InventoryItemBasePEOCasNumber | CAS_NUMBER | — | — |
| 31 | InventoryItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 32 | InventoryItemBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 33 | InventoryItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 34 | InventoryItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 35 | InventoryItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 36 | InventoryItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 37 | InventoryItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 38 | InventoryItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 39 | InventoryItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 40 | InventoryItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 41 | InventoryItemBasePEOCompletenessScore | COMPLETENESS_SCORE | — | — |
| 42 | InventoryItemBasePEOConfigMatch | CONFIG_MATCH | — | — |
| 43 | InventoryItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 44 | InventoryItemBasePEOConfigOrgs | CONFIG_ORGS | — | — |
| 45 | InventoryItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 46 | InventoryItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 47 | InventoryItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 48 | InventoryItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 49 | InventoryItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 50 | InventoryItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 51 | InventoryItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 52 | InventoryItemBasePEOCreatedBy | CREATED_BY | — | — |
| 53 | InventoryItemBasePEOCreationDate | CREATION_DATE | — | — |
| 54 | InventoryItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 55 | InventoryItemBasePEOCssEnabledFlag | CSS_ENABLED_FLAG | — | — |
| 56 | InventoryItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 57 | InventoryItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 58 | InventoryItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 59 | InventoryItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 60 | InventoryItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 61 | InventoryItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 62 | InventoryItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 63 | InventoryItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 64 | InventoryItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 65 | InventoryItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 66 | InventoryItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 67 | InventoryItemBasePEODaysOfCover | DAYS_OF_COVER | — | — |
| 68 | InventoryItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 69 | InventoryItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 70 | InventoryItemBasePEODefaultGrade | DEFAULT_GRADE | — | — |
| 71 | InventoryItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 72 | InventoryItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 73 | InventoryItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 74 | InventoryItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 75 | InventoryItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 76 | InventoryItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 77 | InventoryItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 78 | InventoryItemBasePEODemandPeriod | DEMAND_PERIOD | — | — |
| 79 | InventoryItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 80 | InventoryItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 81 | InventoryItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 82 | InventoryItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 83 | InventoryItemBasePEODqRequiredFlag | DQ_REQUIRED_FLAG | — | — |
| 84 | InventoryItemBasePEODqSemanticKey | DQ_SEMANTIC_KEY | — | — |
| 85 | InventoryItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 86 | InventoryItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | — |
| 87 | InventoryItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | ✅ |
| 88 | InventoryItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | ✅ |
| 89 | InventoryItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 90 | InventoryItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 91 | InventoryItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 92 | InventoryItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 93 | InventoryItemBasePEOEnableGenealogyTrackingFlag | ENABLE_GENEALOGY_TRACKING_FLAG | — | — |
| 94 | InventoryItemBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 95 | InventoryItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 96 | InventoryItemBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 97 | InventoryItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 98 | InventoryItemBasePEOEngineeredItemFlag | ENGINEERED_ITEM_FLAG | — | — |
| 99 | InventoryItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 100 | InventoryItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 101 | InventoryItemBasePEOEventFlag | EVENT_FLAG | — | — |
| 102 | InventoryItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 103 | InventoryItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 104 | InventoryItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 105 | InventoryItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 106 | InventoryItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 107 | InventoryItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 108 | InventoryItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 109 | InventoryItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 110 | InventoryItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 111 | InventoryItemBasePEOForcePurchaseLeadTimeFlag | FORCE_PURCHASE_LEAD_TIME_FLAG | — | — |
| 112 | InventoryItemBasePEOForecastHorizon | FORECAST_HORIZON | — | — |
| 113 | InventoryItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | — |
| 114 | InventoryItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 115 | InventoryItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 116 | InventoryItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 117 | InventoryItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 118 | InventoryItemBasePEOHoldDays | HOLD_DAYS | — | — |
| 119 | InventoryItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 120 | InventoryItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 121 | InventoryItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 122 | InventoryItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 123 | InventoryItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 124 | InventoryItemBasePEOInternalVolume | INTERNAL_VOLUME | — | — |
| 125 | InventoryItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 126 | InventoryItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 127 | InventoryItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 128 | InventoryItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 129 | InventoryItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 130 | InventoryItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 131 | InventoryItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 132 | InventoryItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 133 | InventoryItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 134 | InventoryItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 135 | InventoryItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 136 | InventoryItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 137 | InventoryItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 138 | InventoryItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 139 | InventoryItemBasePEOItemType | ITEM_TYPE | — | — |
| 140 | InventoryItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 141 | InventoryItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 142 | InventoryItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 143 | InventoryItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 144 | InventoryItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 145 | InventoryItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 146 | InventoryItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 147 | InventoryItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 148 | InventoryItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 149 | InventoryItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 150 | InventoryItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 151 | InventoryItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 152 | InventoryItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 153 | InventoryItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 154 | InventoryItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 155 | InventoryItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 156 | InventoryItemBasePEOMarketPrice | MARKET_PRICE | — | — |
| 157 | InventoryItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 158 | InventoryItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 159 | InventoryItemBasePEOMaturityDays | MATURITY_DAYS | — | — |
| 160 | InventoryItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 161 | InventoryItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 162 | InventoryItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 163 | InventoryItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 164 | InventoryItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 165 | InventoryItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 166 | InventoryItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 167 | InventoryItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 168 | InventoryItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 169 | InventoryItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 170 | InventoryItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 171 | InventoryItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 172 | InventoryItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 173 | InventoryItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 174 | InventoryItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 175 | InventoryItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 176 | InventoryItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 177 | InventoryItemBasePEOOrderCost | ORDER_COST | — | — |
| 178 | InventoryItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 179 | InventoryItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 180 | InventoryItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 181 | InventoryItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 182 | InventoryItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 183 | InventoryItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 184 | InventoryItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 185 | InventoryItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 186 | InventoryItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 187 | InventoryItemBasePEOPickingRuleId | PICKING_RULE_ID | — | — |
| 188 | InventoryItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 189 | InventoryItemBasePEOPlannerCode | PLANNER_CODE | — | — |
| 190 | InventoryItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 191 | InventoryItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 192 | InventoryItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 193 | InventoryItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 194 | InventoryItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 195 | InventoryItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 196 | InventoryItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 197 | InventoryItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 198 | InventoryItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 199 | InventoryItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 200 | InventoryItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 201 | InventoryItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 202 | InventoryItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 203 | InventoryItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 204 | InventoryItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 205 | InventoryItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 206 | InventoryItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 207 | InventoryItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 208 | InventoryItemBasePEOProgramName | PROGRAM_NAME | — | — |
| 209 | InventoryItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 210 | InventoryItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 211 | InventoryItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 212 | InventoryItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 213 | InventoryItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 214 | InventoryItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 215 | InventoryItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 216 | InventoryItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 217 | InventoryItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 218 | InventoryItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 219 | InventoryItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 220 | InventoryItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 221 | InventoryItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 222 | InventoryItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 223 | InventoryItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 224 | InventoryItemBasePEORepairProgram | REPAIR_PROGRAM | — | — |
| 225 | InventoryItemBasePEORepairYield | REPAIR_YIELD | — | — |
| 226 | InventoryItemBasePEOReplacementType | REPLACEMENT_TYPE | — | — |
| 227 | InventoryItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 228 | InventoryItemBasePEORequestId | REQUEST_ID | — | — |
| 229 | InventoryItemBasePEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | — |
| 230 | InventoryItemBasePEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | — |
| 231 | InventoryItemBasePEOReservableType | RESERVABLE_TYPE | — | — |
| 232 | InventoryItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 233 | InventoryItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 234 | InventoryItemBasePEORetestInterval | RETEST_INTERVAL | — | — |
| 235 | InventoryItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 236 | InventoryItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 237 | InventoryItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 238 | InventoryItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 239 | InventoryItemBasePEORoundingFactor | ROUNDING_FACTOR | — | — |
| 240 | InventoryItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 241 | InventoryItemBasePEOSalesAccount | SALES_ACCOUNT | — | — |
| 242 | InventoryItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 243 | InventoryItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | ✅ |
| 244 | InventoryItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 245 | InventoryItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 246 | InventoryItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 247 | InventoryItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 248 | InventoryItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 249 | InventoryItemBasePEOServiceDuration | SERVICE_DURATION | — | — |
| 250 | InventoryItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 251 | InventoryItemBasePEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | — |
| 252 | InventoryItemBasePEOServiceStartDelay | SERVICE_START_DELAY | — | — |
| 253 | InventoryItemBasePEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | — |
| 254 | InventoryItemBasePEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 255 | InventoryItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 256 | InventoryItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 257 | InventoryItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 258 | InventoryItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 259 | InventoryItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 260 | InventoryItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 261 | InventoryItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 262 | InventoryItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 263 | InventoryItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 264 | InventoryItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 265 | InventoryItemBasePEOSourceType | SOURCE_TYPE | — | — |
| 266 | InventoryItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 267 | InventoryItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 268 | InventoryItemBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 269 | InventoryItemBasePEOStdLotSize | STD_LOT_SIZE | — | — |
| 270 | InventoryItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 271 | InventoryItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 272 | InventoryItemBasePEOStyleItemId | STYLE_ITEM_ID | — | — |
| 273 | InventoryItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 274 | InventoryItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 275 | InventoryItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 276 | InventoryItemBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 277 | InventoryItemBasePEOTaxCode | TAX_CODE | — | — |
| 278 | InventoryItemBasePEOTaxableFlag | TAXABLE_FLAG | — | — |
| 279 | InventoryItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 280 | InventoryItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 281 | InventoryItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 282 | InventoryItemBasePEOUnNumberId | UN_NUMBER_ID | — | — |
| 283 | InventoryItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 284 | InventoryItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 285 | InventoryItemBasePEOUnitHeight | UNIT_HEIGHT | — | — |
| 286 | InventoryItemBasePEOUnitLength | UNIT_LENGTH | — | — |
| 287 | InventoryItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 288 | InventoryItemBasePEOUnitVolume | UNIT_VOLUME | — | — |
| 289 | InventoryItemBasePEOUnitWeight | UNIT_WEIGHT | — | — |
| 290 | InventoryItemBasePEOUnitWidth | UNIT_WIDTH | — | — |
| 291 | InventoryItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 292 | InventoryItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 293 | InventoryItemBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 294 | InventoryItemBasePEOVersionId | VERSION_ID | — | — |
| 295 | InventoryItemBasePEOVersionStartDate | VERSION_START_DATE | — | — |
| 296 | InventoryItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 297 | InventoryItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 298 | InventoryItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 299 | InventoryItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 300 | InventoryItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 301 | InventoryItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 302 | InventoryItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 303 | InventoryItemBasePEOWebStatus | WEB_STATUS | — | — |
| 304 | InventoryItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 305 | InventoryItemBasePEOWhUpdateDate | WH_UPDATE_DATE | — | — |
| 306 | InventoryItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 307 | InventoryItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 308 | InventoryItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[por_requisition_headers_all|POR_REQUISITION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionHeaderPEOActiveRequisitionFlag | ACTIVE_REQUISITION_FLAG | — | — |
| 2 | RequisitionHeaderPEOApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 3 | RequisitionHeaderPEOApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | RequisitionHeaderPEOBudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | — |
| 5 | RequisitionHeaderPEOChangePendingFlag | CHANGE_PENDING_FLAG | — | — |
| 6 | RequisitionHeaderPEOCreatedBy | CREATED_BY | — | — |
| 7 | RequisitionHeaderPEOCreationDate | CREATION_DATE | — | — |
| 8 | RequisitionHeaderPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 9 | RequisitionHeaderPEODescription | DESCRIPTION | — | ✅ |
| 10 | RequisitionHeaderPEODocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 11 | RequisitionHeaderPEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 12 | RequisitionHeaderPEOEmergencyPoNumber | EMERGENCY_PO_NUMBER | — | — |
| 13 | RequisitionHeaderPEOEmergencyReqFlag | EMERGENCY_REQ_FLAG | — | — |
| 14 | RequisitionHeaderPEOExternallyManagedFlag | EXTERNALLY_MANAGED_FLAG | — | — |
| 15 | RequisitionHeaderPEOFundsChkFailWarnFlag | FUNDS_CHK_FAIL_WARN_FLAG | — | — |
| 16 | RequisitionHeaderPEOFundsOverrideApproverId | FUNDS_OVERRIDE_APPROVER_ID | — | — |
| 17 | RequisitionHeaderPEOFundsStatus | FUNDS_STATUS | — | — |
| 18 | RequisitionHeaderPEOHasCanceledLines | HAS_CANCELED_LINES | — | — |
| 19 | RequisitionHeaderPEOHasIncompleteLines | HAS_INCOMPLETE_LINES | — | — |
| 20 | RequisitionHeaderPEOHasPendingApprLines | HAS_PENDING_APPR_LINES | — | — |
| 21 | RequisitionHeaderPEOHasRejectedLines | HAS_REJECTED_LINES | — | — |
| 22 | RequisitionHeaderPEOHasReturnedLines | HAS_RETURNED_LINES | — | — |
| 23 | RequisitionHeaderPEOHasWithdrawnLines | HAS_WITHDRAWN_LINES | — | — |
| 24 | RequisitionHeaderPEOInsufficientFundsFlag | INSUFFICIENT_FUNDS_FLAG | — | — |
| 25 | RequisitionHeaderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 26 | RequisitionHeaderPEOInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | — |
| 27 | RequisitionHeaderPEOInternalTransferReqFlag | INTERNAL_TRANSFER_REQ_FLAG | — | — |
| 28 | RequisitionHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | RequisitionHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | RequisitionHeaderPEOJustification | JUSTIFICATION | — | ✅ |
| 31 | RequisitionHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | RequisitionHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | RequisitionHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | RequisitionHeaderPEOLineGroup | LINE_GROUP | — | — |
| 35 | RequisitionHeaderPEOLockedByBuyerFlag | LOCKED_BY_BUYER_FLAG | — | — |
| 36 | RequisitionHeaderPEOModifyingApproverId | MODIFYING_APPROVER_ID | — | — |
| 37 | RequisitionHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | RequisitionHeaderPEOOverridingApproverId | OVERRIDING_APPROVER_ID | — | — |
| 39 | RequisitionHeaderPEOPcardId | PCARD_ID | — | — |
| 40 | RequisitionHeaderPEOPrcBuId | PRC_BU_ID | — | — |
| 41 | RequisitionHeaderPEOPreparerId | PREPARER_ID | — | — |
| 42 | RequisitionHeaderPEOReqBuId | REQ_BU_ID | — | — |
| 43 | RequisitionHeaderPEOReqImportApproverId | REQ_IMPORT_APPROVER_ID | — | — |
| 44 | RequisitionHeaderPEORequestId | REQUEST_ID | — | — |
| 45 | RequisitionHeaderPEORequisitionHeaderId | REQUISITION_HEADER_ID | — | — |
| 46 | RequisitionHeaderPEORequisitionNumber | REQUISITION_NUMBER | — | ✅ |
| 47 | RequisitionHeaderPEOSoldtoLeId | SOLDTO_LE_ID | — | — |
| 48 | RequisitionHeaderPEOSubmissionDate | SUBMISSION_DATE | — | — |
| 49 | RequisitionHeaderPEOTaxUserOverrideHdrFlag | TAX_USER_OVERRIDE_HDR_FLAG | — | — |

### [[por_requisition_lines_all|POR_REQUISITION_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequisitionLinePEOAmount | AMOUNT | — | ✅ |
| 2 | RequisitionLinePEOAssessableValue | ASSESSABLE_VALUE | — | — |
| 3 | RequisitionLinePEOAssignedBuyerId | ASSIGNED_BUYER_ID | — | — |
| 4 | RequisitionLinePEOAtSourcingFlag | AT_SOURCING_FLAG | — | — |
| 5 | RequisitionLinePEOAuctionDisplayNumber | AUCTION_DISPLAY_NUMBER | — | — |
| 6 | RequisitionLinePEOAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 7 | RequisitionLinePEOAuctionLineNumber | AUCTION_LINE_NUMBER | — | — |
| 8 | RequisitionLinePEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 9 | RequisitionLinePEOBaseModelId | BASE_MODEL_ID | — | — |
| 10 | RequisitionLinePEOBaseModelPrice | BASE_MODEL_PRICE | — | — |
| 11 | RequisitionLinePEOBidLineNumber | BID_LINE_NUMBER | — | — |
| 12 | RequisitionLinePEOBidNumber | BID_NUMBER | — | — |
| 13 | RequisitionLinePEOBpaPriceUserOverrideFlag | BPA_PRICE_USER_OVERRIDE_FLAG | — | — |
| 14 | RequisitionLinePEOBuyerProcessingFlag | BUYER_PROCESSING_FLAG | — | — |
| 15 | RequisitionLinePEOCancelDate | CANCEL_DATE | — | — |
| 16 | RequisitionLinePEOCancelFlag | CANCEL_FLAG | — | — |
| 17 | RequisitionLinePEOCancelReason | CANCEL_REASON | — | — |
| 18 | RequisitionLinePEOCarrierId | CARRIER_ID | — | — |
| 19 | RequisitionLinePEOCategoryId | CATEGORY_ID | — | — |
| 20 | RequisitionLinePEOConfiguredItemFlag | CONFIGURED_ITEM_FLAG | — | — |
| 21 | RequisitionLinePEOContentPrcBuId | CONTENT_PRC_BU_ID | — | — |
| 22 | RequisitionLinePEOCreatedBy | CREATED_BY | — | — |
| 23 | RequisitionLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 24 | RequisitionLinePEOCurrencyAmount | CURRENCY_AMOUNT | — | — |
| 25 | RequisitionLinePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 26 | RequisitionLinePEOCurrencyUnitPrice | CURRENCY_UNIT_PRICE | — | — |
| 27 | RequisitionLinePEOCustomerItem | CUSTOMER_ITEM | — | — |
| 28 | RequisitionLinePEOCustomerItemDesc | CUSTOMER_ITEM_DESC | — | — |
| 29 | RequisitionLinePEOCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 30 | RequisitionLinePEOCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 31 | RequisitionLinePEOCustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | — |
| 32 | RequisitionLinePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 33 | RequisitionLinePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 34 | RequisitionLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | — |
| 35 | RequisitionLinePEODeliverToCustContactId | DELIVER_TO_CUST_CONTACT_ID | — | — |
| 36 | RequisitionLinePEODeliverToCustId | DELIVER_TO_CUST_ID | — | — |
| 37 | RequisitionLinePEODeliverToCustLocationId | DELIVER_TO_CUST_LOCATION_ID | — | — |
| 38 | RequisitionLinePEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | — |
| 39 | RequisitionLinePEODestinationOrganizationId | DESTINATION_ORGANIZATION_ID | — | — |
| 40 | RequisitionLinePEODestinationSubinventory | DESTINATION_SUBINVENTORY | — | — |
| 41 | RequisitionLinePEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 42 | RequisitionLinePEODocumentSubType | DOCUMENT_SUB_TYPE | — | — |
| 43 | RequisitionLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 44 | RequisitionLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | — |
| 45 | RequisitionLinePEOFundsStatus | FUNDS_STATUS | — | — |
| 46 | RequisitionLinePEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 47 | RequisitionLinePEOInfoTemplateTouchedFlag | INFO_TEMPLATE_TOUCHED_FLAG | — | — |
| 48 | RequisitionLinePEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 49 | RequisitionLinePEOItemId | ITEM_ID | — | ✅ |
| 50 | RequisitionLinePEOItemRevision | ITEM_REVISION | — | ✅ |
| 51 | RequisitionLinePEOItemSource | ITEM_SOURCE | — | ✅ |
| 52 | RequisitionLinePEOItemUserOverrideFlag | ITEM_USER_OVERRIDE_FLAG | — | — |
| 53 | RequisitionLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 54 | RequisitionLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 55 | RequisitionLinePEOLastApprovalDate | LAST_APPROVAL_DATE | — | — |
| 56 | RequisitionLinePEOLastSubmittedDate | LAST_SUBMITTED_DATE | — | — |
| 57 | RequisitionLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | RequisitionLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 59 | RequisitionLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 60 | RequisitionLinePEOLineGroup | LINE_GROUP | — | — |
| 61 | RequisitionLinePEOLineIntendedUse | LINE_INTENDED_USE | — | — |
| 62 | RequisitionLinePEOLineIntendedUseId | LINE_INTENDED_USE_ID | — | — |
| 63 | RequisitionLinePEOLineLocationId | LINE_LOCATION_ID | — | — |
| 64 | RequisitionLinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 65 | RequisitionLinePEOLineStatus | LINE_STATUS | — | — |
| 66 | RequisitionLinePEOLineTypeId | LINE_TYPE_ID | — | — |
| 67 | RequisitionLinePEOManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 68 | RequisitionLinePEOManufacturerPartNumber | MANUFACTURER_PART_NUMBER | — | ✅ |
| 69 | RequisitionLinePEOMatchingBasis | MATCHING_BASIS | — | — |
| 70 | RequisitionLinePEOModeOfTransport | MODE_OF_TRANSPORT | — | — |
| 71 | RequisitionLinePEOModifiedByBuyerFlag | MODIFIED_BY_BUYER_FLAG | — | — |
| 72 | RequisitionLinePEOModifiedByBuyerId | MODIFIED_BY_BUYER_ID | — | — |
| 73 | RequisitionLinePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 74 | RequisitionLinePEONegotiatedByPreparerFlag | NEGOTIATED_BY_PREPARER_FLAG | — | — |
| 75 | RequisitionLinePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 76 | RequisitionLinePEONewSupplierFlag | NEW_SUPPLIER_FLAG | — | — |
| 77 | RequisitionLinePEONoteToBuyer | NOTE_TO_BUYER | — | — |
| 78 | RequisitionLinePEONoteToReceiver | NOTE_TO_RECEIVER | — | — |
| 79 | RequisitionLinePEONoteToSupplier | NOTE_TO_SUPPLIER | — | — |
| 80 | RequisitionLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 81 | RequisitionLinePEOOnRfqFlag | ON_RFQ_FLAG | — | — |
| 82 | RequisitionLinePEOOneTimeLocationFlag | ONE_TIME_LOCATION_FLAG | — | — |
| 83 | RequisitionLinePEOOptionsPrice | OPTIONS_PRICE | — | — |
| 84 | RequisitionLinePEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 85 | RequisitionLinePEOOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 86 | RequisitionLinePEOOriginalApprovalDate | ORIGINAL_APPROVAL_DATE | — | — |
| 87 | RequisitionLinePEOOriginalSubmittedDate | ORIGINAL_SUBMITTED_DATE | — | — |
| 88 | RequisitionLinePEOParentReqLineId | PARENT_REQ_LINE_ID | — | — |
| 89 | RequisitionLinePEOPcardFlag | PCARD_FLAG | — | — |
| 90 | RequisitionLinePEOPoHeaderId | PO_HEADER_ID | — | — |
| 91 | RequisitionLinePEOPoLineId | PO_LINE_ID | — | — |
| 92 | RequisitionLinePEOPrcBuId | PRC_BU_ID | — | — |
| 93 | RequisitionLinePEOProductCategory | PRODUCT_CATEGORY | — | — |
| 94 | RequisitionLinePEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | — |
| 95 | RequisitionLinePEOProductFiscClassificationId | PRODUCT_FISC_CLASSIFICATION_ID | — | — |
| 96 | RequisitionLinePEOProductType | PRODUCT_TYPE | — | — |
| 97 | RequisitionLinePEOPublicListId | PUBLIC_LIST_ID | — | — |
| 98 | RequisitionLinePEOPunchoutCatalogId | PUNCHOUT_CATALOG_ID | — | — |
| 99 | RequisitionLinePEOPurchaseBasis | PURCHASE_BASIS | — | ✅ |
| 100 | RequisitionLinePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 101 | RequisitionLinePEOQuantity | QUANTITY | — | ✅ |
| 102 | RequisitionLinePEOQuantityCancelled | QUANTITY_CANCELLED | — | — |
| 103 | RequisitionLinePEOQuantityDelivered | QUANTITY_DELIVERED | — | — |
| 104 | RequisitionLinePEOQuantityReceived | QUANTITY_RECEIVED | — | — |
| 105 | RequisitionLinePEORate | RATE | — | — |
| 106 | RequisitionLinePEORateDate | RATE_DATE | — | — |
| 107 | RequisitionLinePEORateType | RATE_TYPE | — | — |
| 108 | RequisitionLinePEOReinstateLineLocationId | REINSTATE_LINE_LOCATION_ID | — | — |
| 109 | RequisitionLinePEOReqBuId | REQ_BU_ID | — | — |
| 110 | RequisitionLinePEOReqPoInstanceId | REQ_PO_INSTANCE_ID | — | — |
| 111 | RequisitionLinePEOReqsInPoolFlag | REQS_IN_POOL_FLAG | — | — |
| 112 | RequisitionLinePEOReqtopoAutoFailedReason | REQTOPO_AUTO_FAILED_REASON | — | — |
| 113 | RequisitionLinePEOReqtopoAutomationFailed | REQTOPO_AUTOMATION_FAILED | — | — |
| 114 | RequisitionLinePEORequestId | REQUEST_ID | — | — |
| 115 | RequisitionLinePEORequestedShipDate | REQUESTED_SHIP_DATE | — | — |
| 116 | RequisitionLinePEORequesterId | REQUESTER_ID | — | — |
| 117 | RequisitionLinePEORequesterSupervisorLevel1 | REQUESTER_SUPERVISOR_LEVEL1 | — | — |
| 118 | RequisitionLinePEORequesterSupervisorLevel10 | REQUESTER_SUPERVISOR_LEVEL10 | — | — |
| 119 | RequisitionLinePEORequesterSupervisorLevel2 | REQUESTER_SUPERVISOR_LEVEL2 | — | — |
| 120 | RequisitionLinePEORequesterSupervisorLevel3 | REQUESTER_SUPERVISOR_LEVEL3 | — | — |
| 121 | RequisitionLinePEORequesterSupervisorLevel4 | REQUESTER_SUPERVISOR_LEVEL4 | — | — |
| 122 | RequisitionLinePEORequesterSupervisorLevel5 | REQUESTER_SUPERVISOR_LEVEL5 | — | — |
| 123 | RequisitionLinePEORequesterSupervisorLevel6 | REQUESTER_SUPERVISOR_LEVEL6 | — | — |
| 124 | RequisitionLinePEORequesterSupervisorLevel7 | REQUESTER_SUPERVISOR_LEVEL7 | — | — |
| 125 | RequisitionLinePEORequesterSupervisorLevel8 | REQUESTER_SUPERVISOR_LEVEL8 | — | — |
| 126 | RequisitionLinePEORequesterSupervisorLevel9 | REQUESTER_SUPERVISOR_LEVEL9 | — | — |
| 127 | RequisitionLinePEORequisitionHeaderId | REQUISITION_HEADER_ID | — | ✅ |
| 128 | RequisitionLinePEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 129 | RequisitionLinePEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 130 | RequisitionLinePEOSalesOrderNumber | SALES_ORDER_NUMBER | — | — |
| 131 | RequisitionLinePEOSalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | — |
| 132 | RequisitionLinePEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 133 | RequisitionLinePEOSecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | — |
| 134 | RequisitionLinePEOSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | — |
| 135 | RequisitionLinePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 136 | RequisitionLinePEOServiceLevel | SERVICE_LEVEL | — | — |
| 137 | RequisitionLinePEOShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | — |
| 138 | RequisitionLinePEOShipToCustId | SHIP_TO_CUST_ID | — | — |
| 139 | RequisitionLinePEOShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | — |
| 140 | RequisitionLinePEOSmartFormId | SMART_FORM_ID | — | — |
| 141 | RequisitionLinePEOSourceDocHeaderId | SOURCE_DOC_HEADER_ID | — | — |
| 142 | RequisitionLinePEOSourceDocLineId | SOURCE_DOC_LINE_ID | — | — |
| 143 | RequisitionLinePEOSourceDocumentType | SOURCE_DOCUMENT_TYPE | — | — |
| 144 | RequisitionLinePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 145 | RequisitionLinePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 146 | RequisitionLinePEOSourceTypeCode | SOURCE_TYPE_CODE | — | — |
| 147 | RequisitionLinePEOSuggestedBuyerId | SUGGESTED_BUYER_ID | — | — |
| 148 | RequisitionLinePEOSuggestedSupplierItemNumber | SUGGESTED_SUPPLIER_ITEM_NUMBER | — | ✅ |
| 149 | RequisitionLinePEOSuggestedVendorContact | SUGGESTED_VENDOR_CONTACT | — | — |
| 150 | RequisitionLinePEOSuggestedVendorContactEmail | SUGGESTED_VENDOR_CONTACT_EMAIL | — | — |
| 151 | RequisitionLinePEOSuggestedVendorContactFax | SUGGESTED_VENDOR_CONTACT_FAX | — | — |
| 152 | RequisitionLinePEOSuggestedVendorContactPhone | SUGGESTED_VENDOR_CONTACT_PHONE | — | — |
| 153 | RequisitionLinePEOSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | — |
| 154 | RequisitionLinePEOSuggestedVendorSite | SUGGESTED_VENDOR_SITE | — | — |
| 155 | RequisitionLinePEOSupplierDuns | SUPPLIER_DUNS | — | — |
| 156 | RequisitionLinePEOSupplierRefNumber | SUPPLIER_REF_NUMBER | — | — |
| 157 | RequisitionLinePEOTaxAttrUserOverrideFlag | TAX_ATTR_USER_OVERRIDE_FLAG | — | — |
| 158 | RequisitionLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 159 | RequisitionLinePEOThirdPtyRegId | THIRD_PTY_REG_ID | — | — |
| 160 | RequisitionLinePEOToHeaderId | TO_HEADER_ID | — | — |
| 161 | RequisitionLinePEOToLineId | TO_LINE_ID | — | — |
| 162 | RequisitionLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | — |
| 163 | RequisitionLinePEOUnNumberId | UN_NUMBER_ID | — | — |
| 164 | RequisitionLinePEOUnitPrice | UNIT_PRICE | — | ✅ |
| 165 | RequisitionLinePEOUnspscCode | UNSPSC_CODE | — | — |
| 166 | RequisitionLinePEOUomCode | UOM_CODE | — | ✅ |
| 167 | RequisitionLinePEOUrgentFlag | URGENT_FLAG | — | ✅ |
| 168 | RequisitionLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | — |
| 169 | RequisitionLinePEOVendorContactId | VENDOR_CONTACT_ID | — | — |
| 170 | RequisitionLinePEOVendorId | VENDOR_ID | — | — |
| 171 | RequisitionLinePEOVendorSiteId | VENDOR_SITE_ID | — | — |
| 172 | RequisitionLinePEOWorkOrderId | WORK_ORDER_ID | — | — |
| 173 | RequisitionLinePEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 174 | RequisitionLinePEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |
| 175 | RequisitionLinePEOWorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | — |
| 176 | RequisitionLinePEOWorkOrderProduct | WORK_ORDER_PRODUCT | — | — |
| 177 | RequisitionLinePEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |

### [[por_req_distributions_all|POR_REQ_DISTRIBUTIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 2 | RequisitionDistributionPEOAccountUserOverrideFlag | ACCOUNT_USER_OVERRIDE_FLAG | — | — |
| 3 | RequisitionDistributionPEOAccrualAccountId | ACCRUAL_ACCOUNT_ID | — | — |
| 4 | RequisitionDistributionPEOBudgetDate | BUDGET_DATE | — | — |
| 5 | RequisitionDistributionPEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 6 | RequisitionDistributionPEOCreatedBy | CREATED_BY | — | — |
| 7 | RequisitionDistributionPEOCreationDate | CREATION_DATE | — | — |
| 8 | RequisitionDistributionPEODistributionAmount | DISTRIBUTION_AMOUNT | — | ✅ |
| 9 | RequisitionDistributionPEODistributionCurrencyAmount | DISTRIBUTION_CURRENCY_AMOUNT | — | — |
| 10 | RequisitionDistributionPEODistributionNumber | DISTRIBUTION_NUMBER | — | — |
| 11 | RequisitionDistributionPEODistributionQuantity | DISTRIBUTION_QUANTITY | — | ✅ |
| 12 | RequisitionDistributionPEOFundsStatus | FUNDS_STATUS | — | — |
| 13 | RequisitionDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | RequisitionDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | RequisitionDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | RequisitionDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | RequisitionDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | RequisitionDistributionPEONonrecoverableTax | NONRECOVERABLE_TAX | — | — |
| 19 | RequisitionDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | RequisitionDistributionPEOPJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | — | — |
| 21 | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | — | — |
| 22 | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | — | — |
| 23 | RequisitionDistributionPEOPJC_CONTRACT_ID | PJC_CONTRACT_ID | — | — |
| 24 | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | — | — |
| 25 | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 26 | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | — | — |
| 27 | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | — | — |
| 28 | RequisitionDistributionPEOPJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | — | — |
| 29 | RequisitionDistributionPEOPJC_PROJECT_ID | PJC_PROJECT_ID | — | — |
| 30 | RequisitionDistributionPEOPJC_TASK_ID | PJC_TASK_ID | — | — |
| 31 | RequisitionDistributionPEOPJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | — | — |
| 32 | RequisitionDistributionPEOPercent | PERCENT | — | — |
| 33 | RequisitionDistributionPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 34 | RequisitionDistributionPEORecoverableTax | RECOVERABLE_TAX | — | — |
| 35 | RequisitionDistributionPEOReqBuId | REQ_BU_ID | — | — |
| 36 | RequisitionDistributionPEORequestId | REQUEST_ID | — | — |
| 37 | RequisitionDistributionPEORequisitionLineId | REQUISITION_LINE_ID | — | — |
| 38 | RequisitionDistributionPEOVarianceAccountId | VARIANCE_ACCOUNT_ID | — | — |

### [[po_line_types_vl|PO_LINE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PurchasingLineTypePEOCategoryId | CATEGORY_ID | — | — |
| 2 | PurchasingLineTypePEOCreatedBy | CREATED_BY | — | — |
| 3 | PurchasingLineTypePEOCreationDate | CREATION_DATE | — | — |
| 4 | PurchasingLineTypePEODescription | DESCRIPTION | — | — |
| 5 | PurchasingLineTypePEOInactiveDate | INACTIVE_DATE | — | — |
| 6 | PurchasingLineTypePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 7 | PurchasingLineTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PurchasingLineTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PurchasingLineTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PurchasingLineTypePEOLineType | LINE_TYPE | — | — |
| 11 | PurchasingLineTypePEOLineTypeCode | LINE_TYPE_CODE | — | — |
| 12 | PurchasingLineTypePEOLineTypeId | LINE_TYPE_ID | — | — |
| 13 | PurchasingLineTypePEOMatchOption | MATCH_OPTION | — | — |
| 14 | PurchasingLineTypePEOMatchingBasis | MATCHING_BASIS | — | — |
| 15 | PurchasingLineTypePEOOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 16 | PurchasingLineTypePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 17 | PurchasingLineTypePEOPurchaseBasis | PURCHASE_BASIS | — | — |
| 18 | PurchasingLineTypePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 19 | PurchasingLineTypePEOReceivingFlag | RECEIVING_FLAG | — | — |
| 20 | PurchasingLineTypePEORowId1 | ROW_ID | — | — |
| 21 | PurchasingLineTypePEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 22 | PurchasingLineTypePEOUnitPrice | UNIT_PRICE | — | — |
| 23 | PurchasingLineTypePEOUomCode | UOM_CODE | — | — |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 4 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | — |
| 5 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 6 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | — |
| 7 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 8 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 9 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 10 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 11 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 12 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 13 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 14 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 15 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 16 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 17 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 18 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 19 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 20 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 21 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 22 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 28 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 30 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 31 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 32 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 33 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 34 | WorkOrderAnalyticsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 35 | WorkOrderAnalyticsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 36 | WorkOrderAnalyticsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 37 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 38 | WorkOrderAnalyticsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 39 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 40 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 41 | WorkOrderAnalyticsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 42 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 43 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 44 | WorkOrderAnalyticsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | — |
| 45 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 46 | WorkOrderAnalyticsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 47 | WorkOrderAnalyticsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 48 | WorkOrderAnalyticsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 49 | WorkOrderAnalyticsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 50 | WorkOrderAnalyticsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 51 | WorkOrderAnalyticsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 52 | WorkOrderAnalyticsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 53 | WorkOrderAnalyticsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 54 | WorkOrderAnalyticsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 55 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 56 | WorkOrderAnalyticsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | — |
| 57 | WorkOrderAnalyticsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 58 | WorkOrderAnalyticsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 59 | WorkOrderAnalyticsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 60 | WorkOrderAnalyticsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 61 | WorkOrderAnalyticsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 62 | WorkOrderAnalyticsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 63 | WorkOrderAnalyticsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 64 | WorkOrderAnalyticsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 65 | WorkOrderAnalyticsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 66 | WorkOrderAnalyticsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 67 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 68 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 69 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 70 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 71 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 72 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | — |
| 73 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | — |
| 74 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 75 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 76 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 77 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 78 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 79 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 80 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 81 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 82 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 83 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 84 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 85 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 86 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 87 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 88 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 89 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 90 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 91 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 92 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 93 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 94 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 95 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 96 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WOOperationAnalyticsPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 4 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 5 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 6 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 7 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 8 | WOOperationAnalyticsPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 9 | WOOperationAnalyticsPEOInProcessQuantity | IN_PROCESS_QUANTITY | — | — |
| 10 | WOOperationAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | WOOperationAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | WOOperationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | WOOperationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | WOOperationAnalyticsPEOLeadTimeUom | LEAD_TIME_UOM | — | — |
| 16 | WOOperationAnalyticsPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 17 | WOOperationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | WOOperationAnalyticsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 19 | WOOperationAnalyticsPEOOperationType | OPERATION_TYPE | — | — |
| 20 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 21 | WOOperationAnalyticsPEOOspItemId | OSP_ITEM_ID | — | — |
| 22 | WOOperationAnalyticsPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | — |
| 23 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 24 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 25 | WOOperationAnalyticsPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | — |
| 26 | WOOperationAnalyticsPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | — |
| 27 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 28 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | — |
| 29 | WOOperationAnalyticsPEOReceivedQuantity | RECEIVED_QUANTITY | — | — |
| 30 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 31 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | — |
| 32 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 33 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 34 | WOOperationAnalyticsPEOShippedQuantity | SHIPPED_QUANTITY | — | — |
| 35 | WOOperationAnalyticsPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 36 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | — |
| 37 | WOOperationAnalyticsPEOSupplierId | SUPPLIER_ID | — | — |
| 38 | WOOperationAnalyticsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 39 | WOOperationAnalyticsPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 40 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | — |
| 41 | WOOperationAnalyticsPEOWoOperationId | WO_OPERATION_ID | — | — |
| 42 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 43 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 4 | WorkMethodPEOWorkMethodName | WORK_METHOD_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
