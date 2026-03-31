---
id: DOC-OTHER-PVO-AcademicGroupPVO
doc_type: system-doc
title: "AcademicGroupPVO — PVO Cross-Module"
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
  - AcademicGroupPVO
  - academicgrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcademicGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Academic Group. Acessa as tabelas: HER_CURRICULUM_BUILD_STATUS_VL, HER_CURRICULUM_HEADER_F_VL, HER_CURRICULUM_TYPE_VL (+2).

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.AcademicGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 310 | 5 | 1 | 12 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[her_curriculum_build_status_vl|HER_CURRICULUM_BUILD_STATUS_VL]] — 64 atributos (2 BICC)
- [[her_curriculum_header_f_vl|HER_CURRICULUM_HEADER_F_VL]] — 75 atributos (8 BICC)
- [[her_curriculum_type_vl|HER_CURRICULUM_TYPE_VL]] — 68 atributos (1 BICC)
- [[her_curric_group|HER_CURRIC_GROUP]] — 101 atributos
- [[her_curric_header_vl|HER_CURRIC_HEADER_VL]] — 2 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[her_curriculum_build_status_vl|HER_CURRICULUM_BUILD_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumBuildStatusPEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | CurriculumBuildStatusPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CurriculumBuildStatusPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CurriculumBuildStatusPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CurriculumBuildStatusPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CurriculumBuildStatusPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CurriculumBuildStatusPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CurriculumBuildStatusPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CurriculumBuildStatusPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CurriculumBuildStatusPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CurriculumBuildStatusPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CurriculumBuildStatusPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CurriculumBuildStatusPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CurriculumBuildStatusPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CurriculumBuildStatusPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CurriculumBuildStatusPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CurriculumBuildStatusPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CurriculumBuildStatusPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CurriculumBuildStatusPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CurriculumBuildStatusPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CurriculumBuildStatusPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CurriculumBuildStatusPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | CurriculumBuildStatusPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CurriculumBuildStatusPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | CurriculumBuildStatusPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | CurriculumBuildStatusPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | CurriculumBuildStatusPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | CurriculumBuildStatusPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | CurriculumBuildStatusPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | CurriculumBuildStatusPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | CurriculumBuildStatusPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | CurriculumBuildStatusPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | CurriculumBuildStatusPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | CurriculumBuildStatusPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | CurriculumBuildStatusPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | CurriculumBuildStatusPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | CurriculumBuildStatusPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | CurriculumBuildStatusPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | CurriculumBuildStatusPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | CurriculumBuildStatusPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | CurriculumBuildStatusPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | CurriculumBuildStatusPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | CurriculumBuildStatusPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | CurriculumBuildStatusPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | CurriculumBuildStatusPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | CurriculumBuildStatusPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | CurriculumBuildStatusPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | CurriculumBuildStatusPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | CurriculumBuildStatusPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | CurriculumBuildStatusPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | CurriculumBuildStatusPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | CurriculumBuildStatusPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | CurriculumBuildStatusPEOBuildStatusCode | BUILD_STATUS_CODE | — | — |
| 54 | CurriculumBuildStatusPEOBuildStatusSortNum | BUILD_STATUS_SORT_NUM | — | — |
| 55 | CurriculumBuildStatusPEOCreatedBy | CREATED_BY | — | — |
| 56 | CurriculumBuildStatusPEOCreationDate | CREATION_DATE | — | — |
| 57 | CurriculumBuildStatusPEOCurriculumBuildStatusId | CURRICULUM_BUILD_STATUS_ID | — | — |
| 58 | CurriculumBuildStatusPEODescription | DESCRIPTION | — | — |
| 59 | CurriculumBuildStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | CurriculumBuildStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | CurriculumBuildStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | CurriculumBuildStatusPEONameDisplay | NAME_DISPLAY | — | ✅ |
| 63 | CurriculumBuildStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | CurriculumBuildStatusPEOSystemStatusCode | SYSTEM_STATUS_CODE | — | — |

### [[her_curriculum_header_f_vl|HER_CURRICULUM_HEADER_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumHeaderDPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CurriculumHeaderDPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CurriculumHeaderDPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CurriculumHeaderDPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CurriculumHeaderDPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CurriculumHeaderDPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CurriculumHeaderDPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CurriculumHeaderDPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CurriculumHeaderDPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CurriculumHeaderDPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CurriculumHeaderDPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CurriculumHeaderDPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CurriculumHeaderDPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CurriculumHeaderDPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | CurriculumHeaderDPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | CurriculumHeaderDPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | CurriculumHeaderDPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | CurriculumHeaderDPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | CurriculumHeaderDPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | CurriculumHeaderDPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | CurriculumHeaderDPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | CurriculumHeaderDPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CurriculumHeaderDPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | CurriculumHeaderDPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CurriculumHeaderDPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CurriculumHeaderDPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CurriculumHeaderDPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CurriculumHeaderDPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | CurriculumHeaderDPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | CurriculumHeaderDPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | CurriculumHeaderDPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | CurriculumHeaderDPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CurriculumHeaderDPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | CurriculumHeaderDPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | CurriculumHeaderDPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | CurriculumHeaderDPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | CurriculumHeaderDPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | CurriculumHeaderDPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | CurriculumHeaderDPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | CurriculumHeaderDPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | CurriculumHeaderDPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | CurriculumHeaderDPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | CurriculumHeaderDPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | CurriculumHeaderDPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | CurriculumHeaderDPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | CurriculumHeaderDPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | CurriculumHeaderDPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | CurriculumHeaderDPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | CurriculumHeaderDPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | CurriculumHeaderDPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | CurriculumHeaderDPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CurriculumHeaderDPEOCalId | CAL_ID | — | — |
| 53 | CurriculumHeaderDPEOCartEnabledFlag | CART_ENABLED_FLAG | — | — |
| 54 | CurriculumHeaderDPEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumHeaderDPEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumHeaderDPEOCurriculumBuildStatusId | CURRICULUM_BUILD_STATUS_ID | — | ✅ |
| 57 | CurriculumHeaderDPEOCurriculumFormatCode | CURRICULUM_FORMAT_CODE | — | — |
| 58 | CurriculumHeaderDPEOCurriculumId | CURRICULUM_ID | — | ✅ |
| 59 | CurriculumHeaderDPEOCurriculumItemLastUpdate | CURRICULUM_ITEM_LAST_UPDATE | — | — |
| 60 | CurriculumHeaderDPEOCurriculumLongDescr | CURRICULUM_LONG_DESCR | — | — |
| 61 | CurriculumHeaderDPEOCurriculumName | CURRICULUM_NAME | — | ✅ |
| 62 | CurriculumHeaderDPEOCurriculumStatusCode | CURRICULUM_STATUS_CODE | — | — |
| 63 | CurriculumHeaderDPEOCurriculumTitle | CURRICULUM_TITLE | — | ✅ |
| 64 | CurriculumHeaderDPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 65 | CurriculumHeaderDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 66 | CurriculumHeaderDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 67 | CurriculumHeaderDPEOEnableOsnFlag | ENABLE_OSN_FLAG | — | — |
| 68 | CurriculumHeaderDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | CurriculumHeaderDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | CurriculumHeaderDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | CurriculumHeaderDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 72 | CurriculumHeaderDPEOSearchEnabledFlag | SEARCH_ENABLED_FLAG | — | — |
| 73 | CurriculumHeaderDPEOSystemStatusCode | SYSTEM_STATUS_CODE | — | ✅ |
| 74 | CurriculumHeaderDPEOTemplateId | TEMPLATE_ID | — | — |
| 75 | CurriculumHeaderDPEOWishlistEnabledFlag | WISHLIST_ENABLED_FLAG | — | — |

### [[her_curriculum_type_vl|HER_CURRICULUM_TYPE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumTypePEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | CurriculumTypePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | CurriculumTypePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | CurriculumTypePEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | CurriculumTypePEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | CurriculumTypePEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | CurriculumTypePEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | CurriculumTypePEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | CurriculumTypePEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | CurriculumTypePEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | CurriculumTypePEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | CurriculumTypePEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | CurriculumTypePEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | CurriculumTypePEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | CurriculumTypePEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | CurriculumTypePEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | CurriculumTypePEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | CurriculumTypePEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | CurriculumTypePEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | CurriculumTypePEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | CurriculumTypePEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | CurriculumTypePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | CurriculumTypePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | CurriculumTypePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | CurriculumTypePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | CurriculumTypePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | CurriculumTypePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | CurriculumTypePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | CurriculumTypePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | CurriculumTypePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | CurriculumTypePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | CurriculumTypePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | CurriculumTypePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | CurriculumTypePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | CurriculumTypePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | CurriculumTypePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | CurriculumTypePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | CurriculumTypePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | CurriculumTypePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | CurriculumTypePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | CurriculumTypePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | CurriculumTypePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | CurriculumTypePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | CurriculumTypePEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | CurriculumTypePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | CurriculumTypePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | CurriculumTypePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | CurriculumTypePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | CurriculumTypePEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | CurriculumTypePEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | CurriculumTypePEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | CurriculumTypePEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | CurriculumTypePEOCartEnabledFlag | CART_ENABLED_FLAG | — | — |
| 54 | CurriculumTypePEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumTypePEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumTypePEOCurriculumLevel | CURRICULUM_LEVEL | — | — |
| 57 | CurriculumTypePEOCurriculumType | CURRICULUM_TYPE | — | — |
| 58 | CurriculumTypePEOCurriculumTypeDescription | CURRICULUM_TYPE_DESCRIPTION | — | — |
| 59 | CurriculumTypePEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 60 | CurriculumTypePEOCurriculumTypeName | CURRICULUM_TYPE_NAME | — | — |
| 61 | CurriculumTypePEODateEffectiveFlag | DATE_EFFECTIVE_FLAG | — | — |
| 62 | CurriculumTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | CurriculumTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | CurriculumTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 65 | CurriculumTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 66 | CurriculumTypePEOSearchEnabledFlag | SEARCH_ENABLED_FLAG | — | — |
| 67 | CurriculumTypePEOSeedDataLock | SEED_DATA_LOCK | — | — |
| 68 | CurriculumTypePEOSelfReferenceFlag | SELF_REFERENCE_FLAG | — | — |

### [[her_curric_group|HER_CURRIC_GROUP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumGroupPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CurriculumGroupPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CurriculumGroupPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CurriculumGroupPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CurriculumGroupPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CurriculumGroupPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CurriculumGroupPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CurriculumGroupPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | CurriculumGroupPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | CurriculumGroupPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | CurriculumGroupPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | CurriculumGroupPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | CurriculumGroupPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | CurriculumGroupPEOAttribute3 | ATTRIBUTE3 | — | — |
| 15 | CurriculumGroupPEOAttribute4 | ATTRIBUTE4 | — | — |
| 16 | CurriculumGroupPEOAttribute5 | ATTRIBUTE5 | — | — |
| 17 | CurriculumGroupPEOAttribute6 | ATTRIBUTE6 | — | — |
| 18 | CurriculumGroupPEOAttribute7 | ATTRIBUTE7 | — | — |
| 19 | CurriculumGroupPEOAttribute8 | ATTRIBUTE8 | — | — |
| 20 | CurriculumGroupPEOAttribute9 | ATTRIBUTE9 | — | — |
| 21 | CurriculumGroupPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | CurriculumGroupPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | CurriculumGroupPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | CurriculumGroupPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | CurriculumGroupPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | CurriculumGroupPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | CurriculumGroupPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | CurriculumGroupPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | CurriculumGroupPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | CurriculumGroupPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | CurriculumGroupPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | CurriculumGroupPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | CurriculumGroupPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | CurriculumGroupPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | CurriculumGroupPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | CurriculumGroupPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | CurriculumGroupPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | CurriculumGroupPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | CurriculumGroupPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | CurriculumGroupPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | CurriculumGroupPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | CurriculumGroupPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | CurriculumGroupPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | CurriculumGroupPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | CurriculumGroupPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | CurriculumGroupPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | CurriculumGroupPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | CurriculumGroupPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | CurriculumGroupPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | CurriculumGroupPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | CurriculumGroupPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | CurriculumGroupPEOCreatedBy | CREATED_BY | — | — |
| 53 | CurriculumGroupPEOCreationDate | CREATION_DATE | — | — |
| 54 | CurriculumGroupPEOCurriculumGroupId | CURRICULUM_GROUP_ID | — | — |
| 55 | CurriculumGroupPEOCurriculumHeaderId | CURRICULUM_HEADER_ID | — | — |
| 56 | CurriculumGroupPEODefaultPlanFormatId | DEFAULT_PLAN_FORMAT_ID | — | — |
| 57 | CurriculumGroupPEOGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 58 | CurriculumGroupPEOGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 59 | CurriculumGroupPEOGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 60 | CurriculumGroupPEOGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 61 | CurriculumGroupPEOGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 62 | CurriculumGroupPEOGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 63 | CurriculumGroupPEOGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 64 | CurriculumGroupPEOGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 65 | CurriculumGroupPEOGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 66 | CurriculumGroupPEOGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 67 | CurriculumGroupPEOGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 68 | CurriculumGroupPEOGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 69 | CurriculumGroupPEOGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 70 | CurriculumGroupPEOGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 71 | CurriculumGroupPEOGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 72 | CurriculumGroupPEOGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 73 | CurriculumGroupPEOGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 74 | CurriculumGroupPEOGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 75 | CurriculumGroupPEOGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 76 | CurriculumGroupPEOGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 77 | CurriculumGroupPEOGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 78 | CurriculumGroupPEOGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 79 | CurriculumGroupPEOGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | — |
| 80 | CurriculumGroupPEOGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 81 | CurriculumGroupPEOGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 82 | CurriculumGroupPEOGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 83 | CurriculumGroupPEOGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 84 | CurriculumGroupPEOGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | — |
| 85 | CurriculumGroupPEOGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | — |
| 86 | CurriculumGroupPEOGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | — |
| 87 | CurriculumGroupPEOGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | — |
| 88 | CurriculumGroupPEOGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 89 | CurriculumGroupPEOGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 90 | CurriculumGroupPEOGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 91 | CurriculumGroupPEOGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 92 | CurriculumGroupPEOGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 93 | CurriculumGroupPEOGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 94 | CurriculumGroupPEOGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 95 | CurriculumGroupPEOGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 96 | CurriculumGroupPEOGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 97 | CurriculumGroupPEOGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 98 | CurriculumGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 99 | CurriculumGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 100 | CurriculumGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 101 | CurriculumGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[her_curric_header_vl|HER_CURRIC_HEADER_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumHeaderDPEOCurriculumHeaderId | CURRICULUM_HEADER_ID | 🔑 | ✅ |
| 2 | CurriculumHeaderDPEOCurriculumNameCode | CURRICULUM_NAME_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
