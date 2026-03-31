---
id: DOC-OTHER-PVO-PlanningResourcePVO
doc_type: system-doc
title: "PlanningResourcePVO — PVO Cross-Module"
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
  - PlanningResourcePVO
  - planningresourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningResourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Resource. Acessa as tabelas: MSC_ANALYTIC_RES_FLAT_V_DYD.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningResourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 8 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_res_flat_v_dyd|MSC_ANALYTIC_RES_FLAT_V_DYD]] — 11 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_res_flat_v_dyd|MSC_ANALYTIC_RES_FLAT_V_DYD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanningResourcePEOBottleneckFlag | BOTTLENECK_FLAG | — | — |
| 2 | PlanningResourcePEOCriticalResourceFlag | CRITICAL_RESOURCE_FLAG | — | — |
| 3 | PlanningResourcePEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 4 | PlanningResourcePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 5 | PlanningResourcePEOPlanId | PLAN_ID | — | — |
| 6 | PlanningResourcePEOResourceCode | RESOURCE_CODE | — | ✅ |
| 7 | PlanningResourcePEOWorkAreaCode | WORK_AREA_CODE | — | ✅ |
| 8 | PlanningResourcePEOWorkAreaId | WORK_AREA_ID | — | ✅ |
| 9 | PlanningResourcePEOWorkCenterCode | WORK_CENTER_CODE | — | ✅ |
| 10 | PlanningResourcePEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 11 | ResourceId | RESOURCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
