---
id: DOC-OTHER-PVO-CalendarPeriodExtractPVO
doc_type: system-doc
title: "CalendarPeriodExtractPVO — PVO Cross-Module"
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
  - CalendarPeriodExtractPVO
  - calendarperiodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CalendarPeriodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Calendar Period Extract. Acessa as tabelas: FA_CALENDAR_PERIODS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.CalendarPeriodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_calendar_periods|FA_CALENDAR_PERIODS]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fa_calendar_periods|FA_CALENDAR_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarPeriodCalendarType | CALENDAR_TYPE | 🔑 | ✅ |
| 2 | CalendarPeriodCreatedBy | CREATED_BY | — | ✅ |
| 3 | CalendarPeriodCreationDate | CREATION_DATE | — | ✅ |
| 4 | CalendarPeriodEndDate | END_DATE | — | ✅ |
| 5 | CalendarPeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CalendarPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | CalendarPeriodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | CalendarPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | CalendarPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 10 | CalendarPeriodPeriodNum | PERIOD_NUM | 🔑 | ✅ |
| 11 | CalendarPeriodStartDate | START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
