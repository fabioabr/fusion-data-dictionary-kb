---
id: DOC-OTHER-PVO-PerspectivePVO
doc_type: system-doc
title: "PerspectivePVO — PVO Cross-Module"
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
  - PerspectivePVO
  - perspectivepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerspectivePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Perspective. Acessa as tabelas: GRC_PERSP_ITEM_B, GRC_PERSP_ITEM_TL.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.PerspectivePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 1 | 7 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[grc_persp_item_b|GRC_PERSP_ITEM_B]] — 18 atributos (1 PKs, 4 BICC)
- [[grc_persp_item_tl|GRC_PERSP_ITEM_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[grc_persp_item_b|GRC_PERSP_ITEM_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspectiveBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | PerspectiveBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | PerspectiveBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | PerspectiveBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | PerspectiveBasePEOExternalValue | EXTERNAL_VALUE | — | — |
| 6 | PerspectiveBasePEOGrcRowId | GRC_ROW_ID | — | — |
| 7 | PerspectiveBasePEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 8 | PerspectiveBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PerspectiveBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PerspectiveBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PerspectiveBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PerspectiveBasePEOPerspItemId | PERSP_ITEM_ID | 🔑 | ✅ |
| 13 | PerspectiveBasePEOPerspTypeCode | PERSP_TYPE_CODE | — | — |
| 14 | PerspectiveBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 15 | PerspectiveBasePEORevisionDate | REVISION_DATE | — | ✅ |
| 16 | PerspectiveBasePEORoot | ROOT | — | — |
| 17 | PerspectiveBasePEOStartDate | START_DATE | — | — |
| 18 | PerspectiveBasePEOStatus | STATUS | — | ✅ |

### [[grc_persp_item_tl|GRC_PERSP_ITEM_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspectiveTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PerspectiveTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PerspectiveTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | ✅ |
| 4 | PerspectiveTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | PerspectiveTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PerspectiveTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PerspectiveTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PerspectiveTranslationPEOName | NAME | — | ✅ |
| 9 | PerspectiveTranslationPEOPerspItemId | PERSP_ITEM_ID | — | — |
| 10 | PerspectiveTranslationPEOPerspTypeCode | PERSP_TYPE_CODE | — | — |
| 11 | PerspectiveTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
