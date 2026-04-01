---
id: DOC-OTHER-PVO-PerspectiveHierarchyPVO
doc_type: system-doc
title: "PerspectiveHierarchyPVO — PVO Cross-Module"
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
  - PerspectiveHierarchyPVO
  - perspectivehierarchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerspectiveHierarchyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Perspective Hierarchy. Acessa as tabelas: GRC_PERSP_HIER_XREF, GRC_PERSP_TREE_B, GRC_PERSP_TREE_TL.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.PerspectiveHierarchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 72 | 3 | 2 | 39 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[grc_persp_hier_xref|GRC_PERSP_HIER_XREF]] — 36 atributos (2 PKs, 31 BICC)
- [[grc_persp_tree_b|GRC_PERSP_TREE_B]] — 26 atributos (5 BICC)
- [[grc_persp_tree_tl|GRC_PERSP_TREE_TL]] — 10 atributos (3 BICC)

---

## ⚙️ Atributos

### [[grc_persp_hier_xref|GRC_PERSP_HIER_XREF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspectiveHierPEOCreatedBy | CREATED_BY | — | — |
| 2 | PerspectiveHierPEOCreationDate | CREATION_DATE | — | — |
| 3 | PerspectiveHierPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | PerspectiveHierPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | PerspectiveHierPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | PerspectiveHierPEOLevel01NodeId | LEVEL01_NODE_ID | — | ✅ |
| 7 | PerspectiveHierPEOLevel01Pk1 | LEVEL01_PK1 | — | ✅ |
| 8 | PerspectiveHierPEOLevel02NodeId | LEVEL02_NODE_ID | — | ✅ |
| 9 | PerspectiveHierPEOLevel02Pk1 | LEVEL02_PK1 | — | ✅ |
| 10 | PerspectiveHierPEOLevel03NodeId | LEVEL03_NODE_ID | — | ✅ |
| 11 | PerspectiveHierPEOLevel03Pk1 | LEVEL03_PK1 | — | ✅ |
| 12 | PerspectiveHierPEOLevel04NodeId | LEVEL04_NODE_ID | — | ✅ |
| 13 | PerspectiveHierPEOLevel04Pk1 | LEVEL04_PK1 | — | ✅ |
| 14 | PerspectiveHierPEOLevel05NodeId | LEVEL05_NODE_ID | — | ✅ |
| 15 | PerspectiveHierPEOLevel05Pk1 | LEVEL05_PK1 | — | ✅ |
| 16 | PerspectiveHierPEOLevel06NodeId | LEVEL06_NODE_ID | — | ✅ |
| 17 | PerspectiveHierPEOLevel06Pk1 | LEVEL06_PK1 | — | ✅ |
| 18 | PerspectiveHierPEOLevel07NodeId | LEVEL07_NODE_ID | — | ✅ |
| 19 | PerspectiveHierPEOLevel07Pk1 | LEVEL07_PK1 | — | ✅ |
| 20 | PerspectiveHierPEOLevel08NodeId | LEVEL08_NODE_ID | — | ✅ |
| 21 | PerspectiveHierPEOLevel08Pk1 | LEVEL08_PK1 | — | ✅ |
| 22 | PerspectiveHierPEOLevel09NodeId | LEVEL09_NODE_ID | — | ✅ |
| 23 | PerspectiveHierPEOLevel09Pk1 | LEVEL09_PK1 | — | ✅ |
| 24 | PerspectiveHierPEOLevel10NodeId | LEVEL10_NODE_ID | — | ✅ |
| 25 | PerspectiveHierPEOLevel10Pk1 | LEVEL10_PK1 | — | ✅ |
| 26 | PerspectiveHierPEOLevel11NodeId | LEVEL11_NODE_ID | — | ✅ |
| 27 | PerspectiveHierPEOLevel11Pk1 | LEVEL11_PK1 | — | ✅ |
| 28 | PerspectiveHierPEOLevel12NodeId | LEVEL12_NODE_ID | — | ✅ |
| 29 | PerspectiveHierPEOLevel12Pk1 | LEVEL12_PK1 | — | ✅ |
| 30 | PerspectiveHierPEOLevel13NodeId | LEVEL13_NODE_ID | — | ✅ |
| 31 | PerspectiveHierPEOLevel13Pk1 | LEVEL13_PK1 | — | ✅ |
| 32 | PerspectiveHierPEOLevel14NodeId | LEVEL14_NODE_ID | — | ✅ |
| 33 | PerspectiveHierPEOLevel14Pk1 | LEVEL14_PK1 | — | ✅ |
| 34 | PerspectiveHierPEOLevel15NodeId | LEVEL15_NODE_ID | 🔑 | ✅ |
| 35 | PerspectiveHierPEOLevel15Pk1 | LEVEL15_PK1 | — | ✅ |
| 36 | PerspectiveHierPEOTreeId | TREE_ID | 🔑 | ✅ |

### [[grc_persp_tree_b|GRC_PERSP_TREE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspectiveTreeBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | PerspectiveTreeBasePEOApprovedBy | APPROVED_BY | — | — |
| 3 | PerspectiveTreeBasePEOApprovedDate | APPROVED_DATE | — | — |
| 4 | PerspectiveTreeBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | PerspectiveTreeBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | PerspectiveTreeBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | PerspectiveTreeBasePEOGrcRowId | GRC_ROW_ID | — | — |
| 8 | PerspectiveTreeBasePEOIsSeededFlag | IS_SEEDED_FLAG | — | — |
| 9 | PerspectiveTreeBasePEOIsSystemFlag | IS_SYSTEM_FLAG | — | — |
| 10 | PerspectiveTreeBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 11 | PerspectiveTreeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PerspectiveTreeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PerspectiveTreeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PerspectiveTreeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PerspectiveTreeBasePEOPerspTypeCode | PERSP_TYPE_CODE | — | — |
| 16 | PerspectiveTreeBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 17 | PerspectiveTreeBasePEOReviewedBy | REVIEWED_BY | — | — |
| 18 | PerspectiveTreeBasePEOReviewedDate | REVIEWED_DATE | — | — |
| 19 | PerspectiveTreeBasePEORevisionDate | REVISION_DATE | — | ✅ |
| 20 | PerspectiveTreeBasePEORevisionNumber | REVISION_NUMBER | — | ✅ |
| 21 | PerspectiveTreeBasePEORevisionSubmittedBy | REVISION_SUBMITTED_BY | — | — |
| 22 | PerspectiveTreeBasePEOStartDate | START_DATE | — | — |
| 23 | PerspectiveTreeBasePEOStateCode | STATE_CODE | — | ✅ |
| 24 | PerspectiveTreeBasePEOStateDate | STATE_DATE | — | — |
| 25 | PerspectiveTreeBasePEOStatus | STATUS | — | ✅ |
| 26 | PerspectiveTreeBasePEOTreeId | TREE_ID | — | — |

### [[grc_persp_tree_tl|GRC_PERSP_TREE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerspectiveTreeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PerspectiveTreeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PerspectiveTreeTranslationPEODetailedDescr | DETAILED_DESCRIPTION | — | ✅ |
| 4 | PerspectiveTreeTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | PerspectiveTreeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PerspectiveTreeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PerspectiveTreeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PerspectiveTreeTranslationPEOName | NAME | — | ✅ |
| 9 | PerspectiveTreeTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 10 | PerspectiveTreeTranslationPEOTreeId | TREE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
