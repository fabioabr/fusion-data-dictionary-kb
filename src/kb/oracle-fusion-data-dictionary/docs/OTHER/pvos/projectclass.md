---
id: DOC-OTHER-PVO-ProjectClass
doc_type: system-doc
title: "ProjectClass — PVO Cross-Module"
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
  - ProjectClass
  - projectclass
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectClass

## 📌 Visão Geral

View Object para extração BICC de dados de Project Class. Acessa as tabelas: PJF_CLASS_CATEGORIES_B, PJF_CLASS_CODES_B, PJF_PROJECT_CLASSES.

**Caminho:** `FscmTopModelAM.PjfSetupProjectsAM.ProjectClass`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 3 | 1 | 11 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_categories_b|PJF_CLASS_CATEGORIES_B]] — 17 atributos (1 BICC)
- [[pjf_class_codes_b|PJF_CLASS_CODES_B]] — 10 atributos (1 BICC)
- [[pjf_project_classes|PJF_PROJECT_CLASSES]] — 12 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_class_categories_b|PJF_CLASS_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCategoryBasePEOAllTypesValidFlag | ALL_TYPES_VALID_FLAG | — | — |
| 2 | ClassCategoryBasePEOAllowPercentFlag | ALLOW_PERCENT_FLAG | — | — |
| 3 | ClassCategoryBasePEOAutoaccountingFlag | AUTOACCOUNTING_FLAG | — | — |
| 4 | ClassCategoryBasePEOClassCategoryId | CLASS_CATEGORY_ID | — | — |
| 5 | ClassCategoryBasePEOCreatedBy | CREATED_BY | — | — |
| 6 | ClassCategoryBasePEOCreationDate | CREATION_DATE | — | — |
| 7 | ClassCategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | ClassCategoryBasePEOIncludeInPjiFlag | INCLUDE_IN_PJI_FLAG | — | — |
| 9 | ClassCategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ClassCategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ClassCategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ClassCategoryBasePEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 13 | ClassCategoryBasePEOObjectType | OBJECT_TYPE | — | — |
| 14 | ClassCategoryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ClassCategoryBasePEOPickOneCodeOnlyFlag | PICK_ONE_CODE_ONLY_FLAG | — | — |
| 16 | ClassCategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 17 | ClassCategoryBasePEOTotal100PercentFlag | TOTAL_100_PERCENT_FLAG | — | — |

### [[pjf_class_codes_b|PJF_CLASS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCodeBasePEOClassCategoryId | CLASS_CATEGORY_ID | — | — |
| 2 | ClassCodeBasePEOClassCodeId | CLASS_CODE_ID | — | — |
| 3 | ClassCodeBasePEOCreatedBy | CREATED_BY | — | — |
| 4 | ClassCodeBasePEOCreationDate | CREATION_DATE | — | — |
| 5 | ClassCodeBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | ClassCodeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ClassCodeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ClassCodeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ClassCodeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ClassCodeBasePEOStartDateActive | START_DATE_ACTIVE | — | — |

### [[pjf_project_classes|PJF_PROJECT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfProjectClassesAdwNotifyFlag | ADW_NOTIFY_FLAG | — | — |
| 2 | PjfProjectClassesClassCategoryId | CLASS_CATEGORY_ID | — | ✅ |
| 3 | PjfProjectClassesClassCodeId | CLASS_CODE_ID | — | ✅ |
| 4 | PjfProjectClassesCodePercentage | CODE_PERCENTAGE | — | ✅ |
| 5 | PjfProjectClassesCreatedBy | CREATED_BY | — | ✅ |
| 6 | PjfProjectClassesCreationDate | CREATION_DATE | — | ✅ |
| 7 | PjfProjectClassesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PjfProjectClassesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PjfProjectClassesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PjfProjectClassesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PjfProjectClassesProjectId | PROJECT_ID | — | ✅ |
| 12 | ProjectClassesId | PROJECT_CLASSES_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
