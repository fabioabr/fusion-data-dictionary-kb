---
id: DOC-GL-PVO-FndCalDay
doc_type: system-doc
title: "FndCalDay — PVO General Ledger"
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
  - FndCalDay
  - fndcalday
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndCalDay

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Cal Day. Acessa as tabelas: FND_CAL_DAY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GregorianCalendarAM.FndCalDay`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 6 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_day|FND_CAL_DAY]] — 11 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_cal_day|FND_CAL_DAY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DayOfMonth | DAY_OF_MONTH | — | ✅ |
| 4 | DayOfWeek | DAY_OF_WEEK | — | ✅ |
| 5 | DayOfYear | DAY_OF_YEAR | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ParentMonth | PARENT_MONTH | — | ✅ |
| 10 | ParentWeek | PARENT_WEEK | — | — |
| 11 | ReportDate | REPORT_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
