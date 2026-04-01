---
id: DOC-PO-PVO-RequisitionMediaLinkPVO
doc_type: system-doc
title: "RequisitionMediaLinkPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - RequisitionMediaLinkPVO
  - requisitionmedialinkpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionMediaLinkPVO

## 📌 Visão Geral

Extrai os links de mídia e publicações associados a requisições de contratação, com URLs, idiomas e canais. Permite análise de estratégia de divulgação e alcance de vagas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionMediaLinkPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 4 | 1 | 19 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[irc_media_links_b|IRC_MEDIA_LINKS_B]] — 4 atributos (4 BICC)
- [[irc_media_links_tl|IRC_MEDIA_LINKS_TL]] — 4 atributos (3 BICC)
- [[irc_media_link_languages|IRC_MEDIA_LINK_LANGUAGES]] — 2 atributos (2 BICC)
- [[irc_req_media_links|IRC_REQ_MEDIA_LINKS]] — 12 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[irc_media_links_b|IRC_MEDIA_LINKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MediaLinkPEOMediaLinkId | MEDIA_LINK_ID | — | ✅ |
| 2 | MediaTypeCode | MEDIA_TYPE_CODE | — | ✅ |
| 3 | ThumbnailUrl | THUMBNAIL_URL | — | ✅ |
| 4 | Url | URL | — | ✅ |

### [[irc_media_links_tl|IRC_MEDIA_LINKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | MediaLinkId1 | MEDIA_LINK_ID | — | — |
| 3 | SourceLang | SOURCE_LANG | — | ✅ |
| 4 | Title | TITLE | — | ✅ |

### [[irc_media_link_languages|IRC_MEDIA_LINK_LANGUAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MediaLinkLanguageId | MEDIA_LINK_LANGUAGE_ID | — | ✅ |
| 2 | MediaLinkLanguagePEOLanguageCode | LANGUAGE_CODE | — | ✅ |

### [[irc_req_media_links|IRC_REQ_MEDIA_LINKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | MediaLinkId | MEDIA_LINK_ID | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ReqMediaLinkId | REQ_MEDIA_LINK_ID | 🔑 | ✅ |
| 9 | RequisitionId | REQUISITION_ID | — | ✅ |
| 10 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 11 | ShowOnOffersFlag | SHOW_ON_OFFERS_FLAG | — | ✅ |
| 12 | VisibilityCode | VISIBILITY_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
