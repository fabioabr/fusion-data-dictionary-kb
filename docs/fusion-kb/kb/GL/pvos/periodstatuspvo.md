---
id: DOC-GL-PVO-PeriodStatusPVO
doc_type: system-doc
title: "PeriodStatusPVO — PVO General Ledger"
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
  - PeriodStatusPVO
  - periodstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Period Status. Acessa as tabelas: FND_APPLICATION_VL, GL_PERIOD_STATUSES, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.FinGlCalAccAM.PeriodStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 4 | 3 | 16 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_application_vl|FND_APPLICATION_VL]] — 3 atributos (1 BICC)
- [[gl_period_statuses|GL_PERIOD_STATUSES]] — 25 atributos (3 PKs, 14 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)
- [[per_users|PER_USERS]] — 2 atributos

---

## ⚙️ Atributos

### [[fnd_application_vl|FND_APPLICATION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationPEOApplicationId | APPLICATION_ID | — | — |
| 2 | ApplicationPEOApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | ApplicationPEOApplicationShortName | APPLICATION_SHORT_NAME | — | — |

### [[gl_period_statuses|GL_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | — |
| 2 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 3 | ChronologicalSeqStatusCode | CHRONOLOGICAL_SEQ_STATUS_CODE | — | — |
| 4 | ClosingStatus | CLOSING_STATUS | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | EffectivePeriodNum | EFFECTIVE_PERIOD_NUM | — | ✅ |
| 8 | EliminationConfirmedFlag | ELIMINATION_CONFIRMED_FLAG | — | — |
| 9 | EndDate | END_DATE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 14 | MigrationStatusCode | MIGRATION_STATUS_CODE | — | — |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 17 | PeriodNum | PERIOD_NUM | — | — |
| 18 | PeriodType | PERIOD_TYPE | — | ✅ |
| 19 | PeriodYear | PERIOD_YEAR | — | ✅ |
| 20 | QuarterNum | QUARTER_NUM | — | ✅ |
| 21 | QuarterStartDate | QUARTER_START_DATE | — | ✅ |
| 22 | SetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 23 | StartDate | START_DATE | — | ✅ |
| 24 | TrackBcYtdFlag | TRACK_BC_YTD_FLAG | — | — |
| 25 | YearStartDate | YEAR_START_DATE | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonLastUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonLastUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonLastUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 4 | PersonLastUpdatedByUserName | DISPLAY_NAME | — | ✅ |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserLastUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserLastUpdatedByUserId | USER_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
