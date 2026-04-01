---
id: DOC-OTHER-PVO-StudentProgramDPVO
doc_type: system-doc
title: "StudentProgramDPVO — PVO Cross-Module"
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
  - StudentProgramDPVO
  - studentprogramdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StudentProgramDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Student Program D. Acessa as tabelas: HER_CURRICULUM_HEADER_F_VL, HER_CURRICULUM_PROGRAM, HER_CURRICULUM_TYPE_VL (+6).

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.StudentProgramDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 486 | 9 | 1 | 37 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[her_curriculum_header_f_vl|HER_CURRICULUM_HEADER_F_VL]] — 75 atributos (8 BICC)
- [[her_curriculum_program|HER_CURRICULUM_PROGRAM]] — 67 atributos (3 BICC)
- [[her_curriculum_type_vl|HER_CURRICULUM_TYPE_VL]] — 68 atributos (2 BICC)
- [[her_curric_header_vl|HER_CURRIC_HEADER_VL]] — 2 atributos
- [[her_curric_program|HER_CURRIC_PROGRAM]] — 4 atributos
- [[her_program_type_vl|HER_PROGRAM_TYPE_VL]] — 63 atributos (9 BICC)
- [[her_sct_item|HER_SCT_ITEM]] — 71 atributos (2 BICC)
- [[her_sct_item_status_vl|HER_SCT_ITEM_STATUS_VL]] — 68 atributos (6 BICC)
- [[her_sct_program|HER_SCT_PROGRAM]] — 68 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

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
| 57 | CurriculumHeaderDPEOCurriculumFormatCode | CURRICULUM_FORMAT_CODE | — | ✅ |
| 58 | CurriculumHeaderDPEOCurriculumId | CURRICULUM_ID | — | ✅ |
| 59 | CurriculumHeaderDPEOCurriculumItemLastUpdate | CURRICULUM_ITEM_LAST_UPDATE | — | — |
| 60 | CurriculumHeaderDPEOCurriculumLongDescr | CURRICULUM_LONG_DESCR | — | — |
| 61 | CurriculumHeaderDPEOCurriculumName | CURRICULUM_NAME | — | ✅ |
| 62 | CurriculumHeaderDPEOCurriculumStatusCode | CURRICULUM_STATUS_CODE | — | — |
| 63 | CurriculumHeaderDPEOCurriculumTitle | CURRICULUM_TITLE | — | ✅ |
| 64 | CurriculumHeaderDPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 65 | CurriculumHeaderDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
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

