---
id: DOC-OTHER-PVO-CampAudiencePVO
doc_type: system-doc
title: "CampAudiencePVO — PVO Cross-Module"
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
  - CampAudiencePVO
  - campaudiencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampAudiencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Camp Audience. Acessa as tabelas: IRC_CAMPAIGNS_B, IRC_CAMP_AUDIENCE.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampAudiencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 2 | 2 | 6 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 2 atributos (1 PKs, 1 BICC)
- [[irc_camp_audience|IRC_CAMP_AUDIENCE]] — 12 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |
| 2 | CampaignId | CAMPAIGN_ID | 🔑 | ✅ |

### [[irc_camp_audience|IRC_CAMP_AUDIENCE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AudienceId | AUDIENCE_ID | 🔑 | ✅ |
| 2 | CampAudiencePEOAudienceTypeCode | AUDIENCE_TYPE_CODE | — | ✅ |
| 3 | CampAudiencePEOCampaignId | CAMPAIGN_ID | — | — |
| 4 | CampAudiencePEOCreatedBy | CREATED_BY | — | — |
| 5 | CampAudiencePEOCreationDate | CREATION_DATE | — | — |
| 6 | CampAudiencePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CampAudiencePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CampAudiencePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CampAudiencePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CampAudiencePEOPersonId | PERSON_ID | — | ✅ |
| 11 | CampAudiencePEOUnsubscribedFlag | UNSUBSCRIBED_FLAG | — | ✅ |
| 12 | CampAudiencePEOUnsubscribedTokenId | UNSUBSCRIBED_TOKEN_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
