---
id: DOC-GL-PVO-GLFiscalYearPVO
doc_type: system-doc
title: "GLFiscalYearPVO — PVO General Ledger"
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
  - GLFiscalYearPVO
  - glfiscalyearpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GLFiscalYearPVO

## 📌 Visão Geral

View Object para extração BICC de dados de GLFiscal Year. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_YEAR_V.

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.GLFiscalYearPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 4 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 6 atributos (3 BICC)
- [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]] — 6 atributos (4 PKs, 6 BICC)

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

### [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | 🔑 | ✅ |
| 2 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 3 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |
| 4 | FiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 5 | FiscalYearNumber | FISCAL_YEAR_NUMBER | 🔑 | ✅ |
| 6 | FiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
