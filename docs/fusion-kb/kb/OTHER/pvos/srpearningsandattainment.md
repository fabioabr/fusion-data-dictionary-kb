---
id: DOC-OTHER-PVO-SrpEarningsAndAttainment
doc_type: system-doc
title: "SrpEarningsAndAttainment — PVO Cross-Module"
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
  - SrpEarningsAndAttainment
  - srpearningsandattainment
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpEarningsAndAttainment

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Earnings And Attainment. Acessa as tabelas: CN_PARTICIPANT_ROLES, CN_SRP_COMP_PLANS_ALL, CN_SRP_GOALS_V (+3).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SrpEarningsAndAttainment`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 99 | 6 | 1 | 65 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[cn_participant_roles|CN_PARTICIPANT_ROLES]] — 4 atributos (3 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 10 atributos (6 BICC)
- [[cn_srp_goals_v|CN_SRP_GOALS_V]] — 28 atributos (25 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 4 atributos (2 BICC)
- [[cn_srp_per_form_metrics_all|CN_SRP_PER_FORM_METRICS_ALL]] — 51 atributos (1 PKs, 28 BICC)
- [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_participant_roles|CN_PARTICIPANT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantRoleEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 2 | ParticipantRoleId | PARTICIPANT_ROLE_ID | — | ✅ |
| 3 | ParticipantRoleStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 4 | RoleId | ROLE_ID | — | — |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | CompPlanId | COMP_PLAN_ID | — | — |
| 3 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | RulePlanId | RULE_PLAN_ID | — | — |
| 6 | SrpCompPlanId1 | SRP_COMP_PLAN_ID | — | — |
| 7 | SrpRuleId | SRP_RULE_ID | — | — |
| 8 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 9 | StartDate | START_DATE | — | ✅ |
| 10 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_goals_v|CN_SRP_GOALS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltTarget1 | ALT_TARGET_1 | — | ✅ |
| 2 | AltTarget1Int | ALT_TARGET_1_INT | — | ✅ |
| 3 | AltTarget1Itd | ALT_TARGET_1_ITD | — | ✅ |
| 4 | AltTarget1Per | ALT_TARGET_1_PER | — | ✅ |
| 5 | AltTarget2 | ALT_TARGET_2 | — | ✅ |
| 6 | AltTarget2Int | ALT_TARGET_2_INT | — | ✅ |
| 7 | AltTarget2Itd | ALT_TARGET_2_ITD | — | ✅ |
| 8 | AltTarget2Per | ALT_TARGET_2_PER | — | ✅ |
| 9 | AltTarget3 | ALT_TARGET_3 | — | ✅ |
| 10 | AltTarget3Int | ALT_TARGET_3_INT | — | ✅ |
| 11 | AltTarget3Itd | ALT_TARGET_3_ITD | — | ✅ |
| 12 | AltTarget3Per | ALT_TARGET_3_PER | — | ✅ |
| 13 | AltTarget4 | ALT_TARGET_4 | — | ✅ |
| 14 | AltTarget4Int | ALT_TARGET_4_INT | — | ✅ |
| 15 | AltTarget4Itd | ALT_TARGET_4_ITD | — | ✅ |
| 16 | AltTarget4Per | ALT_TARGET_4_PER | — | ✅ |
| 17 | AltTarget5 | ALT_TARGET_5 | — | ✅ |
| 18 | AltTarget5Int | ALT_TARGET_5_INT | — | ✅ |
| 19 | AltTarget5Itd | ALT_TARGET_5_ITD | — | ✅ |
| 20 | AltTarget5Per | ALT_TARGET_5_PER | — | ✅ |
| 21 | GoalTarget | GOAL_TARGET | — | ✅ |
| 22 | IntervalGoalId | INTERVAL_GOAL_ID | — | — |
| 23 | IntervalNumber | INTERVAL_NUMBER | — | ✅ |
| 24 | IntervalTarget | INTERVAL_TARGET | — | ✅ |
| 25 | SrpIntervalGoalId | SRP_INTERVAL_GOAL_ID | — | — |
| 26 | SrpPerGoalId | SRP_PER_GOAL_ID | — | — |
| 27 | TargetItd | TARGET_ITD | — | ✅ |
| 28 | TargetPer | TARGET_PER | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgId1 | ORG_ID | — | — |
| 2 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 3 | PartyId | PARTY_ID | — | ✅ |
| 4 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |

### [[cn_srp_per_form_metrics_all|CN_SRP_PER_FORM_METRICS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdvanceRecoveredItd | ADVANCE_RECOVERED_ITD | — | ✅ |
| 2 | AdvanceRecoveredPtd | ADVANCE_RECOVERED_PTD | — | ✅ |
| 3 | AdvanceToRecItd | ADVANCE_TO_REC_ITD | — | ✅ |
| 4 | AdvanceToRecPtd | ADVANCE_TO_REC_PTD | — | ✅ |
| 5 | Attribute1 | ATTRIBUTE1 | — | — |
| 6 | Attribute10 | ATTRIBUTE10 | — | — |
| 7 | Attribute11 | ATTRIBUTE11 | — | — |
| 8 | Attribute12 | ATTRIBUTE12 | — | — |
| 9 | Attribute13 | ATTRIBUTE13 | — | — |
| 10 | Attribute14 | ATTRIBUTE14 | — | — |
| 11 | Attribute15 | ATTRIBUTE15 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute3 | ATTRIBUTE3 | — | — |
| 14 | Attribute4 | ATTRIBUTE4 | — | — |
| 15 | Attribute5 | ATTRIBUTE5 | — | — |
| 16 | Attribute6 | ATTRIBUTE6 | — | — |
| 17 | Attribute7 | ATTRIBUTE7 | — | — |
| 18 | Attribute8 | ATTRIBUTE8 | — | — |
| 19 | Attribute9 | ATTRIBUTE9 | — | — |
| 20 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | CommissionPaidItd | COMMISSION_PAID_ITD | — | ✅ |
| 22 | CommissionPaidPtd | COMMISSION_PAID_PTD | — | ✅ |
| 23 | CommissionPaidTuitd | COMMISSION_PAID_TUITD | — | ✅ |
| 24 | CommissionPendItd | COMMISSION_PEND_ITD | — | ✅ |
| 25 | CommissionPendPtd | COMMISSION_PEND_PTD | — | ✅ |
| 26 | CreatedBy | CREATED_BY | — | ✅ |
| 27 | CreationDate | CREATION_DATE | — | ✅ |
| 28 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 29 | FormulaId | FORMULA_ID | — | — |
| 30 | GoalId | GOAL_ID | — | ✅ |
| 31 | InputAchievedItd | INPUT_ACHIEVED_ITD | — | ✅ |
| 32 | InputAchievedPtd | INPUT_ACHIEVED_PTD | — | ✅ |
| 33 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | OrgId | ORG_ID | — | ✅ |
| 38 | OutputAchievedItd | OUTPUT_ACHIEVED_ITD | — | ✅ |
| 39 | OutputAchievedPtd | OUTPUT_ACHIEVED_PTD | — | ✅ |
| 40 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 41 | PeriodId | PERIOD_ID | — | ✅ |
| 42 | PlanComponentId | PLAN_COMPONENT_ID | — | — |
| 43 | RecoveryAmountItd | RECOVERY_AMOUNT_ITD | — | ✅ |
| 44 | RecoveryAmountPtd | RECOVERY_AMOUNT_PTD | — | ✅ |
| 45 | Rollover | ROLLOVER | — | ✅ |
| 46 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | ✅ |
| 47 | SrpFormMetricId | SRP_FORM_METRIC_ID | — | — |
| 48 | SrpPerFormMetricId | SRP_PER_FORM_METRIC_ID | 🔑 | ✅ |
| 49 | SrpPlanComponentId | SRP_PLAN_COMPONENT_ID | — | — |
| 50 | TransactionAmountItd | TRANSACTION_AMOUNT_ITD | — | ✅ |
| 51 | TransactionAmountPtd | TRANSACTION_AMOUNT_PTD | — | ✅ |

### [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrpPlanComponentId1 | SRP_PLAN_COMPONENT_ID | — | — |
| 2 | TargetIncentiveWeight | TARGET_INCENTIVE_WEIGHT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
