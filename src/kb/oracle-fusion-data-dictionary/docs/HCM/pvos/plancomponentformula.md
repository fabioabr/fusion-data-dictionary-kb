---
id: DOC-HCM-PVO-PlanComponentFormula
doc_type: system-doc
title: "PlanComponentFormula — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PlanComponentFormula
  - plancomponentformula
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanComponentFormula

## 📌 Visão Geral

Extrai as fórmulas associadas aos componentes de planos de compensação de incentivos. Define as regras de cálculo para comissões, bônus e remuneração variável.

**Caminho:** `FscmTopModelAM.CompensationPlanAM.PlanComponentFormula`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cn_plan_component_formulas_all|CN_PLAN_COMPONENT_FORMULAS_ALL]] — 31 atributos (1 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[cn_plan_component_formulas_all|CN_PLAN_COMPONENT_FORMULAS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | Attribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | Attribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | Attribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | Attribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | Attribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | Attribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | Attribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | Attribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | Attribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | Attribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | Attribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | Attribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | Attribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | Attribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CalcVariableId | CALC_VARIABLE_ID | — | ✅ |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreationDate | CREATION_DATE | — | ✅ |
| 20 | EarningBasis | EARNING_BASIS | — | ✅ |
| 21 | FormulaId | FORMULA_ID | — | ✅ |
| 22 | FormulaSequence | FORMULA_SEQUENCE | — | ✅ |
| 23 | FormulaWeight | FORMULA_WEIGHT | — | ✅ |
| 24 | IncentiveFormulaFlag | INCENTIVE_FORMULA_FLAG | — | ✅ |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | OrgId | ORG_ID | — | ✅ |
| 30 | PlanCompFormulaId | PLAN_COMP_FORMULA_ID | 🔑 | ✅ |
| 31 | PlanComponentId | PLAN_COMPONENT_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
