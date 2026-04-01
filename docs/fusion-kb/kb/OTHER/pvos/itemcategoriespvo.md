---
id: DOC-OTHER-PVO-ItemCategoriesPVO
doc_type: system-doc
title: "ItemCategoriesPVO — PVO Cross-Module"
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
  - ItemCategoriesPVO
  - itemcategoriespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemCategoriesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Categories. Acessa as tabelas: MSC_ANALYTIC_ITEMS.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.ItemCategoriesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 1 | 3 | 70 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_items|MSC_ANALYTIC_ITEMS]] — 70 atributos (3 PKs, 70 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_items|MSC_ANALYTIC_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 2 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 3 | ItemCategoriesPEOAbcClassName | ABC_CLASS_NAME | — | ✅ |
| 4 | ItemCategoriesPEOAtoForecastControl | ATO_FORECAST_CONTROL | — | ✅ |
| 5 | ItemCategoriesPEOBaseModel | BASE_MODEL | — | ✅ |
| 6 | ItemCategoriesPEOBomItemType | BOM_ITEM_TYPE | — | ✅ |
| 7 | ItemCategoriesPEOBuyerName | BUYER_NAME | — | ✅ |
| 8 | ItemCategoriesPEOCarryingCost | CARRYING_COST | — | ✅ |
| 9 | ItemCategoriesPEOCategorySetName | CATEGORY_SET_NAME | — | ✅ |
| 10 | ItemCategoriesPEOCriticalComponentFlag | CRITICAL_COMPONENT_FLAG | — | ✅ |
| 11 | ItemCategoriesPEOCumManufacturingLeadTime | CUM_MANUFACTURING_LEAD_TIME | — | ✅ |
| 12 | ItemCategoriesPEODemandTimeFenceCode | DEMAND_TIME_FENCE_CODE | — | ✅ |
| 13 | ItemCategoriesPEODemandTimeFenceDate | DEMAND_TIME_FENCE_DATE | — | ✅ |
| 14 | ItemCategoriesPEODemandTimeFenceDays | DEMAND_TIME_FENCE_DAYS | — | ✅ |
| 15 | ItemCategoriesPEODescription | DESCRIPTION | — | ✅ |
| 16 | ItemCategoriesPEOFixedDaysSupply | FIXED_DAYS_SUPPLY | — | ✅ |
| 17 | ItemCategoriesPEOFixedLeadTime | FIXED_LEAD_TIME | — | ✅ |
| 18 | ItemCategoriesPEOFixedLotMultiplier | FIXED_LOT_MULTIPLIER | — | ✅ |
| 19 | ItemCategoriesPEOFixedOrderQuantity | FIXED_ORDER_QUANTITY | — | ✅ |
| 20 | ItemCategoriesPEOForecastName | FORECAST_NAME | — | ✅ |
| 21 | ItemCategoriesPEOFullLeadTime | FULL_LEAD_TIME | — | ✅ |
| 22 | ItemCategoriesPEOHierarchyId | HIERARCHY_ID | — | ✅ |
| 23 | ItemCategoriesPEOItemCostOverride | ITEM_COST_OVERRIDE | — | ✅ |
| 24 | ItemCategoriesPEOItemCostUom | ITEM_COST_UOM | — | ✅ |
| 25 | ItemCategoriesPEOItemName | ITEM_NAME | — | ✅ |
| 26 | ItemCategoriesPEOLifeCyclePhase | LIFE_CYCLE_PHASE | — | ✅ |
| 27 | ItemCategoriesPEOListPrice | LIST_PRICE | — | ✅ |
| 28 | ItemCategoriesPEOMaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 29 | ItemCategoriesPEOMember1 | MEMBER1 | — | ✅ |
| 30 | ItemCategoriesPEOMember10 | MEMBER10 | — | ✅ |
| 31 | ItemCategoriesPEOMember2 | MEMBER2 | — | ✅ |
| 32 | ItemCategoriesPEOMember3 | MEMBER3 | — | ✅ |
| 33 | ItemCategoriesPEOMember4 | MEMBER4 | — | ✅ |
| 34 | ItemCategoriesPEOMember5 | MEMBER5 | — | ✅ |
| 35 | ItemCategoriesPEOMember6 | MEMBER6 | — | ✅ |
| 36 | ItemCategoriesPEOMember7 | MEMBER7 | — | ✅ |
| 37 | ItemCategoriesPEOMember8 | MEMBER8 | — | ✅ |
| 38 | ItemCategoriesPEOMember9 | MEMBER9 | — | ✅ |
| 39 | ItemCategoriesPEOMinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 40 | ItemCategoriesPEOMrpPlanningCode | MRP_PLANNING_CODE | — | ✅ |
| 41 | ItemCategoriesPEOName1 | NAME1 | — | ✅ |
| 42 | ItemCategoriesPEOName10 | NAME10 | — | ✅ |
| 43 | ItemCategoriesPEOName2 | NAME2 | — | ✅ |
| 44 | ItemCategoriesPEOName3 | NAME3 | — | ✅ |
| 45 | ItemCategoriesPEOName4 | NAME4 | — | ✅ |
| 46 | ItemCategoriesPEOName5 | NAME5 | — | ✅ |
| 47 | ItemCategoriesPEOName6 | NAME6 | — | ✅ |
| 48 | ItemCategoriesPEOName7 | NAME7 | — | ✅ |
| 49 | ItemCategoriesPEOName8 | NAME8 | — | ✅ |
| 50 | ItemCategoriesPEOName9 | NAME9 | — | ✅ |
| 51 | ItemCategoriesPEONetSellingPrice | NET_SELLING_PRICE | — | ✅ |
| 52 | ItemCategoriesPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 53 | ItemCategoriesPEOPlanId | PLAN_ID | — | ✅ |
| 54 | ItemCategoriesPEOPlannerCode | PLANNER_CODE | — | ✅ |
| 55 | ItemCategoriesPEOPlanningMakeBuyCode | PLANNING_MAKE_BUY_CODE | — | ✅ |
| 56 | ItemCategoriesPEOPlanningTimeFenceCode | PLANNING_TIME_FENCE_CODE | — | ✅ |
| 57 | ItemCategoriesPEOPlanningTimeFenceDate | PLANNING_TIME_FENCE_DATE | — | ✅ |
| 58 | ItemCategoriesPEOPlanningTimeFenceDays | PLANNING_TIME_FENCE_DAYS | — | ✅ |
| 59 | ItemCategoriesPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 60 | ItemCategoriesPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 61 | ItemCategoriesPEOReleaseTimeFenceCode | RELEASE_TIME_FENCE_CODE | — | ✅ |
| 62 | ItemCategoriesPEOReleaseTimeFenceDays | RELEASE_TIME_FENCE_DAYS | — | ✅ |
| 63 | ItemCategoriesPEOSafetyStockCode | SAFETY_STOCK_CODE | — | ✅ |
| 64 | ItemCategoriesPEOSafetyStockPercent | SAFETY_STOCK_PERCENT | — | ✅ |
| 65 | ItemCategoriesPEOSafetyStockQuantity | SAFETY_STOCK_QUANTITY | — | ✅ |
| 66 | ItemCategoriesPEOSafetyStockQuantityOverride | SAFETY_STOCK_QUANTITY_OVERRIDE | — | ✅ |
| 67 | ItemCategoriesPEOUomCode | UOM_CODE | — | ✅ |
| 68 | ItemCategoriesPEOUseUpDate | USE_UP_DATE | — | ✅ |
| 69 | ItemCategoriesPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | ✅ |
| 70 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
