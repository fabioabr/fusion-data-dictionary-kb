---
id: DOC-HCM-PVO-IdeaRelationshipPVO
doc_type: system-doc
title: "IdeaRelationshipPVO — PVO Human Capital Management"
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
  - IdeaRelationshipPVO
  - idearelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IdeaRelationshipPVO

## 📌 Visão Geral

Consolida relacionamentos de ideias com componentes, conceitos e propostas de produto. Utilizado em gestão de inovação e ideação corporativa.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.IdeaRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 314 | 13 | 1 | 295 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[acd_component_vl|ACD_COMPONENT_VL]] — 31 atributos (28 BICC)
- [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]] — 122 atributos (122 BICC)
- [[acd_concept_vl|ACD_CONCEPT_VL]] — 14 atributos (13 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 13 atributos (13 BICC)
- [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]] — 3 atributos (3 BICC)
- [[acn_idea_relationship_v|ACN_IDEA_RELATIONSHIP_V]] — 20 atributos (1 PKs, 20 BICC)
- [[acn_idea_tag|ACN_IDEA_TAG]] — 16 atributos (16 BICC)
- [[acn_idea_vl|ACN_IDEA_VL]] — 25 atributos (22 BICC)
- [[acn_idea_vote_summary_v|ACN_IDEA_VOTE_SUMMARY_V]] — 4 atributos (4 BICC)
- [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]] — 20 atributos (20 BICC)
- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 11 atributos (11 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 13 atributos (2 BICC)
- [[per_users|PER_USERS]] — 22 atributos (21 BICC)

---

## ⚙️ Atributos

### [[acd_component_vl|ACD_COMPONENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelCompComponentComponentId | COMPONENT_ID | — | ✅ |
| 2 | RelCompComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 3 | RelCompComponentCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelCompComponentCreationDate1 | CREATION_DATE | — | ✅ |
| 5 | RelCompComponentDescription | DESCRIPTION | — | — |
| 6 | RelCompComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RelCompComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RelCompComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RelCompComponentMaterial | MATERIAL | — | ✅ |
| 10 | RelCompComponentName | NAME | — | ✅ |
| 11 | RelCompComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | RelCompComponentSupplier | SUPPLIER | — | ✅ |
| 13 | RelCompComponentTargetType | TARGET_TYPE | — | ✅ |
| 14 | RelCompComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 15 | RelCompComponentType | TYPE | — | ✅ |
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
| 27 | RelComponentRowId1 | ROW_ID | — | — |
| 28 | RelComponentSupplier | SUPPLIER | — | ✅ |
| 29 | RelComponentTargetType | TARGET_TYPE | — | ✅ |
| 30 | RelComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 31 | RelComponentType | TYPE | — | ✅ |

### [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompStructureActualCost | ACTUAL_COST | — | ✅ |
| 2 | CompStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 3 | CompStructureActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 4 | CompStructureAlternate | ALTERNATE | — | ✅ |
| 5 | CompStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 6 | CompStructureAvailability | AVAILABILITY | — | ✅ |
| 7 | CompStructureCompliance | COMPLIANCE | — | ✅ |
| 8 | CompStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 9 | CompStructureCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 10 | CompStructureCostNotes | COST_NOTES | — | ✅ |
| 11 | CompStructureCostVariance | COST_VARIANCE | — | ✅ |
| 12 | CompStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 13 | CompStructureCreatedBy | CREATED_BY | — | ✅ |
| 14 | CompStructureFixedCost | FIXED_COST | — | ✅ |
| 15 | CompStructureFromId | FROM_ID | — | ✅ |
| 16 | CompStructureFromStrId | FROM_STR_ID | — | ✅ |
| 17 | CompStructureFromType | FROM_TYPE | — | ✅ |
| 18 | CompStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 19 | CompStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 20 | CompStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CompStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CompStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CompStructureLeadTime | LEAD_TIME | — | ✅ |
| 24 | CompStructureLocation | LOCATION | — | ✅ |
| 25 | CompStructureMaterial | MATERIAL | — | ✅ |
| 26 | CompStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 27 | CompStructureMorphedId | MORPHED_ID | — | ✅ |
| 28 | CompStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 29 | CompStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 30 | CompStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 31 | CompStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 32 | CompStructurePosNo | POS_NO | — | ✅ |
| 33 | CompStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 34 | CompStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 35 | CompStructurePowerUnit | POWER_UNIT | — | ✅ |
| 36 | CompStructurePreferredStatus | PREFERRED_STATUS | — | ✅ |
| 37 | CompStructurePrice | PRICE | — | ✅ |
| 38 | CompStructureQuantity | QUANTITY | — | ✅ |
| 39 | CompStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 40 | CompStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 41 | CompStructureReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 42 | CompStructureRisk | RISK | — | ✅ |
| 43 | CompStructureScore | SCORE | — | ✅ |
| 44 | CompStructureStatus | STATUS | — | ✅ |
| 45 | CompStructureTargetCost | TARGET_COST | — | ✅ |
| 46 | CompStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 47 | CompStructureTargetWeight | TARGET_WEIGHT | — | ✅ |
| 48 | CompStructureToId | TO_ID | — | ✅ |
| 49 | CompStructureToItemId | TO_ITEM_ID | — | ✅ |
| 50 | CompStructureToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 51 | CompStructureToType | TO_TYPE | — | ✅ |
| 52 | CompStructureTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 53 | CompStructureUnitSize | UNIT_SIZE | — | ✅ |
| 54 | CompStructureVendor | VENDOR | — | ✅ |
| 55 | CompStructureVendorNotes | VENDOR_NOTES | — | ✅ |
| 56 | CompStructureVolume | VOLUME | — | ✅ |
| 57 | CompStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 58 | CompStructureWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 59 | CompStructureWeightUnit | WEIGHT_UNIT | — | ✅ |
| 60 | CompStructureWeightVariance | WEIGHT_VARIANCE | — | ✅ |
| 61 | ConceptStructureActualCost | ACTUAL_COST | — | ✅ |
| 62 | ConceptStructureActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | ✅ |
| 63 | ConceptStructureActualWeight | ACTUAL_WEIGHT | — | ✅ |
| 64 | ConceptStructureAlternate | ALTERNATE | — | ✅ |
| 65 | ConceptStructureAnalyticsDirtyFlag | ANALYTICS_DIRTY_FLAG | — | ✅ |
| 66 | ConceptStructureAvailability | AVAILABILITY | — | ✅ |
| 67 | ConceptStructureCompliance | COMPLIANCE | — | ✅ |
| 68 | ConceptStructureConceptStructureId | CONCEPT_STRUCTURE_ID | — | ✅ |
| 69 | ConceptStructureCostIncomplete | COST_INCOMPLETE | — | ✅ |
| 70 | ConceptStructureCostNotes | COST_NOTES | — | ✅ |
| 71 | ConceptStructureCostVariance | COST_VARIANCE | — | ✅ |
| 72 | ConceptStructureCountryOfOrigin | COUNTRY_OF_ORIGIN | — | ✅ |
| 73 | ConceptStructureCreatedBy | CREATED_BY | — | ✅ |
| 74 | ConceptStructureCreationDate | CREATION_DATE | — | ✅ |
| 75 | ConceptStructureFixedCost | FIXED_COST | — | ✅ |
| 76 | ConceptStructureFromId | FROM_ID | — | ✅ |
| 77 | ConceptStructureFromStrId | FROM_STR_ID | — | ✅ |
| 78 | ConceptStructureFromType | FROM_TYPE | — | ✅ |
| 79 | ConceptStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 80 | ConceptStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 81 | ConceptStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 82 | ConceptStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 83 | ConceptStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 84 | ConceptStructureLeadTime | LEAD_TIME | — | ✅ |
| 85 | ConceptStructureLocation | LOCATION | — | ✅ |
| 86 | ConceptStructureMaterial | MATERIAL | — | ✅ |
| 87 | ConceptStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 88 | ConceptStructureMorphedId | MORPHED_ID | — | ✅ |
| 89 | ConceptStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 90 | ConceptStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 91 | ConceptStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 92 | ConceptStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 93 | ConceptStructurePosNo | POS_NO | — | ✅ |
| 94 | ConceptStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 95 | ConceptStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 96 | ConceptStructurePowerUnit | POWER_UNIT | — | ✅ |
| 97 | ConceptStructurePreferredStatus | PREFERRED_STATUS | — | ✅ |
| 98 | ConceptStructurePrice | PRICE | — | ✅ |
| 99 | ConceptStructureQuantity | QUANTITY | — | ✅ |
| 100 | ConceptStructureReferenceDesignator | REFERENCE_DESIGNATOR | — | ✅ |
| 101 | ConceptStructureReqCountFulfilled | REQ_COUNT_FULFILLED | — | ✅ |
| 102 | ConceptStructureReqCountTotal | REQ_COUNT_TOTAL | — | ✅ |
| 103 | ConceptStructureRisk | RISK | — | ✅ |
| 104 | ConceptStructureScore | SCORE | — | ✅ |
| 105 | ConceptStructureStatus | STATUS | — | ✅ |
| 106 | ConceptStructureTargetCost | TARGET_COST | — | ✅ |
| 107 | ConceptStructureTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | ✅ |
| 108 | ConceptStructureTargetWeight | TARGET_WEIGHT | — | ✅ |
| 109 | ConceptStructureToId | TO_ID | — | ✅ |
| 110 | ConceptStructureToItemId | TO_ITEM_ID | — | ✅ |
| 111 | ConceptStructureToItemStrId | TO_ITEM_STR_ID | — | ✅ |
| 112 | ConceptStructureToType | TO_TYPE | — | ✅ |
| 113 | ConceptStructureTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 114 | ConceptStructureUnitSize | UNIT_SIZE | — | ✅ |
| 115 | ConceptStructureVendor | VENDOR | — | ✅ |
| 116 | ConceptStructureVendorNotes | VENDOR_NOTES | — | ✅ |
| 117 | ConceptStructureVolume | VOLUME | — | ✅ |
| 118 | ConceptStructureWeightIncomplete | WEIGHT_INCOMPLETE | — | ✅ |
| 119 | ConceptStructureWeightQuality | WEIGHT_QUALITY | — | ✅ |
| 120 | ConceptStructureWeightUnit | WEIGHT_UNIT | — | ✅ |
| 121 | ConceptStructureWeightVariance | WEIGHT_VARIANCE | — | ✅ |
| 122 | CreationDate | CREATION_DATE | — | ✅ |

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

### [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IIdeaCommentdeaComment | IDEA_COMMENT | — | ✅ |
| 2 | IdeaCommentCommentLastUpdateDate | COMMENT_LAST_UPDATE_DATE | — | ✅ |
| 3 | IdeaCommentIdeaId | IDEA_ID | — | ✅ |

### [[acn_idea_relationship_v|ACN_IDEA_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaRelationshipCreatedBy | CREATED_BY | — | ✅ |
| 2 | IdeaRelationshipCreationDate | CREATION_DATE | — | ✅ |
| 3 | IdeaRelationshipDerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 4 | IdeaRelationshipDerivedConceptId | DERIVED_CONCEPT_ID | — | ✅ |
| 5 | IdeaRelationshipDerivedProposalId | DERIVED_PROPOSAL_ID | — | ✅ |
| 6 | IdeaRelationshipDerivedRequirementId | DERIVED_REQUIREMENT_ID | — | ✅ |
| 7 | IdeaRelationshipDerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 8 | IdeaRelationshipDestObjId | DEST_OBJ_ID | — | ✅ |
| 9 | IdeaRelationshipDestObjType | DEST_OBJ_TYPE | — | ✅ |
| 10 | IdeaRelationshipDirectionType | DIRECTION_TYPE | — | ✅ |
| 11 | IdeaRelationshipFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 12 | IdeaRelationshipFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 13 | IdeaRelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | IdeaRelationshipLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | IdeaRelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | IdeaRelationshipRelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 17 | IdeaRelationshipRelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 18 | IdeaRelationshipSrcObjId | SRC_OBJ_ID | — | ✅ |
| 19 | IdeaRelationshipSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 20 | IdeaRelationshipTargetType | TARGET_TYPE | — | ✅ |

### [[acn_idea_tag|ACN_IDEA_TAG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedIdeaTagCreatedBy | CREATED_BY | — | ✅ |
| 2 | DerivedIdeaTagCreationDate | CREATION_DATE | — | ✅ |
| 3 | DerivedIdeaTagIdeaId | IDEA_ID | — | ✅ |
| 4 | DerivedIdeaTagLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DerivedIdeaTagLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | DerivedIdeaTagLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DerivedIdeaTagName | NAME | — | ✅ |
| 8 | DerivedIdeaTagTagId | TAG_ID | — | ✅ |
| 9 | DrivingIdeaTagCreatedBy | CREATED_BY | — | ✅ |
| 10 | DrivingIdeaTagCreationDate | CREATION_DATE | — | ✅ |
| 11 | DrivingIdeaTagIdeaId | IDEA_ID | — | ✅ |
| 12 | DrivingIdeaTagLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DrivingIdeaTagLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | DrivingIdeaTagLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | DrivingIdeaTagName | NAME | — | ✅ |
| 16 | DrivingIdeaTagTagId | TAG_ID | — | ✅ |

### [[acn_idea_vl|ACN_IDEA_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedIdeaAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | DerivedIdeaCreatedBy | CREATED_BY | — | ✅ |
| 3 | DerivedIdeaCreationDate | CREATION_DATE | — | ✅ |
| 4 | DerivedIdeaDescription | DESCRIPTION | — | — |
| 5 | DerivedIdeaIdeaId | IDEA_ID | — | ✅ |
| 6 | DerivedIdeaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DerivedIdeaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | DerivedIdeaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DerivedIdeaName | NAME | — | ✅ |
| 10 | DerivedIdeaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | DerivedIdeaStatus | STATUS | — | ✅ |
| 12 | DerivedIdeaType | TYPE | — | ✅ |
| 13 | DrivingIdeaAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 14 | DrivingIdeaCreatedBy | CREATED_BY | — | ✅ |
| 15 | DrivingIdeaCreationDate | CREATION_DATE | — | ✅ |
| 16 | DrivingIdeaDescription | DESCRIPTION | — | — |
| 17 | DrivingIdeaIdeaId | IDEA_ID | — | ✅ |
| 18 | DrivingIdeaIdeaNumber | IDEA_NUMBER | — | — |
| 19 | DrivingIdeaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | DrivingIdeaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | DrivingIdeaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | DrivingIdeaName | NAME | — | ✅ |
| 23 | DrivingIdeaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | DrivingIdeaStatus | STATUS | — | ✅ |
| 25 | DrivingIdeaType | TYPE | — | ✅ |

### [[acn_idea_vote_summary_v|ACN_IDEA_VOTE_SUMMARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaVoteIdeaId | IDEA_ID | — | ✅ |
| 2 | IdeaVoteNoCount | NO_COUNT | — | ✅ |
| 3 | IdeaVoteVoteLastUpdateDate | VOTE_LAST_UPDATE_DATE | — | ✅ |
| 4 | IdeaVoteYesCount | YES_COUNT | — | ✅ |

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
| 16 | RelReqLineItemRequirementLineItemId1 | REQUIREMENT_LINE_ITEM_ID | — | ✅ |
| 17 | RelReqLineItemRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 18 | RelReqLineItemScope | SCOPE | — | ✅ |
| 19 | RelReqLineItemSectionCode | SECTION_CODE | — | ✅ |
| 20 | RelReqLineItemSectionNumber | SECTION_NUMBER | — | ✅ |

### [[acn_requirement_vl|ACN_REQUIREMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedReqAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelatedReqCreatedBy | CREATED_BY | — | ✅ |
| 3 | RelatedReqCreationDate | CREATION_DATE | — | ✅ |
| 4 | RelatedReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RelatedReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RelatedReqLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RelatedReqLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 8 | RelatedReqName | NAME | — | ✅ |
| 9 | RelatedReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RelatedReqRequirementId | REQUIREMENT_ID | — | ✅ |
| 11 | RelatedReqType | TYPE | — | ✅ |

### [[acn_req_version_vl|ACN_REQ_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReqVerPEOCreatedBy | CREATED_BY | — | — |
| 2 | ReqVerPEOCreationDate | CREATION_DATE | — | — |
| 3 | ReqVerPEODescription | DESCRIPTION | — | — |
| 4 | ReqVerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ReqVerPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ReqVerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ReqVerPEOProduct | PRODUCT | — | — |
| 8 | ReqVerPEORequirementId | REQUIREMENT_ID | — | — |
| 9 | ReqVerPEORequirementVersionId | REQUIREMENT_VERSION_ID | — | — |
| 10 | ReqVerPEOStatus | STATUS | — | ✅ |
| 11 | ReqVerPEOStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 12 | ReqVerPEOTotalEstimates | TOTAL_ESTIMATES | — | — |
| 13 | ReqVerPEOVersionNumber | VERSION_NUMBER | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | UserBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | UserCreatedBy | CREATED_BY | — | ✅ |
| 4 | UserCreationDate1 | CREATION_DATE | — | ✅ |
| 5 | UserCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | ✅ |
| 6 | UserEndDate | END_DATE | — | ✅ |
| 7 | UserExternalId | EXTERNAL_ID | — | — |
| 8 | UserHrTerminated | HR_TERMINATED | — | ✅ |
| 9 | UserLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | UserLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | UserLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | UserMultitenancyUsername | MULTITENANCY_USERNAME | — | ✅ |
| 13 | UserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | UserPartyId | PARTY_ID | — | ✅ |
| 15 | UserPersonId | PERSON_ID | — | ✅ |
| 16 | UserStartDate | START_DATE | — | ✅ |
| 17 | UserSuspended | SUSPENDED | — | ✅ |
| 18 | UserUserDataChecksum | USER_DATA_CHECKSUM | — | ✅ |
| 19 | UserUserDistinguishedName | USER_DISTINGUISHED_NAME | — | ✅ |
| 20 | UserUserGuid | USER_GUID | — | ✅ |
| 21 | UserUserId | USER_ID | — | ✅ |
| 22 | UserUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
