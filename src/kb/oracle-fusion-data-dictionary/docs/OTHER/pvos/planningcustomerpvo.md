---
id: DOC-OTHER-PVO-PlanningCustomerPVO
doc_type: system-doc
title: "PlanningCustomerPVO — PVO Cross-Module"
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
  - PlanningCustomerPVO
  - planningcustomerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningCustomerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Customer. Acessa as tabelas: MSC_ANALYTIC_CUST_FLAT_V_DYD.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningCustomerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 4 | 1 | 1 | 4 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_cust_flat_v_dyd|MSC_ANALYTIC_CUST_FLAT_V_DYD]] — 4 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_cust_flat_v_dyd|MSC_ANALYTIC_CUST_FLAT_V_DYD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerSiteId | CUSTOMER_SITE_ID | 🔑 | ✅ |
| 2 | CustomersPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 3 | CustomersPEOCustomerName | CUSTOMER_NAME | — | ✅ |
| 4 | CustomersPEOCustomerSiteCode | CUSTOMER_SITE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
