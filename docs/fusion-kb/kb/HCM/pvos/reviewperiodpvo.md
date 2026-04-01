---
id: DOC-HCM-PVO-ReviewPeriodPVO
doc_type: system-doc
title: "ReviewPeriodPVO — PVO Human Capital Management"
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
  - ReviewPeriodPVO
  - reviewperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReviewPeriodPVO

## 📌 Visão Geral

Extrai períodos de revisão de perfil com datas e descrições. Define ciclos temporais para avaliação e atualização de perfis de talento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.ReviewPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 11 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_review_periods_b|HRT_REVIEW_PERIODS_B]] — 12 atributos (1 PKs, 8 BICC)
- [[hrt_review_periods_tl|HRT_REVIEW_PERIODS_TL]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_review_periods_b|HRT_REVIEW_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ReviePeriodId | REVIEW_PERIOD_ID | — | — |
| 10 | ReviewPeriodId | REVIEW_PERIOD_ID | 🔑 | ✅ |
| 11 | StartDate | START_DATE | — | ✅ |
| 12 | StatusCode | STATUS_CODE | — | ✅ |

### [[hrt_review_periods_tl|HRT_REVIEW_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | Language1 | LANGUAGE | — | — |
| 6 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 10 | ReviewPeriodId1 | REVIEW_PERIOD_ID | — | — |
| 11 | ReviewPeriodName | REVIEW_PERIOD_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
