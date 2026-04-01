---
id: DOC-OTHER-PVO-ContractStatusHistoryP
doc_type: system-doc
title: "ContractStatusHistoryP — PVO Cross-Module"
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
  - ContractStatusHistoryP
  - contractstatushistoryp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractStatusHistoryP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Status History P. Acessa as tabelas: HR_ALL_ORGANIZATION_UNITS_F_VL, HZ_PARTIES, OKC_K_STATUS_HISTORY_VL (+1).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractStatusHistoryP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 4 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 5 atributos (5 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (2 BICC)
- [[okc_k_status_history_vl|OKC_K_STATUS_HISTORY_VL]] — 15 atributos (1 PKs, 15 BICC)
- [[okc_user_statuses_vl|OKC_USER_STATUSES_VL]] — 8 atributos (8 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 4 | OrganizationUnitName | NAME | — | ✅ |
| 5 | OrganizationUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | ✅ |
| 2 | PartyName | PARTY_NAME | — | ✅ |

### [[okc_k_status_history_vl|OKC_K_STATUS_HISTORY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssigneeId | ASSIGNEE_ID | — | ✅ |
| 2 | AssigneeType | ASSIGNEE_TYPE | — | ✅ |
| 3 | Comments | COMMENTS | — | ✅ |
| 4 | ContractId | CONTRACT_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | HistoryCreationDate | HISTORY_CREATION_DATE | — | ✅ |
| 8 | Id | ID | 🔑 | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MajorVersion | MAJOR_VERSION | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | StsCode | STS_CODE | — | ✅ |
| 15 | UserStatusCode | USER_STATUS_CODE | — | ✅ |

### [[okc_user_statuses_vl|OKC_USER_STATUSES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserStatusPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | UserStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | UserStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | UserStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | UserStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | UserStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | UserStatusPEOStatusMeaning | STATUS_MEANING | — | ✅ |
| 8 | UserStatusPEOUserStatusCode | USER_STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
