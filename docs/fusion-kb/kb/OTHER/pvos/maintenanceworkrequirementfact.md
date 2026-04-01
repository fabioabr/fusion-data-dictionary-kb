---
id: DOC-OTHER-PVO-MaintenanceWorkRequirementFact
doc_type: system-doc
title: "MaintenanceWorkRequirementFact — PVO Cross-Module"
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
  - MaintenanceWorkRequirementFact
  - maintenanceworkrequirementfact
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWorkRequirementFact

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Work Requirement Fact. Acessa as tabelas: CSE_ASSETS_VL, MNT_PROGRAMS_B, MNT_WORK_REQUIREMENTS_FACT_V.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceWorkRequirementFact`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 181 | 3 | 2 | 24 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_vl|CSE_ASSETS_VL]] — 83 atributos
- [[mnt_programs_b|MNT_PROGRAMS_B]] — 51 atributos (1 BICC)
- [[mnt_work_requirements_fact_v|MNT_WORK_REQUIREMENTS_FACT_V]] — 47 atributos (2 PKs, 23 BICC)

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
| 46 | AssetPEOCurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | — |
| 47 | AssetPEOCurrentLocationId | CURRENT_LOCATION_ID | — | — |
| 48 | AssetPEOCustomerId | CUSTOMER_ID | — | — |
| 49 | AssetPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 50 | AssetPEODescription | DESCRIPTION | — | — |
| 51 | AssetPEODfltWoSubType | DFLT_WO_SUB_TYPE | — | — |
| 52 | AssetPEODfltWoType | DFLT_WO_TYPE | — | — |
| 53 | AssetPEOGenObjectId | GEN_OBJECT_ID | — | — |
| 54 | AssetPEOInServiceDate | IN_SERVICE_DATE | — | — |
| 55 | AssetPEOInstalledDate | INSTALLED_DATE | — | — |
| 56 | AssetPEOInstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | — |
| 57 | AssetPEOInstalledLocationId | INSTALLED_LOCATION_ID | — | — |
| 58 | AssetPEOInventoryLocatorId | INVENTORY_LOCATOR_ID | — | — |
| 59 | AssetPEOItemId | ITEM_ID | — | — |
| 60 | AssetPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 61 | AssetPEOItemRevision | ITEM_REVISION | — | — |
| 62 | AssetPEOLotNumber | LOT_NUMBER | — | — |
| 63 | AssetPEONewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | — |
| 64 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | AssetPEOOriginationDate | ORIGINATION_DATE | — | — |
| 66 | AssetPEOOwnedBy | OWNED_BY | — | — |
| 67 | AssetPEOPurchaseDate | PURCHASE_DATE | — | — |
| 68 | AssetPEOQuantity | QUANTITY | — | — |
| 69 | AssetPEORegisteredFlag | REGISTERED_FLAG | — | — |
| 70 | AssetPEOSalesOrderId | SALES_ORDER_ID | — | — |
| 71 | AssetPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | — |
| 72 | AssetPEOSerialNumber | SERIAL_NUMBER | — | — |
| 73 | AssetPEOShipmentDate | SHIPMENT_DATE | — | — |
| 74 | AssetPEOSoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | — |
| 75 | AssetPEOStatusCode | STATUS_CODE | — | — |
| 76 | AssetPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 77 | AssetPEOSupplierId | SUPPLIER_ID | — | — |
| 78 | AssetPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 79 | AssetPEOUomCode | UOM_CODE | — | — |
| 80 | AssetPEOUsedBy | USED_BY | — | — |
| 81 | AssetPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 82 | AssetPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 83 | AssetPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |

### [[mnt_programs_b|MNT_PROGRAMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramBasePEOActiveEndDate | ACTIVE_END_DATE | — | — |
| 2 | ProgramBasePEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | ProgramBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | ProgramBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | ProgramBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | ProgramBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | ProgramBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | ProgramBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | ProgramBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | ProgramBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | ProgramBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | ProgramBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | ProgramBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | ProgramBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | ProgramBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | ProgramBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | ProgramBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | ProgramBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | ProgramBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | ProgramBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | ProgramBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | ProgramBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | ProgramBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | ProgramBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | ProgramBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | ProgramBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | ProgramBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | ProgramBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | ProgramBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | ProgramBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | ProgramBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | ProgramBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | ProgramBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | ProgramBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | ProgramBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | ProgramBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | ProgramBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | ProgramBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | ProgramBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | ProgramBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | ProgramBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | ProgramBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | ProgramBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | ProgramBasePEOInProcessFlag | IN_PROCESS_FLAG | — | — |
| 45 | ProgramBasePEOLastForecastDate | LAST_FORECAST_DATE | — | — |
| 46 | ProgramBasePEOModifiedFlag | MODIFIED_FLAG | — | — |
| 47 | ProgramBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | ProgramBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 49 | ProgramBasePEOProgramCode | PROGRAM_CODE | — | — |
| 50 | ProgramBasePEOProgramId | PROGRAM_ID | — | — |
| 51 | ProgramBasePEOSuppressMergeCode | SUPPRESS_MERGE_CODE | — | — |

### [[mnt_work_requirements_fact_v|MNT_WORK_REQUIREMENTS_FACT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkRequirementFactPEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | WorkRequirementFactPEOActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | WorkRequirementFactPEOAssetHistoryServiceDate | ASSET_HISTORY_SERVICE_DATE | — | — |
| 4 | WorkRequirementFactPEOAssetHistoryServiceInterval | ASSET_HISTORY_SERVICE_INTERVAL | — | — |
| 5 | WorkRequirementFactPEOAssetId | ASSET_ID | — | — |
| 6 | WorkRequirementFactPEOAssetIdFinal | ASSET_ID_FINAL | 🔑 | ✅ |
| 7 | WorkRequirementFactPEOAssetInclusionTypeCode | ASSET_INCLUSION_TYPE_CODE | — | — |
| 8 | WorkRequirementFactPEOCalendarBasedFlag | CALENDAR_BASED_FLAG | — | ✅ |
| 9 | WorkRequirementFactPEOConditionBasedFlag | CONDITION_BASED_FLAG | — | ✅ |
| 10 | WorkRequirementFactPEOCreateWorkOrderOptionCode | CREATE_WORK_ORDER_OPTION_CODE | — | — |
| 11 | WorkRequirementFactPEOCreatedBy | CREATED_BY | — | — |
| 12 | WorkRequirementFactPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | WorkRequirementFactPEODayBasedFlag | DAY_BASED_FLAG | — | — |
| 14 | WorkRequirementFactPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 15 | WorkRequirementFactPEOForecastUsingCycleFlag | FORECAST_USING_CYCLE_FLAG | — | ✅ |
| 16 | WorkRequirementFactPEOForecastWindowInDays | FORECAST_WINDOW_IN_DAYS | — | — |
| 17 | WorkRequirementFactPEOIntervalsInTheCycle | INTERVALS_IN_THE_CYCLE | — | ✅ |
| 18 | WorkRequirementFactPEOItemId | ITEM_ID | — | ✅ |
| 19 | WorkRequirementFactPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 20 | WorkRequirementFactPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 21 | WorkRequirementFactPEOLanguage | LANGUAGE | — | — |
| 22 | WorkRequirementFactPEOLastForecastDate | LAST_FORECAST_DATE | — | ✅ |
| 23 | WorkRequirementFactPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | WorkRequirementFactPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | WorkRequirementFactPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | WorkRequirementFactPEOMeterBasedFlag | METER_BASED_FLAG | — | ✅ |
| 27 | WorkRequirementFactPEOModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 28 | WorkRequirementFactPEONextForecastDueByCode | NEXT_FORECAST_DUE_BY_CODE | — | — |
| 29 | WorkRequirementFactPEONextWorkOrderOnlyFlag | NEXT_WORK_ORDER_ONLY_FLAG | — | ✅ |
| 30 | WorkRequirementFactPEONumberOfDays | NUMBER_OF_DAYS | — | — |
| 31 | WorkRequirementFactPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | WorkRequirementFactPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 33 | WorkRequirementFactPEOProgramId | PROGRAM_ID | — | ✅ |
| 34 | WorkRequirementFactPEORequestId | REQUEST_ID | — | — |
| 35 | WorkRequirementFactPEORequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 36 | WorkRequirementFactPEORequirementName | REQUIREMENT_NAME | — | ✅ |
| 37 | WorkRequirementFactPEORequirementReference | REQUIREMENT_REFERENCE | — | — |
| 38 | WorkRequirementFactPEORequirementTypeCode | REQUIREMENT_TYPE_CODE | — | ✅ |
| 39 | WorkRequirementFactPEOSchedulePatternId | SCHEDULE_PATTERN_ID | — | ✅ |
| 40 | WorkRequirementFactPEOStatusCode | STATUS_CODE | — | ✅ |
| 41 | WorkRequirementFactPEOSuppressMergeCode | SUPPRESS_MERGE_CODE | — | ✅ |
| 42 | WorkRequirementFactPEOSuppressMergeOverrideFlag | SUPPRESS_MERGE_OVERRIDE_FLAG | — | ✅ |
| 43 | WorkRequirementFactPEOWoStatusId | WO_STATUS_ID | — | — |
| 44 | WorkRequirementFactPEOWoStatusName | WO_STATUS_NAME | — | — |
| 45 | WorkRequirementFactPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 46 | WorkRequirementFactPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 47 | WorkRequirementFactPEOWorkOrderWindowInDays | WORK_ORDER_WINDOW_IN_DAYS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
