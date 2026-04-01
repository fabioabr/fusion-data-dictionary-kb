---
id: DOC-PO-PVO-ProductProposalRevenueStg
doc_type: system-doc
title: "ProductProposalRevenueStg — PVO Purchasing"
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
  - ProductProposalRevenueStg
  - productproposalrevenuestg
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductProposalRevenueStg

## 📌 Visão Geral

Extrai dados de staging de receitas de propostas de produto em processamento. Suporta o pipeline de carga e validação de dados financeiros antes da consolidação.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductProposalRevenueStg`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 197 | 5 | 1 | 197 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 65 atributos (65 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_revenue_staging|ACE_REVENUE_STAGING]] — 16 atributos (1 PKs, 16 BICC)
- [[ace_sel_products_staging|ACE_SEL_PRODUCTS_STAGING]] — 71 atributos (71 BICC)

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

### [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScenarioActualCost | ACTUAL_COST | — | ✅ |
| 2 | ScenarioActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | ScenarioActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | ScenarioActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
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
| 24 | PortfolioRevenueExpectation | REVENUE_EXPECTATION | — | ✅ |
| 25 | PortfolioSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 26 | PortfolioTargetCost | TARGET_COST | — | ✅ |
| 27 | PortfolioTargetMargin | TARGET_MARGIN | — | ✅ |
| 28 | PortfolioTargetRevenue | TARGET_REVENUE | — | ✅ |
| 29 | PortfolioWorkflow | WORKFLOW | — | ✅ |
| 30 | ProposedPlanId | PROPOSED_PLAN_ID | — | ✅ |

### [[ace_revenue_staging|ACE_REVENUE_STAGING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrdProposalRevenueStgCreatedBy | CREATED_BY | — | ✅ |
| 2 | PrdProposalRevenueStgCreationDate | CREATION_DATE | — | ✅ |
| 3 | PrdProposalRevenueStgEndDate | END_DATE | — | ✅ |
| 4 | PrdProposalRevenueStgLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PrdProposalRevenueStgLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PrdProposalRevenueStgLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PrdProposalRevenueStgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PrdProposalRevenueStgProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 9 | PrdProposalRevenueStgRevenueAmount | REVENUE_AMOUNT | — | ✅ |
| 10 | PrdProposalRevenueStgRevenueCategory | REVENUE_CATEGORY | — | ✅ |
| 11 | PrdProposalRevenueStgRevenueStagingId | REVENUE_STAGING_ID | 🔑 | ✅ |
| 12 | PrdProposalRevenueStgRevenueStatus | REVENUE_STATUS | — | ✅ |
| 13 | PrdProposalRevenueStgRevenueTrend | REVENUE_TREND | — | ✅ |
| 14 | PrdProposalRevenueStgRevenueType | REVENUE_TYPE | — | ✅ |
| 15 | PrdProposalRevenueStgStartDate | START_DATE | — | ✅ |
| 16 | PrdProposalRevenueStgUserId | USER_ID | — | ✅ |

### [[ace_sel_products_staging|ACE_SEL_PRODUCTS_STAGING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SelProductsStgActualCost | ACTUAL_COST | — | ✅ |
| 2 | SelProductsStgActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | SelProductsStgActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | SelProductsStgActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | SelProductsStgActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | SelProductsStgActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | SelProductsStgActualProdFixedCost | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 8 | SelProductsStgActualProdLaborCost | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 9 | SelProductsStgActualProdMaterialCost | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 10 | SelProductsStgActualProdVariableCost | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 11 | SelProductsStgActualProductionCost | ACTUAL_PRODUCTION_COST | — | ✅ |
| 12 | SelProductsStgActualResources | ACTUAL_RESOURCES | — | ✅ |
| 13 | SelProductsStgActualRevenue | ACTUAL_REVENUE | — | ✅ |
| 14 | SelProductsStgAlignment | ALIGNMENT | — | ✅ |
| 15 | SelProductsStgBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 16 | SelProductsStgBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 17 | SelProductsStgBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 18 | SelProductsStgCompetitiveAdvantage | COMPETITIVE_ADVANTAGE | — | ✅ |
| 19 | SelProductsStgConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 20 | SelProductsStgCostValueIndex | COST_VALUE_INDEX | — | ✅ |
| 21 | SelProductsStgCpi | CPI | — | ✅ |
| 22 | SelProductsStgCreatedBy | CREATED_BY | — | ✅ |
| 23 | SelProductsStgCreationDate | CREATION_DATE | — | ✅ |
| 24 | SelProductsStgExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 25 | SelProductsStgImpact | IMPACT | — | ✅ |
| 26 | SelProductsStgIncluded | INCLUDED | — | ✅ |
| 27 | SelProductsStgInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 28 | SelProductsStgLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | SelProductsStgLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | SelProductsStgLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | SelProductsStgMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 32 | SelProductsStgMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 33 | SelProductsStgMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 34 | SelProductsStgNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 35 | SelProductsStgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | SelProductsStgPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 37 | SelProductsStgPriority | PRIORITY | — | ✅ |
| 38 | SelProductsStgProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 39 | SelProductsStgProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 40 | SelProductsStgProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 41 | SelProductsStgProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 42 | SelProductsStgProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 43 | SelProductsStgProductStrategicImp | PRODUCT_STRATEGIC_IMP | — | ✅ |
| 44 | SelProductsStgProjDevCost | PROJ_DEV_COST | — | ✅ |
| 45 | SelProductsStgProjDevFixedCost | PROJ_DEV_FIXED_COST | — | ✅ |
| 46 | SelProductsStgProjDevLaborCost | PROJ_DEV_LABOR_COST | — | ✅ |
| 47 | SelProductsStgProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 48 | SelProductsStgProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 49 | SelProductsStgProjProdCost | PROJ_PROD_COST | — | ✅ |
| 50 | SelProductsStgProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 51 | SelProductsStgProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 52 | SelProductsStgProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 53 | SelProductsStgProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 54 | SelProductsStgProjectedCost | PROJECTED_COST | — | ✅ |
| 55 | SelProductsStgProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 56 | SelProductsStgProjectedRevenue | PROJECTED_REVENUE | — | ✅ |
| 57 | SelProductsStgRank | RANK | — | ✅ |
| 58 | SelProductsStgResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 59 | SelProductsStgRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 60 | SelProductsStgRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 61 | SelProductsStgRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 62 | SelProductsStgRoi | ROI | — | ✅ |
| 63 | SelProductsStgRpi | RPI | — | ✅ |
| 64 | SelProductsStgScore | SCORE | — | ✅ |
| 65 | SelProductsStgSelProductsStagingId | SEL_PRODUCTS_STAGING_ID | — | ✅ |
| 66 | SelProductsStgSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 67 | SelProductsStgTrcc | TRCC | — | ✅ |
| 68 | SelProductsStgUserId | USER_ID | — | ✅ |
| 69 | SelProductsStgYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 70 | SelProductsStgYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 71 | SelProductsStgYear5Revenue | YEAR_5_REVENUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
