---
id: DOC-OTHER-PVO-UserPVO
doc_type: system-doc
title: "UserPVO — PVO Cross-Module"
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
  - UserPVO
  - userpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User. Acessa as tabelas: PER_USERS, PER_USER_HISTORY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.UserAM.UserPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 16 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[per_users|PER_USERS]] — 17 atributos (7 BICC)
- [[per_user_history|PER_USER_HISTORY]] — 13 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | UserPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | UserPEOCreatedBy | CREATED_BY | — | — |
| 4 | UserPEOCreationDate | CREATION_DATE | — | — |
| 5 | UserPEOEndDate | END_DATE | — | — |
| 6 | UserPEOHrTerminated | HR_TERMINATED | — | — |
| 7 | UserPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | UserPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | UserPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | UserPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | UserPEOPartyId | PARTY_ID | — | ✅ |
| 12 | UserPEOPersonId | PERSON_ID | — | ✅ |
| 13 | UserPEOStartDate | START_DATE | — | — |
| 14 | UserPEOSuspended | SUSPENDED | — | — |
| 15 | UserPEOUserGuid | USER_GUID | — | ✅ |
| 16 | UserPEOUserId | USER_ID | — | ✅ |
| 17 | UserPEOUsername | USERNAME | — | ✅ |

### [[per_user_history|PER_USER_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserHistoryPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | UserHistoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | UserHistoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | UserHistoryPEOEndDate | END_DATE | — | ✅ |
| 5 | UserHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | UserHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | UserHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | UserHistoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | UserHistoryPEOStartDate | START_DATE | — | ✅ |
| 10 | UserHistoryPEOUserGuid | USER_GUID | — | ✅ |
| 11 | UserHistoryPEOUserHistoryId | USER_HISTORY_ID | 🔑 | ✅ |
| 12 | UserHistoryPEOUserId | USER_ID | — | — |
| 13 | UserHistoryPEOUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
