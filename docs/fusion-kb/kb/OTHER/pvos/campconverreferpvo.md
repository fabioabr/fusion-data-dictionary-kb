---
id: DOC-OTHER-PVO-CampConverReferPVO
doc_type: system-doc
title: "CampConverReferPVO — PVO Cross-Module"
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
  - CampConverReferPVO
  - campconverreferpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampConverReferPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Camp Conver Refer. Acessa as tabelas: IRC_CAMPAIGNS_B, IRC_CAMP_CONVERSIONS, IRC_CAMP_GOALS_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampConverReferPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 3 | 3 | 5 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 3 atributos (1 PKs, 2 BICC)
- [[irc_camp_conversions|IRC_CAMP_CONVERSIONS]] — 11 atributos (1 PKs, 2 BICC)
- [[irc_camp_goals_b|IRC_CAMP_GOALS_B]] — 2 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignCode | CAMPAIGN_CODE | — | — |
| 2 | CampaignBPEOPurposeCode | PURPOSE_CODE | — | ✅ |
| 3 | CampaignId | CAMPAIGN_ID | 🔑 | ✅ |

### [[irc_camp_conversions|IRC_CAMP_CONVERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampConversionPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampConversionPEOCreatedBy | CREATED_BY | — | — |
| 3 | CampConversionPEOCreationDate | CREATION_DATE | — | — |
| 4 | CampConversionPEOGoalId | GOAL_ID | — | — |
| 5 | CampConversionPEOGoalTypeCode | GOAL_TYPE_CODE | — | — |
| 6 | CampConversionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CampConversionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CampConversionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CampConversionPEOObjectId | OBJECT_ID | — | — |
| 10 | CampConversionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ConversionId | CONVERSION_ID | 🔑 | ✅ |

### [[irc_camp_goals_b|IRC_CAMP_GOALS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | 🔑 | ✅ |
| 2 | GoalTypeCode | GOAL_TYPE_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
