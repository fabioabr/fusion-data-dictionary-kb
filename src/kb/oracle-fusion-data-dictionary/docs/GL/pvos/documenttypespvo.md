---
id: DOC-GL-PVO-DocumentTypesPVO
doc_type: system-doc
title: "DocumentTypesPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DocumentTypesPVO
  - documenttypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DocumentTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Document Types. Acessa as tabelas: FND_APPL_TAXONOMY_VL, HR_DOCUMENT_TYPES_B, HR_DOCUMENT_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DocumentOfRecordsAM.DocumentTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 143 | 3 | 1 | 27 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_appl_taxonomy_vl|FND_APPL_TAXONOMY_VL]] — 2 atributos
- [[hr_document_types_b|HR_DOCUMENT_TYPES_B]] — 120 atributos (1 PKs, 23 BICC)
- [[hr_document_types_tl|HR_DOCUMENT_TYPES_TL]] — 21 atributos (4 BICC)

---

## ⚙️ Atributos

### [[fnd_appl_taxonomy_vl|FND_APPL_TAXONOMY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplTaxonomyPEOModuleId | MODULE_ID | — | — |
| 2 | ApplTaxonomyPEOModuleName | MODULE_NAME | — | — |

### [[hr_document_types_b|HR_DOCUMENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BiReportPath | BI_REPORT_PATH | — | ✅ |
| 2 | DocumentTypeId | DOCUMENT_TYPE_ID | 🔑 | ✅ |
| 3 | DocumentTypeLevel | DOCUMENT_TYPE_LEVEL | — | ✅ |
| 4 | DocumentTypesPEOActiveInactiveFlag | ACTIVE_INACTIVE_FLAG | — | ✅ |
| 5 | DocumentTypesPEOArchiveCriteriaBasis | ARCHIVE_CRITERIA_BASIS | — | — |
| 6 | DocumentTypesPEOArchiveCriteriaDays | ARCHIVE_CRITERIA_DAYS | — | — |
| 7 | DocumentTypesPEOAuthorizationRequired | AUTHORIZATION_REQUIRED | — | ✅ |
| 8 | DocumentTypesPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 9 | DocumentTypesPEOCommentsRequired | COMMENTS_REQUIRED | — | — |
| 10 | DocumentTypesPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | DocumentTypesPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | DocumentTypesPEODateFromRequired | DATE_FROM_REQUIRED | — | — |
| 13 | DocumentTypesPEODateToRequired | DATE_TO_REQUIRED | — | — |
| 14 | DocumentTypesPEODffCtxSegDefaultValue | DFF_CTX_SEG_DEFAULT_VALUE | — | — |
| 15 | DocumentTypesPEODffCtxSegDisplayPref | DFF_CTX_SEG_DISPLAY_PREF | — | — |
| 16 | DocumentTypesPEODffGlbSegDisplayPref | DFF_GLB_SEG_DISPLAY_PREF | — | — |
| 17 | DocumentTypesPEODocumentNameRequired | DOCUMENT_NAME_REQUIRED | — | — |
| 18 | DocumentTypesPEODocumentNumberRequired | DOCUMENT_NUMBER_REQUIRED | — | — |
| 19 | DocumentTypesPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 20 | DocumentTypesPEOHierarchyCode | HIERARCHY_CODE | — | ✅ |
| 21 | DocumentTypesPEOIssuedDateRequired | ISSUED_DATE_REQUIRED | — | — |
| 22 | DocumentTypesPEOIssuingAuthorityRequired | ISSUING_AUTHORITY_REQUIRED | — | — |
| 23 | DocumentTypesPEOIssuingCountryRequired | ISSUING_COUNTRY_REQUIRED | — | — |
| 24 | DocumentTypesPEOIssuingLocationRequired | ISSUING_LOCATION_REQUIRED | — | — |
| 25 | DocumentTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | DocumentTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | DocumentTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | DocumentTypesPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 29 | DocumentTypesPEOLockCreateRoleList | LOCK_CREATE_ROLE_LIST | — | — |
| 30 | DocumentTypesPEOLockDeleteRoleList | LOCK_DELETE_ROLE_LIST | — | — |
| 31 | DocumentTypesPEOLockUpdateRoleList | LOCK_UPDATE_ROLE_LIST | — | — |
| 32 | DocumentTypesPEOModuleId | MODULE_ID | — | — |
| 33 | DocumentTypesPEOMultipleOccurencesFlag | MULTIPLE_OCCURENCES_FLAG | — | ✅ |
| 34 | DocumentTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | DocumentTypesPEOPublishRequired | PUBLISH_REQUIRED | — | ✅ |
| 36 | DocumentTypesPEOPurgeArchiveCriteriaDays | PURGE_ARCHIVE_CRITERIA_DAYS | — | — |
| 37 | DocumentTypesPEOSubCategoryCode | SUB_CATEGORY_CODE | — | — |
| 38 | DocumentTypesPEOSystemDocumentType | SYSTEM_DOCUMENT_TYPE | — | ✅ |
| 39 | DocumentTypesPEOTagList | TAG_LIST | — | — |
| 40 | DocumentTypesPEOWarningPeriod | WARNING_PERIOD | — | ✅ |
| 41 | DtAttribute1 | DT_ATTRIBUTE1 | — | — |
| 42 | DtAttribute10 | DT_ATTRIBUTE10 | — | — |
| 43 | DtAttribute2 | DT_ATTRIBUTE2 | — | — |
| 44 | DtAttribute3 | DT_ATTRIBUTE3 | — | — |
| 45 | DtAttribute4 | DT_ATTRIBUTE4 | — | — |
| 46 | DtAttribute5 | DT_ATTRIBUTE5 | — | — |
| 47 | DtAttribute6 | DT_ATTRIBUTE6 | — | — |
| 48 | DtAttribute7 | DT_ATTRIBUTE7 | — | — |
| 49 | DtAttribute8 | DT_ATTRIBUTE8 | — | — |
| 50 | DtAttribute9 | DT_ATTRIBUTE9 | — | — |
| 51 | DtAttributeCategory | DT_ATTRIBUTE_CATEGORY | — | — |
| 52 | DtAttributeDate1 | DT_ATTRIBUTE_DATE1 | — | — |
| 53 | DtAttributeDate10 | DT_ATTRIBUTE_DATE10 | — | — |
| 54 | DtAttributeDate2 | DT_ATTRIBUTE_DATE2 | — | — |
| 55 | DtAttributeDate3 | DT_ATTRIBUTE_DATE3 | — | — |
| 56 | DtAttributeDate4 | DT_ATTRIBUTE_DATE4 | — | — |
| 57 | DtAttributeDate5 | DT_ATTRIBUTE_DATE5 | — | — |
| 58 | DtAttributeDate6 | DT_ATTRIBUTE_DATE6 | — | — |
| 59 | DtAttributeDate7 | DT_ATTRIBUTE_DATE7 | — | — |
| 60 | DtAttributeDate8 | DT_ATTRIBUTE_DATE8 | — | — |
| 61 | DtAttributeDate9 | DT_ATTRIBUTE_DATE9 | — | — |
| 62 | DtAttributeNumber1 | DT_ATTRIBUTE_NUMBER1 | — | — |
| 63 | DtAttributeNumber10 | DT_ATTRIBUTE_NUMBER10 | — | — |
| 64 | DtAttributeNumber2 | DT_ATTRIBUTE_NUMBER2 | — | — |
| 65 | DtAttributeNumber3 | DT_ATTRIBUTE_NUMBER3 | — | — |
| 66 | DtAttributeNumber4 | DT_ATTRIBUTE_NUMBER4 | — | — |
| 67 | DtAttributeNumber5 | DT_ATTRIBUTE_NUMBER5 | — | — |
| 68 | DtAttributeNumber6 | DT_ATTRIBUTE_NUMBER6 | — | — |
| 69 | DtAttributeNumber7 | DT_ATTRIBUTE_NUMBER7 | — | — |
| 70 | DtAttributeNumber8 | DT_ATTRIBUTE_NUMBER8 | — | — |
| 71 | DtAttributeNumber9 | DT_ATTRIBUTE_NUMBER9 | — | — |
| 72 | DtAttributeTimestamp1 | DT_ATTRIBUTE_TIMESTAMP1 | — | — |
| 73 | DtAttributeTimestamp2 | DT_ATTRIBUTE_TIMESTAMP2 | — | — |
| 74 | DtAttributeTimestamp3 | DT_ATTRIBUTE_TIMESTAMP3 | — | — |
| 75 | DtAttributeTimestamp4 | DT_ATTRIBUTE_TIMESTAMP4 | — | — |
| 76 | DtAttributeTimestamp5 | DT_ATTRIBUTE_TIMESTAMP5 | — | — |
| 77 | DtInformation1 | DT_INFORMATION1 | — | — |
| 78 | DtInformation10 | DT_INFORMATION10 | — | — |
| 79 | DtInformation2 | DT_INFORMATION2 | — | — |
| 80 | DtInformation3 | DT_INFORMATION3 | — | — |
| 81 | DtInformation4 | DT_INFORMATION4 | — | — |
| 82 | DtInformation5 | DT_INFORMATION5 | — | — |
| 83 | DtInformation6 | DT_INFORMATION6 | — | — |
| 84 | DtInformation7 | DT_INFORMATION7 | — | — |
| 85 | DtInformation8 | DT_INFORMATION8 | — | — |
| 86 | DtInformation9 | DT_INFORMATION9 | — | — |
| 87 | DtInformationCategory | DT_INFORMATION_CATEGORY | — | — |
| 88 | DtInformationDate1 | DT_INFORMATION_DATE1 | — | — |
| 89 | DtInformationDate10 | DT_INFORMATION_DATE10 | — | — |
| 90 | DtInformationDate2 | DT_INFORMATION_DATE2 | — | — |
| 91 | DtInformationDate3 | DT_INFORMATION_DATE3 | — | — |
| 92 | DtInformationDate4 | DT_INFORMATION_DATE4 | — | — |
| 93 | DtInformationDate5 | DT_INFORMATION_DATE5 | — | — |
| 94 | DtInformationDate6 | DT_INFORMATION_DATE6 | — | — |
| 95 | DtInformationDate7 | DT_INFORMATION_DATE7 | — | — |
| 96 | DtInformationDate8 | DT_INFORMATION_DATE8 | — | — |
| 97 | DtInformationDate9 | DT_INFORMATION_DATE9 | — | — |
| 98 | DtInformationNumber1 | DT_INFORMATION_NUMBER1 | — | — |
| 99 | DtInformationNumber10 | DT_INFORMATION_NUMBER10 | — | — |
| 100 | DtInformationNumber2 | DT_INFORMATION_NUMBER2 | — | — |
| 101 | DtInformationNumber3 | DT_INFORMATION_NUMBER3 | — | — |
| 102 | DtInformationNumber4 | DT_INFORMATION_NUMBER4 | — | — |
| 103 | DtInformationNumber5 | DT_INFORMATION_NUMBER5 | — | — |
| 104 | DtInformationNumber6 | DT_INFORMATION_NUMBER6 | — | — |
| 105 | DtInformationNumber7 | DT_INFORMATION_NUMBER7 | — | — |
| 106 | DtInformationNumber8 | DT_INFORMATION_NUMBER8 | — | — |
| 107 | DtInformationNumber9 | DT_INFORMATION_NUMBER9 | — | — |
| 108 | DtInformationTimestamp1 | DT_INFORMATION_TIMESTAMP1 | — | — |
| 109 | DtInformationTimestamp2 | DT_INFORMATION_TIMESTAMP2 | — | — |
| 110 | DtInformationTimestamp3 | DT_INFORMATION_TIMESTAMP3 | — | — |
| 111 | DtInformationTimestamp4 | DT_INFORMATION_TIMESTAMP4 | — | — |
| 112 | DtInformationTimestamp5 | DT_INFORMATION_TIMESTAMP5 | — | — |
| 113 | LockCreate | LOCK_CREATE | — | ✅ |
| 114 | LockDelete | LOCK_DELETE | — | ✅ |
| 115 | LockUpdate | LOCK_UPDATE | — | ✅ |
| 116 | MinAttachmentsCount | MIN_ATTACHMENTS_COUNT | — | ✅ |
| 117 | RestrictCreateAttach | RESTRICT_CREATE_ATTACH | — | ✅ |
| 118 | RestrictDeleteAttach | RESTRICT_DELETE_ATTACH | — | ✅ |
| 119 | RestrictUpdateAttach | RESTRICT_UPDATE_ATTACH | — | ✅ |
| 120 | SeedDataSource | SEED_DATA_SOURCE | — | — |

