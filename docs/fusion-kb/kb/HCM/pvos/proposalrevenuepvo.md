---
id: DOC-HCM-PVO-ProposalRevenuePVO
doc_type: system-doc
title: "ProposalRevenuePVO — PVO Human Capital Management"
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
  - ProposalRevenuePVO
  - proposalrevenuepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalRevenuePVO

## 📌 Visão Geral

Extrai receitas projetadas por proposta de produto, com detalhes financeiros. Suporta análise de retorno sobre investimento e viabilidade econômica de conceitos.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ProposalRevenuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 5 | 1 | 145 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]] — 86 atributos (86 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 18 atributos (18 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 16 atributos (16 BICC)
- [[acd_revenue|ACD_REVENUE]] — 15 atributos (1 PKs, 15 BICC)

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

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptConceptNumber | CONCEPT_NUMBER | — | ✅ |
| 4 | ConceptCreatedBy | CREATED_BY | — | ✅ |
| 5 | ConceptCreationDate | CREATION_DATE | — | ✅ |
| 6 | ConceptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | ConceptDueDate | DUE_DATE | — | ✅ |
| 8 | ConceptIsCurrent | IS_CURRENT | — | ✅ |
| 9 | ConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 13 | ConceptMasterId | MASTER_ID | — | ✅ |
| 14 | ConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ConceptPowerUnit | POWER_UNIT | — | ✅ |
| 16 | ConceptType | TYPE | — | ✅ |
| 17 | ConceptVersion | VERSION | — | ✅ |
| 18 | ConceptVolume | VOLUME | — | ✅ |

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

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 3 | ProposalCreatedBy | CREATED_BY | — | ✅ |
| 4 | ProposalCreationDate | CREATION_DATE | — | ✅ |
| 5 | ProposalCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 6 | ProposalIsCloned | IS_CLONED | — | ✅ |
| 7 | ProposalIsLatest | IS_LATEST | — | ✅ |
| 8 | ProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 13 | ProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 14 | ProposalPublishedFromPortfolio | PUBLISHED_FROM_PORTFOLIO | — | ✅ |
| 15 | ProposalType | PROPOSAL_TYPE | — | ✅ |
| 16 | ProposalVersion | VERSION | — | ✅ |

### [[acd_revenue|ACD_REVENUE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RevenueCreatedBy | CREATED_BY | — | ✅ |
| 2 | RevenueCreationDate | CREATION_DATE | — | ✅ |
| 3 | RevenueEndDate | END_DATE | — | ✅ |
| 4 | RevenueLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RevenueLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RevenueLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RevenueObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | RevenueProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 9 | RevenueRevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 10 | RevenueRevenueCategory | REVENUE_CATEGORY | — | ✅ |
| 11 | RevenueRevenueId | REVENUE_ID | 🔑 | ✅ |
| 12 | RevenueRevenueStatus | REVENUE_STATUS | — | ✅ |
| 13 | RevenueRevenueTrend | REVENUE_TREND | — | ✅ |
| 14 | RevenueRevenueType | REVENUE_TYPE | — | ✅ |
| 15 | RevenueStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
