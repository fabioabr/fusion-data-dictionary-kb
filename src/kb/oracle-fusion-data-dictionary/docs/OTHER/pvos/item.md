---
id: DOC-OTHER-PVO-Item
doc_type: system-doc
title: "Item — PVO Cross-Module"
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
  - Item
  - item
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Item

## 📌 Visão Geral

View Object para extração BICC de dados de Item. Acessa as tabelas: EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL, EGP_ITEM_REVISIONS_B_V (+11).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.Item`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 484 | 14 | 3 | 398 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 4 atributos (1 BICC)
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 4 atributos
- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 4 atributos
- [[egp_item_status_vl|EGP_ITEM_STATUS_VL]] — 2 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 332 atributos (2 PKs, 310 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 24 atributos (1 PKs, 20 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 17 atributos (3 BICC)
- [[inv_actions_vl|INV_ACTIONS_VL]] — 3 atributos
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 62 atributos (62 BICC)
- [[inv_rules_vl|INV_RULES_VL]] — 2 atributos
- [[ra_rules|RA_RULES]] — 6 atributos
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos

---

## ⚙️ Atributos

### [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassBasePEODefaultItemClassFlag | DEFAULT_ITEM_CLASS_FLAG | — | — |
| 2 | ItemClassBasePEOItemClassCode | ITEM_CLASS_CODE | — | — |
| 3 | ItemClassBasePEOItemClassId | ITEM_CLASS_ID | — | — |
| 4 | ItemClassBasePEOParentItemClassId | PARENT_ITEM_CLASS_ID | — | ✅ |

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassTranPEODescription | DESCRIPTION | — | — |
| 2 | ItemClassTranPEOItemClassId | ITEM_CLASS_ID | — | — |
| 3 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | — |
| 4 | ItemClassTranPEOLanguage | LANGUAGE | — | — |

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
| 1 | ItemStatusPEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 2 | ItemStatusPEOInventoryItemStatusName | INVENTORY_ITEM_STATUS_NAME | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForcePurchaseLeadTimeFlag | FORCE_PURCHASE_LEAD_TIME_FLAG | — | — |
| 2 | ItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | ✅ |
| 3 | ItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | ✅ |
| 4 | ItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | ✅ |
| 5 | ItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 6 | ItemBasePEOAcdType | ACD_TYPE | — | ✅ |
| 7 | ItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | ✅ |
| 8 | ItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | ✅ |
| 9 | ItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 10 | ItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 11 | ItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | ✅ |
| 12 | ItemBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 13 | ItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | ✅ |
| 14 | ItemBasePEOAssetCreationCode | ASSET_CREATION_CODE | — | ✅ |
| 15 | ItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | ✅ |
| 16 | ItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | ✅ |
| 17 | ItemBasePEOAtpFlag | ATP_FLAG | — | ✅ |
| 18 | ItemBasePEOAtpRuleId | ATP_RULE_ID | — | ✅ |
| 19 | ItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 20 | ItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | ✅ |
| 21 | ItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | ✅ |
| 22 | ItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | ✅ |
| 23 | ItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | ✅ |
| 24 | ItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 25 | ItemBasePEOBaseItemId | BASE_ITEM_ID | — | ✅ |
| 26 | ItemBasePEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 27 | ItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | ✅ |
| 28 | ItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | ✅ |
| 29 | ItemBasePEOBuyerId | BUYER_ID | — | ✅ |
| 30 | ItemBasePEOCarryingCost | CARRYING_COST | — | ✅ |
| 31 | ItemBasePEOCasNumber | CAS_NUMBER | — | ✅ |
| 32 | ItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | ✅ |
| 33 | ItemBasePEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 34 | ItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | ✅ |
| 35 | ItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | ✅ |
| 36 | ItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | ✅ |
| 37 | ItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | ✅ |
| 38 | ItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | ✅ |
| 39 | ItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | ✅ |
| 40 | ItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | ✅ |
| 41 | ItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | ✅ |
| 42 | ItemBasePEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | ✅ |
| 43 | ItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | — |
| 44 | ItemBasePEOConfigMatch | CONFIG_MATCH | — | ✅ |
| 45 | ItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | ✅ |
| 46 | ItemBasePEOConfigOrgs | CONFIG_ORGS | — | ✅ |
| 47 | ItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 48 | ItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | ✅ |
| 49 | ItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | ✅ |
| 50 | ItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | ✅ |
| 51 | ItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 52 | ItemBasePEOConvergence | CONVERGENCE | — | ✅ |
| 53 | ItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | ✅ |
| 54 | ItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | ✅ |
| 55 | ItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | ✅ |
| 56 | ItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | — |
| 57 | ItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | — |
| 58 | ItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | ✅ |
| 59 | ItemBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 60 | ItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | — |
| 61 | ItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | — |
| 62 | ItemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 63 | ItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | ✅ |
| 64 | ItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | ✅ |
| 65 | ItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | ✅ |
| 66 | ItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | ✅ |
| 67 | ItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | ✅ |
| 68 | ItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | ✅ |
| 69 | ItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | ✅ |
| 70 | ItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | ✅ |
| 71 | ItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 72 | ItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 73 | ItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | ✅ |
| 74 | ItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | ✅ |
| 75 | ItemBasePEODaysOfCover | DAYS_OF_COVER | — | — |
| 76 | ItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | ✅ |
| 77 | ItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | ✅ |
| 78 | ItemBasePEODefaultGrade | DEFAULT_GRADE | — | ✅ |
| 79 | ItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | ✅ |
| 80 | ItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | ✅ |
| 81 | ItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | ✅ |
| 82 | ItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | ✅ |
| 83 | ItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | ✅ |
| 84 | ItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | ✅ |
| 85 | ItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | ✅ |
| 86 | ItemBasePEODemandPeriod | DEMAND_PERIOD | — | — |
| 87 | ItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | ✅ |
| 88 | ItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | ✅ |
| 89 | ItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | ✅ |
| 90 | ItemBasePEODivergence | DIVERGENCE | — | ✅ |
| 91 | ItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | ✅ |
| 92 | ItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | ✅ |
| 93 | ItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | ✅ |
| 94 | ItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | ✅ |
| 95 | ItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | ✅ |
| 96 | ItemBasePEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | ✅ |
| 97 | ItemBasePEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | ✅ |
| 98 | ItemBasePEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | ✅ |
| 99 | ItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | ✅ |
| 100 | ItemBasePEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | ✅ |
| 101 | ItemBasePEOEamItemType | EAM_ITEM_TYPE | — | ✅ |
| 102 | ItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 103 | ItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | ✅ |
| 104 | ItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | ✅ |
| 105 | ItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | — |
| 106 | ItemBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 107 | ItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | ✅ |
| 108 | ItemBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 109 | ItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 110 | ItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | ✅ |
| 111 | ItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | ✅ |
| 112 | ItemBasePEOEventFlag | EVENT_FLAG | — | ✅ |
| 113 | ItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | ✅ |
| 114 | ItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 115 | ItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | ✅ |
| 116 | ItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | ✅ |
| 117 | ItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | ✅ |
| 118 | ItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | ✅ |
| 119 | ItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | ✅ |
| 120 | ItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 121 | ItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | ✅ |
| 122 | ItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | ✅ |
| 123 | ItemBasePEOForecastHorizon | FORECAST_HORIZON | — | ✅ |
| 124 | ItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 125 | ItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | ✅ |
| 126 | ItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | ✅ |
| 127 | ItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | — |
| 128 | ItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 129 | ItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | ✅ |
| 130 | ItemBasePEOHoldDays | HOLD_DAYS | — | ✅ |
| 131 | ItemBasePEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | ✅ |
| 132 | ItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 133 | ItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | ✅ |
| 134 | ItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 135 | ItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | ✅ |
| 136 | ItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | ✅ |
| 137 | ItemBasePEOInternalVolume | INTERNAL_VOLUME | — | ✅ |
| 138 | ItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 139 | ItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | ✅ |
| 140 | ItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | ✅ |
| 141 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 142 | ItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | ✅ |
| 143 | ItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 144 | ItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | ✅ |
| 145 | ItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 146 | ItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 147 | ItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | ✅ |
| 148 | ItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 149 | ItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 150 | ItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | ✅ |
| 151 | ItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 152 | ItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | — |
| 153 | ItemBasePEOItemType | ITEM_TYPE | — | ✅ |
| 154 | ItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 155 | ItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 156 | ItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | ✅ |
| 157 | ItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 158 | ItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 159 | ItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 160 | ItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | ✅ |
| 161 | ItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 162 | ItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | ✅ |
| 163 | ItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | ✅ |
| 164 | ItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | ✅ |
| 165 | ItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | ✅ |
| 166 | ItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | ✅ |
| 167 | ItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | ✅ |
| 168 | ItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | ✅ |
| 169 | ItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | ✅ |
| 170 | ItemBasePEOMarketPrice | MARKET_PRICE | — | ✅ |
| 171 | ItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | ✅ |
| 172 | ItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | ✅ |
| 173 | ItemBasePEOMaturityDays | MATURITY_DAYS | — | ✅ |
| 174 | ItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | ✅ |
| 175 | ItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | ✅ |
| 176 | ItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 177 | ItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | ✅ |
| 178 | ItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | ✅ |
| 179 | ItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | ✅ |
| 180 | ItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 181 | ItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | ✅ |
| 182 | ItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 183 | ItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | ✅ |
| 184 | ItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | ✅ |
| 185 | ItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | ✅ |
| 186 | ItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | ✅ |
| 187 | ItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | ✅ |
| 188 | ItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | ✅ |
| 189 | ItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 190 | ItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | ✅ |
| 191 | ItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | ✅ |
| 192 | ItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | ✅ |
| 193 | ItemBasePEOOrderCost | ORDER_COST | — | ✅ |
| 194 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | — |
| 195 | ItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | ✅ |
| 196 | ItemBasePEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 197 | ItemBasePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | ✅ |
| 198 | ItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | ✅ |
| 199 | ItemBasePEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | ✅ |
| 200 | ItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | ✅ |
| 201 | ItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | ✅ |
| 202 | ItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | ✅ |
| 203 | ItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | ✅ |
| 204 | ItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | ✅ |
| 205 | ItemBasePEOPackagingStringId | PACKAGING_STRING_ID | — | — |
| 206 | ItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | ✅ |
| 207 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | — |
| 208 | ItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 209 | ItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | ✅ |
| 210 | ItemBasePEOPickingRuleId | PICKING_RULE_ID | — | ✅ |
| 211 | ItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | ✅ |
| 212 | ItemBasePEOPlannerCode | PLANNER_CODE | — | ✅ |
| 213 | ItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | ✅ |
| 214 | ItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 215 | ItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | ✅ |
| 216 | ItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | ✅ |
| 217 | ItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | ✅ |
| 218 | ItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 219 | ItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | ✅ |
| 220 | ItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 221 | ItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | ✅ |
| 222 | ItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 223 | ItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | ✅ |
| 224 | ItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | ✅ |
| 225 | ItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | ✅ |
| 226 | ItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | ✅ |
| 227 | ItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | ✅ |
| 228 | ItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | ✅ |
| 229 | ItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | ✅ |
| 230 | ItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | ✅ |
| 231 | ItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 232 | ItemBasePEOProgramName | PROGRAM_NAME | — | ✅ |
| 233 | ItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | ✅ |
| 234 | ItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | ✅ |
| 235 | ItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | ✅ |
| 236 | ItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | ✅ |
| 237 | ItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 238 | ItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 239 | ItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 240 | ItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 241 | ItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 242 | ItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 243 | ItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | ✅ |
| 244 | ItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | ✅ |
| 245 | ItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | ✅ |
| 246 | ItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | ✅ |
| 247 | ItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | ✅ |
| 248 | ItemBasePEORepairProgram | REPAIR_PROGRAM | — | ✅ |
| 249 | ItemBasePEORepairTransactionCode | REPAIR_TRANSACTION_CODE | — | — |
| 250 | ItemBasePEORepairYield | REPAIR_YIELD | — | ✅ |
| 251 | ItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | ✅ |
| 252 | ItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | ✅ |
| 253 | ItemBasePEORequestId | REQUEST_ID | — | ✅ |
| 254 | ItemBasePEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 255 | ItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | ✅ |
| 256 | ItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | ✅ |
| 257 | ItemBasePEORetestInterval | RETEST_INTERVAL | — | ✅ |
| 258 | ItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | ✅ |
| 259 | ItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 260 | ItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | ✅ |
| 261 | ItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | ✅ |
| 262 | ItemBasePEORoundingFactor | ROUNDING_FACTOR | — | ✅ |
| 263 | ItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | ✅ |
| 264 | ItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 265 | ItemBasePEOSalesAccount | SALES_ACCOUNT | — | ✅ |
| 266 | ItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | ✅ |
| 267 | ItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | ✅ |
| 268 | ItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 269 | ItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | ✅ |
| 270 | ItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | ✅ |
| 271 | ItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | ✅ |
| 272 | ItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | ✅ |
| 273 | ItemBasePEOServiceDuration | SERVICE_DURATION | — | ✅ |
| 274 | ItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | ✅ |
| 275 | ItemBasePEOServiceStartingDelay | SERVICE_START_DELAY | — | ✅ |
| 276 | ItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | ✅ |
| 277 | ItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | ✅ |
| 278 | ItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | ✅ |
| 279 | ItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | ✅ |
| 280 | ItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | ✅ |
| 281 | ItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | ✅ |
| 282 | ItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | ✅ |
| 283 | ItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | ✅ |
| 284 | ItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 285 | ItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 286 | ItemBasePEOSourceType | SOURCE_TYPE | — | ✅ |
| 287 | ItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | ✅ |
| 288 | ItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 289 | ItemBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 290 | ItemBasePEOStdLotSize | STD_LOT_SIZE | — | ✅ |
| 291 | ItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | ✅ |
| 292 | ItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 293 | ItemBasePEOStyleItemId | STYLE_ITEM_ID | — | ✅ |
| 294 | ItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | ✅ |
| 295 | ItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | ✅ |
| 296 | ItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | ✅ |
| 297 | ItemBasePEOSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 298 | ItemBasePEOTaxCode | TAX_CODE | — | ✅ |
| 299 | ItemBasePEOTaxableFlag | TAXABLE_FLAG | — | ✅ |
| 300 | ItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | ✅ |
| 301 | ItemBasePEOTemplateName | ITEM_NUMBER | — | ✅ |
| 302 | ItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 303 | ItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | ✅ |
| 304 | ItemBasePEOUnNumberId | UN_NUMBER_ID | — | ✅ |
| 305 | ItemBasePEOUnderCompletionToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | — |
| 306 | ItemBasePEOUnderCompletionToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | — |
| 307 | ItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | ✅ |
| 308 | ItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | ✅ |
| 309 | ItemBasePEOUnitHeight | UNIT_HEIGHT | — | ✅ |
| 310 | ItemBasePEOUnitLength | UNIT_LENGTH | — | ✅ |
| 311 | ItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | ✅ |
| 312 | ItemBasePEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 313 | ItemBasePEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 314 | ItemBasePEOUnitWidth | UNIT_WIDTH | — | ✅ |
| 315 | ItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 316 | ItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | ✅ |
| 317 | ItemBasePEOVersionEndDate | VERSION_END_DATE | — | ✅ |
| 318 | ItemBasePEOVersionId | VERSION_ID | — | ✅ |
| 319 | ItemBasePEOVersionStartDate | VERSION_START_DATE | — | ✅ |
| 320 | ItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | ✅ |
| 321 | ItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | ✅ |
| 322 | ItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | ✅ |
| 323 | ItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | ✅ |
| 324 | ItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | ✅ |
| 325 | ItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | ✅ |
| 326 | ItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 327 | ItemBasePEOWebStatus | WEB_STATUS | — | ✅ |
| 328 | ItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 329 | ItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | ✅ |
| 330 | ItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | ✅ |
| 331 | ItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |
| 332 | ReplacementType | REPLACEMENT_TYPE | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEO1CreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemTranslationPEO1CreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemTranslationPEO1Description | DESCRIPTION | — | ✅ |
| 4 | ItemTranslationPEO1InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 5 | ItemTranslationPEO1Language | LANGUAGE | — | ✅ |
| 6 | ItemTranslationPEO1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ItemTranslationPEO1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ItemTranslationPEO1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ItemTranslationPEO1LongDescription | LONG_DESCRIPTION | — | ✅ |
| 10 | ItemTranslationPEO1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ItemTranslationPEO1OrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | ItemTranslationPEO1SourceLang | SOURCE_LANG | — | ✅ |
| 13 | ItemTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | ItemTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | ItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 16 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 17 | ItemTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 18 | ItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 22 | ItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 24 | ItemTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromItemPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | CreatedFromItemPEOItemNumber | ITEM_NUMBER | — | — |
| 4 | CreatedFromItemPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
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
| 15 | OrganizationUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | — |
| 18 | OrganizationUnitPEOType | TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterOrgUnitTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MasterOrgUnitTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MasterOrgUnitTLPEOLanguage | LANGUAGE | — | — |
| 4 | MasterOrgUnitTLPEOName | NAME | — | — |
| 5 | MasterOrgUnitTLPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | OrganizationUnitTLPEOCreatedBy | CREATED_BY | — | — |
| 7 | OrganizationUnitTLPEOCreationDate | CREATION_DATE | — | — |
| 8 | OrganizationUnitTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | OrganizationUnitTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | OrganizationUnitTLPEOLanguage | LANGUAGE | — | — |
| 11 | OrganizationUnitTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrganizationUnitTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrganizationUnitTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrganizationUnitTLPEOName | NAME | — | — |
| 15 | OrganizationUnitTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | OrganizationUnitTLPEOOrganizationId | ORGANIZATION_ID | — | — |
| 17 | OrganizationUnitTLPEOSourceLang | SOURCE_LANG | — | — |

### [[inv_actions_vl|INV_ACTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MtlActionsVlActionCode | ACTION_CODE | — | — |
| 2 | MtlActionsVlDescription | DESCRIPTION | — | — |
| 3 | MtlActionsVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | ✅ |
| 2 | ItemOrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | ✅ |
| 3 | ItemOrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | ✅ |
| 4 | ItemOrganizationParameterPEOAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | ✅ |
| 5 | ItemOrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | ✅ |
| 6 | ItemOrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | ✅ |
| 7 | ItemOrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | ✅ |
| 8 | ItemOrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 9 | ItemOrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | ✅ |
| 10 | ItemOrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | ✅ |
| 11 | ItemOrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | ✅ |
| 12 | ItemOrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | ✅ |
| 13 | ItemOrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | ✅ |
| 14 | ItemOrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | ✅ |
| 15 | ItemOrganizationParameterPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | ItemOrganizationParameterPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | ItemOrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | ✅ |
| 18 | ItemOrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | ✅ |
| 19 | ItemOrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | ✅ |
| 20 | ItemOrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | ✅ |
| 21 | ItemOrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | ✅ |
| 22 | ItemOrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | ✅ |
| 23 | ItemOrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | ✅ |
| 24 | ItemOrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | ✅ |
| 25 | ItemOrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 26 | ItemOrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 27 | ItemOrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ItemOrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | ItemOrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ItemOrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 31 | ItemOrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | ✅ |
| 32 | ItemOrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | ✅ |
| 33 | ItemOrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | ✅ |
| 34 | ItemOrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | ✅ |
| 35 | ItemOrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | ✅ |
| 36 | ItemOrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | ✅ |
| 37 | ItemOrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | ✅ |
| 38 | ItemOrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | ✅ |
| 39 | ItemOrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | ✅ |
| 40 | ItemOrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | ✅ |
| 41 | ItemOrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 42 | ItemOrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 43 | ItemOrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 44 | ItemOrganizationParameterPEOOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | ✅ |
| 45 | ItemOrganizationParameterPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | ✅ |
| 46 | ItemOrganizationParameterPEOPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | ✅ |
| 47 | ItemOrganizationParameterPEOPurchasingByRevision | PURCHASING_BY_REVISION | — | ✅ |
| 48 | ItemOrganizationParameterPEOReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | ✅ |
| 49 | ItemOrganizationParameterPEORequestId | REQUEST_ID | — | ✅ |
| 50 | ItemOrganizationParameterPEORoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | ✅ |
| 51 | ItemOrganizationParameterPEOScheduleId | SCHEDULE_ID | — | ✅ |
| 52 | ItemOrganizationParameterPEOSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | ✅ |
| 53 | ItemOrganizationParameterPEOSerialNumberType | SERIAL_NUMBER_TYPE | — | ✅ |
| 54 | ItemOrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 55 | ItemOrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 56 | ItemOrganizationParameterPEOSourceType | SOURCE_TYPE | — | ✅ |
| 57 | ItemOrganizationParameterPEOStandardPackEnabled | STANDARD_PACK_ENABLED | — | ✅ |
| 58 | ItemOrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 59 | ItemOrganizationParameterPEOStartingRevision | STARTING_REVISION | — | ✅ |
| 60 | ItemOrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | ✅ |
| 61 | ItemOrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | ✅ |
| 62 | ItemOrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | ✅ |

### [[inv_rules_vl|INV_RULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryRulePEORuleId | RULE_ID | — | — |
| 2 | InventoryRulePEORuleName | RULE_NAME | — | — |

### [[ra_rules|RA_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionRulePEOAccountingName | NAME | — | — |
| 2 | DistributionRulePEOAccountingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | DistributionRulePEOAccountingRuleId | RULE_ID | — | — |
| 4 | DistributionRulePEOInvoicingName | NAME | — | — |
| 5 | DistributionRulePEOInvoicingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | DistributionRulePEOInvoicingRuleId | RULE_ID | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermsVlName | NAME | — | — |
| 2 | RaTermsVlTermId | TERM_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
