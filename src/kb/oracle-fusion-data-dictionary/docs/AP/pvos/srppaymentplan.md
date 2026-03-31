---
id: DOC-AP-PVO-SrpPaymentPlan
doc_type: system-doc
title: "SrpPaymentPlan — PVO Accounts Payable"
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
  - SrpPaymentPlan
  - srppaymentplan
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SrpPaymentPlan

## 📌 Visão Geral

Extrai a vinculação de participantes de vendas aos planos de pagamento de incentivos (ICM), incluindo repositório, participante, datas de vigência e regras do plano. Permite auditar quais representantes estão associados a quais planos de comissão.

**Caminho:** `FscmTopModelAM.PaymentPlanAM.SrpPaymentPlan`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 4 | 1 | 31 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]] — 5 atributos (2 BICC)
- [[cn_srp_participants_all|CN_SRP_PARTICIPANTS_ALL]] — 20 atributos (11 BICC)
- [[cn_srp_payment_plans_all|CN_SRP_PAYMENT_PLANS_ALL]] — 40 atributos (1 PKs, 13 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos (5 BICC)

---

## ⚙️ Atributos

### [[cn_repositories_all_b|CN_REPOSITORIES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunctionalCurrency | FUNCTIONAL_CURRENCY | — | ✅ |
| 2 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 3 | OrgId1 | ORG_ID | — | — |
| 4 | ProcessCurrency | PROCESS_CURRENCY | — | ✅ |
| 5 | RepositoryId | REPOSITORY_ID | — | — |

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
| 20 | StartDate1 | START_DATE | — | — |

### [[cn_srp_payment_plans_all|CN_SRP_PAYMENT_PLANS_ALL]]

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
| 19 | CreditTypeId | CREDIT_TYPE_ID | — | — |
| 20 | DrawPercentAmount | DRAW_PERCENT_AMOUNT | — | ✅ |
| 21 | EndDate | END_DATE | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | LockFlag | LOCK_FLAG | — | ✅ |
| 26 | MaxRecoveryAmt | MAX_RECOVERY_AMT | — | ✅ |
| 27 | MaximumAmt | MAXIMUM_AMT | — | ✅ |
| 28 | MinimumAmt | MINIMUM_AMT | — | ✅ |
| 29 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 30 | OrgId | ORG_ID | — | — |
| 31 | ParticipantId | PARTICIPANT_ID | — | — |
| 32 | PaymentPlanId | PAYMENT_PLAN_ID | — | — |
| 33 | RecPercentAmount | REC_PERCENT_AMOUNT | — | ✅ |
| 34 | RecoveryEndDate | RECOVERY_END_DATE | — | ✅ |
| 35 | RecoveryStartDate | RECOVERY_START_DATE | — | ✅ |
| 36 | RoleId | ROLE_ID | — | — |
| 37 | RolePaymentPlanId | ROLE_PAYMENT_PLAN_ID | — | — |
| 38 | SrpPaymentPlanId | SRP_PAYMENT_PLAN_ID | 🔑 | ✅ |
| 39 | SrpRoleId | SRP_ROLE_ID | — | — |
| 40 | StartDate | START_DATE | — | ✅ |

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

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
