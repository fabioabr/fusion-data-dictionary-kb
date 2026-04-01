---
id: DOC-OTHER-PVO-ProjectClassView
doc_type: system-doc
title: "ProjectClassView — PVO Cross-Module"
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
  - ProjectClassView
  - projectclassview
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectClassView

## 📌 Visão Geral

View Object para extração BICC de dados de Project Class View. Acessa as tabelas: PJF_CLASS_CATEGORIES_VL, PJF_CLASS_CODES_VL, PJF_PROJECT_CLASSES.

**Caminho:** `FscmTopModelAM.PjfSetupProjectsAM.ProjectClassView`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 3 | 1 | 8 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_categories_vl|PJF_CLASS_CATEGORIES_VL]] — 19 atributos (3 BICC)
- [[pjf_class_codes_vl|PJF_CLASS_CODES_VL]] — 12 atributos (3 BICC)
- [[pjf_project_classes|PJF_PROJECT_CLASSES]] — 12 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[pjf_class_categories_vl|PJF_CLASS_CATEGORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfClassCategoriesVlAllTypesValidFlag | ALL_TYPES_VALID_FLAG | — | — |
| 2 | PjfClassCategoriesVlAllowPercentFlag | ALLOW_PERCENT_FLAG | — | — |
| 3 | PjfClassCategoriesVlAutoaccountingFlag | AUTOACCOUNTING_FLAG | — | — |
| 4 | PjfClassCategoriesVlClassCategory | CLASS_CATEGORY | — | ✅ |
| 5 | PjfClassCategoriesVlClassCategoryId | CLASS_CATEGORY_ID | — | — |
| 6 | PjfClassCategoriesVlCreatedBy | CREATED_BY | — | — |
| 7 | PjfClassCategoriesVlCreationDate | CREATION_DATE | — | — |
| 8 | PjfClassCategoriesVlDescription | DESCRIPTION | — | ✅ |
| 9 | PjfClassCategoriesVlEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | PjfClassCategoriesVlIncludeInPjiFlag | INCLUDE_IN_PJI_FLAG | — | — |
| 11 | PjfClassCategoriesVlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PjfClassCategoriesVlLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PjfClassCategoriesVlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PjfClassCategoriesVlMandatoryFlag | MANDATORY_FLAG | — | — |
| 15 | PjfClassCategoriesVlObjectType | OBJECT_TYPE | — | — |
| 16 | PjfClassCategoriesVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PjfClassCategoriesVlPickOneCodeOnlyFlag | PICK_ONE_CODE_ONLY_FLAG | — | — |
| 18 | PjfClassCategoriesVlStartDateActive | START_DATE_ACTIVE | — | — |
| 19 | PjfClassCategoriesVlTotal100PercentFlag | TOTAL_100_PERCENT_FLAG | — | — |

### [[pjf_class_codes_vl|PJF_CLASS_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfClassCodesVlClassCategoryId | CLASS_CATEGORY_ID | — | — |
| 2 | PjfClassCodesVlClassCode | CLASS_CODE | — | ✅ |
| 3 | PjfClassCodesVlClassCodeId | CLASS_CODE_ID | — | — |
| 4 | PjfClassCodesVlCreatedBy | CREATED_BY | — | — |
| 5 | PjfClassCodesVlCreationDate | CREATION_DATE | — | — |
| 6 | PjfClassCodesVlDescription | DESCRIPTION | — | ✅ |
| 7 | PjfClassCodesVlEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | PjfClassCodesVlLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PjfClassCodesVlLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PjfClassCodesVlLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PjfClassCodesVlObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PjfClassCodesVlStartDateActive | START_DATE_ACTIVE | — | — |

### [[pjf_project_classes|PJF_PROJECT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfProjectClassesAdwNotifyFlag | ADW_NOTIFY_FLAG | — | — |
| 2 | PjfProjectClassesClassCategoryId | CLASS_CATEGORY_ID | — | — |
| 3 | PjfProjectClassesClassCodeId | CLASS_CODE_ID | — | — |
| 4 | PjfProjectClassesCodePercentage | CODE_PERCENTAGE | — | — |
| 5 | PjfProjectClassesCreatedBy | CREATED_BY | — | — |
| 6 | PjfProjectClassesCreationDate | CREATION_DATE | — | — |
| 7 | PjfProjectClassesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PjfProjectClassesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PjfProjectClassesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PjfProjectClassesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PjfProjectClassesProjectId | PROJECT_ID | — | — |
| 12 | ProjectClassesId | PROJECT_CLASSES_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
