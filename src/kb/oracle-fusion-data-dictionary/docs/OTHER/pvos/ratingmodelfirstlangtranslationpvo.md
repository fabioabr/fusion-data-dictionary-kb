---
id: DOC-OTHER-PVO-RatingModelFirstLangTranslationPVO
doc_type: system-doc
title: "RatingModelFirstLangTranslationPVO — PVO Cross-Module"
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
  - RatingModelFirstLangTranslationPVO
  - ratingmodelfirstlangtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatingModelFirstLangTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rating Model First Lang Translation. Acessa as tabelas: HRT_RATING_MODELS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileContentLibraryAM.RatingModelFirstLangTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrt_rating_models_tl|HRT_RATING_MODELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RatingDescription | RATING_DESCRIPTION | — | ✅ |
| 10 | RatingModelId | RATING_MODEL_ID | 🔑 | ✅ |
| 11 | RatingName | RATING_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
