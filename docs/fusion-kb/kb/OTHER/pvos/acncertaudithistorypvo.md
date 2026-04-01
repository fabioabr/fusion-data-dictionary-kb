---
id: DOC-OTHER-PVO-ACNCertAuditHistoryPVO
doc_type: system-doc
title: "ACNCertAuditHistoryPVO — PVO Cross-Module"
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
  - ACNCertAuditHistoryPVO
  - acncertaudithistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCertAuditHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNCert Audit History. Acessa as tabelas: GRC_ACN_CERT_ROLE_USER, GRC_ACN_CERT_ROLE_USER_HIST, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCertAuditHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 4 | 1 | 5 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_cert_role_user|GRC_ACN_CERT_ROLE_USER]] — 1 atributos
- [[grc_acn_cert_role_user_hist|GRC_ACN_CERT_ROLE_USER_HIST]] — 9 atributos (1 PKs, 4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (1 BICC)
- [[per_users|PER_USERS]] — 5 atributos

---

## ⚙️ Atributos

### [[grc_acn_cert_role_user|GRC_ACN_CERT_ROLE_USER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertRoleUserPEOCertUsrRoleId | CERT_USER_ROLE_ID | — | — |

### [[grc_acn_cert_role_user_hist|GRC_ACN_CERT_ROLE_USER_HIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertRoleUserHistPEOCertUsrRleId | CERT_USER_ROLE_ID | — | — |
| 2 | ACNCertRoleUserHistPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ACNCertRoleUserHistPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ACNCertRoleUserHistPEOEventCode | EVENT_CODE | — | ✅ |
| 5 | ACNCertRoleUserHistPEOHistoryId | HISTORY_ID | 🔑 | ✅ |
| 6 | ACNCertRoleUserHistPEOLastUpdateDt | LAST_UPDATE_DATE | — | — |
| 7 | ACNCertRoleUserHistPEOLastUpdateLgn | LAST_UPDATE_LOGIN | — | — |
| 8 | ACNCertRoleUserHistPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ACNCertRoleUserHistPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AudHistPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | AudHistPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AudHistPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | AudHistPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | AudHistPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AudHistCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | AudHistCreatedByPersonId | PERSON_ID | — | — |
| 3 | AudHistCreatedByUserGuid | USER_GUID | — | — |
| 4 | AudHistCreatedByUserId | USER_ID | — | — |
| 5 | AudHistCreatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
