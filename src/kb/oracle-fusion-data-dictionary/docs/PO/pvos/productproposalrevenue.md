---
id: DOC-PO-PVO-ProductProposalRevenue
doc_type: system-doc
title: "ProductProposalRevenue — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ProductProposalRevenue
  - productproposalrevenue
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductProposalRevenue

## 📌 Visão Geral

Extrai receitas projetadas de propostas de produto, com valores por período e cenário. Suporta análise de ROI, viabilidade econômica e comparação de alternativas de investimento.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductProposalRevenue`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 195 | 5 | 1 | 195 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[acd_revenue|ACD_REVENUE]] — 15 atributos (1 PKs, 15 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 65 atributos (65 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_selected_products|ACE_SELECTED_PRODUCTS]] — 70 atributos (70 BICC)

---

## ⚙️ Atributos

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrdProposalConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 2 | PrdProposalCreatedBy | CREATED_BY | — | ✅ |
| 3 | PrdProposalCreationDate | CREATION_DATE | — | ✅ |
| 4 | PrdProposalIsCloned | IS_CLONED | — | ✅ |
| 5 | PrdProposalIsLatest | IS_LATEST | — | ✅ |
| 6 | PrdProposalLastConceptVersion | LAST_CONCEPT_VERSION | — | ✅ |
| 7 | PrdProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PrdProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PrdProposalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PrdProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PrdProposalProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 12 | PrdProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 13 | PrdProposalProposalType | PROPOSAL_TYPE | — | ✅ |
| 14 | PrdProposalSrcProductProposalId | SRC_PRODUCT_PROPOSAL_ID | — | ✅ |
| 15 | PrdProposalVersion | VERSION | — | ✅ |

### [[acd_revenue|ACD_REVENUE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrdProposalRevenueCreatedBy | CREATED_BY | — | ✅ |
| 2 | PrdProposalRevenueCreationDate | CREATION_DATE | — | ✅ |
| 3 | PrdProposalRevenueEndDate | END_DATE | — | ✅ |
| 4 | PrdProposalRevenueLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PrdProposalRevenueLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PrdProposalRevenueLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PrdProposalRevenueObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PrdProposalRevenueProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 9 | PrdProposalRevenueRevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 10 | PrdProposalRevenueRevenueCategory | REVENUE_CATEGORY | — | ✅ |
| 11 | PrdProposalRevenueRevenueId | REVENUE_ID | 🔑 | ✅ |
| 12 | PrdProposalRevenueRevenueStatus | REVENUE_STATUS | — | ✅ |
| 13 | PrdProposalRevenueRevenueTrend | REVENUE_TREND | — | ✅ |
| 14 | PrdProposalRevenueRevenueType | REVENUE_TYPE | — | ✅ |
| 15 | PrdProposalRevenueStartDate | START_DATE | — | ✅ |

### [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 2 | ScenarioActualCost | ACTUAL_COST | — | ✅ |
| 3 | ScenarioActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 4 | ScenarioActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 5 | ScenarioActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | ScenarioActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | ScenarioActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 8 | ScenarioActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 9 | ScenarioActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 10 | ScenarioActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 11 | ScenarioActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 12 | ScenarioActualResources | ACTUAL_RESOURCES | — | ✅ |
| 13 | ScenarioActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 14 | ScenarioAlignment | ALIGNMENT | — | ✅ |
| 15 | ScenarioCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 16 | ScenarioCostDeviation | COST_DEVIATION | — | ✅ |
| 17 | ScenarioCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 18 | ScenarioCpi | CPI | — | ✅ |
| 19 | ScenarioCreatedBy | CREATED_BY | — | ✅ |
| 20 | ScenarioCreationDate | CREATION_DATE | — | ✅ |
| 21 | ScenarioCreator | CREATOR | — | ✅ |
| 22 | ScenarioDateCreated | DATE_CREATED | — | ✅ |
| 23 | ScenarioExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 24 | ScenarioImpact | IMPACT | — | ✅ |
| 25 | ScenarioInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 26 | ScenarioIsEnabled | IS_ENABLED | — | ✅ |
| 27 | ScenarioLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | ScenarioLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | ScenarioLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | ScenarioMarginDeviation | MARGIN_DEVIATION | — | ✅ |
| 31 | ScenarioNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 32 | ScenarioObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | ScenarioPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 34 | ScenarioPortfolioId | PORTFOLIO_ID | — | ✅ |
| 35 | ScenarioPortfolioRevisionId | PORTFOLIO_REVISION_ID | — | ✅ |
| 36 | ScenarioPortfolioRiskNumeric | PORTFOLIO_RISK_NUMERIC | — | ✅ |
| 37 | ScenarioPortfolioRiskSubjective | PORTFOLIO_RISK_SUBJECTIVE | — | ✅ |
| 38 | ScenarioPortfolioStrategicFit | PORTFOLIO_STRATEGIC_FIT | — | ✅ |
| 39 | ScenarioPortfolioStrategicImp | PORTFOLIO_STRATEGIC_IMP | — | ✅ |
| 40 | ScenarioProjDevCost | PROJ_DEV_COST | — | ✅ |
| 41 | ScenarioProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 42 | ScenarioProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 43 | ScenarioProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 44 | ScenarioProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 45 | ScenarioProjProdCost | PROJ_PROD_COST | — | ✅ |
| 46 | ScenarioProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 47 | ScenarioProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 48 | ScenarioProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 49 | ScenarioProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 50 | ScenarioProjectedCost | PROJECTED_COST | — | ✅ |
| 51 | ScenarioProjectedMargin | PROJECTED_MARGIN | — | ✅ |
| 52 | ScenarioProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 53 | ScenarioProjectedRevenue | PROJECTED_REVENUE | — | ✅ |
| 54 | ScenarioResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 55 | ScenarioRevenueDeviation | REVENUE_DEVIATION | — | ✅ |
| 56 | ScenarioRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 57 | ScenarioRoi | ROI | — | ✅ |
| 58 | ScenarioRpi | RPI | — | ✅ |
| 59 | ScenarioScenarioId | SCENARIO_ID | — | ✅ |
| 60 | ScenarioStatus | STATUS | — | ✅ |
| 61 | ScenarioSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 62 | ScenarioTrcc | TRCC | — | ✅ |
| 63 | ScenarioYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 64 | ScenarioYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 65 | ScenarioYear5Revenue | YEAR_5_REVENUE | — | ✅ |

### [[ace_portfolio_b|ACE_PORTFOLIO_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioArchiveFlag | ARCHIVE_FLAG | — | ✅ |
| 2 | PortfolioBudget | BUDGET | — | ✅ |
| 3 | PortfolioBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 4 | PortfolioClassType | CLASS_TYPE | — | ✅ |
| 5 | PortfolioCompanyNodeId | COMPANY_NODE_ID | — | ✅ |
| 6 | PortfolioCreatedBy | CREATED_BY | — | ✅ |
| 7 | PortfolioCreatedFromPortfolioId | CREATED_FROM_PORTFOLIO_ID | — | ✅ |
| 8 | PortfolioCreationDate | CREATION_DATE | — | ✅ |
| 9 | PortfolioCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | PortfolioCurrentPlanId | CURRENT_PLAN_ID | — | ✅ |
| 11 | PortfolioDeletedFlag | DELETED_FLAG | — | ✅ |
| 12 | PortfolioLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PortfolioLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PortfolioLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PortfolioLatestRevisionId | LATEST_REVISION_ID | — | ✅ |
| 16 | PortfolioLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 17 | PortfolioObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | PortfolioOwner | OWNER | — | ✅ |
| 19 | PortfolioPlanningPeriodId | PLANNING_PERIOD_ID | — | ✅ |
| 20 | PortfolioPortfolioId | PORTFOLIO_ID | — | ✅ |
| 21 | PortfolioPortfolioType | PORTFOLIO_TYPE | — | ✅ |
| 22 | PortfolioPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 23 | PortfolioProductLine | PRODUCT_LINE | — | ✅ |
| 24 | PortfolioProposedPlanId | PROPOSED_PLAN_ID | — | ✅ |
| 25 | PortfolioRevenueExpectation | REVENUE_EXPECTATION | — | ✅ |
| 26 | PortfolioSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 27 | PortfolioTargetCost | TARGET_COST | — | ✅ |
| 28 | PortfolioTargetMargin | TARGET_MARGIN | — | ✅ |
| 29 | PortfolioTargetRevenue | TARGET_REVENUE | — | ✅ |
| 30 | PortfolioWorkflow | WORKFLOW | — | ✅ |

### [[ace_selected_products|ACE_SELECTED_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjDevMaterialCost1 | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 2 | SelProductsActualCost | ACTUAL_COST | — | ✅ |
| 3 | SelProductsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 4 | SelProductsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 5 | SelProductsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 6 | SelProductsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 7 | SelProductsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 8 | SelProductsActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 9 | SelProductsActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 10 | SelProductsActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 11 | SelProductsActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 12 | SelProductsActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 13 | SelProductsActualResources | ACTUAL_RESOURCES | — | ✅ |
| 14 | SelProductsActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 15 | SelProductsAlignment | ALIGNMENT | — | ✅ |
| 16 | SelProductsBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 17 | SelProductsBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 18 | SelProductsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 19 | SelProductsCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 20 | SelProductsConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 21 | SelProductsCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 22 | SelProductsCpi | CPI | — | ✅ |
| 23 | SelProductsCreatedBy | CREATED_BY | — | ✅ |
| 24 | SelProductsCreationDate | CREATION_DATE | — | ✅ |
| 25 | SelProductsExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 26 | SelProductsImpact | IMPACT | — | ✅ |
| 27 | SelProductsIncluded | INCLUDED | — | ✅ |
| 28 | SelProductsInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 29 | SelProductsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | SelProductsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | SelProductsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | SelProductsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 33 | SelProductsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 34 | SelProductsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 35 | SelProductsNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 36 | SelProductsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 37 | SelProductsPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 38 | SelProductsPriority | PRIORITY | — | ✅ |
| 39 | SelProductsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 40 | SelProductsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 41 | SelProductsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 42 | SelProductsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 43 | SelProductsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 44 | SelProductsProductStrategicImp | PRODUCT_STRATEGIC_IMP | — | ✅ |
| 45 | SelProductsProjDevCost | PROJ_DEV_COST | — | ✅ |
| 46 | SelProductsProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 47 | SelProductsProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 48 | SelProductsProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 49 | SelProductsProjProdCost | PROJ_PROD_COST | — | ✅ |
| 50 | SelProductsProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 51 | SelProductsProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 52 | SelProductsProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 53 | SelProductsProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 54 | SelProductsProjectedCost | PROJECTED_COST | — | ✅ |
| 55 | SelProductsProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 56 | SelProductsProjectedRevenue | PROJECTED_REVENUE | — | ✅ |
| 57 | SelProductsRank | RANK | — | ✅ |
| 58 | SelProductsResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 59 | SelProductsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 60 | SelProductsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 61 | SelProductsRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 62 | SelProductsRoi | ROI | — | ✅ |
| 63 | SelProductsRpi | RPI | — | ✅ |
| 64 | SelProductsScore | SCORE | — | ✅ |
| 65 | SelProductsSelectedProductsId | SELECTED_PRODUCTS_ID | — | ✅ |
| 66 | SelProductsSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 67 | SelProductsTrcc | TRCC | — | ✅ |
| 68 | SelProductsYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 69 | SelProductsYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 70 | SelProductsYear5Revenue | YEAR_5_REVENUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
