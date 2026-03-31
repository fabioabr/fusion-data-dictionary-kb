---
id: DOC-OTHER-PVO-IdeaCustomerAssignmentPVO
doc_type: system-doc
title: "IdeaCustomerAssignmentPVO — PVO Cross-Module"
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
  - IdeaCustomerAssignmentPVO
  - ideacustomerassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IdeaCustomerAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Idea Customer Assignment. Acessa as tabelas: ACN_IDEA_COMMENTS_V, ACN_IDEA_CUSTOMER_ASSIGN, ACN_IDEA_TAG (+3).

**Caminho:** `FscmTopModelAM.IdeasAnalyticsAM.IdeaCustomerAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 6 | 1 | 56 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]] — 3 atributos (3 BICC)
- [[acn_idea_customer_assign|ACN_IDEA_CUSTOMER_ASSIGN]] — 9 atributos (9 BICC)
- [[acn_idea_tag|ACN_IDEA_TAG]] — 8 atributos (8 BICC)
- [[acn_idea_vl|ACN_IDEA_VL]] — 13 atributos (1 PKs, 11 BICC)
- [[acn_idea_vote_summary_v|ACN_IDEA_VOTE_SUMMARY_V]] — 4 atributos (4 BICC)
- [[per_users|PER_USERS]] — 22 atributos (21 BICC)

---

## ⚙️ Atributos

### [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaCommentCommentLastUpdateDate | COMMENT_LAST_UPDATE_DATE | — | ✅ |
| 2 | IdeaCommentIdeaComment | IDEA_COMMENT | — | ✅ |
| 3 | IdeaCommentIdeaId | IDEA_ID | — | ✅ |

### [[acn_idea_customer_assign|ACN_IDEA_CUSTOMER_ASSIGN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaCustomerAssignmentCreatedBy | CREATED_BY | — | ✅ |
| 2 | IdeaCustomerAssignmentCreationDate | CREATION_DATE | — | ✅ |
| 3 | IdeaCustomerAssignmentCustomerId | CUSTOMER_ID | — | ✅ |
| 4 | IdeaCustomerAssignmentIdeaCustomerAssignId | IDEA_CUSTOMER_ASSIGN_ID | — | ✅ |
| 5 | IdeaCustomerAssignmentIdeaId | IDEA_ID | — | ✅ |
| 6 | IdeaCustomerAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | IdeaCustomerAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | IdeaCustomerAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | IdeaCustomerAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[acn_idea_tag|ACN_IDEA_TAG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaTagCreatedBy | CREATED_BY | — | ✅ |
| 2 | IdeaTagCreationDate | CREATION_DATE | — | ✅ |
| 3 | IdeaTagIdeaId | IDEA_ID | — | ✅ |
| 4 | IdeaTagLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | IdeaTagLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | IdeaTagLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | IdeaTagName | NAME | — | ✅ |
| 8 | IdeaTagTagId | TAG_ID | — | ✅ |

### [[acn_idea_vl|ACN_IDEA_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | IdeaCreatedBy | CREATED_BY | — | ✅ |
| 3 | IdeaCreationDate | CREATION_DATE | — | ✅ |
| 4 | IdeaDescription | DESCRIPTION | — | — |
| 5 | IdeaIdeaId | IDEA_ID | 🔑 | ✅ |
| 6 | IdeaIdeaNumber | IDEA_NUMBER | — | — |
| 7 | IdeaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | IdeaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | IdeaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | IdeaName | NAME | — | ✅ |
| 11 | IdeaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | IdeaStatus | STATUS | — | ✅ |
| 13 | IdeaType | TYPE | — | ✅ |

### [[acn_idea_vote_summary_v|ACN_IDEA_VOTE_SUMMARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaVoteIdeaId | IDEA_ID | — | ✅ |
| 2 | IdeaVoteNoCount | NO_COUNT | — | ✅ |
| 3 | IdeaVoteVoteLastUpdateDate | VOTE_LAST_UPDATE_DATE | — | ✅ |
| 4 | IdeaVoteYesCount | YES_COUNT | — | ✅ |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | UserBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | UserCreatedBy | CREATED_BY | — | ✅ |
| 4 | UserCreationDate | CREATION_DATE | — | ✅ |
| 5 | UserCredentialsEmailSent | CREDENTIALS_EMAIL_SENT | — | ✅ |
| 6 | UserEndDate | END_DATE | — | ✅ |
| 7 | UserExternalId | EXTERNAL_ID | — | — |
| 8 | UserHrTerminated | HR_TERMINATED | — | ✅ |
| 9 | UserLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | UserLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | UserLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | UserMultitenancyUsername | MULTITENANCY_USERNAME | — | ✅ |
| 13 | UserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | UserPartyId | PARTY_ID | — | ✅ |
| 15 | UserPersonId | PERSON_ID | — | ✅ |
| 16 | UserStartDate | START_DATE | — | ✅ |
| 17 | UserSuspended | SUSPENDED | — | ✅ |
| 18 | UserUserDataChecksum | USER_DATA_CHECKSUM | — | ✅ |
| 19 | UserUserDistinguishedName | USER_DISTINGUISHED_NAME | — | ✅ |
| 20 | UserUserGuid | USER_GUID | — | ✅ |
| 21 | UserUserId | USER_ID | — | ✅ |
| 22 | UserUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
