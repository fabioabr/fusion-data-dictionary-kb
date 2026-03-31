---
id: DOC-HCM-PVO-RatingModelFirstPVO
doc_type: system-doc
title: "RatingModelFirstPVO — PVO Human Capital Management"
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
  - RatingModelFirstPVO
  - ratingmodelfirstpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatingModelFirstPVO

## 📌 Visão Geral

Extrai modelos de avaliação primários com dados base e traduções. Referência principal para escalas de competência no framework de Talent Profile.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.RatingModelFirstPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 3 | 16 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_rating_models_b|HRT_RATING_MODELS_B]] — 13 atributos (2 PKs, 12 BICC)
- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 7 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hrt_rating_models_b|HRT_RATING_MODELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | RatingModelBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 8 | RatingModelBPEODateFrom | DATE_FROM | — | ✅ |
| 9 | RatingModelBPEODateTo | DATE_TO | — | ✅ |
| 10 | RatingModelBPEODistributionThreshold | DISTRIBUTION_THRESHOLD | — | ✅ |
| 11 | RatingModelBPEOModuleId | MODULE_ID | — | — |
| 12 | RatingModelBPEORatingModelCode | RATING_MODEL_CODE | — | ✅ |
| 13 | RatingModelBPEORatingModelId | RATING_MODEL_ID | 🔑 | ✅ |

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | RatingModelTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RatingModelTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | RatingModelTranslationPEORatingDescription | RATING_DESCRIPTION | — | ✅ |
| 5 | RatingModelTranslationPEORatingModelId | RATING_MODEL_ID | — | — |
| 6 | RatingModelTranslationPEORatingName | RATING_NAME | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
