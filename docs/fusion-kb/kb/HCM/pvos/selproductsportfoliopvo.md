---
id: DOC-HCM-PVO-SelProductsPortfolioPVO
doc_type: system-doc
title: "SelProductsPortfolioPVO — PVO Human Capital Management"
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
  - SelProductsPortfolioPVO
  - selproductsportfoliopvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SelProductsPortfolioPVO

## 📌 Visão Geral

Disponibiliza produtos selecionados em portfólios com dados financeiros e de arquivamento. Suporta gestão de portfólio de produtos e priorização de investimentos.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.SelProductsPortfolioPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 124 | 3 | 1 | 122 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_portfolio_tl|ACE_PORTFOLIO_TL]] — 22 atributos (20 BICC)
- [[ace_selected_products|ACE_SELECTED_PRODUCTS]] — 72 atributos (1 PKs, 72 BICC)

---

## ⚙️ Atributos

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

### [[ace_portfolio_tl|ACE_PORTFOLIO_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioTLCreatedCreatedBy | CREATED_BY | — | ✅ |
| 3 | PortfolioTLCreatedCreationDate | CREATION_DATE | — | ✅ |
| 4 | PortfolioTLCreatedDescription | DESCRIPTION | — | — |
| 5 | PortfolioTLCreatedLanguage | LANGUAGE | — | ✅ |
| 6 | PortfolioTLCreatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PortfolioTLCreatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PortfolioTLCreatedLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PortfolioTLCreatedName | NAME | — | ✅ |
| 10 | PortfolioTLCreatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PortfolioTLCreatedPortfolioId | PORTFOLIO_ID | — | ✅ |
| 12 | PortfolioTLCreatedSourceLang | SOURCE_LANG | — | ✅ |
| 13 | PortfolioTLCreationDate | CREATION_DATE | — | ✅ |
| 14 | PortfolioTLDescription | DESCRIPTION | — | — |
| 15 | PortfolioTLLanguage | LANGUAGE | — | ✅ |
| 16 | PortfolioTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | PortfolioTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | PortfolioTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | PortfolioTLName | NAME | — | ✅ |
| 20 | PortfolioTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PortfolioTLPortfolioId | PORTFOLIO_ID | — | ✅ |
| 22 | PortfolioTLSourceLang | SOURCE_LANG | — | ✅ |

### [[ace_selected_products|ACE_SELECTED_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SelProductsActualCost | ACTUAL_COST | — | ✅ |
| 2 | SelProductsActualDevFixedCost | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | SelProductsActualDevLaborCost | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | SelProductsActualDevMaterialCost | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | SelProductsActualDevVariableCost | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | SelProductsActualDevelopmentCost | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | SelProductsActualMargin | ACTUAL_MARGIN | — | ✅ |
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
| 48 | SelProductsProjDevMaterialCost | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 49 | SelProductsProjDevVariableCost | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 50 | SelProductsProjProdCost | PROJ_PROD_COST | — | ✅ |
| 51 | SelProductsProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 52 | SelProductsProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 53 | SelProductsProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 54 | SelProductsProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 55 | SelProductsProjectedCost | PROJECTED_COST | — | ✅ |
| 56 | SelProductsProjectedMargin | PROJECTED_MARGIN | — | ✅ |
| 57 | SelProductsProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 58 | SelProductsProjectedRevenue | PROJECTED_REVENUE | — | ✅ |
| 59 | SelProductsRank | RANK | — | ✅ |
| 60 | SelProductsResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 61 | SelProductsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 62 | SelProductsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 63 | SelProductsRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 64 | SelProductsRoi | ROI | — | ✅ |
| 65 | SelProductsRpi | RPI | — | ✅ |
| 66 | SelProductsScore | SCORE | — | ✅ |
| 67 | SelProductsSelectedProductsId | SELECTED_PRODUCTS_ID | 🔑 | ✅ |
| 68 | SelProductsSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 69 | SelProductsTrcc | TRCC | — | ✅ |
| 70 | SelProductsYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 71 | SelProductsYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 72 | SelProductsYear5Revenue | YEAR_5_REVENUE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
