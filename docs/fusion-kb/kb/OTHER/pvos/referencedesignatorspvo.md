---
id: DOC-OTHER-PVO-ReferenceDesignatorsPVO
doc_type: system-doc
title: "ReferenceDesignatorsPVO — PVO Cross-Module"
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
  - ReferenceDesignatorsPVO
  - referencedesignatorspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceDesignatorsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reference Designators. Acessa as tabelas: EGP_COMPONENTS_B, EGP_REFERENCE_DESIGNATORS.

**Caminho:** `FscmTopModelAM.EgpStructuresPublicModelAM.ReferenceDesignatorsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 144 | 2 | 1 | 6 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[egp_components_b|EGP_COMPONENTS_B]] — 123 atributos
- [[egp_reference_designators|EGP_REFERENCE_DESIGNATORS]] — 21 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[egp_components_b|EGP_COMPONENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentAcdType | ACD_TYPE | — | — |
| 2 | ComponentAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ComponentAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ComponentAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ComponentAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ComponentAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ComponentAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ComponentAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ComponentAttribute16 | ATTRIBUTE16 | — | — |
| 10 | ComponentAttribute17 | ATTRIBUTE17 | — | — |
| 11 | ComponentAttribute18 | ATTRIBUTE18 | — | — |
| 12 | ComponentAttribute19 | ATTRIBUTE19 | — | — |
| 13 | ComponentAttribute2 | ATTRIBUTE2 | — | — |
| 14 | ComponentAttribute20 | ATTRIBUTE20 | — | — |
| 15 | ComponentAttribute21 | ATTRIBUTE21 | — | — |
| 16 | ComponentAttribute22 | ATTRIBUTE22 | — | — |
| 17 | ComponentAttribute23 | ATTRIBUTE23 | — | — |
| 18 | ComponentAttribute24 | ATTRIBUTE24 | — | — |
| 19 | ComponentAttribute25 | ATTRIBUTE25 | — | — |
| 20 | ComponentAttribute26 | ATTRIBUTE26 | — | — |
| 21 | ComponentAttribute27 | ATTRIBUTE27 | — | — |
| 22 | ComponentAttribute28 | ATTRIBUTE28 | — | — |
| 23 | ComponentAttribute29 | ATTRIBUTE29 | — | — |
| 24 | ComponentAttribute3 | ATTRIBUTE3 | — | — |
| 25 | ComponentAttribute30 | ATTRIBUTE30 | — | — |
| 26 | ComponentAttribute4 | ATTRIBUTE4 | — | — |
| 27 | ComponentAttribute5 | ATTRIBUTE5 | — | — |
| 28 | ComponentAttribute6 | ATTRIBUTE6 | — | — |
| 29 | ComponentAttribute7 | ATTRIBUTE7 | — | — |
| 30 | ComponentAttribute8 | ATTRIBUTE8 | — | — |
| 31 | ComponentAttribute9 | ATTRIBUTE9 | — | — |
| 32 | ComponentAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | ComponentAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | ComponentAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 35 | ComponentAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 36 | ComponentAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 37 | ComponentAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 38 | ComponentAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 39 | ComponentAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 40 | ComponentAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 41 | ComponentAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 42 | ComponentAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 43 | ComponentAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 44 | ComponentAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 45 | ComponentAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 46 | ComponentAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 47 | ComponentAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 48 | ComponentAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 49 | ComponentAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 50 | ComponentAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 51 | ComponentAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 52 | ComponentAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 53 | ComponentAutoRequestMaterial | AUTO_REQUEST_MATERIAL | — | — |
| 54 | ComponentBasisType | BASIS_TYPE | — | — |
| 55 | ComponentBillSequenceId | BILL_SEQUENCE_ID | — | — |
| 56 | ComponentBomItemType | BOM_ITEM_TYPE | — | — |
| 57 | ComponentChangeId | CHANGE_ID | — | — |
| 58 | ComponentChangeLineId | CHANGE_LINE_ID | — | — |
| 59 | ComponentCheckAtp | CHECK_ATP | — | — |
| 60 | ComponentCommonComponentSequenceId | COMMON_COMPONENT_SEQUENCE_ID | — | — |
| 61 | ComponentCreatedBy | CREATED_BY | — | — |
| 62 | ComponentCreationDate | CREATION_DATE | — | — |
| 63 | ComponentDeleteGroupName | DELETE_GROUP_NAME | — | — |
| 64 | ComponentDgDescription | DG_DESCRIPTION | — | — |
| 65 | ComponentDisableDate | DISABLE_DATE | — | — |
| 66 | ComponentEffectivityDate | EFFECTIVITY_DATE | — | — |
| 67 | ComponentEnforceIntRequirements | ENFORCE_INT_REQUIREMENTS | — | — |
| 68 | ComponentFromEndItemRevId | FROM_END_ITEM_REV_ID | — | — |
| 69 | ComponentFromEndItemUnitNumber | FROM_END_ITEM_UNIT_NUMBER | — | — |
| 70 | ComponentHighQuantity | HIGH_QUANTITY | — | — |
| 71 | ComponentImplementationDate | IMPLEMENTATION_DATE | — | — |
| 72 | ComponentIncludeOnBillDocs | INCLUDE_ON_BILL_DOCS | — | — |
| 73 | ComponentIncludeOnShipDocs | INCLUDE_ON_SHIP_DOCS | — | — |
| 74 | ComponentInstantiabilityCode | INSTANTIABILITY_CODE | — | — |
| 75 | ComponentItemNum | ITEM_NUM | — | — |
| 76 | ComponentItemRevisionId | COMPONENT_ITEM_REVISION_ID | — | — |
| 77 | ComponentLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 78 | ComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 79 | ComponentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 80 | ComponentLowQuantity | LOW_QUANTITY | — | — |
| 81 | ComponentModelCompSeqId | MODEL_COMP_SEQ_ID | — | — |
| 82 | ComponentMutuallyExclusiveOptions | MUTUALLY_EXCLUSIVE_OPTIONS | — | — |
| 83 | ComponentObjName | OBJ_NAME | — | — |
| 84 | ComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 85 | ComponentOldComponentSequenceId | OLD_COMPONENT_SEQUENCE_ID | — | — |
| 86 | ComponentOperationLeadTimePercent | OPERATION_LEAD_TIME_PERCENT | — | — |
| 87 | ComponentOperationSeqNum | OPERATION_SEQ_NUM | — | — |
| 88 | ComponentOptional | OPTIONAL | — | — |
| 89 | ComponentOptionalOnModel | OPTIONAL_ON_MODEL | — | — |
| 90 | ComponentOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 91 | ComponentParentBillSeqId | PARENT_BILL_SEQ_ID | — | — |
| 92 | ComponentPickComponents | PICK_COMPONENTS | — | — |
| 93 | ComponentPk1Value | PK1_VALUE | — | — |
| 94 | ComponentPk2Value | PK2_VALUE | — | — |
| 95 | ComponentPk3Value | PK3_VALUE | — | — |
| 96 | ComponentPk4Value | PK4_VALUE | — | — |
| 97 | ComponentPk5Value | PK5_VALUE | — | — |
| 98 | ComponentPlanLevel | PLAN_LEVEL | — | — |
| 99 | ComponentPlanningFactor | PLANNING_FACTOR | — | — |
| 100 | ComponentPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 101 | ComponentProgramAppName | PROGRAM_APP_NAME | — | — |
| 102 | ComponentProgramName | PROGRAM_NAME | — | — |
| 103 | ComponentQuantity | COMPONENT_QUANTITY | — | — |
| 104 | ComponentQuantityRelated | QUANTITY_RELATED | — | — |
| 105 | ComponentRemarks | COMPONENT_REMARKS | — | — |
| 106 | ComponentRequestId | REQUEST_ID | — | — |
| 107 | ComponentRequiredForRevenue | REQUIRED_FOR_REVENUE | — | — |
| 108 | ComponentRequiredToShip | REQUIRED_TO_SHIP | — | — |
| 109 | ComponentSequenceId1 | COMPONENT_SEQUENCE_ID | — | — |
| 110 | ComponentShippingAllowed | SHIPPING_ALLOWED | — | — |
| 111 | ComponentShowInSales | SHOW_IN_SALES | — | — |
| 112 | ComponentSoBasis | SO_BASIS | — | — |
| 113 | ComponentSuggestedOperationSeqNum | SUGGESTED_OPERATION_SEQ_NUM | — | — |
| 114 | ComponentSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | — |
| 115 | ComponentSupplyLocatorId | SUPPLY_LOCATOR_ID | — | — |
| 116 | ComponentSupplySubinventory | SUPPLY_SUBINVENTORY | — | — |
| 117 | ComponentToEndItemRevId | TO_END_ITEM_REV_ID | — | — |
| 118 | ComponentToEndItemUnitNumber | TO_END_ITEM_UNIT_NUMBER | — | — |
| 119 | ComponentUnitPrice | UNIT_PRICE | — | — |
| 120 | ComponentUsePlaceholder | USE_PLACEHOLDER | — | — |
| 121 | ComponentVendorId | VENDOR_ID | — | — |
| 122 | ComponentWipSupplyType | WIP_SUPPLY_TYPE | — | — |
| 123 | ComponentYieldFactor | COMPONENT_YIELD_FACTOR | — | — |

### [[egp_reference_designators|EGP_REFERENCE_DESIGNATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcdType | ACD_TYPE | — | ✅ |
| 2 | ComponentReferenceDesignator | COMPONENT_REFERENCE_DESIGNATOR | — | ✅ |
| 3 | ComponentSequenceId | COMPONENT_SEQUENCE_ID | — | ✅ |
| 4 | ReferenceDesignatorPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 5 | ReferenceDesignatorPEOChangeNotice | CHANGE_NOTICE | — | — |
| 6 | ReferenceDesignatorPEOCommonComponentSequenceId | COMMON_COMPONENT_SEQUENCE_ID | — | — |
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
| 18 | ReferenceDesignatorPEORefDesigSequenceId | REF_DESIG_SEQUENCE_ID | 🔑 | ✅ |
| 19 | ReferenceDesignatorPEORefDesignatorComment | REF_DESIGNATOR_COMMENT | — | ✅ |
| 20 | ReferenceDesignatorPEORequestId | REQUEST_ID | — | — |
| 21 | ReferenceDesignatorPEOVersionId | VERSION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
