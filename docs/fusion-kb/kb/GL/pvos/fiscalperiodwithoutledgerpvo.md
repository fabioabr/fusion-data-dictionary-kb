---
id: DOC-GL-PVO-FiscalPeriodWithoutLedgerPVO
doc_type: system-doc
title: "FiscalPeriodWithoutLedgerPVO — PVO General Ledger"
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
  - FiscalPeriodWithoutLedgerPVO
  - fiscalperiodwithoutledgerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalPeriodWithoutLedgerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Period Without Ledger. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_PERIOD_V, GL_FISCAL_QUARTER_V (+1).

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.FiscalPeriodWithoutLedgerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 4 | 4 | 14 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 26 atributos
- [[gl_fiscal_period_v|GL_FISCAL_PERIOD_V]] — 17 atributos (4 PKs, 10 BICC)
- [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]] — 9 atributos (2 BICC)
- [[gl_fiscal_year_v|GL_FISCAL_YEAR_V]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | — |
| 2 | CalendarAdjPeriodsNum | ADJ_PERIODS_NUM | — | — |
| 3 | CalendarCalendarId | CALENDAR_ID | — | — |
| 4 | CalendarCalendarStartDate | CALENDAR_START_DATE | — | — |
| 5 | CalendarCalendarTypeCode | CALENDAR_TYPE_CODE | — | — |
| 6 | CalendarCreatedBy | CREATED_BY | — | — |
| 7 | CalendarCreationDate | CREATION_DATE | — | — |
| 8 | CalendarDescription | DESCRIPTION | — | — |
| 9 | CalendarLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | CalendarLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | CalendarLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | CalendarLatestYearStartDate | LATEST_YEAR_START_DATE | — | — |
| 13 | CalendarLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | — |
| 14 | CalendarLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | — |
| 15 | CalendarNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | — |
| 16 | CalendarNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | — |
| 17 | CalendarObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | CalendarPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | — |
| 19 | CalendarPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | — |
| 20 | CalendarPeriodSetId | PERIOD_SET_ID | — | — |
| 21 | CalendarPeriodSetName | PERIOD_SET_NAME | — | — |
| 22 | CalendarPeriodType | PERIOD_TYPE | — | — |
| 23 | CalendarPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 24 | CalendarSecurityFlag | SECURITY_FLAG | — | — |
| 25 | CalendarUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 26 | CalendarUserPeriodSetName | USER_PERIOD_SET_NAME | — | — |

### [[gl_fiscal_period_v|GL_FISCAL_PERIOD_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalPeriodAdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | FiscalPeriodFiscalPeriodCreationDate | FISCAL_PERIOD_CREATION_DATE | — | — |
| 3 | FiscalPeriodFiscalPeriodEndDate | FISCAL_PERIOD_END_DATE | — | ✅ |
| 4 | FiscalPeriodFiscalPeriodLastUpdateDate | FISCAL_PERIOD_LAST_UPDATE_DATE | — | — |
| 5 | FiscalPeriodFiscalPeriodNumber | FISCAL_PERIOD_NUMBER | — | ✅ |
| 6 | FiscalPeriodFiscalPeriodSetCreationDate | FISCAL_PERIODSET_CREATION_DATE | — | — |
| 7 | FiscalPeriodFiscalPeriodStartDate | FISCAL_PERIOD_START_DATE | — | ✅ |
| 8 | FiscalPeriodFiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | — |
| 9 | FiscalPeriodFiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | ✅ |
| 10 | FiscalPeriodFiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | — |
| 11 | FiscalPeriodFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | — |
| 12 | FiscalPeriodFiscalYearNumber | FISCAL_YEAR_NUMBER | — | ✅ |
| 13 | FiscalPeriodFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | — |
| 14 | FiscalPeriodName | FISCAL_PERIOD_NAME | 🔑 | ✅ |
| 15 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | 🔑 | ✅ |
| 16 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 17 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |

### [[gl_fiscal_quarter_v|GL_FISCAL_QUARTER_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FiscalQuarterFiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | — |
| 2 | FiscalQuarterFiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | — | — |
| 3 | FiscalQuarterFiscalPeriodType | FISCAL_PERIOD_TYPE | — | — |
| 4 | FiscalQuarterFiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 5 | FiscalQuarterFiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | — |
| 6 | FiscalQuarterFiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 7 | FiscalQuarterFiscalYearEndDate | FISCAL_YEAR_END_DATE | — | — |
| 8 | FiscalQuarterFiscalYearNumber | FISCAL_YEAR_NUMBER | — | — |
| 9 | FiscalQuarterFiscalYearStartDate | FISCAL_YEAR_START_DATE | — | — |

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