### [[her_curriculum_program|HER_CURRICULUM_PROGRAM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumProgramExtensionPEOAdmissionRequiredFlag | ADMISSION_REQUIRED_FLAG | — | — |
| 2 | CurriculumProgramExtensionPEOAllGroupsFlag | ALL_GROUPS_FLAG | — | — |
| 3 | CurriculumProgramExtensionPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | CurriculumProgramExtensionPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | CurriculumProgramExtensionPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | CurriculumProgramExtensionPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | CurriculumProgramExtensionPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | CurriculumProgramExtensionPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | CurriculumProgramExtensionPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | CurriculumProgramExtensionPEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | CurriculumProgramExtensionPEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | CurriculumProgramExtensionPEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | CurriculumProgramExtensionPEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | CurriculumProgramExtensionPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | CurriculumProgramExtensionPEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | CurriculumProgramExtensionPEOAttribute3 | ATTRIBUTE3 | — | — |
| 17 | CurriculumProgramExtensionPEOAttribute4 | ATTRIBUTE4 | — | — |
| 18 | CurriculumProgramExtensionPEOAttribute5 | ATTRIBUTE5 | — | — |
| 19 | CurriculumProgramExtensionPEOAttribute6 | ATTRIBUTE6 | — | — |
| 20 | CurriculumProgramExtensionPEOAttribute7 | ATTRIBUTE7 | — | — |
| 21 | CurriculumProgramExtensionPEOAttribute8 | ATTRIBUTE8 | — | — |
| 22 | CurriculumProgramExtensionPEOAttribute9 | ATTRIBUTE9 | — | — |
| 23 | CurriculumProgramExtensionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | CurriculumProgramExtensionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | CurriculumProgramExtensionPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | CurriculumProgramExtensionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | CurriculumProgramExtensionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | CurriculumProgramExtensionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | CurriculumProgramExtensionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | CurriculumProgramExtensionPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | CurriculumProgramExtensionPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | CurriculumProgramExtensionPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | CurriculumProgramExtensionPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | CurriculumProgramExtensionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | CurriculumProgramExtensionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | CurriculumProgramExtensionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | CurriculumProgramExtensionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | CurriculumProgramExtensionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | CurriculumProgramExtensionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | CurriculumProgramExtensionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | CurriculumProgramExtensionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | CurriculumProgramExtensionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | CurriculumProgramExtensionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | CurriculumProgramExtensionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | CurriculumProgramExtensionPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | CurriculumProgramExtensionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | CurriculumProgramExtensionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | CurriculumProgramExtensionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | CurriculumProgramExtensionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | CurriculumProgramExtensionPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | CurriculumProgramExtensionPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | CurriculumProgramExtensionPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | CurriculumProgramExtensionPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | CurriculumProgramExtensionPEOCreatedBy | CREATED_BY | — | — |
| 55 | CurriculumProgramExtensionPEOCreationDate | CREATION_DATE | — | — |
| 56 | CurriculumProgramExtensionPEOEnforceRequirementSeqFlag | ENFORCE_REQUIREMENT_SEQ_FLAG | — | — |
| 57 | CurriculumProgramExtensionPEOFirstAdmitDate | FIRST_ADMIT_DATE | — | ✅ |
| 58 | CurriculumProgramExtensionPEOLastAdmitDate | LAST_ADMIT_DATE | — | ✅ |
| 59 | CurriculumProgramExtensionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | CurriculumProgramExtensionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | CurriculumProgramExtensionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | CurriculumProgramExtensionPEOMaxTimespanMeasure | MAX_TIMESPAN_MEASURE | — | — |
| 63 | CurriculumProgramExtensionPEOMaxTimespanQuantity | MAX_TIMESPAN_QUANTITY | — | — |
| 64 | CurriculumProgramExtensionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | CurriculumProgramExtensionPEOProgramTypeId | PROGRAM_TYPE_ID | — | — |
| 66 | CurriculumProgramExtensionPEOTypicalTimespanMeasure | TYPICAL_TIMESPAN_MEASURE | — | — |
| 67 | CurriculumProgramExtensionPEOTypicalTimespanQuantity | TYPICAL_TIMESPAN_QUANTITY | — | — |

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
| 57 | CurriculumTypePEOCurriculumType | CURRICULUM_TYPE | — | ✅ |
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

### [[her_curric_header_vl|HER_CURRIC_HEADER_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumHeaderDPEOCurriculumHeaderId | CURRICULUM_HEADER_ID | — | — |
| 2 | CurriculumHeaderDPEOCurriculumNameCode | CURRICULUM_NAME_CODE | — | — |

### [[her_curric_program|HER_CURRIC_PROGRAM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurriculumProgramExtensionPEOCurriculumHeaderId | CURRICULUM_HEADER_ID | — | — |
| 2 | CurriculumProgramExtensionPEOCurriculumProgramId | CURRICULUM_PROGRAM_ID | — | — |
| 3 | CurriculumProgramExtensionPEOPayToAccessFlag | PAY_TO_ACCESS_FLAG | — | — |
| 4 | CurriculumProgramExtensionPEOStudentLevelDetermination | STUDENT_LEVEL_DETERMINATION | — | — |

### [[her_program_type_vl|HER_PROGRAM_TYPE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProgramTypePEOActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ProgramTypePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ProgramTypePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ProgramTypePEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ProgramTypePEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ProgramTypePEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ProgramTypePEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ProgramTypePEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ProgramTypePEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | ProgramTypePEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | ProgramTypePEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | ProgramTypePEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | ProgramTypePEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | ProgramTypePEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | ProgramTypePEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | ProgramTypePEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | ProgramTypePEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | ProgramTypePEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | ProgramTypePEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | ProgramTypePEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | ProgramTypePEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | ProgramTypePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | ProgramTypePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | ProgramTypePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | ProgramTypePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | ProgramTypePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | ProgramTypePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | ProgramTypePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | ProgramTypePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | ProgramTypePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | ProgramTypePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | ProgramTypePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | ProgramTypePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | ProgramTypePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | ProgramTypePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | ProgramTypePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | ProgramTypePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | ProgramTypePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | ProgramTypePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | ProgramTypePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | ProgramTypePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | ProgramTypePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | ProgramTypePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | ProgramTypePEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | ProgramTypePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | ProgramTypePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | ProgramTypePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | ProgramTypePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | ProgramTypePEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | ProgramTypePEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | ProgramTypePEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | ProgramTypePEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | ProgramTypePEOCreatedBy | CREATED_BY | — | — |
| 54 | ProgramTypePEOCreationDate | CREATION_DATE | — | — |
| 55 | ProgramTypePEODescription | DESCRIPTION | — | ✅ |
| 56 | ProgramTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 57 | ProgramTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 58 | ProgramTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 59 | ProgramTypePEOMainProgramFlag | MAIN_PROGRAM_FLAG | — | ✅ |
| 60 | ProgramTypePEONameDisplay | NAME_DISPLAY | — | ✅ |
| 61 | ProgramTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 62 | ProgramTypePEOProgramTypeCode | PROGRAM_TYPE_CODE | — | ✅ |
| 63 | ProgramTypePEOProgramTypeId | PROGRAM_TYPE_ID | — | ✅ |

