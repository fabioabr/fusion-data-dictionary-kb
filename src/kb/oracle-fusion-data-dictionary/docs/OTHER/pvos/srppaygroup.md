---
id: DOC-OTHER-PVO-SrpPayGroup
doc_type: system-doc
title: "SrpPayGroup — PVO Cross-Module"
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
  - SrpPayGroup
  - srppaygroup
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpPayGroup

## 📌 Visão Geral

View Object para extração BICC de dados de Srp Pay Group. Acessa as tabelas: CN_PARTICIPANT_ROLES, CN_PAY_GROUPS_ALL_B, CN_PAY_GROUPS_ALL_TL (+3).

**Caminho:** `FscmTopModelAM.PayGroupAM.SrpPayGroup`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 6 | 1 | 29 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[cn_participant_roles|CN_PARTICIPANT_ROLES]] — 5 atributos (2 BICC)
- [[cn_pay_groups_all_b|CN_PAY_GROUPS_ALL_B]] — 5 atributos (1 BICC)
- [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]] — 7 atributos (3 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 20 atributos (11 BICC)
- [[cn_srp_pay_groups_all|CN_SRP_PAY_GROUPS_ALL]] — 15 atributos (1 PKs, 7 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_participant_roles|CN_PARTICIPANT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 2 | ParticipantId | PARTICIPANT_ID | — | — |
| 3 | ParticipantRoleId | PARTICIPANT_ROLE_ID | — | — |
| 4 | RoleId | ROLE_ID | — | — |
| 5 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[cn_pay_groups_all_b|CN_PAY_GROUPS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 2 | OrgId1 | ORG_ID | — | — |
| 3 | PayGroupId1 | PAY_GROUP_ID | — | — |
| 4 | PayGroupType | PAY_GROUP_TYPE | — | ✅ |
| 5 | StartDate1 | START_DATE | — | — |

### [[cn_pay_groups_all_tl|CN_PAY_GROUPS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 4 | OrgId2 | ORG_ID | — | — |
| 5 | PayGroupId2 | PAY_GROUP_ID | — | — |
| 6 | PayGroupName | PAY_GROUP_NAME | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

### [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AnalystId | ANALYST_ID | — | ✅ |
| 3 | CompensationEndDate | COMPENSATION_END_DATE | — | ✅ |
| 4 | DisplayIdentifier | DISPLAY_IDENTIFIER | — | — |
| 5 | EndDate1 | END_DATE | — | — |
| 6 | HoldPaymentFlag | HOLD_PAYMENT_FLAG | — | ✅ |
| 7 | HoldReason | HOLD_REASON | — | ✅ |
| 8 | HrPersonNumber | HR_PERSON_NUMBER | — | ✅ |
| 9 | HrPrimaryWorkerNumber | HR_PRIMARY_WORKER_NUMBER | — | ✅ |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 14 | ParticipantType | PARTICIPANT_TYPE | — | ✅ |
| 15 | PartyId | PARTY_ID | — | ✅ |
| 16 | PayeeOnly | PAYEE_ONLY | — | ✅ |
| 17 | RequestId | REQUEST_ID | — | — |
| 18 | SourceSystem | SOURCE_SYSTEM | — | — |
| 19 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 20 | StartDate2 | START_DATE | — | — |

### [[cn_srp_pay_groups_all|CN_SRP_PAY_GROUPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EndDate | END_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | LockFlag | LOCK_FLAG | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrgId | ORG_ID | — | — |
| 10 | PayGroupId | PAY_GROUP_ID | — | ✅ |
| 11 | RolePayGroupId | ROLE_PAY_GROUP_ID | — | — |
| 12 | SalesrepId | SALESREP_ID | — | — |
| 13 | SrpPayGroupId | SRP_PAY_GROUP_ID | 🔑 | ✅ |
| 14 | SrpRoleId | SRP_ROLE_ID | — | — |
| 15 | StartDate | START_DATE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartcipantPartyPEOPartyId | PARTY_ID | — | — |
| 2 | ParticipantFirstName | PERSON_FIRST_NAME | — | ✅ |
| 3 | ParticipantLastName | PERSON_LAST_NAME | — | ✅ |
| 4 | ParticipantName | PARTY_NAME | — | ✅ |
| 5 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 6 | UserGuid | USER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
