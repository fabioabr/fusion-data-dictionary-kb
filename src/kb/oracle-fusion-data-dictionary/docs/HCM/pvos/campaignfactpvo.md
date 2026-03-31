---
id: DOC-HCM-PVO-CampaignFactPVO
doc_type: system-doc
title: "CampaignFactPVO — PVO Human Capital Management"
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
  - CampaignFactPVO
  - campaignfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CampaignFactPVO

## 📌 Visão Geral

Relaciona campanhas de recrutamento a requisicoes de vagas. Suporta analise de efetividade e alcance de campanhas por posicao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCampaignsAM.CampaignFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 2 | 1 | 3 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[irc_campaigns_b|IRC_CAMPAIGNS_B]] — 3 atributos (1 PKs, 1 BICC)
- [[irc_camp_requisitions|IRC_CAMP_REQUISITIONS]] — 9 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_campaigns_b|IRC_CAMPAIGNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampaignBPEOCampaignCode | CAMPAIGN_CODE | — | — |
| 2 | CampaignBPEOCampaignTypeCode | CAMPAIGN_TYPE_CODE | — | — |
| 3 | CampaignId | CAMPAIGN_ID | 🔑 | ✅ |

### [[irc_camp_requisitions|IRC_CAMP_REQUISITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CampRequisitionId | CAMPAIGN_REQUISITION_ID | — | — |
| 2 | CampRequisitionPEOCampaignId | CAMPAIGN_ID | — | — |
| 3 | CampRequisitionPEOCreatedBy | CREATED_BY | — | — |
| 4 | CampRequisitionPEOCreationDate | CREATION_DATE | — | — |
| 5 | CampRequisitionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CampRequisitionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CampRequisitionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CampRequisitionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RequisitionId | REQUISITION_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