### [[her_sct_item|HER_SCT_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctItemPEOAcademicLevelId | ACADEMIC_LEVEL_ID | — | — |
| 2 | SctItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | SctItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | SctItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | SctItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | SctItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | SctItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | SctItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | SctItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | SctItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | SctItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | SctItemPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | SctItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | SctItemPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | SctItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | SctItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | SctItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | SctItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | SctItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | SctItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | SctItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | SctItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | SctItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | SctItemPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | SctItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | SctItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | SctItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | SctItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | SctItemPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | SctItemPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | SctItemPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | SctItemPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | SctItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | SctItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | SctItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | SctItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | SctItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | SctItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | SctItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | SctItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | SctItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | SctItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | SctItemPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | SctItemPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | SctItemPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | SctItemPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | SctItemPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | SctItemPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | SctItemPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | SctItemPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | SctItemPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | SctItemPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | SctItemPEOCampusId | CAMPUS_ID | — | — |
| 54 | SctItemPEOCreatedBy | CREATED_BY | — | — |
| 55 | SctItemPEOCreationDate | CREATION_DATE | — | — |
| 56 | SctItemPEOCurriculumId | CURRICULUM_ID | — | — |
| 57 | SctItemPEOCurriculumTypeId | CURRICULUM_TYPE_ID | — | — |
| 58 | SctItemPEOInstitutionId | INSTITUTION_ID | — | — |
| 59 | SctItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | SctItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | SctItemPEOLastActionId | LAST_ACTION_ID | — | — |
| 62 | SctItemPEOLastActionReasonId | LAST_ACTION_REASON_ID | — | ✅ |
| 63 | SctItemPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 64 | SctItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | SctItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | SctItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | SctItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 68 | SctItemPEORecordStatus | RECORD_STATUS | — | — |
| 69 | SctItemPEORequestId | REQUEST_ID | — | — |
| 70 | SctItemPEOSctItemId | SCT_ITEM_ID | — | — |
| 71 | SctItemPEOStudentPartyId | STUDENT_PARTY_ID | — | — |

