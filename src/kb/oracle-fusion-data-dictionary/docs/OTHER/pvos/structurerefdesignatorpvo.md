---
id: DOC-OTHER-PVO-StructureRefDesignatorPVO
doc_type: system-doc
title: "StructureRefDesignatorPVO — PVO Cross-Module"
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
  - StructureRefDesignatorPVO
  - structurerefdesignatorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StructureRefDesignatorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Structure Ref Designator. Acessa as tabelas: ACA_STRUCTURE_REF_DESIGNATOR_V, EGP_COMPONENTS_B.

**Caminho:** `FscmTopModelAM.EgpStructuresPublicModelAM.StructureRefDesignatorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 2 | 1 | 2 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[aca_structure_ref_designator_v|ACA_STRUCTURE_REF_DESIGNATOR_V]] — 2 atributos (1 PKs, 2 BICC)
- [[egp_components_b|EGP_COMPONENTS_B]] — 123 atributos

---

## ⚙️ Atributos

### [[aca_structure_ref_designator_v|ACA_STRUCTURE_REF_DESIGNATOR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StructureRefDesignatorComponentSequenceId | COMPONENT_SEQUENCE_ID | 🔑 | ✅ |
| 2 | StructureRefDesignatorReferenceDesignatorStr | REFERENCE_DESIGNATOR_STR | — | ✅ |

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
| 61 | ComponentComponentItemRevisionId | COMPONENT_ITEM_REVISION_ID | — | — |
| 62 | ComponentComponentQuantity | COMPONENT_QUANTITY | — | — |
| 63 | ComponentComponentRemarks | COMPONENT_REMARKS | — | — |
| 64 | ComponentComponentSequenceId | COMPONENT_SEQUENCE_ID | — | — |
| 65 | ComponentComponentYieldFactor | COMPONENT_YIELD_FACTOR | — | — |
| 66 | ComponentCreatedBy | CREATED_BY | — | — |
| 67 | ComponentCreationDate | CREATION_DATE | — | — |
| 68 | ComponentDeleteGroupName | DELETE_GROUP_NAME | — | — |
| 69 | ComponentDgDescription | DG_DESCRIPTION | — | — |
| 70 | ComponentDisableDate | DISABLE_DATE | — | — |
| 71 | ComponentEffectivityDate | EFFECTIVITY_DATE | — | — |
| 72 | ComponentEnforceIntRequirements | ENFORCE_INT_REQUIREMENTS | — | — |
| 73 | ComponentFromEndItemRevId | FROM_END_ITEM_REV_ID | — | — |
| 74 | ComponentFromEndItemUnitNumber | FROM_END_ITEM_UNIT_NUMBER | — | — |
| 75 | ComponentHighQuantity | HIGH_QUANTITY | — | — |
| 76 | ComponentImplementationDate | IMPLEMENTATION_DATE | — | — |
| 77 | ComponentIncludeOnBillDocs | INCLUDE_ON_BILL_DOCS | — | — |
| 78 | ComponentIncludeOnShipDocs | INCLUDE_ON_SHIP_DOCS | — | — |
| 79 | ComponentInstantiabilityCode | INSTANTIABILITY_CODE | — | — |
| 80 | ComponentItemNum | ITEM_NUM | — | — |
| 81 | ComponentLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 82 | ComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 83 | ComponentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 84 | ComponentLowQuantity | LOW_QUANTITY | — | — |
| 85 | ComponentModelCompSeqId | MODEL_COMP_SEQ_ID | — | — |
| 86 | ComponentMutuallyExclusiveOptions | MUTUALLY_EXCLUSIVE_OPTIONS | — | — |
| 87 | ComponentObjName | OBJ_NAME | — | — |
| 88 | ComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 89 | ComponentOldComponentSequenceId | OLD_COMPONENT_SEQUENCE_ID | — | — |
| 90 | ComponentOperationLeadTimePercent | OPERATION_LEAD_TIME_PERCENT | — | — |
| 91 | ComponentOperationSeqNum | OPERATION_SEQ_NUM | — | — |
| 92 | ComponentOptional | OPTIONAL | — | — |
| 93 | ComponentOptionalOnModel | OPTIONAL_ON_MODEL | — | — |
| 94 | ComponentOriginalSystemReference | ORIGINAL_SYSTEM_REFERENCE | — | — |
| 95 | ComponentParentBillSeqId | PARENT_BILL_SEQ_ID | — | — |
| 96 | ComponentPickComponents | PICK_COMPONENTS | — | — |
| 97 | ComponentPk1Value | PK1_VALUE | — | — |
| 98 | ComponentPk2Value | PK2_VALUE | — | — |
| 99 | ComponentPk3Value | PK3_VALUE | — | — |
| 100 | ComponentPk4Value | PK4_VALUE | — | — |
| 101 | ComponentPk5Value | PK5_VALUE | — | — |
| 102 | ComponentPlanLevel | PLAN_LEVEL | — | — |
| 103 | ComponentPlanningFactor | PLANNING_FACTOR | — | — |
| 104 | ComponentPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 105 | ComponentProgramAppName | PROGRAM_APP_NAME | — | — |
| 106 | ComponentProgramName | PROGRAM_NAME | — | — |
| 107 | ComponentQuantityRelated | QUANTITY_RELATED | — | — |
| 108 | ComponentRequestId | REQUEST_ID | — | — |
| 109 | ComponentRequiredForRevenue | REQUIRED_FOR_REVENUE | — | — |
| 110 | ComponentRequiredToShip | REQUIRED_TO_SHIP | — | — |
| 111 | ComponentShippingAllowed | SHIPPING_ALLOWED | — | — |
| 112 | ComponentShowInSales | SHOW_IN_SALES | — | — |
| 113 | ComponentSoBasis | SO_BASIS | — | — |
| 114 | ComponentSuggestedOperationSeqNum | SUGGESTED_OPERATION_SEQ_NUM | — | — |
| 115 | ComponentSuggestedVendorName | SUGGESTED_VENDOR_NAME | — | — |
| 116 | ComponentSupplyLocatorId | SUPPLY_LOCATOR_ID | — | — |
| 117 | ComponentSupplySubinventory | SUPPLY_SUBINVENTORY | — | — |
| 118 | ComponentToEndItemRevId | TO_END_ITEM_REV_ID | — | — |
| 119 | ComponentToEndItemUnitNumber | TO_END_ITEM_UNIT_NUMBER | — | — |
| 120 | ComponentUnitPrice | UNIT_PRICE | — | — |
| 121 | ComponentUsePlaceholder | USE_PLACEHOLDER | — | — |
| 122 | ComponentVendorId | VENDOR_ID | — | — |
| 123 | ComponentWipSupplyType | WIP_SUPPLY_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
