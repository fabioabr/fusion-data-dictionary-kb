---
id: DOC-OTHER-PVO-MaintenanceForecastFact
doc_type: system-doc
title: "MaintenanceForecastFact — PVO Cross-Module"
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
  - MaintenanceForecastFact
  - maintenanceforecastfact
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceForecastFact

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Forecast Fact. Acessa as tabelas: CSE_ASSETS_VL, INV_ORG_PARAMETERS, MNT_FORECASTS (+2).

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceForecastFact`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 200 | 5 | 1 | 28 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_vl|CSE_ASSETS_VL]] — 91 atributos (2 BICC)
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 4 atributos
- [[mnt_forecasts|MNT_FORECASTS]] — 10 atributos (4 BICC)
- [[mnt_forecast_lines|MNT_FORECAST_LINES]] — 36 atributos (1 PKs, 20 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 59 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cse_assets_vl|CSE_ASSETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOActiveEndDate | ACTIVE_END_DATE | — | — |
| 2 | AssetPEOAssetId | ASSET_ID | — | — |
| 3 | AssetPEOAssetNumber | ASSET_NUMBER | — | — |
| 4 | AssetPEOAssetTag | ASSET_TAG | — | — |
| 5 | AssetPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | AssetPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | AssetPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | AssetPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 9 | AssetPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 10 | AssetPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 11 | AssetPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 12 | AssetPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 13 | AssetPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 14 | AssetPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 15 | AssetPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 16 | AssetPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 17 | AssetPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 18 | AssetPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 19 | AssetPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 20 | AssetPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 21 | AssetPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 22 | AssetPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 23 | AssetPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 24 | AssetPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 25 | AssetPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 26 | AssetPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AssetPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | AssetPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | AssetPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | AssetPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | AssetPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 32 | AssetPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 33 | AssetPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 34 | AssetPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 35 | AssetPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 36 | AssetPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 37 | AssetPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 38 | AssetPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 39 | AssetPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 40 | AssetPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 41 | AssetPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 42 | AssetPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 43 | AssetPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 44 | AssetPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 45 | AssetPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 46 | AssetPEOCreatedBy | CREATED_BY | — | — |
| 47 | AssetPEOCreationDate | CREATION_DATE | — | — |
| 48 | AssetPEOCurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | — |
| 49 | AssetPEOCurrentLocationId | CURRENT_LOCATION_ID | — | — |
| 50 | AssetPEOCustomerId | CUSTOMER_ID | — | — |
| 51 | AssetPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 52 | AssetPEODescription | DESCRIPTION | — | — |
| 53 | AssetPEODfltWoSubType | DFLT_WO_SUB_TYPE | — | — |
| 54 | AssetPEODfltWoType | DFLT_WO_TYPE | — | — |
| 55 | AssetPEOGenObjectId | GEN_OBJECT_ID | — | — |
| 56 | AssetPEOInServiceDate | IN_SERVICE_DATE | — | — |
| 57 | AssetPEOInstalledDate | INSTALLED_DATE | — | — |
| 58 | AssetPEOInstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | — |
| 59 | AssetPEOInstalledLocationId | INSTALLED_LOCATION_ID | — | — |
| 60 | AssetPEOInventoryLocatorId | INVENTORY_LOCATOR_ID | — | — |
| 61 | AssetPEOItemId | ITEM_ID | — | — |
| 62 | AssetPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 63 | AssetPEOItemRevision | ITEM_REVISION | — | — |
| 64 | AssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 65 | AssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 66 | AssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 67 | AssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 68 | AssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 69 | AssetPEOLotNumber | LOT_NUMBER | — | — |
| 70 | AssetPEONewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | — |
| 71 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 72 | AssetPEOOriginationDate | ORIGINATION_DATE | — | — |
| 73 | AssetPEOOwnedBy | OWNED_BY | — | — |
| 74 | AssetPEOPurchaseDate | PURCHASE_DATE | — | — |
| 75 | AssetPEOQuantity | QUANTITY | — | — |
| 76 | AssetPEORegisteredFlag | REGISTERED_FLAG | — | — |
| 77 | AssetPEORequestId | REQUEST_ID | — | — |
| 78 | AssetPEOSalesOrderId | SALES_ORDER_ID | — | — |
| 79 | AssetPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | — |
| 80 | AssetPEOSerialNumber | SERIAL_NUMBER | — | — |
| 81 | AssetPEOShipmentDate | SHIPMENT_DATE | — | — |
| 82 | AssetPEOSoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | — |
| 83 | AssetPEOStatusCode | STATUS_CODE | — | — |
| 84 | AssetPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 85 | AssetPEOSupplierId | SUPPLIER_ID | — | — |
| 86 | AssetPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 87 | AssetPEOUomCode | UOM_CODE | — | — |
| 88 | AssetPEOUsedBy | USED_BY | — | — |
| 89 | AssetPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 90 | AssetPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 91 | AssetPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvOrgParametersForecastOrgIdOrganizationCode | ORGANIZATION_CODE | — | — |
| 2 | InvOrgParametersForecastOrgIdOrganizationId | ORGANIZATION_ID | — | — |
| 3 | InvOrgParametersWOOrgIdPEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 4 | InvOrgParametersWOOrgIdPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[mnt_forecasts|MNT_FORECASTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForecastPEOAssetId | ASSET_ID | — | — |
| 2 | ForecastPEOForecastDate | FORECAST_DATE | — | ✅ |
| 3 | ForecastPEOForecastId | FORECAST_ID | — | ✅ |
| 4 | ForecastPEOItemId | ITEM_ID | — | — |
| 5 | ForecastPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | ForecastPEOOrganizationId | ORGANIZATION_ID | — | — |
| 7 | ForecastPEOProgramId | PROGRAM_ID | — | ✅ |
| 8 | ForecastPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 9 | MaintenanceForecastPEORequestedSkipDueDateFlag | REQUESTED_SKIP_DUE_DATE_FLAG | — | — |
| 10 | MaintenanceForecastPEORequestedWoStartDate | REQUESTED_WO_START_DATE | — | — |

### [[mnt_forecast_lines|MNT_FORECAST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ForecastLinePEOAssetId | ASSET_ID | — | ✅ |
| 2 | ForecastLinePEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | ✅ |
| 3 | ForecastLinePEOCreatedBy | CREATED_BY | — | — |
| 4 | ForecastLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ForecastLinePEOCycleInterval | CYCLE_INTERVAL | — | ✅ |
| 6 | ForecastLinePEOForecastDate | FORECAST_DATE | — | ✅ |
| 7 | ForecastLinePEOForecastId | FORECAST_ID | — | ✅ |
| 8 | ForecastLinePEOForecastLineId | FORECAST_LINE_ID | 🔑 | ✅ |
| 9 | ForecastLinePEOForecastMtrReadingValue | FORECAST_MTR_READING_VALUE | — | ✅ |
| 10 | ForecastLinePEOForecastSequence | FORECAST_SEQUENCE | — | ✅ |
| 11 | ForecastLinePEOItemId | ITEM_ID | — | ✅ |
| 12 | ForecastLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ForecastLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ForecastLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ForecastLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ForecastLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ForecastLinePEOMeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 18 | ForecastLinePEOMeterId | METER_ID | — | ✅ |
| 19 | ForecastLinePEONextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 20 | ForecastLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ForecastLinePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 22 | ForecastLinePEORequestId | REQUEST_ID | — | — |
| 23 | ForecastLinePEORequirementId | REQUIREMENT_ID | — | ✅ |
| 24 | ForecastLinePEORequirementWdId | REQUIREMENT_WD_ID | — | — |
| 25 | ForecastLinePEOSchedulePatternId | SCHEDULE_PATTERN_ID | — | ✅ |
| 26 | ForecastLinePEOSuppressedFlag | SUPPRESSED_FLAG | — | ✅ |
| 27 | ForecastLinePEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 28 | ForecastLinePEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 29 | ForecastLinePVOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | — |
| 30 | ForecastLinePVOCycleInterval | CYCLE_INTERVAL | — | — |
| 31 | ForecastLinePVOForecastMtrReadingValue | FORECAST_MTR_READING_VALUE | — | — |
| 32 | ForecastLinePVOForecastSequence | FORECAST_SEQUENCE | — | — |
| 33 | ForecastLinePVOMeterDefinitionId | METER_DEFINITION_ID | — | — |
| 34 | ForecastLinePVORequirementWdId | REQUIREMENT_WD_ID | — | — |
| 35 | MaintenanceForecastLinePEODayIntervalValue | DAY_INTERVAL_VALUE | — | — |
| 36 | MaintenanceForecastLinePEOMeterUtilizationRate | METER_UTILIZATION_RATE | — | — |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 4 | WorkOrderPEOCanceledDate | CANCELED_DATE | — | — |
| 5 | WorkOrderPEOCanceledReason | CANCELED_REASON | — | — |
| 6 | WorkOrderPEOClosedDate | CLOSED_DATE | — | — |
| 7 | WorkOrderPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 8 | WorkOrderPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 9 | WorkOrderPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 10 | WorkOrderPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 11 | WorkOrderPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 12 | WorkOrderPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 13 | WorkOrderPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 14 | WorkOrderPEOCreatedBy | CREATED_BY | — | — |
| 15 | WorkOrderPEOCreationDate | CREATION_DATE | — | — |
| 16 | WorkOrderPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 17 | WorkOrderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 18 | WorkOrderPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 19 | WorkOrderPEOItemRevision | ITEM_REVISION | — | — |
| 20 | WorkOrderPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 21 | WorkOrderPEOItemVersion | ITEM_VERSION | — | — |
| 22 | WorkOrderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | WorkOrderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | WorkOrderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | WorkOrderPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 26 | WorkOrderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | WorkOrderPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 28 | WorkOrderPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 29 | WorkOrderPEOOrganizationId | ORGANIZATION_ID | — | — |
| 30 | WorkOrderPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 31 | WorkOrderPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 32 | WorkOrderPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 33 | WorkOrderPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 34 | WorkOrderPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 35 | WorkOrderPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 36 | WorkOrderPEOReleasedDate | RELEASED_DATE | — | — |
| 37 | WorkOrderPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 38 | WorkOrderPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 39 | WorkOrderPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 40 | WorkOrderPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 41 | WorkOrderPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 42 | WorkOrderPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 43 | WorkOrderPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 44 | WorkOrderPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 45 | WorkOrderPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 46 | WorkOrderPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 47 | WorkOrderPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 48 | WorkOrderPEOSupplyType | SUPPLY_TYPE | — | — |
| 49 | WorkOrderPEOUomCode | UOM_CODE | — | — |
| 50 | WorkOrderPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 51 | WorkOrderPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 52 | WorkOrderPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 53 | WorkOrderPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 54 | WorkOrderPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 55 | WorkOrderPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 56 | WorkOrderPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 57 | WorkOrderPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 58 | WorkOrderPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 59 | WorkOrderPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
