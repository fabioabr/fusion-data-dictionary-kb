---
id: DOC-GL-PVO-FndCalQuarter
doc_type: system-doc
title: "FndCalQuarter — PVO General Ledger"
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
  - FndCalQuarter
  - fndcalquarter
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndCalQuarter

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Cal Quarter. Acessa as tabelas: FND_CAL_QUARTER.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GregorianCalendarAM.FndCalQuarter`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 5 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_quarter|FND_CAL_QUARTER]] — 12 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[fnd_cal_quarter|FND_CAL_QUARTER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalQtrEndDate | CAL_QTR_END_DATE | — | ✅ |
| 2 | CalQtrStartDate | CAL_QTR_START_DATE | — | ✅ |
| 3 | CalQuarter | CAL_QUARTER | 🔑 | ✅ |
| 4 | CalQuarterCode | CAL_QUARTER_CODE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ParentYear | PARENT_YEAR | — | — |
| 11 | PriorSequentialQtr | PRIOR_SEQUENTIAL_QTR | — | — |
| 12 | PriorYearQtr | PRIOR_YEAR_QTR | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
