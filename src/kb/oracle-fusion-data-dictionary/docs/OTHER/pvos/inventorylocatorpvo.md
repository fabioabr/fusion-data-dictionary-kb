---
id: DOC-OTHER-PVO-InventoryLocatorPVO
doc_type: system-doc
title: "InventoryLocatorPVO — PVO Cross-Module"
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
  - InventoryLocatorPVO
  - inventorylocatorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryLocatorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Locator. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, HR_ALL_ORGANIZATION_UNITS_F, HR_ORGANIZATION_UNITS_F_TL (+7).

**Caminho:** `FscmTopModelAM.InventoryAM.InventoryLocatorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 372 | 10 | 2 | 68 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 23 atributos (2 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 53 atributos (6 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 24 atributos (7 BICC)
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 59 atributos (2 PKs, 14 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 18 atributos
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 62 atributos (12 BICC)
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 63 atributos (2 BICC)
- [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]] — 51 atributos (22 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)
- [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]] — 16 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOName | BU_NAME | — | ✅ |
| 3 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 4 | MasterOrgBUBusinessUnitId | BU_ID | — | — |
| 5 | MasterOrgBUCreatedBy | CREATED_BY | — | — |
| 6 | MasterOrgBUCreationDate | CREATION_DATE | — | — |
| 7 | MasterOrgBUDateFrom | DATE_FROM | — | — |
| 8 | MasterOrgBUDateTo | DATE_TO | — | — |
| 9 | MasterOrgBUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 10 | MasterOrgBUDefaultSetId | DEFAULT_SET_ID | — | — |
| 11 | MasterOrgBUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 12 | MasterOrgBUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 13 | MasterOrgBUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 14 | MasterOrgBULastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | MasterOrgBULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | MasterOrgBULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | MasterOrgBULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 18 | MasterOrgBULocationId | LOCATION_ID | — | — |
| 19 | MasterOrgBUManagerId | MANAGER_ID | — | — |
| 20 | MasterOrgBUName | BU_NAME | — | — |
| 21 | MasterOrgBUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 22 | MasterOrgBUShortCode | SHORT_CODE | — | — |
| 23 | MasterOrgBUStatus | STATUS | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvHrAttributesPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | InvHrAttributesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 3 | InvHrAttributesPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 4 | InvHrAttributesPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 5 | InvHrAttributesPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 6 | InvHrAttributesPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 7 | InvHrAttributesPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 8 | InvHrAttributesPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 9 | InvHrAttributesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 10 | InvHrAttributesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 11 | InvHrAttributesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 12 | InvHrAttributesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 13 | InvHrAttributesPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 14 | InvHrAttributesPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 15 | InvHrAttributesPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 16 | InvHrAttributesPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 17 | InvHrAttributesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 18 | InvHrAttributesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 19 | InvHrAttributesPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 20 | InvHrAttributesPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 21 | InvHrAttributesPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 22 | InvHrAttributesPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 23 | InvHrAttributesPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 24 | InvHrAttributesPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 25 | InvHrAttributesPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 26 | InvHrAttributesPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 27 | InvHrAttributesPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 28 | InvHrAttributesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | InvHrAttributesPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 30 | InvHrAttributesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | InvHrAttributesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | InvHrAttributesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | InvHrAttributesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | InvHrAttributesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | InvHrAttributesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | InvHrAttributesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | InvHrAttributesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 38 | InvHrAttributesPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 39 | InvHrAttributesPEOCreatedBy | CREATED_BY | — | — |
| 40 | InvHrAttributesPEOCreationDate | CREATION_DATE | — | — |
| 41 | InvHrAttributesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 42 | InvHrAttributesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 43 | InvHrAttributesPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 44 | InvHrAttributesPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | ✅ |
| 45 | InvHrAttributesPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | ✅ |
| 46 | InvHrAttributesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | InvHrAttributesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | InvHrAttributesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 49 | InvHrAttributesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 50 | InvHrAttributesPEOLocationId | LOCATION_ID | — | — |
| 51 | InvHrAttributesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | InvHrAttributesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 53 | InvHrAttributesPEOType | TYPE | — | ✅ |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvOrgNamePEOCreatedBy | CREATED_BY | — | — |
| 2 | InvOrgNamePEOCreationDate | CREATION_DATE | — | — |
| 3 | InvOrgNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | InvOrgNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | InvOrgNamePEOLanguage | LANGUAGE | — | — |
| 6 | InvOrgNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InvOrgNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InvOrgNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InvOrgNamePEOName | NAME | — | ✅ |
| 10 | InvOrgNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InvOrgNamePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | InvOrgNamePEOSourceLang | SOURCE_LANG | — | — |
| 13 | OrganizationUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 14 | OrganizationUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 15 | OrganizationUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | OrganizationUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 17 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 18 | OrganizationUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | OrganizationUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | OrganizationUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | OrganizationUnitTranslationPEOName | NAME | — | ✅ |
| 22 | OrganizationUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | OrganizationUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 24 | OrganizationUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvLocatorPEOAlias | ALIAS | — | ✅ |
| 2 | InvLocatorPEOAvailabilityType | AVAILABILITY_TYPE | — | — |
| 3 | InvLocatorPEOAvailableCubicArea | AVAILABLE_CUBIC_AREA | — | — |
| 4 | InvLocatorPEOAvailableWeight | AVAILABLE_WEIGHT | — | — |
| 5 | InvLocatorPEOCreatedBy | CREATED_BY | — | — |
| 6 | InvLocatorPEOCreationDate | CREATION_DATE | — | — |
| 7 | InvLocatorPEOCurrentCubicArea | CURRENT_CUBIC_AREA | — | — |
| 8 | InvLocatorPEOCurrentWeight | CURRENT_WEIGHT | — | — |
| 9 | InvLocatorPEODepreciableFlag | DEPRECIABLE_FLAG | — | ✅ |
| 10 | InvLocatorPEODescription | DESCRIPTION | — | ✅ |
| 11 | InvLocatorPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 12 | InvLocatorPEODisableDate | DISABLE_DATE | — | ✅ |
| 13 | InvLocatorPEODroppingOrder | DROPPING_ORDER | — | — |
| 14 | InvLocatorPEOEmptyFlag | EMPTY_FLAG | — | — |
| 15 | InvLocatorPEOEnabledFlag | ENABLED_FLAG | — | — |
| 16 | InvLocatorPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 17 | InvLocatorPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 18 | InvLocatorPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 19 | InvLocatorPEOInventoryLocationType | INVENTORY_LOCATION_TYPE | — | ✅ |
| 20 | InvLocatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 21 | InvLocatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 22 | InvLocatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | InvLocatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | InvLocatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | InvLocatorPEOLocationAvailableUnits | LOCATION_AVAILABLE_UNITS | — | — |
| 26 | InvLocatorPEOLocationCurrentUnits | LOCATION_CURRENT_UNITS | — | — |
| 27 | InvLocatorPEOLocationHeight | LOCATION_HEIGHT | — | — |
| 28 | InvLocatorPEOLocationLength | LOCATION_LENGTH | — | — |
| 29 | InvLocatorPEOLocationMaximumUnits | LOCATION_MAXIMUM_UNITS | — | — |
| 30 | InvLocatorPEOLocationSuggestedUnits | LOCATION_SUGGESTED_UNITS | — | — |
| 31 | InvLocatorPEOLocationWeightUomCode | LOCATION_WEIGHT_UOM_CODE | — | — |
| 32 | InvLocatorPEOLocationWidth | LOCATION_WIDTH | — | — |
| 33 | InvLocatorPEOLocatorStatus | LOCATOR_STATUS | — | ✅ |
| 34 | InvLocatorPEOMaxCubicArea | MAX_CUBIC_AREA | — | — |
| 35 | InvLocatorPEOMaxWeight | MAX_WEIGHT | — | — |
| 36 | InvLocatorPEOMixedItemsFlag | MIXED_ITEMS_FLAG | — | — |
| 37 | InvLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | InvLocatorPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 39 | InvLocatorPEOPhysicalLocationCode | PHYSICAL_LOCATION_CODE | — | — |
| 40 | InvLocatorPEOPhysicalLocationId | PHYSICAL_LOCATION_ID | — | — |
| 41 | InvLocatorPEOPickUomCode | PICK_UOM_CODE | — | — |
| 42 | InvLocatorPEOPickingOrder | PICKING_ORDER | — | ✅ |
| 43 | InvLocatorPEOProjectId | PROJECT_ID | — | — |
| 44 | InvLocatorPEORequestId | REQUEST_ID | — | — |
| 45 | InvLocatorPEOReservableType | RESERVABLE_TYPE | — | — |
| 46 | InvLocatorPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 47 | InvLocatorPEOStatusId | STATUS_ID | — | ✅ |
| 48 | InvLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 49 | InvLocatorPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 50 | InvLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 51 | InvLocatorPEOSuggestedCubicArea | SUGGESTED_CUBIC_AREA | — | — |
| 52 | InvLocatorPEOSuggestedWeight | SUGGESTED_WEIGHT | — | — |
| 53 | InvLocatorPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 54 | InvLocatorPEOTaskId | TASK_ID | — | — |
| 55 | InvLocatorPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 56 | InvLocatorPEOXCoordinate | X_COORDINATE | — | — |
| 57 | InvLocatorPEOYCoordinate | Y_COORDINATE | — | — |
| 58 | InvLocatorPEOZCoordinate | Z_COORDINATE | — | — |
| 59 | InventoryLocationId | INVENTORY_LOCATION_ID | 🔑 | ✅ |

### [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgOrganizationDefinitionsPBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | OrgOrganizationDefinitionsPBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 3 | OrgOrganizationDefinitionsPBusinessUnitName | BUSINESS_UNIT_NAME | — | — |
| 4 | OrgOrganizationDefinitionsPChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 5 | OrgOrganizationDefinitionsPCurrencyCode | CURRENCY_CODE | — | — |
| 6 | OrgOrganizationDefinitionsPDisableDate | DISABLE_DATE | — | — |
| 7 | OrgOrganizationDefinitionsPDistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 8 | OrgOrganizationDefinitionsPInventoryEnabledFlag | INVENTORY_ENABLED_FLAG | — | — |
| 9 | OrgOrganizationDefinitionsPInventoryFlag | INVENTORY_FLAG | — | — |
| 10 | OrgOrganizationDefinitionsPLegalEntity | LEGAL_ENTITY | — | — |
| 11 | OrgOrganizationDefinitionsPLocationId | LOCATION_ID | — | — |
| 12 | OrgOrganizationDefinitionsPOrganizationCode | ORGANIZATION_CODE | — | — |
| 13 | OrgOrganizationDefinitionsPOrganizationId | ORGANIZATION_ID | — | — |
| 14 | OrgOrganizationDefinitionsPOrganizationName | ORGANIZATION_NAME | — | — |
| 15 | OrgOrganizationDefinitionsPOrganizationType | ORGANIZATION_TYPE | — | — |
| 16 | OrgOrganizationDefinitionsPPeriodSetName | PERIOD_SET_NAME | — | — |
| 17 | OrgOrganizationDefinitionsPSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 18 | OrgOrganizationDefinitionsPUserDefinitionEnableDate | USER_DEFINITION_ENABLE_DATE | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | — |
| 2 | OrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | — |
| 3 | OrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | ✅ |
| 4 | OrganizationParameterPEOAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | — |
| 5 | OrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | — |
| 6 | OrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 7 | OrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 8 | OrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 9 | OrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | — |
| 10 | OrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | — |
| 11 | OrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 12 | OrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | — |
| 13 | OrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 14 | OrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | — |
| 15 | OrganizationParameterPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | OrganizationParameterPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | OrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | — |
| 18 | OrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | — |
| 19 | OrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | — |
| 20 | OrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | ✅ |
| 21 | OrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | — |
| 22 | OrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | — |
| 23 | OrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | — |
| 24 | OrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | ✅ |
| 25 | OrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 26 | OrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | OrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | OrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | OrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | OrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 31 | OrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | — |
| 32 | OrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | — |
| 33 | OrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | — |
| 34 | OrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | — |
| 35 | OrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | — |
| 36 | OrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | — |
| 37 | OrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | — |
| 38 | OrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 39 | OrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | ✅ |
| 40 | OrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | ✅ |
| 41 | OrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | OrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 43 | OrganizationParameterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 44 | OrganizationParameterPEOOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | — |
| 45 | OrganizationParameterPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 46 | OrganizationParameterPEOPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | — |
| 47 | OrganizationParameterPEOPurchasingByRevision | PURCHASING_BY_REVISION | — | — |
| 48 | OrganizationParameterPEOReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | — |
| 49 | OrganizationParameterPEORequestId | REQUEST_ID | — | — |
| 50 | OrganizationParameterPEORoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | — |
| 51 | OrganizationParameterPEOScheduleId | SCHEDULE_ID | — | — |
| 52 | OrganizationParameterPEOSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | — |
| 53 | OrganizationParameterPEOSerialNumberType | SERIAL_NUMBER_TYPE | — | — |
| 54 | OrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 55 | OrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 56 | OrganizationParameterPEOSourceType | SOURCE_TYPE | — | — |
| 57 | OrganizationParameterPEOStandardPackEnabled | STANDARD_PACK_ENABLED | — | — |
| 58 | OrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 59 | OrganizationParameterPEOStartingRevision | STARTING_REVISION | — | — |
| 60 | OrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | ✅ |
| 61 | OrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | — |
| 62 | OrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | — |

### [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MasterOrgParamAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | — |
| 2 | MasterOrgParamAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | — |
| 3 | MasterOrgParamAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | — |
| 4 | MasterOrgParamAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | — |
| 5 | MasterOrgParamAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | — |
| 6 | MasterOrgParamAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 7 | MasterOrgParamAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 8 | MasterOrgParamBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 9 | MasterOrgParamCapturePickingException | CAPTURE_PICKING_EXCEPTION | — | — |
| 10 | MasterOrgParamChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | — |
| 11 | MasterOrgParamChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | — |
| 12 | MasterOrgParamChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 13 | MasterOrgParamChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | — |
| 14 | MasterOrgParamCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 15 | MasterOrgParamCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | — |
| 16 | MasterOrgParamCreatedBy | CREATED_BY | — | — |
| 17 | MasterOrgParamCreationDate | CREATION_DATE | — | — |
| 18 | MasterOrgParamDefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | — |
| 19 | MasterOrgParamDefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | — |
| 20 | MasterOrgParamDefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | — |
| 21 | MasterOrgParamDistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 22 | MasterOrgParamEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | — |
| 23 | MasterOrgParamFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | — |
| 24 | MasterOrgParamFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | — |
| 25 | MasterOrgParamJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 26 | MasterOrgParamJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 27 | MasterOrgParamLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | MasterOrgParamLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | MasterOrgParamLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | MasterOrgParamLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 31 | MasterOrgParamLotNumberGeneration | LOT_NUMBER_GENERATION | — | — |
| 32 | MasterOrgParamLotNumberLength | LOT_NUMBER_LENGTH | — | — |
| 33 | MasterOrgParamLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | — |
| 34 | MasterOrgParamLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | — |
| 35 | MasterOrgParamLpnPrefix | LPN_PREFIX | — | — |
| 36 | MasterOrgParamLpnStartingNumber | LPN_STARTING_NUMBER | — | — |
| 37 | MasterOrgParamLpnSuffix | LPN_SUFFIX | — | — |
| 38 | MasterOrgParamMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 39 | MasterOrgParamMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | — |
| 40 | MasterOrgParamNegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | — |
| 41 | MasterOrgParamOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 42 | MasterOrgParamOrganizationId | ORGANIZATION_ID | — | — |
| 43 | MasterOrgParamOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | — |
| 44 | MasterOrgParamParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 45 | MasterOrgParamPickQtyDefaultReasonId | PICK_QTY_DEFAULT_REASON_ID | — | — |
| 46 | MasterOrgParamPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | — |
| 47 | MasterOrgParamPreFillPickedQty | PRE_FILL_PICKED_QTY | — | — |
| 48 | MasterOrgParamPurchasingByRevision | PURCHASING_BY_REVISION | — | — |
| 49 | MasterOrgParamReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | — |
| 50 | MasterOrgParamRequestId | REQUEST_ID | — | — |
| 51 | MasterOrgParamRoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | — |
| 52 | MasterOrgParamScheduleId | SCHEDULE_ID | — | — |
| 53 | MasterOrgParamSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | — |
| 54 | MasterOrgParamSerialNumberType | SERIAL_NUMBER_TYPE | — | — |
| 55 | MasterOrgParamSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 56 | MasterOrgParamSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 57 | MasterOrgParamSourceType | SOURCE_TYPE | — | — |
| 58 | MasterOrgParamStandardPackEnabled | STANDARD_PACK_ENABLED | — | — |
| 59 | MasterOrgParamStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 60 | MasterOrgParamStartingRevision | STARTING_REVISION | — | — |
| 61 | MasterOrgParamStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | — |
| 62 | MasterOrgParamTotalLpnLength | TOTAL_LPN_LENGTH | — | — |
| 63 | MasterOrgParamUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | — |

### [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvSubinvPEOAssetInventory | ASSET_INVENTORY | — | ✅ |
| 2 | InvSubinvPEOAvailabilityType | AVAILABILITY_TYPE | — | ✅ |
| 3 | InvSubinvPEOCartonizationFlag | CARTONIZATION_FLAG | — | — |
| 4 | InvSubinvPEOCountMethod | COUNT_METHOD | — | ✅ |
| 5 | InvSubinvPEOCreatedBy | CREATED_BY | — | — |
| 6 | InvSubinvPEOCreationDate | CREATION_DATE | — | — |
| 7 | InvSubinvPEODefaultCountTypeCode | DEFAULT_COUNT_TYPE_CODE | — | ✅ |
| 8 | InvSubinvPEODefaultLocStatusId | DEFAULT_LOC_STATUS_ID | — | ✅ |
| 9 | InvSubinvPEODemandClass | DEMAND_CLASS | — | — |
| 10 | InvSubinvPEODepreciableFlag | DEPRECIABLE_FLAG | — | ✅ |
| 11 | InvSubinvPEODescription | DESCRIPTION | — | ✅ |
| 12 | InvSubinvPEODisableDate | DISABLE_DATE | — | ✅ |
| 13 | InvSubinvPEODroppingOrder | DROPPING_ORDER | — | — |
| 14 | InvSubinvPEOEnableBulkPick | ENABLE_BULK_PICK | — | — |
| 15 | InvSubinvPEOEnableLocatorAlias | ENABLE_LOCATOR_ALIAS | — | — |
| 16 | InvSubinvPEOEnforceAliasUniqueness | ENFORCE_ALIAS_UNIQUENESS | — | — |
| 17 | InvSubinvPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | ✅ |
| 18 | InvSubinvPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 19 | InvSubinvPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 20 | InvSubinvPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | InvSubinvPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | InvSubinvPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | InvSubinvPEOLocationId | LOCATION_ID | — | — |
| 24 | InvSubinvPEOLocatorType | LOCATOR_TYPE | — | ✅ |
| 25 | InvSubinvPEOLpnControlledFlag | LPN_CONTROLLED_FLAG | — | — |
| 26 | InvSubinvPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | InvSubinvPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 28 | InvSubinvPEOPickMethodology | PICK_METHODOLOGY | — | — |
| 29 | InvSubinvPEOPickUomCode | PICK_UOM_CODE | — | — |
| 30 | InvSubinvPEOPickingOrder | PICKING_ORDER | — | — |
| 31 | InvSubinvPEOPlanningLevel | PLANNING_LEVEL | — | ✅ |
| 32 | InvSubinvPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | — |
| 33 | InvSubinvPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | — |
| 34 | InvSubinvPEOProcessingLeadTime | PROCESSING_LEAD_TIME | — | — |
| 35 | InvSubinvPEOProjectId | PROJECT_ID | — | — |
| 36 | InvSubinvPEOQuantityTracked | QUANTITY_TRACKED | — | ✅ |
| 37 | InvSubinvPEORequestId | REQUEST_ID | — | — |
| 38 | InvSubinvPEORequisitionApprovalType | REQUISITION_APPROVAL_TYPE | — | — |
| 39 | InvSubinvPEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 40 | InvSubinvPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | — | ✅ |
| 41 | InvSubinvPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 42 | InvSubinvPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 43 | InvSubinvPEOSourceType | SOURCE_TYPE | — | ✅ |
| 44 | InvSubinvPEOStandardPackType | STANDARD_PACK_TYPE | — | — |
| 45 | InvSubinvPEOStatusId | STATUS_ID | — | ✅ |
| 46 | InvSubinvPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 47 | InvSubinvPEOSubinventoryGroup | SUBINVENTORY_GROUP | — | ✅ |
| 48 | InvSubinvPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 49 | InvSubinvPEOSubinventoryType | SUBINVENTORY_TYPE | — | ✅ |
| 50 | InvSubinvPEOSubinventoryUsage | SUBINVENTORY_USAGE | — | ✅ |
| 51 | InvSubinvPEOTaskId | TASK_ID | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XleEntityProfilesLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | XleEntityProfilesName | NAME | — | ✅ |
| 3 | XleEntityProfilesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleEOAssignmentNum | ASSIGNMENT_NUM | — | — |
| 2 | ScheduleEOCategoryCode | CATEGORY_CODE | — | — |
| 3 | ScheduleEOCreatedBy | CREATED_BY | — | — |
| 4 | ScheduleEOCreationDate | CREATION_DATE | — | — |
| 5 | ScheduleEODeletedFlag | DELETED_FLAG | — | — |
| 6 | ScheduleEOEffectiveFromDate | EFFECTIVE_FROM_DATE | — | — |
| 7 | ScheduleEOEffectiveToDate | EFFECTIVE_TO_DATE | — | — |
| 8 | ScheduleEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ScheduleEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ScheduleEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ScheduleEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ScheduleEOQtrlyTypeCode | QTRLY_TYPE_CODE | — | — |
| 13 | ScheduleEOScheduleDesc | SCHEDULE_DESC | — | — |
| 14 | ScheduleEOScheduleId | SCHEDULE_ID | — | — |
| 15 | ScheduleEOScheduleName | SCHEDULE_NAME | — | ✅ |
| 16 | ScheduleEOScheduleTypeCode | SCHEDULE_TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
