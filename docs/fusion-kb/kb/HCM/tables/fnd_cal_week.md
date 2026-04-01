---
id: DOC-HCM-118
doc_type: system-doc
title: "FND_CAL_WEEK — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_CAL_WEEK
  - fnd_cal_week
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CAL_WEEK

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAL_WEEK | — | — | — | — | — | — |
| 2 | CAL_WEEK_CODE | — | — | — | — | — | — |
| 3 | CAL_WEEK_END_DATE | — | — | — | — | — | — |
| 4 | CAL_WEEK_START_DATE | — | — | — | — | — | — |
| 5 | CREATED_BY | — | — | — | — | — | — |
| 6 | CREATION_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | PARENT_YEAR | — | — | — | — | — | — |
| 11 | PRIOR_SEQUENTIAL_WEEK | — | — | — | — | — | — |
| 12 | PRIOR_YEAR_WEEK | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fndcalweek|FndCalWeek]] (GL · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_WEEK | CalWeek | ✅ |
| CAL_WEEK_CODE | CalWeekCode | ✅ |
| CAL_WEEK_END_DATE | CalWeekEndDate | ✅ |
| CAL_WEEK_START_DATE | CalWeekStartDate | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_YEAR | ParentYear | ✅ |
| PRIOR_SEQUENTIAL_WEEK | PriorSequentialWeek | — |
| PRIOR_YEAR_WEEK | PriorYearWeek | — |

### [[resourcerequestweekpvo|ResourceRequestWeekPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_WEEK | CalWeek | ✅ |
| CAL_WEEK_END_DATE | CalWeekEndDate | — |
| CAL_WEEK_START_DATE | CalWeekStartDate | — |
