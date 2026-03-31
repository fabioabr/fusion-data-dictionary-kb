---
id: DOC-OTHER-PVO-HierarchyGrandParentToChildPVO
doc_type: system-doc
title: "HierarchyGrandParentToChildPVO — PVO Cross-Module"
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
  - HierarchyGrandParentToChildPVO
  - hierarchygrandparenttochildpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HierarchyGrandParentToChildPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hierarchy Grand Parent To Child. Acessa as tabelas: WLF_LI_HIERARCHIES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.HierarchyGrandParentToChildPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 6 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]] — 12 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChildLearningItemHierarchyEOChildLearningItemId | CHILD_LEARNING_ITEM_ID | — | ✅ |
| 2 | ChildLearningItemHierarchyEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ChildLearningItemHierarchyEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ChildLearningItemHierarchyEOHierarchyId | HIERARCHY_ID | — | — |
| 5 | ChildLearningItemHierarchyEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 6 | ChildLearningItemHierarchyEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | GParentLearningItemHierarchyChildLearningItemId | CHILD_LEARNING_ITEM_ID | — | ✅ |
| 8 | GParentLearningItemHierarchyEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 9 | GParentLearningItemHierarchyEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | GParentLearningItemHierarchyHierarchyId | HIERARCHY_ID | 🔑 | ✅ |
| 11 | GParentLearningItemHierarchyLearningItemId | LEARNING_ITEM_ID | — | — |
| 12 | GParentLearningItemHierarchyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
