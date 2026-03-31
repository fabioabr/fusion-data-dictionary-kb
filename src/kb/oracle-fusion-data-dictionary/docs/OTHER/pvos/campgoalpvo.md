---
id: DOC-OTHER-PVO-CampGoalPVO
doc_type: system-doc
title: "CampGoalPVO — PVO Cross-Module"
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
  - CampGoalPVO
  - campgoalpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampGoalPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Camp Goal. Acessa as tabelas: IRC_CAMPAIGNS_B, IRC_CAMP_GOALS_B, IRC_CAMP_GOALS_TL (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampGoalPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 5 | 1 | 14 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 2 atributos
- [[irc_camp_goals_b|IRC_CAMP_GOALS_B]] — 11 atributos (1 PKs, 5 BICC)
- [[irc_camp_goals_tl|IRC_CAMP_GOALS_TL]] — 10 atributos (2 BICC)
- [[irc_camp_goal_resp_b|IRC_CAMP_GOAL_RESP_B]] — 11 atributos (5 BICC)
- [[irc_camp_goal_resp_tl|IRC_CAMP_GOAL_RESP_TL]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |

### [[irc_camp_goals_b|IRC_CAMP_GOALS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampGoalBPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampGoalBPEOCreatedBy | CREATED_BY | — | — |
| 3 | CampGoalBPEOCreationDate | CREATION_DATE | — | — |
| 4 | CampGoalBPEOGoalTypeCode | GOAL_TYPE_CODE | — | ✅ |
| 5 | CampGoalBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CampGoalBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CampGoalBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CampGoalBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | CampGoalBPEOPrimaryGoalFlag | PRIMARY_GOAL_FLAG | — | ✅ |
| 10 | CampGoalBPEOSystemGoalFlag | SYSTEM_GOAL_FLAG | — | ✅ |
| 11 | GoalId | GOAL_ID | 🔑 | ✅ |

### [[irc_camp_goals_tl|IRC_CAMP_GOALS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampGoalTranslationPEOCreatedBy3 | CREATED_BY | — | — |
| 2 | CampGoalTranslationPEOCreationDate3 | CREATION_DATE | — | — |
| 3 | CampGoalTranslationPEOGoalId2 | GOAL_ID | — | — |
| 4 | CampGoalTranslationPEOGoalName | GOAL_NAME | — | ✅ |
| 5 | CampGoalTranslationPEOLanguage1 | LANGUAGE | — | — |
| 6 | CampGoalTranslationPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 7 | CampGoalTranslationPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 8 | CampGoalTranslationPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 9 | CampGoalTranslationPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 10 | CampGoalTranslationPEOSourceLang1 | SOURCE_LANG | — | — |

### [[irc_camp_goal_resp_b|IRC_CAMP_GOAL_RESP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampGoalRespBPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | CampGoalRespBPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | CampGoalRespBPEODestinationUrl | DESTINATION_URL | — | ✅ |
| 4 | CampGoalRespBPEOGoalId | GOAL_ID | — | — |
| 5 | CampGoalRespBPEOGoalResponseId | GOAL_RESPONSE_ID | — | ✅ |
| 6 | CampGoalRespBPEOIncludeInTargetFlag | INCLUDE_IN_TARGET_FLAG | — | ✅ |
| 7 | CampGoalRespBPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | CampGoalRespBPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | CampGoalRespBPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | CampGoalRespBPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | CampGoalRespBPEOUseDefaultUrlFlag | USE_DEFAULT_URL_FLAG | — | ✅ |

### [[irc_camp_goal_resp_tl|IRC_CAMP_GOAL_RESP_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampGoalRespTranslationPEOCreatedBy2 | CREATED_BY | — | — |
| 2 | CampGoalRespTranslationPEOCreationDate2 | CREATION_DATE | — | — |
| 3 | CampGoalRespTranslationPEOGoalResponseId1 | GOAL_RESPONSE_ID | — | — |
| 4 | CampGoalRespTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | CampGoalRespTranslationPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 6 | CampGoalRespTranslationPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 7 | CampGoalRespTranslationPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 8 | CampGoalRespTranslationPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 9 | CampGoalRespTranslationPEOResponseLabel | RESPONSE_LABEL | — | ✅ |
| 10 | CampGoalRespTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
