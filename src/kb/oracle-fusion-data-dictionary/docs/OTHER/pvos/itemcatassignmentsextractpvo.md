---
id: DOC-OTHER-PVO-ItemCatAssignmentsExtractPVO
doc_type: system-doc
title: "ItemCatAssignmentsExtractPVO — PVO Cross-Module"
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
  - ItemCatAssignmentsExtractPVO
  - itemcatassignmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemCatAssignmentsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Cat Assignments Extract. Acessa as tabelas: EGP_ITEM_CAT_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemCatAssignmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_cat_assignments|EGP_ITEM_CAT_ASSIGNMENTS]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[egp_item_cat_assignments|EGP_ITEM_CAT_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemCatAssignPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 2 | ItemCatAssignPEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 3 | ItemCatAssignPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ItemCatAssignPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ItemCatAssignPEOEndDate | END_DATE | — | ✅ |
| 6 | ItemCatAssignPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 7 | ItemCatAssignPEOItemCategoryAssignmentId | ITEM_CATEGORY_ASSIGNMENT_ID | — | ✅ |
| 8 | ItemCatAssignPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ItemCatAssignPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ItemCatAssignPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ItemCatAssignPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 12 | ItemCatAssignPEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
