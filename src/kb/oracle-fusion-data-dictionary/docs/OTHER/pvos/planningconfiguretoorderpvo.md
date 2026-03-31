---
id: DOC-OTHER-PVO-PlanningConfigureToOrderPVO
doc_type: system-doc
title: "PlanningConfigureToOrderPVO — PVO Cross-Module"
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
  - PlanningConfigureToOrderPVO
  - planningconfiguretoorderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningConfigureToOrderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Configure To Order. Acessa as tabelas: MSC_ANALYTIC_FACT_CTO_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningConfigureToOrderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 8 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_cto_v|MSC_ANALYTIC_FACT_CTO_V]] — 17 atributos (8 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_cto_v|MSC_ANALYTIC_FACT_CTO_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConfigureToOrderPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ConfigureToOrderPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ConfigureToOrderPEOFinalOptionDemandFcst | FINAL_OPTION_DEMAND_FCST | — | ✅ |
| 4 | ConfigureToOrderPEOFinalPlanningPercent | FINAL_PLANNING_PERCENT | — | ✅ |
| 5 | ConfigureToOrderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ConfigureToOrderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ConfigureToOrderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ConfigureToOrderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ConfigureToOrderPEOOptionDemandFcst | OPTION_DEMAND_FCST | — | ✅ |
| 10 | CtoLvlMemberId | CTO_LVL_MEMBER_ID | 🔑 | ✅ |
| 11 | CustomerSiteId | CUSTOMER_SITE_ID | 🔑 | ✅ |
| 12 | DemandClassId | DEMAND_CLASS_ID | 🔑 | ✅ |
| 13 | DemandDate | DEMAND_DATE | 🔑 | ✅ |
| 14 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 15 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 16 | PlanId | PLAN_ID | 🔑 | ✅ |
| 17 | TopModelItemId | TOP_MODEL_ITEM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
