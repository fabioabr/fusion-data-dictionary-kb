---
id: DOC-GL-PVO-FndCalYear
doc_type: system-doc
title: "FndCalYear — PVO General Ledger"
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
  - FndCalYear
  - fndcalyear
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndCalYear

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Cal Year. Acessa as tabelas: FND_CAL_YEAR.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GregorianCalendarAM.FndCalYear`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 4 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_year|FND_CAL_YEAR]] — 10 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_cal_year|FND_CAL_YEAR]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalYear | CAL_YEAR | 🔑 | ✅ |
| 2 | CalYearEndDate | CAL_YEAR_END_DATE | — | ✅ |
| 3 | CalYearName | CAL_YEAR_NAME | — | — |
| 4 | CalYearStartDate | CAL_YEAR_START_DATE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PriorYear | PRIOR_YEAR | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
