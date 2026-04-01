---
id: DOC-OTHER-PVO-FormulaDPVO
doc_type: system-doc
title: "FormulaDPVO — PVO Cross-Module"
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
  - FormulaDPVO
  - formuladpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FormulaDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Formula D. Acessa as tabelas: FF_FORMULAS_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.FormulaSearchAM.FormulaDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 3 | 5 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[ff_formulas_vl|FF_FORMULAS_VL]] — 19 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ff_formulas_vl|FF_FORMULAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormulaDPEOBaseFormulaName | BASE_FORMULA_NAME | — | — |
| 2 | FormulaDPEOCompileFlag | COMPILE_FLAG | — | — |
| 3 | FormulaDPEOCreatedBy | CREATED_BY | — | — |
| 4 | FormulaDPEOCreationDate | CREATION_DATE | — | — |
| 5 | FormulaDPEODescription | DESCRIPTION | — | — |
| 6 | FormulaDPEOEditStatus | EDIT_STATUS | — | — |
| 7 | FormulaDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | FormulaDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | FormulaDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | FormulaDPEOFormulaId | FORMULA_ID | 🔑 | ✅ |
| 11 | FormulaDPEOFormulaName | FORMULA_NAME | — | ✅ |
| 12 | FormulaDPEOFormulaText | FORMULA_TEXT | — | — |
| 13 | FormulaDPEOFormulaTypeId | FORMULA_TYPE_ID | — | — |
| 14 | FormulaDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | FormulaDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | FormulaDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | FormulaDPEOLegislationCode | LEGISLATION_CODE | — | — |
| 18 | FormulaDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 19 | FormulaDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
