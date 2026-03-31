---
id: DOC-HCM-PVO-CampAssetPVO
doc_type: system-doc
title: "CampAssetPVO — PVO Human Capital Management"
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
  - CampAssetPVO
  - campassetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampAssetPVO

## 📌 Visão Geral

Disponibiliza ativos (assets) de campanhas de recrutamento como e-mails e landing pages. Suporta gestao de materiais de comunicacao de campanhas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampAssetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 3 | 1 | 10 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 2 atributos
- [[irc_camp_assets_b|IRC_CAMP_ASSETS_B]] — 14 atributos (1 PKs, 7 BICC)
- [[irc_camp_assets_tl|IRC_CAMP_ASSETS_TL]] — 13 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |
| 2 | CampaignId | CAMPAIGN_ID | — | — |

### [[irc_camp_assets_b|IRC_CAMP_ASSETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampAssetBPEOAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | CampAssetBPEOAssetStatusCode | ASSET_STATUS_CODE | — | ✅ |
| 3 | CampAssetBPEOAssetTypeCode | ASSET_TYPE_CODE | — | ✅ |
| 4 | CampAssetBPEOAudienceDerivedFlag | AUDIENCE_DERIVED_FLAG | — | ✅ |
| 5 | CampAssetBPEOCampaignId | CAMPAIGN_ID | — | — |
| 6 | CampAssetBPEOCreatedBy | CREATED_BY | — | — |
| 7 | CampAssetBPEOCreationDate | CREATION_DATE | — | — |
| 8 | CampAssetBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CampAssetBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | CampAssetBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | CampAssetBPEOMessageDesignId | MESSAGE_DESIGN_ID | — | — |
| 12 | CampAssetBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CampAssetBPEOParentAssetId | PARENT_ASSET_ID | — | ✅ |
| 14 | CampAssetBPEOScheduledDate | SCHEDULED_DATE | — | ✅ |

### [[irc_camp_assets_tl|IRC_CAMP_ASSETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | — |
| 2 | CampAssetParentTranslationPEOAssetName | ASSET_NAME | — | ✅ |
| 3 | CampAssetTranslationPEOAssetId | ASSET_ID | — | — |
| 4 | CampAssetTranslationPEOAssetName | ASSET_NAME | — | ✅ |
| 5 | CampAssetTranslationPEOCreatedBy | CREATED_BY | — | — |
| 6 | CampAssetTranslationPEOCreationDate | CREATION_DATE | — | — |
| 7 | CampAssetTranslationPEOLanguage | LANGUAGE | — | — |
| 8 | CampAssetTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CampAssetTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | CampAssetTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | CampAssetTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CampAssetTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | Language | LANGUAGE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
