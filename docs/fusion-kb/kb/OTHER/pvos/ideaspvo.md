---
id: DOC-OTHER-PVO-IdeasPVO
doc_type: system-doc
title: "IdeasPVO — PVO Cross-Module"
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
  - IdeasPVO
  - ideaspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IdeasPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ideas. Acessa as tabelas: ACN_IDEA_B, ACN_IDEA_COMMENTS_V, ACN_IDEA_TAG (+3).

**Caminho:** `FscmTopModelAM.IdeasAnalyticsAM.IdeasPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 6 | 1 | 55 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[acn_idea_b|ACN_IDEA_B]] — 11 atributos (1 PKs, 10 BICC)
- [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]] — 3 atributos (3 BICC)
- [[acn_idea_tag|ACN_IDEA_TAG]] — 8 atributos (8 BICC)
- [[acn_idea_tl|ACN_IDEA_TL]] — 11 atributos (10 BICC)
- [[acn_idea_vote_summary_v|ACN_IDEA_VOTE_SUMMARY_V]] — 4 atributos (4 BICC)
- [[per_users|PER_USERS]] — 21 atributos (20 BICC)

---

## ⚙️ Atributos

### [[acn_idea_b|ACN_IDEA_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | IdeaBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | IdeaBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | IdeaBaseIdeaId | IDEA_ID | 🔑 | ✅ |
| 5 | IdeaBaseIdeaNumber | IDEA_NUMBER | — | — |
| 6 | IdeaBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | IdeaBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | IdeaBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | IdeaBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | IdeaBaseStatus | STATUS | — | ✅ |
| 11 | IdeaBaseType | TYPE | — | ✅ |

### [[acn_idea_comments_v|ACN_IDEA_COMMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaCommentCommentLastUpdateDate | COMMENT_LAST_UPDATE_DATE | — | ✅ |
| 2 | IdeaCommentIdeaComment | IDEA_COMMENT | — | ✅ |
| 3 | IdeaCommentIdeaId | IDEA_ID | — | ✅ |

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

### [[acn_idea_tl|ACN_IDEA_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IdeaTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | IdeaTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | IdeaTranslationDescription | DESCRIPTION | — | — |
| 4 | IdeaTranslationIdeaId | IDEA_ID | — | ✅ |
| 5 | IdeaTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | IdeaTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | IdeaTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | IdeaTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | IdeaTranslationName | NAME | — | ✅ |
| 10 | IdeaTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | IdeaTranslationSourceLang | SOURCE_LANG | — | ✅ |

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
| 19 | UserUserGuid | USER_GUID | — | ✅ |
| 20 | UserUserId | USER_ID | — | ✅ |
| 21 | UserUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
