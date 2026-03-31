---
id: DOC-PO-PVO-SelectedProductsStg
doc_type: system-doc
title: "SelectedProductsStg — PVO Purchasing"
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
  - SelectedProductsStg
  - selectedproductsstg
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SelectedProductsStg

## 📌 Visão Geral

Extrai dados de staging de produtos selecionados em portfólios, em fase de processamento. Suporta o pipeline de carga e validação de dados de seleção antes da consolidação.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.SelectedProductsStg`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 413 | 15 | 1 | 365 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 59 atributos (17 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 12 atributos (11 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[ace_business_det_staging_b|ACE_BUSINESS_DET_STAGING_B]] — 32 atributos (31 BICC)
- [[ace_metric_config_b|ACE_METRIC_CONFIG_B]] — 16 atributos (16 BICC)
- [[ace_metric_goal|ACE_METRIC_GOAL]] — 13 atributos (13 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 65 atributos (65 BICC)
- [[ace_pf_scenario_tl|ACE_PF_SCENARIO_TL]] — 11 atributos (10 BICC)
- [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]] — 12 atributos (12 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_portfolio_revision|ACE_PORTFOLIO_REVISION]] — 9 atributos (9 BICC)
- [[ace_portfolio_tl|ACE_PORTFOLIO_TL]] — 22 atributos (20 BICC)
- [[ace_sel_products_staging|ACE_SEL_PRODUCTS_STAGING]] — 71 atributos (1 PKs, 71 BICC)
- [[fnd_lookup_values_b|FND_LOOKUP_VALUES_B]] — 32 atributos (32 BICC)
- [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]] — 14 atributos (13 BICC)

---

## ⚙️ Atributos

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptActualCost | ACTUAL_COST | — | — |
| 2 | ConceptActualPowerConsumption | ACTUAL_POWER_CONSUMPTION | — | — |
| 3 | ConceptActualWeight | ACTUAL_WEIGHT | — | — |
| 4 | ConceptAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | ConceptAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 6 | ConceptAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 7 | ConceptAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 8 | ConceptAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 9 | ConceptAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 10 | ConceptAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 11 | ConceptAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 12 | ConceptAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 13 | ConceptAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 14 | ConceptAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 15 | ConceptAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 16 | ConceptAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 17 | ConceptAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 18 | ConceptAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 19 | ConceptAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 20 | ConceptAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 21 | ConceptAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 22 | ConceptAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 23 | ConceptAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 24 | ConceptAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 25 | ConceptAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 26 | ConceptAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 27 | ConceptAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 28 | ConceptAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 29 | ConceptAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 30 | ConceptAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 31 | ConceptAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 32 | ConceptAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 33 | ConceptAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 34 | ConceptAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 35 | ConceptCompliance | COMPLIANCE | — | ✅ |
| 36 | ConceptConceptId | CONCEPT_ID | — | ✅ |
| 37 | ConceptCostVariance | COST_VARIANCE | — | — |
| 38 | ConceptCreatedBy | CREATED_BY | — | ✅ |
| 39 | ConceptCreationDate | CREATION_DATE | — | ✅ |
| 40 | ConceptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 41 | ConceptDueDate | DUE_DATE | — | ✅ |
| 42 | ConceptIsCurrent | IS_CURRENT | — | ✅ |
| 43 | ConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | ConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | ConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | ConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 47 | ConceptMasterId | MASTER_ID | — | ✅ |
| 48 | ConceptMorphedTo | MORPHED_TO | — | — |
| 49 | ConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 50 | ConceptOwnerId | OWNER_ID | — | — |
| 51 | ConceptPowerConsumptionVariance | POWER_CONSUMPTION_VARIANCE | — | — |
| 52 | ConceptPowerUnit | POWER_UNIT | — | ✅ |
| 53 | ConceptTargetCost | TARGET_COST | — | — |
| 54 | ConceptTargetPowerConsumption | TARGET_POWER_CONSUMPTION | — | — |
| 55 | ConceptTargetWeight | TARGET_WEIGHT | — | — |
| 56 | ConceptType | TYPE | — | ✅ |
| 57 | ConceptVersion | VERSION | — | ✅ |
| 58 | ConceptVolume | VOLUME | — | ✅ |
| 59 | ConceptWeightVariance | WEIGHT_VARIANCE | — | — |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTLConceptId | CONCEPT_ID | — | ✅ |
| 2 | ConceptTLCreatedBy | CREATED_BY | — | ✅ |
| 3 | ConceptTLCreationDate | CREATION_DATE | — | ✅ |
| 4 | ConceptTLDescription | DESCRIPTION | — | — |
| 5 | ConceptTLLanguage | LANGUAGE | — | ✅ |
| 6 | ConceptTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ConceptTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ConceptTLName | NAME | — | ✅ |
| 10 | ConceptTLNotes | NOTES | — | ✅ |
| 11 | ConceptTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ConceptTLSourceLang | SOURCE_LANG | — | ✅ |

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

### [[ace_business_det_staging_b|ACE_BUSINESS_DET_STAGING_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessDetailStgAllocatedBudget | ALLOCATED_BUDGET | — | ✅ |
| 2 | BusinessDetailStgAverageSellingPrice | AVERAGE_SELLING_PRICE | — | ✅ |
| 3 | BusinessDetailStgBreakEvenTime | BREAK_EVEN_TIME | — | ✅ |
| 4 | BusinessDetailStgBusinessDetStagingId | BUSINESS_DET_STAGING_ID | — | ✅ |
| 5 | BusinessDetailStgBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 6 | BusinessDetailStgCreatedBy | CREATED_BY | — | ✅ |
| 7 | BusinessDetailStgCreationDate | CREATION_DATE | — | ✅ |
| 8 | BusinessDetailStgDevelopmentEnd | DEVELOPMENT_END | — | ✅ |
| 9 | BusinessDetailStgDevelopmentStart | DEVELOPMENT_START | — | ✅ |
| 10 | BusinessDetailStgDiscountRate | DISCOUNT_RATE | — | ✅ |
| 11 | BusinessDetailStgEol | EOL | — | ✅ |
| 12 | BusinessDetailStgFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 13 | BusinessDetailStgFundingRequestFor | FUNDING_REQUEST_FOR | — | ✅ |
| 14 | BusinessDetailStgHighLevelDesign | HIGH_LEVEL_DESIGN | — | ✅ |
| 15 | BusinessDetailStgInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 16 | BusinessDetailStgLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | BusinessDetailStgLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | BusinessDetailStgLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | BusinessDetailStgLaunch | LAUNCH | — | ✅ |
| 20 | BusinessDetailStgNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 21 | BusinessDetailStgObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | BusinessDetailStgPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 23 | BusinessDetailStgProductLine | PRODUCT_LINE | — | ✅ |
| 24 | BusinessDetailStgProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 25 | BusinessDetailStgProposalProjectedCost | PROPOSAL_PROJECTED_COST | — | ✅ |
| 26 | BusinessDetailStgProposalProjectedRevenue | PROPOSAL_PROJECTED_REVENUE | — | ✅ |
| 27 | BusinessDetailStgRequirementsDefinition | REQUIREMENTS_DEFINITION | — | ✅ |
| 28 | BusinessDetailStgReturnOnInvestment | RETURN_ON_INVESTMENT | — | ✅ |
| 29 | BusinessDetailStgSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 30 | BusinessDetailStgSummary | SUMMARY | — | — |
| 31 | BusinessDetailStgTargetCost | TARGET_COST | — | ✅ |
| 32 | BusinessDetailStgUserId | USER_ID | — | ✅ |

### [[ace_metric_config_b|ACE_METRIC_CONFIG_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MetricConfigColumnName | COLUMN_NAME | — | ✅ |
| 2 | MetricConfigCreatedBy | CREATED_BY | — | ✅ |
| 3 | MetricConfigCreationDate | CREATION_DATE | — | ✅ |
| 4 | MetricConfigDataType | DATA_TYPE | — | ✅ |
| 5 | MetricConfigDefaultSelected | DEFAULT_SELECTED | — | ✅ |
| 6 | MetricConfigIsEnabled | IS_ENABLED | — | ✅ |
| 7 | MetricConfigIsSystem | IS_SYSTEM | — | ✅ |
| 8 | MetricConfigLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | MetricConfigLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | MetricConfigLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MetricConfigMaxValue | MAX_VALUE | — | ✅ |
| 12 | MetricConfigMetricConfigId | METRIC_CONFIG_ID | — | ✅ |
| 13 | MetricConfigMetricType | METRIC_TYPE | — | ✅ |
| 14 | MetricConfigMinValue | MIN_VALUE | — | ✅ |
| 15 | MetricConfigObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | MetricConfigTableName | TABLE_NAME | — | ✅ |

### [[ace_metric_goal|ACE_METRIC_GOAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GMetricGoaloalMaxValue | GOAL_MAX_VALUE | — | ✅ |
| 2 | MMetricGoaletricType | METRIC_TYPE | — | ✅ |
| 3 | MetricGoalBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 4 | MetricGoalBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 5 | MetricGoalCreatedBy | CREATED_BY | — | ✅ |
| 6 | MetricGoalCreationDate | CREATION_DATE | — | ✅ |
| 7 | MetricGoalGoalMinValue | GOAL_MIN_VALUE | — | ✅ |
| 8 | MetricGoalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | MetricGoalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | MetricGoalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MetricGoalMetricConfigId | METRIC_CONFIG_ID | — | ✅ |
| 12 | MetricGoalMetricGoalId | METRIC_GOAL_ID | — | ✅ |
| 13 | MetricGoalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

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

### [[ace_pf_scenario_tl|ACE_PF_SCENARIO_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScenarioTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | ScenarioTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | ScenarioTLDescription | DESCRIPTION | — | — |
| 4 | ScenarioTLLanguage | LANGUAGE | — | ✅ |
| 5 | ScenarioTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ScenarioTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ScenarioTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ScenarioTLName | NAME | — | ✅ |
| 9 | ScenarioTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ScenarioTLScenarioId | SCENARIO_ID | — | ✅ |
| 11 | ScenarioTLSourceLang | SOURCE_LANG | — | ✅ |

### [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioPlngPeriodCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioPlngPeriodCreationDate | CREATION_DATE | — | ✅ |
| 3 | PortfolioPlngPeriodEndPlanPeriodUnitId | END_PLAN_PERIOD_UNIT_ID | — | ✅ |
| 4 | PortfolioPlngPeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PortfolioPlngPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PortfolioPlngPeriodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PortfolioPlngPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PortfolioPlngPeriodPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 9 | PortfolioPlngPeriodPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 10 | PortfolioPlngPeriodPeriodStatus | PERIOD_STATUS | — | ✅ |
| 11 | PortfolioPlngPeriodPlanningPeriodId | PLANNING_PERIOD_ID | — | ✅ |
| 12 | PortfolioPlngPeriodStartPlanPeriodUnitId | START_PLAN_PERIOD_UNIT_ID | — | ✅ |

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

### [[ace_portfolio_revision|ACE_PORTFOLIO_REVISION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioRevisionCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioRevisionCreationDate | CREATION_DATE | — | ✅ |
| 3 | PortfolioRevisionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PortfolioRevisionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PortfolioRevisionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PortfolioRevisionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PortfolioRevisionPortfolioId | PORTFOLIO_ID | — | ✅ |
| 8 | PortfolioRevisionPortfolioRevisionId | PORTFOLIO_REVISION_ID | — | ✅ |
| 9 | PortfolioRevisionRevisionNumber | REVISION_NUMBER | — | ✅ |

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
| 65 | SelProductsStgSelProductsStagingId | SEL_PRODUCTS_STAGING_ID | 🔑 | ✅ |
| 66 | SelProductsStgSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 67 | SelProductsStgTrcc | TRCC | — | ✅ |
| 68 | SelProductsStgUserId | USER_ID | — | ✅ |
| 69 | SelProductsStgYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 70 | SelProductsStgYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 71 | SelProductsStgYear5Revenue | YEAR_5_REVENUE | — | ✅ |

### [[fnd_lookup_values_b|FND_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | LookupAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | LookupAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | LookupAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | LookupAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | LookupAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | LookupAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | LookupAttribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | LookupAttribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | LookupAttribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | LookupAttribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | LookupAttribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | LookupAttribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | LookupAttribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | LookupAttribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | LookupAttributeCategory1 | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | LookupCreatedBy | CREATED_BY | — | ✅ |
| 18 | LookupCreationDate | CREATION_DATE | — | ✅ |
| 19 | LookupDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 20 | LookupEnabledFlag | ENABLED_FLAG | — | ✅ |
| 21 | LookupEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 22 | LookupEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 23 | LookupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | LookupLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | LookupLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | LookupLookupCode | LOOKUP_CODE | — | ✅ |
| 27 | LookupLookupType | LOOKUP_TYPE | — | ✅ |
| 28 | LookupSetId | SET_ID | — | ✅ |
| 29 | LookupStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 30 | LookupTag | TAG | — | ✅ |
| 31 | LookupTerritoryCode | TERRITORY_CODE | — | ✅ |
| 32 | LookupViewApplicationId | VIEW_APPLICATION_ID | — | ✅ |

### [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | LookupTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | LookupTLDescription | DESCRIPTION | — | — |
| 4 | LookupTLEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | LookupTLLanguage | LANGUAGE | — | ✅ |
| 6 | LookupTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LookupTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LookupTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LookupTLLookupCode | LOOKUP_CODE | — | ✅ |
| 10 | LookupTLLookupType | LOOKUP_TYPE | — | ✅ |
| 11 | LookupTLMeaning | MEANING | — | ✅ |
| 12 | LookupTLSetId | SET_ID | — | ✅ |
| 13 | LookupTLSourceLang | SOURCE_LANG | — | ✅ |
| 14 | LookupTLViewApplicationId | VIEW_APPLICATION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
