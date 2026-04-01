---
id: DOC-OTHER-PVO-SrpFormMetric
doc_type: system-doc
title: "SrpFormMetric — PVO Cross-Module"
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
  - SrpFormMetric
  - srpformmetric
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpFormMetric

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Form Metric. Acessa as tabelas: CN_PARTICIPANT_ROLES, CN_SRP_COMP_PLANS_ALL, CN_SRP_FORM_METRICS_ALL (+4).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SrpFormMetric`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 185 | 7 | 1 | 44 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[cn_participant_roles|CN_PARTICIPANT_ROLES]] — 27 atributos (2 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 34 atributos (7 BICC)
- [[cn_srp_form_metrics_all|CN_SRP_FORM_METRICS_ALL]] — 30 atributos (1 PKs, 7 BICC)
- [[cn_srp_goals_all|CN_SRP_GOALS_ALL]] — 17 atributos (7 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 42 atributos (13 BICC)
- [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]] — 29 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_participant_roles|CN_PARTICIPANT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory4 | ATTRIBUTE_CATEGORY | — | — |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 10 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 11 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 12 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 13 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 14 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 15 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 16 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 17 | CreatedBy5 | CREATED_BY | — | — |
| 18 | CreationDate5 | CREATION_DATE | — | — |
| 19 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 20 | LastUpdateDate5 | LAST_UPDATE_DATE | — | — |
| 21 | LastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 22 | LastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 23 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 24 | ParticipantId3 | PARTICIPANT_ID | — | — |
| 25 | ParticipantRoleId | PARTICIPANT_ROLE_ID | — | — |
| 26 | RoleId | ROLE_ID | — | — |
| 27 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

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
| 19 | CreatedBy1 | CREATED_BY | — | — |
| 20 | CreationDate1 | CREATION_DATE | — | — |
| 21 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 22 | EndDate | END_DATE | — | ✅ |
| 23 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 25 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 26 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 27 | OrgId1 | ORG_ID | — | — |
| 28 | ParticipantId | PARTICIPANT_ID | — | — |
| 29 | RulePlanId | RULE_PLAN_ID | — | — |
| 30 | SrpCompPlanId1 | SRP_COMP_PLAN_ID | — | — |
| 31 | SrpRuleId | SRP_RULE_ID | — | — |
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
| 17 | CreatedBy | CREATED_BY | — | — |
| 18 | CreationDate | CREATION_DATE | — | ✅ |
| 19 | FormulaId | FORMULA_ID | — | — |
| 20 | GoalId | GOAL_ID | — | — |
| 21 | IncentiveFormulaFlag | INCENTIVE_FORMULA_FLAG | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | OrgId | ORG_ID | — | — |
| 27 | PlanComponentId | PLAN_COMPONENT_ID | — | ✅ |
| 28 | SrpCompPlanId | SRP_COMP_PLAN_ID | — | ✅ |
| 29 | SrpFormMetricId | SRP_FORM_METRIC_ID | 🔑 | ✅ |
| 30 | SrpPlanComponentId | SRP_PLAN_COMPONENT_ID | — | ✅ |

### [[cn_srp_goals_all|CN_SRP_GOALS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltTarget1 | ALT_TARGET_1 | — | ✅ |
| 2 | AltTarget2 | ALT_TARGET_2 | — | ✅ |
| 3 | AltTarget3 | ALT_TARGET_3 | — | ✅ |
| 4 | AltTarget4 | ALT_TARGET_4 | — | ✅ |
| 5 | AltTarget5 | ALT_TARGET_5 | — | ✅ |
| 6 | CreatedBy3 | CREATED_BY | — | — |
| 7 | CreationDate3 | CREATION_DATE | — | — |
| 8 | GoalId1 | GOAL_ID | — | — |
| 9 | LastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 10 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 12 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrgId3 | ORG_ID | — | — |
| 14 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 15 | SrpFormMetricId1 | SRP_FORM_METRIC_ID | — | — |
| 16 | SrpGoalId | SRP_GOAL_ID | — | ✅ |
| 17 | Target | TARGET | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | Attribute103 | ATTRIBUTE10 | — | — |
| 4 | Attribute113 | ATTRIBUTE11 | — | — |
| 5 | Attribute123 | ATTRIBUTE12 | — | — |
| 6 | Attribute133 | ATTRIBUTE13 | — | — |
| 7 | Attribute143 | ATTRIBUTE14 | — | — |
| 8 | Attribute153 | ATTRIBUTE15 | — | — |
| 9 | Attribute18 | ATTRIBUTE1 | — | — |
| 10 | Attribute23 | ATTRIBUTE2 | — | — |
| 11 | Attribute33 | ATTRIBUTE3 | — | — |
| 12 | Attribute43 | ATTRIBUTE4 | — | — |
| 13 | Attribute53 | ATTRIBUTE5 | — | — |
| 14 | Attribute63 | ATTRIBUTE6 | — | — |
| 15 | Attribute73 | ATTRIBUTE7 | — | — |
| 16 | Attribute83 | ATTRIBUTE8 | — | — |
| 17 | Attribute93 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory3 | ATTRIBUTE_CATEGORY | — | — |
| 19 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 20 | CreatedBy4 | CREATED_BY | — | — |
| 21 | CreationDate4 | CREATION_DATE | — | — |
| 22 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | — |
| 23 | EndDate1 | END_DATE | — | — |
| 24 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 25 | HoldReason | HOLD_REASON | — | ✅ |
| 26 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 27 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 30 | LastUpdateDate4 | LAST_UPDATE_DATE | — | — |
| 31 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 33 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 34 | OrgId4 | ORG_ID | — | — |
| 35 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 36 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 37 | PartyId | PARTY_ID | — | ✅ |
| 38 | PayeeOnly | PAYEE_ONLY | — | — |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 41 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 42 | StartDate1 | START_DATE | — | — |

### [[cn_srp_plan_components_all|CN_SRP_PLAN_COMPONENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute102 | ATTRIBUTE10 | — | — |
| 2 | Attribute112 | ATTRIBUTE11 | — | — |
| 3 | Attribute122 | ATTRIBUTE12 | — | — |
| 4 | Attribute132 | ATTRIBUTE13 | — | — |
| 5 | Attribute142 | ATTRIBUTE14 | — | — |
| 6 | Attribute152 | ATTRIBUTE15 | — | — |
| 7 | Attribute17 | ATTRIBUTE1 | — | — |
| 8 | Attribute22 | ATTRIBUTE2 | — | — |
| 9 | Attribute32 | ATTRIBUTE3 | — | — |
| 10 | Attribute42 | ATTRIBUTE4 | — | — |
| 11 | Attribute52 | ATTRIBUTE5 | — | — |
| 12 | Attribute62 | ATTRIBUTE6 | — | — |
| 13 | Attribute72 | ATTRIBUTE7 | — | — |
| 14 | Attribute82 | ATTRIBUTE8 | — | — |
| 15 | Attribute92 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 17 | CreatedBy2 | CREATED_BY | — | — |
| 18 | CreationDate2 | CREATION_DATE | — | — |
| 19 | CustomizedFlag1 | CUSTOMIZED_FLAG | — | ✅ |
| 20 | CustomizedOption | CUSTOMIZED_OPTION | — | ✅ |
| 21 | LastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 22 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 23 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 24 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 25 | OrgId2 | ORG_ID | — | — |
| 26 | PlanComponentId1 | PLAN_COMPONENT_ID | — | — |
| 27 | SrpCompPlanId2 | SRP_COMP_PLAN_ID | — | — |
| 28 | SrpPlanComponentId1 | SRP_PLAN_COMPONENT_ID | — | — |
| 29 | TargetIncentiveWeight | TARGET_INCENTIVE_WEIGHT | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 2 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 3 | ParticipantName | PARTY_NAME | — | ✅ |
| 4 | ParticipantPartyPEOPartyId | PARTY_ID | — | — |
| 5 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 6 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
