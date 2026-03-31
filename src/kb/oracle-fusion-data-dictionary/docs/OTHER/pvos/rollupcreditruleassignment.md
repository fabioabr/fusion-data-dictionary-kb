---
id: DOC-OTHER-PVO-RollupCreditRuleAssignment
doc_type: system-doc
title: "RollupCreditRuleAssignment — PVO Cross-Module"
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
  - RollupCreditRuleAssignment
  - rollupcreditruleassignment
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RollupCreditRuleAssignment

## 📌 Visão Geral

View Object para extração BICC de dados de Rollup Credit Rule Assignment. Acessa as tabelas: CN_RS_RULES_ALL_B, CN_RS_RULES_HIERARCHY_CF_ALL, CN_RS_RULE_ASSIGNMENTS_ALL (+2).

**Caminho:** `FscmTopModelAM.RuleAM.RollupCreditRuleAssignment`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 5 | 1 | 34 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rs_rules_all_b|CN_RS_RULES_ALL_B]] — 2 atributos
- [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]] — 26 atributos
- [[cn_rs_rule_assignments_all|CN_RS_RULE_ASSIGNMENTS_ALL]] — 19 atributos (1 PKs, 13 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 25 atributos (16 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_rs_rules_all_b|CN_RS_RULES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RulePEORuleId | RULE_ID | — | — |
| 2 | RulePEOUsageId | USAGE_ID | — | — |

### [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleHierCFPEOBaseRuleId | BASE_RULE_ID | — | — |
| 2 | RuleHierCFPEOBaseRuleUsageId | BASE_RULE_USAGE_ID | — | — |
| 3 | RuleHierCFPEOCreatedBy | CREATED_BY | — | — |
| 4 | RuleHierCFPEOCreationDate | CREATION_DATE | — | — |
| 5 | RuleHierCFPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | RuleHierCFPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | RuleHierCFPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | RuleHierCFPEOLevel01RuleId | LEVEL_01_RULE_ID | — | — |
| 9 | RuleHierCFPEOLevel02RuleId | LEVEL_02_RULE_ID | — | — |
| 10 | RuleHierCFPEOLevel03RuleId | LEVEL_03_RULE_ID | — | — |
| 11 | RuleHierCFPEOLevel04RuleId | LEVEL_04_RULE_ID | — | — |
| 12 | RuleHierCFPEOLevel05RuleId | LEVEL_05_RULE_ID | — | — |
| 13 | RuleHierCFPEOLevel06RuleId | LEVEL_06_RULE_ID | — | — |
| 14 | RuleHierCFPEOLevel07RuleId | LEVEL_07_RULE_ID | — | — |
| 15 | RuleHierCFPEOLevel08RuleId | LEVEL_08_RULE_ID | — | — |
| 16 | RuleHierCFPEOLevel09RuleId | LEVEL_09_RULE_ID | — | — |
| 17 | RuleHierCFPEOLevel10RuleId | LEVEL_10_RULE_ID | — | — |
| 18 | RuleHierCFPEOLevel11RuleId | LEVEL_11_RULE_ID | — | — |
| 19 | RuleHierCFPEOLevel12RuleId | LEVEL_12_RULE_ID | — | — |
| 20 | RuleHierCFPEOLevel13RuleId | LEVEL_13_RULE_ID | — | — |
| 21 | RuleHierCFPEOLevel14RuleId | LEVEL_14_RULE_ID | — | — |
| 22 | RuleHierCFPEOLevel15RuleId | LEVEL_15_RULE_ID | — | — |
| 23 | RuleHierCFPEOObjVersNum | OBJECT_VERSION_NUMBER | — | — |
| 24 | RuleHierCFPEOOrgId | ORG_ID | — | — |
| 25 | RuleHierCFPEORuleHierarchyCfId | RULE_HIERARCHY_CF_ID | — | — |
| 26 | RuleHierCFPEOTopRuleId | TOP_RULE_ID | — | — |

### [[cn_rs_rule_assignments_all|CN_RS_RULE_ASSIGNMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignedObjectId | ASSIGNED_OBJECT_ID | — | — |
| 2 | AssignedObjectType | ASSIGNED_OBJECT_TYPE | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | GroupMemberCreditFlag | GROUP_MEMBER_CREDIT_FLAG | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | OrgId | ORG_ID | — | — |
| 12 | RevenueType | REVENUE_TYPE | — | ✅ |
| 13 | RoleId | ROLE_ID | — | — |
| 14 | RollupFlag | ROLLUP_FLAG | — | ✅ |
| 15 | RuleAssignmentId | RULE_ASSIGNMENT_ID | 🔑 | ✅ |
| 16 | RuleId | RULE_ID | — | — |
| 17 | SplitPct | SPLIT_PCT | — | ✅ |
| 18 | StartDate | START_DATE | — | ✅ |
| 19 | SummaryFlag | SUMMARY_FLAG | — | ✅ |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 4 | CreatedBy1 | CREATED_BY | — | — |
| 5 | CreationDate1 | CREATION_DATE | — | — |
| 6 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | ✅ |
| 7 | EndDate1 | END_DATE | — | — |
| 8 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 9 | HoldReason | HOLD_REASON | — | ✅ |
| 10 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 11 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 12 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 13 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 16 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 17 | OrgId1 | ORG_ID | — | — |
| 18 | ParticipantId | PARTICIPANT_ID | — | ✅ |
| 19 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 20 | PartyId | PARTY_ID | — | ✅ |
| 21 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 22 | RequestId | REQUEST_ID | — | — |
| 23 | SourceSystem | SOURCE_SYSTEM | — | ✅ |
| 24 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 25 | StartDate1 | START_DATE | — | — |

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
