---
id: DOC-OTHER-PVO-ItemRef
doc_type: system-doc
title: "ItemRef — PVO Cross-Module"
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
  - ItemRef
  - itemref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemRef

## 📌 Visão Geral

View Object para extração BICC de dados de Item Ref. Acessa as tabelas: EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL, EGP_ITEM_REVISIONS_B_V (+17).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 519 | 20 | 2 | 214 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 4 atributos (2 BICC)
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 4 atributos (3 BICC)
- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 4 atributos
- [[egp_item_status_vl|EGP_ITEM_STATUS_VL]] — 2 atributos (2 BICC)
- [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]] — 1 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 348 atributos (2 PKs, 156 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 13 atributos (7 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 8 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (6 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 17 atributos (10 BICC)
- [[inv_actions_tl|INV_ACTIONS_TL]] — 4 atributos (1 BICC)
- [[inv_material_statuses_vl|INV_MATERIAL_STATUSES_VL]] — 6 atributos
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 62 atributos (13 BICC)
- [[inv_rules_vl|INV_RULES_VL]] — 2 atributos (2 BICC)
- [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]] — 8 atributos
- [[msc_planners_with_pimid_v|MSC_PLANNERS_WITH_PIMID_V]] — 5 atributos (5 BICC)
- [[okc_coverage_headers_vl|OKC_COVERAGE_HEADERS_VL]] — 3 atributos
- [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]] — 2 atributos
- [[ra_rules|RA_RULES]] — 6 atributos (6 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassBasePEODefaultItemClassFlag | DEFAULT_ITEM_CLASS_FLAG | — | — |
| 2 | ItemClassBasePEOItemClassCode | ITEM_CLASS_CODE | — | ✅ |
| 3 | ItemClassBasePEOItemClassId | ITEM_CLASS_ID | — | ✅ |
| 4 | ItemClassBasePEOParentItemClassId | PARENT_ITEM_CLASS_ID | — | — |

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassTranPEODescription | DESCRIPTION | — | — |
| 2 | ItemClassTranPEOItemClassId | ITEM_CLASS_ID | — | ✅ |
| 3 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | ✅ |
| 4 | ItemClassTranPEOLanguage | LANGUAGE | — | ✅ |

### [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromRevisionPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromRevisionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 3 | CreatedFromRevisionPEORevision | REVISION | — | — |
| 4 | CreatedFromRevisionPEORevisionId | REVISION_ID | — | — |

### [[egp_item_status_vl|EGP_ITEM_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemStatusPEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | ✅ |
| 2 | ItemStatusPEOInventoryItemStatusName | INVENTORY_ITEM_STATUS_NAME | — | ✅ |

### [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemBasePEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForcePurchaseLeadTimeFlag | FORCE_PURCHASE_LEAD_TIME_FLAG | — | ✅ |
| 2 | InventoryItemBasePEOPreliminaryItemFlag | PRELIMINARY_ITEM_FLAG | — | — |
| 3 | ItemBaePEOEngineeredItemFlag | ENGINEERED_ITEM_FLAG | — | — |
| 4 | ItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 5 | ItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 6 | ItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 7 | ItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 8 | ItemBasePEOAcdType | ACD_TYPE | — | — |
| 9 | ItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | ✅ |
| 10 | ItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 11 | ItemBasePEOAllowMaintenanceAssetFlag | ALLOW_MAINTENANCE_ASSET_FLAG | — | — |
| 12 | ItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 13 | ItemBasePEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | — |
| 14 | ItemBasePEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | — |
| 15 | ItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 16 | ItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | ✅ |
| 17 | ItemBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 18 | ItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 19 | ItemBasePEOAssetClass | ASSET_CLASS | — | ✅ |
| 20 | ItemBasePEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 21 | ItemBasePEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | ✅ |
| 22 | ItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 23 | ItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | ✅ |
| 24 | ItemBasePEOAtpFlag | ATP_FLAG | — | ✅ |
| 25 | ItemBasePEOAtpRuleId | ATP_RULE_ID | — | ✅ |
| 26 | ItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 27 | ItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 28 | ItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 29 | ItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 30 | ItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 31 | ItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 32 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | ✅ |
| 33 | ItemBasePEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 34 | ItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 35 | ItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | ✅ |
| 36 | ItemBasePEOBuyerId | BUYER_ID | — | ✅ |
| 37 | ItemBasePEOCarryingCost | CARRYING_COST | — | ✅ |
| 38 | ItemBasePEOCasNumber | CAS_NUMBER | — | ✅ |
| 39 | ItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 40 | ItemBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 41 | ItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | ✅ |
| 42 | ItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 43 | ItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 44 | ItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 45 | ItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 46 | ItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 47 | ItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | ✅ |
| 48 | ItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 49 | ItemBasePEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 50 | ItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | — |
| 51 | ItemBasePEOCompletenessScore | COMPLETENESS_SCORE | — | — |
| 52 | ItemBasePEOConfigMatch | CONFIG_MATCH | — | — |
| 53 | ItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | ✅ |
| 54 | ItemBasePEOConfigOrgs | CONFIG_ORGS | — | — |
| 55 | ItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 56 | ItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | ✅ |
| 57 | ItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | ✅ |
| 58 | ItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 59 | ItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 60 | ItemBasePEOConvergence | CONVERGENCE | — | — |
| 61 | ItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 62 | ItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | ✅ |
| 63 | ItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 64 | ItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | — |
| 65 | ItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | — |
| 66 | ItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 67 | ItemBasePEOCreatedBy | CREATED_BY | — | — |
| 68 | ItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | — |
| 69 | ItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | — |
| 70 | ItemBasePEOCreationDate | CREATION_DATE | — | — |
| 71 | ItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 72 | ItemBasePEOCssEnabledFlag | CSS_ENABLED_FLAG | — | — |
| 73 | ItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | — |
| 74 | ItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | — |
| 75 | ItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | ✅ |
| 76 | ItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | ✅ |
| 77 | ItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | ✅ |
| 78 | ItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | ✅ |
| 79 | ItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | ✅ |
| 80 | ItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 81 | ItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 82 | ItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 83 | ItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 84 | ItemBasePEODaysOfCover | DAYS_OF_COVER | — | — |
| 85 | ItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 86 | ItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 87 | ItemBasePEODefaultGrade | DEFAULT_GRADE | — | — |
| 88 | ItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | ✅ |
| 89 | ItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 90 | ItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 91 | ItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 92 | ItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 93 | ItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 94 | ItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 95 | ItemBasePEODemandPeriod | DEMAND_PERIOD | — | — |
| 96 | ItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 97 | ItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 98 | ItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | ✅ |
| 99 | ItemBasePEODivergence | DIVERGENCE | — | — |
| 100 | ItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | ✅ |
| 101 | ItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 102 | ItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | ✅ |
| 103 | ItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 104 | ItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 105 | ItemBasePEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 106 | ItemBasePEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 107 | ItemBasePEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 108 | ItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 109 | ItemBasePEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 110 | ItemBasePEOEamItemType | EAM_ITEM_TYPE | — | — |
| 111 | ItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 112 | ItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | ✅ |
| 113 | ItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | ✅ |
| 114 | ItemBasePEOEnableGenealogyTrackingFlag | ENABLE_GENEALOGY_TRACKING_FLAG | — | — |
| 115 | ItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | — |
| 116 | ItemBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 117 | ItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | ✅ |
| 118 | ItemBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 119 | ItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 120 | ItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | ✅ |
| 121 | ItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | ✅ |
| 122 | ItemBasePEOEventFlag | EVENT_FLAG | — | ✅ |
| 123 | ItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | ✅ |
| 124 | ItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 125 | ItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | ✅ |
| 126 | ItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | ✅ |
| 127 | ItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | ✅ |
| 128 | ItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | ✅ |
| 129 | ItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 130 | ItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 131 | ItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | ✅ |
| 132 | ItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | ✅ |
| 133 | ItemBasePEOForecastHorizon | FORECAST_HORIZON | — | ✅ |
| 134 | ItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 135 | ItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | ✅ |
| 136 | ItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | ✅ |
| 137 | ItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | — |
| 138 | ItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 139 | ItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | ✅ |
| 140 | ItemBasePEOHoldDays | HOLD_DAYS | — | ✅ |
| 141 | ItemBasePEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 142 | ItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 143 | ItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | ✅ |
| 144 | ItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 145 | ItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | ✅ |
| 146 | ItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | ✅ |
| 147 | ItemBasePEOInternalVolume | INTERNAL_VOLUME | — | ✅ |
| 148 | ItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 149 | ItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | ✅ |
| 150 | ItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | ✅ |
| 151 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 152 | ItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | ✅ |
| 153 | ItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 154 | ItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | ✅ |
| 155 | ItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 156 | ItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 157 | ItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | ✅ |
| 158 | ItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 159 | ItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 160 | ItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | ✅ |
| 161 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 162 | ItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | — |
| 163 | ItemBasePEOItemType | ITEM_TYPE | — | ✅ |
| 164 | ItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 165 | ItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 166 | ItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | ✅ |
| 167 | ItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 168 | ItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 169 | ItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 170 | ItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 171 | ItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 172 | ItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | ✅ |
| 173 | ItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | ✅ |
| 174 | ItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 175 | ItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 176 | ItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 177 | ItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | ✅ |
| 178 | ItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 179 | ItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | ✅ |
| 180 | ItemBasePEOMarketPrice | MARKET_PRICE | — | ✅ |
| 181 | ItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | ✅ |
| 182 | ItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | ✅ |
| 183 | ItemBasePEOMaturityDays | MATURITY_DAYS | — | ✅ |
| 184 | ItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | ✅ |
| 185 | ItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | ✅ |
| 186 | ItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 187 | ItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | ✅ |
| 188 | ItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | ✅ |
| 189 | ItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 190 | ItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | — |
| 191 | ItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 192 | ItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | — |
| 193 | ItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 194 | ItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 195 | ItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | ✅ |
| 196 | ItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 197 | ItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 198 | ItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 199 | ItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 200 | ItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | ✅ |
| 201 | ItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 202 | ItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 203 | ItemBasePEOOrderCost | ORDER_COST | — | — |
| 204 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | — |
| 205 | ItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 206 | ItemBasePEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 207 | ItemBasePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | ✅ |
| 208 | ItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | ✅ |
| 209 | ItemBasePEOOutsideProcessServiceFlag | OUTSIDE_PROCESS_SERVICE_FLAG | — | — |
| 210 | ItemBasePEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | ✅ |
| 211 | ItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 212 | ItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 213 | ItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 214 | ItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 215 | ItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 216 | ItemBasePEOPackagingStringId | PACKAGING_STRING_ID | — | — |
| 217 | ItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 218 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | — |
| 219 | ItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 220 | ItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | ✅ |
| 221 | ItemBasePEOPickingRuleId | PICKING_RULE_ID | — | — |
| 222 | ItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 223 | ItemBasePEOPlannerCode | PLANNER_CODE | — | — |
| 224 | ItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 225 | ItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 226 | ItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 227 | ItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | — |
| 228 | ItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 229 | ItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 230 | ItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 231 | ItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 232 | ItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 233 | ItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 234 | ItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 235 | ItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 236 | ItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | — |
| 237 | ItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 238 | ItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 239 | ItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 240 | ItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 241 | ItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 242 | ItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 243 | ItemBasePEOProgramName | PROGRAM_NAME | — | — |
| 244 | ItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | ✅ |
| 245 | ItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | ✅ |
| 246 | ItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | ✅ |
| 247 | ItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 248 | ItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 249 | ItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 250 | ItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 251 | ItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 252 | ItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 253 | ItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 254 | ItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 255 | ItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 256 | ItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 257 | ItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 258 | ItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 259 | ItemBasePEORepairProgram | REPAIR_PROGRAM | — | — |
| 260 | ItemBasePEORepairTransactionCode | REPAIR_TRANSACTION_CODE | — | — |
| 261 | ItemBasePEORepairYield | REPAIR_YIELD | — | — |
| 262 | ItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 263 | ItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 264 | ItemBasePEORequestId | REQUEST_ID | — | — |
| 265 | ItemBasePEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | — |
| 266 | ItemBasePEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | — |
| 267 | ItemBasePEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 268 | ItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | ✅ |
| 269 | ItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | ✅ |
| 270 | ItemBasePEORetestInterval | RETEST_INTERVAL | — | — |
| 271 | ItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | ✅ |
| 272 | ItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 273 | ItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | ✅ |
| 274 | ItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 275 | ItemBasePEORoundingFactor | ROUNDING_FACTOR | — | — |
| 276 | ItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 277 | ItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 278 | ItemBasePEOSalesAccount | SALES_ACCOUNT | — | ✅ |
| 279 | ItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | ✅ |
| 280 | ItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | ✅ |
| 281 | ItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 282 | ItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | ✅ |
| 283 | ItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | ✅ |
| 284 | ItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 285 | ItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 286 | ItemBasePEOServiceDuration | SERVICE_DURATION | — | — |
| 287 | ItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 288 | ItemBasePEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | — |
| 289 | ItemBasePEOServiceStartDelay | SERVICE_START_DELAY | — | — |
| 290 | ItemBasePEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | — |
| 291 | ItemBasePEOServiceStartingDelay | SERVICE_STARTING_DELAY | — | — |
| 292 | ItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 293 | ItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | ✅ |
| 294 | ItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | ✅ |
| 295 | ItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | ✅ |
| 296 | ItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | ✅ |
| 297 | ItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 298 | ItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 299 | ItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | ✅ |
| 300 | ItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 301 | ItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 302 | ItemBasePEOSourceType | SOURCE_TYPE | — | ✅ |
| 303 | ItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | ✅ |
| 304 | ItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 305 | ItemBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 306 | ItemBasePEOStdLotSize | STD_LOT_SIZE | — | ✅ |
| 307 | ItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | ✅ |
| 308 | ItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 309 | ItemBasePEOStyleItemId | STYLE_ITEM_ID | — | ✅ |
| 310 | ItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 311 | ItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 312 | ItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 313 | ItemBasePEOSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 314 | ItemBasePEOTaxCode | TAX_CODE | — | ✅ |
| 315 | ItemBasePEOTaxableFlag | TAXABLE_FLAG | — | ✅ |
| 316 | ItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 317 | ItemBasePEOTemplateName | ITEM_NUMBER | — | — |
| 318 | ItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 319 | ItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | ✅ |
| 320 | ItemBasePEOUnNumberId | UN_NUMBER_ID | — | ✅ |
| 321 | ItemBasePEOUnderCompletionToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | — |
| 322 | ItemBasePEOUnderCompletionToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | — |
| 323 | ItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 324 | ItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 325 | ItemBasePEOUnitHeight | UNIT_HEIGHT | — | ✅ |
| 326 | ItemBasePEOUnitLength | UNIT_LENGTH | — | ✅ |
| 327 | ItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | ✅ |
| 328 | ItemBasePEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 329 | ItemBasePEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 330 | ItemBasePEOUnitWidth | UNIT_WIDTH | — | ✅ |
| 331 | ItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 332 | ItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | ✅ |
| 333 | ItemBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 334 | ItemBasePEOVersionId | VERSION_ID | — | — |
| 335 | ItemBasePEOVersionStartDate | VERSION_START_DATE | — | — |
| 336 | ItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 337 | ItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 338 | ItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 339 | ItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 340 | ItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 341 | ItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 342 | ItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 343 | ItemBasePEOWebStatus | WEB_STATUS | — | — |
| 344 | ItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 345 | ItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 346 | ItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 347 | ItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |
| 348 | ReplacementType | REPLACEMENT_TYPE | — | ✅ |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ItemTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemTranslationPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | — |
| 5 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 6 | ItemTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | ItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 11 | ItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 13 | ItemTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromItemPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | CreatedFromItemPEOItemNumber | ITEM_NUMBER | — | — |
| 4 | CreatedFromItemPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | StyleItemAllPEODescription | DESCRIPTION | — | — |
| 6 | StyleItemAllPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 7 | StyleItemAllPEOItemNumber | ITEM_NUMBER | — | — |
| 8 | StyleItemAllPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | OrganizationUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | OrganizationUnitPEOCreatedBy | CREATED_BY | — | — |
| 5 | OrganizationUnitPEOCreationDate | CREATION_DATE | — | — |
| 6 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | OrganizationUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 9 | OrganizationUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 10 | OrganizationUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 11 | OrganizationUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrganizationUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | OrganizationUnitPEOLocationId | LOCATION_ID | — | ✅ |
| 16 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 18 | OrganizationUnitPEOType | TYPE | — | ✅ |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterOrgUnitTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MasterOrgUnitTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MasterOrgUnitTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | MasterOrgUnitTLPEOName | NAME | — | ✅ |
| 5 | MasterOrgUnitTLPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 6 | OrganizationUnitTLPEOCreatedBy | CREATED_BY | — | — |
| 7 | OrganizationUnitTLPEOCreationDate | CREATION_DATE | — | — |
| 8 | OrganizationUnitTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | OrganizationUnitTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | OrganizationUnitTLPEOLanguage | LANGUAGE | — | ✅ |
| 11 | OrganizationUnitTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrganizationUnitTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationUnitTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationUnitTLPEOName | NAME | — | ✅ |
| 15 | OrganizationUnitTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | OrganizationUnitTLPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | OrganizationUnitTLPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[inv_actions_tl|INV_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MtlActionsVlActionCode | ACTION_CODE | — | — |
| 2 | MtlActionsVlDescription | DESCRIPTION | — | ✅ |
| 3 | MtlActionsVlLanguage | LANGUAGE | — | — |
| 4 | MtlActionsVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_material_statuses_vl|INV_MATERIAL_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefaultLotStatusPEODescription | DESCRIPTION | — | — |
| 2 | DefaultLotStatusPEOStatusCode | STATUS_CODE | — | — |
| 3 | DefaultLotStatusPEOStatusId | STATUS_ID | — | — |
| 4 | DefaultSerialStatusPEODescription | DESCRIPTION | — | — |
| 5 | DefaultSerialStatusPEOStatusCode | STATUS_CODE | — | — |
| 6 | DefaultSerialStatusPEOStatusId | STATUS_ID | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | — |
| 2 | ItemOrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | — |
| 3 | ItemOrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | — |
| 4 | ItemOrganizationParameterPEOAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | — |
| 5 | ItemOrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | — |
| 6 | ItemOrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 7 | ItemOrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 8 | ItemOrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 9 | ItemOrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | — |
| 10 | ItemOrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | — |
| 11 | ItemOrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 12 | ItemOrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | — |
| 13 | ItemOrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 14 | ItemOrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | — |
| 15 | ItemOrganizationParameterPEOCreatedBy | CREATED_BY | — | — |
| 16 | ItemOrganizationParameterPEOCreationDate | CREATION_DATE | — | — |
| 17 | ItemOrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | ✅ |
| 18 | ItemOrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | ✅ |
| 19 | ItemOrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | ✅ |
| 20 | ItemOrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 21 | ItemOrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | — |
| 22 | ItemOrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | — |
| 23 | ItemOrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | — |
| 24 | ItemOrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | ✅ |
| 25 | ItemOrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 26 | ItemOrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | ItemOrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ItemOrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | ItemOrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | ItemOrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 31 | ItemOrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | — |
| 32 | ItemOrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | — |
| 33 | ItemOrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | — |
| 34 | ItemOrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | — |
| 35 | ItemOrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | — |
| 36 | ItemOrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | — |
| 37 | ItemOrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | — |
| 38 | ItemOrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 39 | ItemOrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | — |
| 40 | ItemOrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | — |
| 41 | ItemOrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | ItemOrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 43 | ItemOrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 44 | ItemOrganizationParameterPEOOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | — |
| 45 | ItemOrganizationParameterPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 46 | ItemOrganizationParameterPEOPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | — |
| 47 | ItemOrganizationParameterPEOPurchasingByRevision | PURCHASING_BY_REVISION | — | — |
| 48 | ItemOrganizationParameterPEOReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | — |
| 49 | ItemOrganizationParameterPEORequestId | REQUEST_ID | — | — |
| 50 | ItemOrganizationParameterPEORoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | — |
| 51 | ItemOrganizationParameterPEOScheduleId | SCHEDULE_ID | — | — |
| 52 | ItemOrganizationParameterPEOSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | — |
| 53 | ItemOrganizationParameterPEOSerialNumberType | SERIAL_NUMBER_TYPE | — | — |
| 54 | ItemOrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 55 | ItemOrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 56 | ItemOrganizationParameterPEOSourceType | SOURCE_TYPE | — | ✅ |
| 57 | ItemOrganizationParameterPEOStandardPackEnabled | STANDARD_PACK_ENABLED | — | — |
| 58 | ItemOrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 59 | ItemOrganizationParameterPEOStartingRevision | STARTING_REVISION | — | — |
| 60 | ItemOrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | — |
| 61 | ItemOrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | — |
| 62 | ItemOrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | — |

### [[inv_rules_vl|INV_RULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryRulePEORuleId | RULE_ID | — | ✅ |
| 2 | InventoryRulePEORuleName | RULE_NAME | — | ✅ |

### [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PSInvSubInventoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | PSInvSubInventoryPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |
| 3 | PSInvSubInventoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 4 | PSInvSubInventoryPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 5 | WipInvSubInventoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | WipInvSubInventoryPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |
| 7 | WipInvSubInventoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 8 | WipInvSubInventoryPEOSubinventoryId | SUBINVENTORY_ID | — | — |

### [[msc_planners_with_pimid_v|MSC_PLANNERS_WITH_PIMID_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlannerPEODescription | DESCRIPTION | — | ✅ |
| 2 | PlannerPEOEMailAddress | ELECTRONIC_MAIL_ADDRESS | — | ✅ |
| 3 | PlannerPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 4 | PlannerPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 5 | PlannerPEOPlannerCode | PLANNER_CODE | — | ✅ |

### [[okc_coverage_headers_vl|OKC_COVERAGE_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractCoveragePEOCoverageDescription | COVERAGE_DESCRIPTION | — | — |
| 2 | ContractCoveragePEOCoverageHeaderId | COVERAGE_HEADER_ID | — | — |
| 3 | ContractCoveragePEOCoverageName | COVERAGE_NAME | — | — |

### [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgentAssignmentPEOAgentId | AGENT_ID | — | — |
| 2 | AgentAssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionRulePEOAccountingName | NAME | — | ✅ |
| 2 | DistributionRulePEOAccountingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | DistributionRulePEOAccountingRuleId | RULE_ID | — | ✅ |
| 4 | DistributionRulePEOInvoicingName | NAME | — | ✅ |
| 5 | DistributionRulePEOInvoicingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 6 | DistributionRulePEOInvoicingRuleId | RULE_ID | — | ✅ |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermsVlName | NAME | — | ✅ |
| 2 | RaTermsVlTermId | TERM_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
