---
id: DOC-PO-PVO-ProductProposalResourceUtilMonth
doc_type: system-doc
title: "ProductProposalResourceUtilMonth — PVO Purchasing"
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
  - ProductProposalResourceUtilMonth
  - productproposalresourceutilmonth
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProductProposalResourceUtilMonth

## 📌 Visão Geral

Extrai a utilização mensal de recursos em propostas de produto, comparando alocação versus capacidade. Permite análise de eficiência e otimização de alocação de recursos.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.ProductProposalResourceUtilMonth`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 243 | 8 | 1 | 242 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 18 atributos (18 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 12 atributos (12 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[acd_resource|ACD_RESOURCE]] — 15 atributos (15 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 67 atributos (67 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (1 PKs, 30 BICC)
- [[ace_resource_util_month_v|ACE_RESOURCE_UTIL_MONTH_V]] — 15 atributos (14 BICC)
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
| 1 | ProductProposalConceptMasterId1 | CONCEPT_MASTER_ID | — | ✅ |
| 2 | ProductProposalCreatedBy3 | CREATED_BY | — | ✅ |
| 3 | ProductProposalCreationDate3 | CREATION_DATE | — | ✅ |
| 4 | ProductProposalIsCloned | IS_CLONED | — | ✅ |
| 5 | ProductProposalIsLatest | IS_LATEST | — | ✅ |
| 6 | ProductProposalLastConceptVersion | LAST_CONCEPT_VERSION | — | ✅ |
| 7 | ProductProposalLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProductProposalLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ProductProposalLastUpdatedBy3 | LAST_UPDATED_BY | — | ✅ |
| 10 | ProductProposalObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProductProposalProductProposalId1 | PRODUCT_PROPOSAL_ID | — | ✅ |
| 12 | ProductProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 13 | ProductProposalProposalType | PROPOSAL_TYPE | — | ✅ |
| 14 | ProductProposalSrcProductProposalId | SRC_PRODUCT_PROPOSAL_ID | — | ✅ |
| 15 | ProductProposalVersion | VERSION | — | ✅ |

### [[acd_resource|ACD_RESOURCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductProposalResourceCreatedBy6 | CREATED_BY | — | ✅ |
| 2 | ProductProposalResourceCreationDate6 | CREATION_DATE | — | ✅ |
| 3 | ProductProposalResourceEndDate1 | END_DATE | — | ✅ |
| 4 | ProductProposalResourceLastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProductProposalResourceLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ProductProposalResourceLastUpdatedBy6 | LAST_UPDATED_BY | — | ✅ |
| 7 | ProductProposalResourceObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ProductProposalResourceProductProposalId3 | PRODUCT_PROPOSAL_ID | — | ✅ |
| 9 | ProductProposalResourceResourceCategory1 | RESOURCE_CATEGORY | — | ✅ |
| 10 | ProductProposalResourceResourceHeadcount | RESOURCE_HEADCOUNT | — | ✅ |
| 11 | ProductProposalResourceResourceId1 | RESOURCE_ID | — | ✅ |
| 12 | ProductProposalResourceResourcePool2 | RESOURCE_POOL | — | ✅ |
| 13 | ProductProposalResourceResourceStatus1 | RESOURCE_STATUS | — | ✅ |
| 14 | ProductProposalResourceResourceTrend | RESOURCE_TREND | — | ✅ |
| 15 | ProductProposalResourceStartDate1 | START_DATE | — | ✅ |

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

### [[ace_resource_util_month_v|ACE_RESOURCE_UTIL_MONTH_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceUtilMonthCalMonth1 | CAL_MONTH | — | ✅ |
| 2 | ResourceUtilMonthCalMonthCode1 | CAL_MONTH_CODE | — | ✅ |
| 3 | ResourceUtilMonthCalMonthEndDate1 | CAL_MONTH_END_DATE | — | ✅ |
| 4 | ResourceUtilMonthCalMonthStartDate1 | CAL_MONTH_START_DATE | — | ✅ |
| 5 | ResourceUtilMonthEndDate | END_DATE | — | ✅ |
| 6 | ResourceUtilMonthHeadCountMonth | HEAD_COUNT_MONTH | — | ✅ |
| 7 | ResourceUtilMonthHeadCountQuarter | HEAD_COUNT_QUARTER | — | ✅ |
| 8 | ResourceUtilMonthHeadCountYear | HEAD_COUNT_YEAR | — | ✅ |
| 9 | ResourceUtilMonthProductProposalId2 | PRODUCT_PROPOSAL_ID | — | ✅ |
| 10 | ResourceUtilMonthResourceCategory | RESOURCE_CATEGORY | — | ✅ |
| 11 | ResourceUtilMonthResourceId | RESOURCE_ID | — | ✅ |
| 12 | ResourceUtilMonthResourcePool1 | RESOURCE_POOL | — | ✅ |
| 13 | ResourceUtilMonthResourceSource | SOURCE | — | — |
| 14 | ResourceUtilMonthResourceStatus | RESOURCE_STATUS | — | ✅ |
| 15 | ResourceUtilMonthStartDate | START_DATE | — | ✅ |

### [[ace_selected_products|ACE_SELECTED_PRODUCTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SelectedProductsActualCost1 | ACTUAL_COST | — | ✅ |
| 2 | SelectedProductsActualDevFixedCost1 | ACTUAL_DEV_FIXED_COST | — | ✅ |
| 3 | SelectedProductsActualDevLaborCost1 | ACTUAL_DEV_LABOR_COST | — | ✅ |
| 4 | SelectedProductsActualDevMaterialCost1 | ACTUAL_DEV_MATERIAL_COST | — | ✅ |
| 5 | SelectedProductsActualDevVariableCost1 | ACTUAL_DEV_VARIABLE_COST | — | ✅ |
| 6 | SelectedProductsActualDevelopmentCost1 | ACTUAL_DEVELOPMENT_COST | — | ✅ |
| 7 | SelectedProductsActualProdFixedCost1 | ACTUAL_PROD_FIXED_COST | — | ✅ |
| 8 | SelectedProductsActualProdLaborCost1 | ACTUAL_PROD_LABOR_COST | — | ✅ |
| 9 | SelectedProductsActualProdMaterialCost1 | ACTUAL_PROD_MATERIAL_COST | — | ✅ |
| 10 | SelectedProductsActualProdVariableCost1 | ACTUAL_PROD_VARIABLE_COST | — | ✅ |
| 11 | SelectedProductsActualProductionCost1 | ACTUAL_PRODUCTION_COST | — | ✅ |
| 12 | SelectedProductsActualResources1 | ACTUAL_RESOURCES | — | ✅ |
| 13 | SelectedProductsActualRevenue1 | ACTUAL_REVENUE | — | ✅ |
| 14 | SelectedProductsAlignment1 | ALIGNMENT | — | ✅ |
| 15 | SelectedProductsBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 16 | SelectedProductsBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 17 | SelectedProductsBusinessUnitStrength | BUSINESS_UNIT_STRENGTH | — | ✅ |
| 18 | SelectedProductsCompetitiveAdvantage1 | COMPETITIVE_ADVANTAGE | — | ✅ |
| 19 | SelectedProductsConceptMasterId | CONCEPT_MASTER_ID | — | ✅ |
| 20 | SelectedProductsCostValueIndex1 | COST_VALUE_INDEX | — | ✅ |
| 21 | SelectedProductsCpi1 | CPI | — | ✅ |
| 22 | SelectedProductsCreatedBy2 | CREATED_BY | — | ✅ |
| 23 | SelectedProductsCreationDate2 | CREATION_DATE | — | ✅ |
| 24 | SelectedProductsExpectedCommercialValue1 | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
| 25 | SelectedProductsImpact1 | IMPACT | — | ✅ |
| 26 | SelectedProductsIncluded | INCLUDED | — | ✅ |
| 27 | SelectedProductsInternalRateOfReturn1 | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 28 | SelectedProductsLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 29 | SelectedProductsLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | SelectedProductsLastUpdatedBy2 | LAST_UPDATED_BY | — | ✅ |
| 31 | SelectedProductsMarketAttractiveness | MARKET_ATTRACTIVENESS | — | ✅ |
| 32 | SelectedProductsMarketGrowthPercent | MARKET_GROWTH_PERCENT | — | ✅ |
| 33 | SelectedProductsMarketSharePercent | MARKET_SHARE_PERCENT | — | ✅ |
| 34 | SelectedProductsNetPresentValue1 | NET_PRESENT_VALUE | — | ✅ |
| 35 | SelectedProductsObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | SelectedProductsPaybackPeriod1 | PAYBACK_PERIOD | — | ✅ |
| 37 | SelectedProductsPriority | PRIORITY | — | ✅ |
| 38 | SelectedProductsProbOfCommercialSuccess | PROB_OF_COMMERCIAL_SUCCESS | — | ✅ |
| 39 | SelectedProductsProbOfTechnicalSuccess | PROB_OF_TECHNICAL_SUCCESS | — | ✅ |
| 40 | SelectedProductsProductCategorization | PRODUCT_CATEGORIZATION | — | ✅ |
| 41 | SelectedProductsProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 42 | SelectedProductsProductStrategicFit | PRODUCT_STRATEGIC_FIT | — | ✅ |
| 43 | SelectedProductsProductStrategicImp | PRODUCT_STRATEGIC_IMP | — | ✅ |
| 44 | SelectedProductsProjDevCost1 | PROJ_DEV_COST | — | ✅ |
| 45 | SelectedProductsProjDevFixedCost1 | PROJ_DEV_FIXED_COST | — | ✅ |
| 46 | SelectedProductsProjDevLaborCost1 | PROJ_DEV_LABOR_COST | — | ✅ |
| 47 | SelectedProductsProjDevMaterialCost1 | PROJ_DEV_MATERIAL_COST | — | ✅ |
| 48 | SelectedProductsProjDevVariableCost1 | PROJ_DEV_VARIABLE_COST | — | ✅ |
| 49 | SelectedProductsProjProdCost1 | PROJ_PROD_COST | — | ✅ |
| 50 | SelectedProductsProjProdFixedCost1 | PROJ_PROD_FIXED_COST | — | ✅ |
| 51 | SelectedProductsProjProdLaborCost1 | PROJ_PROD_LABOR_COST | — | ✅ |
| 52 | SelectedProductsProjProdMaterialCost1 | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 53 | SelectedProductsProjProdVariableCost1 | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 54 | SelectedProductsProjectedCost1 | PROJECTED_COST | — | ✅ |
| 55 | SelectedProductsProjectedResources1 | PROJECTED_RESOURCES | — | ✅ |
| 56 | SelectedProductsProjectedRevenue1 | PROJECTED_REVENUE | — | ✅ |
| 57 | SelectedProductsRank | RANK | — | ✅ |
| 58 | SelectedProductsResourceValueIndex1 | RESOURCE_VALUE_INDEX | — | ✅ |
| 59 | SelectedProductsRiskNumberic | RISK_NUMBERIC | — | ✅ |
| 60 | SelectedProductsRiskSubjective | RISK_SUBJECTIVE | — | ✅ |
| 61 | SelectedProductsRndKnowHow1 | RND_KNOW_HOW | — | ✅ |
| 62 | SelectedProductsRoi1 | ROI | — | ✅ |
| 63 | SelectedProductsRpi1 | RPI | — | ✅ |
| 64 | SelectedProductsScore | SCORE | — | ✅ |
| 65 | SelectedProductsSelectedProductsId | SELECTED_PRODUCTS_ID | — | ✅ |
| 66 | SelectedProductsSelectedProductsId1 | SELECTED_PRODUCTS_ID | — | ✅ |
| 67 | SelectedProductsSupplyChainFit1 | SUPPLY_CHAIN_FIT | — | ✅ |
| 68 | SelectedProductsTrcc1 | TRCC | — | ✅ |
| 69 | SelectedProductsYear2Revenue1 | YEAR_2_REVENUE | — | ✅ |
| 70 | SelectedProductsYear3Revenue1 | YEAR_3_REVENUE | — | ✅ |
| 71 | SelectedProductsYear5Revenue1 | YEAR_5_REVENUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
