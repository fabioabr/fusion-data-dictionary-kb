---
id: DOC-OTHER-PVO-FormulaRateTable
doc_type: system-doc
title: "FormulaRateTable — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - FormulaRateTable
  - formularatetable
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FormulaRateTable

## 📌 Visão Geral

View Object para extração BICC de dados de Formula Rate Table. Acessa as tabelas: CN_FORMULA_RATE_TABLES_ALL.

**Caminho:** `FscmTopModelAM.RateTableAM.FormulaRateTable`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cn_formula_rate_tables_all|CN_FORMULA_RATE_TABLES_ALL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[cn_formula_rate_tables_all|CN_FORMULA_RATE_TABLES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EndDate | END_DATE | — | ✅ |
| 4 | FormulaId | FORMULA_ID | — | ✅ |
| 5 | FormulaRateTableId | FORMULA_RATE_TABLE_ID | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | OrgId | ORG_ID | — | ✅ |
| 11 | RateTableId | RATE_TABLE_ID | — | ✅ |
| 12 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
