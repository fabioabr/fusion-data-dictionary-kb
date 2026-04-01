---
id: DOC-HCM-PVO-LearningItemPVO
doc_type: system-doc
title: "LearningItemPVO — PVO Human Capital Management"
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
  - LearningItemPVO
  - learningitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LearningItemPVO

## 📌 Visão Geral

Disponibiliza itens de aprendizagem (cursos, módulos, atividades) com duração e vigência. Fundamental para catálogo de treinamentos corporativos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.LearningItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 3 | 12 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_learning_items_f|WLF_LEARNING_ITEMS_F]] — 36 atributos (3 PKs, 9 BICC)
- [[wlf_learning_items_f_tl|WLF_LEARNING_ITEMS_F_TL]] — 10 atributos (3 BICC)

---

## ⚙️ Atributos

### [[wlf_learning_items_f|WLF_LEARNING_ITEMS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningItemDEOAssignmentRuleEnabled | ASSIGNMENT_RULE_ENABLED | — | — |
| 2 | LearningItemDEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | — |
| 3 | LearningItemDEOAttributionId | ATTRIBUTION_ID | — | — |
| 4 | LearningItemDEOAttributionType | ATTRIBUTION_TYPE | — | — |
| 5 | LearningItemDEOAutoCompetancyUpdateFlag | AUTO_COMPETANCY_UPDATE_FLAG | — | — |
| 6 | LearningItemDEOCreatedBy | CREATED_BY | — | — |
| 7 | LearningItemDEOCreatedById | CREATED_BY_ID | — | — |
| 8 | LearningItemDEOCreationDate | CREATION_DATE | — | — |
| 9 | LearningItemDEODeletedById | DELETED_BY_ID | — | — |
| 10 | LearningItemDEODeletedDate | DELETED_DATE | — | — |
| 11 | LearningItemDEODuration | DURATION | — | ✅ |
| 12 | LearningItemDEODurationUom | DURATION_UOM | — | — |
| 13 | LearningItemDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 14 | LearningItemDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 15 | LearningItemDEOEndDate | END_DATE | — | ✅ |
| 16 | LearningItemDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 17 | LearningItemDEOEresEnabled | ERES_ENABLED | — | — |
| 18 | LearningItemDEOLanguageId | LANGUAGE_ID | — | — |
| 19 | LearningItemDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LearningItemDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | LearningItemDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | LearningItemDEOLearningItemId | LEARNING_ITEM_ID | 🔑 | ✅ |
| 23 | LearningItemDEOLearningItemNumber | LEARNING_ITEM_NUMBER | — | ✅ |
| 24 | LearningItemDEOLearningItemSubType | LEARNING_ITEM_SUB_TYPE | — | — |
| 25 | LearningItemDEOLearningItemType | LEARNING_ITEM_TYPE | — | ✅ |
| 26 | LearningItemDEOLocation | LOCATION | — | — |
| 27 | LearningItemDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | LearningItemDEOOwnedById | OWNED_BY_ID | — | — |
| 29 | LearningItemDEOSourceId | SOURCE_ID | — | — |
| 30 | LearningItemDEOSourceInfo | SOURCE_INFO | — | — |
| 31 | LearningItemDEOSourceType | SOURCE_TYPE | — | — |
| 32 | LearningItemDEOStartDate | START_DATE | — | ✅ |
| 33 | LearningItemDEOStatus | STATUS | — | — |
| 34 | LearningItemDEOThumbnailId | THUMBNAIL_ID | — | — |
| 35 | LearningItemDEOTrailerLiId | TRAILER_LI_ID | — | — |
| 36 | LearningItemDEOVisibility | VISIBILITY | — | — |

### [[wlf_learning_items_f_tl|WLF_LEARNING_ITEMS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningItemTranslationDEODescription | DESCRIPTION | — | ✅ |
| 2 | LearningItemTranslationDEODescriptionLong | DESCRIPTION_LONG | — | — |
| 3 | LearningItemTranslationDEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | LearningItemTranslationDEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | LearningItemTranslationDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | LearningItemTranslationDEOLanguage | LANGUAGE | — | — |
| 7 | LearningItemTranslationDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 8 | LearningItemTranslationDEOName | NAME | — | ✅ |
| 9 | LearningItemTranslationDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LearningItemTranslationDEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
