---
id: DOC-OTHER-PVO-ContentRootPVO
doc_type: system-doc
title: "ContentRootPVO — PVO Cross-Module"
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
  - ContentRootPVO
  - contentrootpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContentRootPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Content Root. Acessa as tabelas: WLF_LEARNING_ITEMS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.ContentRootPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 3 | 4 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_learning_items_f|WLF_LEARNING_ITEMS_F]] — 25 atributos (3 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[wlf_learning_items_f|WLF_LEARNING_ITEMS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentRootDEOAssignmentRuleEnabled | ASSIGNMENT_RULE_ENABLED | — | — |
| 2 | ContentRootDEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | — |
| 3 | ContentRootDEOAutoCompetancyUpdateFlag | AUTO_COMPETANCY_UPDATE_FLAG | — | — |
| 4 | ContentRootDEOCreatedBy | CREATED_BY | — | — |
| 5 | ContentRootDEOCreatedById | CREATED_BY_ID | — | — |
| 6 | ContentRootDEOCreationDate | CREATION_DATE | — | — |
| 7 | ContentRootDEODeletedById | DELETED_BY_ID | — | — |
| 8 | ContentRootDEODeletedDate | DELETED_DATE | — | — |
| 9 | ContentRootDEODuration | DURATION | — | — |
| 10 | ContentRootDEODurationUom | DURATION_UOM | — | — |
| 11 | ContentRootDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 12 | ContentRootDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 13 | ContentRootDEOEndDate | END_DATE | — | — |
| 14 | ContentRootDEOEresEnabled | ERES_ENABLED | — | — |
| 15 | ContentRootDEOLanguageId | LANGUAGE_ID | — | — |
| 16 | ContentRootDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ContentRootDEOLearningItemId | LEARNING_ITEM_ID | 🔑 | ✅ |
| 18 | ContentRootDEOLearningItemNumber | LEARNING_ITEM_NUMBER | — | — |
| 19 | ContentRootDEOLearningItemType | LEARNING_ITEM_TYPE | — | — |
| 20 | ContentRootDEOLocation | LOCATION | — | — |
| 21 | ContentRootDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ContentRootDEOOwnedById | OWNED_BY_ID | — | — |
| 23 | ContentRootDEOStartDate | START_DATE | — | — |
| 24 | ContentRootDEOStatus | STATUS | — | — |
| 25 | ContentRootDEOVisibility | VISIBILITY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
