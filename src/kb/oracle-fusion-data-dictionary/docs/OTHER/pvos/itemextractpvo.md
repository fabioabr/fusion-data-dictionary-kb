---
id: DOC-OTHER-PVO-ItemExtractPVO
doc_type: system-doc
title: "ItemExtractPVO — PVO Cross-Module"
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
  - ItemExtractPVO
  - itemextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Extract. Acessa as tabelas: EGP_SYSTEM_ITEMS_B, egp_system_items_tl.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 395 | 2 | 2 | 388 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]] — 389 atributos (2 PKs, 388 BICC)
- [[egp_system_items_tl|egp_system_items_tl]] — 6 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | ✅ |
| 2 | ItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | ✅ |
| 3 | ItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | ✅ |
| 4 | ItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 5 | ItemBasePEOAcdType | ACD_TYPE | — | ✅ |
| 6 | ItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | ✅ |
| 7 | ItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | ✅ |
| 8 | ItemBasePEOAllowMaintenanceAssetFlag | ALLOW_MAINTENANCE_ASSET_FLAG | — | ✅ |
| 9 | ItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 10 | ItemBasePEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | ✅ |
| 11 | ItemBasePEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | ✅ |
| 12 | ItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 13 | ItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | ✅ |
| 14 | ItemBasePEOAltItemCode | ALT_ITEM_CODE | — | ✅ |
| 15 | ItemBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 16 | ItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | ✅ |
| 17 | ItemBasePEOAssetCategoryId | ASSET_CATEGORY_ID | — | ✅ |
| 18 | ItemBasePEOAssetClass | ASSET_CLASS | — | ✅ |
| 19 | ItemBasePEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | ✅ |
| 20 | ItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | ✅ |
| 21 | ItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | ✅ |
| 22 | ItemBasePEOAtpFlag | ATP_FLAG | — | ✅ |
| 23 | ItemBasePEOAtpRuleId | ATP_RULE_ID | — | ✅ |
| 24 | ItemBasePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 25 | ItemBasePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 26 | ItemBasePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 27 | ItemBasePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 28 | ItemBasePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 29 | ItemBasePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 30 | ItemBasePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 31 | ItemBasePEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 32 | ItemBasePEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 33 | ItemBasePEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 34 | ItemBasePEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 35 | ItemBasePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 36 | ItemBasePEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 37 | ItemBasePEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 38 | ItemBasePEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 39 | ItemBasePEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 40 | ItemBasePEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 41 | ItemBasePEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 42 | ItemBasePEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 43 | ItemBasePEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 44 | ItemBasePEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 45 | ItemBasePEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 46 | ItemBasePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 47 | ItemBasePEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 48 | ItemBasePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 49 | ItemBasePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 50 | ItemBasePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 51 | ItemBasePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 52 | ItemBasePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 53 | ItemBasePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 54 | ItemBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 55 | ItemBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 56 | ItemBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 57 | ItemBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 58 | ItemBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 59 | ItemBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 60 | ItemBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 61 | ItemBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 62 | ItemBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 63 | ItemBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 64 | ItemBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 65 | ItemBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 66 | ItemBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 67 | ItemBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 68 | ItemBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 69 | ItemBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 70 | ItemBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 71 | ItemBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 72 | ItemBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 73 | ItemBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 74 | ItemBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 75 | ItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 76 | ItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | ✅ |
| 77 | ItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | ✅ |
| 78 | ItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | ✅ |
| 79 | ItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | ✅ |
| 80 | ItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | ✅ |
| 81 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | ✅ |
| 82 | ItemBasePEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 83 | ItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | ✅ |
| 84 | ItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | ✅ |
| 85 | ItemBasePEOBuyerId | BUYER_ID | — | ✅ |
| 86 | ItemBasePEOCarryingCost | CARRYING_COST | — | ✅ |
| 87 | ItemBasePEOCasNumber | CAS_NUMBER | — | ✅ |
| 88 | ItemBasePEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 89 | ItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | ✅ |
| 90 | ItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | ✅ |
| 91 | ItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | ✅ |
| 92 | ItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | ✅ |
| 93 | ItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | ✅ |
| 94 | ItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | ✅ |
| 95 | ItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | ✅ |
| 96 | ItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | ✅ |
| 97 | ItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | ✅ |
| 98 | ItemBasePEOCompletenessScore | COMPLETENESS_SCORE | — | ✅ |
| 99 | ItemBasePEOConfigMatch | CONFIG_MATCH | — | ✅ |
| 100 | ItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | ✅ |
| 101 | ItemBasePEOConfigOrgs | CONFIG_ORGS | — | ✅ |
| 102 | ItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 103 | ItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | ✅ |
| 104 | ItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | ✅ |
| 105 | ItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | ✅ |
| 106 | ItemBasePEOContractItemTypeCode | CONTRACT_ITEM_TYPE_CODE | — | ✅ |
| 107 | ItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | ✅ |
| 108 | ItemBasePEOConvergence | CONVERGENCE | — | ✅ |
| 109 | ItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | ✅ |
| 110 | ItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | ✅ |
| 111 | ItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | ✅ |
| 112 | ItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | ✅ |
| 113 | ItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | ✅ |
| 114 | ItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | ✅ |
| 115 | ItemBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 116 | ItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | ✅ |
| 117 | ItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | ✅ |
| 118 | ItemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 119 | ItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | ✅ |
| 120 | ItemBasePEOCssEnabledFlag | CSS_ENABLED_FLAG | — | ✅ |
| 121 | ItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | ✅ |
| 122 | ItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | ✅ |
| 123 | ItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | ✅ |
| 124 | ItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | ✅ |
| 125 | ItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | ✅ |
| 126 | ItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | ✅ |
| 127 | ItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | ✅ |
| 128 | ItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 129 | ItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 130 | ItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | ✅ |
| 131 | ItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | ✅ |
| 132 | ItemBasePEODaysOfCover | DAYS_OF_COVER | — | ✅ |
| 133 | ItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | ✅ |
| 134 | ItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | ✅ |
| 135 | ItemBasePEODefaultGrade | DEFAULT_GRADE | — | ✅ |
| 136 | ItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | ✅ |
| 137 | ItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | ✅ |
| 138 | ItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | ✅ |
| 139 | ItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | ✅ |
| 140 | ItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | ✅ |
| 141 | ItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | ✅ |
| 142 | ItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | ✅ |
| 143 | ItemBasePEODemandPeriod | DEMAND_PERIOD | — | ✅ |
| 144 | ItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | ✅ |
| 145 | ItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | ✅ |
| 146 | ItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | ✅ |
| 147 | ItemBasePEODivergence | DIVERGENCE | — | ✅ |
| 148 | ItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | ✅ |
| 149 | ItemBasePEODqRequiredFlag | DQ_REQUIRED_FLAG | — | ✅ |
| 150 | ItemBasePEODqSemanticKey | DQ_SEMANTIC_KEY | — | ✅ |
| 151 | ItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | ✅ |
| 152 | ItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | ✅ |
| 153 | ItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | ✅ |
| 154 | ItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | ✅ |
| 155 | ItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 156 | ItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | ✅ |
| 157 | ItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | ✅ |
| 158 | ItemBasePEOEnableGenealogyTrackingFlag | ENABLE_GENEALOGY_TRACKING_FLAG | — | ✅ |
| 159 | ItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | ✅ |
| 160 | ItemBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 161 | ItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | ✅ |
| 162 | ItemBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 163 | ItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 164 | ItemBasePEOEngineeredItemFlag | ENGINEERED_ITEM_FLAG | — | ✅ |
| 165 | ItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | ✅ |
| 166 | ItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | ✅ |
| 167 | ItemBasePEOEventFlag | EVENT_FLAG | — | ✅ |
| 168 | ItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | ✅ |
| 169 | ItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 170 | ItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | ✅ |
| 171 | ItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | ✅ |
| 172 | ItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | ✅ |
| 173 | ItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | ✅ |
| 174 | ItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | ✅ |
| 175 | ItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 176 | ItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | ✅ |
| 177 | ItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | ✅ |
| 178 | ItemBasePEOForcePurchaseLeadTimeFlag | FORCE_PURCHASE_LEAD_TIME_FLAG | — | ✅ |
| 179 | ItemBasePEOForecastHorizon | FORECAST_HORIZON | — | ✅ |
| 180 | ItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 181 | ItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | ✅ |
| 182 | ItemBasePEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 183 | ItemBasePEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 184 | ItemBasePEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 185 | ItemBasePEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 186 | ItemBasePEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 187 | ItemBasePEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 188 | ItemBasePEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 189 | ItemBasePEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 190 | ItemBasePEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 191 | ItemBasePEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 192 | ItemBasePEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 193 | ItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | ✅ |
| 194 | ItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | ✅ |
| 195 | ItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 196 | ItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | ✅ |
| 197 | ItemBasePEOHoldDays | HOLD_DAYS | — | ✅ |
| 198 | ItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 199 | ItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | ✅ |
| 200 | ItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 201 | ItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | ✅ |
| 202 | ItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | ✅ |
| 203 | ItemBasePEOInternalVolume | INTERNAL_VOLUME | — | ✅ |
| 204 | ItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 205 | ItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | ✅ |
| 206 | ItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | ✅ |
| 207 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 208 | ItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | ✅ |
| 209 | ItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 210 | ItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | ✅ |
| 211 | ItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 212 | ItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 213 | ItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | ✅ |
| 214 | ItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 215 | ItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 216 | ItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | ✅ |
| 217 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 218 | ItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | ✅ |
| 219 | ItemBasePEOItemType | ITEM_TYPE | — | ✅ |
| 220 | ItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | ✅ |
| 221 | ItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 222 | ItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 223 | ItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 224 | ItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | ✅ |
| 225 | ItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 226 | ItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | ✅ |
| 227 | ItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | ✅ |
| 228 | ItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | ✅ |
| 229 | ItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | ✅ |
| 230 | ItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | ✅ |
| 231 | ItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | ✅ |
| 232 | ItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | ✅ |
| 233 | ItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | ✅ |
| 234 | ItemBasePEOMarketPrice | MARKET_PRICE | — | ✅ |
| 235 | ItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | ✅ |
| 236 | ItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | ✅ |
| 237 | ItemBasePEOMaturityDays | MATURITY_DAYS | — | ✅ |
| 238 | ItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | ✅ |
| 239 | ItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | ✅ |
| 240 | ItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 241 | ItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | ✅ |
| 242 | ItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | ✅ |
| 243 | ItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | ✅ |
| 244 | ItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 245 | ItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | ✅ |
| 246 | ItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 247 | ItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | ✅ |
| 248 | ItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | ✅ |
| 249 | ItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | ✅ |
| 250 | ItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | ✅ |
| 251 | ItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | ✅ |
| 252 | ItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | ✅ |
| 253 | ItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | ✅ |
| 254 | ItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | ✅ |
| 255 | ItemBasePEOOrderCost | ORDER_COST | — | ✅ |
| 256 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | ✅ |
| 257 | ItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | ✅ |
| 258 | ItemBasePEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 259 | ItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | ✅ |
| 260 | ItemBasePEOOutsideProcessServiceFlag | OUTSIDE_PROCESS_SERVICE_FLAG | — | ✅ |
| 261 | ItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | ✅ |
| 262 | ItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | ✅ |
| 263 | ItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | ✅ |
| 264 | ItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | ✅ |
| 265 | ItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | ✅ |
| 266 | ItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | ✅ |
| 267 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | ✅ |
| 268 | ItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 269 | ItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | ✅ |
| 270 | ItemBasePEOPickingRuleId | PICKING_RULE_ID | — | ✅ |
| 271 | ItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | ✅ |
| 272 | ItemBasePEOPlannerCode | PLANNER_CODE | — | ✅ |
| 273 | ItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | ✅ |
| 274 | ItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 275 | ItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | ✅ |
| 276 | ItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | ✅ |
| 277 | ItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | ✅ |
| 278 | ItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 279 | ItemBasePEOPreliminaryItemFlag | PRELIMINARY_ITEM_FLAG | — | — |
| 280 | ItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | ✅ |
| 281 | ItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 282 | ItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | ✅ |
| 283 | ItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 284 | ItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | ✅ |
| 285 | ItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | ✅ |
| 286 | ItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | ✅ |
| 287 | ItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | ✅ |
| 288 | ItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | ✅ |
| 289 | ItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | ✅ |
| 290 | ItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | ✅ |
| 291 | ItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | ✅ |
| 292 | ItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | ✅ |
| 293 | ItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | ✅ |
| 294 | ItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | ✅ |
| 295 | ItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 296 | ItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 297 | ItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 298 | ItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 299 | ItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 300 | ItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | ✅ |
| 301 | ItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | ✅ |
| 302 | ItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | ✅ |
| 303 | ItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | ✅ |
| 304 | ItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | ✅ |
| 305 | ItemBasePEORepairProgram | REPAIR_PROGRAM | — | ✅ |
| 306 | ItemBasePEORepairTransactionCode | REPAIR_TRANSACTION_CODE | — | ✅ |
| 307 | ItemBasePEORepairYield | REPAIR_YIELD | — | ✅ |
| 308 | ItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | ✅ |
| 309 | ItemBasePEOReplacementType | REPLACEMENT_TYPE | — | ✅ |
| 310 | ItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | ✅ |
| 311 | ItemBasePEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | ✅ |
| 312 | ItemBasePEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | ✅ |
| 313 | ItemBasePEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 314 | ItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | ✅ |
| 315 | ItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | ✅ |
| 316 | ItemBasePEORetestInterval | RETEST_INTERVAL | — | ✅ |
| 317 | ItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | ✅ |
| 318 | ItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 319 | ItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | ✅ |
| 320 | ItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | ✅ |
| 321 | ItemBasePEORoundingFactor | ROUNDING_FACTOR | — | ✅ |
| 322 | ItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | ✅ |
| 323 | ItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | ✅ |
| 324 | ItemBasePEOSalesAccount | SALES_ACCOUNT | — | ✅ |
| 325 | ItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | ✅ |
| 326 | ItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | ✅ |
| 327 | ItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 328 | ItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | ✅ |
| 329 | ItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | ✅ |
| 330 | ItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | ✅ |
| 331 | ItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | ✅ |
| 332 | ItemBasePEOServiceDuration | SERVICE_DURATION | — | ✅ |
| 333 | ItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | ✅ |
| 334 | ItemBasePEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | ✅ |
| 335 | ItemBasePEOServiceStartDelay | SERVICE_START_DELAY | — | ✅ |
| 336 | ItemBasePEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | ✅ |
| 337 | ItemBasePEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | ✅ |
| 338 | ItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | ✅ |
| 339 | ItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | ✅ |
| 340 | ItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | ✅ |
| 341 | ItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | ✅ |
| 342 | ItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | ✅ |
| 343 | ItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | ✅ |
| 344 | ItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | ✅ |
| 345 | ItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | ✅ |
| 346 | ItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 347 | ItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 348 | ItemBasePEOSourceType | SOURCE_TYPE | — | ✅ |
| 349 | ItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | ✅ |
| 350 | ItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 351 | ItemBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 352 | ItemBasePEOStdLotSize | STD_LOT_SIZE | — | ✅ |
| 353 | ItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | ✅ |
| 354 | ItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 355 | ItemBasePEOStyleItemId | STYLE_ITEM_ID | — | ✅ |
| 356 | ItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | ✅ |
| 357 | ItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | ✅ |
| 358 | ItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | ✅ |
| 359 | ItemBasePEOTaxCode | TAX_CODE | — | ✅ |
| 360 | ItemBasePEOTaxableFlag | TAXABLE_FLAG | — | ✅ |
| 361 | ItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 362 | ItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | ✅ |
| 363 | ItemBasePEOUnNumberId | UN_NUMBER_ID | — | ✅ |
| 364 | ItemBasePEOUnderComplToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | ✅ |
| 365 | ItemBasePEOUnderComplToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | ✅ |
| 366 | ItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | ✅ |
| 367 | ItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | ✅ |
| 368 | ItemBasePEOUnitHeight | UNIT_HEIGHT | — | ✅ |
| 369 | ItemBasePEOUnitLength | UNIT_LENGTH | — | ✅ |
| 370 | ItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | ✅ |
| 371 | ItemBasePEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 372 | ItemBasePEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 373 | ItemBasePEOUnitWidth | UNIT_WIDTH | — | ✅ |
| 374 | ItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 375 | ItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | ✅ |
| 376 | ItemBasePEOVersionId | VERSION_ID | — | ✅ |
| 377 | ItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | ✅ |
| 378 | ItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | ✅ |
| 379 | ItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | ✅ |
| 380 | ItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | ✅ |
| 381 | ItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | ✅ |
| 382 | ItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | ✅ |
| 383 | ItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 384 | ItemBasePEOWebStatus | WEB_STATUS | — | ✅ |
| 385 | ItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 386 | ItemBasePEOWhUpdateDate | WH_UPDATE_DATE | — | ✅ |
| 387 | ItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | ✅ |
| 388 | ItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | ✅ |
| 389 | ItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |

### [[egp_system_items_tl|egp_system_items_tl]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEODescription | DESCRIPTION | — | — |
| 2 | ItemTranslationPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | — |
| 3 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | ItemTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | — |
| 6 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
