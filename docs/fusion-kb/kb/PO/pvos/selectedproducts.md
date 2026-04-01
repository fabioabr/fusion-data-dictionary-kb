---
id: DOC-PO-PVO-SelectedProducts
doc_type: system-doc
title: "SelectedProducts — PVO Purchasing"
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
  - SelectedProducts
  - selectedproducts
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SelectedProducts

## 📌 Visão Geral

Extrai produtos selecionados em portfólios de planejamento, com propostas, conceitos e detalhes de negócio. Suporta análise de decisões de investimento e rastreabilidade de seleções estratégicas.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.SelectedProducts`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 412 | 15 | 1 | 364 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[acd_business_details_b|ACD_BUSINESS_DETAILS_B]] — 32 atributos (31 BICC)
- [[acd_concept_b|ACD_CONCEPT_B]] — 59 atributos (17 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 12 atributos (11 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (15 BICC)
- [[ace_metric_config_b|ACE_METRIC_CONFIG_B]] — 16 atributos (16 BICC)
- [[ace_metric_goal|ACE_METRIC_GOAL]] — 13 atributos (13 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 65 atributos (65 BICC)
- [[ace_pf_scenario_tl|ACE_PF_SCENARIO_TL]] — 11 atributos (10 BICC)
- [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]] — 12 atributos (12 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_portfolio_revision|ACE_PORTFOLIO_REVISION]] — 9 atributos (9 BICC)
- [[ace_portfolio_tl|ACE_PORTFOLIO_TL]] — 22 atributos (20 BICC)
- [[ace_selected_products|ACE_SELECTED_PRODUCTS]] — 70 atributos (1 PKs, 70 BICC)
- [[fnd_lookup_values_b|FND_LOOKUP_VALUES_B]] — 32 atributos (32 BICC)
- [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]] — 14 atributos (13 BICC)

---

## ⚙️ Atributos

### [[acd_business_details_b|ACD_BUSINESS_DETAILS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessDetailAllocatedBudget | ALLOCATED_BUDGET | — | ✅ |
| 2 | BusinessDetailAverageSellingPrice | AVERAGE_SELLING_PRICE | — | ✅ |
| 3 | BusinessDetailBaselineDate | BASELINE_DATE | — | ✅ |
| 4 | BusinessDetailBreakEvenTime | BREAK_EVEN_TIME | — | ✅ |
| 5 | BusinessDetailBusinessDetailId | BUSINESS_DETAIL_ID | — | ✅ |
| 6 | BusinessDetailBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 7 | BusinessDetailCreatedBy | CREATED_BY | — | ✅ |
| 8 | BusinessDetailCreationDate | CREATION_DATE | — | ✅ |
| 9 | BusinessDetailDevelopmentEnd | DEVELOPMENT_END | — | ✅ |
| 10 | BusinessDetailDevelopmentStart | DEVELOPMENT_START | — | ✅ |
| 11 | BusinessDetailDiscountRate | DISCOUNT_RATE | — | ✅ |
| 12 | BusinessDetailEol | EOL | — | ✅ |
| 13 | BusinessDetailFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 14 | BusinessDetailFundingRequestFor | FUNDING_REQUEST_FOR | — | ✅ |
| 15 | BusinessDetailHighLevelDesign | HIGH_LEVEL_DESIGN | — | ✅ |
| 16 | BusinessDetailInternalRateOfReturn | INTERNAL_RATE_OF_RETURN | — | ✅ |
| 17 | BusinessDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | BusinessDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | BusinessDetailLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | BusinessDetailLaunch | LAUNCH | — | ✅ |
| 21 | BusinessDetailNetPresentValue | NET_PRESENT_VALUE | — | ✅ |
| 22 | BusinessDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | BusinessDetailPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 24 | BusinessDetailProductLine | PRODUCT_LINE | — | ✅ |
| 25 | BusinessDetailProductProposalId | PRODUCT_PROPOSAL_ID | — | ✅ |
| 26 | BusinessDetailProposalProjectedCost | PROPOSAL_PROJECTED_COST | — | ✅ |
| 27 | BusinessDetailProposalProjectedRevenue | PROPOSAL_PROJECTED_REVENUE | — | ✅ |
| 28 | BusinessDetailRequirementsDefinition | REQUIREMENTS_DEFINITION | — | ✅ |
| 29 | BusinessDetailReturnOnInvestment | RETURN_ON_INVESTMENT | — | ✅ |
| 30 | BusinessDetailSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 31 | BusinessDetailSummary | SUMMARY | — | — |
| 32 | BusinessDetailTargetCost | TARGET_COST | — | ✅ |

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
| 1 | MetricGoalBusinessObjectId | BUSINESS_OBJECT_ID | — | ✅ |
| 2 | MetricGoalBusinessObjectType | BUSINESS_OBJECT_TYPE | — | ✅ |
| 3 | MetricGoalCreatedBy | CREATED_BY | — | ✅ |
| 4 | MetricGoalCreationDate | CREATION_DATE | — | ✅ |
| 5 | MetricGoalGoalMaxValue | GOAL_MAX_VALUE | — | ✅ |
| 6 | MetricGoalGoalMinValue | GOAL_MIN_VALUE | — | ✅ |
| 7 | MetricGoalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MetricGoalLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | MetricGoalLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MetricGoalMetricConfigId | METRIC_CONFIG_ID | — | ✅ |
| 11 | MetricGoalMetricGoalId | METRIC_GOAL_ID | — | ✅ |
| 12 | MetricGoalMetricType | METRIC_TYPE | — | ✅ |
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
| 14 | PortfolioTLDescription1 | DESCRIPTION | — | — |
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
| 24 | SelProductsExpectedCommercialValue | EXPECTED_COMMERCIAL_VALUE | — | ✅ |
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
| 65 | SelProductsSelectedProductsId | SELECTED_PRODUCTS_ID | 🔑 | ✅ |
| 66 | SelProductsSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 67 | SelProductsTrcc | TRCC | — | ✅ |
| 68 | SelProductsYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 69 | SelProductsYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 70 | SelProductsYear5Revenue | YEAR_5_REVENUE | — | ✅ |

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
| 16 | LookupAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
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
