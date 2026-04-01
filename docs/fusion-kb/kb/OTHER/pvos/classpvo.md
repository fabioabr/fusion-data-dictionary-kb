---
id: DOC-OTHER-PVO-ClassPVO
doc_type: system-doc
title: "ClassPVO — PVO Cross-Module"
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
  - ClassPVO
  - classpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Class. Acessa as tabelas: WLF_LI_CLASSES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.ClassPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 3 | 12 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_li_classes_f|WLF_LI_CLASSES_F]] — 27 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[wlf_li_classes_f|WLF_LI_CLASSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassDEOClassId | CLASS_ID | 🔑 | ✅ |
| 2 | ClassDEOCoordinatorId | COORDINATOR_ID | — | — |
| 3 | ClassDEOCreatedBy | CREATED_BY | — | — |
| 4 | ClassDEOCreationDate | CREATION_DATE | — | — |
| 5 | ClassDEODeliveryMode | DELIVERY_MODE | — | ✅ |
| 6 | ClassDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | ClassDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | ClassDEOEnableCapacity | ENABLE_CAPACITY | — | ✅ |
| 9 | ClassDEOEnableWaitlist | ENABLE_WAITLIST | — | ✅ |
| 10 | ClassDEOEnrolmentEndDate | ENROLMENT_END_DATE | — | — |
| 11 | ClassDEOEnrolmentStartDate | ENROLMENT_START_DATE | — | — |
| 12 | ClassDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 13 | ClassDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ClassDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ClassDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ClassDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 17 | ClassDEOLocationId | LOCATION_ID | — | — |
| 18 | ClassDEOMaximumAttendees | MAXIMUM_ATTENDEES | — | ✅ |
| 19 | ClassDEOMaximumInternalAttendees | MAXIMUM_INTERNAL_ATTENDEES | — | — |
| 20 | ClassDEOMinimumAttendees | MINIMUM_ATTENDEES | — | ✅ |
| 21 | ClassDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | ClassDEOPrimaryInstructorId | PRIMARY_INSTRUCTOR_ID | — | — |
| 23 | ClassDEORelatedContentId | RELATED_CONTENT_ID | — | — |
| 24 | ClassDEORemainingSeats | REMAINING_SEATS | — | ✅ |
| 25 | ClassDEOTimezone | TIMEZONE | — | ✅ |
| 26 | ClassDEOUserStatus | USER_STATUS | — | — |
| 27 | ClassDEOWaitlistMgmtMode | WAITLIST_MGMT_MODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
