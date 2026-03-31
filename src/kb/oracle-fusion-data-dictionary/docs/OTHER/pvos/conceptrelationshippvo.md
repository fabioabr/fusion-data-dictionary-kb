---
id: DOC-OTHER-PVO-ConceptRelationshipPVO
doc_type: system-doc
title: "ConceptRelationshipPVO — PVO Cross-Module"
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
  - ConceptRelationshipPVO
  - conceptrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptRelationshipPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Concept Relationship. Acessa as tabelas: ACD_COMPONENT_VL, ACD_CONCEPTS_PROJ_TASKS_V, ACD_CONCEPTS_RELATIONSHIP_V (+11).

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.ConceptRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 408 | 14 | 1 | 320 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[acd_component_vl|ACD_COMPONENT_VL]] — 15 atributos (15 BICC)
- [[acd_concepts_proj_tasks_v|ACD_CONCEPTS_PROJ_TASKS_V]] — 2 atributos (2 BICC)
- [[acd_concepts_relationship_v|ACD_CONCEPTS_RELATIONSHIP_V]] — 22 atributos (1 PKs, 22 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 35 atributos (35 BICC)
- [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]] — 180 atributos (123 BICC)
- [[acd_concept_str_concepts_v|ACD_CONCEPT_STR_CONCEPTS_V]] — 4 atributos (4 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 22 atributos (20 BICC)
- [[acd_concept_vl|ACD_CONCEPT_VL]] — 19 atributos (3 BICC)
- [[acd_metrics|ACD_METRICS]] — 40 atributos (40 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 13 atributos (13 BICC)
- [[acn_idea_vl|ACN_IDEA_VL]] — 12 atributos (11 BICC)
- [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]] — 19 atributos (19 BICC)
- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 11 atributos (11 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 14 atributos (2 BICC)

---

## ⚙️ Atributos

### [[acd_component_vl|ACD_COMPONENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelComponentComponentId | COMPONENT_ID | — | ✅ |
| 2 | RelComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 3 | RelComponentCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelComponentCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelComponentDescription | DESCRIPTION | — | ✅ |
| 6 | RelComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RelComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RelComponentMaterial | MATERIAL | — | ✅ |
| 10 | RelComponentName | NAME | — | ✅ |
| 11 | RelComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | RelComponentSupplier | SUPPLIER | — | ✅ |
| 13 | RelComponentTargetType | TARGET_TYPE | — | ✅ |
| 14 | RelComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 15 | RelComponentType | TYPE | — | ✅ |

### [[acd_concepts_proj_tasks_v|ACD_CONCEPTS_PROJ_TASKS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelConceptProjTaskConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 2 | RelConceptProjTaskTaskidcount | TASKIDCOUNT | — | ✅ |

### [[acd_concepts_relationship_v|ACD_CONCEPTS_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptsRelationshipCreatedBy | CREATED_BY | — | ✅ |
| 2 | ConceptsRelationshipCreationDate | CREATION_DATE | — | ✅ |
| 3 | ConceptsRelationshipDerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 4 | ConceptsRelationshipDerivedIdeaId | DERIVED_IDEA_ID | — | ✅ |
| 5 | ConceptsRelationshipDerivedItemId | DERIVED_ITEM_ID | — | ✅ |
| 6 | ConceptsRelationshipDerivedProjectsId | DERIVED_PROJECTS_ID | — | ✅ |
| 7 | ConceptsRelationshipDerivedProposalId | DERIVED_PROPOSAL_ID | — | ✅ |
| 8 | ConceptsRelationshipDerivedRequirementId | DERIVED_REQUIREMENT_ID | — | ✅ |
| 9 | ConceptsRelationshipDerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 10 | ConceptsRelationshipDestObjId | DEST_OBJ_ID | — | ✅ |
| 11 | ConceptsRelationshipDestObjType | DEST_OBJ_TYPE | — | ✅ |
| 12 | ConceptsRelationshipDirectionType | DIRECTION_TYPE | — | ✅ |
| 13 | ConceptsRelationshipFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 14 | ConceptsRelationshipFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 15 | ConceptsRelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ConceptsRelationshipLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ConceptsRelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ConceptsRelationshipRelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 19 | ConceptsRelationshipRelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 20 | ConceptsRelationshipSrcObjId | SRC_OBJ_ID | — | ✅ |
| 21 | ConceptsRelationshipSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 22 | ConceptsRelationshipTargetType | TARGET_TYPE | — | ✅ |

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedConceptBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | DerivedConceptBaseConceptId | CONCEPT_ID | — | ✅ |
| 3 | DerivedConceptBaseCreatedBy | CREATED_BY | — | ✅ |
| 4 | DerivedConceptBaseCreationDate | CREATION_DATE | — | ✅ |
| 5 | DerivedConceptBaseCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | DerivedConceptBaseDueDate | DUE_DATE | — | ✅ |
| 7 | DerivedConceptBaseIsCurrent | IS_CURRENT | — | ✅ |
| 8 | DerivedConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DerivedConceptBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | DerivedConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DerivedConceptBaseLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 12 | DerivedConceptBaseMasterId | MASTER_ID | — | ✅ |
| 13 | DerivedConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | DerivedConceptBasePowerUnit | POWER_UNIT | — | ✅ |
| 15 | DerivedConceptBaseType | TYPE | — | ✅ |
| 16 | DerivedConceptBaseVersion | VERSION | — | ✅ |
| 17 | DerivedConceptBaseVolume | VOLUME | — | ✅ |
| 18 | DrivingConceptBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 19 | DrivingConceptBaseConceptId | CONCEPT_ID | — | ✅ |
| 20 | DrivingConceptBaseConceptNumber | CONCEPT_NUMBER | — | ✅ |
| 21 | DrivingConceptBaseCreatedBy | CREATED_BY | — | ✅ |
| 22 | DrivingConceptBaseCreationDate | CREATION_DATE | — | ✅ |
| 23 | DrivingConceptBaseCurrencyCode | CURRENCY_CODE | — | ✅ |
| 24 | DrivingConceptBaseDueDate | DUE_DATE | — | ✅ |
| 25 | DrivingConceptBaseIsCurrent | IS_CURRENT | — | ✅ |
| 26 | DrivingConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | DrivingConceptBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | DrivingConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | DrivingConceptBaseLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 30 | DrivingConceptBaseMasterId | MASTER_ID | — | ✅ |
| 31 | DrivingConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | DrivingConceptBasePowerUnit | POWER_UNIT | — | ✅ |
| 33 | DrivingConceptBaseType | TYPE | — | ✅ |
| 34 | DrivingConceptBaseVersion | VERSION | — | ✅ |
| 35 | DrivingConceptBaseVolume | VOLUME | — | ✅ |

### [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompStructureActualCost | ACTUAL_COST | — | — |
| 2 | CompStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | — |
| 3 | CompStructureActualWeight | ACTUAL_WEIGHT | — | — |
| 4 | CompStructureAlternate | ALTERNATE | — | — |
| 5 | CompStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | — |
| 6 | CompStructureAvailability | AVAILABILITY | — | — |
| 7 | CompStructureCompliance | COMPLIANCE | — | — |
| 8 | CompStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 9 | CompStructureCostIncomplete | COST_INCOMPLETE | — | — |
| 10 | CompStructureCostNotes | COST_NOTES | — | — |
| 11 | CompStructureCostVariance | COST_VARIANCE | — | — |
| 12 | CompStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | — |
| 13 | CompStructureCreatedBy | CREATED_BY | — | — |
| 14 | CompStructureCreationDate | CREATION_DATE | — | — |
| 15 | CompStructureFromId | FROM_ID | — | — |
| 16 | CompStructureFromStrId | FROM_STR_ID | — | — |
| 17 | CompStructureFromType | FROM_TYPE | — | — |
| 18 | CompStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | — |
| 19 | CompStructureLastCostUpdate | LAST_COST_UPDATE | — | — |
| 20 | CompStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CompStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | CompStructureLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CompStructureLeadTime | LEAD_TIME | — | — |
| 24 | CompStructureLocation | LOCATION | — | — |
| 25 | CompStructureMaterial | MATERIAL | — | — |
| 26 | CompStructureMaterialCost | MATERIAL_COST | — | — |
| 27 | CompStructureMorphedId | MORPHED_ID | — | — |
| 28 | CompStructureNonMaterialCost | NON_MATERIAL_COST | — | — |
| 29 | CompStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | — |
| 30 | CompStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | CompStructurePlaceholder | PLACEHOLDER | — | — |
| 32 | CompStructurePosNo | POS_NO | — | — |
| 33 | CompStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | — |
| 34 | CompStructurePowerIncomplete | POWER_INCOMPLETE | — | — |
| 35 | CompStructurePowerUnit | POWER_UNIT | — | — |
| 36 | CompStructurePreferredStatus | PREFERRED_STATUS | — | — |
| 37 | CompStructurePrice | PRICE | — | — |
| 38 | CompStructureQuantity | QUANTITY | — | — |
| 39 | CompStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | — |
| 40 | CompStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | — |
| 41 | CompStructureReqCountTotal | REQ_COUNT_TOTAL | — | — |
| 42 | CompStructureRisk | RISK | — | — |
| 43 | CompStructureScore | SCORE | — | — |
| 44 | CompStructureStatus | STATUS | — | — |
| 45 | CompStructureTargetCost | TARGET_COST | — | — |
| 46 | CompStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | — |
| 47 | CompStructureTargetWeight | TARGET_WEIGHT | — | — |
| 48 | CompStructureToId | TO_ID | — | ✅ |
| 49 | CompStructureToItemId | TO_ITEM_ID | — | — |
| 50 | CompStructureToItemStrId | TO_ITEM_STR_ID | — | — |
| 51 | CompStructureToType | TO_TYPE | — | — |
| 52 | CompStructureTopConceptId | TOP_CONCEPT_ID | — | — |
| 53 | CompStructureUnitSize | UNIT_SIZE | — | — |
| 54 | CompStructureVendor | VENDOR | — | — |
| 55 | CompStructureVendorNotes | VENDOR_NOTES | — | — |
| 56 | CompStructureVolume | VOLUME | — | — |
| 57 | CompStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | — |
| 58 | CompStructureWeightQuality | WEIGHT_QUALITY | — | — |
| 59 | CompStructureWeightUnit | WEIGHT_UNIT | — | — |
| 60 | CompStructureWeightVariance | WEIGHT_VARIANCE | — | — |
| 61 | ConceptStructureDerivedActualCost | ACTUAL_COST | — | ✅ |
| 62 | ConceptStructureDerivedActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 63 | ConceptStructureDerivedActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 64 | ConceptStructureDerivedAlternate | ALTERNATE | — | ✅ |
| 65 | ConceptStructureDerivedAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 66 | ConceptStructureDerivedAvailability | AVAILABILITY | — | ✅ |
| 67 | ConceptStructureDerivedConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 68 | ConceptStructureDerivedCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 69 | ConceptStructureDerivedCostNotes | COST_NOTES | — | ✅ |
| 70 | ConceptStructureDerivedCostVariance | COST_VARIANCE | — | ✅ |
| 71 | ConceptStructureDerivedCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 72 | ConceptStructureDerivedCreatedBy | CREATED_BY | — | ✅ |
| 73 | ConceptStructureDerivedCreationDate | CREATION_DATE | — | ✅ |
| 74 | ConceptStructureDerivedFixedCost | FIXED_COST | — | ✅ |
| 75 | ConceptStructureDerivedFromId | FROM_ID | — | ✅ |
| 76 | ConceptStructureDerivedFromStrId | FROM_STR_ID | — | ✅ |
| 77 | ConceptStructureDerivedFromType | FROM_TYPE | — | ✅ |
| 78 | ConceptStructureDerivedItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 79 | ConceptStructureDerivedLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 80 | ConceptStructureDerivedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 81 | ConceptStructureDerivedLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 82 | ConceptStructureDerivedLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 83 | ConceptStructureDerivedLeadTime | LEAD_TIME | — | ✅ |
| 84 | ConceptStructureDerivedLocation | LOCATION | — | ✅ |
| 85 | ConceptStructureDerivedMaterial | MATERIAL | — | ✅ |
| 86 | ConceptStructureDerivedMaterialCost | MATERIAL_COST | — | ✅ |
| 87 | ConceptStructureDerivedMorphedId | MORPHED_ID | — | ✅ |
| 88 | ConceptStructureDerivedNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 89 | ConceptStructureDerivedNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 90 | ConceptStructureDerivedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 91 | ConceptStructureDerivedPlaceholder | PLACEHOLDER | — | ✅ |
| 92 | ConceptStructureDerivedPosNo | POS_NO | — | ✅ |
| 93 | ConceptStructureDerivedPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 94 | ConceptStructureDerivedPowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 95 | ConceptStructureDerivedPowerUnit | POWER_UNIT | — | ✅ |
| 96 | ConceptStructureDerivedPreferredStatus | PREFERRED_STATUS | — | ✅ |
| 97 | ConceptStructureDerivedPrice | PRICE | — | ✅ |
| 98 | ConceptStructureDerivedQuantity | QUANTITY | — | ✅ |
| 99 | ConceptStructureDerivedReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 100 | ConceptStructureDerivedReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 101 | ConceptStructureDerivedReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 102 | ConceptStructureDerivedRisk | RISK | — | ✅ |
| 103 | ConceptStructureDerivedScore | SCORE | — | ✅ |
| 104 | ConceptStructureDerivedStatus | STATUS | — | ✅ |
| 105 | ConceptStructureDerivedTargetCost | TARGET_COST | — | ✅ |
| 106 | ConceptStructureDerivedTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 107 | ConceptStructureDerivedTargetWeight | TARGET_WEIGHT | — | ✅ |
| 108 | ConceptStructureDerivedToId | TO_ID | — | ✅ |
| 109 | ConceptStructureDerivedToItemId | TO_ITEM_ID | — | ✅ |
| 110 | ConceptStructureDerivedToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 111 | ConceptStructureDerivedToType | TO_TYPE | — | ✅ |
| 112 | ConceptStructureDerivedTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 113 | ConceptStructureDerivedUnitSize | UNIT_SIZE | — | ✅ |
| 114 | ConceptStructureDerivedVendor | VENDOR | — | ✅ |
| 115 | ConceptStructureDerivedVendorNotes | VENDOR_NOTES | — | ✅ |
| 116 | ConceptStructureDerivedVolume | VOLUME | — | ✅ |
| 117 | ConceptStructureDerivedWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 118 | ConceptStructureDerivedWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 119 | ConceptStructureDerivedWeightUnit | WEIGHT_UNIT | — | ✅ |
| 120 | ConceptStructureDerivedWeightVariance | WEIGHT_VARIANCE | — | ✅ |
| 121 | ConceptStructureDrivingActualCost | ACTUAL_COST | — | ✅ |
| 122 | ConceptStructureDrivingActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 123 | ConceptStructureDrivingActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 124 | ConceptStructureDrivingAlternate | ALTERNATE | — | ✅ |
| 125 | ConceptStructureDrivingAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 126 | ConceptStructureDrivingAvailability | AVAILABILITY | — | ✅ |
| 127 | ConceptStructureDrivingConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 128 | ConceptStructureDrivingCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 129 | ConceptStructureDrivingCostNotes | COST_NOTES | — | ✅ |
| 130 | ConceptStructureDrivingCostVariance | COST_VARIANCE | — | ✅ |
| 131 | ConceptStructureDrivingCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 132 | ConceptStructureDrivingCreatedBy | CREATED_BY | — | ✅ |
| 133 | ConceptStructureDrivingCreationDate | CREATION_DATE | — | ✅ |
| 134 | ConceptStructureDrivingFixedCost | FIXED_COST | — | ✅ |
| 135 | ConceptStructureDrivingFromId | FROM_ID | — | ✅ |
| 136 | ConceptStructureDrivingFromStrId | FROM_STR_ID | — | ✅ |
| 137 | ConceptStructureDrivingFromType | FROM_TYPE | — | ✅ |
| 138 | ConceptStructureDrivingItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 139 | ConceptStructureDrivingLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 140 | ConceptStructureDrivingLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 141 | ConceptStructureDrivingLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 142 | ConceptStructureDrivingLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 143 | ConceptStructureDrivingLeadTime | LEAD_TIME | — | ✅ |
| 144 | ConceptStructureDrivingLocation | LOCATION | — | ✅ |
| 145 | ConceptStructureDrivingMaterial | MATERIAL | — | ✅ |
| 146 | ConceptStructureDrivingMaterialCost | MATERIAL_COST | — | ✅ |
| 147 | ConceptStructureDrivingMorphedId | MORPHED_ID | — | ✅ |
| 148 | ConceptStructureDrivingNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 149 | ConceptStructureDrivingNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 150 | ConceptStructureDrivingObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 151 | ConceptStructureDrivingPlaceholder | PLACEHOLDER | — | ✅ |
| 152 | ConceptStructureDrivingPosNo | POS_NO | — | ✅ |
| 153 | ConceptStructureDrivingPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 154 | ConceptStructureDrivingPowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 155 | ConceptStructureDrivingPowerUnit | POWER_UNIT | — | ✅ |
| 156 | ConceptStructureDrivingPreferredStatus | PREFERRED_STATUS | — | ✅ |
| 157 | ConceptStructureDrivingPrice | PRICE | — | ✅ |
| 158 | ConceptStructureDrivingQuantity | QUANTITY | — | ✅ |
| 159 | ConceptStructureDrivingReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 160 | ConceptStructureDrivingReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 161 | ConceptStructureDrivingReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 162 | ConceptStructureDrivingRisk | RISK | — | ✅ |
| 163 | ConceptStructureDrivingScore | SCORE | — | ✅ |
| 164 | ConceptStructureDrivingStatus | STATUS | — | ✅ |
| 165 | ConceptStructureDrivingTargetCost | TARGET_COST | — | ✅ |
| 166 | ConceptStructureDrivingTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 167 | ConceptStructureDrivingTargetWeight | TARGET_WEIGHT | — | ✅ |
| 168 | ConceptStructureDrivingToId | TO_ID | — | ✅ |
| 169 | ConceptStructureDrivingToItemId | TO_ITEM_ID | — | ✅ |
| 170 | ConceptStructureDrivingToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 171 | ConceptStructureDrivingToType | TO_TYPE | — | ✅ |
| 172 | ConceptStructureDrivingTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 173 | ConceptStructureDrivingUnitSize | UNIT_SIZE | — | ✅ |
| 174 | ConceptStructureDrivingVendor | VENDOR | — | ✅ |
| 175 | ConceptStructureDrivingVendorNotes | VENDOR_NOTES | — | ✅ |
| 176 | ConceptStructureDrivingVolume | VOLUME | — | ✅ |
| 177 | ConceptStructureDrivingWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 178 | ConceptStructureDrivingWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 179 | ConceptStructureDrivingWeightUnit | WEIGHT_UNIT | — | ✅ |
| 180 | ConceptStructureDrivingWeightVariance | WEIGHT_VARIANCE | — | ✅ |

### [[acd_concept_str_concepts_v|ACD_CONCEPT_STR_CONCEPTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedConceptStructureConceptId | CONCEPT_ID | — | ✅ |
| 2 | DerivedConceptStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 3 | DrivingConceptStructureConceptId | CONCEPT_ID | — | ✅ |
| 4 | DrivingConceptStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedConceptTranslationConceptId | CONCEPT_ID | — | ✅ |
| 2 | DerivedConceptTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | DerivedConceptTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | DerivedConceptTranslationDescription | DESCRIPTION | — | — |
| 5 | DerivedConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | DerivedConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DerivedConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | DerivedConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DerivedConceptTranslationName | NAME | — | ✅ |
| 10 | DerivedConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | DerivedConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 12 | DrivingConceptTranslationConceptId | CONCEPT_ID | — | ✅ |
| 13 | DrivingConceptTranslationCreatedBy | CREATED_BY | — | ✅ |
| 14 | DrivingConceptTranslationCreationDate | CREATION_DATE | — | ✅ |
| 15 | DrivingConceptTranslationDescription | DESCRIPTION | — | — |
| 16 | DrivingConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 17 | DrivingConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | DrivingConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | DrivingConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | DrivingConceptTranslationName | NAME | — | ✅ |
| 21 | DrivingConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | DrivingConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |

### [[acd_concept_vl|ACD_CONCEPT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptRelProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | — |
| 2 | ConceptRelProposalConceptId | CONCEPT_ID | — | — |
| 3 | ConceptRelProposalConceptRelProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ConceptRelProposalCreatedBy | CREATED_BY | — | — |
| 5 | ConceptRelProposalCreationDate | CREATION_DATE | — | — |
| 6 | ConceptRelProposalCurrencyCode | CURRENCY_CODE | — | — |
| 7 | ConceptRelProposalDescription | DESCRIPTION | — | ✅ |
| 8 | ConceptRelProposalDueDate | DUE_DATE | — | — |
| 9 | ConceptRelProposalIsCurrent | IS_CURRENT | — | — |
| 10 | ConceptRelProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ConceptRelProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ConceptRelProposalLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ConceptRelProposalLifecyclePhase | LIFECYCLE_PHASE | — | — |
| 14 | ConceptRelProposalMasterId | MASTER_ID | — | — |
| 15 | ConceptRelProposalName | NAME | — | ✅ |
| 16 | ConceptRelProposalNotes | NOTES | — | — |
| 17 | ConceptRelProposalType | TYPE | — | — |
| 18 | ConceptRelProposalVersion | VERSION | — | — |
| 19 | ConceptRelProposalVolume | VOLUME | — | — |

### [[acd_metrics|ACD_METRICS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedMetricsAlternativeIndex | ALTERNATIVE_INDEX | — | ✅ |
| 2 | DerivedMetricsCompliance | COMPLIANCE | — | ✅ |
| 3 | DerivedMetricsConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 4 | DerivedMetricsCost | COST | — | ✅ |
| 5 | DerivedMetricsCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 6 | DerivedMetricsCostVariance | COST_VARIANCE | — | ✅ |
| 7 | DerivedMetricsCreatedBy | CREATED_BY | — | ✅ |
| 8 | DerivedMetricsCreationDate | CREATION_DATE | — | ✅ |
| 9 | DerivedMetricsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | DerivedMetricsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | DerivedMetricsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | DerivedMetricsMetricsId | METRICS_ID | — | ✅ |
| 13 | DerivedMetricsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | DerivedMetricsPowerConsumption | POWER_CONSUMPTION | — | ✅ |
| 15 | DerivedMetricsPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 16 | DerivedMetricsPowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 17 | DerivedMetricsScore | SCORE | — | ✅ |
| 18 | DerivedMetricsWeight | WEIGHT | — | ✅ |
| 19 | DerivedMetricsWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 20 | DerivedMetricsWeightVariance | WEIGHT_VARIANCE | — | ✅ |
| 21 | DrivingMetricsAlternativeIndex | ALTERNATIVE_INDEX | — | ✅ |
| 22 | DrivingMetricsCompliance | COMPLIANCE | — | ✅ |
| 23 | DrivingMetricsConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 24 | DrivingMetricsCost | COST | — | ✅ |
| 25 | DrivingMetricsCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 26 | DrivingMetricsCostVariance | COST_VARIANCE | — | ✅ |
| 27 | DrivingMetricsCreatedBy | CREATED_BY | — | ✅ |
| 28 | DrivingMetricsCreationDate | CREATION_DATE | — | ✅ |
| 29 | DrivingMetricsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | DrivingMetricsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | DrivingMetricsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | DrivingMetricsMetricsId | METRICS_ID | — | ✅ |
| 33 | DrivingMetricsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 34 | DrivingMetricsPowerConsumption | POWER_CONSUMPTION | — | ✅ |
| 35 | DrivingMetricsPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 36 | DrivingMetricsPowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 37 | DrivingMetricsScore | SCORE | — | ✅ |
| 38 | DrivingMetricsWeight | WEIGHT | — | ✅ |
| 39 | DrivingMetricsWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 40 | DrivingMetricsWeightVariance | WEIGHT_VARIANCE | — | ✅ |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelProductProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelProductProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 3 | RelProductProposalCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelProductProposalCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelProductProposalIsCloned | IS_CLONED | — | ✅ |
| 6 | RelProductProposalIsLatest | IS_LATEST | — | ✅ |
| 7 | RelProductProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RelProductProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RelProductProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RelProductProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RelProductProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 12 | RelProductProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 13 | RelProductProposalVersion | VERSION | — | ✅ |

### [[acn_idea_vl|ACN_IDEA_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelIdeaAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelIdeaCreatedBy | CREATED_BY | — | ✅ |
| 3 | RelIdeaCreationDate | CREATION_DATE | — | ✅ |
| 4 | RelIdeaDescription | DESCRIPTION | — | — |
| 5 | RelIdeaIdeaId | IDEA_ID | — | ✅ |
| 6 | RelIdeaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelIdeaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RelIdeaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RelIdeaName | NAME | — | ✅ |
| 10 | RelIdeaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RelIdeaStatus | STATUS | — | ✅ |
| 12 | RelIdeaType | TYPE | — | ✅ |

### [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelReqLineItemBaseLineItemId | BASE_LINE_ITEM_ID | — | ✅ |
| 2 | RelReqLineItemContent | CONTENT | — | ✅ |
| 3 | RelReqLineItemCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelReqLineItemCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelReqLineItemEstimates | ESTIMATES | — | ✅ |
| 6 | RelReqLineItemFulfilled | FULFILLED | — | ✅ |
| 7 | RelReqLineItemLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RelReqLineItemLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RelReqLineItemLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RelReqLineItemName | NAME | — | ✅ |
| 11 | RelReqLineItemObjectId | OBJECT_ID | — | ✅ |
| 12 | RelReqLineItemObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | RelReqLineItemParentLineItemId | PARENT_LINE_ITEM_ID | — | ✅ |
| 14 | RelReqLineItemPriority | PRIORITY | — | ✅ |
| 15 | RelReqLineItemRequirementLineItemId | REQUIREMENT_LINE_ITEM_ID | — | ✅ |
| 16 | RelReqLineItemRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 17 | RelReqLineItemScope | SCOPE | — | ✅ |
| 18 | RelReqLineItemSectionCode | SECTION_CODE | — | ✅ |
| 19 | RelReqLineItemSectionNumber | SECTION_NUMBER | — | ✅ |

### [[acn_requirement_vl|ACN_REQUIREMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelRequirementAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelRequirementCreatedBy | CREATED_BY | — | ✅ |
| 3 | RelRequirementCreationDate | CREATION_DATE | — | ✅ |
| 4 | RelRequirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RelRequirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RelRequirementLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RelRequirementLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 8 | RelRequirementName | NAME | — | ✅ |
| 9 | RelRequirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RelRequirementRequirementId | REQUIREMENT_ID | — | ✅ |
| 11 | RelRequirementType | TYPE | — | ✅ |

### [[acn_req_version_vl|ACN_REQ_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptRelProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RelRequirementVersionCreatedBy | CREATED_BY | — | — |
| 3 | RelRequirementVersionCreationDate | CREATION_DATE | — | — |
| 4 | RelRequirementVersionDescription | DESCRIPTION | — | — |
| 5 | RelRequirementVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RelRequirementVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RelRequirementVersionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RelRequirementVersionProduct | PRODUCT | — | — |
| 9 | RelRequirementVersionRequirementId | REQUIREMENT_ID | — | — |
| 10 | RelRequirementVersionRequirementVersionId | REQUIREMENT_VERSION_ID | — | — |
| 11 | RelRequirementVersionStatus | STATUS | — | ✅ |
| 12 | RelRequirementVersionStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 13 | RelRequirementVersionTotalEstimates | TOTAL_ESTIMATES | — | — |
| 14 | RelRequirementVersionVersionNumber | VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
