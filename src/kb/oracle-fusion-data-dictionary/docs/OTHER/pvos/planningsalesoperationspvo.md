---
id: DOC-OTHER-PVO-PlanningSalesOperationsPVO
doc_type: system-doc
title: "PlanningSalesOperationsPVO — PVO Cross-Module"
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
  - PlanningSalesOperationsPVO
  - planningsalesoperationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningSalesOperationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Sales Operations. Acessa as tabelas: MSC_ANALYTIC_FACT_SOP_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningSalesOperationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 6 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_sop_v|MSC_ANALYTIC_FACT_SOP_V]] — 18 atributos (6 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_sop_v|MSC_ANALYTIC_FACT_SOP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerSiteId | CUSTOMER_SITE_ID | 🔑 | ✅ |
| 2 | DemandClassId | DEMAND_CLASS_ID | 🔑 | ✅ |
| 3 | DemandDate | DEMAND_DATE | 🔑 | ✅ |
| 4 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 5 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 6 | PlanId | PLAN_ID | 🔑 | ✅ |
| 7 | SalesOperationsPEOConsensusFcst | CONSENSUS_FCST | — | ✅ |
| 8 | SalesOperationsPEOConsensusFcstValue | CONSENSUS_FCST_VALUE | — | ✅ |
| 9 | SalesOperationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | SalesOperationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | SalesOperationsPEOFinalSalesFcst | FINAL_SALES_FCST | — | ✅ |
| 12 | SalesOperationsPEOFinalSalesFcstValue | FINAL_SALES_FCST_VALUE | — | ✅ |
| 13 | SalesOperationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | SalesOperationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | SalesOperationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | SalesOperationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | SalesOperationsPEOSalesFcst | SALES_FCST | — | ✅ |
| 18 | SalesOperationsPEOSalesFcstValue | SALES_FCST_VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
