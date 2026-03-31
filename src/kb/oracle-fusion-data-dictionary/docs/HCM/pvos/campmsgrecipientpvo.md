---
id: DOC-HCM-PVO-CampMsgRecipientPVO
doc_type: system-doc
title: "CampMsgRecipientPVO — PVO Human Capital Management"
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
  - CampMsgRecipientPVO
  - campmsgrecipientpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampMsgRecipientPVO

## 📌 Visão Geral

Extrai destinatarios de mensagens de campanhas com status de envio. Permite rastreamento de comunicacoes e engajamento em campanhas de recrutamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampMsgRecipientPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 4 | 1 | 4 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 2 atributos
- [[irc_camp_assets_b|IRC_CAMP_ASSETS_B]] — 1 atributos
- [[irc_cmt_launches|IRC_CMT_LAUNCHES]] — 19 atributos (1 BICC)
- [[irc_cmt_recipients|IRC_CMT_RECIPIENTS]] — 22 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignId | CAMPAIGN_ID | — | — |
| 2 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |

### [[irc_camp_assets_b|IRC_CAMP_ASSETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampAssetBPEOAssetId | ASSET_ID | — | — |

### [[irc_cmt_launches|IRC_CMT_LAUNCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampMsgLaunchPEOBounceCount | BOUNCE_COUNT | — | — |
| 2 | CampMsgLaunchPEOCreatedBy | CREATED_BY | — | — |
| 3 | CampMsgLaunchPEOCreationDate | CREATION_DATE | — | — |
| 4 | CampMsgLaunchPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CampMsgLaunchPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | CampMsgLaunchPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | CampMsgLaunchPEOLaunchCompleteTs | LAUNCH_COMPLETE_TS | — | — |
| 8 | CampMsgLaunchPEOLaunchId | LAUNCH_ID | — | — |
| 9 | CampMsgLaunchPEOLaunchStartTs | LAUNCH_START_TS | — | — |
| 10 | CampMsgLaunchPEOLaunchStatusCode | LAUNCH_STATUS_CODE | — | — |
| 11 | CampMsgLaunchPEOLaunchTypeCode | LAUNCH_TYPE_CODE | — | — |
| 12 | CampMsgLaunchPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | CampMsgLaunchPEOOpenCount | OPEN_COUNT | — | — |
| 14 | CampMsgLaunchPEOPendingCount | PENDING_COUNT | — | — |
| 15 | CampMsgLaunchPEORecipientCount | RECIPIENT_COUNT | — | — |
| 16 | CampMsgLaunchPEOScheduleDate | SCHEDULE_DATE | — | — |
| 17 | CampMsgLaunchPEOSendByDate | SEND_BY_DATE | — | — |
| 18 | CampMsgLaunchPEOSubjectId | SUBJECT_ID | — | — |
| 19 | CampMsgLaunchPEOUnsentCount | UNSENT_COUNT | — | — |

### [[irc_cmt_recipients|IRC_CMT_RECIPIENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampMsgRecipientPEOAddress | ADDRESS | — | — |
| 2 | CampMsgRecipientPEOAddressId | ADDRESS_ID | — | — |
| 3 | CampMsgRecipientPEOCreatedBy | CREATED_BY | — | — |
| 4 | CampMsgRecipientPEOCreationDate | CREATION_DATE | — | — |
| 5 | CampMsgRecipientPEODeliveryTypeCode | DELIVERY_TYPE_CODE | — | — |
| 6 | CampMsgRecipientPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CampMsgRecipientPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CampMsgRecipientPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CampMsgRecipientPEOLaunchId | LAUNCH_ID | — | — |
| 10 | CampMsgRecipientPEOMsgBounceReason | MSG_BOUNCE_REASON | — | — |
| 11 | CampMsgRecipientPEOMsgBounceTs | MSG_BOUNCE_TS | — | — |
| 12 | CampMsgRecipientPEOMsgBounceTypeCode | MSG_BOUNCE_TYPE_CODE | — | — |
| 13 | CampMsgRecipientPEOMsgDeliveryTs | MSG_DELIVERY_TS | — | — |
| 14 | CampMsgRecipientPEOMsgOpenTs | MSG_OPEN_TS | — | — |
| 15 | CampMsgRecipientPEOMsgRetryCount | MSG_RETRY_COUNT | — | — |
| 16 | CampMsgRecipientPEOMsgSentTs | MSG_SENT_TS | — | — |
| 17 | CampMsgRecipientPEOMsgStatusCode | MSG_STATUS_CODE | — | ✅ |
| 18 | CampMsgRecipientPEOMsgUnsentTypeCode | MSG_UNSENT_TYPE_CODE | — | — |
| 19 | CampMsgRecipientPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | CampMsgRecipientPEOPersonId | PERSON_ID | — | — |
| 21 | CampMsgRecipientPEORecipientId | RECIPIENT_ID | 🔑 | ✅ |
| 22 | CampMsgRecipientPEOUmsMsgId | UMS_MSG_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
