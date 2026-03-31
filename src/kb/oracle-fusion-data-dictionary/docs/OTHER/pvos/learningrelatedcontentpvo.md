---
id: DOC-OTHER-PVO-LearningRelatedContentPVO
doc_type: system-doc
title: "LearningRelatedContentPVO — PVO Cross-Module"
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
  - LearningRelatedContentPVO
  - learningrelatedcontentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningRelatedContentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Learning Related Content. Acessa as tabelas: WLF_LI_CONTENT_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningRelatedContentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 3 | 11 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_li_content_f|WLF_LI_CONTENT_F]] — 44 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wlf_li_content_f|WLF_LI_CONTENT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedContentDEOAuthor | AUTHOR | — | — |
| 2 | RelatedContentDEOCatalog | CATALOG | — | — |
| 3 | RelatedContentDEOCatalogNumber | CATALOG_NUMBER | — | — |
| 4 | RelatedContentDEOCompletionOnOpen | COMPLETION_ON_OPEN | — | — |
| 5 | RelatedContentDEOContentId | CONTENT_ID | 🔑 | ✅ |
| 6 | RelatedContentDEOCopyrightText | COPYRIGHT_TEXT | — | — |
| 7 | RelatedContentDEOCreatedBy | CREATED_BY | — | — |
| 8 | RelatedContentDEOCreationDate | CREATION_DATE | — | — |
| 9 | RelatedContentDEOCurrency | CURRENCY | — | — |
| 10 | RelatedContentDEODisableReview | DISABLE_REVIEW | — | — |
| 11 | RelatedContentDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 12 | RelatedContentDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 13 | RelatedContentDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 14 | RelatedContentDEOExternalIdentifier | EXTERNAL_IDENTIFIER | — | — |
| 15 | RelatedContentDEOHideCorrectAnswers | HIDE_CORRECT_ANSWERS | — | — |
| 16 | RelatedContentDEOHideScoreAdmin | HIDE_SCORE_ADMIN | — | ✅ |
| 17 | RelatedContentDEOHideScoreLearner | HIDE_SCORE_LEARNER | — | ✅ |
| 18 | RelatedContentDEOIngestionName | INGESTION_NAME | — | — |
| 19 | RelatedContentDEOIngestionStatus | INGESTION_STATUS | — | — |
| 20 | RelatedContentDEOIngestionStatusLog | INGESTION_STATUS_LOG | — | — |
| 21 | RelatedContentDEOIsAutoCommit | IS_AUTO_COMMIT | — | — |
| 22 | RelatedContentDEOIsCopyrighted | IS_COPYRIGHTED | — | — |
| 23 | RelatedContentDEOIsVisible | IS_VISIBLE | — | — |
| 24 | RelatedContentDEOKeywords | KEYWORDS | — | — |
| 25 | RelatedContentDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | RelatedContentDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | RelatedContentDEOLastUpdateMethod | LAST_UPDATE_METHOD | — | — |
| 28 | RelatedContentDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | RelatedContentDEOLaunchData | LAUNCH_DATA | — | — |
| 30 | RelatedContentDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 31 | RelatedContentDEOMasteryScore | MASTERY_SCORE | — | ✅ |
| 32 | RelatedContentDEOMaxAttempts | MAX_ATTEMPTS | — | ✅ |
| 33 | RelatedContentDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | RelatedContentDEOPlayableItemsCount | PLAYABLE_ITEMS_COUNT | — | — |
| 35 | RelatedContentDEOPrice | PRICE | — | — |
| 36 | RelatedContentDEORecordedAttemptReview | RECORDED_ATTEMPT_REVIEW | — | — |
| 37 | RelatedContentDEORecordedAttempts | RECORDED_ATTEMPTS | — | — |
| 38 | RelatedContentDEORelatedContentId | RELATED_CONTENT_ID | — | — |
| 39 | RelatedContentDEOStartingUrl | STARTING_URL | — | — |
| 40 | RelatedContentDEOTimeLimit | TIME_LIMIT | — | ✅ |
| 41 | RelatedContentDEOTimeLimitAction | TIME_LIMIT_ACTION | — | — |
| 42 | RelatedContentDEOTimeLimitUom | TIME_LIMIT_UOM | — | ✅ |
| 43 | RelatedContentDEOTrackingType | TRACKING_TYPE | — | ✅ |
| 44 | RelatedContentDEOVersion | VERSION | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
