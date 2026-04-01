---
id: DOC-OTHER-PVO-ACNCommentsPVO
doc_type: system-doc
title: "ACNCommentsPVO — PVO Cross-Module"
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
  - ACNCommentsPVO
  - acncommentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCommentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNComments. Acessa as tabelas: GRC_COMMENT, PER_PERSON_NAMES_F_V, PER_USERS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCommentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 3 | 1 | 8 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[grc_comment|GRC_COMMENT]] — 13 atributos (1 PKs, 6 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_comment|GRC_COMMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCommentPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ACNCommentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ACNCommentPEODelegated | DELEGATED | — | — |
| 4 | ACNCommentPEOId | ID | — | — |
| 5 | ACNCommentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ACNCommentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ACNCommentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ACNCommentPEOObjectEffectiveSequence | OBJECT_EFFECTIVE_SEQUENCE | — | — |
| 9 | ACNCommentPEOObjectId | OBJECT_ID | 🔑 | ✅ |
| 10 | ACNCommentPEOObjectStateCode | OBJECT_STATE_CODE | — | — |
| 11 | ACNCommentPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 12 | ACNCommentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ACNCommentPEOUserComment | USER_COMMENT | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CreatedByPersonId | PERSON_ID | — | — |
| 3 | CreatedByUserGuid | USER_GUID | — | — |
| 4 | CreatedByUserId | USER_ID | — | — |
| 5 | CreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
