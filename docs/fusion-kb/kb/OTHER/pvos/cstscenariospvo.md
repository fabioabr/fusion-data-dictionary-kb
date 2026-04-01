---
id: DOC-OTHER-PVO-CstScenariosPVO
doc_type: system-doc
title: "CstScenariosPVO — PVO Cross-Module"
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
  - CstScenariosPVO
  - cstscenariospvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstScenariosPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Scenarios. Acessa as tabelas: CST_SCENARIOS.

**Caminho:** `FscmTopModelAM.ScenariosAM.CstScenariosPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 1 | 11 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[cst_scenarios|CST_SCENARIOS]] — 35 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cst_scenarios|CST_SCENARIOS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstScenariosPEOAssignmentSetId | ASSIGNMENT_SET_ID | — | — |
| 2 | CstScenariosPEOComments | COMMENTS | — | ✅ |
| 3 | CstScenariosPEOConfiguredEnabled | CONFIGURED_ENABLED | — | — |
| 4 | CstScenariosPEOConfiguredFromDate | CONFIGURED_FROM_DATE | — | — |
| 5 | CstScenariosPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstScenariosPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstScenariosPEOCreatedBy | CREATED_BY | — | — |
| 8 | CstScenariosPEOCreationDate | CREATION_DATE | — | — |
| 9 | CstScenariosPEOCurrencyCode | CURRENCY_CODE | — | — |
| 10 | CstScenariosPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | — |
| 11 | CstScenariosPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | CstScenariosPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | CstScenariosPEOInvOrgId | INV_ORG_ID | — | — |
| 14 | CstScenariosPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 15 | CstScenariosPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 16 | CstScenariosPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CstScenariosPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | CstScenariosPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | CstScenariosPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | CstScenariosPEOPlanningCostOrgId | PLANNING_COST_ORG_ID | — | — |
| 21 | CstScenariosPEOPlanningMode | PLANNING_MODE | — | ✅ |
| 22 | CstScenariosPEOPreviousScenarioId | PREVIOUS_SCENARIO_ID | — | — |
| 23 | CstScenariosPEOPublishToAccountingFlag | PUBLISH_TO_ACCOUNTING_FLAG | — | — |
| 24 | CstScenariosPEOPurposeCode | PURPOSE_CODE | — | — |
| 25 | CstScenariosPEORequestId | REQUEST_ID | — | — |
| 26 | CstScenariosPEOScenarioHeaderId | SCENARIO_HEADER_ID | — | — |
| 27 | CstScenariosPEOScenarioNumber | SCENARIO_NUMBER | — | ✅ |
| 28 | CstScenariosPEOScenarioType | SCENARIO_TYPE | — | ✅ |
| 29 | CstScenariosPEOScenarioVersionNumber | SCENARIO_VERSION_NUMBER | — | — |
| 30 | CstScenariosPEOScenarioVersionType | SCENARIO_VERSION_TYPE | — | — |
| 31 | CstScenariosPEOStateCode | STATE_CODE | — | ✅ |
| 32 | CstScenariosPEOStatusCode | STATUS_CODE | — | ✅ |
| 33 | CstScenariosPEOSupplyChainRollupFlag | SUPPLY_CHAIN_ROLLUP_FLAG | — | — |
| 34 | CstScenariosPEOTransferCostRuleSetId | TRANSFER_COST_RULE_SET_ID | — | — |
| 35 | ScenarioId | SCENARIO_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
