---
id: DOC-OTHER-PVO-InventoryItemRef
doc_type: system-doc
title: "InventoryItemRef — PVO Cross-Module"
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
  - InventoryItemRef
  - inventoryitemref
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryItemRef

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Item Ref. Acessa as tabelas: EGP_ITEM_CLASSES_B_V, EGP_ITEM_CLASSES_TL, EGP_ITEM_REVISIONS_B_V (+18).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.InventoryItemRef`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 576 | 21 | 2 | 315 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_classes_b_v|EGP_ITEM_CLASSES_B_V]] — 40 atributos (1 BICC)
- [[egp_item_classes_tl|EGP_ITEM_CLASSES_TL]] — 11 atributos (3 BICC)
- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 4 atributos
- [[egp_item_status_vl|EGP_ITEM_STATUS_VL]] — 2 atributos (1 BICC)
- [[egp_phases_vl|EGP_PHASES_VL]] — 4 atributos (4 BICC)
- [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]] — 1 atributos (1 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 349 atributos (2 PKs, 265 BICC)
- [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]] — 13 atributos (6 BICC)
- [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]] — 14 atributos (6 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (3 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 17 atributos (8 BICC)
- [[inv_actions_vl|INV_ACTIONS_VL]] — 3 atributos (1 BICC)
- [[inv_material_statuses_vl|INV_MATERIAL_STATUSES_VL]] — 6 atributos (4 BICC)
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 62 atributos (3 BICC)
- [[inv_rules_vl|INV_RULES_VL]] — 2 atributos (1 BICC)
- [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]] — 12 atributos
- [[msc_planners_with_pimid_v|MSC_PLANNERS_WITH_PIMID_V]] — 5 atributos (5 BICC)
- [[okc_coverage_headers_vl|OKC_COVERAGE_HEADERS_VL]] — 3 atributos
- [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]] — 2 atributos
- [[ra_rules|RA_RULES]] — 6 atributos (2 BICC)
- [[ra_terms_vl|RA_TERMS_VL]] — 2 atributos (1 BICC)

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
| 5 | ItemClassTranPEOItemClassName | ITEM_CLASS_NAME | — | ✅ |
| 6 | ItemClassTranPEOLanguage | LANGUAGE | — | ✅ |
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
| 2 | ItemStatusPEOInventoryItemStatusName | INVENTORY_ITEM_STATUS_NAME | — | ✅ |

### [[egp_phases_vl|EGP_PHASES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PhasesPEOPhaseCode | PHASE_CODE | — | ✅ |
| 2 | PhasesPEOPhaseName | PHASE_NAME | — | ✅ |
| 3 | PhasesPEOPhaseType | PHASE_TYPE | — | ✅ |
| 4 | PhasesPEOStartDate | START_DATE | — | ✅ |

### [[egp_system_items_b|EGP_SYSTEM_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemBasePEOAssetCategoryId | ASSET_CATEGORY_ID | — | ✅ |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForcePurchaseLeadTimeFlag | FORCE_PURCHASE_LEAD_TIME_FLAG | — | ✅ |
| 2 | InventoryItemBasePEOAcceptableEarlyDays | ACCEPTABLE_EARLY_DAYS | — | ✅ |
| 3 | InventoryItemBasePEOAcceptableRateDecrease | ACCEPTABLE_RATE_DECREASE | — | — |
| 4 | InventoryItemBasePEOAcceptableRateIncrease | ACCEPTABLE_RATE_INCREASE | — | — |
| 5 | InventoryItemBasePEOAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 6 | InventoryItemBasePEOAcdType | ACD_TYPE | — | ✅ |
| 7 | InventoryItemBasePEOAllowExpressDeliveryFlag | ALLOW_EXPRESS_DELIVERY_FLAG | — | ✅ |
| 8 | InventoryItemBasePEOAllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | ✅ |
| 9 | InventoryItemBasePEOAllowMaintenanceAssetFlag | ALLOW_MAINTENANCE_ASSET_FLAG | — | ✅ |
| 10 | InventoryItemBasePEOAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 11 | InventoryItemBasePEOAllowSuspendFlag | ALLOW_SUSPEND_FLAG | — | ✅ |
| 12 | InventoryItemBasePEOAllowTerminateFlag | ALLOW_TERMINATE_FLAG | — | ✅ |
| 13 | InventoryItemBasePEOAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 14 | InventoryItemBasePEOAllowedUnitsLookupCode | ALLOWED_UNITS_LOOKUP_CODE | — | ✅ |
| 15 | InventoryItemBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 16 | InventoryItemBasePEOAsnAutoexpireFlag | ASN_AUTOEXPIRE_FLAG | — | ✅ |
| 17 | InventoryItemBasePEOAssetClass | ASSET_CLASS | — | ✅ |
| 18 | InventoryItemBasePEOAssetCreationCode | ASSET_CREATION_CODE | — | ✅ |
| 19 | InventoryItemBasePEOAssetTrackedFlag | ASSET_TRACKED_FLAG | — | ✅ |
| 20 | InventoryItemBasePEOAtoForecastControl | ATO_FORECAST_CONTROL | — | ✅ |
| 21 | InventoryItemBasePEOAtpComponentsFlag | ATP_COMPONENTS_FLAG | — | ✅ |
| 22 | InventoryItemBasePEOAtpFlag | ATP_FLAG | — | ✅ |
| 23 | InventoryItemBasePEOAtpRuleId | ATP_RULE_ID | — | — |
| 24 | InventoryItemBasePEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 25 | InventoryItemBasePEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | ✅ |
| 26 | InventoryItemBasePEOAutoReduceMps | AUTO_REDUCE_MPS | — | — |
| 27 | InventoryItemBasePEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | ✅ |
| 28 | InventoryItemBasePEOBackOrderableFlag | BACK_ORDERABLE_FLAG | — | ✅ |
| 29 | InventoryItemBasePEOBackToBackEnabled | BACK_TO_BACK_ENABLED | — | ✅ |
| 30 | InventoryItemBasePEOBaseItemId | BASE_ITEM_ID | — | ✅ |
| 31 | InventoryItemBasePEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 32 | InventoryItemBasePEOBuildInWipFlag | BUILD_IN_WIP_FLAG | — | ✅ |
| 33 | InventoryItemBasePEOBulkPickedFlag | BULK_PICKED_FLAG | — | ✅ |
| 34 | InventoryItemBasePEOBuyerId | BUYER_ID | — | — |
| 35 | InventoryItemBasePEOCarryingCost | CARRYING_COST | — | ✅ |
| 36 | InventoryItemBasePEOCasNumber | CAS_NUMBER | — | ✅ |
| 37 | InventoryItemBasePEOChangeBitMap | CHANGE_BIT_MAP | — | — |
| 38 | InventoryItemBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 39 | InventoryItemBasePEOChargePeriodicityCode | CHARGE_PERIODICITY_CODE | — | ✅ |
| 40 | InventoryItemBasePEOCheckShortagesFlag | CHECK_SHORTAGES_FLAG | — | ✅ |
| 41 | InventoryItemBasePEOChildLotFlag | CHILD_LOT_FLAG | — | ✅ |
| 42 | InventoryItemBasePEOChildLotPrefix | CHILD_LOT_PREFIX | — | ✅ |
| 43 | InventoryItemBasePEOChildLotStartingNumber | CHILD_LOT_STARTING_NUMBER | — | ✅ |
| 44 | InventoryItemBasePEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | ✅ |
| 45 | InventoryItemBasePEOCollateralFlag | COLLATERAL_FLAG | — | ✅ |
| 46 | InventoryItemBasePEOCommsActivationReqdFlag | COMMS_ACTIVATION_REQD_FLAG | — | ✅ |
| 47 | InventoryItemBasePEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | ✅ |
| 48 | InventoryItemBasePEOComnSupplyPrjDemandFlag | COMN_SUPPLY_PRJ_DEMAND_FLAG | — | ✅ |
| 49 | InventoryItemBasePEOCompletenessScore | COMPLETENESS_SCORE | — | ✅ |
| 50 | InventoryItemBasePEOConfigMatch | CONFIG_MATCH | — | ✅ |
| 51 | InventoryItemBasePEOConfigModelType | CONFIG_MODEL_TYPE | — | ✅ |
| 52 | InventoryItemBasePEOConfigOrgs | CONFIG_ORGS | — | ✅ |
| 53 | InventoryItemBasePEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 54 | InventoryItemBasePEOContainerItemFlag | CONTAINER_ITEM_FLAG | — | ✅ |
| 55 | InventoryItemBasePEOContainerTypeCode | CONTAINER_TYPE_CODE | — | ✅ |
| 56 | InventoryItemBasePEOContinousTransfer | CONTINOUS_TRANSFER | — | — |
| 57 | InventoryItemBasePEOContractManufacturing | CONTRACT_MANUFACTURING | — | ✅ |
| 58 | InventoryItemBasePEOConvergence | CONVERGENCE | — | — |
| 59 | InventoryItemBasePEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | ✅ |
| 60 | InventoryItemBasePEOCostingEnabledFlag | COSTING_ENABLED_FLAG | — | ✅ |
| 61 | InventoryItemBasePEOCoverageScheduleId | COVERAGE_SCHEDULE_ID | — | ✅ |
| 62 | InventoryItemBasePEOCreateFixedAsset | CREATE_FIXED_ASSET | — | — |
| 63 | InventoryItemBasePEOCreateSupplyAfterDate | CREATE_SUPPLY_AFTER_DATE | — | ✅ |
| 64 | InventoryItemBasePEOCreateSupplyFlag | CREATE_SUPPLY_FLAG | — | ✅ |
| 65 | InventoryItemBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 66 | InventoryItemBasePEOCreatedFromItemId | CREATED_FROM_ITEM_ID | — | — |
| 67 | InventoryItemBasePEOCreatedFromRevisionId | CREATED_FROM_REVISION_ID | — | — |
| 68 | InventoryItemBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 69 | InventoryItemBasePEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | — |
| 70 | InventoryItemBasePEOCssEnabledFlag | CSS_ENABLED_FLAG | — | ✅ |
| 71 | InventoryItemBasePEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | ✅ |
| 72 | InventoryItemBasePEOCumulativeTotalLeadTime | CUMULATIVE_TOTAL_LEAD_TIME | — | ✅ |
| 73 | InventoryItemBasePEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | ✅ |
| 74 | InventoryItemBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 75 | InventoryItemBasePEOCustomerOrderEnabledFlag | CUSTOMER_ORDER_ENABLED_FLAG | — | ✅ |
| 76 | InventoryItemBasePEOCustomerOrderFlag | CUSTOMER_ORDER_FLAG | — | ✅ |
| 77 | InventoryItemBasePEOCycleCountEnabledFlag | CYCLE_COUNT_ENABLED_FLAG | — | ✅ |
| 78 | InventoryItemBasePEODaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 79 | InventoryItemBasePEODaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 80 | InventoryItemBasePEODaysMaxInvSupply | DAYS_MAX_INV_SUPPLY | — | — |
| 81 | InventoryItemBasePEODaysMaxInvWindow | DAYS_MAX_INV_WINDOW | — | — |
| 82 | InventoryItemBasePEODaysOfCover | DAYS_OF_COVER | — | ✅ |
| 83 | InventoryItemBasePEODaysTgtInvSupply | DAYS_TGT_INV_SUPPLY | — | — |
| 84 | InventoryItemBasePEODaysTgtInvWindow | DAYS_TGT_INV_WINDOW | — | — |
| 85 | InventoryItemBasePEODefaultGrade | DEFAULT_GRADE | — | ✅ |
| 86 | InventoryItemBasePEODefaultIncludeInRollupFlag | DEFAULT_INCLUDE_IN_ROLLUP_FLAG | — | ✅ |
| 87 | InventoryItemBasePEODefaultLotStatusId | DEFAULT_LOT_STATUS_ID | — | — |
| 88 | InventoryItemBasePEODefaultSerialStatusId | DEFAULT_SERIAL_STATUS_ID | — | — |
| 89 | InventoryItemBasePEODefaultShippingOrg | DEFAULT_SHIPPING_ORG | — | ✅ |
| 90 | InventoryItemBasePEODefaultSoSourceType | DEFAULT_SO_SOURCE_TYPE | — | ✅ |
| 91 | InventoryItemBasePEODefaultTemplateFlag | DEFAULT_TEMPLATE_FLAG | — | — |
| 92 | InventoryItemBasePEODefectTrackingOnFlag | DEFECT_TRACKING_ON_FLAG | — | ✅ |
| 93 | InventoryItemBasePEODemandPeriod | DEMAND_PERIOD | — | ✅ |
| 94 | InventoryItemBasePEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | ✅ |
| 95 | InventoryItemBasePEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | ✅ |
| 96 | InventoryItemBasePEODimensionUomCode | DIMENSION_UOM_CODE | — | ✅ |
| 97 | InventoryItemBasePEODivergence | DIVERGENCE | — | — |
| 98 | InventoryItemBasePEODownloadableFlag | DOWNLOADABLE_FLAG | — | ✅ |
| 99 | InventoryItemBasePEODrpPlannedFlag | DRP_PLANNED_FLAG | — | — |
| 100 | InventoryItemBasePEODualUomControl | DUAL_UOM_CONTROL | — | ✅ |
| 101 | InventoryItemBasePEODualUomDeviationHigh | DUAL_UOM_DEVIATION_HIGH | — | ✅ |
| 102 | InventoryItemBasePEODualUomDeviationLow | DUAL_UOM_DEVIATION_LOW | — | ✅ |
| 103 | InventoryItemBasePEOEamActNotificationFlag | EAM_ACT_NOTIFICATION_FLAG | — | ✅ |
| 104 | InventoryItemBasePEOEamActShutdownStatus | EAM_ACT_SHUTDOWN_STATUS | — | ✅ |
| 105 | InventoryItemBasePEOEamActivityCauseCode | EAM_ACTIVITY_CAUSE_CODE | — | ✅ |
| 106 | InventoryItemBasePEOEamActivitySourceCode | EAM_ACTIVITY_SOURCE_CODE | — | ✅ |
| 107 | InventoryItemBasePEOEamActivityTypeCode | EAM_ACTIVITY_TYPE_CODE | — | ✅ |
| 108 | InventoryItemBasePEOEamItemType | EAM_ITEM_TYPE | — | ✅ |
| 109 | InventoryItemBasePEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 110 | InventoryItemBasePEOElectronicFlag | ELECTRONIC_FLAG | — | ✅ |
| 111 | InventoryItemBasePEOEligibilityCompatibilityRule | ELIGIBILITY_COMPATIBILITY_RULE | — | ✅ |
| 112 | InventoryItemBasePEOEnableGenealogyTrackingFlag | ENABLE_GENEALOGY_TRACKING_FLAG | — | ✅ |
| 113 | InventoryItemBasePEOEnableIotFlag | ENABLE_IOT_FLAG | — | ✅ |
| 114 | InventoryItemBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 115 | InventoryItemBasePEOEndAssemblyPeggingFlag | END_ASSEMBLY_PEGGING_FLAG | — | — |
| 116 | InventoryItemBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 117 | InventoryItemBasePEOEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 118 | InventoryItemBasePEOEngineeredItemFlag | ENGINEERED_ITEM_FLAG | — | ✅ |
| 119 | InventoryItemBasePEOEngineeringItemId | ENGINEERING_ITEM_ID | — | — |
| 120 | InventoryItemBasePEOEquipmentType | EQUIPMENT_TYPE | — | ✅ |
| 121 | InventoryItemBasePEOEventFlag | EVENT_FLAG | — | ✅ |
| 122 | InventoryItemBasePEOExcludeFromBudgetFlag | EXCLUDE_FROM_BUDGET_FLAG | — | — |
| 123 | InventoryItemBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 124 | InventoryItemBasePEOExpenseAccount | EXPENSE_ACCOUNT | — | — |
| 125 | InventoryItemBasePEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 126 | InventoryItemBasePEOExpirationActionInterval | EXPIRATION_ACTION_INTERVAL | — | ✅ |
| 127 | InventoryItemBasePEOFinancingAllowedFlag | FINANCING_ALLOWED_FLAG | — | ✅ |
| 128 | InventoryItemBasePEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | ✅ |
| 129 | InventoryItemBasePEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 130 | InventoryItemBasePEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | ✅ |
| 131 | InventoryItemBasePEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | ✅ |
| 132 | InventoryItemBasePEOForecastHorizon | FORECAST_HORIZON | — | ✅ |
| 133 | InventoryItemBasePEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 134 | InventoryItemBasePEOGdsnOutboundEnabledFlag | GDSN_OUTBOUND_ENABLED_FLAG | — | — |
| 135 | InventoryItemBasePEOGradeControlFlag | GRADE_CONTROL_FLAG | — | ✅ |
| 136 | InventoryItemBasePEOHardPeggingLevel | HARD_PEGGING_LEVEL | — | ✅ |
| 137 | InventoryItemBasePEOHazardClassId | HAZARD_CLASS_ID | — | ✅ |
| 138 | InventoryItemBasePEOHazardousMaterialFlag | HAZARDOUS_MATERIAL_FLAG | — | ✅ |
| 139 | InventoryItemBasePEOHoldDays | HOLD_DAYS | — | ✅ |
| 140 | InventoryItemBasePEOIbItemInstanceClass | IB_ITEM_INSTANCE_CLASS | — | ✅ |
| 141 | InventoryItemBasePEOImplementationDate | IMPLEMENTATION_DATE | — | — |
| 142 | InventoryItemBasePEOIndivisibleFlag | INDIVISIBLE_FLAG | — | ✅ |
| 143 | InventoryItemBasePEOInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 144 | InventoryItemBasePEOInternalOrderEnabledFlag | INTERNAL_ORDER_ENABLED_FLAG | — | ✅ |
| 145 | InventoryItemBasePEOInternalOrderFlag | INTERNAL_ORDER_FLAG | — | ✅ |
| 146 | InventoryItemBasePEOInternalVolume | INTERNAL_VOLUME | — | ✅ |
| 147 | InventoryItemBasePEOInventoryAssetFlag | INVENTORY_ASSET_FLAG | — | ✅ |
| 148 | InventoryItemBasePEOInventoryCarryPenalty | INVENTORY_CARRY_PENALTY | — | ✅ |
| 149 | InventoryItemBasePEOInventoryItemFlag | INVENTORY_ITEM_FLAG | — | ✅ |
| 150 | InventoryItemBasePEOInventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | — | — |
| 151 | InventoryItemBasePEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 152 | InventoryItemBasePEOInventoryPlanningCode | INVENTORY_PLANNING_CODE | — | ✅ |
| 153 | InventoryItemBasePEOInvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 154 | InventoryItemBasePEOInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 155 | InventoryItemBasePEOInvoiceMatchOption | INVOICE_MATCH_OPTION | — | ✅ |
| 156 | InventoryItemBasePEOInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 157 | InventoryItemBasePEOInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 158 | InventoryItemBasePEOItemCatalogGroupId | ITEM_CATALOG_GROUP_ID | — | — |
| 159 | InventoryItemBasePEOItemDefinitionOrgId | ITEM_DEFINITION_ORG_ID | — | — |
| 160 | InventoryItemBasePEOItemNumber | ITEM_NUMBER | — | ✅ |
| 161 | InventoryItemBasePEOItemObjectType | ITEM_OBJECT_TYPE | — | — |
| 162 | InventoryItemBasePEOItemType | ITEM_TYPE | — | ✅ |
| 163 | InventoryItemBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 164 | InventoryItemBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 165 | InventoryItemBasePEOLastSubmittedNirId | LAST_SUBMITTED_NIR_ID | — | — |
| 166 | InventoryItemBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 167 | InventoryItemBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 168 | InventoryItemBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 169 | InventoryItemBasePEOLeadTimeLotSize | LEAD_TIME_LOT_SIZE | — | ✅ |
| 170 | InventoryItemBasePEOListPricePerUnit | LIST_PRICE_PER_UNIT | — | ✅ |
| 171 | InventoryItemBasePEOLocationControlCode | LOCATION_CONTROL_CODE | — | ✅ |
| 172 | InventoryItemBasePEOLotControlCode | LOT_CONTROL_CODE | — | ✅ |
| 173 | InventoryItemBasePEOLotDivisibleFlag | LOT_DIVISIBLE_FLAG | — | ✅ |
| 174 | InventoryItemBasePEOLotMergeEnabled | LOT_MERGE_ENABLED | — | ✅ |
| 175 | InventoryItemBasePEOLotSplitEnabled | LOT_SPLIT_ENABLED | — | ✅ |
| 176 | InventoryItemBasePEOLotStatusEnabled | LOT_STATUS_ENABLED | — | ✅ |
| 177 | InventoryItemBasePEOLotSubstitutionEnabled | LOT_SUBSTITUTION_ENABLED | — | ✅ |
| 178 | InventoryItemBasePEOLotTranslateEnabled | LOT_TRANSLATE_ENABLED | — | ✅ |
| 179 | InventoryItemBasePEOMarketPrice | MARKET_PRICE | — | ✅ |
| 180 | InventoryItemBasePEOMatchApprovalLevel | MATCH_APPROVAL_LEVEL | — | ✅ |
| 181 | InventoryItemBasePEOMaterialBillableFlag | MATERIAL_BILLABLE_FLAG | — | ✅ |
| 182 | InventoryItemBasePEOMaturityDays | MATURITY_DAYS | — | ✅ |
| 183 | InventoryItemBasePEOMaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | ✅ |
| 184 | InventoryItemBasePEOMaximumLoadWeight | MAXIMUM_LOAD_WEIGHT | — | ✅ |
| 185 | InventoryItemBasePEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 186 | InventoryItemBasePEOMinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | ✅ |
| 187 | InventoryItemBasePEOMinimumFillPercent | MINIMUM_FILL_PERCENT | — | ✅ |
| 188 | InventoryItemBasePEOMinimumLicenseQuantity | MINIMUM_LICENSE_QUANTITY | — | ✅ |
| 189 | InventoryItemBasePEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 190 | InventoryItemBasePEOMrpCalculateAtpFlag | MRP_CALCULATE_ATP_FLAG | — | ✅ |
| 191 | InventoryItemBasePEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 192 | InventoryItemBasePEOMrpSafetyStockCode | MRP_SAFETY_STOCK_CODE | — | — |
| 193 | InventoryItemBasePEOMrpSafetyStockPercent | MRP_SAFETY_STOCK_PERCENT | — | — |
| 194 | InventoryItemBasePEOMtlTransactionsEnabledFlag | MTL_TRANSACTIONS_ENABLED_FLAG | — | ✅ |
| 195 | InventoryItemBasePEOMustUseApprovedVendorFlag | MUST_USE_APPROVED_VENDOR_FLAG | — | ✅ |
| 196 | InventoryItemBasePEONegativeMeasurementError | NEGATIVE_MEASUREMENT_ERROR | — | ✅ |
| 197 | InventoryItemBasePEONegotiationRequiredFlag | NEGOTIATION_REQUIRED_FLAG | — | ✅ |
| 198 | InventoryItemBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 199 | InventoryItemBasePEOOntPricingQtySource | ONT_PRICING_QTY_SOURCE | — | ✅ |
| 200 | InventoryItemBasePEOOperationSlackPenalty | OPERATION_SLACK_PENALTY | — | ✅ |
| 201 | InventoryItemBasePEOOptionSpecificSourced | OPTION_SPECIFIC_SOURCED | — | — |
| 202 | InventoryItemBasePEOOrderCost | ORDER_COST | — | ✅ |
| 203 | InventoryItemBasePEOOrderableOnWebFlag | ORDERABLE_ON_WEB_FLAG | — | ✅ |
| 204 | InventoryItemBasePEOOutsideOperationFlag | OUTSIDE_OPERATION_FLAG | — | ✅ |
| 205 | InventoryItemBasePEOOutsideOperationUomType | OUTSIDE_OPERATION_UOM_TYPE | — | ✅ |
| 206 | InventoryItemBasePEOOutsideProcessServiceFlag | OUTSIDE_PROCESS_SERVICE_FLAG | — | ✅ |
| 207 | InventoryItemBasePEOOutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | ✅ |
| 208 | InventoryItemBasePEOOverReturnTolerance | OVER_RETURN_TOLERANCE | — | ✅ |
| 209 | InventoryItemBasePEOOverShipmentTolerance | OVER_SHIPMENT_TOLERANCE | — | ✅ |
| 210 | InventoryItemBasePEOOvercompletionToleranceType | OVERCOMPLETION_TOLERANCE_TYPE | — | ✅ |
| 211 | InventoryItemBasePEOOvercompletionToleranceValue | OVERCOMPLETION_TOLERANCE_VALUE | — | ✅ |
| 212 | InventoryItemBasePEOOverrunPercentage | OVERRUN_PERCENTAGE | — | — |
| 213 | InventoryItemBasePEOPackagingStringId | PACKAGING_STRING_ID | — | — |
| 214 | InventoryItemBasePEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | ✅ |
| 215 | InventoryItemBasePEOPaymentTermsId | PAYMENT_TERMS_ID | — | — |
| 216 | InventoryItemBasePEOPickComponentsFlag | PICK_COMPONENTS_FLAG | — | ✅ |
| 217 | InventoryItemBasePEOPickingRuleId | PICKING_RULE_ID | — | — |
| 218 | InventoryItemBasePEOPlannedInvPointFlag | PLANNED_INV_POINT_FLAG | — | — |
| 219 | InventoryItemBasePEOPlannerCode | PLANNER_CODE | — | — |
| 220 | InventoryItemBasePEOPlanningExceptionSet | PLANNING_EXCEPTION_SET | — | — |
| 221 | InventoryItemBasePEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 222 | InventoryItemBasePEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | ✅ |
| 223 | InventoryItemBasePEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | ✅ |
| 224 | InventoryItemBasePEOPositiveMeasurementError | POSITIVE_MEASUREMENT_ERROR | — | ✅ |
| 225 | InventoryItemBasePEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 226 | InventoryItemBasePEOPreliminaryItemFlag | PRELIMINARY_ITEM_FLAG | — | — |
| 227 | InventoryItemBasePEOPrepositionPoint | PREPOSITION_POINT | — | — |
| 228 | InventoryItemBasePEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 229 | InventoryItemBasePEOPriceTolerancePercent | PRICE_TOLERANCE_PERCENT | — | ✅ |
| 230 | InventoryItemBasePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 231 | InventoryItemBasePEOProcessCostingEnabledFlag | PROCESS_COSTING_ENABLED_FLAG | — | ✅ |
| 232 | InventoryItemBasePEOProcessExecutionEnabledFlag | PROCESS_EXECUTION_ENABLED_FLAG | — | ✅ |
| 233 | InventoryItemBasePEOProcessQualityEnabledFlag | PROCESS_QUALITY_ENABLED_FLAG | — | ✅ |
| 234 | InventoryItemBasePEOProcessSupplyLocatorId | PROCESS_SUPPLY_LOCATOR_ID | — | — |
| 235 | InventoryItemBasePEOProcessSupplySubinventory | PROCESS_SUPPLY_SUBINVENTORY | — | ✅ |
| 236 | InventoryItemBasePEOProcessYieldLocatorId | PROCESS_YIELD_LOCATOR_ID | — | ✅ |
| 237 | InventoryItemBasePEOProcessYieldSubinventory | PROCESS_YIELD_SUBINVENTORY | — | ✅ |
| 238 | InventoryItemBasePEOProductFamilyItemId | PRODUCT_FAMILY_ITEM_ID | — | — |
| 239 | InventoryItemBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 240 | InventoryItemBasePEOProgramName | PROGRAM_NAME | — | — |
| 241 | InventoryItemBasePEOPurchasingEnabledFlag | PURCHASING_ENABLED_FLAG | — | ✅ |
| 242 | InventoryItemBasePEOPurchasingItemFlag | PURCHASING_ITEM_FLAG | — | ✅ |
| 243 | InventoryItemBasePEOPurchasingTaxCode | PURCHASING_TAX_CODE | — | ✅ |
| 244 | InventoryItemBasePEOQscSalesProductType | QSC_SALES_PRODUCT_TYPE | — | — |
| 245 | InventoryItemBasePEOQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 246 | InventoryItemBasePEOQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 247 | InventoryItemBasePEOReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 248 | InventoryItemBasePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 249 | InventoryItemBasePEOReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 250 | InventoryItemBasePEOReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 251 | InventoryItemBasePEORecipeEnabledFlag | RECIPE_ENABLED_FLAG | — | ✅ |
| 252 | InventoryItemBasePEORecoveredPartDispCode | RECOVERED_PART_DISP_CODE | — | ✅ |
| 253 | InventoryItemBasePEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | ✅ |
| 254 | InventoryItemBasePEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | ✅ |
| 255 | InventoryItemBasePEORepairLeadtime | REPAIR_LEADTIME | — | — |
| 256 | InventoryItemBasePEORepairProgram | REPAIR_PROGRAM | — | — |
| 257 | InventoryItemBasePEORepairYield | REPAIR_YIELD | — | — |
| 258 | InventoryItemBasePEORepetitivePlanningFlag | REPETITIVE_PLANNING_FLAG | — | — |
| 259 | InventoryItemBasePEOReplenishToOrderFlag | REPLENISH_TO_ORDER_FLAG | — | ✅ |
| 260 | InventoryItemBasePEORequestId | REQUEST_ID | — | — |
| 261 | InventoryItemBasePEORequiresFulfillmentLocFlag | REQUIRES_FULFILLMENT_LOC_FLAG | — | ✅ |
| 262 | InventoryItemBasePEORequiresItmAssociationFlag | REQUIRES_ITM_ASSOCIATION_FLAG | — | ✅ |
| 263 | InventoryItemBasePEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 264 | InventoryItemBasePEORestrictLocatorsCode | RESTRICT_LOCATORS_CODE | — | ✅ |
| 265 | InventoryItemBasePEORestrictSubinventoriesCode | RESTRICT_SUBINVENTORIES_CODE | — | ✅ |
| 266 | InventoryItemBasePEORetestInterval | RETEST_INTERVAL | — | ✅ |
| 267 | InventoryItemBasePEOReturnInspectionRequirement | RETURN_INSPECTION_REQUIREMENT | — | ✅ |
| 268 | InventoryItemBasePEOReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 269 | InventoryItemBasePEORevisionQtyControlCode | REVISION_QTY_CONTROL_CODE | — | ✅ |
| 270 | InventoryItemBasePEORoundingControlType | ROUNDING_CONTROL_TYPE | — | ✅ |
| 271 | InventoryItemBasePEORoundingFactor | ROUNDING_FACTOR | — | ✅ |
| 272 | InventoryItemBasePEOSafetyStockBucketDays | SAFETY_STOCK_BUCKET_DAYS | — | — |
| 273 | InventoryItemBasePEOSafetyStockPlanningMethod | SAFETY_STOCK_PLANNING_METHOD | — | ✅ |
| 274 | InventoryItemBasePEOSalesAccount | SALES_ACCOUNT | — | ✅ |
| 275 | InventoryItemBasePEOSalesProductType | SALES_PRODUCT_TYPE | — | ✅ |
| 276 | InventoryItemBasePEOSecondaryDefaultInd | SECONDARY_DEFAULT_IND | — | ✅ |
| 277 | InventoryItemBasePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 278 | InventoryItemBasePEOSerialNumberControlCode | SERIAL_NUMBER_CONTROL_CODE | — | ✅ |
| 279 | InventoryItemBasePEOSerialStatusEnabled | SERIAL_STATUS_ENABLED | — | ✅ |
| 280 | InventoryItemBasePEOServBillingEnabledFlag | SERV_BILLING_ENABLED_FLAG | — | ✅ |
| 281 | InventoryItemBasePEOServReqEnabledCode | SERV_REQ_ENABLED_CODE | — | ✅ |
| 282 | InventoryItemBasePEOServiceDuration | SERVICE_DURATION | — | ✅ |
| 283 | InventoryItemBasePEOServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | ✅ |
| 284 | InventoryItemBasePEOServiceDurationTypeCode | SERVICE_DURATION_TYPE_CODE | — | ✅ |
| 285 | InventoryItemBasePEOServiceStartTypeCode | SERVICE_START_TYPE_CODE | — | ✅ |
| 286 | InventoryItemBasePEOServiceStartingDelay | SERVICE_START_DELAY | — | ✅ |
| 287 | InventoryItemBasePEOServiceableProductFlag | SERVICEABLE_PRODUCT_FLAG | — | ✅ |
| 288 | InventoryItemBasePEOShelfLifeCode | SHELF_LIFE_CODE | — | ✅ |
| 289 | InventoryItemBasePEOShelfLifeDays | SHELF_LIFE_DAYS | — | ✅ |
| 290 | InventoryItemBasePEOShipModelCompleteFlag | SHIP_MODEL_COMPLETE_FLAG | — | ✅ |
| 291 | InventoryItemBasePEOShippableItemFlag | SHIPPABLE_ITEM_FLAG | — | ✅ |
| 292 | InventoryItemBasePEOShrinkageRate | SHRINKAGE_RATE | — | ✅ |
| 293 | InventoryItemBasePEOSoAuthorizationFlag | SO_AUTHORIZATION_FLAG | — | ✅ |
| 294 | InventoryItemBasePEOSoTransactionsFlag | SO_TRANSACTIONS_FLAG | — | ✅ |
| 295 | InventoryItemBasePEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 296 | InventoryItemBasePEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 297 | InventoryItemBasePEOSourceType | SOURCE_TYPE | — | ✅ |
| 298 | InventoryItemBasePEOStartAutoLotNumber | START_AUTO_LOT_NUMBER | — | ✅ |
| 299 | InventoryItemBasePEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | ✅ |
| 300 | InventoryItemBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 301 | InventoryItemBasePEOStdLotSize | STD_LOT_SIZE | — | ✅ |
| 302 | InventoryItemBasePEOStockEnabledFlag | STOCK_ENABLED_FLAG | — | ✅ |
| 303 | InventoryItemBasePEOStyleItemFlag | STYLE_ITEM_FLAG | — | ✅ |
| 304 | InventoryItemBasePEOStyleItemId | STYLE_ITEM_ID | — | ✅ |
| 305 | InventoryItemBasePEOSubcontractingComponent | SUBCONTRACTING_COMPONENT | — | ✅ |
| 306 | InventoryItemBasePEOSubstitutionWindowCode | SUBSTITUTION_WINDOW_CODE | — | — |
| 307 | InventoryItemBasePEOSubstitutionWindowDays | SUBSTITUTION_WINDOW_DAYS | — | — |
| 308 | InventoryItemBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 309 | InventoryItemBasePEOTaxCode | TAX_CODE | — | ✅ |
| 310 | InventoryItemBasePEOTaxableFlag | TAXABLE_FLAG | — | ✅ |
| 311 | InventoryItemBasePEOTemplateItemFlag | TEMPLATE_ITEM_FLAG | — | — |
| 312 | InventoryItemBasePEOTemplateName | ITEM_NUMBER | — | — |
| 313 | InventoryItemBasePEOTrackingQuantityInd | TRACKING_QUANTITY_IND | — | ✅ |
| 314 | InventoryItemBasePEOTradeItemDescriptor | TRADE_ITEM_DESCRIPTOR | — | ✅ |
| 315 | InventoryItemBasePEOURepairTransactionCode | REPAIR_TRANSACTION_CODE | — | — |
| 316 | InventoryItemBasePEOUnNumberId | UN_NUMBER_ID | — | ✅ |
| 317 | InventoryItemBasePEOUnderCompletionToleranceType | UNDER_COMPL_TOLERANCE_TYPE | — | — |
| 318 | InventoryItemBasePEOUnderCompletionToleranceValue | UNDER_COMPL_TOLERANCE_VALUE | — | — |
| 319 | InventoryItemBasePEOUnderReturnTolerance | UNDER_RETURN_TOLERANCE | — | ✅ |
| 320 | InventoryItemBasePEOUnderShipmentTolerance | UNDER_SHIPMENT_TOLERANCE | — | ✅ |
| 321 | InventoryItemBasePEOUnitHeight | UNIT_HEIGHT | — | ✅ |
| 322 | InventoryItemBasePEOUnitLength | UNIT_LENGTH | — | ✅ |
| 323 | InventoryItemBasePEOUnitOfIssue | UNIT_OF_ISSUE | — | ✅ |
| 324 | InventoryItemBasePEOUnitVolume | UNIT_VOLUME | — | ✅ |
| 325 | InventoryItemBasePEOUnitWeight | UNIT_WEIGHT | — | ✅ |
| 326 | InventoryItemBasePEOUnitWidth | UNIT_WIDTH | — | ✅ |
| 327 | InventoryItemBasePEOVariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 328 | InventoryItemBasePEOVehicleItemFlag | VEHICLE_ITEM_FLAG | — | ✅ |
| 329 | InventoryItemBasePEOVersionEndDate | VERSION_END_DATE | — | — |
| 330 | InventoryItemBasePEOVersionId | VERSION_ID | — | — |
| 331 | InventoryItemBasePEOVersionStartDate | VERSION_START_DATE | — | — |
| 332 | InventoryItemBasePEOVmiFixedOrderQuantity | VMI_FIXED_ORDER_QUANTITY | — | ✅ |
| 333 | InventoryItemBasePEOVmiForecastType | VMI_FORECAST_TYPE | — | ✅ |
| 334 | InventoryItemBasePEOVmiMaximumDays | VMI_MAXIMUM_DAYS | — | ✅ |
| 335 | InventoryItemBasePEOVmiMaximumUnits | VMI_MAXIMUM_UNITS | — | ✅ |
| 336 | InventoryItemBasePEOVmiMinimumDays | VMI_MINIMUM_DAYS | — | ✅ |
| 337 | InventoryItemBasePEOVmiMinimumUnits | VMI_MINIMUM_UNITS | — | ✅ |
| 338 | InventoryItemBasePEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 339 | InventoryItemBasePEOWebStatus | WEB_STATUS | — | ✅ |
| 340 | InventoryItemBasePEOWeightUomCode | WEIGHT_UOM_CODE | — | ✅ |
| 341 | InventoryItemBasePEOWipSupplyLocatorId | WIP_SUPPLY_LOCATOR_ID | — | — |
| 342 | InventoryItemBasePEOWipSupplySubinventory | WIP_SUPPLY_SUBINVENTORY | — | ✅ |
| 343 | InventoryItemBasePEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |
| 344 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 345 | ItemBasePEOOrderModifierStartQtyFlag | ORDER_MODIFIER_START_QTY_FLAG | — | — |
| 346 | ItemBasePEOPartsSourcing | PARTS_SOURCING | — | — |
| 347 | ItemBasePEOPlannerCode | PLANNER_CODE | — | — |
| 348 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 349 | ReplacementType | REPLACEMENT_TYPE | — | ✅ |

### [[egp_system_items_tl_v|EGP_SYSTEM_ITEMS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryItemTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | InventoryItemTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | InventoryItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | InventoryItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 5 | InventoryItemTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | InventoryItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InventoryItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InventoryItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InventoryItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 10 | InventoryItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InventoryItemTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | InventoryItemTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | ItemTranslationPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | ✅ |

### [[egp_system_items_vl|EGP_SYSTEM_ITEMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedFromItemPEODescription | DESCRIPTION | — | — |
| 2 | CreatedFromItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 3 | CreatedFromItemPEOItemNumber | ITEM_NUMBER | — | — |
| 4 | CreatedFromItemPEOOrganizationId | ORGANIZATION_ID | — | — |
| 5 | InventoryItemBaseModelPEODescription | DESCRIPTION | — | ✅ |
| 6 | InventoryItemBaseModelPEOItemId | INVENTORY_ITEM_ID | — | ✅ |
| 7 | InventoryItemBaseModelPEOItemNumber | ITEM_NUMBER | — | ✅ |
| 8 | InventoryItemBaseModelPEOItemType | ITEM_TYPE | — | ✅ |
| 9 | InventoryItemBaseModelPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 10 | InventoryItemBaseModelPEOOrgId | ORGANIZATION_ID | — | ✅ |
| 11 | StyleItemAllPEODescription | DESCRIPTION | — | — |
| 12 | StyleItemAllPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 13 | StyleItemAllPEOItemNumber | ITEM_NUMBER | — | — |
| 14 | StyleItemAllPEOOrganizationId | ORGANIZATION_ID | — | — |

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
| 17 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 18 | OrganizationUnitPEOType | TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterOrgUnitTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MasterOrgUnitTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MasterOrgUnitTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | MasterOrgUnitTLPEOName | NAME | — | ✅ |
| 5 | MasterOrgUnitTLPEOOrganizationId | ORGANIZATION_ID | — | — |
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
| 17 | OrganizationUnitTLPEOSourceLang | SOURCE_LANG | — | — |

### [[inv_actions_vl|INV_ACTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MtlActionsVlActionCode | ACTION_CODE | — | — |
| 2 | MtlActionsVlDescription | DESCRIPTION | — | ✅ |
| 3 | MtlActionsVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_material_statuses_vl|INV_MATERIAL_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DefaultLotStatusPEODescription | DESCRIPTION | — | ✅ |
| 2 | DefaultLotStatusPEOStatusCode | STATUS_CODE | — | ✅ |
| 3 | DefaultLotStatusPEOStatusId | STATUS_ID | — | — |
| 4 | DefaultSerialStatusPEODescription | DESCRIPTION | — | ✅ |
| 5 | DefaultSerialStatusPEOStatusCode | STATUS_CODE | — | ✅ |
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
| 2 | InventoryRulePEORuleName | RULE_NAME | — | ✅ |

### [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PSInvSubInventoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | PSInvSubInventoryPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |
| 3 | PSInvSubInventoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 4 | PSInvSubInventoryPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 5 | PYInvSubinventoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | PYInvSubinventoryPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |
| 7 | PYInvSubinventoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 8 | PYInvSubinventoryPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 9 | WipInvSubInventoryPEOOrganizationId | ORGANIZATION_ID | — | — |
| 10 | WipInvSubInventoryPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | — |
| 11 | WipInvSubInventoryPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 12 | WipInvSubInventoryPEOSubinventoryId | SUBINVENTORY_ID | — | — |

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
| 2 | DistributionRulePEOAccountingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | DistributionRulePEOAccountingRuleId | RULE_ID | — | — |
| 4 | DistributionRulePEOInvoicingName | NAME | — | ✅ |
| 5 | DistributionRulePEOInvoicingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | DistributionRulePEOInvoicingRuleId | RULE_ID | — | — |

### [[ra_terms_vl|RA_TERMS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermsVlName | NAME | — | ✅ |
| 2 | RaTermsVlTermId | TERM_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
