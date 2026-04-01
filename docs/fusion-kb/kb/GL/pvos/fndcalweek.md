---
id: DOC-GL-PVO-FndCalWeek
doc_type: system-doc
title: "FndCalWeek — PVO General Ledger"
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
  - FndCalWeek
  - fndcalweek
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndCalWeek

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Cal Week. Acessa as tabelas: FND_CAL_WEEK.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GregorianCalendarAM.FndCalWeek`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 6 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_week|FND_CAL_WEEK]] — 12 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_cal_week|FND_CAL_WEEK]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalWeek | CAL_WEEK | 🔑 | ✅ |
| 2 | CalWeekCode | CAL_WEEK_CODE | — | ✅ |
| 3 | CalWeekEndDate | CAL_WEEK_END_DATE | — | ✅ |
| 4 | CalWeekStartDate | CAL_WEEK_START_DATE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ParentYear | PARENT_YEAR | — | ✅ |
| 11 | PriorSequentialWeek | PRIOR_SEQUENTIAL_WEEK | — | — |
| 12 | PriorYearWeek | PRIOR_YEAR_WEEK | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
