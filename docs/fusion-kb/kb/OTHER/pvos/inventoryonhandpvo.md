---
id: DOC-OTHER-PVO-InventoryOnhandPVO
doc_type: system-doc
title: "InventoryOnhandPVO — PVO Cross-Module"
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
  - InventoryOnhandPVO
  - inventoryonhandpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryOnhandPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Onhand. Acessa as tabelas: EGP_SYSTEM_ITEMS_B_V, INV_ONHAND_QUANTITIES_DETAIL, POZ_SUPPLIER_SITES_ALL_M.

**Caminho:** `FscmTopModelAM.InventoryAM.InventoryOnhandPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 335 | 3 | 2 | 17 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 299 atributos (1 PKs, 2 BICC)
- [[inv_onhand_quantities_detail|INV_ONHAND_QUANTITIES_DETAIL]] — 31 atributos (1 PKs, 15 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 5 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBPEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | ItemBPEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | ItemBPEOAcdType | ACD_TYPE | — | — |
| 4 | ItemBPEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 5 | ItemBPEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 6 | ItemBPEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 7 | ItemBPEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 8 | ItemBPEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 9 | ItemBPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 10 | ItemBPEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 11 | ItemBPEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 12 | ItemBPEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 13 | ItemBPEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 14 | ItemBPEOAtpFlag | ATP_FLAG | — | — |
| 15 | ItemBPEOAtpRuleId | ATP_RULE_ID | — | — |
| 16 | ItemBPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 17 | ItemBPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 18 | ItemBPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 19 | ItemBPEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 20 | ItemBPEOBaseItemId | BASE_ITEM_ID | — | — |
| 21 | ItemBPEOBomItemType | BOM_ITEM_TYPE | — | — |
| 22 | ItemBPEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 23 | ItemBPEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 24 | ItemBPEOBuyerId | BUYER_ID | — | — |
| 25 | ItemBPEOCarryingCost | CARRYING_COST | — | — |
| 26 | ItemBPEOCasNumber | CAS_NUMBER | — | — |
| 27 | ItemBPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 28 | ItemBPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 29 | ItemBPEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 30 | ItemBPEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 31 | ItemBPEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 32 | ItemBPEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 33 | ItemBPEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 34 | ItemBPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 35 | ItemBPEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 36 | ItemBPEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 37 | ItemBPEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 38 | ItemBPEOConfigMatch | CONFIG_MATCH | — | — |
| 39 | ItemBPEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 40 | ItemBPEOConfigOrgs | CONFIG_ORGS | — | — |
| 41 | ItemBPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 42 | ItemBPEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 43 | ItemBPEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 44 | ItemBPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 45 | ItemBPEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 46 | ItemBPEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 47 | ItemBPEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 48 | ItemBPEOCreatedBy | CREATED_BY | — | — |
| 49 | ItemBPEOCreationDate | CREATION_DATE | — | — |
| 50 | ItemBPEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 51 | ItemBPEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 52 | ItemBPEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 53 | ItemBPEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 54 | ItemBPEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 55 | ItemBPEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 56 | ItemBPEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 57 | ItemBPEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 58 | ItemBPEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 59 | ItemBPEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 60 | ItemBPEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 61 | ItemBPEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 62 | ItemBPEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 63 | ItemBPEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 64 | ItemBPEODefaultGrade | DEFAULT_GRADE | — | — |
| 65 | ItemBPEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 66 | ItemBPEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 67 | ItemBPEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 68 | ItemBPEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 69 | ItemBPEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 70 | ItemBPEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 71 | ItemBPEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 72 | ItemBPEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 73 | ItemBPEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 74 | ItemBPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 75 | ItemBPEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 76 | ItemBPEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 77 | ItemBPEODualUomControl | DUAL_UOM_CONTROL | — | — |
| 78 | ItemBPEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 79 | ItemBPEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 80 | ItemBPEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 81 | ItemBPEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 82 | ItemBPEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 83 | ItemBPEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 84 | ItemBPEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 85 | ItemBPEOEamItemType | EAM_ITEM_TYPE | — | — |
| 86 | ItemBPEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 87 | ItemBPEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 88 | ItemBPEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 89 | ItemBPEOEnabledFlag | ENABLED_FLAG | — | — |
| 90 | ItemBPEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 91 | ItemBPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 92 | ItemBPEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 93 | ItemBPEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 94 | ItemBPEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 95 | ItemBPEOEventFlag | EVENT_FLAG | — | — |
| 96 | ItemBPEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 97 | ItemBPEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 98 | ItemBPEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 99 | ItemBPEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 100 | ItemBPEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 101 | ItemBPEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 102 | ItemBPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 103 | ItemBPEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 104 | ItemBPEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 105 | ItemBPEOForecastHorizon | FORECAST_HORIZON | — | — |
| 106 | ItemBPEOFullLeadTime | FULL_LEAD_TIME | — | — |
| 107 | ItemBPEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 108 | ItemBPEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 109 | ItemBPEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 110 | ItemBPEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 111 | ItemBPEOHoldDays | HOLD_DAYS | — | — |
| 112 | ItemBPEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 113 | ItemBPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 114 | ItemBPEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 115 | ItemBPEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 116 | ItemBPEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 117 | ItemBPEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 118 | ItemBPEOInternalVolume | INTERNAL_VOLUME | — | — |
| 119 | ItemBPEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 120 | ItemBPEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 121 | ItemBPEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 122 | ItemBPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | — |
| 123 | ItemBPEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 124 | ItemBPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 125 | ItemBPEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 126 | ItemBPEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 127 | ItemBPEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 128 | ItemBPEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 129 | ItemBPEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 130 | ItemBPEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 131 | ItemBPEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 132 | ItemBPEOItemNumber | ITEM_NUMBER | — | — |
| 133 | ItemBPEOItemType | ITEM_TYPE | — | — |
| 134 | ItemBPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 135 | ItemBPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 136 | ItemBPEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 137 | ItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 138 | ItemBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 139 | ItemBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 140 | ItemBPEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 141 | ItemBPEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 142 | ItemBPEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 143 | ItemBPEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 144 | ItemBPEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 145 | ItemBPEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 146 | ItemBPEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 147 | ItemBPEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 148 | ItemBPEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 149 | ItemBPEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 150 | ItemBPEOMarketPrice | MARKET_PRICE | — | — |
| 151 | ItemBPEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 152 | ItemBPEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 153 | ItemBPEOMaturityDays | MATURITY_DAYS | — | — |
| 154 | ItemBPEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 155 | ItemBPEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 156 | ItemBPEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 157 | ItemBPEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 158 | ItemBPEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 159 | ItemBPEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 160 | ItemBPEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 161 | ItemBPEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 162 | ItemBPEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 163 | ItemBPEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 164 | ItemBPEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 165 | ItemBPEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 166 | ItemBPEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 167 | ItemBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 168 | ItemBPEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 169 | ItemBPEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 170 | ItemBPEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 171 | ItemBPEOOrderCost | ORDER_COST | — | — |
| 172 | ItemBPEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 173 | ItemBPEOOrganizationId | ORGANIZATION_ID | — | — |
| 174 | ItemBPEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 175 | ItemBPEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | — |
| 176 | ItemBPEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 177 | ItemBPEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 178 | ItemBPEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 179 | ItemBPEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 180 | ItemBPEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 181 | ItemBPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 182 | ItemBPEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 183 | ItemBPEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 184 | ItemBPEOPickingRuleId | PICKING_RULE_ID | — | — |
| 185 | ItemBPEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 186 | ItemBPEOPlannerCode | PLANNER_CODE | — | — |
| 187 | ItemBPEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 188 | ItemBPEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 189 | ItemBPEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 190 | ItemBPEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 191 | ItemBPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 192 | ItemBPEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 193 | ItemBPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 194 | ItemBPEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 195 | ItemBPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 196 | ItemBPEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 197 | ItemBPEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 198 | ItemBPEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 199 | ItemBPEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 200 | ItemBPEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 201 | ItemBPEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 202 | ItemBPEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 203 | ItemBPEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 204 | ItemBPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 205 | ItemBPEOProgramName | PROGRAM_NAME | — | — |
| 206 | ItemBPEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 207 | ItemBPEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 208 | ItemBPEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 209 | ItemBPEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 210 | ItemBPEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 211 | ItemBPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 212 | ItemBPEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 213 | ItemBPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 214 | ItemBPEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 215 | ItemBPEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 216 | ItemBPEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 217 | ItemBPEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 218 | ItemBPEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 219 | ItemBPEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 220 | ItemBPEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 221 | ItemBPEORepairProgram | REPAIR_PROGRAM | — | — |
| 222 | ItemBPEORepairYield | REPAIR_YIELD | — | — |
| 223 | ItemBPEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 224 | ItemBPEORequestId | REQUEST_ID | — | — |
| 225 | ItemBPEOReservableType | RESERVABLE_TYPE | — | — |
| 226 | ItemBPEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 227 | ItemBPEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 228 | ItemBPEORetestInterval | RETEST_INTERVAL | — | — |
| 229 | ItemBPEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 230 | ItemBPEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 231 | ItemBPEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 232 | ItemBPEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 233 | ItemBPEORoundingFactor | ROUNDING_FACTOR | — | — |
| 234 | ItemBPEOSalesAccount | SALES_ACCOUNT | — | — |
| 235 | ItemBPEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 236 | ItemBPEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 237 | ItemBPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 238 | ItemBPEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 239 | ItemBPEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 240 | ItemBPEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 241 | ItemBPEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 242 | ItemBPEOServiceDuration | SERVICE_DURATION | — | — |
| 243 | ItemBPEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 244 | ItemBPEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 245 | ItemBPEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 246 | ItemBPEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 247 | ItemBPEOShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 248 | ItemBPEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 249 | ItemBPEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 250 | ItemBPEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 251 | ItemBPEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 252 | ItemBPEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 253 | ItemBPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 254 | ItemBPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 255 | ItemBPEOSourceType | SOURCE_TYPE | — | — |
| 256 | ItemBPEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 257 | ItemBPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 258 | ItemBPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 259 | ItemBPEOStdLotSize | STD_LOT_SIZE | — | — |
| 260 | ItemBPEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 261 | ItemBPEOStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 262 | ItemBPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 263 | ItemBPEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 264 | ItemBPEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 265 | ItemBPEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 266 | ItemBPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 267 | ItemBPEOTaxCode | TAX_CODE | — | — |
| 268 | ItemBPEOTaxableFlag | TAXABLE_FLAG | — | — |
| 269 | ItemBPEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 270 | ItemBPEOTemplateName | ITEM_NUMBER | — | — |
| 271 | ItemBPEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 272 | ItemBPEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 273 | ItemBPEOUnNumberId | UN_NUMBER_ID | — | — |
| 274 | ItemBPEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 275 | ItemBPEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 276 | ItemBPEOUnitHeight | UNIT_HEIGHT | — | — |
| 277 | ItemBPEOUnitLength | UNIT_LENGTH | — | — |
| 278 | ItemBPEOUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 279 | ItemBPEOUnitVolume | UNIT_VOLUME | — | — |
| 280 | ItemBPEOUnitWeight | UNIT_WEIGHT | — | — |
| 281 | ItemBPEOUnitWidth | UNIT_WIDTH | — | — |
| 282 | ItemBPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 283 | ItemBPEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 284 | ItemBPEOVersionEndDate | VERSION_END_DATE | — | — |
| 285 | ItemBPEOVersionId | VERSION_ID | — | — |
| 286 | ItemBPEOVersionStartDate | VERSION_START_DATE | — | — |
| 287 | ItemBPEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 288 | ItemBPEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 289 | ItemBPEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 290 | ItemBPEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 291 | ItemBPEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 292 | ItemBPEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 293 | ItemBPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 294 | ItemBPEOWebStatus | WEB_STATUS | — | — |
| 295 | ItemBPEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 296 | ItemBPEOWhUpdateDate | WH_UPDATE_DATE | — | — |
| 297 | ItemBPEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 298 | ItemBPEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 299 | ItemBPEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[inv_onhand_quantities_detail|INV_ONHAND_QUANTITIES_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryOnhandPEOAgingExpirationDate | AGING_EXPIRATION_DATE | — | ✅ |
| 2 | InventoryOnhandPEOAgingOnsetDate | AGING_ONSET_DATE | — | ✅ |
| 3 | InventoryOnhandPEOCreateTransactionId | CREATE_TRANSACTION_ID | — | — |
| 4 | InventoryOnhandPEOCreatedBy | CREATED_BY | — | — |
| 5 | InventoryOnhandPEOCreationDate | CREATION_DATE | — | — |
| 6 | InventoryOnhandPEODateReceived | DATE_RECEIVED | — | — |
| 7 | InventoryOnhandPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 8 | InventoryOnhandPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | InventoryOnhandPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | InventoryOnhandPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | InventoryOnhandPEOLocatorId | LOCATOR_ID | — | ✅ |
| 12 | InventoryOnhandPEOLotNumber | LOT_NUMBER | — | — |
| 13 | InventoryOnhandPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | InventoryOnhandPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 15 | InventoryOnhandPEOOrigDateReceived | ORIG_DATE_RECEIVED | — | — |
| 16 | InventoryOnhandPEOOrigSourceTxnId | ORIG_SOURCE_TXN_ID | — | — |
| 17 | InventoryOnhandPEOOwningEntityId | OWNING_ENTITY_ID | — | ✅ |
| 18 | InventoryOnhandPEOOwningType | OWNING_TYPE | — | ✅ |
| 19 | InventoryOnhandPEOPrimaryTransactionQuantity | PRIMARY_TRANSACTION_QUANTITY | — | ✅ |
| 20 | InventoryOnhandPEOProjectId | PROJECT_ID | — | — |
| 21 | InventoryOnhandPEORevision | REVISION | — | — |
| 22 | InventoryOnhandPEOSecondaryTransactionQuantity | SECONDARY_TRANSACTION_QUANTITY | — | ✅ |
| 23 | InventoryOnhandPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 24 | InventoryOnhandPEOStandardPackQuantity | STANDARD_PACK_QUANTITY | — | — |
| 25 | InventoryOnhandPEOStandardPackUom | STANDARD_PACK_UOM | — | — |
| 26 | InventoryOnhandPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 27 | InventoryOnhandPEOTaskId | TASK_ID | — | — |
| 28 | InventoryOnhandPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 29 | InventoryOnhandPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 30 | InventoryOnhandPEOUpdateTransactionId | UPDATE_TRANSACTION_ID | — | — |
| 31 | OnhandQuantitiesId | ONHAND_QUANTITIES_ID | 🔑 | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryOnhandPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 2 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | VendorId | VENDOR_ID | — | — |
| 4 | VendorSiteCode | VENDOR_SITE_CODE | — | — |
| 5 | VendorSiteId | VENDOR_SITE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
