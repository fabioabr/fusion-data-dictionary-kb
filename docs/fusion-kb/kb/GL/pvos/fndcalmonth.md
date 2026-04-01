---
id: DOC-GL-PVO-FndCalMonth
doc_type: system-doc
title: "FndCalMonth — PVO General Ledger"
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
  - FndCalMonth
  - fndcalmonth
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndCalMonth

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Cal Month. Acessa as tabelas: FND_CAL_MONTH.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GregorianCalendarAM.FndCalMonth`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 5 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_cal_month|FND_CAL_MONTH]] — 12 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[fnd_cal_month|FND_CAL_MONTH]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalMonth | CAL_MONTH | 🔑 | ✅ |
| 2 | CalMonthCode | CAL_MONTH_CODE | — | ✅ |
| 3 | CalMonthEndDate | CAL_MONTH_END_DATE | — | ✅ |
| 4 | CalMonthStartDate | CAL_MONTH_START_DATE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ParentQuarter | PARENT_QUARTER | — | — |
| 11 | PriorSequentialMonth | PRIOR_SEQUENTIAL_MONTH | — | — |
| 12 | PriorYearMonth | PRIOR_YEAR_MONTH | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
