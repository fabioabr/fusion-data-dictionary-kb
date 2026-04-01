---
id: DOC-OTHER-PVO-SrpCompPlan
doc_type: system-doc
title: "SrpCompPlan — PVO Cross-Module"
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
  - SrpCompPlan
  - srpcompplan
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpCompPlan

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Comp Plan. Acessa as tabelas: CN_PARTICIPANT_ROLES, CN_SRP_COMP_PLANS_ALL, CN_SRP_PARTICIPANTS_ALL (+1).

**Caminho:** `FscmTopModelAM.SrpCompPlanAM.SrpCompPlan`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 111 | 4 | 1 | 35 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[cn_participant_roles|CN_PARTICIPANT_ROLES]] — 27 atributos (4 BICC)
- [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]] — 36 atributos (1 PKs, 12 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 42 atributos (14 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_participant_roles|CN_PARTICIPANT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
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
| 17 | CreatedBy2 | CREATED_BY | — | — |
| 18 | CreationDate2 | CREATION_DATE | — | — |
| 19 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 20 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 21 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 22 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 23 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 24 | ParticipantId2 | PARTICIPANT_ID | — | — |
| 25 | ParticipantRoleId | PARTICIPANT_ROLE_ID | — | ✅ |
| 26 | RoleId | ROLE_ID | — | — |
| 27 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[cn_srp_comp_plans_all|CN_SRP_COMP_PLANS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | — |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute2 | ATTRIBUTE2 | — | — |
| 10 | Attribute3 | ATTRIBUTE3 | — | — |
| 11 | Attribute4 | ATTRIBUTE4 | — | — |
| 12 | Attribute5 | ATTRIBUTE5 | — | — |
| 13 | Attribute6 | ATTRIBUTE6 | — | — |
| 14 | Attribute7 | ATTRIBUTE7 | — | — |
| 15 | Attribute8 | ATTRIBUTE8 | — | — |
| 16 | Attribute9 | ATTRIBUTE9 | — | — |
| 17 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | CompPlanId | COMP_PLAN_ID | — | — |
| 19 | CreatedBy | CREATED_BY | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 22 | CustomizedFlag | CUSTOMIZED_FLAG | — | ✅ |
| 23 | EndDate | END_DATE | — | ✅ |
| 24 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | OrgId | ORG_ID | — | ✅ |
| 29 | ParticipantId | PARTICIPANT_ID | — | — |
| 30 | ParticipantPlanNumber | PARTICIPANT_PLAN_NUMBER | — | — |
| 31 | RulePlanId | RULE_PLAN_ID | — | — |
| 32 | SrpCompPlanId | SRP_COMP_PLAN_ID | 🔑 | ✅ |
| 33 | SrpRuleId | SRP_RULE_ID | — | — |
| 34 | SrpRuleTypeCode | SRP_RULE_TYPE_CODE | — | ✅ |
| 35 | StartDate | START_DATE | — | ✅ |
| 36 | TargetIncentive | TARGET_INCENTIVE | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | Attribute101 | ATTRIBUTE10 | — | — |
| 4 | Attribute111 | ATTRIBUTE11 | — | — |
| 5 | Attribute121 | ATTRIBUTE12 | — | — |
| 6 | Attribute131 | ATTRIBUTE13 | — | — |
| 7 | Attribute141 | ATTRIBUTE14 | — | — |
| 8 | Attribute151 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE1 | — | — |
| 10 | Attribute21 | ATTRIBUTE2 | — | — |
| 11 | Attribute31 | ATTRIBUTE3 | — | — |
| 12 | Attribute41 | ATTRIBUTE4 | — | — |
| 13 | Attribute51 | ATTRIBUTE5 | — | — |
| 14 | Attribute61 | ATTRIBUTE6 | — | — |
| 15 | Attribute71 | ATTRIBUTE7 | — | — |
| 16 | Attribute81 | ATTRIBUTE8 | — | — |
| 17 | Attribute91 | ATTRIBUTE9 | — | — |
| 18 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 19 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 20 | CreatedBy1 | CREATED_BY | — | — |
| 21 | CreationDate1 | CREATION_DATE | — | — |
| 22 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 23 | EndDate1 | END_DATE | — | — |
| 24 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 25 | HoldReason | HOLD_REASON | — | ✅ |
| 26 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 27 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 30 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 33 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 34 | OrgId1 | ORG_ID | — | — |
| 35 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 36 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 37 | PartyId | PARTY_ID | — | ✅ |
| 38 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 39 | RequestId | REQUEST_ID | — | — |
| 40 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 41 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 42 | StartDate1 | START_DATE | — | — |

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
