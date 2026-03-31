---
id: DOC-OTHER-PVO-RcsCrmFiscalDay
doc_type: system-doc
title: "RcsCrmFiscalDay — PVO Cross-Module"
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
  - RcsCrmFiscalDay
  - rcscrmfiscalday
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RcsCrmFiscalDay

## 📌 Visão Geral

View Object para extração BICC de dados de Rcs Crm Fiscal Day. Acessa as tabelas: ZCA_BI_CRM_CALENDAR.

**Caminho:** `FscmTopModelAM.RcsCommonPublicViewAM.RcsCrmFiscalDay`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 2 | 33 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[zca_bi_crm_calendar|ZCA_BI_CRM_CALENDAR]] — 38 atributos (2 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[zca_bi_crm_calendar|ZCA_BI_CRM_CALENDAR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalMonth | CAL_MONTH | — | ✅ |
| 2 | CalMonthCode | CAL_MONTH_CODE | — | ✅ |
| 3 | CalMonthEndDate | CAL_MONTH_END_DATE | — | ✅ |
| 4 | CalMonthStartDate | CAL_MONTH_START_DATE | — | ✅ |
| 5 | CalQtrEndDate | CAL_QTR_END_DATE | — | ✅ |
| 6 | CalQtrStartDate | CAL_QTR_START_DATE | — | ✅ |
| 7 | CalQuarter | CAL_QUARTER | — | ✅ |
| 8 | CalQuarterCode | CAL_QUARTER_CODE | — | ✅ |
| 9 | CalWeek | CAL_WEEK | — | ✅ |
| 10 | CalWeekCode | CAL_WEEK_CODE | — | ✅ |
| 11 | CalWeekEndDate | CAL_WEEK_END_DATE | — | ✅ |
| 12 | CalWeekStartDate | CAL_WEEK_START_DATE | — | ✅ |
| 13 | CalYear | CAL_YEAR | — | ✅ |
| 14 | CalYearEndDate | CAL_YEAR_END_DATE | — | ✅ |
| 15 | CalYearStartDate | CAL_YEAR_START_DATE | — | ✅ |
| 16 | CalendarId | CALENDAR_ID | — | — |
| 17 | CalendarWeek | CALENDAR_WEEK | — | ✅ |
| 18 | DayOfMonth | DAY_OF_MONTH | — | ✅ |
| 19 | DayOfWeek | DAY_OF_WEEK | — | ✅ |
| 20 | DayOfYear | DAY_OF_YEAR | — | ✅ |
| 21 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 22 | EnterpriseQuarter | ENTERPRISE_QUARTER | — | ✅ |
| 23 | EnterpriseYear | ENTERPRISE_YEAR | — | ✅ |
| 24 | FiscalPeriodAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | — |
| 25 | FiscalPeriodEndDate | FISCAL_PERIOD_END_DATE | — | ✅ |
| 26 | FiscalPeriodName | FISCAL_PERIOD_NAME | — | ✅ |
| 27 | FiscalPeriodNumber | FISCAL_PERIOD_NUMBER | — | ✅ |
| 28 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | — |
| 29 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | — | — |
| 30 | FiscalPeriodStartDate | FISCAL_PERIOD_START_DATE | — | ✅ |
| 31 | FiscalPeriodType | FISCAL_PERIOD_TYPE | — | — |
| 32 | FiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 33 | FiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | ✅ |
| 34 | FiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 35 | FiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 36 | FiscalYearNumber | FISCAL_YEAR_NUMBER | — | ✅ |
| 37 | FiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |
| 38 | ReportDate | REPORT_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
