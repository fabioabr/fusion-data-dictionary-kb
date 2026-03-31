---
id: DOC-OTHER-PVO-CoursePVO
doc_type: system-doc
title: "CoursePVO — PVO Cross-Module"
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
  - CoursePVO
  - coursepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CoursePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Course. Acessa as tabelas: WLF_LI_COURSES_F, WLF_LI_HIERARCHIES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.CoursePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 2 | 3 | 32 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_li_courses_f|WLF_LI_COURSES_F]] — 24 atributos (3 PKs, 24 BICC)
- [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]] — 8 atributos (8 BICC)

---

## ⚙️ Atributos

### [[wlf_li_courses_f|WLF_LI_COURSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CourseDEOCourseId | COURSE_ID | 🔑 | ✅ |
| 2 | CourseDEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | CourseDEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | CourseDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | CourseDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | CourseDEOEffort | EFFORT | — | ✅ |
| 7 | CourseDEOEffortUom | EFFORT_UOM | — | ✅ |
| 8 | CourseDEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 9 | CourseDEOExpensesAllowed | EXPENSES_ALLOWED | — | ✅ |
| 10 | CourseDEOIntendedAudience | INTENDED_AUDIENCE | — | ✅ |
| 11 | CourseDEOInvOrganizationId | INV_ORGANIZATION_ID | — | ✅ |
| 12 | CourseDEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 13 | CourseDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CourseDEOLearningItemId | LEARNING_ITEM_ID | — | ✅ |
| 15 | CourseDEOMaximumAttendees | MAXIMUM_ATTENDEES | — | ✅ |
| 16 | CourseDEOMaximumInternalAttendees | MAXIMUM_INTERNAL_ATTENDEES | — | ✅ |
| 17 | CourseDEOMaximumTrainingHours | MAXIMUM_TRAINING_HOURS | — | ✅ |
| 18 | CourseDEOMinimumAttendees | MINIMUM_ATTENDEES | — | ✅ |
| 19 | CourseDEOMinimumTrainingHours | MINIMUM_TRAINING_HOURS | — | ✅ |
| 20 | CourseDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | CourseDEOProfessionalCreditType | PROFESSIONAL_CREDIT_TYPE | — | ✅ |
| 22 | CourseDEOProfessionalCredits | PROFESSIONAL_CREDITS | — | ✅ |
| 23 | CourseDEOSuccessCriteria | SUCCESS_CRITERIA | — | ✅ |
| 24 | CourseDEOUserStatus | USER_STATUS | — | ✅ |

### [[wlf_li_hierarchies_f|WLF_LI_HIERARCHIES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LearningItemHierarchyDEOChildLearningItemId | CHILD_LEARNING_ITEM_ID | — | ✅ |
| 2 | LearningItemHierarchyDEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | LearningItemHierarchyDEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | LearningItemHierarchyDEOHierarchyId | HIERARCHY_ID | — | ✅ |
| 5 | LearningItemHierarchyDEOLearningItemId | LEARNING_ITEM_ID | — | ✅ |
| 6 | LearningItemHierarchyDEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 7 | LearningItemHierarchyDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | LearningItemHierarchyDEOPosition | POSITION | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
