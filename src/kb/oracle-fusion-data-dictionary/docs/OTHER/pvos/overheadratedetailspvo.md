---
id: DOC-OTHER-PVO-OverheadRateDetailsPVO
doc_type: system-doc
title: "OverheadRateDetailsPVO — PVO Cross-Module"
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
  - OverheadRateDetailsPVO
  - overheadratedetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OverheadRateDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Overhead Rate Details. Acessa as tabelas: CST_COST_ORG_BOOKS, CST_STD_OVERHEAD_RATES, CST_STD_OVERHEAD_RATE_DETAILS (+1).

**Caminho:** `FscmTopModelAM.ResourceRateAM.OverheadRateDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 4 | 2 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_cost_org_books|CST_COST_ORG_BOOKS]] — 4 atributos (4 BICC)
- [[cst_std_overhead_rates|CST_STD_OVERHEAD_RATES]] — 27 atributos (1 PKs, 27 BICC)
- [[cst_std_overhead_rate_details|CST_STD_OVERHEAD_RATE_DETAILS]] — 11 atributos (1 PKs, 11 BICC)
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

### [[cst_std_overhead_rates|CST_STD_OVERHEAD_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OverheadRatesPEOBasisType | BASIS_TYPE | — | ✅ |
| 2 | OverheadRatesPEOCategoryId | CATEGORY_ID | — | ✅ |
| 3 | OverheadRatesPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 4 | OverheadRatesPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | OverheadRatesPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 6 | OverheadRatesPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | OverheadRatesPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | OverheadRatesPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | OverheadRatesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 10 | OverheadRatesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | OverheadRatesPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | OverheadRatesPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 13 | OverheadRatesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 14 | OverheadRatesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 15 | OverheadRatesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | OverheadRatesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | OverheadRatesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | OverheadRatesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | OverheadRatesPEOOverheadRateType | OVERHEAD_RATE_TYPE | — | ✅ |
| 20 | OverheadRatesPEORequestId | REQUEST_ID | — | ✅ |
| 21 | OverheadRatesPEOResourceType | RESOURCE_TYPE | — | ✅ |
| 22 | OverheadRatesPEOScenarioId | SCENARIO_ID | — | ✅ |
| 23 | OverheadRatesPEOSourceDi | SOURCE_DI | — | ✅ |
| 24 | OverheadRatesPEOStatusCode | STATUS_CODE | — | ✅ |
| 25 | OverheadRatesPEOStdOverheadRateId | STD_OVERHEAD_RATE_ID | 🔑 | ✅ |
| 26 | OverheadRatesPEOTotalRate | TOTAL_RATE | — | ✅ |
| 27 | OverheadRatesPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

### [[cst_std_overhead_rate_details|CST_STD_OVERHEAD_RATE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OverheadRateDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 2 | OverheadRateDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | OverheadRateDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | OverheadRateDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 5 | OverheadRateDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | OverheadRateDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | OverheadRateDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | OverheadRateDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | OverheadRateDetailsPEOStdOverheadRateId | STD_OVERHEAD_RATE_ID | — | ✅ |
| 10 | OverheadRateDetailsPEOUnitRate | UNIT_RATE | — | ✅ |
| 11 | StdOverheadRateDetailId | STD_OVERHEAD_RATE_DETAIL_ID | 🔑 | ✅ |

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
