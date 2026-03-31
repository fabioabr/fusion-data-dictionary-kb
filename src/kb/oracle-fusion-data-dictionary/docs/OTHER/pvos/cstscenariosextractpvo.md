---
id: DOC-OTHER-PVO-CstScenariosExtractPVO
doc_type: system-doc
title: "CstScenariosExtractPVO — PVO Cross-Module"
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
  - CstScenariosExtractPVO
  - cstscenariosextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstScenariosExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Scenarios Extract. Acessa as tabelas: CST_SCENARIOS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstScenariosExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_scenarios|CST_SCENARIOS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[cst_scenarios|CST_SCENARIOS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstScenariosPEOAssignmentSetId | ASSIGNMENT_SET_ID | — | ✅ |
| 2 | CstScenariosPEOComments | COMMENTS | — | ✅ |
| 3 | CstScenariosPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstScenariosPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | CstScenariosPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstScenariosPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstScenariosPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | CstScenariosPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | CstScenariosPEOInvOrgId | INV_ORG_ID | — | ✅ |
| 10 | CstScenariosPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CstScenariosPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CstScenariosPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CstScenariosPEOOrganizationContext | ORGANIZATION_CONTEXT | — | ✅ |
| 14 | CstScenariosPEOPlanningCostOrgId | PLANNING_COST_ORG_ID | — | ✅ |
| 15 | CstScenariosPEOPlanningMode | PLANNING_MODE | — | ✅ |
| 16 | CstScenariosPEOPreviousScenarioId | PREVIOUS_SCENARIO_ID | — | ✅ |
| 17 | CstScenariosPEOPublishToAccountingFlag | PUBLISH_TO_ACCOUNTING_FLAG | — | ✅ |
| 18 | CstScenariosPEOPurposeCode | PURPOSE_CODE | — | ✅ |
| 19 | CstScenariosPEORollupGroupId | ROLLUP_GROUP_ID | — | ✅ |
| 20 | CstScenariosPEOScenarioHeaderId | SCENARIO_HEADER_ID | — | ✅ |
| 21 | CstScenariosPEOScenarioId | SCENARIO_ID | 🔑 | ✅ |
| 22 | CstScenariosPEOScenarioNumber | SCENARIO_NUMBER | — | ✅ |
| 23 | CstScenariosPEOScenarioType | SCENARIO_TYPE | — | ✅ |
| 24 | CstScenariosPEOStateCode | STATE_CODE | — | ✅ |
| 25 | CstScenariosPEOStatusCode | STATUS_CODE | — | ✅ |
| 26 | CstScenariosPEOSupplyChainRollupFlag | SUPPLY_CHAIN_ROLLUP_FLAG | — | ✅ |
| 27 | CstScenariosPEOTransferCostRuleSetId | TRANSFER_COST_RULE_SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
