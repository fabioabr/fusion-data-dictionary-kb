---
id: DOC-HCM-115
doc_type: system-doc
title: "FND_CAL_DAY — (título a preencher)"
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
  - FND_CAL_DAY
  - fnd_cal_day
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_CAL_DAY

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DAY_OF_MONTH | — | — | — | — | — | — |
| 4 | DAY_OF_WEEK | — | — | — | — | — | — |
| 5 | DAY_OF_YEAR | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | PARENT_MONTH | — | — | — | — | — | — |
| 10 | PARENT_WEEK | — | — | — | — | — | — |
| 11 | REPORT_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fndcalday|FndCalDay]] (GL · BICC: 6/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DAY_OF_MONTH | DayOfMonth | ✅ |
| DAY_OF_WEEK | DayOfWeek | ✅ |
| DAY_OF_YEAR | DayOfYear | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| PARENT_MONTH | ParentMonth | ✅ |
| PARENT_WEEK | ParentWeek | — |
| REPORT_DATE | ReportDate | ✅ |
