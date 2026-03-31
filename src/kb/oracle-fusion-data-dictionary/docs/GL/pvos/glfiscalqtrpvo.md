---
id: DOC-GL-PVO-GLFiscalQtrPVO
doc_type: system-doc
title: "GLFiscalQtrPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - GLFiscalQtrPVO
  - glfiscalqtrpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GLFiscalQtrPVO

## 📌 Visão Geral

View Object para extração BICC de dados de GLFiscal Qtr. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_QUARTER_V, GL_FISCAL_YEAR_V.

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.GLFiscalQtrPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 3 | 5 | 12 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 6 atributos (3 BICC)
- [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]] — 9 atributos (5 PKs, 7 BICC)
- [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsCalendarId | CALENDAR_ID | — | ✅ |
| 2 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | GlCalendarsPeriodSetId | PERIOD_SET_ID | — | — |
| 4 | GlCalendarsPeriodSetName1 | PERIOD_SET_NAME | — | ✅ |
| 5 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 6 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

### [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | 🔑 | ✅ |
| 2 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 3 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |
| 4 | FiscalQuarterFiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 5 | FiscalQuarterFiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 6 | FiscalQuarterFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | — |
| 7 | FiscalQuarterFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | — |
| 8 | FiscalQuarterNumber | FISCAL_QUARTER_NUMBER | 🔑 | ✅ |
| 9 | FiscalYearNumber | FISCAL_YEAR_NUMBER | 🔑 | ✅ |

### [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalYearFiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | — |
| 2 | FiscalYearFiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | — | — |
| 3 | FiscalYearFiscalPeriodType | FISCAL_PERIOD_TYPE | — | — |
| 4 | FiscalYearFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 5 | FiscalYearFiscalYearNumber | FISCAL_YEAR_NUMBER | — | — |
| 6 | FiscalYearFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
