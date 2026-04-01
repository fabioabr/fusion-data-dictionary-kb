---
id: DOC-OTHER-PVO-ComponentPVO
doc_type: system-doc
title: "ComponentPVO — PVO Cross-Module"
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
  - ComponentPVO
  - componentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ComponentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Component. Acessa as tabelas: EGP_COMPONENTS_B, EGP_REFERENCE_DESIGNATORS, EGP_STRUCTURES_B (+4).

**Caminho:** `FscmTopModelAM.EgpStructuresPublicModelAM.ComponentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 191 | 7 | 1 | 48 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[egp_components_b|EGP_COMPONENTS_B]] — 74 atributos (1 PKs, 36 BICC)
- [[egp_reference_designators|EGP_REFERENCE_DESIGNATORS]] — 21 atributos (1 BICC)
- [[egp_structures_b|EGP_STRUCTURES_B]] — 29 atributos (6 BICC)
- [[egp_structure_names_vl|EGP_STRUCTURE_NAMES_VL]] — 21 atributos (1 BICC)
- [[egp_substitute_components|EGP_SUBSTITUTE_COMPONENTS]] — 22 atributos (1 BICC)
- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 12 atributos
- [[msc_units_of_measure|MSC_UNITS_OF_MEASURE]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[egp_components_b|EGP_COMPONENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentPEOAcdType | ACD_TYPE | — | — |
| 2 | ComponentPEOAutoRequestMaterial | AUTO_REQUEST_MATERIAL | — | — |
| 3 | ComponentPEOBasisType | BASIS_TYPE | — | — |
| 4 | ComponentPEOBillSequenceId | BILL_SEQUENCE_ID | — | ✅ |
| 5 | ComponentPEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 6 | ComponentPEOChangeId | CHANGE_ID | — | ✅ |
| 7 | ComponentPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 8 | ComponentPEOCheckAtp | CHECK_ATP | — | ✅ |
| 9 | ComponentPEOCommonComponentSequenceId | COMMON_COMPONENT_SEQUENCE_ID | — | — |
| 10 | ComponentPEOComponentItemRevisionId | COMPONENT_ITEM_REVISION_ID | — | — |
| 11 | ComponentPEOComponentQuantity | COMPONENT_QUANTITY | — | ✅ |
| 12 | ComponentPEOComponentRemarks | COMPONENT_REMARKS | — | ✅ |
| 13 | ComponentPEOComponentYieldFactor | COMPONENT_YIELD_FACTOR | — | ✅ |
| 14 | ComponentPEOCreatedBy | CREATED_BY | — | — |
| 15 | ComponentPEOCreationDate | CREATION_DATE | — | — |
| 16 | ComponentPEODeleteGroupName | DELETE_GROUP_NAME | — | ✅ |
| 17 | ComponentPEODgDescription | DG_DESCRIPTION | — | ✅ |
| 18 | ComponentPEODisableDate | DISABLE_DATE | — | ✅ |
| 19 | ComponentPEOEffectivityDate | EFFECTIVITY_DATE | — | ✅ |
| 20 | ComponentPEOEnforceIntRequirements | ENFORCE_INT_REQUIREMENTS | — | — |
| 21 | ComponentPEOFromEndItemRevId | FROM_END_ITEM_REV_ID | — | — |
| 22 | ComponentPEOFromEndItemUnitNumber | FROM_END_ITEM_UNIT_NUMBER | — | — |
| 23 | ComponentPEOHighQuantity | HIGH_QUANTITY | — | ✅ |
| 24 | ComponentPEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 25 | ComponentPEOIncludeOnBillDocs | INCLUDE_ON_BILL_DOCS | — | ✅ |
| 26 | ComponentPEOIncludeOnShipDocs | INCLUDE_ON_SHIP_DOCS | — | ✅ |
| 27 | ComponentPEOInstantiabilityCode | INSTANTIABILITY_CODE | — | ✅ |
| 28 | ComponentPEOItemNum | ITEM_NUM | — | ✅ |
| 29 | ComponentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | ComponentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | ComponentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | ComponentPEOLowQuantity | LOW_QUANTITY | — | ✅ |
| 33 | ComponentPEOModelCompSeqId | MODEL_COMP_SEQ_ID | — | — |
| 34 | ComponentPEOMutuallyExclusiveOptions | MUTUALLY_EXCLUSIVE_OPTIONS | — | ✅ |
| 35 | ComponentPEOObjName | OBJ_NAME | — | ✅ |
| 36 | ComponentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | ComponentPEOOldComponentSequenceId | OLD_COMPONENT_SEQUENCE_ID | — | — |
| 38 | ComponentPEOOperationLeadTimePercent | OPERATION_LEAD_TIME_PERCENT | — | ✅ |
| 39 | ComponentPEOOperationSeqNum | OPERATION_SEQ_NUM | — | ✅ |
| 40 | ComponentPEOOptional | OPTIONAL | — | ✅ |
| 41 | ComponentPEOOptionalOnModel | OPTIONAL_ON_MODEL | — | ✅ |
| 42 | ComponentPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 43 | ComponentPEOParentBillSeqId | PARENT_BILL_SEQ_ID | — | — |
| 44 | ComponentPEOPickComponents | PICK_COMPONENTS | — | ✅ |
| 45 | ComponentPEOPk1Value | PK1_VALUE | — | — |
| 46 | ComponentPEOPk2Value | PK2_VALUE | — | — |
| 47 | ComponentPEOPk3Value | PK3_VALUE | — | — |
| 48 | ComponentPEOPk4Value | PK4_VALUE | — | — |
| 49 | ComponentPEOPk5Value | PK5_VALUE | — | — |
| 50 | ComponentPEOPlanLevel | PLAN_LEVEL | — | — |
| 51 | ComponentPEOPlanningFactor | PLANNING_FACTOR | — | ✅ |
| 52 | ComponentPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 53 | ComponentPEOProgramName | PROGRAM_NAME | — | — |
| 54 | ComponentPEOQuantityRelated | QUANTITY_RELATED | — | — |
| 55 | ComponentPEOReplacedByComponent | REPLACED_BY_COMPONENT | — | — |
| 56 | ComponentPEOReplacedForCompSeqId | REPLACED_FOR_COMP_SEQ_ID | — | — |
| 57 | ComponentPEOReplacedForComponent | REPLACED_FOR_COMPONENT | — | — |
| 58 | ComponentPEORequestId | REQUEST_ID | — | — |
| 59 | ComponentPEORequiredForRevenue | REQUIRED_FOR_REVENUE | — | ✅ |
| 60 | ComponentPEORequiredToShip | REQUIRED_TO_SHIP | — | ✅ |
| 61 | ComponentPEOShippingAllowed | SHIPPING_ALLOWED | — | ✅ |
| 62 | ComponentPEOShowInSales | SHOW_IN_SALES | — | ✅ |
| 63 | ComponentPEOSoBasis | SO_BASIS | — | ✅ |
| 64 | ComponentPEOSuggestedOperationSeqNum | SUGGESTED_OPERATION_SEQ_NUM | — | — |
| 65 | ComponentPEOSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | — |
| 66 | ComponentPEOSupplyLocatorId | SUPPLY_LOCATOR_ID | — | — |
| 67 | ComponentPEOSupplySubinventory | SUPPLY_SUBINVENTORY | — | ✅ |
| 68 | ComponentPEOToEndItemRevId | TO_END_ITEM_REV_ID | — | — |
| 69 | ComponentPEOToEndItemUnitNumber | TO_END_ITEM_UNIT_NUMBER | — | — |
| 70 | ComponentPEOUnitPrice | UNIT_PRICE | — | ✅ |
| 71 | ComponentPEOUsePlaceholder | USE_PLACEHOLDER | — | — |
| 72 | ComponentPEOVendorId | VENDOR_ID | — | — |
| 73 | ComponentPEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |
| 74 | ComponentSequenceId | COMPONENT_SEQUENCE_ID | 🔑 | ✅ |

### [[egp_reference_designators|EGP_REFERENCE_DESIGNATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceDesignatorPEOAcdType | ACD_TYPE | — | — |
| 2 | ReferenceDesignatorPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 3 | ReferenceDesignatorPEOChangeNotice | CHANGE_NOTICE | — | — |
| 4 | ReferenceDesignatorPEOCommonComponentSequenceId | COMMON_COMPONENT_SEQUENCE_ID | — | — |
| 5 | ReferenceDesignatorPEOComponentReferenceDesignator | COMPONENT_REFERENCE_DESIGNATOR | — | — |
| 6 | ReferenceDesignatorPEOComponentSequenceId | COMPONENT_SEQUENCE_ID | — | — |
| 7 | ReferenceDesignatorPEOCreatedBy | CREATED_BY | — | — |
| 8 | ReferenceDesignatorPEOCreationDate | CREATION_DATE | — | — |
| 9 | ReferenceDesignatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | ReferenceDesignatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | ReferenceDesignatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ReferenceDesignatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ReferenceDesignatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ReferenceDesignatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ReferenceDesignatorPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 16 | ReferenceDesignatorPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | ReferenceDesignatorPEOProgramName | PROGRAM_NAME | — | — |
| 18 | ReferenceDesignatorPEORefDesigSequenceId | REF_DESIG_SEQUENCE_ID | — | — |
| 19 | ReferenceDesignatorPEORefDesignatorComment | REF_DESIGNATOR_COMMENT | — | — |
| 20 | ReferenceDesignatorPEORequestId | REQUEST_ID | — | — |
| 21 | ReferenceDesignatorPEOVersionId | VERSION_ID | — | — |

### [[egp_structures_b|EGP_STRUCTURES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureHeaderPEOAlternateBomDesignator | ALTERNATE_BOM_DESIGNATOR | — | ✅ |
| 2 | StructureHeaderPEOBillSequenceId | BILL_SEQUENCE_ID | — | ✅ |
| 3 | StructureHeaderPEOChangeId | CHANGE_ID | — | — |
| 4 | StructureHeaderPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 5 | StructureHeaderPEOCommonAssemblyItemId | COMMON_ASSEMBLY_ITEM_ID | — | — |
| 6 | StructureHeaderPEOCommonBillSequenceId | COMMON_BILL_SEQUENCE_ID | — | — |
| 7 | StructureHeaderPEOCommonOrganizationId | COMMON_ORGANIZATION_ID | — | — |
| 8 | StructureHeaderPEOCreatedBy | CREATED_BY | — | — |
| 9 | StructureHeaderPEOCreationDate | CREATION_DATE | — | — |
| 10 | StructureHeaderPEOEffectivityControl | EFFECTIVITY_CONTROL | — | ✅ |
| 11 | StructureHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | StructureHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | StructureHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | StructureHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | StructureHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | StructureHeaderPEOObjName | OBJ_NAME | — | ✅ |
| 17 | StructureHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | StructureHeaderPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 19 | StructureHeaderPEOPk1Value | PK1_VALUE | — | — |
| 20 | StructureHeaderPEOPk2Value | PK2_VALUE | — | — |
| 21 | StructureHeaderPEOPk3Value | PK3_VALUE | — | — |
| 22 | StructureHeaderPEOPk4Value | PK4_VALUE | — | — |
| 23 | StructureHeaderPEOPk5Value | PK5_VALUE | — | — |
| 24 | StructureHeaderPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 25 | StructureHeaderPEOProgramName | PROGRAM_NAME | — | — |
| 26 | StructureHeaderPEORequestId | REQUEST_ID | — | — |
| 27 | StructureHeaderPEOSourceBillSequenceId | SOURCE_BILL_SEQUENCE_ID | — | — |
| 28 | StructureHeaderPEOSpecificAssemblyComment | SPECIFIC_ASSEMBLY_COMMENT | — | ✅ |
| 29 | StructureHeaderPEOStructureTypeId | STRUCTURE_TYPE_ID | — | — |

### [[egp_structure_names_vl|EGP_STRUCTURE_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureNamePEOAlternateDesignatorCode | ALTERNATE_DESIGNATOR_CODE | — | — |
| 2 | StructureNamePEOAlternateDesignatorId | ALTERNATE_DESIGNATOR_ID | — | — |
| 3 | StructureNamePEOApplicationId | APPLICATION_ID | — | — |
| 4 | StructureNamePEOCreatedBy | CREATED_BY | — | — |
| 5 | StructureNamePEOCreationDate | CREATION_DATE | — | — |
| 6 | StructureNamePEODescription | DESCRIPTION | — | — |
| 7 | StructureNamePEODisableDate | DISABLE_DATE | — | — |
| 8 | StructureNamePEODisplayName | DISPLAY_NAME | — | — |
| 9 | StructureNamePEOEffectiveDate | EFFECTIVE_DATE | — | — |
| 10 | StructureNamePEOLanguage | LANGUAGE | — | — |
| 11 | StructureNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | StructureNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | StructureNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | StructureNamePEOLifecycleValidationFlag | LIFECYCLE_VALIDATION_FLAG | — | — |
| 15 | StructureNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | StructureNamePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | StructureNamePEOProgramName | PROGRAM_NAME | — | — |
| 18 | StructureNamePEORequestId | REQUEST_ID | — | — |
| 19 | StructureNamePEOSourceLang | SOURCE_LANG | — | — |
| 20 | StructureNamePEOStructureTypeId | STRUCTURE_TYPE_ID | — | — |
| 21 | StructureNamePEOUsePrimaryForExplFlag | USE_PRIMARY_FOR_EXPL_FLAG | — | — |

### [[egp_substitute_components|EGP_SUBSTITUTE_COMPONENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubstituteComponentsPEOAcdType | ACD_TYPE | — | — |
| 2 | SubstituteComponentsPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 3 | SubstituteComponentsPEOChangeNotice | CHANGE_NOTICE | — | — |
| 4 | SubstituteComponentsPEOCommonComponentSequenceId | COMMON_COMPONENT_SEQUENCE_ID | — | — |
| 5 | SubstituteComponentsPEOComponentSequenceId | COMPONENT_SEQUENCE_ID | — | — |
| 6 | SubstituteComponentsPEOCreatedBy | CREATED_BY | — | — |
| 7 | SubstituteComponentsPEOCreationDate | CREATION_DATE | — | — |
| 8 | SubstituteComponentsPEOEnforceIntRequirements | ENFORCE_INT_REQUIREMENTS | — | — |
| 9 | SubstituteComponentsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | SubstituteComponentsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | SubstituteComponentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | SubstituteComponentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | SubstituteComponentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | SubstituteComponentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | SubstituteComponentsPEOOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 16 | SubstituteComponentsPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | SubstituteComponentsPEOProgramName | PROGRAM_NAME | — | — |
| 18 | SubstituteComponentsPEORequestId | REQUEST_ID | — | — |
| 19 | SubstituteComponentsPEOSubstituteComponentId | SUBSTITUTE_COMPONENT_ID | — | — |
| 20 | SubstituteComponentsPEOSubstituteItemQuantity | SUBSTITUTE_ITEM_QUANTITY | — | — |
| 21 | SubstituteComponentsPEOVersionId | VERSION_ID | — | — |
| 22 | SubstitutecomponentsPEOSubCompSequenceId | SUB_COMP_SEQUENCE_ID | — | — |

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemPEOAcdType | ACD_TYPE | — | — |
| 2 | ItemPEOBomItemType | BOM_ITEM_TYPE | — | — |
| 3 | ItemPEOCreatedBy | CREATED_BY | — | — |
| 4 | ItemPEOCreationDate | CREATION_DATE | — | — |
| 5 | ItemPEOCurrentPhaseCode | CURRENT_PHASE_CODE | — | — |
| 6 | ItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 7 | ItemPEOItemNumber | ITEM_NUMBER | — | — |
| 8 | ItemPEOItemType | ITEM_TYPE | — | — |
| 9 | ItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | ItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ItemPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[msc_units_of_measure|MSC_UNITS_OF_MEASURE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitofMeasurePEOBaseUomFlag | BASE_UOM_FLAG | — | — |
| 2 | UnitofMeasurePEOCreatedBy | CREATED_BY | — | — |
| 3 | UnitofMeasurePEOCreationDate | CREATION_DATE | — | — |
| 4 | UnitofMeasurePEODescription | DESCRIPTION | — | — |
| 5 | UnitofMeasurePEODisableDate | DISABLE_DATE | — | — |
| 6 | UnitofMeasurePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | UnitofMeasurePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | UnitofMeasurePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | UnitofMeasurePEORefreshNumber | REFRESH_NUMBER | — | — |
| 10 | UnitofMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 11 | UnitofMeasurePEOUomClass | UOM_CLASS | — | ✅ |
| 12 | UnitofMeasurePEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
