---
id: DOC-HCM-PVO-CampaignPVO
doc_type: system-doc
title: "CampaignPVO — PVO Human Capital Management"
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
  - CampaignPVO
  - campaignpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampaignPVO

## 📌 Visão Geral

Extrai campanhas de recrutamento com codigo, status, data de ativacao e tipo de audiencia. Base para gestao e analise de campanhas de atracao de talentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampaignPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 16 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 20 atributos (1 PKs, 14 BICC)
- [[irc_campaigns_tl|IRC_CAMPAIGNS_TL]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOActivatedOnDate | ACTIVATED_ON_DATE | — | ✅ |
| 2 | CampaignBPEOAudiencePopulatedFlag | AUDIENCE_POPULATED_FLAG | — | ✅ |
| 3 | CampaignBPEOAudienceSavedSearchId | AUDIENCE_SAVED_SEARCH_ID | — | — |
| 4 | CampaignBPEOCampaignCode | CAMPAIGN_CODE | — | ✅ |
| 5 | CampaignBPEOCampaignLanguageCode | CAMPAIGN_LANGUAGE_CODE | — | — |
| 6 | CampaignBPEOCampaignStatusCode | CAMPAIGN_STATUS_CODE | — | ✅ |
| 7 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |
| 8 | CampaignBPEOCancelledOnDate | CANCELLED_ON_DATE | — | ✅ |
| 9 | CampaignBPEOClosedOnDate | CLOSED_ON_DATE | — | ✅ |
| 10 | CampaignBPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CampaignBPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CampaignBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CampaignBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | CampaignBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CampaignBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | CampaignBPEOPurposeCode | PURPOSE_CODE | — | ✅ |
| 17 | CampaignBPEOReqSavedSearchId | REQ_SAVED_SEARCH_ID | — | — |
| 18 | CampaignBPEOSearchRequisitionsFlag | SEARCH_REQUISITIONS_FLAG | — | ✅ |
| 19 | CampaignBPEOTargetGoalValue | TARGET_GOAL_VALUE | — | ✅ |
| 20 | CampaignId | CAMPAIGN_ID | 🔑 | ✅ |

### [[irc_campaigns_tl|IRC_CAMPAIGNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignTranslationPEOCampaignDescription | CAMPAIGN_DESCRIPTION | — | — |
| 2 | CampaignTranslationPEOCampaignId1 | CAMPAIGN_ID | — | — |
| 3 | CampaignTranslationPEOCampaignName | CAMPAIGN_NAME | — | ✅ |
| 4 | CampaignTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 5 | CampaignTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 6 | CampaignTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | CampaignTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | CampaignTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | CampaignTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | CampaignTranslationPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | CampaignTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
