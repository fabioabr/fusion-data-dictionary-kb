---
id: DOC-OTHER-PVO-PlanningDatePVO
doc_type: system-doc
title: "PlanningDatePVO — PVO Cross-Module"
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
  - PlanningDatePVO
  - planningdatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningDatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Date. Acessa as tabelas: MSC_ANALYTIC_CALENDARS_V.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.PlanningDatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 2 | 11 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[msc_analytic_calendars_v|MSC_ANALYTIC_CALENDARS_V]] — 21 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[msc_analytic_calendars_v|MSC_ANALYTIC_CALENDARS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarCode | CALENDAR_CODE | 🔑 | ✅ |
| 2 | CalendarDate | CALENDAR_DATE | 🔑 | ✅ |
| 3 | CalendarsFlattnedEOCalendarName | CALENDAR_NAME | — | ✅ |
| 4 | CalendarsFlattnedEOCalendarType | CALENDAR_TYPE | — | ✅ |
| 5 | CalendarsFlattnedEODescription | DESCRIPTION | — | — |
| 6 | CalendarsFlattnedEOMonth | MONTH | — | — |
| 7 | CalendarsFlattnedEOMonthEndDate | MONTH_END_DATE | — | — |
| 8 | CalendarsFlattnedEOMonthStartDate | MONTH_START_DATE | — | — |
| 9 | CalendarsFlattnedEOPeriodLastDate | PERIOD_LAST_DATE | — | ✅ |
| 10 | CalendarsFlattnedEOPeriodName | PERIOD_NAME | — | ✅ |
| 11 | CalendarsFlattnedEOPeriodNextDate | PERIOD_NEXT_DATE | — | ✅ |
| 12 | CalendarsFlattnedEOPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 13 | CalendarsFlattnedEOQuarter | QUARTER | — | — |
| 14 | CalendarsFlattnedEOQuarterEndDate | QUARTER_END_DATE | — | — |
| 15 | CalendarsFlattnedEOQuarterStartDate | QUARTER_START_DATE | — | — |
| 16 | CalendarsFlattnedEOWeekEndDate | WEEK_END_DATE | — | ✅ |
| 17 | CalendarsFlattnedEOWeekNextDate | WEEK_NEXT_DATE | — | ✅ |
| 18 | CalendarsFlattnedEOWeekStartDate | WEEK_START_DATE | — | ✅ |
| 19 | CalendarsFlattnedEOYear | YEAR | — | — |
| 20 | CalendarsFlattnedEOYearEndDate | YEAR_END_DATE | — | — |
| 21 | CalendarsFlattnedEOYearStartDate | YEAR_START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
