---
id: DOC-OTHER-PVO-Formula
doc_type: system-doc
title: "Formula — PVO Cross-Module"
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
  - Formula
  - formula
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Formula

## 📌 Visão Geral

View Object para extração BICC de dados de Formula. Acessa as tabelas: CN_EXPRESSIONS_ALL_TL, CN_FORMULAS_ALL_B, CN_FORMULAS_ALL_TL (+5).

**Caminho:** `FscmTopModelAM.FormulaAM.Formula`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 8 | 1 | 38 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 3 atributos (1 BICC)
- [[cn_formulas_all_b|CN_FORMULAS_ALL_B]] — 26 atributos (1 PKs, 23 BICC)
- [[cn_formulas_all_tl|CN_FORMULAS_ALL_TL]] — 6 atributos (4 BICC)
- [[cn_goals_all_b|CN_GOALS_ALL_B]] — 9 atributos (6 BICC)
- [[cn_goals_all_tl|CN_GOALS_ALL_TL]] — 3 atributos
- [[cn_interval_types_all_b|CN_INTERVAL_TYPES_ALL_B]] — 3 atributos (1 BICC)
- [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]] — 5 atributos (2 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpressionId | EXPRESSION_ID | — | — |
| 2 | ExpressionName | EXPRESSION_NAME | — | ✅ |
| 3 | OrgId3 | ORG_ID | — | — |

### [[cn_formulas_all_b|CN_FORMULAS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccumulationFlag | ACCUMULATION_FLAG | — | ✅ |
| 2 | AccumulationInterval | ACCUMULATION_INTERVAL | — | ✅ |
| 3 | CalcVariableId | CALC_VARIABLE_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EndDate | END_DATE | — | ✅ |
| 7 | ExtFormulaName | EXT_FORMULA_NAME | — | ✅ |
| 8 | FormulaId | FORMULA_ID | 🔑 | ✅ |
| 9 | FormulaStatus | FORMULA_STATUS | — | ✅ |
| 10 | FormulaTypeCode | FORMULA_TYPE_CODE | — | ✅ |
| 11 | GoalId | GOAL_ID | — | ✅ |
| 12 | ItdFlag | ITD_FLAG | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | NumberDim | NUMBER_DIM | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | OrgId | ORG_ID | — | — |
| 19 | OutputExpId | OUTPUT_EXP_ID | — | ✅ |
| 20 | PackageName | PACKAGE_NAME | — | ✅ |
| 21 | ProcessTxn | PROCESS_TXN | — | ✅ |
| 22 | ReportEnabledFlag | REPORT_ENABLED_FLAG | — | ✅ |
| 23 | SplitOption | SPLIT_OPTION | — | ✅ |
| 24 | StartDate | START_DATE | — | ✅ |
| 25 | UnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 26 | UseExtFormulaFlag | USE_EXT_FORMULA_FLAG | — | ✅ |

### [[cn_formulas_all_tl|CN_FORMULAS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayName | DISPLAY_NAME | — | ✅ |
| 3 | FormulaId1 | FORMULA_ID | — | — |
| 4 | FormulaName | FORMULA_NAME | — | ✅ |
| 5 | Language | LANGUAGE | — | ✅ |
| 6 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |

### [[cn_goals_all_b|CN_GOALS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccumulationIntervalId | ACCUMULATION_INTERVAL_ID | — | — |
| 2 | AltTarget1 | ALT_TARGET_1 | — | ✅ |
| 3 | AltTarget2 | ALT_TARGET_2 | — | ✅ |
| 4 | AltTarget3 | ALT_TARGET_3 | — | ✅ |
| 5 | AltTarget4 | ALT_TARGET_4 | — | ✅ |
| 6 | AltTarget5 | ALT_TARGET_5 | — | ✅ |
| 7 | GoalId1 | GOAL_ID | — | — |
| 8 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 9 | Target | TARGET | — | ✅ |

### [[cn_goals_all_tl|CN_GOALS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId2 | GOAL_ID | — | — |
| 2 | Language2 | LANGUAGE | — | — |
| 3 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |

### [[cn_interval_types_all_b|CN_INTERVAL_TYPES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntervalTypeId1 | INTERVAL_TYPE_ID | — | ✅ |
| 2 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId2 | ORG_ID | — | — |

### [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntervalName | INTERVAL_NAME | — | ✅ |
| 2 | IntervalTypeId | INTERVAL_TYPE_ID | — | ✅ |
| 3 | Language1 | LANGUAGE | — | — |
| 4 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgId1 | ORG_ID | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
