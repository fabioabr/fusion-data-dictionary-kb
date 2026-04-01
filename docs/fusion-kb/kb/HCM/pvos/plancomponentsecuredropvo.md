---
id: DOC-HCM-PVO-PlanComponentSecuredROPVO
doc_type: system-doc
title: "PlanComponentSecuredROPVO — PVO Human Capital Management"
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
  - PlanComponentSecuredROPVO
  - plancomponentsecuredropvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanComponentSecuredROPVO

## 📌 Visão Geral

Versão somente-leitura e segura dos componentes de plano de incentivos, com expressões e fórmulas. Combina segurança por business unit com visão analítica completa.

**Caminho:** `FscmTopModelAM.CompensationPlanAM.PlanComponentSecuredROPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 73 | 7 | 2 | 32 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 3 atributos (1 BICC)
- [[cn_formulas_all_b|CN_FORMULAS_ALL_B]] — 3 atributos
- [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]] — 5 atributos (2 BICC)
- [[cn_lookups|CN_LOOKUPS]] — 3 atributos (1 BICC)
- [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]] — 42 atributos (2 PKs, 23 BICC)
- [[cn_plan_components_all_tl|CN_PLAN_COMPONENTS_ALL_TL]] — 13 atributos (4 BICC)
- [[cn_plan_component_formulas_all|CN_PLAN_COMPONENT_FORMULAS_ALL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpressionId | EXPRESSION_ID | — | — |
| 2 | ExpressionName | EXPRESSION_NAME | — | ✅ |
| 3 | OrgId5 | ORG_ID | — | — |

### [[cn_formulas_all_b|CN_FORMULAS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormulaId | FORMULA_ID | — | — |
| 2 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId3 | ORG_ID | — | — |

### [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntervalName | INTERVAL_NAME | — | ✅ |
| 2 | IntervalTypeId | INTERVAL_TYPE_ID | — | ✅ |
| 3 | Language3 | LANGUAGE | — | — |
| 4 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgId4 | ORG_ID | — | — |

### [[cn_lookups|CN_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | — | — |
| 2 | LookupType | LOOKUP_TYPE | — | — |
| 3 | Meaning | MEANING | — | ✅ |

### [[cn_plan_components_all_b|CN_PLAN_COMPONENTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApExpId | AP_EXP_ID | — | ✅ |
| 2 | ApLiabId | AP_LIAB_ID | — | ✅ |
| 3 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 4 | Attribute1 | ATTRIBUTE1 | — | — |
| 5 | Attribute10 | ATTRIBUTE10 | — | — |
| 6 | Attribute11 | ATTRIBUTE11 | — | — |
| 7 | Attribute12 | ATTRIBUTE12 | — | — |
| 8 | Attribute13 | ATTRIBUTE13 | — | — |
| 9 | Attribute14 | ATTRIBUTE14 | — | — |
| 10 | Attribute15 | ATTRIBUTE15 | — | — |
| 11 | Attribute2 | ATTRIBUTE2 | — | — |
| 12 | Attribute3 | ATTRIBUTE3 | — | — |
| 13 | Attribute4 | ATTRIBUTE4 | — | — |
| 14 | Attribute5 | ATTRIBUTE5 | — | — |
| 15 | Attribute6 | ATTRIBUTE6 | — | — |
| 16 | Attribute7 | ATTRIBUTE7 | — | — |
| 17 | Attribute8 | ATTRIBUTE8 | — | — |
| 18 | Attribute9 | ATTRIBUTE9 | — | — |
| 19 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 20 | CalcVariableId | CALC_VARIABLE_ID | — | — |
| 21 | CalculationPhase | CALCULATION_PHASE | — | ✅ |
| 22 | CreatedBy | CREATED_BY | — | ✅ |
| 23 | CreationDate | CREATION_DATE | — | ✅ |
| 24 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 25 | DeleteFlag | DELETE_FLAG | — | ✅ |
| 26 | EarningTypeId | EARNING_TYPE_ID | — | — |
| 27 | EndDate | END_DATE | — | ✅ |
| 28 | IncentiveType | INCENTIVE_TYPE | — | ✅ |
| 29 | IncrementalType | INCREMENTAL_TYPE | — | ✅ |
| 30 | IndirectCredit | INDIRECT_CREDIT | — | ✅ |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | OrgId | ORG_ID | 🔑 | ✅ |
| 36 | PaymentGroupCode | PAYMENT_GROUP_CODE | — | ✅ |
| 37 | PlanCompStatus | PLAN_COMP_STATUS | — | ✅ |
| 38 | PlanComponentId | PLAN_COMPONENT_ID | 🔑 | ✅ |
| 39 | ReportGroup | REPORT_GROUP | — | ✅ |
| 40 | SalesrepEnddatedFlag | SALESREP_ENDDATED_FLAG | — | ✅ |
| 41 | StartDate | START_DATE | — | ✅ |
| 42 | ThirdpartyPayeeFlag | THIRDPARTY_PAYEE_FLAG | — | ✅ |

### [[cn_plan_components_all_tl|CN_PLAN_COMPONENTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayName | DISPLAY_NAME | — | ✅ |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | Language1 | LANGUAGE | — | — |
| 5 | Language2 | LANGUAGE | — | — |
| 6 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 7 | OrgId1 | ORG_ID | — | — |
| 8 | OrgId2 | ORG_ID | — | — |
| 9 | PlanComponentId1 | PLAN_COMPONENT_ID | — | — |
| 10 | PlanComponentId2 | PLAN_COMPONENT_ID | — | — |
| 11 | PlanComponentName | PLAN_COMPONENT_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | — |
| 13 | SourceLang1 | SOURCE_LANG | — | — |

### [[cn_plan_component_formulas_all|CN_PLAN_COMPONENT_FORMULAS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FormulaId1 | FORMULA_ID | — | — |
| 2 | IncentiveFormulaFlag | INCENTIVE_FORMULA_FLAG | — | ✅ |
| 3 | PlanCompFormulaId | PLAN_COMP_FORMULA_ID | — | — |
| 4 | PlanComponentId3 | PLAN_COMPONENT_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
