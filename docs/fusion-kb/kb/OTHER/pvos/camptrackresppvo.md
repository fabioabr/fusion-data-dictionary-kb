---
id: DOC-OTHER-PVO-CampTrackRespPVO
doc_type: system-doc
title: "CampTrackRespPVO — PVO Cross-Module"
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
  - CampTrackRespPVO
  - camptrackresppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampTrackRespPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Camp Track Resp. Acessa as tabelas: IRC_CAMPAIGNS_B, IRC_CAMP_GOALS_B, IRC_CAMP_GOAL_RESP_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampTrackRespPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 4 | 4 | 5 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 2 atributos (1 PKs, 1 BICC)
- [[irc_camp_goals_b|IRC_CAMP_GOALS_B]] — 2 atributos (1 PKs, 1 BICC)
- [[irc_camp_goal_resp_b|IRC_CAMP_GOAL_RESP_B]] — 1 atributos (1 PKs, 1 BICC)
- [[irc_camp_track_response|IRC_CAMP_TRACK_RESPONSE]] — 11 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOPurposeCode | PURPOSE_CODE | — | — |
| 2 | CampaignId | CAMPAIGN_ID | 🔑 | ✅ |

### [[irc_camp_goals_b|IRC_CAMP_GOALS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampGoalBPEOGoalTypeCode | GOAL_TYPE_CODE | — | — |
| 2 | GoalId | GOAL_ID | 🔑 | ✅ |

### [[irc_camp_goal_resp_b|IRC_CAMP_GOAL_RESP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalResponseId | GOAL_RESPONSE_ID | 🔑 | ✅ |

### [[irc_camp_track_response|IRC_CAMP_TRACK_RESPONSE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampTrackRespPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampTrackRespPEOCreatedBy | CREATED_BY | — | — |
| 3 | CampTrackRespPEOCreationDate | CREATION_DATE | — | — |
| 4 | CampTrackRespPEOGoalId | GOAL_ID | — | — |
| 5 | CampTrackRespPEOGoalResponseId | GOAL_RESPONSE_ID | — | — |
| 6 | CampTrackRespPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CampTrackRespPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CampTrackRespPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CampTrackRespPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CampTrackRespPEOPersonId | PERSON_ID | — | — |
| 11 | TrackResponseId | TRACK_RESPONSE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
