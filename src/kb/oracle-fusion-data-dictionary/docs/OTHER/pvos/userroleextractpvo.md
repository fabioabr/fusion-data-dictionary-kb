---
id: DOC-OTHER-PVO-UserRoleExtractPVO
doc_type: system-doc
title: "UserRoleExtractPVO — PVO Cross-Module"
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
  - UserRoleExtractPVO
  - userroleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserRoleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Role Extract. Acessa as tabelas: PER_USER_ROLES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.UserBiccExtractAM.UserRoleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_user_roles|PER_USER_ROLES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[per_user_roles|PER_USER_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MethodCode | METHOD_CODE | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RoleGuid | ROLE_GUID | — | ✅ |
| 12 | RoleId | ROLE_ID | — | ✅ |
| 13 | StartDate | START_DATE | — | ✅ |
| 14 | TerminatedFlag | TERMINATED_FLAG | — | ✅ |
| 15 | UserId | USER_ID | — | ✅ |
| 16 | UserRoleId | USER_ROLE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
