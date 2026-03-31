---
id: DOC-PO-PVO-Scenario
doc_type: system-doc
title: "Scenario — PVO Purchasing"
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
  - Scenario
  - scenario
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Scenario

## 📌 Visão Geral

Extrai cenários de planejamento de portfólio, com premissas, metas e projeções por período. Permite análise de sensibilidade e planejamento baseado em múltiplos cenários de investimento e procurement.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.Scenario`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 181 | 8 | 1 | 175 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[ace_metric_config_b|ACE_METRIC_CONFIG_B]] — 16 atributos (16 BICC)
- [[ace_metric_goal|ACE_METRIC_GOAL]] — 13 atributos (13 BICC)
- [[ace_pf_scenario_b|ACE_PF_SCENARIO_B]] — 68 atributos (1 PKs, 65 BICC)
- [[ace_pf_scenario_tl|ACE_PF_SCENARIO_TL]] — 11 atributos (10 BICC)
- [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]] — 12 atributos (12 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (30 BICC)
- [[ace_portfolio_revision|ACE_PORTFOLIO_REVISION]] — 9 atributos (9 BICC)
- [[ace_portfolio_tl|ACE_PORTFOLIO_TL]] — 22 atributos (20 BICC)

---

## ⚙️ Atributos

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
| 23 | ScenarioDiscountRate | SCENARIO_DISCOUNT_RATE | — | — |
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
| 47 | ScenarioProjProdFixedCost | PROJ_PROD_FIXED_COST | — | ✅ |
| 48 | ScenarioProjProdLaborCost | PROJ_PROD_LABOR_COST | — | ✅ |
| 49 | ScenarioProjProdMaterialCost | PROJ_PROD_MATERIAL_COST | — | ✅ |
| 50 | ScenarioProjProdVariableCost | PROJ_PROD_VARIABLE_COST | — | ✅ |
| 51 | ScenarioProjectedCost | PROJECTED_COST | — | ✅ |
| 52 | ScenarioProjectedMargin | PROJECTED_MARGIN | — | ✅ |
| 53 | ScenarioProjectedResources | PROJECTED_RESOURCES | — | ✅ |
| 54 | ScenarioProjectedRevenue | PROJECTED_REVENUE | — | ✅ |
| 55 | ScenarioResourceValueIndex | RESOURCE_VALUE_INDEX | — | ✅ |
| 56 | ScenarioRevenueDeviation | REVENUE_DEVIATION | — | ✅ |
| 57 | ScenarioRndKnowHow | RND_KNOW_HOW | — | ✅ |
| 58 | ScenarioRoi | ROI | — | ✅ |
| 59 | ScenarioRpi | RPI | — | ✅ |
| 60 | ScenarioScenarioBaselineDate | SCENARIO_BASELINE_DATE | — | — |
| 61 | ScenarioScenarioId | SCENARIO_ID | 🔑 | ✅ |
| 62 | ScenarioStatus | STATUS | — | ✅ |
| 63 | ScenarioSupplyChainFit | SUPPLY_CHAIN_FIT | — | ✅ |
| 64 | ScenarioTrcc | TRCC | — | ✅ |
| 65 | ScenarioWorstAllocResourcePool | WORST_ALLOC_RESOURCE_POOL | — | — |
| 66 | ScenarioYear2Revenue | YEAR_2_REVENUE | — | ✅ |
| 67 | ScenarioYear3Revenue | YEAR_3_REVENUE | — | ✅ |
| 68 | ScenarioYear5Revenue | YEAR_5_REVENUE | — | ✅ |

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

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
