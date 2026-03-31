---
id: DOC-HCM-PVO-ContractPVO
doc_type: system-doc
title: "ContractPVO — PVO Human Capital Management"
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
  - ContractPVO
  - contractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractPVO

## 📌 Visão Geral

Extrai contratos de trabalho com acoes, traducoes e vigencia. Suporta gestao contratual e conformidade trabalhista de colaboradores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.ContractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 3 | 2 | 35 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[per_actions_b|PER_ACTIONS_B]] — 3 atributos (1 BICC)
- [[per_actions_tl|PER_ACTIONS_TL]] — 3 atributos (1 BICC)
- [[per_contracts_f|PER_CONTRACTS_F]] — 34 atributos (2 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[per_actions_b|PER_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsPEOActionCode | ACTION_CODE | — | ✅ |
| 2 | ActionsPEOActionId | ACTION_ID | — | — |
| 3 | ActionsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |

### [[per_actions_tl|PER_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ActionTranslationPEOActionName | ACTION_NAME | — | ✅ |
| 3 | ActionTranslationPEOLanguage | LANGUAGE | — | — |

### [[per_contracts_f|PER_CONTRACTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractId | CONTRACT_ID | 🔑 | ✅ |
| 2 | ContractPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | ContractPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | ContractPEOContractEndDate | CONTRACT_END_DATE | — | ✅ |
| 5 | ContractPEOContractNumber | CONTRACT_NUMBER | — | ✅ |
| 6 | ContractPEOContractualJobTitle | CONTRACTUAL_JOB_TITLE | — | ✅ |
| 7 | ContractPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ContractPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ContractPEODescription | DESCRIPTION | — | ✅ |
| 10 | ContractPEODocStatus | DOC_STATUS | — | ✅ |
| 11 | ContractPEODocStatusChangeDate | DOC_STATUS_CHANGE_DATE | — | ✅ |
| 12 | ContractPEODuration | DURATION | — | ✅ |
| 13 | ContractPEODurationUnits | DURATION_UNITS | — | ✅ |
| 14 | ContractPEOEndReason | END_REASON | — | ✅ |
| 15 | ContractPEOExtensionPeriod | EXTENSION_PERIOD | — | ✅ |
| 16 | ContractPEOExtensionPeriodUnits | EXTENSION_PERIOD_UNITS | — | ✅ |
| 17 | ContractPEOExtensionReason | EXTENSION_REASON | — | ✅ |
| 18 | ContractPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ContractPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | ContractPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ContractPEOLegislationCode | LEGISLATION_CODE | — | — |
| 22 | ContractPEONumberOfExtensions | NUMBER_OF_EXTENSIONS | — | ✅ |
| 23 | ContractPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | ContractPEOParties | PARTIES | — | ✅ |
| 25 | ContractPEOPeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | ✅ |
| 26 | ContractPEOPersonId | PERSON_ID | — | ✅ |
| 27 | ContractPEOReference | REFERENCE | — | ✅ |
| 28 | ContractPEOStartReason | START_REASON | — | ✅ |
| 29 | ContractPEOStatus | STATUS | — | ✅ |
| 30 | ContractPEOStatusReason | STATUS_REASON | — | ✅ |
| 31 | ContractPEOType | TYPE | — | ✅ |
| 32 | ContractPEOWorkTermsType | WORK_TERMS_TYPE | — | ✅ |
| 33 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 34 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
