---
id: DOC-HCM-PVO-UserExtractPVO
doc_type: system-doc
title: "UserExtractPVO — PVO Human Capital Management"
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
  - UserExtractPVO
  - userextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserExtractPVO

## 📌 Visão Geral

Extrai dados de usuários do HCM para carga BICC, com status e grupo de negócio. Suporta extração analítica de contas de acesso ao sistema.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.UserBiccExtractAM.UserExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_users|PER_USERS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | CredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | ✅ |
| 6 | EndDate | END_DATE | — | ✅ |
| 7 | ExternalId | EXTERNAL_ID | — | ✅ |
| 8 | HrTerminated | HR_TERMINATED | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MultitenancyUsername | MULTITENANCY_USERNAME | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PartyId | PARTY_ID | — | ✅ |
| 15 | PersonId | PERSON_ID | — | ✅ |
| 16 | StartDate | START_DATE | — | ✅ |
| 17 | Suspended | SUSPENDED | — | ✅ |
| 18 | UserDataChecksum | USER_DATA_CHECKSUM | — | ✅ |
| 19 | UserDistinguishedName | USER_DISTINGUISHED_NAME | — | ✅ |
| 20 | UserGuid | USER_GUID | — | ✅ |
| 21 | UserId | USER_ID | 🔑 | ✅ |
| 22 | Username | USERNAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
