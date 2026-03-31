---
id: DOC-PO-PVO-ProductProposalCost
doc_type: system-doc
title: "ProductProposalCost — PVO Purchasing"
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
  - ProductProposalCost
  - productproposalcost
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductProposalCost

## 📌 Visão Geral

Extrai custos de propostas de produto, incluindo componentes de preço, markup e período. Permite análise de viabilidade financeira, composição de custos e comparação entre cenários.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductProposalCost`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 195 | 5 | 1 | 195 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acd_costs|ACD_COSTS]] — 15 atributos (1 PKs, 15 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 65 atributos (65 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_selected_products|ACE_SELECTED_PRODUCTS]] — 70 atributos (70 BICC)

---

## ⚙️ Atributos

### [[acd_costs|ACD_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrdProposalCostCostAmount | COST_AMOUNT | — | ✅ |
| 2 | PrdProposalCostCostCategory | COST_CATEGORY | — | ✅ |
| 3 | PrdProposalCostCostId | COST_ID | 🔑 | ✅ |
| 4 | PrdProposalCostCostStatus | COST_STATUS | — | ✅ |
| 5 | PrdProposalCostCostTrend | COST_TREND | — | ✅ |
| 6 | PrdProposalCostCostType | COST_TYPE | — | ✅ |
| 7 | PrdProposalCostCreatedBy | CREATED_BY | — | ✅ |
| 8 | PrdProposalCostCreationDate | CREATION_DATE | — | ✅ |
| 9 | PrdProposalCostEndDate | END_DATE | — | ✅ |
| 10 | PrdProposalCostLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PrdProposalCostLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PrdProposalCostLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PrdProposalCostObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PrdProposalCostProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 15 | PrdProposalCostStartDate | START_DATE | — | ✅ |

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

### [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 2 | ScenarioActualCost | ACTUAL_COST | — | ✅ |
| 3 | ScenarioActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 4 | ScenarioActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 5 | ScenarioActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 6 | ScenarioActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 7 | ScenarioActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 8 | ScenarioActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 9 | ScenarioActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 10 | ScenarioActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 11 | ScenarioActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 12 | ScenarioActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 13 | ScenarioActualResources | ACTUAL_RESOURCES | — | ✅ |
| 14 | ScenarioActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 15 | ScenarioAlignment | ALIGNMENT | — | ✅ |
| 16 | ScenarioCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 17 | ScenarioCostDeviation | COST_DEVIATION | — | ✅ |
| 18 | ScenarioCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 19 | ScenarioCpi | CPI | — | ✅ |
| 20 | ScenarioCreatedBy | CREATED_BY | — | ✅ |
| 21 | ScenarioCreationDate | CREATION_DATE | — | ✅ |
| 22 | ScenarioCreator | CREATOR | — | ✅ |
| 23 | ScenarioDateCreated | DATE_CREATED | — | ✅ |
| 24 | ScenarioExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 25 | ScenarioImpact | IMPACT | — | ✅ |
| 26 | ScenarioInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 27 | ScenarioIsEnabled | IS_ENABLED | — | ✅ |
| 28 | ScenarioLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | ScenarioLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | ScenarioLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | ScenarioMarginDeviation | MARGIN_DEVIATION | — | ✅ |
| 32 | ScenarioNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 33 | ScenarioObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 34 | ScenarioPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 35 | ScenarioPortfolioId | PORTFOLIO_ID | — | ✅ |
| 36 | ScenarioPortfolioRevisionId | PORTFOLIO_REVISION_ID | — | ✅ |
| 37 | ScenarioPortfolioRiskNumeric | PORTFOLIO_RISK_NUMERIC | — | ✅ |
| 38 | ScenarioPortfolioRiskSubjective | PORTFOLIO_RISK_SUBJECTIVE | — | ✅ |
| 39 | ScenarioPortfolioStrategicFit | PORTFOLIO_STRATEGIC_FIT | — | ✅ |
| 40 | ScenarioPortfolioStrategicImp | PORTFOLIO_STRATEGIC_IMP | — | ✅ |
| 41 | ScenarioProjDevCost | PROJ_DEV_COST | — | ✅ |
| 42 | ScenarioProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 43 | ScenarioProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 44 | ScenarioProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 45 | ScenarioProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 46 | ScenarioProjProdCost | PROJ_PROD_COST | — | ✅ |
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
| 25 | PortfolioSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 26 | PortfolioTargetCost | TARGET_COST | — | ✅ |
| 27 | PortfolioTargetMargin | TARGET_MARGIN | — | ✅ |
| 28 | PortfolioTargetRevenue | TARGET_REVENUE | — | ✅ |
| 29 | PortfolioWorkflow | WORKFLOW | — | ✅ |
| 30 | RPortfolioevenueExpectation | REVENUE_EXPECTATION | — | ✅ |

### [[ace_selected_products|ACE_SELECTED_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SelProductsActualCost | ACTUAL_COST | — | ✅ |
| 2 | SelProductsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | SelProductsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | SelProductsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | SelProductsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | SelProductsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | SelProductsActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 8 | SelProductsActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 9 | SelProductsActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 10 | SelProductsActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 11 | SelProductsActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 12 | SelProductsActualResources | ACTUAL_RESOURCES | — | ✅ |
| 13 | SelProductsActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 14 | SelProductsAlignment | ALIGNMENT | — | ✅ |
| 15 | SelProductsBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 16 | SelProductsBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 17 | SelProductsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 18 | SelProductsCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 19 | SelProductsConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 20 | SelProductsCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 21 | SelProductsCpi | CPI | — | ✅ |
| 22 | SelProductsCreatedBy | CREATED_BY | — | ✅ |
| 23 | SelProductsCreationDate | CREATION_DATE | — | ✅ |
| 24 | SelProductsExpectedCommercialValue1 | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 25 | SelProductsImpact | IMPACT | — | ✅ |
| 26 | SelProductsIncluded | INCLUDED | — | ✅ |
| 27 | SelProductsInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 28 | SelProductsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | SelProductsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | SelProductsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | SelProductsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 32 | SelProductsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 33 | SelProductsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 34 | SelProductsNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 35 | SelProductsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | SelProductsPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 37 | SelProductsPriority | PRIORITY | — | ✅ |
| 38 | SelProductsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 39 | SelProductsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 40 | SelProductsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 41 | SelProductsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 42 | SelProductsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 43 | SelProductsProductStrategicImp | PRODUCT_STRATEGIC_IMP | — | ✅ |
| 44 | SelProductsProjDevCost | PROJ_DEV_COST | — | ✅ |
| 45 | SelProductsProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 46 | SelProductsProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 47 | SelProductsProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
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
