---
id: DOC-OTHER-PVO-RMCSFiscalDayPVO
doc_type: system-doc
title: "RMCSFiscalDayPVO — PVO Cross-Module"
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
  - RMCSFiscalDayPVO
  - rmcsfiscaldaypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RMCSFiscalDayPVO

## 📌 Visão Geral

View Object para extração BICC de dados de RMCSFiscal Day. Acessa as tabelas: GL_CALENDARS, GL_FISCAL_DAY_V.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RMCSFiscalDayPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 2 | 5 | 22 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 33 atributos (4 BICC)
- [[gl_fiscal_day_v|GL_FISCAL_DAY_V]] — 29 atributos (5 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarPEOAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | — |
| 2 | CalendarPEOAdjPeriodsNum | ADJ_PERIODS_NUM | — | — |
| 3 | CalendarPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | CalendarPEOAttribute2 | ATTRIBUTE2 | — | — |
| 5 | CalendarPEOAttribute3 | ATTRIBUTE3 | — | — |
| 6 | CalendarPEOAttribute4 | ATTRIBUTE4 | — | — |
| 7 | CalendarPEOAttribute5 | ATTRIBUTE5 | — | — |
| 8 | CalendarPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | CalendarPEOCalendarId | CALENDAR_ID | — | ✅ |
| 10 | CalendarPEOCalendarStartDate | CALENDAR_START_DATE | — | — |
| 11 | CalendarPEOCalendarTypeCode | CALENDAR_TYPE_CODE | — | — |
| 12 | CalendarPEOCreatedBy | CREATED_BY | — | — |
| 13 | CalendarPEOCreationDate | CREATION_DATE | — | — |
| 14 | CalendarPEODescription | DESCRIPTION | — | — |
| 15 | CalendarPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 16 | CalendarPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CalendarPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | CalendarPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | CalendarPEOLatestYearStartDate | LATEST_YEAR_START_DATE | — | — |
| 20 | CalendarPEOLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | — |
| 21 | CalendarPEOLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | — |
| 22 | CalendarPEONonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | — |
| 23 | CalendarPEONonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | — |
| 24 | CalendarPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | CalendarPEOPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | — |
| 26 | CalendarPEOPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | — |
| 27 | CalendarPEOPeriodSetId | PERIOD_SET_ID | — | — |
| 28 | CalendarPEOPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 29 | CalendarPEOPeriodType | PERIOD_TYPE | — | — |
| 30 | CalendarPEOPeriodTypeId | PERIOD_TYPE_ID | — | — |
| 31 | CalendarPEOSecurityFlag | SECURITY_FLAG | — | — |
| 32 | CalendarPEOUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | — |
| 33 | CalendarPEOUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

### [[gl_fiscal_day_v|GL_FISCAL_DAY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DayOfMonth | DAY_OF_MONTH | — | — |
| 5 | DayOfWeek | DAY_OF_WEEK | — | ✅ |
| 6 | DayOfYear | DAY_OF_YEAR | — | — |
| 7 | EnterpriseId | ENTERPRISE_ID | — | — |
| 8 | FiscalPeriodCreationDate | FISCAL_PERIOD_CREATION_DATE | — | — |
| 9 | FiscalPeriodEndDate | FISCAL_PERIOD_END_DATE | — | ✅ |
| 10 | FiscalPeriodLastUpdateDate | FISCAL_PERIOD_LAST_UPDATE_DATE | — | ✅ |
| 11 | FiscalPeriodName | FISCAL_PERIOD_NAME | — | ✅ |
| 12 | FiscalPeriodNumber | FISCAL_PERIOD_NUMBER | 🔑 | ✅ |
| 13 | FiscalPeriodSetId | FISCAL_PERIOD_SET_ID | — | ✅ |
| 14 | FiscalPeriodSetName | FISCAL_PERIOD_SET_NAME | 🔑 | ✅ |
| 15 | FiscalPeriodStartDate | FISCAL_PERIOD_START_DATE | — | ✅ |
| 16 | FiscalPeriodType | FISCAL_PERIOD_TYPE | 🔑 | ✅ |
| 17 | FiscalPeriodsetCreationDate | FISCAL_PERIODSET_CREATION_DATE | — | — |
| 18 | FiscalQuarterEndDate | FISCAL_QUARTER_END_DATE | — | ✅ |
| 19 | FiscalQuarterNumber | FISCAL_QUARTER_NUMBER | — | ✅ |
| 20 | FiscalQuarterStartDate | FISCAL_QUARTER_START_DATE | — | ✅ |
| 21 | FiscalYearEndDate | FISCAL_YEAR_END_DATE | — | ✅ |
| 22 | FiscalYearNumber | FISCAL_YEAR_NUMBER | 🔑 | ✅ |
| 23 | FiscalYearStartDate | FISCAL_YEAR_START_DATE | — | ✅ |
| 24 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | ParentMonth | PARENT_MONTH | — | — |
| 28 | ParentWeek | PARENT_WEEK | — | — |
| 29 | ReportDate | REPORT_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
