---
id: DOC-OTHER-PVO-ResourceRateDetailsPVO
doc_type: system-doc
title: "ResourceRateDetailsPVO — PVO Cross-Module"
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
  - ResourceRateDetailsPVO
  - resourceratedetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceRateDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Rate Details. Acessa as tabelas: CST_COST_ORG_BOOKS, CST_STD_RESOURCE_RATES, CST_STD_RESOURCE_RATE_DETAILS (+1).

**Caminho:** `FscmTopModelAM.ResourceRateAM.ResourceRateDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 4 | 1 | 57 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 4 atributos (4 BICC)
- [[cst_std_resource_rates|CST_STD_RESOURCE_RATES]] — 34 atributos (32 BICC)
- [[cst_std_resource_rate_details|CST_STD_RESOURCE_RATE_DETAILS]] — 15 atributos (1 PKs, 15 BICC)
- [[gl_calendars|GL_CALENDARS]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cst_cost_org_books|CST_COST_ORG_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostOrgBookPEOCalendarId | CALENDAR_ID | — | ✅ |
| 2 | CostOrgBookPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CostOrgBookPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | CostOrgBookPEOLedgerId | LEDGER_ID | — | ✅ |

### [[cst_std_resource_rates|CST_STD_RESOURCE_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceRatesPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | ResourceRatesPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 3 | ResourceRatesPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 4 | ResourceRatesPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 5 | ResourceRatesPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | ResourceRatesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | ResourceRatesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | ResourceRatesPEOFromPeriodName | FROM_PERIOD_NAME | — | — |
| 9 | ResourceRatesPEOInvOrgId | INV_ORG_ID | — | ✅ |
| 10 | ResourceRatesPEOJobDefinitionName1 | JOB_DEFINITION_NAME | — | ✅ |
| 11 | ResourceRatesPEOJobDefinitionPackage1 | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | ResourceRatesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 13 | ResourceRatesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ResourceRatesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 15 | ResourceRatesPEOLastUsedDate | LAST_USED_DATE | — | ✅ |
| 16 | ResourceRatesPEOLastUsedTransactionId | LAST_USED_TRANSACTION_ID | — | ✅ |
| 17 | ResourceRatesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ResourceRatesPEOPlanningResourceRateId | PLANNING_RESOURCE_RATE_ID | — | ✅ |
| 19 | ResourceRatesPEOPreviousEffectiveEndDate | PREVIOUS_EFFECTIVE_END_DATE | — | ✅ |
| 20 | ResourceRatesPEOPreviousEffectiveStartDate | PREVIOUS_EFFECTIVE_START_DATE | — | ✅ |
| 21 | ResourceRatesPEOPreviousStdResourceRateId | PREVIOUS_STD_RESOURCE_RATE_ID | — | ✅ |
| 22 | ResourceRatesPEORequestId1 | REQUEST_ID | — | ✅ |
| 23 | ResourceRatesPEOResourceId | RESOURCE_ID | — | ✅ |
| 24 | ResourceRatesPEOScenarioEventId | SCENARIO_EVENT_ID | — | ✅ |
| 25 | ResourceRatesPEOScenarioId | SCENARIO_ID | — | ✅ |
| 26 | ResourceRatesPEOScenarioPublishHeaderId | SCENARIO_PUBLISH_HEADER_ID | — | ✅ |
| 27 | ResourceRatesPEOScenarioRollupHeaderId | SCENARIO_ROLLUP_HEADER_ID | — | ✅ |
| 28 | ResourceRatesPEOSourceDi | SOURCE_DI | — | ✅ |
| 29 | ResourceRatesPEOStagedForStdCostAdjFlag | STAGED_FOR_STD_COST_ADJ_FLAG | — | ✅ |
| 30 | ResourceRatesPEOStatusCode | STATUS_CODE | — | ✅ |
| 31 | ResourceRatesPEOStdResourceRateId1 | STD_RESOURCE_RATE_ID | — | ✅ |
| 32 | ResourceRatesPEOToPeriodName | TO_PERIOD_NAME | — | — |
| 33 | ResourceRatesPEOTotalRate | TOTAL_RATE | — | ✅ |
| 34 | ResourceRatesPEOUomCode | UOM_CODE | — | ✅ |

### [[cst_std_resource_rate_details|CST_STD_RESOURCE_RATE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceRateDetailsPEOCostComponentId | COST_COMPONENT_ID | — | ✅ |
| 2 | ResourceRateDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 3 | ResourceRateDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ResourceRateDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ResourceRateDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 6 | ResourceRateDetailsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | ResourceRateDetailsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | ResourceRateDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ResourceRateDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ResourceRateDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ResourceRateDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ResourceRateDetailsPEORequestId | REQUEST_ID | — | ✅ |
| 13 | ResourceRateDetailsPEOStdResourceRateId | STD_RESOURCE_RATE_ID | — | ✅ |
| 14 | ResourceRateDetailsPEOUnitRate | UNIT_RATE | — | ✅ |
| 15 | StdResourceRateDetailId | STD_RESOURCE_RATE_DETAIL_ID | 🔑 | ✅ |

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsPEOCalendarId1 | CALENDAR_ID | — | ✅ |
| 2 | GlCalendarsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | GlCalendarsPEOPeriodSetId | PERIOD_SET_ID | — | ✅ |
| 4 | GlCalendarsPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 5 | GlCalendarsPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 6 | GlCalendarsPEOPeriodTypeId | PERIOD_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
