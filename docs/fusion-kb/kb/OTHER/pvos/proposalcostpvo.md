---
id: DOC-OTHER-PVO-ProposalCostPVO
doc_type: system-doc
title: "ProposalCostPVO — PVO Cross-Module"
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
  - ProposalCostPVO
  - proposalcostpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalCostPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Proposal Cost. Acessa as tabelas: ACD_BUSINESS_DETAILS_VL, ACD_CONCEPT_B, ACD_CONCEPT_TL (+2).

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ProposalCostPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 5 | 1 | 145 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]] — 86 atributos (86 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 18 atributos (18 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)
- [[acd_costs|ACD_COSTS]] — 15 atributos (1 PKs, 15 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 16 atributos (16 BICC)

---

## ⚙️ Atributos

### [[acd_business_details_vl|ACD_BUSINESS_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessDetailId | BUSINESS_DETAIL_ID | — | ✅ |
| 2 | BusinessDetalsActualCost | ACTUAL_COST | — | ✅ |
| 3 | BusinessDetalsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 4 | BusinessDetalsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 5 | BusinessDetalsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 6 | BusinessDetalsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 7 | BusinessDetalsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 8 | BusinessDetalsActualLaunch | ACTUAL_LAUNCH | — | ✅ |
| 9 | BusinessDetalsActualMargin | ACTUAL_MARGIN | — | ✅ |
| 10 | BusinessDetalsActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 11 | BusinessDetalsActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 12 | BusinessDetalsActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 13 | BusinessDetalsActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 14 | BusinessDetalsActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 15 | BusinessDetalsActualResources | ACTUAL_RESOURCES | — | ✅ |
| 16 | BusinessDetalsActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 17 | BusinessDetalsAlignment | ALIGNMENT | — | ✅ |
| 18 | BusinessDetalsAllocatedBudget | ALLOCATED_BUDGET | — | ✅ |
| 19 | BusinessDetalsAverageSellingPrice | AVERAGE_SELLING_PRICE | — | ✅ |
| 20 | BusinessDetalsBaselineDate | BASELINE_DATE | — | ✅ |
| 21 | BusinessDetalsBreakEvenTime | BREAK_EVEN_TIME | — | ✅ |
| 22 | BusinessDetalsBusinessObjectives | BUSINESS_OBJECTIVES | — | ✅ |
| 23 | BusinessDetalsBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 24 | BusinessDetalsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 25 | BusinessDetalsCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 26 | BusinessDetalsCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 27 | BusinessDetalsCpi | CPI | — | ✅ |
| 28 | BusinessDetalsCreatedBy | CREATED_BY | — | ✅ |
| 29 | BusinessDetalsCreationDate | CREATION_DATE | — | ✅ |
| 30 | BusinessDetalsDevelopmentEnd | DEVELOPMENT_END | — | ✅ |
| 31 | BusinessDetalsDevelopmentStart | DEVELOPMENT_START | — | ✅ |
| 32 | BusinessDetalsDiscountRate | DISCOUNT_RATE | — | ✅ |
| 33 | BusinessDetalsEol | EOL | — | ✅ |
| 34 | BusinessDetalsExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 35 | BusinessDetalsFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 36 | BusinessDetalsFundingRequestFor | FUNDING_REQUEST_FOR | — | ✅ |
| 37 | BusinessDetalsHighLevelDesign | HIGH_LEVEL_DESIGN | — | ✅ |
| 38 | BusinessDetalsImpact | IMPACT | — | ✅ |
| 39 | BusinessDetalsInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 40 | BusinessDetalsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | BusinessDetalsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | BusinessDetalsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | BusinessDetalsLaunch | LAUNCH | — | ✅ |
| 44 | BusinessDetalsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 45 | BusinessDetalsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 46 | BusinessDetalsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 47 | BusinessDetalsMarketStrategy | MARKET_STRATEGY | — | ✅ |
| 48 | BusinessDetalsNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 49 | BusinessDetalsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 50 | BusinessDetalsPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 51 | BusinessDetalsPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 52 | BusinessDetalsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 53 | BusinessDetalsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 54 | BusinessDetalsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 55 | BusinessDetalsProductLine | PRODUCT_LINE | — | ✅ |
| 56 | BusinessDetalsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 57 | BusinessDetalsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 58 | BusinessDetalsProjDevCost | PROJ_DEV_COST | — | ✅ |
| 59 | BusinessDetalsProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 60 | BusinessDetalsProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 61 | BusinessDetalsProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 62 | BusinessDetalsProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 63 | BusinessDetalsProjProdCost | PROJ_PROD_COST | — | ✅ |
| 64 | BusinessDetalsProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 65 | BusinessDetalsProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 66 | BusinessDetalsProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 67 | BusinessDetalsProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 68 | BusinessDetalsProjectedMargin | PROJECTED_MARGIN | — | ✅ |
| 69 | BusinessDetalsProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 70 | BusinessDetalsProposalProjectedCost | PROPOSAL_PROJECTED_COST | — | ✅ |
| 71 | BusinessDetalsProposalProjectedRevenue | PROPOSAL_PROJECTED_REVENUE | — | ✅ |
| 72 | BusinessDetalsProposalVersionNotes | PROPOSAL_VERSION_NOTES | — | ✅ |
| 73 | BusinessDetalsRequirementsDefinition | REQUIREMENTS_DEFINITION | — | ✅ |
| 74 | BusinessDetalsResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 75 | BusinessDetalsReturnOnInvestment | RETURN_ON_INVESTMENT | — | ✅ |
| 76 | BusinessDetalsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 77 | BusinessDetalsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 78 | BusinessDetalsRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 79 | BusinessDetalsRpi | RPI | — | ✅ |
| 80 | BusinessDetalsSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 81 | BusinessDetalsSummary | SUMMARY | — | ✅ |
| 82 | BusinessDetalsSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 83 | BusinessDetalsTargetCost | TARGET_COST | — | ✅ |
| 84 | BusinessDetalsYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 85 | BusinessDetalsYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 86 | BusinessDetalsYear5Revenue | YEAR_5_REVENUE | — | ✅ |

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

### [[acd_costs|ACD_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostCostAmount | COST_AMOUNT | — | ✅ |
| 2 | CostCostCategory | COST_CATEGORY | — | ✅ |
| 3 | CostCostId | COST_ID | 🔑 | ✅ |
| 4 | CostCostStatus | COST_STATUS | — | ✅ |
| 5 | CostCostTrend | COST_TREND | — | ✅ |
| 6 | CostCostType | COST_TYPE | — | ✅ |
| 7 | CostCreatedBy | CREATED_BY | — | ✅ |
| 8 | CostCreationDate | CREATION_DATE | — | ✅ |
| 9 | CostEndDate | END_DATE | — | ✅ |
| 10 | CostLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CostLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CostLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CostObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | CostProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 15 | CostStartDate | START_DATE | — | ✅ |

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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
