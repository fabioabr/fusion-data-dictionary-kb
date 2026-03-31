---
id: DOC-OTHER-PVO-DepreciationPeriodPVO
doc_type: system-doc
title: "DepreciationPeriodPVO — PVO Cross-Module"
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
  - DepreciationPeriodPVO
  - depreciationperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DepreciationPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Depreciation Period. Acessa as tabelas: FA_DEPRN_PERIODS.

**Caminho:** `FscmTopModelAM.FinFaSharedSetupBookCtrlsAM.DepreciationPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 3 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deprn_periods|FA_DEPRN_PERIODS]] — 16 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[fa_deprn_periods|FA_DEPRN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookTypeCode | BOOK_TYPE_CODE | 🔑 | ✅ |
| 2 | CalendarPeriodCloseDate | CALENDAR_PERIOD_CLOSE_DATE | — | — |
| 3 | CalendarPeriodOpenDate | CALENDAR_PERIOD_OPEN_DATE | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | DeprnRun | DEPRN_RUN | — | — |
| 7 | FiscalYear | FISCAL_YEAR | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PeriodCloseDate | PERIOD_CLOSE_DATE | — | — |
| 13 | PeriodCounter | PERIOD_COUNTER | 🔑 | ✅ |
| 14 | PeriodName | PERIOD_NAME | — | — |
| 15 | PeriodNum | PERIOD_NUM | — | — |
| 16 | PeriodOpenDate | PERIOD_OPEN_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
