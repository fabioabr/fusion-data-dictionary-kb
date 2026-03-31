---
id: DOC-HCM-117
doc_type: system-doc
title: "FND_CAL_QUARTER — (título a preencher)"
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
  - FND_CAL_QUARTER
  - fnd_cal_quarter
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CAL_QUARTER

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAL_QTR_END_DATE | — | — | — | — | — | — |
| 2 | CAL_QTR_START_DATE | — | — | — | — | — | — |
| 3 | CAL_QUARTER | — | — | — | — | — | — |
| 4 | CAL_QUARTER_CODE | — | — | — | — | — | — |
| 5 | CREATED_BY | — | — | — | — | — | — |
| 6 | CREATION_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | PARENT_YEAR | — | — | — | — | — | — |
| 11 | PRIOR_SEQUENTIAL_QTR | — | — | — | — | — | — |
| 12 | PRIOR_YEAR_QTR | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fndcalquarter|FndCalQuarter]] (GL · BICC: 5/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_QTR_END_DATE | CalQtrEndDate | ✅ |
| CAL_QTR_START_DATE | CalQtrStartDate | ✅ |
| CAL_QUARTER | CalQuarter | ✅ |
| CAL_QUARTER_CODE | CalQuarterCode | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_YEAR | ParentYear | — |
| PRIOR_SEQUENTIAL_QTR | PriorSequentialQtr | — |
| PRIOR_YEAR_QTR | PriorYearQtr | — |

### [[resourcerequestquarterpvo|ResourceRequestQuarterPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAL_QTR_END_DATE | CalQtrEndDate | — |
| CAL_QTR_START_DATE | CalQtrStartDate | — |
| CAL_QUARTER | CalQuarter | ✅ |
