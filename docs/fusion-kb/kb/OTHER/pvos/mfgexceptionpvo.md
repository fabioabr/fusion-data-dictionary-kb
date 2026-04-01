---
id: DOC-OTHER-PVO-MfgExceptionPVO
doc_type: system-doc
title: "MfgExceptionPVO — PVO Cross-Module"
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
  - MfgExceptionPVO
  - mfgexceptionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MfgExceptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mfg Exception. Acessa as tabelas: EGP_SYSTEM_ITEMS_VL, ENQ_AFFECTED_OBJECTS_B, ENQ_ISSUES_B (+10).

**Caminho:** `FscmTopModelAM.WorkOrderAM.MfgExceptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 810 | 13 | 2 | 51 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 395 atributos (4 BICC)
- [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]] — 17 atributos (1 PKs, 4 BICC)
- [[enq_issues_b|ENQ_ISSUES_B]] — 23 atributos (9 BICC)
- [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]] — 15 atributos (2 BICC)
- [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]] — 10 atributos (2 BICC)
- [[enq_workflow_otbi_vl|ENQ_WORKFLOW_OTBI_VL]] — 7 atributos (3 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 103 atributos (5 BICC)
- [[wie_wo_exceptions_v|WIE_WO_EXCEPTIONS_V]] — 15 atributos (1 PKs, 7 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 84 atributos (6 BICC)
- [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]] — 59 atributos (3 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 14 atributos (2 BICC)
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 14 atributos (2 BICC)
- [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]] — 54 atributos (2 BICC)

---

## ⚙️ Atributos

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemPEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 2 | ItemPEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 3 | ItemPEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 4 | ItemPEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 5 | ItemPEOAcdType | ACD_TYPE | — | — |
| 6 | ItemPEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 7 | ItemPEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 8 | ItemPEOAllowMaintenanceAssetFlag | ALLOW_MAINTENANCE_ASSET_FLAG | — | — |
| 9 | ItemPEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 10 | ItemPEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | — |
| 11 | ItemPEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | — |
| 12 | ItemPEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 13 | ItemPEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 14 | ItemPEOApprovalStatus | APPROVAL_STATUS | — | — |
| 15 | ItemPEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 16 | ItemPEOAssetClass | ASSET_CLASS | — | — |
| 17 | ItemPEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 18 | ItemPEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | — |
| 19 | ItemPEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 20 | ItemPEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 21 | ItemPEOAtpFlag | ATP_FLAG | — | — |
| 22 | ItemPEOAtpRuleId | ATP_RULE_ID | — | — |
| 23 | ItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 24 | ItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 25 | ItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 26 | ItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 27 | ItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 28 | ItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 29 | ItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 30 | ItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 31 | ItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 32 | ItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 33 | ItemPEOAttribute19 | ATTRIBUTE19 | — | — |
| 34 | ItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 35 | ItemPEOAttribute20 | ATTRIBUTE20 | — | — |
| 36 | ItemPEOAttribute21 | ATTRIBUTE21 | — | — |
| 37 | ItemPEOAttribute22 | ATTRIBUTE22 | — | — |
| 38 | ItemPEOAttribute23 | ATTRIBUTE23 | — | — |
| 39 | ItemPEOAttribute24 | ATTRIBUTE24 | — | — |
| 40 | ItemPEOAttribute25 | ATTRIBUTE25 | — | — |
| 41 | ItemPEOAttribute26 | ATTRIBUTE26 | — | — |
| 42 | ItemPEOAttribute27 | ATTRIBUTE27 | — | — |
| 43 | ItemPEOAttribute28 | ATTRIBUTE28 | — | — |
| 44 | ItemPEOAttribute29 | ATTRIBUTE29 | — | — |
| 45 | ItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 46 | ItemPEOAttribute30 | ATTRIBUTE30 | — | — |
| 47 | ItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 48 | ItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 49 | ItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 50 | ItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 51 | ItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 52 | ItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 53 | ItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 54 | ItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 55 | ItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 56 | ItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 57 | ItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 58 | ItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 59 | ItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 60 | ItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 61 | ItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 62 | ItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 63 | ItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 64 | ItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 65 | ItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 66 | ItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 67 | ItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 68 | ItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 69 | ItemPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 70 | ItemPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 71 | ItemPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 72 | ItemPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 73 | ItemPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 74 | ItemPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 75 | ItemPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 76 | ItemPEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 77 | ItemPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 78 | ItemPEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 79 | ItemPEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 80 | ItemPEOBaseItemId | BASE_ITEM_ID | — | — |
| 81 | ItemPEOBomItemType | BOM_ITEM_TYPE | — | — |
| 82 | ItemPEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 83 | ItemPEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 84 | ItemPEOBuyerId | BUYER_ID | — | — |
| 85 | ItemPEOCarryingCost | CARRYING_COST | — | — |
| 86 | ItemPEOCasNumber | CAS_NUMBER | — | — |
| 87 | ItemPEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 88 | ItemPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 89 | ItemPEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 90 | ItemPEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 91 | ItemPEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 92 | ItemPEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 93 | ItemPEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 94 | ItemPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 95 | ItemPEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 96 | ItemPEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 97 | ItemPEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 98 | ItemPEOCompletenessScore | COMPLETENESS_SCORE | — | — |
| 99 | ItemPEOConfigMatch | CONFIG_MATCH | — | — |
| 100 | ItemPEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 101 | ItemPEOConfigOrgs | CONFIG_ORGS | — | — |
| 102 | ItemPEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 103 | ItemPEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 104 | ItemPEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 105 | ItemPEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 106 | ItemPEOContractItemTypeCode | CONTRACT_ITEM_TYPE_CODE | — | — |
| 107 | ItemPEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 108 | ItemPEOConvergence | CONVERGENCE | — | — |
| 109 | ItemPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 110 | ItemPEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 111 | ItemPEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 112 | ItemPEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 113 | ItemPEOCreatedBy | CREATED_BY | — | — |
| 114 | ItemPEOCreationDate | CREATION_DATE | — | — |
| 115 | ItemPEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 116 | ItemPEOCssEnabledFlag | CSS_ENABLED_FLAG | — | — |
| 117 | ItemPEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 118 | ItemPEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 119 | ItemPEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 120 | ItemPEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 121 | ItemPEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 122 | ItemPEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 123 | ItemPEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 124 | ItemPEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 125 | ItemPEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 126 | ItemPEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 127 | ItemPEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 128 | ItemPEODaysOfCover | DAYS_OF_COVER | — | — |
| 129 | ItemPEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 130 | ItemPEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 131 | ItemPEODefaultGrade | DEFAULT_GRADE | — | — |
| 132 | ItemPEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 133 | ItemPEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 134 | ItemPEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 135 | ItemPEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 136 | ItemPEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 137 | ItemPEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 138 | ItemPEODemandPeriod | DEMAND_PERIOD | — | — |
| 139 | ItemPEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 140 | ItemPEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 141 | ItemPEODescription | DESCRIPTION | — | — |
| 142 | ItemPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 143 | ItemPEODivergence | DIVERGENCE | — | — |
| 144 | ItemPEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 145 | ItemPEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 146 | ItemPEODualUomControl | DUAL_UOM_CONTROL | — | — |
| 147 | ItemPEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 148 | ItemPEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 149 | ItemPEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 150 | ItemPEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 151 | ItemPEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 152 | ItemPEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 153 | ItemPEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 154 | ItemPEOEamItemType | EAM_ITEM_TYPE | — | — |
| 155 | ItemPEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 156 | ItemPEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 157 | ItemPEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 158 | ItemPEOEnableGenealogyTrackingFlag | ENABLE_GENEALOGY_TRACKING_FLAG | — | — |
| 159 | ItemPEOEnabledFlag | ENABLED_FLAG | — | — |
| 160 | ItemPEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 161 | ItemPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 162 | ItemPEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 163 | ItemPEOEngineeredItemFlag | ENGINEERED_ITEM_FLAG | — | — |
| 164 | ItemPEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 165 | ItemPEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 166 | ItemPEOEventFlag | EVENT_FLAG | — | — |
| 167 | ItemPEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 168 | ItemPEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 169 | ItemPEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 170 | ItemPEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 171 | ItemPEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 172 | ItemPEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 173 | ItemPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 174 | ItemPEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 175 | ItemPEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 176 | ItemPEOForecastHorizon | FORECAST_HORIZON | — | — |
| 177 | ItemPEOFullLeadTime | FULL_LEAD_TIME | — | — |
| 178 | ItemPEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 179 | ItemPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 180 | ItemPEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 181 | ItemPEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 182 | ItemPEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 183 | ItemPEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 184 | ItemPEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 185 | ItemPEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 186 | ItemPEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 187 | ItemPEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 188 | ItemPEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 189 | ItemPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 190 | ItemPEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 191 | ItemPEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 192 | ItemPEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 193 | ItemPEOHoldDays | HOLD_DAYS | — | — |
| 194 | ItemPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | — |
| 195 | ItemPEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 196 | ItemPEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 197 | ItemPEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 198 | ItemPEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 199 | ItemPEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 200 | ItemPEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 201 | ItemPEOInternalVolume | INTERNAL_VOLUME | — | — |
| 202 | ItemPEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 203 | ItemPEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 204 | ItemPEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 205 | ItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 206 | ItemPEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 207 | ItemPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 208 | ItemPEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 209 | ItemPEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 210 | ItemPEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 211 | ItemPEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 212 | ItemPEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 213 | ItemPEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 214 | ItemPEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 215 | ItemPEOItemNumber | ITEM_NUMBER | — | — |
| 216 | ItemPEOItemType | ITEM_TYPE | — | — |
| 217 | ItemPEOLanguage | LANGUAGE | — | — |
| 218 | ItemPEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 219 | ItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 220 | ItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 221 | ItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 222 | ItemPEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 223 | ItemPEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 224 | ItemPEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 225 | ItemPEOLongDescription | LONG_DESCRIPTION | — | — |
| 226 | ItemPEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 227 | ItemPEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 228 | ItemPEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 229 | ItemPEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 230 | ItemPEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 231 | ItemPEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 232 | ItemPEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 233 | ItemPEOMarketPrice | MARKET_PRICE | — | — |
| 234 | ItemPEOMasterOrgId | MASTER_ORG_ID | — | — |
| 235 | ItemPEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 236 | ItemPEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 237 | ItemPEOMaturityDays | MATURITY_DAYS | — | — |
| 238 | ItemPEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 239 | ItemPEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 240 | ItemPEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | — |
| 241 | ItemPEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 242 | ItemPEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 243 | ItemPEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 244 | ItemPEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 245 | ItemPEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 246 | ItemPEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 247 | ItemPEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 248 | ItemPEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 249 | ItemPEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 250 | ItemPEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 251 | ItemPEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 252 | ItemPEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 253 | ItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 254 | ItemPEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 255 | ItemPEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 256 | ItemPEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 257 | ItemPEOOrderCost | ORDER_COST | — | — |
| 258 | ItemPEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 259 | ItemPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 260 | ItemPEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 261 | ItemPEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | — |
| 262 | ItemPEOOutsideProcessServiceFlag | OUTSIDE_PROCESS_SERVICE_FLAG | — | — |
| 263 | ItemPEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 264 | ItemPEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 265 | ItemPEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 266 | ItemPEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 267 | ItemPEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 268 | ItemPEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 269 | ItemPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 270 | ItemPEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 271 | ItemPEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 272 | ItemPEOPickingRuleId | PICKING_RULE_ID | — | — |
| 273 | ItemPEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 274 | ItemPEOPlannerCode | PLANNER_CODE | — | — |
| 275 | ItemPEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 276 | ItemPEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | — |
| 277 | ItemPEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 278 | ItemPEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 279 | ItemPEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 280 | ItemPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 281 | ItemPEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 282 | ItemPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 283 | ItemPEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 284 | ItemPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 285 | ItemPEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 286 | ItemPEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 287 | ItemPEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 288 | ItemPEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 289 | ItemPEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 290 | ItemPEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 291 | ItemPEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 292 | ItemPEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 293 | ItemPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 294 | ItemPEOProgramName | PROGRAM_NAME | — | — |
| 295 | ItemPEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 296 | ItemPEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 297 | ItemPEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 298 | ItemPEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 299 | ItemPEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 300 | ItemPEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 301 | ItemPEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 302 | ItemPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 303 | ItemPEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 304 | ItemPEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 305 | ItemPEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 306 | ItemPEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 307 | ItemPEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 308 | ItemPEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 309 | ItemPEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 310 | ItemPEORepairProgram | REPAIR_PROGRAM | — | — |
| 311 | ItemPEORepairYield | REPAIR_YIELD | — | — |
| 312 | ItemPEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 313 | ItemPEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 314 | ItemPEORequestId | REQUEST_ID | — | — |
| 315 | ItemPEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | — |
| 316 | ItemPEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | — |
| 317 | ItemPEOReservableType | RESERVABLE_TYPE | — | — |
| 318 | ItemPEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 319 | ItemPEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 320 | ItemPEORetestInterval | RETEST_INTERVAL | — | — |
| 321 | ItemPEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 322 | ItemPEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 323 | ItemPEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 324 | ItemPEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 325 | ItemPEORoundingFactor | ROUNDING_FACTOR | — | — |
| 326 | ItemPEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 327 | ItemPEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 328 | ItemPEOSalesAccount | SALES_ACCOUNT | — | — |
| 329 | ItemPEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 330 | ItemPEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 331 | ItemPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 332 | ItemPEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 333 | ItemPEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 334 | ItemPEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 335 | ItemPEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 336 | ItemPEOServiceDuration | SERVICE_DURATION | — | — |
| 337 | ItemPEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 338 | ItemPEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | — |
| 339 | ItemPEOServiceStartDelay | SERVICE_START_DELAY | — | — |
| 340 | ItemPEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | — |
| 341 | ItemPEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 342 | ItemPEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 343 | ItemPEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 344 | ItemPEOShelfLifeDays | SHELF_LIFE_DAYS | — | — |
| 345 | ItemPEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 346 | ItemPEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 347 | ItemPEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 348 | ItemPEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 349 | ItemPEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 350 | ItemPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 351 | ItemPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 352 | ItemPEOSourceType | SOURCE_TYPE | — | — |
| 353 | ItemPEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 354 | ItemPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 355 | ItemPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 356 | ItemPEOStdLotSize | STD_LOT_SIZE | — | — |
| 357 | ItemPEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 358 | ItemPEOStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 359 | ItemPEOStyleItemId | STYLE_ITEM_ID | — | — |
| 360 | ItemPEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 361 | ItemPEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 362 | ItemPEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 363 | ItemPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 364 | ItemPEOTaxCode | TAX_CODE | — | — |
| 365 | ItemPEOTaxableFlag | TAXABLE_FLAG | — | — |
| 366 | ItemPEOTemplateName | TEMPLATE_NAME | — | — |
| 367 | ItemPEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 368 | ItemPEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 369 | ItemPEOUnNumberId | UN_NUMBER_ID | — | — |
| 370 | ItemPEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 371 | ItemPEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 372 | ItemPEOUnitHeight | UNIT_HEIGHT | — | — |
| 373 | ItemPEOUnitLength | UNIT_LENGTH | — | — |
| 374 | ItemPEOUnitOfIssue | UNIT_OF_ISSUE | — | — |
| 375 | ItemPEOUnitVolume | UNIT_VOLUME | — | — |
| 376 | ItemPEOUnitWeight | UNIT_WEIGHT | — | — |
| 377 | ItemPEOUnitWidth | UNIT_WIDTH | — | — |
| 378 | ItemPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 379 | ItemPEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 380 | ItemPEOVersionEndDate | VERSION_END_DATE | — | — |
| 381 | ItemPEOVersionId | VERSION_ID | — | — |
| 382 | ItemPEOVersionStartDate | VERSION_START_DATE | — | — |
| 383 | ItemPEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 384 | ItemPEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 385 | ItemPEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 386 | ItemPEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 387 | ItemPEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 388 | ItemPEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 389 | ItemPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 390 | ItemPEOWebStatus | WEB_STATUS | — | — |
| 391 | ItemPEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 392 | ItemPEOWhUpdateDate | WH_UPDATE_DATE | — | — |
| 393 | ItemPEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 394 | ItemPEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 395 | ItemPEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |

### [[enq_affected_objects_b|ENQ_AFFECTED_OBJECTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AffectedObjectsBasePEOAffectedObjectId | AFFECTED_OBJECT_ID | 🔑 | ✅ |
| 2 | AffectedObjectsBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | AffectedObjectsBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | AffectedObjectsBasePEOImpactType | IMPACT_TYPE | — | — |
| 5 | AffectedObjectsBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AffectedObjectsBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AffectedObjectsBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AffectedObjectsBasePEOObjectId | OBJECT_ID | — | — |
| 9 | AffectedObjectsBasePEOObjectType | OBJECT_TYPE | — | — |
| 10 | AffectedObjectsBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AffectedObjectsBasePEOPk1Value | PK1_VALUE | — | ✅ |
| 12 | AffectedObjectsBasePEOPk2Value | PK2_VALUE | — | — |
| 13 | AffectedObjectsBasePEOPk3Value | PK3_VALUE | — | — |
| 14 | AffectedObjectsBasePEOPk4Value | PK4_VALUE | — | — |
| 15 | AffectedObjectsBasePEOPk5Value | PK5_VALUE | — | — |
| 16 | AffectedObjectsBasePEOStatus | STATUS | — | ✅ |
| 17 | AffectedObjectsBasePEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | — |

### [[enq_issues_b|ENQ_ISSUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IssueBasePEOActualResolutionDate | ACTUAL_RESOLUTION_DATE | — | ✅ |
| 2 | IssueBasePEOAssignedTo | ASSIGNED_TO | — | — |
| 3 | IssueBasePEOCreatedBy | CREATED_BY | — | — |
| 4 | IssueBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | IssueBasePEOCustomerId | CUSTOMER_ID | — | — |
| 6 | IssueBasePEODisposition | DISPOSITION | — | — |
| 7 | IssueBasePEODowntime | DOWNTIME | — | ✅ |
| 8 | IssueBasePEOExpectedResolutionDate | EXPECTED_RESOLUTION_DATE | — | ✅ |
| 9 | IssueBasePEOIssueId | ISSUE_ID | — | ✅ |
| 10 | IssueBasePEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 11 | IssueBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | IssueBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | IssueBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | IssueBasePEOLikelihoodOfRecurrence | LIKELIHOOD_OF_RECURRENCE | — | — |
| 15 | IssueBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | IssueBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 17 | IssueBasePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 18 | IssueBasePEOReportedBy | REPORTED_BY | — | — |
| 19 | IssueBasePEOReportedDate | REPORTED_DATE | — | — |
| 20 | IssueBasePEOSeverity | SEVERITY | — | ✅ |
| 21 | IssueBasePEOSource | SOURCE | — | — |
| 22 | IssueBasePEOSupplierId | SUPPLIER_ID | — | — |
| 23 | IssueBasePEOWorkflowStatusId | WORKFLOW_STATUS_ID | — | — |

### [[enq_quality_types_b|ENQ_QUALITY_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypePEOCode | CODE | — | — |
| 2 | QualityTypePEOCreatedBy | CREATED_BY | — | — |
| 3 | QualityTypePEOCreationDate | CREATION_DATE | — | — |
| 4 | QualityTypePEODisplayOrder | DISPLAY_ORDER | — | — |
| 5 | QualityTypePEOInstantiationAllowed | INSTANTIATION_ALLOWED | — | — |
| 6 | QualityTypePEOIsActive | IS_ACTIVE | — | — |
| 7 | QualityTypePEOIsSeeded | IS_SEEDED | — | — |
| 8 | QualityTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QualityTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | QualityTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | QualityTypePEOObjectType | OBJECT_TYPE | — | — |
| 12 | QualityTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | QualityTypePEOParentQualityTypeId | PARENT_QUALITY_TYPE_ID | — | — |
| 14 | QualityTypePEOQualityTypeId | QUALITY_TYPE_ID | — | ✅ |
| 15 | QualityTypePEOSource | SOURCE | — | — |

### [[enq_supported_entities|ENQ_SUPPORTED_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualitySupportedEntitiyPEOCreatedBy | CREATED_BY | — | — |
| 2 | QualitySupportedEntitiyPEOCreationDate | CREATION_DATE | — | — |
| 3 | QualitySupportedEntitiyPEOEntityType | ENTITY_TYPE | — | — |
| 4 | QualitySupportedEntitiyPEOIsSeeded | IS_SEEDED | — | — |
| 5 | QualitySupportedEntitiyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QualitySupportedEntitiyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | QualitySupportedEntitiyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | QualitySupportedEntitiyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | QualitySupportedEntitiyPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 10 | QualitySupportedEntitiyPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | ✅ |

### [[enq_workflow_otbi_vl|ENQ_WORKFLOW_OTBI_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkflowStatusOtbiPEOName | NAME | — | — |
| 2 | WorkflowStatusOtbiPEOObjectCode | OBJECT_CODE | — | — |
| 3 | WorkflowStatusOtbiPEOObjectPk1 | OBJECT_PK1 | — | ✅ |
| 4 | WorkflowStatusOtbiPEOStatusName | STATUS_NAME | — | ✅ |
| 5 | WorkflowStatusOtbiPEOStatusType | STATUS_TYPE | — | — |
| 6 | WorkflowStatusOtbiPEOSubStatusName | SUB_STATUS_NAME | — | ✅ |
| 7 | WorkflowStatusOtbiPEOSubStatusType | SUB_STATUS_TYPE | — | — |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WorkOrderAnalyticsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WorkOrderAnalyticsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WorkOrderAnalyticsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WorkOrderAnalyticsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WorkOrderAnalyticsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WorkOrderAnalyticsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WorkOrderAnalyticsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WorkOrderAnalyticsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WorkOrderAnalyticsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WorkOrderAnalyticsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WorkOrderAnalyticsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WorkOrderAnalyticsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WorkOrderAnalyticsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WorkOrderAnalyticsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WorkOrderAnalyticsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WorkOrderAnalyticsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WorkOrderAnalyticsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WorkOrderAnalyticsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WorkOrderAnalyticsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WorkOrderAnalyticsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WorkOrderAnalyticsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WorkOrderAnalyticsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WorkOrderAnalyticsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WorkOrderAnalyticsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WorkOrderAnalyticsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WorkOrderAnalyticsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WorkOrderAnalyticsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WorkOrderAnalyticsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WorkOrderAnalyticsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WorkOrderAnalyticsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WorkOrderAnalyticsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WorkOrderAnalyticsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WorkOrderAnalyticsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WorkOrderAnalyticsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WorkOrderAnalyticsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WorkOrderAnalyticsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WorkOrderAnalyticsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WorkOrderAnalyticsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WorkOrderAnalyticsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WorkOrderAnalyticsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 45 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | — |
| 46 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 47 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | — |
| 48 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 49 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 50 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 51 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 52 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 53 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 54 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 55 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 56 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 57 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 58 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 59 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 60 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 61 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 62 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 63 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 64 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 65 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 69 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 71 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 72 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 73 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 74 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 75 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 76 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 77 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 78 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 79 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | — |
| 80 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | — |
| 81 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 82 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 83 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 84 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 85 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 86 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 87 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 88 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 89 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 90 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 91 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 92 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 93 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 94 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 95 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 96 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 97 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 98 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 99 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 100 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 101 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 102 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 103 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_exceptions_v|WIE_WO_EXCEPTIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOExceptionsAnalyticsPEOExceptionComponentId | EXCEPTION_COMPONENT_ID | — | ✅ |
| 2 | WOExceptionsAnalyticsPEOExceptionComponentName | EXCEPTION_COMPONENT_NAME | — | — |
| 3 | WOExceptionsAnalyticsPEOExceptionComponentOrgId | EXCEPTION_COMPONENT_ORG_ID | — | ✅ |
| 4 | WOExceptionsAnalyticsPEOExceptionOnObjectName | EXCEPTION_ON_OBJECT_NAME | — | ✅ |
| 5 | WOExceptionsAnalyticsPEOIssueId | ISSUE_ID | 🔑 | ✅ |
| 6 | WOExceptionsAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 7 | WOExceptionsAnalyticsPEOResourceId | RESOURCE_ID | — | ✅ |
| 8 | WOExceptionsAnalyticsPEOResourceInstanceId | RESOURCE_INSTANCE_ID | — | ✅ |
| 9 | WOExceptionsAnalyticsPEOResourceName | RESOURCE_NAME | — | — |
| 10 | WOExceptionsAnalyticsPEOSupportedEntityId | SUPPORTED_ENTITY_ID | — | — |
| 11 | WOExceptionsAnalyticsPEOSupportedEntityIdDummy | SUPPORTED_ENTITY_ID_DUMMY | — | — |
| 12 | WOExceptionsAnalyticsPEOWorkAreaId | WORK_AREA_ID | — | — |
| 13 | WOExceptionsAnalyticsPEOWorkAreaName | WORK_AREA_NAME | — | — |
| 14 | WOExceptionsAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 15 | WOExceptionsAnalyticsPEOWorkCenterName | WORK_CENTER_NAME | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WOOperationAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WOOperationAnalyticsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WOOperationAnalyticsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WOOperationAnalyticsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WOOperationAnalyticsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WOOperationAnalyticsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WOOperationAnalyticsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WOOperationAnalyticsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WOOperationAnalyticsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WOOperationAnalyticsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WOOperationAnalyticsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WOOperationAnalyticsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WOOperationAnalyticsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WOOperationAnalyticsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WOOperationAnalyticsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WOOperationAnalyticsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WOOperationAnalyticsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WOOperationAnalyticsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WOOperationAnalyticsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WOOperationAnalyticsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WOOperationAnalyticsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WOOperationAnalyticsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WOOperationAnalyticsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WOOperationAnalyticsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WOOperationAnalyticsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WOOperationAnalyticsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WOOperationAnalyticsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WOOperationAnalyticsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WOOperationAnalyticsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WOOperationAnalyticsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WOOperationAnalyticsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WOOperationAnalyticsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WOOperationAnalyticsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WOOperationAnalyticsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WOOperationAnalyticsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WOOperationAnalyticsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WOOperationAnalyticsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WOOperationAnalyticsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WOOperationAnalyticsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WOOperationAnalyticsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WOOperationAnalyticsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WOOperationAnalyticsPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 45 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 46 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 47 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 48 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 49 | WOOperationAnalyticsPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 50 | WOOperationAnalyticsPEOInProcessQuantity | IN_PROCESS_QUANTITY | — | — |
| 51 | WOOperationAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 52 | WOOperationAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 53 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | WOOperationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | WOOperationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 56 | WOOperationAnalyticsPEOLeadTimeUom | LEAD_TIME_UOM | — | — |
| 57 | WOOperationAnalyticsPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 58 | WOOperationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | WOOperationAnalyticsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 60 | WOOperationAnalyticsPEOOperationType | OPERATION_TYPE | — | — |
| 61 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 62 | WOOperationAnalyticsPEOOspItemId | OSP_ITEM_ID | — | — |
| 63 | WOOperationAnalyticsPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | — |
| 64 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 65 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 66 | WOOperationAnalyticsPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | — |
| 67 | WOOperationAnalyticsPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | — |
| 68 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 69 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | — |
| 70 | WOOperationAnalyticsPEOReceivedQuantity | RECEIVED_QUANTITY | — | — |
| 71 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 72 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | — |
| 73 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 74 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 75 | WOOperationAnalyticsPEOShippedQuantity | SHIPPED_QUANTITY | — | — |
| 76 | WOOperationAnalyticsPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 77 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | — |
| 78 | WOOperationAnalyticsPEOSupplierId | SUPPLIER_ID | — | — |
| 79 | WOOperationAnalyticsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 80 | WOOperationAnalyticsPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 81 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | — |
| 82 | WOOperationAnalyticsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 83 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 84 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductSerialPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkOrderProductSerialPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | WorkOrderProductSerialPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | WorkOrderProductSerialPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | WorkOrderProductSerialPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | WorkOrderProductSerialPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | WorkOrderProductSerialPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | WorkOrderProductSerialPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | WorkOrderProductSerialPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | WorkOrderProductSerialPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | WorkOrderProductSerialPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | WorkOrderProductSerialPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | WorkOrderProductSerialPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkOrderProductSerialPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | WorkOrderProductSerialPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | WorkOrderProductSerialPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | WorkOrderProductSerialPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | WorkOrderProductSerialPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | WorkOrderProductSerialPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | WorkOrderProductSerialPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | WorkOrderProductSerialPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | WorkOrderProductSerialPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | WorkOrderProductSerialPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | WorkOrderProductSerialPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | WorkOrderProductSerialPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | WorkOrderProductSerialPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | WorkOrderProductSerialPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkOrderProductSerialPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | WorkOrderProductSerialPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | WorkOrderProductSerialPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | WorkOrderProductSerialPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | WorkOrderProductSerialPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | WorkOrderProductSerialPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | WorkOrderProductSerialPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | WorkOrderProductSerialPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | WorkOrderProductSerialPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | WorkOrderProductSerialPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | WorkOrderProductSerialPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | WorkOrderProductSerialPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | WorkOrderProductSerialPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | WorkOrderProductSerialPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | WorkOrderProductSerialPEOCreatedBy | CREATED_BY | — | — |
| 43 | WorkOrderProductSerialPEOCreationDate | CREATION_DATE | — | — |
| 44 | WorkOrderProductSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 45 | WorkOrderProductSerialPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 46 | WorkOrderProductSerialPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 47 | WorkOrderProductSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | WorkOrderProductSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | WorkOrderProductSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | WorkOrderProductSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | WorkOrderProductSerialPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 52 | WorkOrderProductSerialPEOOrganizationId | ORGANIZATION_ID | — | — |
| 53 | WorkOrderProductSerialPEORequestId | REQUEST_ID | — | — |
| 54 | WorkOrderProductSerialPEOSerialNumber | SERIAL_NUMBER | — | — |
| 55 | WorkOrderProductSerialPEOSerialStatus | SERIAL_STATUS | — | — |
| 56 | WorkOrderProductSerialPEOWoOperationId | WO_OPERATION_ID | — | — |
| 57 | WorkOrderProductSerialPEOWoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | — |
| 58 | WorkOrderProductSerialPEOWoProductSerialId | WO_PRODUCT_SERIAL_ID | — | — |
| 59 | WorkOrderProductSerialPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EquipmentInstancePEOAssetId | ASSET_ID | — | ✅ |
| 2 | EquipmentInstancePEOCreatedBy | CREATED_BY | — | — |
| 3 | EquipmentInstancePEOCreationDate | CREATION_DATE | — | — |
| 4 | EquipmentInstancePEOEquipmentInstanceCode | EQUIPMENT_INSTANCE_CODE | — | — |
| 5 | EquipmentInstancePEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | — |
| 6 | EquipmentInstancePEOEquipmentInstanceName | EQUIPMENT_INSTANCE_NAME | — | — |
| 7 | EquipmentInstancePEOInactiveDate | INACTIVE_DATE | — | — |
| 8 | EquipmentInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EquipmentInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | EquipmentInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | EquipmentInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | EquipmentInstancePEOOrganizationId | ORGANIZATION_ID | — | — |
| 13 | EquipmentInstancePEOResourceId | RESOURCE_ID | — | — |
| 14 | EquipmentInstancePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_labor_instances|WIS_LABOR_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborInstancePEOCreatedBy | CREATED_BY | — | — |
| 2 | LaborInstancePEOCreationDate | CREATION_DATE | — | — |
| 3 | LaborInstancePEOInactiveDate | INACTIVE_DATE | — | — |
| 4 | LaborInstancePEOLaborInstanceCode | LABOR_INSTANCE_CODE | — | — |
| 5 | LaborInstancePEOLaborInstanceId | LABOR_INSTANCE_ID | — | — |
| 6 | LaborInstancePEOLaborInstanceName | LABOR_INSTANCE_NAME | — | — |
| 7 | LaborInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LaborInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LaborInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LaborInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | LaborInstancePEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | LaborInstancePEOPartyId | PARTY_ID | — | ✅ |
| 13 | LaborInstancePEOResourceId | RESOURCE_ID | — | — |
| 14 | LaborInstancePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkCenterPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | WorkCenterPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | WorkCenterPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | WorkCenterPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | WorkCenterPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | WorkCenterPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | WorkCenterPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | WorkCenterPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | WorkCenterPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | WorkCenterPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | WorkCenterPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | WorkCenterPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkCenterPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | WorkCenterPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | WorkCenterPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | WorkCenterPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | WorkCenterPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | WorkCenterPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | WorkCenterPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | WorkCenterPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | WorkCenterPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | WorkCenterPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | WorkCenterPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | WorkCenterPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | WorkCenterPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | WorkCenterPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkCenterPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | WorkCenterPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | WorkCenterPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | WorkCenterPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | WorkCenterPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | WorkCenterPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | WorkCenterPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | WorkCenterPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | WorkCenterPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | WorkCenterPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | WorkCenterPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | WorkCenterPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | WorkCenterPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | WorkCenterPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | WorkCenterPEOCreatedBy | CREATED_BY | — | — |
| 43 | WorkCenterPEOCreationDate | CREATION_DATE | — | — |
| 44 | WorkCenterPEOInactiveDate | INACTIVE_DATE | — | — |
| 45 | WorkCenterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | WorkCenterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 47 | WorkCenterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 48 | WorkCenterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | WorkCenterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 50 | WorkCenterPEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 51 | WorkCenterPEOWorkCenterCode | WORK_CENTER_CODE | — | — |
| 52 | WorkCenterPEOWorkCenterDescription | WORK_CENTER_DESCRIPTION | — | — |
| 53 | WorkCenterPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 54 | WorkCenterPEOWorkCenterName | WORK_CENTER_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
