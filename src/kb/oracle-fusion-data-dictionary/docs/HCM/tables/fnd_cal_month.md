---
id: DOC-HCM-116
doc_type: system-doc
title: "FND_CAL_MONTH — (título a preencher)"
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
  - FND_CAL_MONTH
  - fnd_cal_month
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CAL_MONTH

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAL_MONTH | — | — | — | — | — | — |
| 2 | CAL_MONTH_CODE | — | — | — | — | — | — |
| 3 | CAL_MONTH_END_DATE | — | — | — | — | — | — |
| 4 | CAL_MONTH_START_DATE | — | — | — | — | — | — |
| 5 | CREATED_BY | — | — | — | — | — | — |
| 6 | CREATION_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | PARENT_QUARTER | — | — | — | — | — | — |
| 11 | PRIOR_SEQUENTIAL_MONTH | — | — | — | — | — | — |
| 12 | PRIOR_YEAR_MONTH | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fndcalmonth|FndCalMonth]] (GL · BICC: 5/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_MONTH | CalMonth | ✅ |
| CAL_MONTH_CODE | CalMonthCode | ✅ |
| CAL_MONTH_END_DATE | CalMonthEndDate | ✅ |
| CAL_MONTH_START_DATE | CalMonthStartDate | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_QUARTER | ParentQuarter | — |
| PRIOR_SEQUENTIAL_MONTH | PriorSequentialMonth | — |
| PRIOR_YEAR_MONTH | PriorYearMonth | — |

### [[resourcerequestmonthpvo|ResourceRequestMonthPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_MONTH | CalMonth | — |
| CAL_MONTH_END_DATE | CalMonthEndDate | — |
| CAL_MONTH_START_DATE | CalMonthStartDate | — |
