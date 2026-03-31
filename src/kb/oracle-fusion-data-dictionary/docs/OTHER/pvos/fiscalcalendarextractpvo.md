---
id: DOC-OTHER-PVO-FiscalCalendarExtractPVO
doc_type: system-doc
title: "FiscalCalendarExtractPVO — PVO Cross-Module"
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
  - FiscalCalendarExtractPVO
  - fiscalcalendarextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FiscalCalendarExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fiscal Calendar Extract. Acessa as tabelas: GL_CALENDARS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.FiscalCalendarExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 5 | 26 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[gl_calendars|GL_CALENDARS]] — 32 atributos (5 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[gl_calendars|GL_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlCalendarsAdjPeriodFreqCode | ADJ_PERIOD_FREQ_CODE | — | ✅ |
| 2 | GlCalendarsAdjPeriodsNum | ADJ_PERIODS_NUM | — | ✅ |
| 3 | GlCalendarsAttribute1 | ATTRIBUTE1 | — | — |
| 4 | GlCalendarsAttribute2 | ATTRIBUTE2 | — | — |
| 5 | GlCalendarsAttribute3 | ATTRIBUTE3 | — | — |
| 6 | GlCalendarsAttribute4 | ATTRIBUTE4 | — | — |
| 7 | GlCalendarsAttribute5 | ATTRIBUTE5 | — | — |
| 8 | GlCalendarsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | GlCalendarsCalendarId | CALENDAR_ID | 🔑 | ✅ |
| 10 | GlCalendarsCalendarStartDate | CALENDAR_START_DATE | — | ✅ |
| 11 | GlCalendarsCalendarTypeCode | CALENDAR_TYPE_CODE | — | ✅ |
| 12 | GlCalendarsCreatedBy | CREATED_BY | — | ✅ |
| 13 | GlCalendarsCreationDate | CREATION_DATE | — | ✅ |
| 14 | GlCalendarsDescription | DESCRIPTION | — | ✅ |
| 15 | GlCalendarsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | GlCalendarsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | GlCalendarsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | GlCalendarsLatestYearStartDate | LATEST_YEAR_START_DATE | — | ✅ |
| 19 | GlCalendarsLegacyCalendarFlag | LEGACY_CALENDAR_FLAG | — | ✅ |
| 20 | GlCalendarsLegacyRulesEnabledFlag | LEGACY_RULES_ENABLED_FLAG | — | ✅ |
| 21 | GlCalendarsNonAdjPeriodFreqCode | NON_ADJ_PERIOD_FREQ_CODE | — | ✅ |
| 22 | GlCalendarsNonAdjPeriodsNum | NON_ADJ_PERIODS_NUM | — | ✅ |
| 23 | GlCalendarsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | GlCalendarsPeriodNameFormatCode | PERIOD_NAME_FORMAT_CODE | — | ✅ |
| 25 | GlCalendarsPeriodNameSeparatorCode | PERIOD_NAME_SEPARATOR_CODE | — | ✅ |
| 26 | GlCalendarsPeriodSetId | PERIOD_SET_ID | 🔑 | ✅ |
| 27 | GlCalendarsPeriodSetName | PERIOD_SET_NAME | 🔑 | ✅ |
| 28 | GlCalendarsPeriodType | PERIOD_TYPE | 🔑 | ✅ |
| 29 | GlCalendarsPeriodTypeId | PERIOD_TYPE_ID | 🔑 | ✅ |
| 30 | GlCalendarsSecurityFlag | SECURITY_FLAG | — | ✅ |
| 31 | GlCalendarsUserPeriodNamePrefix | USER_PERIOD_NAME_PREFIX | — | ✅ |
| 32 | GlCalendarsUserPeriodSetName | USER_PERIOD_SET_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
