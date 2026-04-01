---
id: DOC-OTHER-PVO-Dispute
doc_type: system-doc
title: "Dispute — PVO Cross-Module"
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
  - Dispute
  - dispute
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Dispute

## 📌 Visão Geral

View Object para extração BICC de dados de Dispute. Acessa as tabelas: CN_DISPUTES_ALL, CN_SRP_PARTICIPANTS_ALL, EGP_SYSTEM_ITEMS_VL (+3).

**Caminho:** `FscmTopModelAM.DisputeAM.Dispute`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 403 | 6 | 1 | 64 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[cn_disputes_all|CN_DISPUTES_ALL]] — 48 atributos (1 PKs, 22 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 24 atributos (14 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 294 atributos (9 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 25 atributos (14 BICC)
- [[hz_parties|HZ_PARTIES]] — 10 atributos (4 BICC)

---

## ⚙️ Atributos

### [[cn_disputes_all|CN_DISPUTES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualValue | ACTUAL_VALUE | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute2 | ATTRIBUTE2 | — | — |
| 10 | Attribute3 | ATTRIBUTE3 | — | — |
| 11 | Attribute4 | ATTRIBUTE4 | — | — |
| 12 | Attribute5 | ATTRIBUTE5 | — | — |
| 13 | Attribute6 | ATTRIBUTE6 | — | — |
| 14 | Attribute7 | ATTRIBUTE7 | — | — |
| 15 | Attribute8 | ATTRIBUTE8 | — | — |
| 16 | Attribute9 | ATTRIBUTE9 | — | — |
| 17 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ClosedDate | CLOSED_DATE | — | ✅ |
| 19 | CreatedBy | CREATED_BY | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | CustomerId | CUSTOMER_ID | — | — |
| 23 | DisputeDescription | DISPUTE_DESCRIPTION | — | ✅ |
| 24 | DisputeId | DISPUTE_ID | 🔑 | ✅ |
| 25 | DisputeJustification | DISPUTE_JUSTIFICATION | — | ✅ |
| 26 | DisputeName | DISPUTE_NAME | — | ✅ |
| 27 | DisputeStatus | DISPUTE_STATUS | — | ✅ |
| 28 | DisputeType | DISPUTE_TYPE | — | ✅ |
| 29 | ExpectedValue | EXPECTED_VALUE | — | ✅ |
| 30 | InventoryItemId | INVENTORY_ITEM_ID | — | — |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | OrgId | ORG_ID | — | — |
| 36 | ParticipantId | PARTICIPANT_ID | — | — |
| 37 | PaymentAdjustmentType | PAYMENT_ADJUSTMENT_TYPE | — | ✅ |
| 38 | PeriodId | PERIOD_ID | — | — |
| 39 | PlanComponentName | PLAN_COMPONENT_NAME | — | ✅ |
| 40 | PrimaryParticipantId | PRIMARY_PARTICIPANT_ID | — | — |
| 41 | RequestorParticipantId | REQUESTOR_PARTICIPANT_ID | — | — |
| 42 | ResolutionCode | RESOLUTION_CODE | — | ✅ |
| 43 | SourceEventDate | SOURCE_EVENT_DATE | — | ✅ |
| 44 | SourceTrxNumber | SOURCE_TRX_NUMBER | — | ✅ |
| 45 | TaskId | TASK_ID | — | — |
| 46 | TransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 47 | TransactionQty | TRANSACTION_QTY | — | ✅ |
| 48 | TransactionType | TRANSACTION_TYPE | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 4 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 7 | HoldReason | HOLD_REASON | — | ✅ |
| 8 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 9 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 14 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 15 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 16 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 17 | ParticipantId3 | PARTICIPANT_ID | — | — |
| 18 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 19 | PartyId | PARTY_ID | — | ✅ |
| 20 | PayeeOnly | PAYEE_ONLY | — | — |
| 21 | RequestId | REQUEST_ID | — | — |
| 22 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 23 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 24 | StartDate | START_DATE | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | AcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 3 | AcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 4 | AccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 5 | AcdType | ACD_TYPE | — | — |
| 6 | AllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 7 | AllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 8 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 9 | AllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 10 | AllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 11 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 12 | AsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 13 | AtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 14 | AtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 15 | AtpFlag | ATP_FLAG | — | ✅ |
| 16 | AtpRuleId | ATP_RULE_ID | — | — |
| 17 | AutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 18 | AutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 19 | AutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 20 | AutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 21 | BackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 22 | BaseItemId | BASE_ITEM_ID | — | — |
| 23 | BomItemType | BOM_ITEM_TYPE | — | — |
| 24 | BuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 25 | BulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 26 | BuyerId | BUYER_ID | — | — |
| 27 | CarryingCost | CARRYING_COST | — | — |
| 28 | CasNumber | CAS_NUMBER | — | — |
| 29 | ChangeBitMap | CHANGE_BIT_MAP | — | — |
| 30 | ChangeLineId | CHANGE_LINE_ID | — | — |
| 31 | ChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 32 | CheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | ✅ |
| 33 | ChildLotFlag | CHILD_LOT_FLAG | — | — |
| 34 | ChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 35 | ChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 36 | ChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 37 | CollateralFlag | COLLATERAL_FLAG | — | — |
| 38 | CommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 39 | ConfigMatch | CONFIG_MATCH | — | — |
| 40 | ConfigOrgs | CONFIG_ORGS | — | — |
| 41 | ConsignedFlag | CONSIGNED_FLAG | — | — |
| 42 | ContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 43 | ContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 44 | ContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 45 | ContractItemTypeCode | CONTRACT_ITEM_TYPE_CODE | — | — |
| 46 | Convergence | CONVERGENCE | — | — |
| 47 | CopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 48 | CostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 49 | CoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 50 | CreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 51 | CriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 52 | CumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 53 | CumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 54 | CurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 55 | CurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 56 | CustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 57 | CustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 58 | CycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 59 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 60 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 61 | DaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 62 | DaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 63 | DaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 64 | DaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 65 | DefaultGrade | DEFAULT_GRADE | — | — |
| 66 | DefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 67 | DefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 68 | DefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 69 | DefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 70 | DefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 71 | DefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 72 | DefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 73 | DemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 74 | DemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 75 | DimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 76 | Divergence | DIVERGENCE | — | — |
| 77 | DownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 78 | DrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 79 | DualUomControl | DUAL_UOM_CONTROL | — | — |
| 80 | DualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 81 | DualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 82 | EffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 83 | ElectronicFlag | ELECTRONIC_FLAG | — | — |
| 84 | EligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 85 | EnabledFlag | ENABLED_FLAG | — | — |
| 86 | EndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 87 | EndDateActive | END_DATE_ACTIVE | — | — |
| 88 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 89 | EngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 90 | EquipmentType | EQUIPMENT_TYPE | — | — |
| 91 | EventFlag | EVENT_FLAG | — | — |
| 92 | ExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 93 | ExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 94 | ExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 95 | ExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 96 | FinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 97 | FixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 98 | FixedLeadTime | FIXED_LEAD_TIME | — | — |
| 99 | FixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 100 | FixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 101 | ForecastHorizon | FORECAST_HORIZON | — | — |
| 102 | FullLeadTime | FULL_LEAD_TIME | — | — |
| 103 | GdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 104 | GradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 105 | HazardClassId | HAZARD_CLASS_ID | — | — |
| 106 | HazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 107 | HoldDays | HOLD_DAYS | — | — |
| 108 | ImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 109 | IndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 110 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 111 | InternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 112 | InternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 113 | InternalVolume | INTERNAL_VOLUME | — | — |
| 114 | InventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 115 | InventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 116 | InventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 117 | InventoryItemId1 | INVENTORY_ITEM_ID | — | — |
| 118 | InventoryItemId2 | INVENTORY_ITEM_ID | — | — |
| 119 | InventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 120 | InventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 121 | InventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 122 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 123 | InvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 124 | InvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 125 | InvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 126 | InvoicingRuleId | INVOICING_RULE_ID | — | — |
| 127 | ItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 128 | ItemNumber | ITEM_NUMBER | — | — |
| 129 | ItemType | ITEM_TYPE | — | — |
| 130 | JobDefinitionName1 | JOB_DEFINITION_NAME | — | — |
| 131 | JobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | — |
| 132 | LastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 133 | LeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 134 | ListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 135 | LocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 136 | LotControlCode | LOT_CONTROL_CODE | — | — |
| 137 | LotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 138 | LotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 139 | LotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 140 | LotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 141 | LotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 142 | LotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 143 | MarketPrice | MARKET_PRICE | — | — |
| 144 | MatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 145 | MaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 146 | MaturityDays | MATURITY_DAYS | — | — |
| 147 | MaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 148 | MaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 149 | MaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 150 | MinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 151 | MinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 152 | MinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 153 | MinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 154 | MrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 155 | MrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 156 | MrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 157 | MrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 158 | MtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 159 | MustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 160 | NegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 161 | NegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 162 | OntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 163 | OperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 164 | OptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 165 | OrderCost | ORDER_COST | — | — |
| 166 | OrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 167 | OrganizationId | ORGANIZATION_ID | — | — |
| 168 | OverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 169 | OverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 170 | OvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 171 | OvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 172 | OverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 173 | ParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 174 | PaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 175 | PickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 176 | PickingRuleId | PICKING_RULE_ID | — | — |
| 177 | PlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 178 | PlannerCode | PLANNER_CODE | — | — |
| 179 | PlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 180 | PlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 181 | PlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 182 | PlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 183 | PositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 184 | PostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 185 | PrepositionPoint | PREPOSITION_POINT | — | — |
| 186 | PreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 187 | PriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 188 | PrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 189 | ProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 190 | ProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 191 | ProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 192 | ProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 193 | ProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 194 | ProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 195 | ProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 196 | ProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 197 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 198 | ProgramName | PROGRAM_NAME | — | — |
| 199 | PurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 200 | PurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 201 | PurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 202 | QscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 203 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 204 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 205 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 206 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 207 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 208 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 209 | RecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | ✅ |
| 210 | RecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 211 | ReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 212 | ReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 213 | RepairLeadtime | REPAIR_LEADTIME | — | — |
| 214 | RepairProgram | REPAIR_PROGRAM | — | — |
| 215 | RepairYield | REPAIR_YIELD | — | — |
| 216 | RepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 217 | ReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 218 | RequestId1 | REQUEST_ID | — | — |
| 219 | ReservableType | RESERVABLE_TYPE | — | ✅ |
| 220 | RestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 221 | RestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 222 | RetestInterval | RETEST_INTERVAL | — | — |
| 223 | ReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 224 | ReturnableFlag | RETURNABLE_FLAG | — | — |
| 225 | RevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 226 | RoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 227 | RoundingFactor | ROUNDING_FACTOR | — | — |
| 228 | SafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 229 | SalesAccount | SALES_ACCOUNT | — | — |
| 230 | SalesProductType | SALES_PRODUCT_TYPE | — | ✅ |
| 231 | SecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 232 | SecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 233 | SerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 234 | SerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 235 | ServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 236 | ServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 237 | ServiceDuration | SERVICE_DURATION | — | — |
| 238 | ServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 239 | ServiceStartingDelay | SERVICE_STARTING_DELAY | — | ✅ |
| 240 | ServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 241 | ShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 242 | ShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 243 | ShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 244 | ShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 245 | ShrinkageRate | SHRINKAGE_RATE | — | — |
| 246 | SoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 247 | SoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 248 | SourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 249 | SourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 250 | SourceType | SOURCE_TYPE | — | ✅ |
| 251 | StartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 252 | StartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 253 | StartDateActive | START_DATE_ACTIVE | — | — |
| 254 | StdLotSize | STD_LOT_SIZE | — | — |
| 255 | StockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 256 | StyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 257 | StyleItemId | STYLE_ITEM_ID | — | — |
| 258 | SubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 259 | SubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 260 | SubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 261 | SummaryFlag | SUMMARY_FLAG | — | — |
| 262 | TaxCode1 | TAX_CODE | — | — |
| 263 | TaxableFlag | TAXABLE_FLAG | — | — |
| 264 | TemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 265 | TemplateName | TEMPLATE_NAME | — | — |
| 266 | TrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 267 | TradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 268 | UnNumberId | UN_NUMBER_ID | — | — |
| 269 | UnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 270 | UnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 271 | UnitHeight | UNIT_HEIGHT | — | — |
| 272 | UnitLength | UNIT_LENGTH | — | — |
| 273 | UnitOfIssue | UNIT_OF_ISSUE | — | — |
| 274 | UnitVolume | UNIT_VOLUME | — | — |
| 275 | UnitWeight | UNIT_WEIGHT | — | — |
| 276 | UnitWidth | UNIT_WIDTH | — | — |
| 277 | VariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 278 | VehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 279 | VersionEndDate | VERSION_END_DATE | — | — |
| 280 | VersionId | VERSION_ID | — | — |
| 281 | VersionStartDate | VERSION_START_DATE | — | — |
| 282 | VmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 283 | VmiForecastType | VMI_FORECAST_TYPE | — | — |
| 284 | VmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 285 | VmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 286 | VmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 287 | VmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 288 | VolumeUomCode | VOLUME_UOM_CODE | — | — |
| 289 | WebStatus | WEB_STATUS | — | — |
| 290 | WeightUomCode | WEIGHT_UOM_CODE | — | — |
| 291 | WhUpdateDate | WH_UPDATE_DATE | — | — |
| 292 | WipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 293 | WipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 294 | WipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | AccountName | ACCOUNT_NAME | — | ✅ |
| 3 | AccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 4 | ArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | AutopayFlag | AUTOPAY_FLAG | — | ✅ |
| 6 | Comments | COMMENTS | — | — |
| 7 | CoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | CustAccountId | CUST_ACCOUNT_ID | — | — |
| 9 | CustomerClassCode | CUSTOMER_CLASS_CODE | — | ✅ |
| 10 | CustomerType | CUSTOMER_TYPE | — | ✅ |
| 11 | DateTypePreference | DATE_TYPE_PREFERENCE | — | ✅ |
| 12 | DepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 13 | HeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | ✅ |
| 14 | HoldBillFlag | HOLD_BILL_FLAG | — | ✅ |
| 15 | LastBatchId | LAST_BATCH_ID | — | — |
| 16 | NpaNumber | NPA_NUMBER | — | — |
| 17 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 18 | PartyId1 | PARTY_ID | — | — |
| 19 | SellingPartyId | SELLING_PARTY_ID | — | — |
| 20 | SourceCode | SOURCE_CODE | — | ✅ |
| 21 | Status | STATUS | — | ✅ |
| 22 | StatusUpdateDate | STATUS_UPDATE_DATE | — | ✅ |
| 23 | TaxCode | TAX_CODE | — | ✅ |
| 24 | TaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | ✅ |
| 25 | TaxRoundingRule | TAX_ROUNDING_RULE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantFirstName | PERSON_FIRST_NAME | — | — |
| 2 | ParticipantLastName | PERSON_LAST_NAME | — | — |
| 3 | ParticipantName | PARTY_NAME | — | ✅ |
| 4 | ParticipantName1 | PARTY_NAME | — | ✅ |
| 5 | ParticipantName2 | PARTY_NAME | — | ✅ |
| 6 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 7 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 8 | PrimaryPartyPEOPartyId | PARTY_ID | — | — |
| 9 | RequestorPartyPEOPartyId | PARTY_ID | — | — |
| 10 | UserGuid | USER_GUID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
