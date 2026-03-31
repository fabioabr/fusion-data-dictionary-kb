---
id: DOC-OTHER-PVO-FormulaROPVO
doc_type: system-doc
title: "FormulaROPVO — PVO Cross-Module"
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
  - FormulaROPVO
  - formularopvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FormulaROPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Formula RO. Acessa as tabelas: CN_EXPRESSIONS_ALL_TL, CN_FORMULAS_ALL_B, CN_FORMULAS_ALL_TL (+1).

**Caminho:** `FscmTopModelAM.FormulaAM.FormulaROPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 4 | 2 | 19 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 2 atributos (1 BICC)
- [[cn_formulas_all_b|CN_FORMULAS_ALL_B]] — 29 atributos (1 PKs, 11 BICC)
- [[cn_formulas_all_tl|CN_FORMULAS_ALL_TL]] — 6 atributos (1 PKs, 5 BICC)
- [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpressionId | EXPRESSION_ID | — | — |
| 2 | ExpressionName | EXPRESSION_NAME | — | ✅ |

### [[cn_formulas_all_b|CN_FORMULAS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccumulationFlag | ACCUMULATION_FLAG | — | ✅ |
| 2 | AccumulationInterval | ACCUMULATION_INTERVAL | — | ✅ |
| 3 | Attribute1 | ATTRIBUTE1 | — | — |
| 4 | Attribute10 | ATTRIBUTE10 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute2 | ATTRIBUTE2 | — | — |
| 11 | Attribute3 | ATTRIBUTE3 | — | — |
| 12 | Attribute4 | ATTRIBUTE4 | — | — |
| 13 | Attribute5 | ATTRIBUTE5 | — | — |
| 14 | Attribute6 | ATTRIBUTE6 | — | — |
| 15 | Attribute7 | ATTRIBUTE7 | — | — |
| 16 | Attribute8 | ATTRIBUTE8 | — | — |
| 17 | Attribute9 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | EndDate | END_DATE | — | ✅ |
| 20 | FormulaId1 | FORMULA_ID | 🔑 | ✅ |
| 21 | FormulaStatus | FORMULA_STATUS | — | ✅ |
| 22 | FormulaTypeCode | FORMULA_TYPE_CODE | — | ✅ |
| 23 | NumberDim | NUMBER_DIM | — | ✅ |
| 24 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | OrgId | ORG_ID | — | — |
| 26 | ProcessTxn | PROCESS_TXN | — | ✅ |
| 27 | ReportEnabledFlag | REPORT_ENABLED_FLAG | — | ✅ |
| 28 | StartDate | START_DATE | — | ✅ |
| 29 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |

### [[cn_formulas_all_tl|CN_FORMULAS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayName | DISPLAY_NAME | — | ✅ |
| 3 | FormulaId | FORMULA_ID | 🔑 | ✅ |
| 4 | FormulaName | FORMULA_NAME | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntervalName | INTERVAL_NAME | — | ✅ |
| 2 | IntervalTypeId | INTERVAL_TYPE_ID | — | ✅ |
| 3 | Language1 | LANGUAGE | — | — |
| 4 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgId1 | ORG_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
