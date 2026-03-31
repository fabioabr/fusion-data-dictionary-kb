---
id: DOC-OTHER-PVO-PlanningPeggingPVO
doc_type: system-doc
title: "PlanningPeggingPVO — PVO Cross-Module"
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
  - PlanningPeggingPVO
  - planningpeggingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningPeggingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Pegging. Acessa as tabelas: MSC_ANALYTIC_FACT_PEG_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningPeggingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 3 | 18 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_peg_v|MSC_ANALYTIC_FACT_PEG_V]] — 19 atributos (3 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_peg_v|MSC_ANALYTIC_FACT_PEG_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DemandId | DEMAND_ID | 🔑 | ✅ |
| 2 | PeggingPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 3 | PeggingPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 4 | PeggingPEODemandOrderDate | DEMAND_ORDER_DATE | — | ✅ |
| 5 | PeggingPEODemandOrderItemId | DEMAND_ORDER_ITEM_ID | — | ✅ |
| 6 | PeggingPEODemandOrderQty | DEMAND_ORDER_QTY | — | ✅ |
| 7 | PeggingPEODemandOrderType | DEMAND_ORDER_TYPE | — | ✅ |
| 8 | PeggingPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | PeggingPEOOrganization | DEMAND_ORDER_ORGANIZATION | — | ✅ |
| 10 | PeggingPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | PeggingPEOPeggedQty | PEGGED_QTY | — | ✅ |
| 12 | PeggingPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 13 | PeggingPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 14 | PeggingPEOSupplyOrderDate | SUPPLY_ORDER_DATE | — | ✅ |
| 15 | PeggingPEOSupplyOrderQty | SUPPLY_ORDER_QTY | — | ✅ |
| 16 | PeggingPEOSupplyOrderType | SUPPLY_ORDER_TYPE | — | ✅ |
| 17 | PeggingPEOUsingAssemblyDemandDate | USING_ASSEMBLY_DEMAND_DATE | — | — |
| 18 | PlanId | PLAN_ID | 🔑 | ✅ |
| 19 | TransactionId | TRANSACTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
