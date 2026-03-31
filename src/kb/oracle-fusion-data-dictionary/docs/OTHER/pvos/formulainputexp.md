---
id: DOC-OTHER-PVO-FormulaInputExp
doc_type: system-doc
title: "FormulaInputExp — PVO Cross-Module"
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
  - FormulaInputExp
  - formulainputexp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FormulaInputExp

## 📌 Visão Geral

View Object para extração BICC de dados de Formula Input Exp. Acessa as tabelas: CN_FORMULA_INPUT_EXPS_ALL.

**Caminho:** `FscmTopModelAM.FormulaAM.FormulaInputExp`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cn_formula_input_exps_all|CN_FORMULA_INPUT_EXPS_ALL]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cn_formula_input_exps_all|CN_FORMULA_INPUT_EXPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccumulateFlag | ACCUMULATE_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | ExpressionId | EXPRESSION_ID | — | ✅ |
| 5 | FormulaId | FORMULA_ID | — | ✅ |
| 6 | FormulaInputExpId | FORMULA_INPUT_EXP_ID | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OrgId | ORG_ID | — | ✅ |
| 12 | RateDimSequence | RATE_DIM_SEQUENCE | — | ✅ |
| 13 | SplitFlag | SPLIT_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
