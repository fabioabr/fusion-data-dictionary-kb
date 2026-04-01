---
id: DOC-OTHER-PVO-ItemInterface
doc_type: system-doc
title: "ItemInterface — PVO Cross-Module"
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
  - ItemInterface
  - iteminterface
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemInterface

## 📌 Visão Geral

View Object para extração BICC de dados de Item Interface. Acessa as tabelas: EGP_SYSTEM_ITEMS_INTERFACE.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.ItemInterface`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 357 | 1 | 1 | 15 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_interface|EGP_SYSTEM_ITEMS_INTERFACE]] — 357 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[egp_system_items_interface|EGP_SYSTEM_ITEMS_INTERFACE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | AccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 3 | AllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 4 | AllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 5 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 6 | AllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | — |
| 7 | AllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | — |
| 8 | AllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 9 | AllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 10 | AsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 11 | AssetClass | ASSET_CLASS | — | — |
| 12 | AssetTrackedFlag | ASSET_TRACKED_FLAG | — | — |
| 13 | AtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 14 | AtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 15 | AtpFlag | ATP_FLAG | — | — |
| 16 | AtpRuleId | ATP_RULE_ID | — | — |
| 17 | AutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 18 | AutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 19 | AutoRelTimeFenceCode | AUTO_REL_TIME_FENCE_CODE | — | — |
| 20 | AutoRelTimeFenceDays | AUTO_REL_TIME_FENCE_DAYS | — | — |
| 21 | AutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 22 | BackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 23 | BackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 24 | BaseItemId | BASE_ITEM_ID | — | — |
| 25 | BaseItemNumber | BASE_ITEM_NUMBER | — | — |
| 26 | BatchId | BATCH_ID | — | ✅ |
| 27 | BatchNumber | BATCH_NUMBER | — | — |
| 28 | BomItemType | BOM_ITEM_TYPE | — | — |
| 29 | BuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 30 | BulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 31 | BundleId | BUNDLE_ID | — | — |
| 32 | BuyerId | BUYER_ID | — | — |
| 33 | CarryingCost | CARRYING_COST | — | — |
| 34 | CartonizationGroupId | CARTONIZATION_GROUP_ID | — | — |
| 35 | CasNumber | CAS_NUMBER | — | — |
| 36 | ChangeId | CHANGE_ID | — | — |
| 37 | ChangeLineId | CHANGE_LINE_ID | — | — |
| 38 | ChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 39 | ChargePeriodicityName | CHARGE_PERIODICITY_NAME | — | — |
| 40 | CheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 41 | ChildLotFlag | CHILD_LOT_FLAG | — | — |
| 42 | ChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 43 | ChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 44 | ChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 45 | CollateralFlag | COLLATERAL_FLAG | — | — |
| 46 | CommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 47 | ConfigMatch | CONFIG_MATCH | — | — |
| 48 | ConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 49 | ConfigOrgs | CONFIG_ORGS | — | — |
| 50 | ConfirmStatus | CONFIRM_STATUS | — | ✅ |
| 51 | ConsignedFlag | CONSIGNED_FLAG | — | — |
| 52 | ContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 53 | ContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 54 | ContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 55 | CopyItemId | COPY_ITEM_ID | — | — |
| 56 | CopyItemNumber | COPY_ITEM_NUMBER | — | — |
| 57 | CopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 58 | CopyOrganizationCode | COPY_ORGANIZATION_CODE | — | — |
| 59 | CopyOrganizationId | COPY_ORGANIZATION_ID | — | — |
| 60 | CopyRevisionId | COPY_REVISION_ID | — | — |
| 61 | CostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 62 | CoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 63 | CreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 64 | CreatedBy | CREATED_BY | — | ✅ |
| 65 | CreationDate | CREATION_DATE | — | ✅ |
| 66 | CriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 67 | CumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 68 | CumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 69 | CurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 70 | CurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 71 | CustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 72 | CustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 73 | CycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 74 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 75 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 76 | DaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 77 | DaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 78 | DaysOfCover | DAYS_OF_COVER | — | — |
| 79 | DaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 80 | DaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 81 | DefaultGrade | DEFAULT_GRADE | — | — |
| 82 | DefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 83 | DefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 84 | DefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 85 | DefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 86 | DefaultShippingOrgCode | DEFAULT_SHIPPING_ORG_CODE | — | — |
| 87 | DefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 88 | DefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 89 | DemandPeriod | DEMAND_PERIOD | — | — |
| 90 | DemandSourceHeaderId | DEMAND_SOURCE_HEADER_ID | — | — |
| 91 | DemandSourceLine | DEMAND_SOURCE_LINE | — | — |
| 92 | DemandSourceType | DEMAND_SOURCE_TYPE | — | — |
| 93 | DemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 94 | DemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 95 | Description | DESCRIPTION | — | — |
| 96 | DimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 97 | DimensionUomName | DIMENSION_UOM_NAME | — | — |
| 98 | DownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 99 | DqCompletionStatus | DQ_COMPLETION_STATUS | — | ✅ |
| 100 | DqDataType | DQ_DATA_TYPE | — | ✅ |
| 101 | DqSemanticKey | DQ_SEMANTIC_KEY | — | — |
| 102 | DrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 103 | DualUomControl | DUAL_UOM_CONTROL | — | — |
| 104 | DualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 105 | DualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 106 | EffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 107 | ElectronicFlag | ELECTRONIC_FLAG | — | — |
| 108 | EligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 109 | EnabledFlag | ENABLED_FLAG | — | — |
| 110 | EndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 111 | EndDateActive | END_DATE_ACTIVE | — | — |
| 112 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 113 | EngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 114 | EquipmentType | EQUIPMENT_TYPE | — | — |
| 115 | EventFlag | EVENT_FLAG | — | — |
| 116 | ExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 117 | ExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 118 | ExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 119 | FinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 120 | FixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 121 | FixedLeadTime | FIXED_LEAD_TIME | — | — |
| 122 | FixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 123 | FixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 124 | ForecastHorizon | FORECAST_HORIZON | — | — |
| 125 | FullLeadTime | FULL_LEAD_TIME | — | — |
| 126 | GdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 127 | GlobalTradeItemNumber | GLOBAL_TRADE_ITEM_NUMBER | — | — |
| 128 | GpcCode | GPC_CODE | — | — |
| 129 | GradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 130 | GtinDescription | GTIN_DESCRIPTION | — | — |
| 131 | HazardClassCode | HAZARD_CLASS_CODE | — | — |
| 132 | HazardClassId | HAZARD_CLASS_ID | — | — |
| 133 | HazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 134 | HoldDays | HOLD_DAYS | — | — |
| 135 | IndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 136 | InternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 137 | InternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 138 | InternalVolume | INTERNAL_VOLUME | — | — |
| 139 | IntraBatchMatchParent | INTRA_BATCH_MATCH_PARENT | — | — |
| 140 | IntraBatchMatchStatus | INTRA_BATCH_MATCH_STATUS | — | — |
| 141 | IntraBatchMatchedSsref | INTRA_BATCH_MATCHED_SSREF | — | — |
| 142 | InventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 143 | InventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 144 | InventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 145 | InventoryItemId | INVENTORY_ITEM_ID | — | — |
| 146 | InventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 147 | InventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 148 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 149 | InvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 150 | InvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 151 | InvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 152 | InvoicingRuleId | INVOICING_RULE_ID | — | — |
| 153 | ItemCatalogGroupId | ITEM_CLASS_ID | — | ✅ |
| 154 | ItemCatalogGroupName | ITEM_CLASS_NAME | — | — |
| 155 | ItemNumber | ITEM_NUMBER | — | — |
| 156 | ItemType | ITEM_TYPE | — | — |
| 157 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 158 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 159 | LastMatchActionDate | LAST_MATCH_DATE | — | ✅ |
| 160 | LastMatchDate | LAST_MATCH_DATE | — | — |
| 161 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 162 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 163 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 164 | LeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 165 | ListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 166 | LocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 167 | LongDescription | LONG_DESCRIPTION | — | — |
| 168 | LotControlCode | LOT_CONTROL_CODE | — | — |
| 169 | LotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 170 | LotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 171 | LotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 172 | LotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 173 | LotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 174 | LotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 175 | MarketPrice | MARKET_PRICE | — | — |
| 176 | MatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 177 | MatchCount1 | MATCH_COUNT | — | — |
| 178 | MaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 179 | MaterialCost | MATERIAL_COST | — | — |
| 180 | MaterialOhRate | MATERIAL_OH_RATE | — | — |
| 181 | MaterialOhSubElem | MATERIAL_OH_SUB_ELEM | — | — |
| 182 | MaterialOhSubElemId | MATERIAL_OH_SUB_ELEM_ID | — | — |
| 183 | MaterialSubElem | MATERIAL_SUB_ELEM | — | — |
| 184 | MaterialSubElemId | MATERIAL_SUB_ELEM_ID | — | — |
| 185 | MaturityDays | MATURITY_DAYS | — | — |
| 186 | MaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 187 | MaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 188 | MaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 189 | MessageId | MESSAGE_ID | — | — |
| 190 | MessageTimestamp | MESSAGE_TIMESTAMP | — | — |
| 191 | MinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 192 | MinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 193 | MinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 194 | MinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 195 | MrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 196 | MrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 197 | MtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 198 | MustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 199 | NegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 200 | NegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 201 | NirRequired | NIR_REQUIRED | — | — |
| 202 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 203 | OntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 204 | Operation | OPERATION | — | — |
| 205 | OperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 206 | OrderCost | ORDER_COST | — | — |
| 207 | OrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 208 | OrganizationCode | ORGANIZATION_CODE | — | — |
| 209 | OrganizationId | ORGANIZATION_ID | — | — |
| 210 | OverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 211 | OverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 212 | OvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 213 | OvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 214 | ParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 215 | PaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 216 | PaymentTermsName | PAYMENT_TERMS_NAME | — | — |
| 217 | PhaseNumber | PHASE_NUMBER | — | — |
| 218 | PickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 219 | PickingRuleId | PICKING_RULE_ID | — | — |
| 220 | PlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 221 | PlannerCode | PLANNER_CODE | — | — |
| 222 | PlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 223 | PlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 224 | PlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 225 | PositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 226 | PostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 227 | PrepositionPoint | PREPOSITION_POINT | — | — |
| 228 | PreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 229 | PriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 230 | PrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 231 | PrimaryUomName | PRIMARY_UOM_NAME | — | — |
| 232 | ProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 233 | ProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 234 | ProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 235 | ProcessStatus | PROCESS_STATUS | — | ✅ |
| 236 | ProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 237 | ProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 238 | ProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 239 | ProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 240 | ProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 241 | PurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 242 | PurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 243 | PurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 244 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 245 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 246 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 247 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 248 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 249 | RecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 250 | RecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 251 | ReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 252 | ReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 253 | RepairLeadtime | REPAIR_LEADTIME | — | — |
| 254 | RepairProgram | REPAIR_PROGRAM | — | — |
| 255 | RepairYield | REPAIR_YIELD | — | — |
| 256 | ReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 257 | RequestId | REQUEST_ID | — | — |
| 258 | RequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | — |
| 259 | RequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | — |
| 260 | ReservableType | RESERVABLE_TYPE | — | — |
| 261 | RestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 262 | RestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 263 | RetestInterval | RETEST_INTERVAL | — | — |
| 264 | ReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 265 | ReturnableFlag | RETURNABLE_FLAG | — | — |
| 266 | Revision | REVISION | — | — |
| 267 | RevisionImportPolicy | REVISION_IMPORT_POLICY | — | — |
| 268 | RevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 269 | RoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 270 | RoundingFactor | ROUNDING_FACTOR | — | — |
| 271 | SafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 272 | SalesProductType | SALES_PRODUCT_TYPE | — | — |
| 273 | SecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 274 | SecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 275 | SecondaryUomName | SECONDARY_UOM_NAME | — | — |
| 276 | SerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 277 | SerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 278 | ServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 279 | ServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 280 | ServiceDuration | SERVICE_DURATION | — | — |
| 281 | ServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 282 | ServiceDurationPeriodName | SERVICE_DURATION_PERIOD_NAME | — | — |
| 283 | ServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | — |
| 284 | ServiceStartDelay | SERVICE_START_DELAY | — | — |
| 285 | ServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | — |
| 286 | ServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 287 | ServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 288 | ShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 289 | ShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 290 | ShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 291 | ShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 292 | ShrinkageRate | SHRINKAGE_RATE | — | — |
| 293 | SoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 294 | SoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 295 | SourceOrganizationCode | SOURCE_ORGANIZATION_CODE | — | — |
| 296 | SourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 297 | SourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 298 | SourceSystemCode | SOURCE_SYSTEM_CODE | — | — |
| 299 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 300 | SourceSystemReference | SOURCE_SYSTEM_REFERENCE | — | ✅ |
| 301 | SourceSystemReferenceDesc | SOURCE_SYSTEM_REFERENCE_DESC | — | — |
| 302 | SourceType | SOURCE_TYPE | — | — |
| 303 | StartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 304 | StartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 305 | StartDateActive | START_DATE_ACTIVE | — | — |
| 306 | StdLotSize | STD_LOT_SIZE | — | — |
| 307 | StockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 308 | StyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 309 | StyleItemId | STYLE_ITEM_ID | — | — |
| 310 | StyleItemNumber | STYLE_ITEM_NUMBER | — | — |
| 311 | SubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 312 | SubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 313 | SubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 314 | SummaryFlag | SUMMARY_FLAG | — | — |
| 315 | TaxCode | TAX_CODE | — | — |
| 316 | TaxableFlag | TAXABLE_FLAG | — | — |
| 317 | TemplateId | TEMPLATE_ID | — | — |
| 318 | TemplateName | TEMPLATE_NAME | — | — |
| 319 | ThreadNumber | THREAD_NUMBER | — | — |
| 320 | TopItemFlag | TOP_ITEM_FLAG | — | — |
| 321 | TrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 322 | TradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 323 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 324 | TransactionType | TRANSACTION_TYPE | — | ✅ |
| 325 | UnNumberCode | UN_NUMBER_CODE | — | — |
| 326 | UnNumberId | UN_NUMBER_ID | — | — |
| 327 | UnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 328 | UnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 329 | UnitHeight | UNIT_HEIGHT | — | — |
| 330 | UnitLength | UNIT_LENGTH | — | — |
| 331 | UnitOfIssue | UNIT_OF_ISSUE | — | — |
| 332 | UnitVolume | UNIT_VOLUME | — | — |
| 333 | UnitWeight | UNIT_WEIGHT | — | — |
| 334 | UnitWidth | UNIT_WIDTH | — | — |
| 335 | VariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 336 | VehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 337 | VersionEnabledFlag | VERSION_ENABLED_FLAG | — | — |
| 338 | VersionId | VERSION_ID | — | — |
| 339 | VersionLabel | VERSION_LABEL | — | — |
| 340 | VersionRevisionCode | VERSION_REVISION_CODE | — | — |
| 341 | VersionRevisionId | VERSION_REVISION_ID | — | — |
| 342 | VersionStartDate | VERSION_START_DATE | — | — |
| 343 | VmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 344 | VmiForecastType | VMI_FORECAST_TYPE | — | — |
| 345 | VmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 346 | VmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 347 | VmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 348 | VmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 349 | VolumeUomCode | VOLUME_UOM_CODE | — | — |
| 350 | VolumeUomName | VOLUME_UOM_NAME | — | — |
| 351 | WebStatus | WEB_STATUS | — | — |
| 352 | WeightUomCode | WEIGHT_UOM_CODE | — | — |
| 353 | WeightUomName | WEIGHT_UOM_NAME | — | — |
| 354 | WhUpdateDate | WH_UPDATE_DATE | — | — |
| 355 | WipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 356 | WipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 357 | WipSupplyType | WIP_SUPPLY_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
