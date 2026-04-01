---
id: DOC-HCM-PVO-SectionHierarchyPVO
doc_type: system-doc
title: "SectionHierarchyPVO — PVO Human Capital Management"
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
  - SectionHierarchyPVO
  - sectionhierarchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SectionHierarchyPVO

## 📌 Visão Geral

Disponibiliza hierarquia de seções de conteúdo de aprendizagem (e-learning). Mapeia a estrutura de módulos e lições em cursos do Oracle Learning.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.SectionHierarchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 72 | 3 | 6 | 12 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_li_content_f|WLF_LI_CONTENT_F]] — 44 atributos (3 BICC)
- [[wlf_li_elearnings_f|WLF_LI_ELEARNINGS_F]] — 14 atributos (3 PKs, 4 BICC)
- [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]] — 14 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[wlf_li_content_f|WLF_LI_CONTENT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentDEOAuthor | AUTHOR | — | — |
| 2 | ContentDEOCatalog | CATALOG | — | — |
| 3 | ContentDEOCatalogNumber | CATALOG_NUMBER | — | — |
| 4 | ContentDEOCompletionOnOpen | COMPLETION_ON_OPEN | — | — |
| 5 | ContentDEOContentId | CONTENT_ID | — | — |
| 6 | ContentDEOCopyrightText | COPYRIGHT_TEXT | — | — |
| 7 | ContentDEOCreatedBy | CREATED_BY | — | — |
| 8 | ContentDEOCreationDate | CREATION_DATE | — | — |
| 9 | ContentDEOCurrency | CURRENCY | — | — |
| 10 | ContentDEODisableReview | DISABLE_REVIEW | — | — |
| 11 | ContentDEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | ContentDEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 13 | ContentDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 14 | ContentDEOExternalIdentifier | EXTERNAL_IDENTIFIER | — | — |
| 15 | ContentDEOHideCorrectAnswers | HIDE_CORRECT_ANSWERS | — | — |
| 16 | ContentDEOHideScoreAdmin | HIDE_SCORE_ADMIN | — | — |
| 17 | ContentDEOHideScoreLearner | HIDE_SCORE_LEARNER | — | — |
| 18 | ContentDEOIngestionName | INGESTION_NAME | — | — |
| 19 | ContentDEOIngestionStatus | INGESTION_STATUS | — | — |
| 20 | ContentDEOIngestionStatusLog | INGESTION_STATUS_LOG | — | — |
| 21 | ContentDEOIsAutoCommit | IS_AUTO_COMMIT | — | — |
| 22 | ContentDEOIsCopyrighted | IS_COPYRIGHTED | — | — |
| 23 | ContentDEOIsVisible | IS_VISIBLE | — | — |
| 24 | ContentDEOKeywords | KEYWORDS | — | — |
| 25 | ContentDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | ContentDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | ContentDEOLastUpdateMethod | LAST_UPDATE_METHOD | — | — |
| 28 | ContentDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 29 | ContentDEOLaunchData | LAUNCH_DATA | — | — |
| 30 | ContentDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 31 | ContentDEOMasteryScore | MASTERY_SCORE | — | — |
| 32 | ContentDEOMaxAttempts | MAX_ATTEMPTS | — | — |
| 33 | ContentDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | ContentDEOPlayableItemsCount | PLAYABLE_ITEMS_COUNT | — | — |
| 35 | ContentDEOPrice | PRICE | — | — |
| 36 | ContentDEORecordedAttemptReview | RECORDED_ATTEMPT_REVIEW | — | — |
| 37 | ContentDEORecordedAttempts | RECORDED_ATTEMPTS | — | — |
| 38 | ContentDEORelatedContentId | RELATED_CONTENT_ID | — | — |
| 39 | ContentDEOStartingUrl | STARTING_URL | — | — |
| 40 | ContentDEOTimeLimit | TIME_LIMIT | — | — |
| 41 | ContentDEOTimeLimitAction | TIME_LIMIT_ACTION | — | — |
| 42 | ContentDEOTimeLimitUom | TIME_LIMIT_UOM | — | — |
| 43 | ContentDEOTrackingType | TRACKING_TYPE | — | ✅ |
| 44 | ContentDEOVersion | VERSION | — | — |

### [[wlf_li_elearnings_f|WLF_LI_ELEARNINGS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ELearningDEOCreatedBy | CREATED_BY | — | — |
| 2 | ELearningDEOCreatedById | CREATED_BY_ID | — | — |
| 3 | ELearningDEOCreationDate | CREATION_DATE | — | — |
| 4 | ELearningDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | ELearningDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | ELearningDEOElearningId | ELEARNING_ID | 🔑 | ✅ |
| 7 | ELearningDEOElearningType | ELEARNING_TYPE | — | — |
| 8 | ELearningDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | ELearningDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ELearningDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ELearningDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ELearningDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 13 | ELearningDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ELearningDEORelatedContentId | RELATED_CONTENT_ID | — | — |

### [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningItemHierarchyDEOChildLearningItemId | CHILD_LEARNING_ITEM_ID | — | ✅ |
| 2 | LearningItemHierarchyDEOCreatedBy | CREATED_BY | — | — |
| 3 | LearningItemHierarchyDEOCreationDate | CREATION_DATE | — | — |
| 4 | LearningItemHierarchyDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | LearningItemHierarchyDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | LearningItemHierarchyDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | LearningItemHierarchyDEOHierarchyId | HIERARCHY_ID | 🔑 | ✅ |
| 8 | LearningItemHierarchyDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LearningItemHierarchyDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LearningItemHierarchyDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LearningItemHierarchyDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 12 | LearningItemHierarchyDEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 13 | LearningItemHierarchyDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | LearningItemHierarchyDEOPosition | POSITION | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
