---
id: DOC-OTHER-PVO-ReportingDeprnPeriodExtractPVO
doc_type: system-doc
title: "ReportingDeprnPeriodExtractPVO — PVO Cross-Module"
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
  - ReportingDeprnPeriodExtractPVO
  - reportingdeprnperiodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingDeprnPeriodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Deprn Period Extract. Acessa as tabelas: FA_MC_DEPRN_PERIODS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingDeprnPeriodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 3 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_deprn_periods|FA_MC_DEPRN_PERIODS]] — 17 atributos (3 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[fa_mc_deprn_periods|FA_MC_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingDeprnPeriodBookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 2 | ReportingDeprnPeriodCalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | ✅ |
| 3 | ReportingDeprnPeriodCalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | ✅ |
| 4 | ReportingDeprnPeriodCreatedBy | CREATED_BY | — | ✅ |
| 5 | ReportingDeprnPeriodCreationDate | CREATION_DATE | — | ✅ |
| 6 | ReportingDeprnPeriodDeprnRun | DEPRN_RUN | — | ✅ |
| 7 | ReportingDeprnPeriodFiscalYear | FISCAL_YEAR | — | ✅ |
| 8 | ReportingDeprnPeriodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ReportingDeprnPeriodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ReportingDeprnPeriodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ReportingDeprnPeriodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ReportingDeprnPeriodPeriodCloseDate | PERIOD_CLOSE_DATE | — | ✅ |
| 13 | ReportingDeprnPeriodPeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 14 | ReportingDeprnPeriodPeriodName | PERIOD_NAME | — | ✅ |
| 15 | ReportingDeprnPeriodPeriodNum | PERIOD_NUM | — | ✅ |
| 16 | ReportingDeprnPeriodPeriodOpenDate | PERIOD_OPEN_DATE | — | ✅ |
| 17 | ReportingDeprnPeriodSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
