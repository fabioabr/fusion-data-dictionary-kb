---
id: DOC-OTHER-PVO-PlanningDemandMangementPVO
doc_type: system-doc
title: "PlanningDemandMangementPVO — PVO Cross-Module"
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
  - PlanningDemandMangementPVO
  - planningdemandmangementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningDemandMangementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Demand Mangement. Acessa as tabelas: MSC_ANALYTIC_FACT_DM_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningDemandMangementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 6 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_dm_v|MSC_ANALYTIC_FACT_DM_V]] — 23 atributos (6 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_dm_v|MSC_ANALYTIC_FACT_DM_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerSiteId | CUSTOMER_SITE_ID | 🔑 | ✅ |
| 2 | DemandClassId | DEMAND_CLASS_ID | 🔑 | ✅ |
| 3 | DemandDate | DEMAND_DATE | 🔑 | ✅ |
| 4 | DemandManagementPEOBookFcst | BOOK_FCST | — | ✅ |
| 5 | DemandManagementPEOBookHistory | BOOK_HISTORY | — | ✅ |
| 6 | DemandManagementPEOBookHistoryValue | BOOK_HISTORY_VALUE | — | ✅ |
| 7 | DemandManagementPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | DemandManagementPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | DemandManagementPEOFinalBookFcst | FINAL_BOOK_FCST | — | ✅ |
| 10 | DemandManagementPEOFinalConsFcst | FINAL_CONS_FCST | — | ✅ |
| 11 | DemandManagementPEOFinalConsHistory | FINAL_CONS_HISTORY | — | ✅ |
| 12 | DemandManagementPEOFinalShipFcst | FINAL_SHIP_FCST | — | ✅ |
| 13 | DemandManagementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | DemandManagementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | DemandManagementPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | DemandManagementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | DemandManagementPEOShipFcst | SHIP_FCST | — | ✅ |
| 18 | DemandManagementPEOShipFcstValue | SHIP_FCST_VALUE | — | ✅ |
| 19 | DemandManagementPEOShipHistory | SHIP_HISTORY | — | ✅ |
| 20 | DemandManagementPEOShipHistoryValue | SHIP_HISTORY_VALUE | — | ✅ |
| 21 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 22 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 23 | PlanId | PLAN_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
