---
id: DOC-OTHER-PVO-PeriodStatusExtractPVO
doc_type: system-doc
title: "PeriodStatusExtractPVO — PVO Cross-Module"
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
  - PeriodStatusExtractPVO
  - periodstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Period Status Extract. Acessa as tabelas: XCC_CB_PERIOD_STATUSES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.PeriodStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_cb_period_statuses|XCC_CB_PERIOD_STATUSES]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[xcc_cb_period_statuses|XCC_CB_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetEffectivePeriodNum | BUDGET_EFFECTIVE_PERIOD_NUM | — | ✅ |
| 2 | BudgetPeriodNum | BUDGET_PERIOD_NUM | — | ✅ |
| 3 | ControlBudgetId | CONTROL_BUDGET_ID | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EffectivePeriodNum | EFFECTIVE_PERIOD_NUM | — | ✅ |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | FiscalYear | FISCAL_YEAR | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | PeriodName | PERIOD_NAME | — | ✅ |
| 14 | PeriodNum | PERIOD_NUM | — | ✅ |
| 15 | PeriodStatusId | PERIOD_STATUS_ID | 🔑 | ✅ |
| 16 | PeriodYear | PERIOD_YEAR | — | ✅ |
| 17 | QuarterNum | QUARTER_NUM | — | ✅ |
| 18 | StartDate | START_DATE | — | ✅ |
| 19 | StatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
