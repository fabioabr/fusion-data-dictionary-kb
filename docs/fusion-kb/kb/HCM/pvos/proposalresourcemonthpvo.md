---
id: DOC-HCM-PVO-ProposalResourceMonthPVO
doc_type: system-doc
title: "ProposalResourceMonthPVO — PVO Human Capital Management"
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
  - ProposalResourceMonthPVO
  - proposalresourcemonthpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalResourceMonthPVO

## 📌 Visão Geral

Extrai alocação mensal de recursos por proposta de produto. Suporta planejamento de capacidade e análise temporal de demanda de recursos em conceitos.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ProposalResourceMonthPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 167 | 6 | 2 | 165 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]] — 86 atributos (86 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)
- [[acd_concept_vl|ACD_CONCEPT_VL]] — 20 atributos (19 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 21 atributos (21 BICC)
- [[acd_resource|ACD_RESOURCE]] — 16 atributos (16 BICC)
- [[acd_resource_month_v|ACD_RESOURCE_MONTH_V]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessDetailsActualCost | ACTUAL_COST | — | ✅ |
| 2 | BusinessDetailsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | BusinessDetailsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | BusinessDetailsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | BusinessDetailsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | BusinessDetailsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | BusinessDetailsActualLaunch | ACTUAL_LAUNCH | — | ✅ |
| 8 | BusinessDetailsActualMargin | ACTUAL_MARGIN | — | ✅ |
| 9 | BusinessDetailsActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 10 | BusinessDetailsActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 11 | BusinessDetailsActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 12 | BusinessDetailsActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 13 | BusinessDetailsActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 14 | BusinessDetailsActualResources | ACTUAL_RESOURCES | — | ✅ |
| 15 | BusinessDetailsActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 16 | BusinessDetailsAlignment | ALIGNMENT | — | ✅ |
| 17 | BusinessDetailsAllocatedBudget | ALLOCATED_BUDGET | — | ✅ |
| 18 | BusinessDetailsAverageSellingPrice | AVERAGE_SELLING_PRICE | — | ✅ |
| 19 | BusinessDetailsBaselineDate | BASELINE_DATE | — | ✅ |
| 20 | BusinessDetailsBreakEvenTime | BREAK_EVEN_TIME | — | ✅ |
| 21 | BusinessDetailsBusinessDetailId | BUSINESS_DETAIL_ID | — | ✅ |
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
| 1 | ConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptConceptNumber | CONCEPT_NUMBER | — | ✅ |
| 4 | ConceptCreatedBy | CREATED_BY | — | ✅ |
| 5 | ConceptCreationDate | CREATION_DATE | — | ✅ |
| 6 | ConceptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | ConceptDescription | DESCRIPTION | — | — |
| 8 | ConceptDueDate | DUE_DATE | — | ✅ |
| 9 | ConceptIsCurrent | IS_CURRENT | — | ✅ |
| 10 | ConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | ConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 14 | ConceptMasterId | MASTER_ID | — | ✅ |
| 15 | ConceptName | NAME | — | ✅ |
| 16 | ConceptNotes | NOTES | — | ✅ |
| 17 | ConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ConceptType | TYPE | — | ✅ |
| 19 | ConceptVersion | VERSION | — | ✅ |
| 20 | ConceptVolume | VOLUME | — | ✅ |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptProposalSrcProductProposalId | SRC_PRODUCT_PROPOSAL_ID | — | ✅ |
| 2 | ConceptProposalVersion | VERSION | — | ✅ |
| 3 | ConceptPublishedFromPortfolio | PUBLISHED_FROM_PORTFOLIO | — | ✅ |
| 4 | ProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 5 | ProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 6 | ProposalCreatedBy | CREATED_BY | — | ✅ |
| 7 | ProposalCreationDate | CREATION_DATE | — | ✅ |
| 8 | ProposalCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 9 | ProposalIsCloned | IS_CLONED | — | ✅ |
| 10 | ProposalIsLatest | IS_LATEST | — | ✅ |
| 11 | ProposalLastConceptVersion | LAST_CONCEPT_VERSION | — | ✅ |
| 12 | ProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ProposalObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 18 | ProposalProductProposalId1 | PRODUCT_PROPOSAL_ID | — | ✅ |
| 19 | ProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 20 | ProposalType | PROPOSAL_TYPE | — | ✅ |
| 21 | ProposalVersion | VERSION | — | ✅ |

### [[acd_resource|ACD_RESOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductResourceCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProductResourceCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProductResourceEndDate | END_DATE | — | ✅ |
| 4 | ProductResourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProductResourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ProductResourceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ProductResourceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ProductResourceProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 9 | ProductResourceResourceCategory | RESOURCE_CATEGORY | — | ✅ |
| 10 | ProductResourceResourceHeadcount | RESOURCE_HEADCOUNT | — | ✅ |
| 11 | ProductResourceResourceId | RESOURCE_ID | — | ✅ |
| 12 | ProductResourceResourcePool | RESOURCE_POOL | — | ✅ |
| 13 | ProductResourceResourceStatus | RESOURCE_STATUS | — | ✅ |
| 14 | ProductResourceResourceTrend | RESOURCE_TREND | — | ✅ |
| 15 | ProductResourceSource | SOURCE | — | ✅ |
| 16 | ProductResourceStartDate | START_DATE | — | ✅ |

### [[acd_resource_month_v|ACD_RESOURCE_MONTH_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductProposalResourceMonthCalMonth | CAL_MONTH | — | ✅ |
| 2 | ProductProposalResourceMonthEndDate | END_DATE | — | ✅ |
| 3 | ProductProposalResourceMonthHeadCountMonth | HEAD_COUNT_MONTH | — | ✅ |
| 4 | ProductProposalResourceMonthHeadCountQuarter | HEAD_COUNT_QUARTER | — | ✅ |
| 5 | ProductProposalResourceMonthHeadCountYear | HEAD_COUNT_YEAR | — | ✅ |
| 6 | ProductProposalResourceMonthMonth | MONTH | — | ✅ |
| 7 | ProductProposalResourceMonthProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 8 | ProductProposalResourceMonthResourceCategory | RESOURCE_CATEGORY | — | ✅ |
| 9 | ProductProposalResourceMonthResourceId | RESOURCE_ID | 🔑 | ✅ |
| 10 | ProductProposalResourceMonthResourcePool | RESOURCE_POOL | — | ✅ |
| 11 | ProductProposalResourceMonthResourceStatus | RESOURCE_STATUS | — | ✅ |
| 12 | ProductProposalResourceMonthRn | RN | 🔑 | ✅ |
| 13 | ProductProposalResourceMonthStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
