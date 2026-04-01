---
id: DOC-HCM-PVO-RequirementRelationshipPVO
doc_type: system-doc
title: "RequirementRelationshipPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequirementRelationshipPVO
  - requirementrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementRelationshipPVO

## 📌 Visão Geral

Extrai relacionamentos entre requisitos, componentes e propostas de produto. Mapeia dependências entre requisitos funcionais no ciclo de desenvolvimento de produtos.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.RequirementRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 282 | 9 | 1 | 274 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[acd_component_vl|ACD_COMPONENT_VL]] — 30 atributos (28 BICC)
- [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]] — 122 atributos (122 BICC)
- [[acd_concept_vl|ACD_CONCEPT_VL]] — 14 atributos (13 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 13 atributos (13 BICC)
- [[acn_idea_vl|ACN_IDEA_VL]] — 12 atributos (11 BICC)
- [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]] — 21 atributos (21 BICC)
- [[acn_requirement_relationship_v|ACN_REQUIREMENT_RELATIONSHIP_V]] — 20 atributos (1 PKs, 20 BICC)
- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 22 atributos (22 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 28 atributos (24 BICC)

---

## ⚙️ Atributos

### [[acd_component_vl|ACD_COMPONENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompRelComponentComponentId | COMPONENT_ID | — | ✅ |
| 2 | CompRelComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 3 | CompRelComponentCreatedBy | CREATED_BY | — | ✅ |
| 4 | CompRelComponentCreationDate | CREATION_DATE | — | ✅ |
| 5 | CompRelComponentDescription | DESCRIPTION | — | — |
| 6 | CompRelComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CompRelComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CompRelComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CompRelComponentMaterial | MATERIAL | — | ✅ |
| 10 | CompRelComponentName | NAME | — | ✅ |
| 11 | CompRelComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | CompRelComponentSupplier | SUPPLIER | — | ✅ |
| 13 | CompRelComponentTargetType | TARGET_TYPE | — | ✅ |
| 14 | CompRelComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 15 | CompRelComponentType | TYPE | — | ✅ |
| 16 | RelComponentComponentId | COMPONENT_ID | — | ✅ |
| 17 | RelComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 18 | RelComponentCreatedBy | CREATED_BY | — | ✅ |
| 19 | RelComponentCreationDate | CREATION_DATE | — | ✅ |
| 20 | RelComponentDescription | DESCRIPTION | — | — |
| 21 | RelComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | RelComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | RelComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | RelComponentMaterial | MATERIAL | — | ✅ |
| 25 | RelComponentName | NAME | — | ✅ |
| 26 | RelComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | RelComponentSupplier | SUPPLIER | — | ✅ |
| 28 | RelComponentTargetType | TARGET_TYPE | — | ✅ |
| 29 | RelComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 30 | RelComponentType | TYPE | — | ✅ |

### [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompStructureActualCost | ACTUAL_COST | — | ✅ |
| 2 | CompStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 3 | CompStructureActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 4 | CompStructureAlternate | ALTERNATE | — | ✅ |
| 5 | CompStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 6 | CompStructureAvailability | AVAILABILITY | — | ✅ |
| 7 | CompStructureCompStructurePowerUnit | POWER_UNIT | — | ✅ |
| 8 | CompStructureCompliance | COMPLIANCE | — | ✅ |
| 9 | CompStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 10 | CompStructureCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 11 | CompStructureCostNotes | COST_NOTES | — | ✅ |
| 12 | CompStructureCostVariance | COST_VARIANCE | — | ✅ |
| 13 | CompStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 14 | CompStructureCreatedBy | CREATED_BY | — | ✅ |
| 15 | CompStructureCreationDate | CREATION_DATE | — | ✅ |
| 16 | CompStructureFixedCost | FIXED_COST | — | ✅ |
| 17 | CompStructureFromId | FROM_ID | — | ✅ |
| 18 | CompStructureFromStrId | FROM_STR_ID | — | ✅ |
| 19 | CompStructureFromType | FROM_TYPE | — | ✅ |
| 20 | CompStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 21 | CompStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 22 | CompStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CompStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CompStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CompStructureLeadTime | LEAD_TIME | — | ✅ |
| 26 | CompStructureLocation | LOCATION | — | ✅ |
| 27 | CompStructureMaterial | MATERIAL | — | ✅ |
| 28 | CompStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 29 | CompStructureMorphedId | MORPHED_ID | — | ✅ |
| 30 | CompStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 31 | CompStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 32 | CompStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | CompStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 34 | CompStructurePosNo | POS_NO | — | ✅ |
| 35 | CompStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 36 | CompStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 37 | CompStructurePreferredStatus | PREFERRED_STATUS | — | ✅ |
| 38 | CompStructurePrice | PRICE | — | ✅ |
| 39 | CompStructureQuantity | QUANTITY | — | ✅ |
| 40 | CompStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 41 | CompStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 42 | CompStructureReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 43 | CompStructureRisk | RISK | — | ✅ |
| 44 | CompStructureScore | SCORE | — | ✅ |
| 45 | CompStructureStatus | STATUS | — | ✅ |
| 46 | CompStructureTargetCost | TARGET_COST | — | ✅ |
| 47 | CompStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 48 | CompStructureTargetWeight | TARGET_WEIGHT | — | ✅ |
| 49 | CompStructureToId | TO_ID | — | ✅ |
| 50 | CompStructureToItemId | TO_ITEM_ID | — | ✅ |
| 51 | CompStructureToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 52 | CompStructureToType | TO_TYPE | — | ✅ |
| 53 | CompStructureTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 54 | CompStructureUnitSize | UNIT_SIZE | — | ✅ |
| 55 | CompStructureVendor | VENDOR | — | ✅ |
| 56 | CompStructureVendorNotes | VENDOR_NOTES | — | ✅ |
| 57 | CompStructureVolume | VOLUME | — | ✅ |
| 58 | CompStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 59 | CompStructureWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 60 | CompStructureWeightUnit | WEIGHT_UNIT | — | ✅ |
| 61 | CompStructureWeightVariance | WEIGHT_VARIANCE | — | ✅ |
| 62 | ConceptStructureActualCost | ACTUAL_COST | — | ✅ |
| 63 | ConceptStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 64 | ConceptStructureActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 65 | ConceptStructureAlternate | ALTERNATE | — | ✅ |
| 66 | ConceptStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 67 | ConceptStructureAvailability | AVAILABILITY | — | ✅ |
| 68 | ConceptStructureCompliance | COMPLIANCE | — | ✅ |
| 69 | ConceptStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 70 | ConceptStructureCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 71 | ConceptStructureCostNotes | COST_NOTES | — | ✅ |
| 72 | ConceptStructureCostVariance | COST_VARIANCE | — | ✅ |
| 73 | ConceptStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 74 | ConceptStructureCreatedBy | CREATED_BY | — | ✅ |
| 75 | ConceptStructureCreationDate | CREATION_DATE | — | ✅ |
| 76 | ConceptStructureFixedCost | FIXED_COST | — | ✅ |
| 77 | ConceptStructureFromId | FROM_ID | — | ✅ |
| 78 | ConceptStructureFromStrId | FROM_STR_ID | — | ✅ |
| 79 | ConceptStructureFromType | FROM_TYPE | — | ✅ |
| 80 | ConceptStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 81 | ConceptStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 82 | ConceptStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | ConceptStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 84 | ConceptStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 85 | ConceptStructureLeadTime | LEAD_TIME | — | ✅ |
| 86 | ConceptStructureLocation | LOCATION | — | ✅ |
| 87 | ConceptStructureMaterial | MATERIAL | — | ✅ |
| 88 | ConceptStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 89 | ConceptStructureMorphedId | MORPHED_ID | — | ✅ |
| 90 | ConceptStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 91 | ConceptStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 92 | ConceptStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 93 | ConceptStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 94 | ConceptStructurePosNo | POS_NO | — | ✅ |
| 95 | ConceptStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 96 | ConceptStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 97 | ConceptStructurePowerUnit | POWER_UNIT | — | ✅ |
| 98 | ConceptStructurePreferredStatus | PREFERRED_STATUS | — | ✅ |
| 99 | ConceptStructurePrice | PRICE | — | ✅ |
| 100 | ConceptStructureQuantity | QUANTITY | — | ✅ |
| 101 | ConceptStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 102 | ConceptStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 103 | ConceptStructureReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 104 | ConceptStructureRisk | RISK | — | ✅ |
| 105 | ConceptStructureScore | SCORE | — | ✅ |
| 106 | ConceptStructureStatus | STATUS | — | ✅ |
| 107 | ConceptStructureTargetCost | TARGET_COST | — | ✅ |
| 108 | ConceptStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 109 | ConceptStructureTargetWeight | TARGET_WEIGHT | — | ✅ |
| 110 | ConceptStructureToId | TO_ID | — | ✅ |
| 111 | ConceptStructureToItemId | TO_ITEM_ID | — | ✅ |
| 112 | ConceptStructureToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 113 | ConceptStructureToType | TO_TYPE | — | ✅ |
| 114 | ConceptStructureTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 115 | ConceptStructureUnitSize | UNIT_SIZE | — | ✅ |
| 116 | ConceptStructureVendor | VENDOR | — | ✅ |
| 117 | ConceptStructureVendorNotes | VENDOR_NOTES | — | ✅ |
| 118 | ConceptStructureVolume | VOLUME | — | ✅ |
| 119 | ConceptStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 120 | ConceptStructureWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 121 | ConceptStructureWeightUnit | WEIGHT_UNIT | — | ✅ |
| 122 | ConceptStructureWeightVariance | WEIGHT_VARIANCE | — | ✅ |

### [[acd_concept_vl|ACD_CONCEPT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelatedConceptConceptId | CONCEPT_ID | — | ✅ |
| 3 | RelatedConceptCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelatedConceptCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelatedConceptDescription | DESCRIPTION | — | — |
| 6 | RelatedConceptIsCurrent | IS_CURRENT | — | ✅ |
| 7 | RelatedConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RelatedConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RelatedConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RelatedConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 11 | RelatedConceptMasterId | MASTER_ID | — | ✅ |
| 12 | RelatedConceptName | NAME | — | ✅ |
| 13 | RelatedConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | RelatedConceptVersion | VERSION | — | ✅ |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelatedProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 3 | RelatedProposalCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelatedProposalCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelatedProposalIsCloned | IS_CLONED | — | ✅ |
| 6 | RelatedProposalIsLatest | IS_LATEST | — | ✅ |
| 7 | RelatedProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RelatedProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RelatedProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RelatedProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RelatedProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 12 | RelatedProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 13 | RelatedProposalVersion | VERSION | — | ✅ |

### [[acn_idea_vl|ACN_IDEA_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedIdeaAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelatedIdeaCreatedBy | CREATED_BY | — | ✅ |
| 3 | RelatedIdeaCreationDate | CREATION_DATE | — | ✅ |
| 4 | RelatedIdeaDescription | DESCRIPTION | — | — |
| 5 | RelatedIdeaIdeaId | IDEA_ID | — | ✅ |
| 6 | RelatedIdeaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelatedIdeaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RelatedIdeaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RelatedIdeaName | NAME | — | ✅ |
| 10 | RelatedIdeaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RelatedIdeaStatus | STATUS | — | ✅ |
| 12 | RelatedIdeaType | TYPE | — | ✅ |

### [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelReqLineItemBaseLineItemId | BASE_LINE_ITEM_ID | — | ✅ |
| 2 | RelReqLineItemContent | CONTENT | — | ✅ |
| 3 | RelReqLineItemCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelReqLineItemCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelReqLineItemDescription | DESCRIPTION | — | ✅ |
| 6 | RelReqLineItemEstimates | ESTIMATES | — | ✅ |
| 7 | RelReqLineItemFulfilled | FULFILLED | — | ✅ |
| 8 | RelReqLineItemLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RelReqLineItemLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | RelReqLineItemLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RelReqLineItemName | NAME | — | ✅ |
| 12 | RelReqLineItemObjectId | OBJECT_ID | — | ✅ |
| 13 | RelReqLineItemObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | RelReqLineItemParentLineItemId | PARENT_LINE_ITEM_ID | — | ✅ |
| 15 | RelReqLineItemPriority | PRIORITY | — | ✅ |
| 16 | RelReqLineItemRequirementLineItemId | REQUIREMENT_LINE_ITEM_ID | — | ✅ |
| 17 | RelReqLineItemRequirementLineItemId1 | REQUIREMENT_LINE_ITEM_ID | — | ✅ |
| 18 | RelReqLineItemRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 19 | RelReqLineItemScope | SCOPE | — | ✅ |
| 20 | RelReqLineItemSectionCode | SECTION_CODE | — | ✅ |
| 21 | RelReqLineItemSectionNumber | SECTION_NUMBER | — | ✅ |

### [[acn_requirement_relationship_v|ACN_REQUIREMENT_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementRelationshipCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementRelationshipCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementRelationshipDerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 4 | RequirementRelationshipDerivedConceptId | DERIVED_CONCEPT_ID | — | ✅ |
| 5 | RequirementRelationshipDerivedIdeaId | DERIVED_IDEA_ID | — | ✅ |
| 6 | RequirementRelationshipDerivedProposalId | DERIVED_PROPOSAL_ID | — | ✅ |
| 7 | RequirementRelationshipDerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 8 | RequirementRelationshipDestObjId | DEST_OBJ_ID | — | ✅ |
| 9 | RequirementRelationshipDestObjType | DEST_OBJ_TYPE | — | ✅ |
| 10 | RequirementRelationshipDirectionType | DIRECTION_TYPE | — | ✅ |
| 11 | RequirementRelationshipFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 12 | RequirementRelationshipFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 13 | RequirementRelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | RequirementRelationshipLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | RequirementRelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | RequirementRelationshipRelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 17 | RequirementRelationshipRelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 18 | RequirementRelationshipSrcObjId | SRC_OBJ_ID | — | ✅ |
| 19 | RequirementRelationshipSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 20 | RequirementRelationshipTargetType | TARGET_TYPE | — | ✅ |

### [[acn_requirement_vl|ACN_REQUIREMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedReqAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | DerivedReqCreatedBy | CREATED_BY | — | ✅ |
| 3 | DerivedReqCreationDate | CREATION_DATE | — | ✅ |
| 4 | DerivedReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DerivedReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | DerivedReqLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DerivedReqLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 8 | DerivedReqName | NAME | — | ✅ |
| 9 | DerivedReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | DerivedReqRequirementId | REQUIREMENT_ID | — | ✅ |
| 11 | DerivedReqType | TYPE | — | ✅ |
| 12 | DrivingReqAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 13 | DrivingReqCreatedBy | CREATED_BY | — | ✅ |
| 14 | DrivingReqCreationDate | CREATION_DATE | — | ✅ |
| 15 | DrivingReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | DrivingReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | DrivingReqLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | DrivingReqLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 19 | DrivingReqName | NAME | — | ✅ |
| 20 | DrivingReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | DrivingReqRequirementId | REQUIREMENT_ID | — | ✅ |
| 22 | DrivingReqType | TYPE | — | ✅ |

### [[acn_req_version_vl|ACN_REQ_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementVersionCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementVersionCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementVersionDerivedReqCreatedBy | CREATED_BY | — | ✅ |
| 4 | RequirementVersionDerivedReqCreationDate | CREATION_DATE | — | ✅ |
| 5 | RequirementVersionDerivedReqDescription | DESCRIPTION | — | — |
| 6 | RequirementVersionDerivedReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RequirementVersionDerivedReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RequirementVersionDerivedReqLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RequirementVersionDerivedReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RequirementVersionDerivedReqProduct | PRODUCT | — | ✅ |
| 11 | RequirementVersionDerivedReqRequirementId | REQUIREMENT_ID | — | ✅ |
| 12 | RequirementVersionDerivedReqRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 13 | RequirementVersionDerivedReqStatus | STATUS | — | ✅ |
| 14 | RequirementVersionDerivedReqStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 15 | RequirementVersionDerivedReqTotalEstimates | TOTAL_ESTIMATES | — | ✅ |
| 16 | RequirementVersionDerivedReqVersionNumber | VERSION_NUMBER | — | ✅ |
| 17 | RequirementVersionDescription | DESCRIPTION | — | — |
| 18 | RequirementVersionDrivingReqProduct | PRODUCT | — | ✅ |
| 19 | RequirementVersionDrivingReqStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 20 | RequirementVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | RequirementVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | RequirementVersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | RequirementVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | RequirementVersionRequirementId | REQUIREMENT_ID | — | ✅ |
| 25 | RequirementVersionRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 26 | RequirementVersionStatus | STATUS | — | ✅ |
| 27 | RequirementVersionVersionNumber | VERSION_NUMBER | — | ✅ |
| 28 | RequirmentVersionTotalEstimates | TOTAL_ESTIMATES | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
