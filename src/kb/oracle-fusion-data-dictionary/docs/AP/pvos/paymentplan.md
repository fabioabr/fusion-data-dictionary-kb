---
id: DOC-AP-PVO-PaymentPlan
doc_type: system-doc
title: "PaymentPlan — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PaymentPlan
  - paymentplan
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentPlan

## 📌 Visão Geral

Extrai os planos de pagamento de compensação por incentivos (ICM), incluindo categorias, intervalos, expressões de cálculo, valores mínimos/máximos e regras de recuperação. Permite configurar e auditar as políticas de pagamento de comissões e bonificações de vendas.

**Caminho:** `FscmTopModelAM.PaymentPlanAM.PaymentPlan`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 5 | 1 | 24 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 6 atributos (2 BICC)
- [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]] — 5 atributos (1 BICC)
- [[cn_payment_plans_all_b|CN_PAYMENT_PLANS_ALL_B]] — 29 atributos (1 PKs, 17 BICC)
- [[cn_payment_plans_all_tl|CN_PAYMENT_PLANS_ALL_TL]] — 6 atributos (3 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpressionId | EXPRESSION_ID | — | — |
| 2 | ExpressionId1 | EXPRESSION_ID | — | — |
| 3 | ExpressionName | EXPRESSION_NAME | — | ✅ |
| 4 | ExpressionName1 | EXPRESSION_NAME | — | ✅ |
| 5 | OrgId1 | ORG_ID | — | — |
| 6 | OrgId2 | ORG_ID | — | — |

### [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntervalName | INTERVAL_NAME | — | ✅ |
| 2 | IntervalTypeId | INTERVAL_TYPE_ID | — | — |
| 3 | Language3 | LANGUAGE | — | — |
| 4 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 5 | OrgId3 | ORG_ID | — | — |

### [[cn_payment_plans_all_b|CN_PAYMENT_PLANS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | CreditTypeId | CREDIT_TYPE_ID | — | — |
| 4 | DelayRecoveryFlag | DELAY_RECOVERY_FLAG | — | ✅ |
| 5 | DrawEnd | DRAW_END | — | ✅ |
| 6 | DrawExpressionId | DRAW_EXPRESSION_ID | — | — |
| 7 | DrawPercentAmount | DRAW_PERCENT_AMOUNT | — | ✅ |
| 8 | EndDate | END_DATE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | MaxRecoveryAmount | MAX_RECOVERY_AMOUNT | — | ✅ |
| 13 | MaximumAmount | MAXIMUM_AMOUNT | — | ✅ |
| 14 | MinRecoverFlag | MIN_RECOVER_FLAG | — | ✅ |
| 15 | MinimumAmount | MINIMUM_AMOUNT | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrgId | ORG_ID | — | — |
| 18 | PayExcessLaterFlag | PAY_EXCESS_LATER_FLAG | — | ✅ |
| 19 | PayIntervalTypeId | PAY_INTERVAL_TYPE_ID | — | — |
| 20 | PaymentPlanCategory | PAYMENT_PLAN_CATEGORY | — | ✅ |
| 21 | PaymentPlanId | PAYMENT_PLAN_ID | 🔑 | ✅ |
| 22 | RecoverExpressionId | RECOVER_EXPRESSION_ID | — | — |
| 23 | RecoverIntervalTypeId | RECOVER_INTERVAL_TYPE_ID | — | — |
| 24 | RecoverPercentAmount | RECOVER_PERCENT_AMOUNT | — | ✅ |
| 25 | RecoveryEndIntervalId | RECOVERY_END_INTERVAL_ID | — | — |
| 26 | RecoveryEndIntervalId1 | RECOVERY_END_INTERVAL_ID | — | ✅ |
| 27 | RecoveryStartIntervalId | RECOVERY_START_INTERVAL_ID | — | — |
| 28 | RecoveryStartIntervalId1 | RECOVERY_START_INTERVAL_ID | — | ✅ |
| 29 | StartDate | START_DATE | — | ✅ |

### [[cn_payment_plans_all_tl|CN_PAYMENT_PLANS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 4 | PaymentPlanId1 | PAYMENT_PLAN_ID | — | — |
| 5 | PaymentPlanName | PAYMENT_PLAN_NAME | — | ✅ |
| 6 | SourceLang | SOURCE_LANG | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
