---
id: DOC-HCM-PVO-ProposalRelationshipPVO
doc_type: system-doc
title: "ProposalRelationshipPVO — PVO Human Capital Management"
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
  - ProposalRelationshipPVO
  - proposalrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalRelationshipPVO

## 📌 Visão Geral

Disponibiliza relacionamentos entre propostas, componentes e estruturas de conceito. Mapeia dependências e vínculos entre propostas no ciclo de inovação.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.ProposalRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 376 | 12 | 1 | 358 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]] — 86 atributos (86 BICC)
- [[acd_component_vl|ACD_COMPONENT_VL]] — 15 atributos (14 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 18 atributos (17 BICC)
- [[acd_concept_structure|ACD_CONCEPT_STRUCTURE]] — 122 atributos (122 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)
- [[acd_concept_vl|ACD_CONCEPT_VL]] — 15 atributos (14 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 31 atributos (30 BICC)
- [[acd_prop_relationship_v|ACD_PROP_RELATIONSHIP_V]] — 22 atributos (1 PKs, 22 BICC)
- [[acn_idea_vl|ACN_IDEA_VL]] — 12 atributos (11 BICC)
- [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]] — 19 atributos (19 BICC)
- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 11 atributos (11 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 14 atributos (2 BICC)

---

## ⚙️ Atributos

### [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessDetailId | BUSINESS_DETAIL_ID | — | ✅ |
| 2 | BusinessDetailsActualCost | ACTUAL_COST | — | ✅ |
| 3 | BusinessDetailsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 4 | BusinessDetailsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 5 | BusinessDetailsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 6 | BusinessDetailsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 7 | BusinessDetailsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 8 | BusinessDetailsActualLaunch | ACTUAL_LAUNCH | — | ✅ |
| 9 | BusinessDetailsActualMargin | ACTUAL_MARGIN | — | ✅ |
| 10 | BusinessDetailsActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 11 | BusinessDetailsActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 12 | BusinessDetailsActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 13 | BusinessDetailsActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 14 | BusinessDetailsActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 15 | BusinessDetailsActualResources | ACTUAL_RESOURCES | — | ✅ |
| 16 | BusinessDetailsActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 17 | BusinessDetailsAlignment | ALIGNMENT | — | ✅ |
| 18 | BusinessDetailsAllocatedBudget | ALLOCATED_BUDGET | — | ✅ |
| 19 | BusinessDetailsAverageSellingPrice | AVERAGE_SELLING_PRICE | — | ✅ |
| 20 | BusinessDetailsBaselineDate | BASELINE_DATE | — | ✅ |
| 21 | BusinessDetailsBreakEvenTime | BREAK_EVEN_TIME | — | ✅ |
| 22 | BusinessDetailsBusinessObjectives | BUSINESS_OBJECTIVES | — | ✅ |
| 23 | BusinessDetailsBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 24 | BusinessDetailsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 25 | BusinessDetailsCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 26 | BusinessDetailsCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 27 | BusinessDetailsCpi | CPI | — | ✅ |
| 28 | BusinessDetailsCreatedBy | CREATED_BY | — | ✅ |
| 29 | BusinessDetailsCreationDate | CREATION_DATE | — | ✅ |
| 30 | BusinessDetailsDevelopmentEnd | DEVELOPMENT_END | — | ✅ |
| 31 | BusinessDetailsDevelopmentStart | DEVELOPMENT_START | — | ✅ |
| 32 | BusinessDetailsDiscountRate | DISCOUNT_RATE | — | ✅ |
| 33 | BusinessDetailsEol | EOL | — | ✅ |
| 34 | BusinessDetailsExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 35 | BusinessDetailsFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 36 | BusinessDetailsFundingRequestFor | FUNDING_REQUEST_FOR | — | ✅ |
| 37 | BusinessDetailsHighLevelDesign | HIGH_LEVEL_DESIGN | — | ✅ |
| 38 | BusinessDetailsImpact | IMPACT | — | ✅ |
| 39 | BusinessDetailsInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 40 | BusinessDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | BusinessDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | BusinessDetailsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | BusinessDetailsLaunch | LAUNCH | — | ✅ |
| 44 | BusinessDetailsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 45 | BusinessDetailsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 46 | BusinessDetailsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 47 | BusinessDetailsMarketStrategy | MARKET_STRATEGY | — | ✅ |
| 48 | BusinessDetailsNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 49 | BusinessDetailsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 50 | BusinessDetailsPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 51 | BusinessDetailsPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 52 | BusinessDetailsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 53 | BusinessDetailsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 54 | BusinessDetailsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 55 | BusinessDetailsProductLine | PRODUCT_LINE | — | ✅ |
| 56 | BusinessDetailsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 57 | BusinessDetailsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 58 | BusinessDetailsProjDevCost | PROJ_DEV_COST | — | ✅ |
| 59 | BusinessDetailsProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 60 | BusinessDetailsProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 61 | BusinessDetailsProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 62 | BusinessDetailsProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 63 | BusinessDetailsProjProdCost | PROJ_PROD_COST | — | ✅ |
| 64 | BusinessDetailsProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 65 | BusinessDetailsProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 66 | BusinessDetailsProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 67 | BusinessDetailsProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 68 | BusinessDetailsProjectedMargin | PROJECTED_MARGIN | — | ✅ |
| 69 | BusinessDetailsProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 70 | BusinessDetailsProposalProjectedCost | PROPOSAL_PROJECTED_COST | — | ✅ |
| 71 | BusinessDetailsProposalProjectedRevenue | PROPOSAL_PROJECTED_REVENUE | — | ✅ |
| 72 | BusinessDetailsProposalVersionNotes | PROPOSAL_VERSION_NOTES | — | ✅ |
| 73 | BusinessDetailsRequirementsDefinition | REQUIREMENTS_DEFINITION | — | ✅ |
| 74 | BusinessDetailsResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 75 | BusinessDetailsReturnOnInvestment | RETURN_ON_INVESTMENT | — | ✅ |
| 76 | BusinessDetailsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 77 | BusinessDetailsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 78 | BusinessDetailsRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 79 | BusinessDetailsRpi | RPI | — | ✅ |
| 80 | BusinessDetailsSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 81 | BusinessDetailsSummary | SUMMARY | — | ✅ |
| 82 | BusinessDetailsSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 83 | BusinessDetailsTargetCost | TARGET_COST | — | ✅ |
| 84 | BusinessDetailsYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 85 | BusinessDetailsYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 86 | BusinessDetailsYear5Revenue | YEAR_5_REVENUE | — | ✅ |

### [[acd_component_vl|ACD_COMPONENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelComponentComponentId | COMPONENT_ID | — | ✅ |
| 2 | RelComponentComponentSize | COMPONENT_SIZE | — | ✅ |
| 3 | RelComponentCreationDate | CREATION_DATE | — | ✅ |
| 4 | RelComponentDescription | DESCRIPTION | — | — |
| 5 | RelComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RelComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RelComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RelComponentMaterial | MATERIAL | — | ✅ |
| 9 | RelComponentName | NAME | — | ✅ |
| 10 | RelComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RelComponentSupplier | SUPPLIER | — | ✅ |
| 12 | RelComponentTargetType | TARGET_TYPE | — | ✅ |
| 13 | RelComponentTopConceptId | TOP_CONCEPT_ID | — | ✅ |
| 14 | RelComponentType | TYPE | — | ✅ |
| 15 | RelComponentreatedBy | CREATED_BY | — | ✅ |

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptBaseConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptBaseConceptNumber | CONCEPT_NUMBER | — | — |
| 4 | ConceptBaseCreatedBy | CREATED_BY | — | ✅ |
| 5 | ConceptBaseCreationDate | CREATION_DATE | — | ✅ |
| 6 | ConceptBaseCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | ConceptBaseDueDate | DUE_DATE | — | ✅ |
| 8 | ConceptBaseIsCurrent | IS_CURRENT | — | ✅ |
| 9 | ConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ConceptBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ConceptBaseLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 13 | ConceptBaseMasterId | MASTER_ID | — | ✅ |
| 14 | ConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ConceptBasePowerUnit | POWER_UNIT | — | ✅ |
| 16 | ConceptBaseType | TYPE | — | ✅ |
| 17 | ConceptBaseVersion | VERSION | — | ✅ |
| 18 | ConceptBaseVolume | VOLUME | — | ✅ |

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
| 14 | CompStructureCreationDate | CREATION_DATE | — | ✅ |
| 15 | CompStructureFixedCost | FIXED_COST | — | ✅ |
| 16 | CompStructureFromId | FROM_ID | — | ✅ |
| 17 | CompStructureFromStrId | FROM_STR_ID | — | ✅ |
| 18 | CompStructureFromType | FROM_TYPE | — | ✅ |
| 19 | CompStructureItemNumberManifacturers | ITEM_NUMBER_MANIFACTURERS | — | ✅ |
| 20 | CompStructureLastCostUpdate | LAST_COST_UPDATE | — | ✅ |
| 21 | CompStructureLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CompStructureLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CompStructureLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CompStructureLeadTime | LEAD_TIME | — | ✅ |
| 25 | CompStructureLocation | LOCATION | — | ✅ |
| 26 | CompStructureMaterial | MATERIAL | — | ✅ |
| 27 | CompStructureMaterialCost | MATERIAL_COST | — | ✅ |
| 28 | CompStructureMorphedId | MORPHED_ID | — | ✅ |
| 29 | CompStructureNonMaterialCost | NON_MATERIAL_COST | — | ✅ |
| 30 | CompStructureNumberManufacturers | NUMBER_MANUFACTURERS | — | ✅ |
| 31 | CompStructureObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | CompStructurePlaceholder | PLACEHOLDER | — | ✅ |
| 33 | CompStructurePosNo | POS_NO | — | ✅ |
| 34 | CompStructurePowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | ✅ |
| 35 | CompStructurePowerIncomplete | POWER_INCOMPLETE | — | ✅ |
| 36 | CompStructurePowerUnit | POWER_UNIT | — | ✅ |
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
| 122 | ConceptStructureaterialCost | MATERIAL_COST | — | ✅ |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTranslationConceptId | CONCEPT_ID | — | ✅ |
| 2 | ConceptTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | ConceptTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | ConceptTranslationDescription | DESCRIPTION | — | — |
| 5 | ConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | ConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ConceptTranslationName | NAME | — | ✅ |
| 10 | ConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |

### [[acd_concept_vl|ACD_CONCEPT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RelatedConceptConceptId | CONCEPT_ID | — | ✅ |
| 3 | RelatedConceptCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelatedConceptCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelatedConceptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | RelatedConceptDescription | DESCRIPTION | — | — |
| 7 | RelatedConceptIsCurrent | IS_CURRENT | — | ✅ |
| 8 | RelatedConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RelatedConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | RelatedConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RelatedConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 12 | RelatedConceptMasterId | MASTER_ID | — | ✅ |
| 13 | RelatedConceptName | NAME | — | ✅ |
| 14 | RelatedConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | RelatedConceptVersion | VERSION | — | ✅ |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DerivedProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | DerivedProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 3 | DerivedProposalCreatedBy | CREATED_BY | — | ✅ |
| 4 | DerivedProposalCreationDate | CREATION_DATE | — | ✅ |
| 5 | DerivedProposalCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 6 | DerivedProposalIsCloned | IS_CLONED | — | ✅ |
| 7 | DerivedProposalIsLatest | IS_LATEST | — | ✅ |
| 8 | DerivedProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DerivedProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | DerivedProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DerivedProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | DerivedProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 13 | DerivedProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 14 | DerivedProposalType | PROPOSAL_TYPE | — | ✅ |
| 15 | DerivedProposalVersion | VERSION | — | ✅ |
| 16 | DrivingProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 17 | DrivingProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 18 | DrivingProposalCreatedBy | CREATED_BY | — | ✅ |
| 19 | DrivingProposalCreationDate | CREATION_DATE | — | ✅ |
| 20 | DrivingProposalCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 21 | DrivingProposalIsCloned | IS_CLONED | — | ✅ |
| 22 | DrivingProposalIsLatest | IS_LATEST | — | ✅ |
| 23 | DrivingProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | DrivingProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | DrivingProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | DrivingProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | DrivingProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 28 | DrivingProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 29 | DrivingProposalPublishedFromPortfolio | PUBLISHED_FROM_PORTFOLIO | — | ✅ |
| 30 | DrivingProposalType | PROPOSAL_TYPE | — | ✅ |
| 31 | DrivingProposalVersion | VERSION | — | ✅ |

### [[acd_prop_relationship_v|ACD_PROP_RELATIONSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProposalRelationshipCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProposalRelationshipCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProposalRelationshipDerivedComponentId | DERIVED_COMPONENT_ID | — | ✅ |
| 4 | ProposalRelationshipDerivedConceptId | DERIVED_CONCEPT_ID | — | ✅ |
| 5 | ProposalRelationshipDerivedIdeaId | DERIVED_IDEA_ID | — | ✅ |
| 6 | ProposalRelationshipDerivedProjectId | DERIVED_PROJECT_ID | — | ✅ |
| 7 | ProposalRelationshipDerivedRequirementId | DERIVED_REQUIREMENT_ID | — | ✅ |
| 8 | ProposalRelationshipDerivedRequirementLineId | DERIVED_REQUIREMENT_LINE_ID | — | ✅ |
| 9 | ProposalRelationshipDerivedTaskId | DERIVED_TASK_ID | — | ✅ |
| 10 | ProposalRelationshipDestObjId | DEST_OBJ_ID | — | ✅ |
| 11 | ProposalRelationshipDestObjType | DEST_OBJ_TYPE | — | ✅ |
| 12 | ProposalRelationshipDirectionType | DIRECTION_TYPE | — | ✅ |
| 13 | ProposalRelationshipFinalDerivedId | FINAL_DERIVED_ID | — | ✅ |
| 14 | ProposalRelationshipFinalDrivingId | FINAL_DRIVING_ID | — | ✅ |
| 15 | ProposalRelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ProposalRelationshipLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ProposalRelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ProposalRelationshipRelationshipId | RELATIONSHIP_ID | 🔑 | ✅ |
| 19 | ProposalRelationshipRelationshipType | RELATIONSHIP_TYPE | — | ✅ |
| 20 | ProposalRelationshipSrcObjId | SRC_OBJ_ID | — | ✅ |
| 21 | ProposalRelationshipSrcObjType | SRC_OBJ_TYPE | — | ✅ |
| 22 | ProposalRelationshipTargetType | TARGET_TYPE | — | ✅ |

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
| 1 | RelatedReqVersionCreatedBy | CREATED_BY | — | — |
| 2 | RelatedReqVersionCreationDate | CREATION_DATE | — | — |
| 3 | RelatedReqVersionDescription | DESCRIPTION | — | — |
| 4 | RelatedReqVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RelatedReqVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | RelatedReqVersionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | RelatedReqVersionNumber | VERSION_NUMBER | — | — |
| 8 | RelatedReqVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RelatedReqVersionProduct | PRODUCT | — | — |
| 10 | RelatedReqVersionRequirementId | REQUIREMENT_ID | — | — |
| 11 | RelatedReqVersionRequirementVersionId | REQUIREMENT_VERSION_ID | — | — |
| 12 | RelatedReqVersionStatus | STATUS | — | ✅ |
| 13 | RelatedReqVersionStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 14 | RelatedReqVersionTotalEstimates | TOTAL_ESTIMATES | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
