---
id: DOC-PO-PVO-ProductProposalResourceCapacityMonth
doc_type: system-doc
title: "ProductProposalResourceCapacityMonth — PVO Purchasing"
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
  - ProductProposalResourceCapacityMonth
  - productproposalresourcecapacitymonth
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductProposalResourceCapacityMonth

## 📌 Visão Geral

Extrai a capacidade mensal de recursos alocados a propostas de produto, por conceito e cenário. Suporta planejamento de capacidade e identificação de gargalos produtivos ao longo do tempo.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductProposalResourceCapacityMonth`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 229 | 7 | 1 | 229 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 18 atributos (18 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 12 atributos (12 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 67 atributos (67 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (1 PKs, 30 BICC)
- [[ace_resource_capacity_month_v|ACE_RESOURCE_CAPACITY_MONTH_V]] — 16 atributos (16 BICC)
- [[ace_selected_products|ACE_SELECTED_PRODUCTS]] — 71 atributos (71 BICC)

---

## ⚙️ Atributos

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptCompliance | COMPLIANCE | — | ✅ |
| 2 | ConceptConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptConceptId1 | CONCEPT_ID | — | ✅ |
| 4 | ConceptCreatedBy4 | CREATED_BY | — | ✅ |
| 5 | ConceptCreationDate4 | CREATION_DATE | — | ✅ |
| 6 | ConceptCurrencyCode1 | CURRENCY_CODE | — | ✅ |
| 7 | ConceptDueDate | DUE_DATE | — | ✅ |
| 8 | ConceptIsCurrent | IS_CURRENT | — | ✅ |
| 9 | ConceptLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 10 | ConceptLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ConceptLastUpdatedBy4 | LAST_UPDATED_BY | — | ✅ |
| 12 | ConceptLifecyclePhase1 | LIFECYCLE_PHASE | — | ✅ |
| 13 | ConceptMasterId | MASTER_ID | — | ✅ |
| 14 | ConceptObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ConceptPowerUnit | POWER_UNIT | — | ✅ |
| 16 | ConceptType | TYPE | — | ✅ |
| 17 | ConceptVersion1 | VERSION | — | ✅ |
| 18 | ConceptVolume | VOLUME | — | ✅ |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTranslationConceptId2 | CONCEPT_ID | — | ✅ |
| 2 | ConceptTranslationCreatedBy5 | CREATED_BY | — | ✅ |
| 3 | ConceptTranslationCreationDate5 | CREATION_DATE | — | ✅ |
| 4 | ConceptTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | ConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | ConceptTranslationLastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTranslationLastUpdateLogin5 | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ConceptTranslationLastUpdatedBy5 | LAST_UPDATED_BY | — | ✅ |
| 9 | ConceptTranslationName | NAME | — | ✅ |
| 10 | ConceptTranslationNotes | NOTES | — | ✅ |
| 11 | ConceptTranslationObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrdProposalConceptMasterId1 | CONCEPT_MASTER_ID | — | ✅ |
| 2 | PrdProposalCreatedBy3 | CREATED_BY | — | ✅ |
| 3 | PrdProposalCreationDate3 | CREATION_DATE | — | ✅ |
| 4 | PrdProposalIsCloned | IS_CLONED | — | ✅ |
| 5 | PrdProposalIsLatest | IS_LATEST | — | ✅ |
| 6 | PrdProposalLastConceptVersion | LAST_CONCEPT_VERSION | — | ✅ |
| 7 | PrdProposalLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | PrdProposalLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PrdProposalLastUpdatedBy3 | LAST_UPDATED_BY | — | ✅ |
| 10 | PrdProposalObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PrdProposalProductProposalId1 | PRODUCT_PROPOSAL_ID | — | ✅ |
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
| 19 | ScenarioCreatedBy1 | CREATED_BY | — | ✅ |
| 20 | ScenarioCreationDate1 | CREATION_DATE | — | ✅ |
| 21 | ScenarioCreator | CREATOR | — | ✅ |
| 22 | ScenarioDateCreated | DATE_CREATED | — | ✅ |
| 23 | ScenarioExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 24 | ScenarioImpact | IMPACT | — | ✅ |
| 25 | ScenarioInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 26 | ScenarioIsEnabled | IS_ENABLED | — | ✅ |
| 27 | ScenarioLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 28 | ScenarioLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | ScenarioLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 30 | ScenarioMarginDeviation | MARGIN_DEVIATION | — | ✅ |
| 31 | ScenarioNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 32 | ScenarioObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | ScenarioPaybackPeriod | PAYBACK_PERIOD | — | ✅ |
| 34 | ScenarioPortfolioId1 | PORTFOLIO_ID | — | ✅ |
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
| 59 | ScenarioScenarioBaselineDate | SCENARIO_BASELINE_DATE | — | ✅ |
| 60 | ScenarioScenarioDiscountRate | SCENARIO_DISCOUNT_RATE | — | ✅ |
| 61 | ScenarioScenarioId | SCENARIO_ID | — | ✅ |
| 62 | ScenarioStatus | STATUS | — | ✅ |
| 63 | ScenarioSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 64 | ScenarioTrcc | TRCC | — | ✅ |
| 65 | ScenarioYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 66 | ScenarioYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 67 | ScenarioYear5Revenue | YEAR_5_REVENUE | — | ✅ |

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
| 20 | PortfolioPortfolioId | PORTFOLIO_ID | 🔑 | ✅ |
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

### [[ace_resource_capacity_month_v|ACE_RESOURCE_CAPACITY_MONTH_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResCapacityMonthCalMonth | CAL_MONTH | — | ✅ |
| 2 | ResCapacityMonthCalMonthCode | CAL_MONTH_CODE | — | ✅ |
| 3 | ResCapacityMonthCalMonthEndDate | CAL_MONTH_END_DATE | — | ✅ |
| 4 | ResCapacityMonthCalMonthStartDate | CAL_MONTH_START_DATE | — | ✅ |
| 5 | ResCapacityMonthDuration | DURATION | — | ✅ |
| 6 | ResCapacityMonthHeadcountMonth | HEADCOUNT_MONTH | — | ✅ |
| 7 | ResCapacityMonthHeadcountPpu | HEADCOUNT_PPU | — | ✅ |
| 8 | ResCapacityMonthHeadcountQuarter | HEADCOUNT_QUARTER | — | ✅ |
| 9 | ResCapacityMonthHeadcountYear | HEADCOUNT_YEAR | — | ✅ |
| 10 | ResCapacityMonthParentQuarter | PARENT_QUARTER | — | ✅ |
| 11 | ResCapacityMonthPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 12 | ResCapacityMonthPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 13 | ResCapacityMonthPortfolioId2 | PORTFOLIO_ID | — | ✅ |
| 14 | ResCapacityMonthResourceCapacityId | RESOURCE_CAPACITY_ID | — | ✅ |
| 15 | ResCapacityMonthResourcePool | RESOURCE_POOL | — | ✅ |
| 16 | ResCapacityMonthUnitId | UNIT_ID | — | ✅ |

### [[ace_selected_products|ACE_SELECTED_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SelProductsActualCost1 | ACTUAL_COST | — | ✅ |
| 2 | SelProductsActualDevFixedCost1 | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | SelProductsActualDevLaborCost1 | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | SelProductsActualDevMaterialCost1 | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | SelProductsActualDevVariableCost1 | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | SelProductsActualDevelopmentCost1 | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | SelProductsActualProdFixedCost1 | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 8 | SelProductsActualProdLaborCost1 | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 9 | SelProductsActualProdMaterialCost1 | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 10 | SelProductsActualProdVariableCost1 | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 11 | SelProductsActualProductionCost1 | ACTUAL_PRODUCTION_COST | — | ✅ |
| 12 | SelProductsActualResources1 | ACTUAL_RESOURCES | — | ✅ |
| 13 | SelProductsActualRevenue1 | ACTUAL_REVENUE | — | ✅ |
| 14 | SelProductsAlignment1 | ALIGNMENT | — | ✅ |
| 15 | SelProductsBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 16 | SelProductsBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 17 | SelProductsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 18 | SelProductsCompetitiveAdvantage1 | COMPETITIVE_ADVANTAGE | — | ✅ |
| 19 | SelProductsConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 20 | SelProductsCostValueIndex1 | COST_VALUE_INDEX | — | ✅ |
| 21 | SelProductsCpi1 | CPI | — | ✅ |
| 22 | SelProductsCreatedBy2 | CREATED_BY | — | ✅ |
| 23 | SelProductsCreationDate2 | CREATION_DATE | — | ✅ |
| 24 | SelProductsExpectedCommercialValue1 | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 25 | SelProductsImpact1 | IMPACT | — | ✅ |
| 26 | SelProductsIncluded | INCLUDED | — | ✅ |
| 27 | SelProductsInternalRateOfReturn1 | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 28 | SelProductsLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 29 | SelProductsLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | SelProductsLastUpdatedBy2 | LAST_UPDATED_BY | — | ✅ |
| 31 | SelProductsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 32 | SelProductsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 33 | SelProductsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 34 | SelProductsNetPresentValue1 | NET_PRESENT_VALUE | — | ✅ |
| 35 | SelProductsObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | SelProductsPaybackPeriod1 | PAYBACK_PERIOD | — | ✅ |
| 37 | SelProductsPriority | PRIORITY | — | ✅ |
| 38 | SelProductsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 39 | SelProductsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 40 | SelProductsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 41 | SelProductsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 42 | SelProductsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 43 | SelProductsProductStrategicImp | PRODUCT_STRATEGIC_IMP | — | ✅ |
| 44 | SelProductsProjDevCost1 | PROJ_DEV_COST | — | ✅ |
| 45 | SelProductsProjDevFixedCost1 | PROJ_DEV_FIXED_COST | — | ✅ |
| 46 | SelProductsProjDevLaborCost1 | PROJ_DEV_LABOR_COST | — | ✅ |
| 47 | SelProductsProjDevMaterialCost1 | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 48 | SelProductsProjDevVariableCost1 | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 49 | SelProductsProjProdCost1 | PROJ_PROD_COST | — | ✅ |
| 50 | SelProductsProjProdFixedCost1 | PROJ_PROD_FIXED_COST | — | ✅ |
| 51 | SelProductsProjProdLaborCost1 | PROJ_PROD_LABOR_COST | — | ✅ |
| 52 | SelProductsProjProdMaterialCost1 | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 53 | SelProductsProjProdVariableCost1 | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 54 | SelProductsProjectedCost1 | PROJECTED_COST | — | ✅ |
| 55 | SelProductsProjectedResources1 | PROJECTED_RESOURCES | — | ✅ |
| 56 | SelProductsProjectedRevenue1 | PROJECTED_REVENUE | — | ✅ |
| 57 | SelProductsRank | RANK | — | ✅ |
| 58 | SelProductsResourceValueIndex1 | RESOURCE_VALUE_INDEX | — | ✅ |
| 59 | SelProductsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 60 | SelProductsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 61 | SelProductsRndKnowHow1 | RND_KNOW_HOW | — | ✅ |
| 62 | SelProductsRoi1 | ROI | — | ✅ |
| 63 | SelProductsRpi1 | RPI | — | ✅ |
| 64 | SelProductsScore | SCORE | — | ✅ |
| 65 | SelProductsSelectedProductsId | SELECTED_PRODUCTS_ID | — | ✅ |
| 66 | SelProductsSelectedProductsId1 | SELECTED_PRODUCTS_ID | — | ✅ |
| 67 | SelProductsSupplyChainFit1 | SUPPLY_CHAIN_FIT | — | ✅ |
| 68 | SelProductsTrcc1 | TRCC | — | ✅ |
| 69 | SelProductsYear2Revenue1 | YEAR_2_REVENUE | — | ✅ |
| 70 | SelProductsYear3Revenue1 | YEAR_3_REVENUE | — | ✅ |
| 71 | SelProductsYear5Revenue1 | YEAR_5_REVENUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
