---
id: DOC-OTHER-PVO-CommentsPVO
doc_type: system-doc
title: "CommentsPVO — PVO Cross-Module"
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
  - CommentsPVO
  - commentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CommentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Comments. Acessa as tabelas: GRC_COMMENT, PER_PERSON_NAMES_F_V, PER_USERS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.CommentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 3 | 1 | 9 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[grc_comment|GRC_COMMENT]] — 15 atributos (1 PKs, 8 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (1 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_comment|GRC_COMMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CommentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CommentsPEODelegated | DELEGATED | — | — |
| 4 | CommentsPEOId | ID | 🔑 | ✅ |
| 5 | CommentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CommentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CommentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CommentsPEONextStateCode | NEXT_STATE_CODE | — | — |
| 9 | CommentsPEOObjectEffectiveSequence | OBJECT_EFFECTIVE_SEQUENCE | — | — |
| 10 | CommentsPEOObjectId | OBJECT_ID | — | — |
| 11 | CommentsPEOObjectStateCode | OBJECT_STATE_CODE | — | ✅ |
| 12 | CommentsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 13 | CommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CommentsPEORevApprvAct | REVIEW_APPROVE_ACTION | — | ✅ |
| 15 | CommentsPEOUserComment | USER_COMMENT | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
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
