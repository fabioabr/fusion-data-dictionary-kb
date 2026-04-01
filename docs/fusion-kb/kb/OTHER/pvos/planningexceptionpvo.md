---
id: DOC-OTHER-PVO-PlanningExceptionPVO
doc_type: system-doc
title: "PlanningExceptionPVO — PVO Cross-Module"
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
  - PlanningExceptionPVO
  - planningexceptionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningExceptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Exception. Acessa as tabelas: MSC_ANALYTIC_FACT_EXP, MSC_EXCEPTION_VL.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningExceptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 7 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_fact_exp|MSC_ANALYTIC_FACT_EXP]] — 19 atributos (7 PKs, 19 BICC)
- [[msc_exception_vl|MSC_EXCEPTION_VL]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_fact_exp|MSC_ANALYTIC_FACT_EXP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerSiteId | CUSTOMER_SITE_ID | 🔑 | ✅ |
| 2 | ExceptionDate | EXCEPTION_DATE | 🔑 | ✅ |
| 3 | ExceptionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ExceptionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ExceptionsPEOExceptionCount | EXCEPTION_COUNT | — | ✅ |
| 6 | ExceptionsPEOExceptionDays | EXCEPTION_DAYS | — | ✅ |
| 7 | ExceptionsPEOExceptionQuantity | EXCEPTION_QUANTITY | — | ✅ |
| 8 | ExceptionsPEOExceptionRatio | EXCEPTION_RATIO | — | ✅ |
| 9 | ExceptionsPEOExceptionType | EXCEPTION_TYPE | — | ✅ |
| 10 | ExceptionsPEOExceptionValue | EXCEPTION_VALUE | — | ✅ |
| 11 | ExceptionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ExceptionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ExceptionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ExceptionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 16 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 17 | PlanId | PLAN_ID | 🔑 | ✅ |
| 18 | ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 19 | SupplierSiteId | SUPPLIER_SITE_ID | 🔑 | ✅ |

### [[msc_exception_vl|MSC_EXCEPTION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MscExceptionNamePEOExceptionId | EXCEPTION_ID | — | ✅ |
| 2 | MscExceptionNamePEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