### [[her_sct_item_status_vl|HER_SCT_ITEM_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctCurrentItemStatusPEOActionEndDate | ACTION_END_DATE | — | ✅ |
| 2 | SctCurrentItemStatusPEOActionStartDate | ACTION_START_DATE | — | ✅ |
| 3 | SctCurrentItemStatusPEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | SctCurrentItemStatusPEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | SctCurrentItemStatusPEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | SctCurrentItemStatusPEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | SctCurrentItemStatusPEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | SctCurrentItemStatusPEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | SctCurrentItemStatusPEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | SctCurrentItemStatusPEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | SctCurrentItemStatusPEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | SctCurrentItemStatusPEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | SctCurrentItemStatusPEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | SctCurrentItemStatusPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | SctCurrentItemStatusPEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | SctCurrentItemStatusPEOAttribute3 | ATTRIBUTE3 | — | — |
| 17 | SctCurrentItemStatusPEOAttribute4 | ATTRIBUTE4 | — | — |
| 18 | SctCurrentItemStatusPEOAttribute5 | ATTRIBUTE5 | — | — |
| 19 | SctCurrentItemStatusPEOAttribute6 | ATTRIBUTE6 | — | — |
| 20 | SctCurrentItemStatusPEOAttribute7 | ATTRIBUTE7 | — | — |
| 21 | SctCurrentItemStatusPEOAttribute8 | ATTRIBUTE8 | — | — |
| 22 | SctCurrentItemStatusPEOAttribute9 | ATTRIBUTE9 | — | — |
| 23 | SctCurrentItemStatusPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | SctCurrentItemStatusPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | SctCurrentItemStatusPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | SctCurrentItemStatusPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | SctCurrentItemStatusPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | SctCurrentItemStatusPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | SctCurrentItemStatusPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | SctCurrentItemStatusPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | SctCurrentItemStatusPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | SctCurrentItemStatusPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | SctCurrentItemStatusPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | SctCurrentItemStatusPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | SctCurrentItemStatusPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | SctCurrentItemStatusPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | SctCurrentItemStatusPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | SctCurrentItemStatusPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | SctCurrentItemStatusPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | SctCurrentItemStatusPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | SctCurrentItemStatusPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | SctCurrentItemStatusPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | SctCurrentItemStatusPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | SctCurrentItemStatusPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | SctCurrentItemStatusPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | SctCurrentItemStatusPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | SctCurrentItemStatusPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | SctCurrentItemStatusPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | SctCurrentItemStatusPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | SctCurrentItemStatusPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | SctCurrentItemStatusPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | SctCurrentItemStatusPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | SctCurrentItemStatusPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | SctCurrentItemStatusPEOCreatedBy | CREATED_BY | — | — |
| 55 | SctCurrentItemStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 56 | SctCurrentItemStatusPEOItemStatusCode | ITEM_STATUS_CODE | — | ✅ |
| 57 | SctCurrentItemStatusPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 58 | SctCurrentItemStatusPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 59 | SctCurrentItemStatusPEOLastActionReasonId | LAST_ACTION_REASON_ID | — | ✅ |
| 60 | SctCurrentItemStatusPEOLastActionType | LAST_ACTION_TYPE | — | — |
| 61 | SctCurrentItemStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | SctCurrentItemStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | SctCurrentItemStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | SctCurrentItemStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | SctCurrentItemStatusPEORequestId | REQUEST_ID | — | — |
| 66 | SctCurrentItemStatusPEOSctItemId | SCT_ITEM_ID | — | — |
| 67 | SctCurrentItemStatusPEOSctItemStatusId | SCT_ITEM_STATUS_ID | — | — |
| 68 | SctCurrentItemStatusPEOStatusAsOfDate | STATUS_AS_OF_DATE | — | — |

### [[her_sct_program|HER_SCT_PROGRAM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SctProgramPEOAcademicGroupCurriculumId | ACADEMIC_GROUP_CURRICULUM_ID | — | ✅ |
| 2 | SctProgramPEOActiveDate | ACTIVE_DATE | — | ✅ |
| 3 | SctProgramPEOAdmitAcademicPeriodId | ADMIT_ACADEMIC_PERIOD_ID | — | — |
| 4 | SctProgramPEOAdmitDate | ADMIT_DATE | — | — |
| 5 | SctProgramPEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | SctProgramPEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | SctProgramPEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | SctProgramPEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | SctProgramPEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | SctProgramPEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | SctProgramPEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | SctProgramPEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | SctProgramPEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | SctProgramPEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | SctProgramPEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | SctProgramPEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | SctProgramPEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | SctProgramPEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | SctProgramPEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | SctProgramPEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | SctProgramPEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | SctProgramPEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | SctProgramPEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | SctProgramPEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | SctProgramPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | SctProgramPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | SctProgramPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 28 | SctProgramPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 29 | SctProgramPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 30 | SctProgramPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 31 | SctProgramPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 32 | SctProgramPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 33 | SctProgramPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 34 | SctProgramPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 35 | SctProgramPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 36 | SctProgramPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 37 | SctProgramPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 38 | SctProgramPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | SctProgramPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | SctProgramPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | SctProgramPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | SctProgramPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 43 | SctProgramPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 44 | SctProgramPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 45 | SctProgramPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 46 | SctProgramPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 47 | SctProgramPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 48 | SctProgramPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 49 | SctProgramPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 50 | SctProgramPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 51 | SctProgramPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 52 | SctProgramPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 53 | SctProgramPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 54 | SctProgramPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 55 | SctProgramPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 56 | SctProgramPEOCreatedBy | CREATED_BY | — | — |
| 57 | SctProgramPEOCreationDate | CREATION_DATE | — | — |
| 58 | SctProgramPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 59 | SctProgramPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 60 | SctProgramPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | SctProgramPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 62 | SctProgramPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 63 | SctProgramPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | SctProgramPEOProgramStatus | PROGRAM_STATUS | — | ✅ |
| 65 | SctProgramPEOProgramTypeId | PROGRAM_TYPE_ID | — | ✅ |
| 66 | SctProgramPEORequestId | REQUEST_ID | — | ✅ |
| 67 | SctProgramPEORequirementPeriodId | REQUIREMENT_PERIOD_ID | — | — |
| 68 | SctProgramSctItemId | SCT_ITEM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
