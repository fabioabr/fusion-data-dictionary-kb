---
id: DOC-OTHER-PVO-InventoryItem
doc_type: system-doc
title: "InventoryItem — PVO Cross-Module"
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
  - InventoryItem
  - inventoryitem
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryItem

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Item. Acessa as tabelas: EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL, EGP_ITEM_REVISIONS_B_V (+11).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.InventoryItem`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 515 | 14 | 3 | 52 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 40 atributos (1 BICC)
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 11 atributos (1 BICC)
- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 4 atributos
- [[egp_item_status_vl|EGP_ITEM_STATUS_VL]] — 2 atributos
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 332 atributos (2 PKs, 34 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 12 atributos (1 PKs, 10 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 4 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (2 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 17 atributos (3 BICC)
- [[inv_actions_vl|INV_ACTIONS_VL]] — 3 atributos
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 62 atributos (1 BICC)
- [[inv_rules_vl|INV_RULES_VL]] — 2 atributos
- [[ra_rules|RA_RULES]] — 6 atributos
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos

---

## ⚙️ Atributos

### [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 2 | ItemClassBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 3 | ItemClassBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 4 | ItemClassBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 5 | ItemClassBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 6 | ItemClassBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 7 | ItemClassBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 8 | ItemClassBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 9 | ItemClassBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 10 | ItemClassBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 11 | ItemClassBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 12 | ItemClassBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 13 | ItemClassBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 14 | ItemClassBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 15 | ItemClassBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 16 | ItemClassBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 17 | ItemClassBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 18 | ItemClassBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 19 | ItemClassBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 20 | ItemClassBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 21 | ItemClassBasePEOChangeOrderTypeId | CHANGE_ORDER_TYPE_ID | — | — |
| 22 | ItemClassBasePEOCreatedBy | CREATED_BY | — | — |
| 23 | ItemClassBasePEOCreationDate | CREATION_DATE | — | — |
| 24 | ItemClassBasePEODefaultItemClassFlag | DEFAULT_ITEM_CLASS_FLAG | — | — |
| 25 | ItemClassBasePEOItemClassCode | ITEM_CLASS_CODE | — | — |
| 26 | ItemClassBasePEOItemClassId | ITEM_CLASS_ID | — | — |
| 27 | ItemClassBasePEOItemCreationAllowedFlag | ITEM_CREATION_ALLOWED_FLAG | — | — |
| 28 | ItemClassBasePEOItemDescGenMethod | ITEM_DESC_GEN_METHOD | — | — |
| 29 | ItemClassBasePEOItemNumGenMethod | ITEM_NUM_GEN_METHOD | — | — |
| 30 | ItemClassBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 31 | ItemClassBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 32 | ItemClassBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | ItemClassBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | ItemClassBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 35 | ItemClassBasePEONirChangeTypeId | NIR_CHANGE_TYPE_ID | — | — |
| 36 | ItemClassBasePEONirReqd | NIR_REQD | — | — |
| 37 | ItemClassBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | ItemClassBasePEOParentItemClassId | PARENT_ITEM_CLASS_ID | — | — |
| 39 | ItemClassBasePEORequestId | REQUEST_ID | — | — |
| 40 | ItemClassBasePEOVersionEnabledFlag | VERSION_ENABLED_FLAG | — | — |

### [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemClassTranPEOCreatedBy | CREATED_BY | — | — |
| 2 | ItemClassTranPEOCreationDate | CREATION_DATE | — | — |
| 3 | ItemClassTranPEODescription | DESCRIPTION | — | — |
| 4 | ItemClassTranPEOItemClassId | ITEM_CLASS_ID | — | — |
| 5 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | — |
| 6 | ItemClassTranPEOLanguage | LANGUAGE | — | — |
| 7 | ItemClassTranPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemClassTranPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ItemClassTranPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ItemClassTranPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ItemClassTranPEOSourceLang | SOURCE_LANG | — | — |

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
| 2 | InventoryItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | — |
| 3 | InventoryItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 4 | InventoryItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 5 | InventoryItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 6 | InventoryItemBasePEOAcdType | ACD_TYPE | — | — |
| 7 | InventoryItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | — |
| 8 | InventoryItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | — |
| 9 | InventoryItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 10 | InventoryItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 11 | InventoryItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | — |
| 12 | InventoryItemBasePEOApprovalStatus | APPROVAL_STATUS | — | — |
| 13 | InventoryItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | — |
| 14 | InventoryItemBasePEOAssetCreationCode | ASSET_CREATION_CODE | — | — |
| 15 | InventoryItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | — |
| 16 | InventoryItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | — |
| 17 | InventoryItemBasePEOAtpFlag | ATP_FLAG | — | — |
| 18 | InventoryItemBasePEOAtpRuleId | ATP_RULE_ID | — | — |
| 19 | InventoryItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | — |
| 20 | InventoryItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 21 | InventoryItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 22 | InventoryItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 23 | InventoryItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | — |
| 24 | InventoryItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | — |
| 25 | InventoryItemBasePEOBaseItemId | BASE_ITEM_ID | — | — |
| 26 | InventoryItemBasePEOBomItemType | BOM_ITEM_TYPE | — | — |
| 27 | InventoryItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | — |
| 28 | InventoryItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | — |
| 29 | InventoryItemBasePEOBuyerId | BUYER_ID | — | ✅ |
| 30 | InventoryItemBasePEOCarryingCost | CARRYING_COST | — | — |
| 31 | InventoryItemBasePEOCasNumber | CAS_NUMBER | — | — |
| 32 | InventoryItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 33 | InventoryItemBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 34 | InventoryItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | — |
| 35 | InventoryItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | — |
| 36 | InventoryItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | — |
| 37 | InventoryItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | — |
| 38 | InventoryItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | — |
| 39 | InventoryItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 40 | InventoryItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | — |
| 41 | InventoryItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | — |
| 42 | InventoryItemBasePEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 43 | InventoryItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | — |
| 44 | InventoryItemBasePEOConfigMatch | CONFIG_MATCH | — | — |
| 45 | InventoryItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | — |
| 46 | InventoryItemBasePEOConfigOrgs | CONFIG_ORGS | — | — |
| 47 | InventoryItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | — |
| 48 | InventoryItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | — |
| 49 | InventoryItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | — |
| 50 | InventoryItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 51 | InventoryItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | — |
| 52 | InventoryItemBasePEOConvergence | CONVERGENCE | — | — |
| 53 | InventoryItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 54 | InventoryItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | — |
| 55 | InventoryItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | — |
| 56 | InventoryItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | — |
| 57 | InventoryItemBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 58 | InventoryItemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 59 | InventoryItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 60 | InventoryItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | ✅ |
| 61 | InventoryItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | ✅ |
| 62 | InventoryItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 63 | InventoryItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 64 | InventoryItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | — |
| 65 | InventoryItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | — |
| 66 | InventoryItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | — |
| 67 | InventoryItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 68 | InventoryItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 69 | InventoryItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 70 | InventoryItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 71 | InventoryItemBasePEODaysOfCover | DAYS_OF_COVER | — | — |
| 72 | InventoryItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 73 | InventoryItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 74 | InventoryItemBasePEODefaultGrade | DEFAULT_GRADE | — | — |
| 75 | InventoryItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | — |
| 76 | InventoryItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 77 | InventoryItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 78 | InventoryItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | — |
| 79 | InventoryItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | — |
| 80 | InventoryItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 81 | InventoryItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | — |
| 82 | InventoryItemBasePEODemandPeriod | DEMAND_PERIOD | — | — |
| 83 | InventoryItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | — |
| 84 | InventoryItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | — |
| 85 | InventoryItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 86 | InventoryItemBasePEODivergence | DIVERGENCE | — | — |
| 87 | InventoryItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | — |
| 88 | InventoryItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 89 | InventoryItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | — |
| 90 | InventoryItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | — |
| 91 | InventoryItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | — |
| 92 | InventoryItemBasePEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | — |
| 93 | InventoryItemBasePEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | — |
| 94 | InventoryItemBasePEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | — |
| 95 | InventoryItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | — |
| 96 | InventoryItemBasePEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | — |
| 97 | InventoryItemBasePEOEamItemType | EAM_ITEM_TYPE | — | — |
| 98 | InventoryItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | — |
| 99 | InventoryItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | — |
| 100 | InventoryItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | — |
| 101 | InventoryItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | — |
| 102 | InventoryItemBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 103 | InventoryItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 104 | InventoryItemBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 105 | InventoryItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 106 | InventoryItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 107 | InventoryItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | — |
| 108 | InventoryItemBasePEOEventFlag | EVENT_FLAG | — | — |
| 109 | InventoryItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 110 | InventoryItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 111 | InventoryItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 112 | InventoryItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 113 | InventoryItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | — |
| 114 | InventoryItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | — |
| 115 | InventoryItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | — |
| 116 | InventoryItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 117 | InventoryItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | — |
| 118 | InventoryItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | — |
| 119 | InventoryItemBasePEOForecastHorizon | FORECAST_HORIZON | — | — |
| 120 | InventoryItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 121 | InventoryItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 122 | InventoryItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | — |
| 123 | InventoryItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | — |
| 124 | InventoryItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | — |
| 125 | InventoryItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | — |
| 126 | InventoryItemBasePEOHoldDays | HOLD_DAYS | — | — |
| 127 | InventoryItemBasePEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | — |
| 128 | InventoryItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 129 | InventoryItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | — |
| 130 | InventoryItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 131 | InventoryItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | — |
| 132 | InventoryItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | — |
| 133 | InventoryItemBasePEOInternalVolume | INTERNAL_VOLUME | — | — |
| 134 | InventoryItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | — |
| 135 | InventoryItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | — |
| 136 | InventoryItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | — |
| 137 | InventoryItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | ✅ |
| 138 | InventoryItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 139 | InventoryItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | — |
| 140 | InventoryItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | — |
| 141 | InventoryItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 142 | InventoryItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | — |
| 143 | InventoryItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 144 | InventoryItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 145 | InventoryItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 146 | InventoryItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 147 | InventoryItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | — |
| 148 | InventoryItemBasePEOItemType | ITEM_TYPE | — | ✅ |
| 149 | InventoryItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 150 | InventoryItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 151 | InventoryItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 152 | InventoryItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 153 | InventoryItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 154 | InventoryItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 155 | InventoryItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | — |
| 156 | InventoryItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | — |
| 157 | InventoryItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | — |
| 158 | InventoryItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | — |
| 159 | InventoryItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | — |
| 160 | InventoryItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | — |
| 161 | InventoryItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | — |
| 162 | InventoryItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | — |
| 163 | InventoryItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | — |
| 164 | InventoryItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | — |
| 165 | InventoryItemBasePEOMarketPrice | MARKET_PRICE | — | — |
| 166 | InventoryItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | — |
| 167 | InventoryItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | — |
| 168 | InventoryItemBasePEOMaturityDays | MATURITY_DAYS | — | — |
| 169 | InventoryItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | — |
| 170 | InventoryItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | — |
| 171 | InventoryItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 172 | InventoryItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | — |
| 173 | InventoryItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | — |
| 174 | InventoryItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | — |
| 175 | InventoryItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 176 | InventoryItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | — |
| 177 | InventoryItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 178 | InventoryItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 179 | InventoryItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 180 | InventoryItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | — |
| 181 | InventoryItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | — |
| 182 | InventoryItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | — |
| 183 | InventoryItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | — |
| 184 | InventoryItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 185 | InventoryItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | — |
| 186 | InventoryItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | — |
| 187 | InventoryItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 188 | InventoryItemBasePEOOrderCost | ORDER_COST | — | — |
| 189 | InventoryItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | — |
| 190 | InventoryItemBasePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | — |
| 191 | InventoryItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | — |
| 192 | InventoryItemBasePEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | — |
| 193 | InventoryItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | — |
| 194 | InventoryItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | — |
| 195 | InventoryItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | — |
| 196 | InventoryItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | — |
| 197 | InventoryItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 198 | InventoryItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 199 | InventoryItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 200 | InventoryItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | — |
| 201 | InventoryItemBasePEOPickingRuleId | PICKING_RULE_ID | — | — |
| 202 | InventoryItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 203 | InventoryItemBasePEOPlannerCode | PLANNER_CODE | — | ✅ |
| 204 | InventoryItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 205 | InventoryItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 206 | InventoryItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | — |
| 207 | InventoryItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | ✅ |
| 208 | InventoryItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | — |
| 209 | InventoryItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 210 | InventoryItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 211 | InventoryItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 212 | InventoryItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | — |
| 213 | InventoryItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 214 | InventoryItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | — |
| 215 | InventoryItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | — |
| 216 | InventoryItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | ✅ |
| 217 | InventoryItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 218 | InventoryItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | — |
| 219 | InventoryItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | — |
| 220 | InventoryItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | — |
| 221 | InventoryItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 222 | InventoryItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 223 | InventoryItemBasePEOProgramName | PROGRAM_NAME | — | — |
| 224 | InventoryItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | — |
| 225 | InventoryItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | — |
| 226 | InventoryItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | — |
| 227 | InventoryItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 228 | InventoryItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 229 | InventoryItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 230 | InventoryItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 231 | InventoryItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 232 | InventoryItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | — |
| 233 | InventoryItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 234 | InventoryItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | — |
| 235 | InventoryItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | — |
| 236 | InventoryItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | — |
| 237 | InventoryItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | — |
| 238 | InventoryItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 239 | InventoryItemBasePEORepairProgram | REPAIR_PROGRAM | — | — |
| 240 | InventoryItemBasePEORepairYield | REPAIR_YIELD | — | — |
| 241 | InventoryItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 242 | InventoryItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | — |
| 243 | InventoryItemBasePEORequestId | REQUEST_ID | — | — |
| 244 | InventoryItemBasePEOReservableType | RESERVABLE_TYPE | — | — |
| 245 | InventoryItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | — |
| 246 | InventoryItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | — |
| 247 | InventoryItemBasePEORetestInterval | RETEST_INTERVAL | — | — |
| 248 | InventoryItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | — |
| 249 | InventoryItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | — |
| 250 | InventoryItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | — |
| 251 | InventoryItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | — |
| 252 | InventoryItemBasePEORoundingFactor | ROUNDING_FACTOR | — | — |
| 253 | InventoryItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 254 | InventoryItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | — |
| 255 | InventoryItemBasePEOSalesAccount | SALES_ACCOUNT | — | — |
| 256 | InventoryItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | — |
| 257 | InventoryItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | — |
| 258 | InventoryItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 259 | InventoryItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | — |
| 260 | InventoryItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | — |
| 261 | InventoryItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | — |
| 262 | InventoryItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | — |
| 263 | InventoryItemBasePEOServiceDuration | SERVICE_DURATION | — | — |
| 264 | InventoryItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 265 | InventoryItemBasePEOServiceStartingDelay | SERVICE_START_DELAY | — | — |
| 266 | InventoryItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | — |
| 267 | InventoryItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | — |
| 268 | InventoryItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | ✅ |
| 269 | InventoryItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | — |
| 270 | InventoryItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | — |
| 271 | InventoryItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | — |
| 272 | InventoryItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | — |
| 273 | InventoryItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | — |
| 274 | InventoryItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 275 | InventoryItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 276 | InventoryItemBasePEOSourceType | SOURCE_TYPE | — | — |
| 277 | InventoryItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | — |
| 278 | InventoryItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 279 | InventoryItemBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 280 | InventoryItemBasePEOStdLotSize | STD_LOT_SIZE | — | ✅ |
| 281 | InventoryItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | — |
| 282 | InventoryItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | — |
| 283 | InventoryItemBasePEOStyleItemId | STYLE_ITEM_ID | — | — |
| 284 | InventoryItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | — |
| 285 | InventoryItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 286 | InventoryItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 287 | InventoryItemBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 288 | InventoryItemBasePEOTaxCode | TAX_CODE | — | — |
| 289 | InventoryItemBasePEOTaxableFlag | TAXABLE_FLAG | — | — |
| 290 | InventoryItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 291 | InventoryItemBasePEOTemplateName | ITEM_NUMBER | — | — |
| 292 | InventoryItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | — |
| 293 | InventoryItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | — |
| 294 | InventoryItemBasePEOUnNumberId | UN_NUMBER_ID | — | — |
| 295 | InventoryItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | — |
| 296 | InventoryItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | — |
| 297 | InventoryItemBasePEOUnitHeight | UNIT_HEIGHT | — | — |
| 298 | InventoryItemBasePEOUnitLength | UNIT_LENGTH | — | — |
| 299 | InventoryItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | ✅ |
| 300 | InventoryItemBasePEOUnitVolume | UNIT_VOLUME | — | — |
| 301 | InventoryItemBasePEOUnitWeight | UNIT_WEIGHT | — | — |
| 302 | InventoryItemBasePEOUnitWidth | UNIT_WIDTH | — | — |
| 303 | InventoryItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 304 | InventoryItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | — |
| 305 | InventoryItemBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 306 | InventoryItemBasePEOVersionId | VERSION_ID | — | — |
| 307 | InventoryItemBasePEOVersionStartDate | VERSION_START_DATE | — | — |
| 308 | InventoryItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | — |
| 309 | InventoryItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | — |
| 310 | InventoryItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | — |
| 311 | InventoryItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | — |
| 312 | InventoryItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | — |
| 313 | InventoryItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | — |
| 314 | InventoryItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 315 | InventoryItemBasePEOWebStatus | WEB_STATUS | — | — |
| 316 | InventoryItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | — |
| 317 | InventoryItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 318 | InventoryItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | — |
| 319 | InventoryItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | — |
| 320 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 321 | ItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | — |
| 322 | ItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | — |
| 323 | ItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | — |
| 324 | ItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | — |
| 325 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | — |
| 326 | ItemBasePEOPackagingStringId | PACKAGING_STRING_ID | — | — |
| 327 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | — |
| 328 | ItemBasePEORepairTransactionCode | REPAIR_TRANSACTION_CODE | — | — |
| 329 | ItemBasePEOUnderCompletionToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | — |
| 330 | ItemBasePEOUnderCompletionToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | — |
| 331 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 332 | ReplacementType | REPLACEMENT_TYPE | — | — |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InventoryItemTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InventoryItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | InventoryItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 5 | InventoryItemTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InventoryItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InventoryItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InventoryItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InventoryItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 10 | InventoryItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InventoryItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | InventoryItemTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

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
| 1 | ItemOrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | — |
| 2 | ItemOrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | — |
| 3 | ItemOrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | — |
| 4 | ItemOrganizationParameterPEOAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | — |
| 5 | ItemOrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | — |
| 6 | ItemOrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 7 | ItemOrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 8 | ItemOrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 9 | ItemOrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | — |
| 10 | ItemOrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | — |
| 11 | ItemOrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 12 | ItemOrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | — |
| 13 | ItemOrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 14 | ItemOrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | — |
| 15 | ItemOrganizationParameterPEOCreatedBy | CREATED_BY | — | — |
| 16 | ItemOrganizationParameterPEOCreationDate | CREATION_DATE | — | — |
| 17 | ItemOrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | — |
| 18 | ItemOrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | — |
| 19 | ItemOrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | — |
| 20 | ItemOrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 21 | ItemOrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | — |
| 22 | ItemOrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | — |
| 23 | ItemOrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | — |
| 24 | ItemOrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | — |
| 25 | ItemOrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 26 | ItemOrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | ItemOrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ItemOrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | ItemOrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | ItemOrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 31 | ItemOrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | — |
| 32 | ItemOrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | — |
| 33 | ItemOrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | — |
| 34 | ItemOrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | — |
| 35 | ItemOrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | — |
| 36 | ItemOrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | — |
| 37 | ItemOrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | — |
| 38 | ItemOrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 39 | ItemOrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | — |
| 40 | ItemOrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | — |
| 41 | ItemOrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | ItemOrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 43 | ItemOrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |
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
| 54 | ItemOrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 55 | ItemOrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 56 | ItemOrganizationParameterPEOSourceType | SOURCE_TYPE | — | — |
| 57 | ItemOrganizationParameterPEOStandardPackEnabled | STANDARD_PACK_ENABLED | — | — |
| 58 | ItemOrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 59 | ItemOrganizationParameterPEOStartingRevision | STARTING_REVISION | — | — |
| 60 | ItemOrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | — |
| 61 | ItemOrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | — |
| 62 | ItemOrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | — |

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
