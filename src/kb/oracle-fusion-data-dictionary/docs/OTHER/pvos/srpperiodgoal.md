---
id: DOC-OTHER-PVO-SrpPeriodGoal
doc_type: system-doc
title: "SrpPeriodGoal — PVO Cross-Module"
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
  - SrpPeriodGoal
  - srpperiodgoal
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpPeriodGoal

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Period Goal. Acessa as tabelas: CN_SRP_COMP_PLANS_ALL, CN_SRP_FORM_METRICS_ALL, CN_SRP_GOALS_ALL (+4).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SrpPeriodGoal`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 170 | 7 | 1 | 58 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 34 atributos (10 BICC)
- [[cn_srp_form_metrics_all|CN_SRP_FORM_METRICS_ALL]] — 30 atributos (4 BICC)
- [[cn_srp_goals_all|CN_SRP_GOALS_ALL]] — 17 atributos (7 BICC)
- [[cn_srp_interval_goals_all|CN_SRP_INTERVAL_GOALS_ALL]] — 17 atributos (7 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 42 atributos (10 BICC)
- [[cn_srp_per_goals_all|CN_SRP_PER_GOALS_ALL]] — 24 atributos (1 PKs, 16 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (4 BICC)

---

## ⚙️ Atributos

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | Attribute101 | ATTRIBUTE10 | — | — |
| 3 | Attribute111 | ATTRIBUTE11 | — | — |
| 4 | Attribute121 | ATTRIBUTE12 | — | — |
| 5 | Attribute131 | ATTRIBUTE13 | — | — |
| 6 | Attribute141 | ATTRIBUTE14 | — | — |
| 7 | Attribute151 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE1 | — | — |
| 9 | Attribute21 | ATTRIBUTE2 | — | — |
| 10 | Attribute31 | ATTRIBUTE3 | — | — |
| 11 | Attribute41 | ATTRIBUTE4 | — | — |
| 12 | Attribute51 | ATTRIBUTE5 | — | — |
| 13 | Attribute61 | ATTRIBUTE6 | — | — |
| 14 | Attribute71 | ATTRIBUTE7 | — | — |
| 15 | Attribute81 | ATTRIBUTE8 | — | — |
| 16 | Attribute91 | ATTRIBUTE9 | — | — |
| 17 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 18 | CompPlanId | COMP_PLAN_ID | — | — |
| 19 | CreatedBy4 | CREATED_BY | — | — |
| 20 | CreationDate4 | CREATION_DATE | — | — |
| 21 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 22 | EndDate | END_DATE | — | ✅ |
| 23 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 25 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 26 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrgId4 | ORG_ID | — | — |
| 28 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 29 | RulePlanId | RULE_PLAN_ID | — | ✅ |
| 30 | SrpCompPlanId1 | SRP_COMP_PLAN_ID | — | ✅ |
| 31 | SrpRuleId | SRP_RULE_ID | — | ✅ |
| 32 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 33 | StartDate | START_DATE | — | ✅ |
| 34 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_form_metrics_all|CN_SRP_FORM_METRICS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | CreatedBy3 | CREATED_BY | — | — |
| 18 | CreationDate3 | CREATION_DATE | — | — |
| 19 | FormulaId | FORMULA_ID | — | — |
| 20 | GoalId1 | GOAL_ID | — | — |
| 21 | IncentiveFormulaFlag | INCENTIVE_FORMULA_FLAG | — | ✅ |
| 22 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 25 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 26 | OrgId3 | ORG_ID | — | — |
| 27 | PlanComponentId | PLAN_COMPONENT_ID | — | ✅ |
| 28 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | ✅ |
| 29 | SrpFormMetricId1 | SRP_FORM_METRIC_ID | — | — |
| 30 | SrpPlanComponentId | SRP_PLAN_COMPONENT_ID | — | — |

### [[cn_srp_goals_all|CN_SRP_GOALS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltTarget1 | ALT_TARGET_1 | — | ✅ |
| 2 | AltTarget2 | ALT_TARGET_2 | — | ✅ |
| 3 | AltTarget3 | ALT_TARGET_3 | — | ✅ |
| 4 | AltTarget4 | ALT_TARGET_4 | — | ✅ |
| 5 | AltTarget5 | ALT_TARGET_5 | — | ✅ |
| 6 | CreatedBy2 | CREATED_BY | — | — |
| 7 | CreationDate2 | CREATION_DATE | — | — |
| 8 | GoalId | GOAL_ID | — | — |
| 9 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 12 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrgId2 | ORG_ID | — | — |
| 14 | ParticipantId | PARTICIPANT_ID | — | — |
| 15 | SrpFormMetricId | SRP_FORM_METRIC_ID | — | — |
| 16 | SrpGoalId1 | SRP_GOAL_ID | — | — |
| 17 | Target | TARGET | — | ✅ |

### [[cn_srp_interval_goals_all|CN_SRP_INTERVAL_GOALS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltTarget1Int | ALT_TARGET_1_INT | — | ✅ |
| 2 | AltTarget2Int | ALT_TARGET_2_INT | — | ✅ |
| 3 | AltTarget3Int | ALT_TARGET_3_INT | — | ✅ |
| 4 | AltTarget4Int | ALT_TARGET_4_INT | — | ✅ |
| 5 | AltTarget5Int | ALT_TARGET_5_INT | — | ✅ |
| 6 | CreatedBy1 | CREATED_BY | — | — |
| 7 | CreationDate1 | CREATION_DATE | — | — |
| 8 | IntervalGoalId | INTERVAL_GOAL_ID | — | — |
| 9 | IntervalNumber | INTERVAL_NUMBER | — | — |
| 10 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 13 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgId1 | ORG_ID | — | — |
| 15 | SrpGoalId | SRP_GOAL_ID | — | — |
| 16 | SrpIntervalGoalId1 | SRP_INTERVAL_GOAL_ID | — | — |
| 17 | TargetInt | TARGET_INT | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | — |
| 3 | Attribute102 | ATTRIBUTE10 | — | — |
| 4 | Attribute112 | ATTRIBUTE11 | — | — |
| 5 | Attribute122 | ATTRIBUTE12 | — | — |
| 6 | Attribute132 | ATTRIBUTE13 | — | — |
| 7 | Attribute142 | ATTRIBUTE14 | — | — |
| 8 | Attribute152 | ATTRIBUTE15 | — | — |
| 9 | Attribute17 | ATTRIBUTE1 | — | — |
| 10 | Attribute22 | ATTRIBUTE2 | — | — |
| 11 | Attribute32 | ATTRIBUTE3 | — | — |
| 12 | Attribute42 | ATTRIBUTE4 | — | — |
| 13 | Attribute52 | ATTRIBUTE5 | — | — |
| 14 | Attribute62 | ATTRIBUTE6 | — | — |
| 15 | Attribute72 | ATTRIBUTE7 | — | — |
| 16 | Attribute82 | ATTRIBUTE8 | — | — |
| 17 | Attribute92 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 19 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 20 | CreatedBy5 | CREATED_BY | — | — |
| 21 | CreationDate5 | CREATION_DATE | — | — |
| 22 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | — |
| 23 | EndDate1 | END_DATE | — | — |
| 24 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 25 | HoldReason | HOLD_REASON | — | ✅ |
| 26 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 27 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | LastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 33 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 34 | OrgId5 | ORG_ID | — | — |
| 35 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 36 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 37 | PartyId | PARTY_ID | — | — |
| 38 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 41 | SourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 42 | StartDate1 | START_DATE | — | — |

### [[cn_srp_per_goals_all|CN_SRP_PER_GOALS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltTarget1Itd | ALT_TARGET_1_ITD | — | ✅ |
| 2 | AltTarget1Per | ALT_TARGET_1_PER | — | ✅ |
| 3 | AltTarget2Itd | ALT_TARGET_2_ITD | — | ✅ |
| 4 | AltTarget2Per | ALT_TARGET_2_PER | — | ✅ |
| 5 | AltTarget3Itd | ALT_TARGET_3_ITD | — | ✅ |
| 6 | AltTarget3Per | ALT_TARGET_3_PER | — | ✅ |
| 7 | AltTarget4Itd | ALT_TARGET_4_ITD | — | ✅ |
| 8 | AltTarget4Per | ALT_TARGET_4_PER | — | ✅ |
| 9 | AltTarget5Itd | ALT_TARGET_5_ITD | — | ✅ |
| 10 | AltTarget5Per | ALT_TARGET_5_PER | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | — |
| 12 | CreationDate | CREATION_DATE | — | — |
| 13 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | OrgId | ORG_ID | — | ✅ |
| 19 | PeriodGoalId | PERIOD_GOAL_ID | — | — |
| 20 | PeriodId | PERIOD_ID | — | — |
| 21 | SrpIntervalGoalId | SRP_INTERVAL_GOAL_ID | — | — |
| 22 | SrpPerGoalId | SRP_PER_GOAL_ID | 🔑 | ✅ |
| 23 | TargetItd | TARGET_ITD | — | ✅ |
| 24 | TargetPer | TARGET_PER | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 2 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 3 | ParticipantName | PARTY_NAME | — | ✅ |
| 4 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 5 | PartyNumber | PARTY_NUMBER | — | — |
| 6 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
