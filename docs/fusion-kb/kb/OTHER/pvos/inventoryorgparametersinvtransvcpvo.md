---
id: DOC-OTHER-PVO-InventoryOrgParametersInvTransVCPVO
doc_type: system-doc
title: "InventoryOrgParametersInvTransVCPVO — PVO Cross-Module"
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
  - InventoryOrgParametersInvTransVCPVO
  - inventoryorgparametersinvtransvcpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryOrgParametersInvTransVCPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Org Parameters Inv Trans VC. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, HR_ALL_ORGANIZATION_UNITS_F, HR_ORGANIZATION_UNITS_F_TL (+5).

**Caminho:** `FscmTopModelAM.InvOrgPublicViewAM.InventoryOrgParametersInvTransVCPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 323 | 8 | 1 | 6 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 40 atributos (2 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 53 atributos
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 24 atributos
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 19 atributos
- [[inv_org_parameters|INV_ORG_PARAMETERS]] — 66 atributos (1 PKs, 2 BICC)
- [[inv_org_parameters_v|INV_ORG_PARAMETERS_V]] — 63 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 42 atributos (1 BICC)
- [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]] — 16 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | ✅ |
| 2 | BusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 3 | BusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 4 | BusinessUnitPEODateFrom | DATE_FROM | — | — |
| 5 | BusinessUnitPEODateTo | DATE_TO | — | — |
| 6 | BusinessUnitPEODefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BusinessUnitPEODefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BusinessUnitPEOEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BusinessUnitPEOEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BusinessUnitPEOFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOManagerId | MANAGER_ID | — | — |
| 17 | BusinessUnitPEOName | BU_NAME | — | — |
| 18 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BusinessUnitPEOShortCode | SHORT_CODE | — | — |
| 20 | BusinessUnitPEOStatus | STATUS | — | — |
| 21 | MasterOrgBUBusinessUnitId | BU_ID | — | — |
| 22 | MasterOrgBUCreatedBy | CREATED_BY | — | — |
| 23 | MasterOrgBUCreationDate | CREATION_DATE | — | — |
| 24 | MasterOrgBUDateFrom | DATE_FROM | — | — |
| 25 | MasterOrgBUDateTo | DATE_TO | — | — |
| 26 | MasterOrgBUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 27 | MasterOrgBUDefaultSetId | DEFAULT_SET_ID | — | — |
| 28 | MasterOrgBUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 29 | MasterOrgBUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 30 | MasterOrgBUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 31 | MasterOrgBULastUpdateDate | LAST_UPDATE_DATE | — | — |
| 32 | MasterOrgBULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | MasterOrgBULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | MasterOrgBULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 35 | MasterOrgBULocationId | LOCATION_ID | — | — |
| 36 | MasterOrgBUManagerId | MANAGER_ID | — | — |
| 37 | MasterOrgBUName | BU_NAME | — | — |
| 38 | MasterOrgBUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 39 | MasterOrgBUShortCode | SHORT_CODE | — | — |
| 40 | MasterOrgBUStatus | STATUS | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvOrgHrAttributesPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | InvOrgHrAttributesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 3 | InvOrgHrAttributesPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 4 | InvOrgHrAttributesPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 5 | InvOrgHrAttributesPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 6 | InvOrgHrAttributesPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 7 | InvOrgHrAttributesPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 8 | InvOrgHrAttributesPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 9 | InvOrgHrAttributesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 10 | InvOrgHrAttributesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 11 | InvOrgHrAttributesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 12 | InvOrgHrAttributesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 13 | InvOrgHrAttributesPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 14 | InvOrgHrAttributesPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 15 | InvOrgHrAttributesPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 16 | InvOrgHrAttributesPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 17 | InvOrgHrAttributesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 18 | InvOrgHrAttributesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 19 | InvOrgHrAttributesPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 20 | InvOrgHrAttributesPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 21 | InvOrgHrAttributesPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 22 | InvOrgHrAttributesPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 23 | InvOrgHrAttributesPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 24 | InvOrgHrAttributesPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 25 | InvOrgHrAttributesPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 26 | InvOrgHrAttributesPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 27 | InvOrgHrAttributesPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 28 | InvOrgHrAttributesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | InvOrgHrAttributesPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 30 | InvOrgHrAttributesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | InvOrgHrAttributesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | InvOrgHrAttributesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | InvOrgHrAttributesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | InvOrgHrAttributesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | InvOrgHrAttributesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | InvOrgHrAttributesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | InvOrgHrAttributesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 38 | InvOrgHrAttributesPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 39 | InvOrgHrAttributesPEOCreatedBy | CREATED_BY | — | — |
| 40 | InvOrgHrAttributesPEOCreationDate | CREATION_DATE | — | — |
| 41 | InvOrgHrAttributesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 42 | InvOrgHrAttributesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 43 | InvOrgHrAttributesPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 44 | InvOrgHrAttributesPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 45 | InvOrgHrAttributesPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 46 | InvOrgHrAttributesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 47 | InvOrgHrAttributesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | InvOrgHrAttributesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 49 | InvOrgHrAttributesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 50 | InvOrgHrAttributesPEOLocationId | LOCATION_ID | — | — |
| 51 | InvOrgHrAttributesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | InvOrgHrAttributesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 53 | InvOrgHrAttributesPEOType | TYPE | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvOrgNamePEOCreatedBy | CREATED_BY | — | — |
| 2 | InvOrgNamePEOCreationDate | CREATION_DATE | — | — |
| 3 | InvOrgNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | InvOrgNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | InvOrgNamePEOLanguage | LANGUAGE | — | — |
| 6 | InvOrgNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | InvOrgNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InvOrgNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InvOrgNamePEOName | NAME | — | — |
| 10 | InvOrgNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | InvOrgNamePEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | InvOrgNamePEOSourceLang | SOURCE_LANG | — | — |
| 13 | OrganizationUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 14 | OrganizationUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 15 | OrganizationUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 16 | OrganizationUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 17 | OrganizationUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 18 | OrganizationUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 19 | OrganizationUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | OrganizationUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | OrganizationUnitTranslationPEOName | NAME | — | — |
| 22 | OrganizationUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | OrganizationUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 24 | OrganizationUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |

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
| 12 | OrgOrganizationDefinitionsPMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 13 | OrgOrganizationDefinitionsPOrganizationCode | ORGANIZATION_CODE | — | — |
| 14 | OrgOrganizationDefinitionsPOrganizationId | ORGANIZATION_ID | — | — |
| 15 | OrgOrganizationDefinitionsPOrganizationName | ORGANIZATION_NAME | — | — |
| 16 | OrgOrganizationDefinitionsPOrganizationType | ORGANIZATION_TYPE | — | — |
| 17 | OrgOrganizationDefinitionsPPeriodSetName | PERIOD_SET_NAME | — | — |
| 18 | OrgOrganizationDefinitionsPSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 19 | OrgOrganizationDefinitionsPUserDefinitionEnableDate | USER_DEFINITION_ENABLE_DATE | — | — |

### [[inv_org_parameters|INV_ORG_PARAMETERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 2 | OrganizationParameterPEOAllocateSerialFlag | ALLOCATE_SERIAL_FLAG | — | — |
| 3 | OrganizationParameterPEOAllowDifferentStatus | ALLOW_DIFFERENT_STATUS | — | — |
| 4 | OrganizationParameterPEOAllowNegOnhandCcTxns | ALLOW_NEG_ONHAND_CC_TXNS | — | — |
| 5 | OrganizationParameterPEOAutoBreakdownEnabled | AUTO_BREAKDOWN_ENABLED | — | — |
| 6 | OrganizationParameterPEOAutoDelAllocFlag | AUTO_DEL_ALLOC_FLAG | — | — |
| 7 | OrganizationParameterPEOAutoLotAlphaPrefix | AUTO_LOT_ALPHA_PREFIX | — | — |
| 8 | OrganizationParameterPEOAutoSerialAlphaPrefix | AUTO_SERIAL_ALPHA_PREFIX | — | — |
| 9 | OrganizationParameterPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 10 | OrganizationParameterPEOChildLotAlphaPrefix | CHILD_LOT_ALPHA_PREFIX | — | — |
| 11 | OrganizationParameterPEOChildLotNumberLength | CHILD_LOT_NUMBER_LENGTH | — | — |
| 12 | OrganizationParameterPEOChildLotValidationFlag | CHILD_LOT_VALIDATION_FLAG | — | — |
| 13 | OrganizationParameterPEOChildLotZeroPaddingFlag | CHILD_LOT_ZERO_PADDING_FLAG | — | — |
| 14 | OrganizationParameterPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 15 | OrganizationParameterPEOCopyLotAttributeFlag | COPY_LOT_ATTRIBUTE_FLAG | — | — |
| 16 | OrganizationParameterPEOCreateLotUomConversion | CREATE_LOT_UOM_CONVERSION | — | — |
| 17 | OrganizationParameterPEOCreatedBy | CREATED_BY | — | — |
| 18 | OrganizationParameterPEOCreationDate | CREATION_DATE | — | — |
| 19 | OrganizationParameterPEODefaultLocatorOrderValue | DEFAULT_LOCATOR_ORDER_VALUE | — | — |
| 20 | OrganizationParameterPEODefaultPickingRuleId | DEFAULT_PICKING_RULE_ID | — | — |
| 21 | OrganizationParameterPEODefaultSubinvOrderValue | DEFAULT_SUBINV_ORDER_VALUE | — | — |
| 22 | OrganizationParameterPEODistributedOrganizationFlag | DISTRIBUTED_ORGANIZATION_FLAG | — | — |
| 23 | OrganizationParameterPEOEnforceLocatorAlisUnqFlag | ENFORCE_LOCATOR_ALIS_UNQ_FLAG | — | — |
| 24 | OrganizationParameterPEOFifoOrigRcptDateFlag | FIFO_ORIG_RCPT_DATE_FLAG | — | — |
| 25 | OrganizationParameterPEOFillKillMoveOrderFlag | FILL_KILL_MOVE_ORDER_FLAG | — | — |
| 26 | OrganizationParameterPEOInventoryFlag | INVENTORY_FLAG | — | — |
| 27 | OrganizationParameterPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | OrganizationParameterPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | OrganizationParameterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | OrganizationParameterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | OrganizationParameterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | OrganizationParameterPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 33 | OrganizationParameterPEOLotNumberGeneration | LOT_NUMBER_GENERATION | — | — |
| 34 | OrganizationParameterPEOLotNumberLength | LOT_NUMBER_LENGTH | — | — |
| 35 | OrganizationParameterPEOLotNumberUniqueness | LOT_NUMBER_UNIQUENESS | — | — |
| 36 | OrganizationParameterPEOLotNumberZeroPadding | LOT_NUMBER_ZERO_PADDING | — | — |
| 37 | OrganizationParameterPEOLpnPrefix | LPN_PREFIX | — | — |
| 38 | OrganizationParameterPEOLpnStartingNumber | LPN_STARTING_NUMBER | — | — |
| 39 | OrganizationParameterPEOLpnSuffix | LPN_SUFFIX | — | — |
| 40 | OrganizationParameterPEOMasterOrganizationId | MASTER_ORGANIZATION_ID | — | — |
| 41 | OrganizationParameterPEOMfgPlantFlag | MFG_PLANT_FLAG | — | — |
| 42 | OrganizationParameterPEOMoPickConfirmRequired | MO_PICK_CONFIRM_REQUIRED | — | — |
| 43 | OrganizationParameterPEONegativeInvReceiptCode | NEGATIVE_INV_RECEIPT_CODE | — | — |
| 44 | OrganizationParameterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | OrganizationParameterPEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 46 | OrganizationParameterPEOOvpkTransferOrdersEnabled | OVPK_TRANSFER_ORDERS_ENABLED | — | — |
| 47 | OrganizationParameterPEOParentChildGenerationFlag | PARENT_CHILD_GENERATION_FLAG | — | — |
| 48 | OrganizationParameterPEOPickSlipBatchSize | PICK_SLIP_BATCH_SIZE | — | — |
| 49 | OrganizationParameterPEOPurchasingByRevision | PURCHASING_BY_REVISION | — | — |
| 50 | OrganizationParameterPEOReplnshMoveOrderGrouping | REPLNSH_MOVE_ORDER_GROUPING | — | — |
| 51 | OrganizationParameterPEORequestId | REQUEST_ID | — | — |
| 52 | OrganizationParameterPEORoundReorderQtyFlag | ROUND_REORDER_QTY_FLAG | — | — |
| 53 | OrganizationParameterPEOScheduleId | SCHEDULE_ID | — | — |
| 54 | OrganizationParameterPEOSerialNumberGeneration | SERIAL_NUMBER_GENERATION | — | — |
| 55 | OrganizationParameterPEOSerialNumberType | SERIAL_NUMBER_TYPE | — | — |
| 56 | OrganizationParameterPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | — |
| 57 | OrganizationParameterPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | — |
| 58 | OrganizationParameterPEOSourceType | SOURCE_TYPE | — | — |
| 59 | OrganizationParameterPEOStandardPackEnabled | STANDARD_PACK_ENABLED | — | — |
| 60 | OrganizationParameterPEOStartAutoSerialNumber | START_AUTO_SERIAL_NUMBER | — | — |
| 61 | OrganizationParameterPEOStartingRevision | STARTING_REVISION | — | — |
| 62 | OrganizationParameterPEOStockLocatorControlCode | STOCK_LOCATOR_CONTROL_CODE | — | — |
| 63 | OrganizationParameterPEOSupplierId | SUPPLIER_ID | — | — |
| 64 | OrganizationParameterPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 65 | OrganizationParameterPEOTotalLpnLength | TOTAL_LPN_LENGTH | — | — |
| 66 | OrganizationParameterPEOUcc128SuffixFlag | UCC_128_SUFFIX_FLAG | — | — |

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
| 27 | MasterOrgParamLastUpdateDate | LAST_UPDATE_DATE | — | — |
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
| 41 | MasterOrgParamOrganizationCode | ORGANIZATION_CODE | — | — |
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

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityPEOActivityCode | ACTIVITY_CODE | — | — |
| 2 | LegalEntityPEOCreatedBy | CREATED_BY | — | — |
| 3 | LegalEntityPEOCreationDate | CREATION_DATE | — | — |
| 4 | LegalEntityPEOEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | LegalEntityPEOEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | LegalEntityPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | LegalEntityPEOGeographyId | GEOGRAPHY_ID | — | — |
| 8 | LegalEntityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LegalEntityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LegalEntityPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LegalEntityPEOLeInformation1 | LE_INFORMATION1 | — | — |
| 12 | LegalEntityPEOLeInformation10 | LE_INFORMATION10 | — | — |
| 13 | LegalEntityPEOLeInformation11 | LE_INFORMATION11 | — | — |
| 14 | LegalEntityPEOLeInformation12 | LE_INFORMATION12 | — | — |
| 15 | LegalEntityPEOLeInformation13 | LE_INFORMATION13 | — | — |
| 16 | LegalEntityPEOLeInformation14 | LE_INFORMATION14 | — | — |
| 17 | LegalEntityPEOLeInformation15 | LE_INFORMATION15 | — | — |
| 18 | LegalEntityPEOLeInformation16 | LE_INFORMATION16 | — | — |
| 19 | LegalEntityPEOLeInformation17 | LE_INFORMATION17 | — | — |
| 20 | LegalEntityPEOLeInformation18 | LE_INFORMATION18 | — | — |
| 21 | LegalEntityPEOLeInformation19 | LE_INFORMATION19 | — | — |
| 22 | LegalEntityPEOLeInformation2 | LE_INFORMATION2 | — | — |
| 23 | LegalEntityPEOLeInformation20 | LE_INFORMATION20 | — | — |
| 24 | LegalEntityPEOLeInformation3 | LE_INFORMATION3 | — | — |
| 25 | LegalEntityPEOLeInformation4 | LE_INFORMATION4 | — | — |
| 26 | LegalEntityPEOLeInformation5 | LE_INFORMATION5 | — | — |
| 27 | LegalEntityPEOLeInformation6 | LE_INFORMATION6 | — | — |
| 28 | LegalEntityPEOLeInformation7 | LE_INFORMATION7 | — | — |
| 29 | LegalEntityPEOLeInformation8 | LE_INFORMATION8 | — | — |
| 30 | LegalEntityPEOLeInformation9 | LE_INFORMATION9 | — | — |
| 31 | LegalEntityPEOLeInformationContext | LE_INFORMATION_CONTEXT | — | — |
| 32 | LegalEntityPEOLegalEmployerFlag | LEGAL_EMPLOYER_FLAG | — | — |
| 33 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 34 | LegalEntityPEOLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | — |
| 35 | LegalEntityPEOName | NAME | — | — |
| 36 | LegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | LegalEntityPEOParentPsuId | PARENT_PSU_ID | — | — |
| 38 | LegalEntityPEOPartyId | PARTY_ID | — | — |
| 39 | LegalEntityPEOPsuFlag | PSU_FLAG | — | — |
| 40 | LegalEntityPEOSubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 41 | LegalEntityPEOTransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | — |
| 42 | LegalEntityPEOTypeOfCompany | TYPE_OF_COMPANY | — | — |

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
| 15 | ScheduleEOScheduleName | SCHEDULE_NAME | — | — |
| 16 | ScheduleEOScheduleTypeCode | SCHEDULE_TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