### [[hr_document_types_tl|HR_DOCUMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentTypesTranslationPEOCommentsLabel | COMMENTS_LABEL | — | — |
| 2 | DocumentTypesTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 3 | DocumentTypesTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 4 | DocumentTypesTranslationPEODateFromLabel | DATE_FROM_LABEL | — | — |
| 5 | DocumentTypesTranslationPEODateToLabel | DATE_TO_LABEL | — | — |
| 6 | DocumentTypesTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | DocumentTypesTranslationPEODocumentNameLabel | DOCUMENT_NAME_LABEL | — | — |
| 8 | DocumentTypesTranslationPEODocumentNumberLabel | DOCUMENT_NUMBER_LABEL | — | — |
| 9 | DocumentTypesTranslationPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 10 | DocumentTypesTranslationPEODocumentTypeId1 | DOCUMENT_TYPE_ID | — | — |
| 11 | DocumentTypesTranslationPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 12 | DocumentTypesTranslationPEOIssuedDateLabel | ISSUED_DATE_LABEL | — | — |
| 13 | DocumentTypesTranslationPEOIssuingAuthorityLabel | ISSUING_AUTHORITY_LABEL | — | — |
| 14 | DocumentTypesTranslationPEOIssuingCountryLabel | ISSUING_COUNTRY_LABEL | — | — |
| 15 | DocumentTypesTranslationPEOIssuingLocationLabel | ISSUING_LOCATION_LABEL | — | — |
| 16 | DocumentTypesTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 17 | DocumentTypesTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 18 | DocumentTypesTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 19 | DocumentTypesTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 20 | DocumentTypesTranslationPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 21 | DocumentTypesTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
