---
id: DOC-PO-PVO-PortfolioPlanningPeriod
doc_type: system-doc
title: "PortfolioPlanningPeriod — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PortfolioPlanningPeriod
  - portfolioplanningperiod
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PortfolioPlanningPeriod

## 📌 Visão Geral

Extrai períodos de planejamento de portfólio, com datas de início, fim e ciclos orçamentários. Permite alinhamento entre planejamento de compras e ciclos de planejamento corporativo.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.PortfolioPlanningPeriod`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 1 | 16 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]] — 12 atributos (1 PKs, 12 BICC)
- [[ace_planning_period_tl|ACE_PLANNING_PERIOD_TL]] — 5 atributos (4 BICC)

---

## ⚙️ Atributos

### [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioPlngPrdCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioPlngPrdCreationDate | CREATION_DATE | — | ✅ |
| 3 | PortfolioPlngPrdEndPlanPeriodUnitId | END_PLAN_PERIOD_UNIT_ID | — | ✅ |
| 4 | PortfolioPlngPrdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PortfolioPlngPrdLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PortfolioPlngPrdLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PortfolioPlngPrdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PortfolioPlngPrdPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 9 | PortfolioPlngPrdPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 10 | PortfolioPlngPrdPeriodStatus | PERIOD_STATUS | — | ✅ |
| 11 | PortfolioPlngPrdPlanningPeriodId | PLANNING_PERIOD_ID | 🔑 | ✅ |
| 12 | PortfolioPlngPrdStartPlanPeriodUnitId | START_PLAN_PERIOD_UNIT_ID | — | ✅ |

### [[ace_planning_period_tl|ACE_PLANNING_PERIOD_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioPlngPrdTLDescription | DESCRIPTION | — | — |
| 2 | PortfolioPlngPrdTLLanguage | LANGUAGE | — | ✅ |
| 3 | PortfolioPlngPrdTLName | NAME | — | ✅ |
| 4 | PortfolioPlngPrdTLPlanningPeriodId | PLANNING_PERIOD_ID | — | ✅ |
| 5 | PortfolioPlngPrdTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
