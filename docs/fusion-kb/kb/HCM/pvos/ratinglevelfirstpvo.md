---
id: DOC-HCM-PVO-RatingLevelFirstPVO
doc_type: system-doc
title: "RatingLevelFirstPVO — PVO Human Capital Management"
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
  - RatingLevelFirstPVO
  - ratinglevelfirstpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatingLevelFirstPVO

## 📌 Visão Geral

Extrai níveis de avaliação primários com traduções no idioma base. Utilizado como referência de escala em avaliações de competências e desempenho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.RatingLevelFirstPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 3 | 26 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 21 atributos (2 PKs, 20 BICC)
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 8 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 8 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | ✅ |
| 9 | RatingLevelBPEODateFrom | DATE_FROM | — | ✅ |
| 10 | RatingLevelBPEODateTo | DATE_TO | — | ✅ |
| 11 | RatingLevelBPEOFromPoints | FROM_POINTS | — | ✅ |
| 12 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | ✅ |
| 13 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | ✅ |
| 14 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 15 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | ✅ |
| 16 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 17 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | 🔑 | ✅ |
| 18 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 19 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | ✅ |
| 20 | RatingLevelBPEOStarRating | STAR_RATING | — | ✅ |
| 21 | RatingLevelBPEOToPoints | TO_POINTS | — | ✅ |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | RatingLevelTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RatingLevelTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | RatingLevelTranslationPEORatingDescription | RATING_DESCRIPTION | — | ✅ |
| 5 | RatingLevelTranslationPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 6 | RatingLevelTranslationPEORatingShortDescr | RATING_SHORT_DESCR | — | ✅ |
| 7 | RatingLevelTranslationPEOReviewRatingDescr | REVIEW_RATING_DESCR | — | ✅ |
| 8 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
