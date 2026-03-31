---
id: DOC-OTHER-PVO-CycleCountPVO
doc_type: system-doc
title: "CycleCountPVO — PVO Cross-Module"
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
  - CycleCountPVO
  - cyclecountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CycleCountPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cycle Count. Acessa as tabelas: EGP_SYSTEM_ITEMS_B_V, HZ_PARTIES, INV_ABC_ASSIGNMENT_GROUPS (+8).

**Caminho:** `FscmTopModelAM.InventoryAM.CycleCountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 475 | 11 | 2 | 88 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 300 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]] — 3 atributos (1 BICC)
- [[inv_cc_subinventories|INV_CC_SUBINVENTORIES]] — 13 atributos (3 BICC)
- [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]] — 20 atributos (9 BICC)
- [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]] — 56 atributos (1 PKs, 35 BICC)
- [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]] — 47 atributos (24 BICC)
- [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]] — 20 atributos (7 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (1 PKs, 4 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 3 atributos
- [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MSIItemNumber | ITEM_NUMBER | — | — |
| 2 | MSIPeoAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 3 | MSIPeoAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 4 | MSIPeoAcdType | ACD_TYPE | — | — |
| 5 | MSIPeoAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 6 | MSIPeoAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 7 | MSIPeoAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 8 | MSIPeoAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 9 | MSIPeoAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 10 | MSIPeoApprovalStatus | APPROVAL_STATUS | — | — |
| 11 | MSIPeoAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 12 | MSIPeoAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 13 | MSIPeoAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 14 | MSIPeoAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 15 | MSIPeoAtpFlag | ATP_FLAG | — | — |
| 16 | MSIPeoAtpRuleId | ATP_RULE_ID | — | — |
| 17 | MSIPeoAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 18 | MSIPeoAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 19 | MSIPeoAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 20 | MSIPeoBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 21 | MSIPeoBaseItemId | BASE_ITEM_ID | — | — |
| 22 | MSIPeoBomItemType | BOM_ITEM_TYPE | — | — |
| 23 | MSIPeoBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 24 | MSIPeoBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 25 | MSIPeoBuyerId | BUYER_ID | — | — |
| 26 | MSIPeoCarryingCost | CARRYING_COST | — | — |
| 27 | MSIPeoCasNumber | CAS_NUMBER | — | — |
| 28 | MSIPeoChangeBitMap | CHANGE_BIT_MAP | — | — |
| 29 | MSIPeoChangeLineId | CHANGE_LINE_ID | — | — |
| 30 | MSIPeoChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 31 | MSIPeoCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 32 | MSIPeoChildLotFlag | CHILD_LOT_FLAG | — | — |
| 33 | MSIPeoChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 34 | MSIPeoChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 35 | MSIPeoChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 36 | MSIPeoCollateralFlag | COLLATERAL_FLAG | — | — |
| 37 | MSIPeoCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 38 | MSIPeoCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 39 | MSIPeoConfigMatch | CONFIG_MATCH | — | — |
| 40 | MSIPeoConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 41 | MSIPeoConfigOrgs | CONFIG_ORGS | — | — |
| 42 | MSIPeoConsignedFlag | CONSIGNED_FLAG | — | — |
| 43 | MSIPeoContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 44 | MSIPeoContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 45 | MSIPeoCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 46 | MSIPeoCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 47 | MSIPeoCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 48 | MSIPeoCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 49 | MSIPeoCreatedBy | CREATED_BY | — | — |
| 50 | MSIPeoCreationDate | CREATION_DATE | — | — |
| 51 | MSIPeoCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 52 | MSIPeoCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 53 | MSIPeoCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 54 | MSIPeoCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 55 | MSIPeoCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 56 | MSIPeoCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 57 | MSIPeoCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 58 | MSIPeoCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 59 | MSIPeoDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 60 | MSIPeoDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 61 | MSIPeoDaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 62 | MSIPeoDaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 63 | MSIPeoDaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 64 | MSIPeoDaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 65 | MSIPeoDefaultGrade | DEFAULT_GRADE | — | — |
| 66 | MSIPeoDefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 67 | MSIPeoDefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 68 | MSIPeoDefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 69 | MSIPeoDefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 70 | MSIPeoDefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 71 | MSIPeoDefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 72 | MSIPeoDefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 73 | MSIPeoDemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 74 | MSIPeoDemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 75 | MSIPeoDimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 76 | MSIPeoDownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 77 | MSIPeoDrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 78 | MSIPeoDualUomControl | DUAL_UOM_CONTROL | — | — |
| 79 | MSIPeoDualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 80 | MSIPeoDualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 81 | MSIPeoEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 82 | MSIPeoEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 83 | MSIPeoEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 84 | MSIPeoEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 85 | MSIPeoEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 86 | MSIPeoEamItemType | EAM_ITEM_TYPE | — | — |
| 87 | MSIPeoEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 88 | MSIPeoElectronicFlag | ELECTRONIC_FLAG | — | — |
| 89 | MSIPeoEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 90 | MSIPeoEnabledFlag | ENABLED_FLAG | — | — |
| 91 | MSIPeoEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 92 | MSIPeoEndDateActive | END_DATE_ACTIVE | — | — |
| 93 | MSIPeoEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 94 | MSIPeoEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 95 | MSIPeoEquipmentType | EQUIPMENT_TYPE | — | — |
| 96 | MSIPeoEventFlag | EVENT_FLAG | — | — |
| 97 | MSIPeoExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 98 | MSIPeoExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 99 | MSIPeoExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 100 | MSIPeoExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 101 | MSIPeoFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 102 | MSIPeoFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 103 | MSIPeoFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 104 | MSIPeoFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 105 | MSIPeoFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 106 | MSIPeoForecastHorizon | FORECAST_HORIZON | — | — |
| 107 | MSIPeoFullLeadTime | FULL_LEAD_TIME | — | — |
| 108 | MSIPeoGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 109 | MSIPeoGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 110 | MSIPeoHazardClassId | HAZARD_CLASS_ID | — | — |
| 111 | MSIPeoHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 112 | MSIPeoHoldDays | HOLD_DAYS | — | — |
| 113 | MSIPeoIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 114 | MSIPeoImplementationDate | IMPLEMENTATION_DATE | — | — |
| 115 | MSIPeoIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 116 | MSIPeoInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 117 | MSIPeoInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 118 | MSIPeoInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 119 | MSIPeoInternalVolume | INTERNAL_VOLUME | — | — |
| 120 | MSIPeoInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 121 | MSIPeoInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 122 | MSIPeoInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 123 | MSIPeoInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 124 | MSIPeoInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 125 | MSIPeoInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 126 | MSIPeoInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 127 | MSIPeoInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 128 | MSIPeoInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 129 | MSIPeoInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 130 | MSIPeoInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 131 | MSIPeoInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 132 | MSIPeoItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 133 | MSIPeoItemNumber | ITEM_NUMBER | — | ✅ |
| 134 | MSIPeoItemType | ITEM_TYPE | — | — |
| 135 | MSIPeoJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 136 | MSIPeoJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 137 | MSIPeoLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 138 | MSIPeoLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 139 | MSIPeoLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 140 | MSIPeoLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 141 | MSIPeoLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 142 | MSIPeoListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 143 | MSIPeoLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 144 | MSIPeoLotControlCode | LOT_CONTROL_CODE | — | — |
| 145 | MSIPeoLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 146 | MSIPeoLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 147 | MSIPeoLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 148 | MSIPeoLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 149 | MSIPeoLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 150 | MSIPeoLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 151 | MSIPeoMarketPrice | MARKET_PRICE | — | — |
| 152 | MSIPeoMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 153 | MSIPeoMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 154 | MSIPeoMaturityDays | MATURITY_DAYS | — | — |
| 155 | MSIPeoMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 156 | MSIPeoMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 157 | MSIPeoMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 158 | MSIPeoMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 159 | MSIPeoMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 160 | MSIPeoMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 161 | MSIPeoMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 162 | MSIPeoMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 163 | MSIPeoMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 164 | MSIPeoMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 165 | MSIPeoMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 166 | MSIPeoNegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 167 | MSIPeoNegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 168 | MSIPeoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 169 | MSIPeoOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 170 | MSIPeoOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 171 | MSIPeoOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 172 | MSIPeoOrderCost | ORDER_COST | — | — |
| 173 | MSIPeoOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 174 | MSIPeoOrganizationId | ORGANIZATION_ID | — | — |
| 175 | MSIPeoOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 176 | MSIPeoOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | — |
| 177 | MSIPeoOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 178 | MSIPeoOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 179 | MSIPeoOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 180 | MSIPeoOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 181 | MSIPeoOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 182 | MSIPeoParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 183 | MSIPeoPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 184 | MSIPeoPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 185 | MSIPeoPickingRuleId | PICKING_RULE_ID | — | — |
| 186 | MSIPeoPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 187 | MSIPeoPlannerCode | PLANNER_CODE | — | — |
| 188 | MSIPeoPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 189 | MSIPeoPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 190 | MSIPeoPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 191 | MSIPeoPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 192 | MSIPeoPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 193 | MSIPeoPrepositionPoint | PREPOSITION_POINT | — | — |
| 194 | MSIPeoPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 195 | MSIPeoPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 196 | MSIPeoPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 197 | MSIPeoProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 198 | MSIPeoProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 199 | MSIPeoProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 200 | MSIPeoProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 201 | MSIPeoProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 202 | MSIPeoProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 203 | MSIPeoProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 204 | MSIPeoProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 205 | MSIPeoProgramAppName | PROGRAM_APP_NAME | — | — |
| 206 | MSIPeoProgramName | PROGRAM_NAME | — | — |
| 207 | MSIPeoPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 208 | MSIPeoPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 209 | MSIPeoPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 210 | MSIPeoQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 211 | MSIPeoQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 212 | MSIPeoQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 213 | MSIPeoReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 214 | MSIPeoReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 215 | MSIPeoReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 216 | MSIPeoReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 217 | MSIPeoRecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 218 | MSIPeoRecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 219 | MSIPeoReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 220 | MSIPeoReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 221 | MSIPeoRepairLeadtime | REPAIR_LEADTIME | — | — |
| 222 | MSIPeoRepairProgram | REPAIR_PROGRAM | — | — |
| 223 | MSIPeoRepairYield | REPAIR_YIELD | — | — |
| 224 | MSIPeoReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 225 | MSIPeoRequestId | REQUEST_ID | — | — |
| 226 | MSIPeoReservableType | RESERVABLE_TYPE | — | — |
| 227 | MSIPeoRestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 228 | MSIPeoRestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 229 | MSIPeoRetestInterval | RETEST_INTERVAL | — | — |
| 230 | MSIPeoReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 231 | MSIPeoReturnableFlag | RETURNABLE_FLAG | — | — |
| 232 | MSIPeoRevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 233 | MSIPeoRoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 234 | MSIPeoRoundingFactor | ROUNDING_FACTOR | — | — |
| 235 | MSIPeoSalesAccount | SALES_ACCOUNT | — | — |
| 236 | MSIPeoSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 237 | MSIPeoSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 238 | MSIPeoSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 239 | MSIPeoSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 240 | MSIPeoSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 241 | MSIPeoServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 242 | MSIPeoServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 243 | MSIPeoServiceDuration | SERVICE_DURATION | — | — |
| 244 | MSIPeoServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 245 | MSIPeoServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 246 | MSIPeoServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 247 | MSIPeoShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 248 | MSIPeoShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 249 | MSIPeoShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 250 | MSIPeoShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 251 | MSIPeoShrinkageRate | SHRINKAGE_RATE | — | — |
| 252 | MSIPeoSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 253 | MSIPeoSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 254 | MSIPeoSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 255 | MSIPeoSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 256 | MSIPeoSourceType | SOURCE_TYPE | — | — |
| 257 | MSIPeoStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 258 | MSIPeoStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 259 | MSIPeoStartDateActive | START_DATE_ACTIVE | — | — |
| 260 | MSIPeoStdLotSize | STD_LOT_SIZE | — | — |
| 261 | MSIPeoStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 262 | MSIPeoStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 263 | MSIPeoStyleItemId | STYLE_ITEM_ID | — | — |
| 264 | MSIPeoSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 265 | MSIPeoSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 266 | MSIPeoSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 267 | MSIPeoSummaryFlag | SUMMARY_FLAG | — | — |
| 268 | MSIPeoTaxCode | TAX_CODE | — | — |
| 269 | MSIPeoTaxableFlag | TAXABLE_FLAG | — | — |
| 270 | MSIPeoTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 271 | MSIPeoTemplateName | ITEM_NUMBER | — | — |
| 272 | MSIPeoTrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 273 | MSIPeoTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 274 | MSIPeoUnNumberId | UN_NUMBER_ID | — | — |
| 275 | MSIPeoUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 276 | MSIPeoUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 277 | MSIPeoUnitHeight | UNIT_HEIGHT | — | — |
| 278 | MSIPeoUnitLength | UNIT_LENGTH | — | — |
| 279 | MSIPeoUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 280 | MSIPeoUnitVolume | UNIT_VOLUME | — | — |
| 281 | MSIPeoUnitWeight | UNIT_WEIGHT | — | — |
| 282 | MSIPeoUnitWidth | UNIT_WIDTH | — | — |
| 283 | MSIPeoVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 284 | MSIPeoVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 285 | MSIPeoVersionEndDate | VERSION_END_DATE | — | — |
| 286 | MSIPeoVersionId | VERSION_ID | — | — |
| 287 | MSIPeoVersionStartDate | VERSION_START_DATE | — | — |
| 288 | MSIPeoVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 289 | MSIPeoVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 290 | MSIPeoVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 291 | MSIPeoVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 292 | MSIPeoVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 293 | MSIPeoVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 294 | MSIPeoVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 295 | MSIPeoWebStatus | WEB_STATUS | — | — |
| 296 | MSIPeoWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 297 | MSIPeoWhUpdateDate | WH_UPDATE_DATE | — | — |
| 298 | MSIPeoWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 299 | MSIPeoWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 300 | MSIPeoWipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

### [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupPEOAssignmentGroupName | ASSIGNMENT_GROUP_NAME | — | ✅ |
| 2 | AbcAssignmentGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | AssignmentGroupId | ASSIGNMENT_GROUP_ID | — | — |

### [[inv_cc_subinventories|INV_CC_SUBINVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvCCSubinventoriesCreatedBy | CREATED_BY | — | — |
| 2 | InvCCSubinventoriesCreationDate | CREATION_DATE | — | — |
| 3 | InvCCSubinventoriesCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 4 | InvCCSubinventoriesIncludeInCount | INCLUDE_IN_COUNT | — | ✅ |
| 5 | InvCCSubinventoriesJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | InvCCSubinventoriesJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | InvCCSubinventoriesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | InvCCSubinventoriesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | InvCCSubinventoriesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | InvCCSubinventoriesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InvCCSubinventoriesOrganizationId | ORGANIZATION_ID | — | — |
| 12 | InvCCSubinventoriesRequestId | REQUEST_ID | — | — |
| 13 | InvCCSubinventoriesSubinventory | SUBINVENTORY | — | ✅ |

### [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCCPeoAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | — |
| 2 | ICCCPeoAbcClassId | ABC_CLASS_ID | — | ✅ |
| 3 | ICCCPeoApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 4 | ICCCPeoApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 5 | ICCCPeoCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 6 | ICCCPeoCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 7 | ICCCPeoCreatedBy | CREATED_BY | — | — |
| 8 | ICCCPeoCreationDate | CREATION_DATE | — | — |
| 9 | ICCCPeoCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 10 | ICCCPeoHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | ✅ |
| 11 | ICCCPeoHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | ✅ |
| 12 | ICCCPeoJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ICCCPeoJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ICCCPeoLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ICCCPeoLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ICCCPeoLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ICCCPeoNumCountsPerYear | NUM_COUNTS_PER_YEAR | — | ✅ |
| 18 | ICCCPeoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ICCCPeoOrganizationId | ORGANIZATION_ID | — | — |
| 20 | ICCCPeoRequestId | REQUEST_ID | — | — |

### [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | AdjustmentDate | ADJUSTMENT_DATE | — | ✅ |
| 3 | AdjustmentQuantity | ADJUSTMENT_QUANTITY | — | ✅ |
| 4 | ApprovalDate | APPROVAL_DATE | — | ✅ |
| 5 | ApprovalType | APPROVAL_TYPE | — | ✅ |
| 6 | ApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 7 | Comments | COMMENTS | — | — |
| 8 | CountDate | COUNT_DATE | — | ✅ |
| 9 | CountDueDate | COUNT_DUE_DATE | — | ✅ |
| 10 | CountListSequence | COUNT_LIST_SEQUENCE | — | ✅ |
| 11 | CountQuantity | COUNT_QUANTITY | — | ✅ |
| 12 | CountSecondaryUom | COUNT_SECONDARY_UOM | — | ✅ |
| 13 | CountTypeCode | COUNT_TYPE_CODE | — | ✅ |
| 14 | CountUom | COUNT_UOM | — | ✅ |
| 15 | CountedByEmployeeId | COUNTED_BY_EMPLOYEE_ID | — | — |
| 16 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 17 | CreatedBy | CREATED_BY | — | ✅ |
| 18 | CreationDate | CREATION_DATE | — | ✅ |
| 19 | CycleCountEntryId | CYCLE_COUNT_ENTRY_ID | 🔑 | ✅ |
| 20 | CycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | ✅ |
| 21 | EntryStatusCode | ENTRY_STATUS_CODE | — | ✅ |
| 22 | ExportFlag | EXPORT_FLAG | — | ✅ |
| 23 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 24 | ItemLotControlCode | ITEM_LOT_CONTROL_CODE | — | — |
| 25 | ItemRevisionQtyControlCode | ITEM_REVISION_QTY_CONTROL_CODE | — | — |
| 26 | ItemSerialControlCode | ITEM_SERIAL_CONTROL_CODE | — | — |
| 27 | ItemUnitCost | ITEM_UNIT_COST | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | LocatorId | LOCATOR_ID | — | ✅ |
| 34 | LotNumber | LOT_NUMBER | — | ✅ |
| 35 | NumberOfCounts | NUMBER_OF_COUNTS | — | ✅ |
| 36 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 38 | OutermostLpnId | OUTERMOST_LPN_ID | — | — |
| 39 | OwningEntityId | OWNING_ENTITY_ID | — | — |
| 40 | OwningType | OWNING_TYPE | — | ✅ |
| 41 | ParentLpnId | PARENT_LPN_ID | — | — |
| 42 | PrimaryUomQuantity | PRIMARY_UOM_QUANTITY | — | ✅ |
| 43 | ProjectId | PROJECT_ID | — | — |
| 44 | RequestId | REQUEST_ID | — | — |
| 45 | Revision | REVISION | — | ✅ |
| 46 | SecondaryAdjustmentQuantity | SECONDARY_ADJUSTMENT_QUANTITY | — | ✅ |
| 47 | SecondarySystemQty | SECONDARY_SYSTEM_QTY | — | ✅ |
| 48 | SecondaryUomQuantity | SECONDARY_UOM_QUANTITY | — | ✅ |
| 49 | SerialDetail | SERIAL_DETAIL | — | — |
| 50 | SerialNumber | SERIAL_NUMBER | — | ✅ |
| 51 | StandardOperationId | STANDARD_OPERATION_ID | — | — |
| 52 | Subinventory | SUBINVENTORY | — | ✅ |
| 53 | SystemQuantity | SYSTEM_QUANTITY | — | ✅ |
| 54 | TaskId | TASK_ID | — | — |
| 55 | TaskPriority | TASK_PRIORITY | — | — |
| 56 | TransactionReasonId | TRANSACTION_REASON_ID | — | — |

### [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutoscheduleEnabledFlag | AUTOSCHEDULE_ENABLED_FLAG | — | ✅ |
| 2 | ICCHPeoAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | — |
| 3 | ICCHPeoAbcInitializationStatus | ABC_INITIALIZATION_STATUS | — | — |
| 4 | ICCHPeoAllowSerialItems | ALLOW_SERIAL_ITEMS | — | ✅ |
| 5 | ICCHPeoApprovalOptionCode | APPROVAL_OPTION_CODE | — | — |
| 6 | ICCHPeoApprovalRequired | APPROVAL_REQUIRED | — | ✅ |
| 7 | ICCHPeoApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 8 | ICCHPeoApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 9 | ICCHPeoContainerAdjustmentOption | CONTAINER_ADJUSTMENT_OPTION | — | — |
| 10 | ICCHPeoContainerDiscrepancyOption | CONTAINER_DISCREPANCY_OPTION | — | — |
| 11 | ICCHPeoContainerEnabledFlag | CONTAINER_ENABLED_FLAG | — | — |
| 12 | ICCHPeoCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 13 | ICCHPeoCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 14 | ICCHPeoCreatedBy | CREATED_BY | — | — |
| 15 | ICCHPeoCreationDate | CREATION_DATE | — | — |
| 16 | ICCHPeoCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 17 | ICCHPeoCycleCountHeaderName | CYCLE_COUNT_HEADER_NAME | — | ✅ |
| 18 | ICCHPeoDaysUntilLate | DAYS_UNTIL_LATE | — | ✅ |
| 19 | ICCHPeoDefaultApprover | DEFAULT_APPROVER | — | — |
| 20 | ICCHPeoDescription | DESCRIPTION | — | ✅ |
| 21 | ICCHPeoEndDate | END_DATE | — | — |
| 22 | ICCHPeoHeaderLastScheduleDate | HEADER_LAST_SCHEDULE_DATE | — | — |
| 23 | ICCHPeoHeaderNextScheduleDate | HEADER_NEXT_SCHEDULE_DATE | — | — |
| 24 | ICCHPeoHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | ✅ |
| 25 | ICCHPeoHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | ✅ |
| 26 | ICCHPeoJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | ICCHPeoJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | ICCHPeoLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | ICCHPeoLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | ICCHPeoLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | ICCHPeoMaximumAutoRecounts | MAXIMUM_AUTO_RECOUNTS | — | ✅ |
| 32 | ICCHPeoNextUserCountSequence | NEXT_USER_COUNT_SEQUENCE | — | ✅ |
| 33 | ICCHPeoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | ICCHPeoOnhandVisibleFlag | ONHAND_VISIBLE_FLAG | — | ✅ |
| 35 | ICCHPeoOrganizationId | ORGANIZATION_ID | — | — |
| 36 | ICCHPeoOverrideDefaultApprover | OVERRIDE_DEFAULT_APPROVER | — | — |
| 37 | ICCHPeoRequestId | REQUEST_ID | — | — |
| 38 | ICCHPeoScheduleIntervalTime | SCHEDULE_INTERVAL_TIME | — | ✅ |
| 39 | ICCHPeoSerialAdjustmentOption | SERIAL_ADJUSTMENT_OPTION | — | ✅ |
| 40 | ICCHPeoSerialCountOption | SERIAL_COUNT_OPTION | — | ✅ |
| 41 | ICCHPeoSerialDetailOption | SERIAL_DETAIL_OPTION | — | ✅ |
| 42 | ICCHPeoSerialDiscrepancyOption | SERIAL_DISCREPANCY_OPTION | — | ✅ |
| 43 | ICCHPeoStartDate | START_DATE | — | — |
| 44 | ICCHPeoUnscheduledCountEntry | UNSCHEDULED_COUNT_ENTRY | — | ✅ |
| 45 | ICCHPeoWorkdaySchedule | WORKDAY_SCHEDULE | — | — |
| 46 | ICCHPeoZeroCountFlag | ZERO_COUNT_FLAG | — | ✅ |
| 47 | ICCHStartManualCountsPrefix | START_MANUAL_COUNTS_PREFIX | — | ✅ |

### [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCIPeoAbcClassId | ABC_CLASS_ID | — | — |
| 2 | ICCIPeoApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 3 | ICCIPeoApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 4 | ICCIPeoCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 5 | ICCIPeoCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 6 | ICCIPeoCreatedBy | CREATED_BY | — | — |
| 7 | ICCIPeoCreationDate | CREATION_DATE | — | — |
| 8 | ICCIPeoCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 9 | ICCIPeoIncludeInSchedule | INCLUDE_IN_SCHEDULE | — | ✅ |
| 10 | ICCIPeoInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 11 | ICCIPeoItemLastScheduleDate | ITEM_LAST_SCHEDULE_DATE | — | ✅ |
| 12 | ICCIPeoJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ICCIPeoJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ICCIPeoLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ICCIPeoLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ICCIPeoLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ICCIPeoObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ICCIPeoOrganizationId | ORGANIZATION_ID | — | — |
| 19 | ICCIPeoRequestId | REQUEST_ID | — | — |
| 20 | ICCIPeoScheduleOrder | SCHEDULE_ORDER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEO1CountedByemployeeId | DISPLAY_NAME | — | ✅ |
| 2 | PersonNamePEO1EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNamePEO1EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 4 | PersonNamePEO1PersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonNamePEOApproverEmployeeId | DISPLAY_NAME | — | ✅ |
| 6 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 2 | VendorSiteCode | VENDOR_SITE_CODE | — | — |
| 3 | VendorSiteId | VENDOR_SITE_ID | — | — |

### [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ScheduleEOScheduleName | SCHEDULE_NAME | — | ✅ |
| 3 | ScheduleId | SCHEDULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
