---
id: DOC-OTHER-PVO-FNDValuesP1
doc_type: system-doc
title: "FNDValuesP1 — PVO Cross-Module"
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
  - FNDValuesP1
  - fndvaluesp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FNDValuesP1

## 📌 Visão Geral

View Object para extração BICC de dados de FNDValues P1. Acessa as tabelas: EGP_CATEGORY_SETS_B, FND_KF_SEGMENTS_B, FND_KF_SEGMENTS_TL (+6).

**Caminho:** `FscmTopModelAM.CatalogAM.FNDValuesP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 155 | 9 | 6 | 20 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[egp_category_sets_b|EGP_CATEGORY_SETS_B]] — 34 atributos (1 PKs, 1 BICC)
- [[fnd_kf_segments_b|FND_KF_SEGMENTS_B]] — 12 atributos (1 PKs, 2 BICC)
- [[fnd_kf_segments_tl|FND_KF_SEGMENTS_TL]] — 7 atributos (1 PKs, 1 BICC)
- [[fnd_kf_segment_instances|FND_KF_SEGMENT_INSTANCES]] — 14 atributos (1 BICC)
- [[fnd_kf_str_instances_b|FND_KF_STR_INSTANCES_B]] — 12 atributos (1 BICC)
- [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]] — 6 atributos (1 PKs, 1 BICC)
- [[fnd_vs_values_b|FND_VS_VALUES_B]] — 44 atributos (1 PKs, 9 BICC)
- [[fnd_vs_values_tl|FND_VS_VALUES_TL]] — 4 atributos (1 PKs, 2 BICC)
- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 22 atributos (2 BICC)

---

## ⚙️ Atributos

### [[egp_category_sets_b|EGP_CATEGORY_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogBasePEOCatalogCode | CATALOG_CODE | — | — |
| 2 | CatalogBasePEOCatalogContentCode | CATALOG_CONTENT_CODE | — | — |
| 3 | CatalogBasePEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 4 | CatalogBasePEOControlLevel | CONTROL_LEVEL | — | — |
| 5 | CatalogBasePEOControlLevelUpdateableFlag | CONTROL_LEVEL_UPDATEABLE_FLAG | — | — |
| 6 | CatalogBasePEOCreatedBy | CREATED_BY | — | — |
| 7 | CatalogBasePEOCreationDate | CREATION_DATE | — | — |
| 8 | CatalogBasePEODefaultCategoryId | DEFAULT_CATEGORY_ID | — | — |
| 9 | CatalogBasePEOEndDate | END_DATE | — | — |
| 10 | CatalogBasePEOHierarchyEnabled | HIERARCHY_ENABLED | — | — |
| 11 | CatalogBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | CatalogBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | CatalogBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | CatalogBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | CatalogBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | CatalogBasePEOMultItemCatAssignFlag | MULT_ITEM_CAT_ASSIGN_FLAG | — | — |
| 17 | CatalogBasePEOMultItemCatUpdateableFlag | MULT_ITEM_CAT_UPDATEABLE_FLAG | — | — |
| 18 | CatalogBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | CatalogBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 20 | CatalogBasePEOProgramName | PROGRAM_NAME | — | — |
| 21 | CatalogBasePEORaiseAltCatHierChgEvent | RAISE_ALT_CAT_HIER_CHG_EVENT | — | — |
| 22 | CatalogBasePEORaiseCatalogCatChgEvent | RAISE_CATALOG_CAT_CHG_EVENT | — | — |
| 23 | CatalogBasePEORaiseItemCatAssignEvent | RAISE_ITEM_CAT_ASSIGN_EVENT | — | — |
| 24 | CatalogBasePEORequestId | REQUEST_ID | — | — |
| 25 | CatalogBasePEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 26 | CatalogBasePEOSharingContentCode | SHARING_CONTENT_CODE | — | — |
| 27 | CatalogBasePEOSharingControlCode | SHARING_CONTROL_CODE | — | — |
| 28 | CatalogBasePEOSourceCategorySetId | SOURCE_CATEGORY_SET_ID | — | — |
| 29 | CatalogBasePEOStartDate | START_DATE | — | — |
| 30 | CatalogBasePEOStatusFlag | STATUS_FLAG | — | — |
| 31 | CatalogBasePEOStructureId | STRUCTURE_ID | — | — |
| 32 | CatalogBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 33 | CatalogBasePEOValidateFlag | VALIDATE_FLAG | — | — |
| 34 | CatalogBasePEOValidateFlagUpdateableFlag | VALIDATE_FLAG_UPDATEABLE_FLAG | — | — |

### [[fnd_kf_segments_b|FND_KF_SEGMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldSegmentPEOColumnName | COLUMN_NAME | 🔑 | ✅ |
| 2 | KeyFlexfieldSegmentPEOCreatedBy | CREATED_BY | — | — |
| 3 | KeyFlexfieldSegmentPEOCreationDate | CREATION_DATE | — | — |
| 4 | KeyFlexfieldSegmentPEODisplayWidth | DISPLAY_WIDTH | — | — |
| 5 | KeyFlexfieldSegmentPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | KeyFlexfieldSegmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | KeyFlexfieldSegmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | KeyFlexfieldSegmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | KeyFlexfieldSegmentPEORangeType | RANGE_TYPE | — | — |
| 10 | KeyFlexfieldSegmentPEOSegmentCode | SEGMENT_CODE | — | ✅ |
| 11 | KeyFlexfieldSegmentPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 12 | KeyFlexfieldSegmentPEOStructureId | STRUCTURE_ID | — | — |

### [[fnd_kf_segments_tl|FND_KF_SEGMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexSegmentsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 2 | KeyFlexSegmentsTLPEOSegmentCode | SEGMENT_CODE | — | — |
| 3 | KeyFlexSegmentsTLPEOStructureId | STRUCTURE_ID | — | — |
| 4 | KeyFlexfieldSegmentPEODescription | DESCRIPTION | — | — |
| 5 | KeyFlexfieldSegmentPEOName | NAME | — | — |
| 6 | KeyFlexfieldSegmentPEOPrompt | PROMPT | — | — |
| 7 | KeyFlexfieldSegmentPEOShortPrompt | SHORT_PROMPT | — | — |

### [[fnd_kf_segment_instances|FND_KF_SEGMENT_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldSegmentInstanceP1BIEnabledFlag | BI_ENABLED_FLAG | — | — |
| 2 | KeyFlexfieldSegmentInstanceP1CreatedBy | CREATED_BY | — | — |
| 3 | KeyFlexfieldSegmentInstanceP1CreationDate | CREATION_DATE | — | — |
| 4 | KeyFlexfieldSegmentInstanceP1DefaultType | DEFAULT_TYPE | — | — |
| 5 | KeyFlexfieldSegmentInstanceP1DefaultValue | DEFAULT_VALUE | — | — |
| 6 | KeyFlexfieldSegmentInstanceP1DisplayFlag | DISPLAY_FLAG | — | — |
| 7 | KeyFlexfieldSegmentInstanceP1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | KeyFlexfieldSegmentInstanceP1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | KeyFlexfieldSegmentInstanceP1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | KeyFlexfieldSegmentInstanceP1RequiredFlag | REQUIRED_FLAG | — | — |
| 11 | KeyFlexfieldSegmentInstanceP1SegmentCode | SEGMENT_CODE | — | ✅ |
| 12 | KeyFlexfieldSegmentInstanceP1StructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 13 | KeyFlexfieldSegmentInstanceP1TreeCode | TREE_CODE | — | — |
| 14 | KeyFlexfieldSegmentInstanceP1ValueSetId | VALUE_SET_ID | — | — |

### [[fnd_kf_str_instances_b|FND_KF_STR_INSTANCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldStructureInstanc1ApplicationId | APPLICATION_ID | — | — |
| 2 | KeyFlexfieldStructureInstanc1CreatedBy | CREATED_BY | — | — |
| 3 | KeyFlexfieldStructureInstanc1CreationDate | CREATION_DATE | — | — |
| 4 | KeyFlexfieldStructureInstanc1EnabledFlag | ENABLED_FLAG | — | — |
| 5 | KeyFlexfieldStructureInstanc1KeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | ✅ |
| 6 | KeyFlexfieldStructureInstanc1LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | KeyFlexfieldStructureInstanc1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | KeyFlexfieldStructureInstanc1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | KeyFlexfieldStructureInstanc1StructureId | STRUCTURE_ID | — | — |
| 10 | KeyFlexfieldStructureInstanc1StructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | — |
| 11 | KeyFlexfieldStructureInstanc1StructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 12 | KeyFlexfieldStructureInstanc1StructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |

### [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexStructureInstancesTLP1ApplicationId | APPLICATION_ID | — | — |
| 2 | KeyFlexStructureInstancesTLP1KeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | — |
| 3 | KeyFlexStructureInstancesTLP1Language | LANGUAGE | 🔑 | ✅ |
| 4 | KeyFlexStructureInstancesTLP1StructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | — |
| 5 | KeyFlexfieldStructureInstanc1Description | DESCRIPTION | — | — |
| 6 | KeyFlexfieldStructureInstanc1Name | NAME | — | — |

### [[fnd_vs_values_b|FND_VS_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueId | VALUE_ID | 🔑 | ✅ |
| 2 | ValueSetValuePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ValueSetValuePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ValueSetValuePEOCustomValueAttribute1 | CUSTOM_VALUE_ATTRIBUTE1 | — | — |
| 5 | ValueSetValuePEOCustomValueAttribute10 | CUSTOM_VALUE_ATTRIBUTE10 | — | — |
| 6 | ValueSetValuePEOCustomValueAttribute2 | CUSTOM_VALUE_ATTRIBUTE2 | — | — |
| 7 | ValueSetValuePEOCustomValueAttribute3 | CUSTOM_VALUE_ATTRIBUTE3 | — | — |
| 8 | ValueSetValuePEOCustomValueAttribute4 | CUSTOM_VALUE_ATTRIBUTE4 | — | — |
| 9 | ValueSetValuePEOCustomValueAttribute5 | CUSTOM_VALUE_ATTRIBUTE5 | — | — |
| 10 | ValueSetValuePEOCustomValueAttribute6 | CUSTOM_VALUE_ATTRIBUTE6 | — | — |
| 11 | ValueSetValuePEOCustomValueAttribute7 | CUSTOM_VALUE_ATTRIBUTE7 | — | — |
| 12 | ValueSetValuePEOCustomValueAttribute8 | CUSTOM_VALUE_ATTRIBUTE8 | — | — |
| 13 | ValueSetValuePEOCustomValueAttribute9 | CUSTOM_VALUE_ATTRIBUTE9 | — | — |
| 14 | ValueSetValuePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 15 | ValueSetValuePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 16 | ValueSetValuePEOFlexValueAttribute1 | FLEX_VALUE_ATTRIBUTE1 | — | — |
| 17 | ValueSetValuePEOFlexValueAttribute10 | FLEX_VALUE_ATTRIBUTE10 | — | — |
| 18 | ValueSetValuePEOFlexValueAttribute11 | FLEX_VALUE_ATTRIBUTE11 | — | — |
| 19 | ValueSetValuePEOFlexValueAttribute12 | FLEX_VALUE_ATTRIBUTE12 | — | — |
| 20 | ValueSetValuePEOFlexValueAttribute13 | FLEX_VALUE_ATTRIBUTE13 | — | — |
| 21 | ValueSetValuePEOFlexValueAttribute14 | FLEX_VALUE_ATTRIBUTE14 | — | — |
| 22 | ValueSetValuePEOFlexValueAttribute15 | FLEX_VALUE_ATTRIBUTE15 | — | — |
| 23 | ValueSetValuePEOFlexValueAttribute16 | FLEX_VALUE_ATTRIBUTE16 | — | — |
| 24 | ValueSetValuePEOFlexValueAttribute17 | FLEX_VALUE_ATTRIBUTE17 | — | — |
| 25 | ValueSetValuePEOFlexValueAttribute18 | FLEX_VALUE_ATTRIBUTE18 | — | — |
| 26 | ValueSetValuePEOFlexValueAttribute19 | FLEX_VALUE_ATTRIBUTE19 | — | — |
| 27 | ValueSetValuePEOFlexValueAttribute2 | FLEX_VALUE_ATTRIBUTE2 | — | — |
| 28 | ValueSetValuePEOFlexValueAttribute20 | FLEX_VALUE_ATTRIBUTE20 | — | — |
| 29 | ValueSetValuePEOFlexValueAttribute3 | FLEX_VALUE_ATTRIBUTE3 | — | — |
| 30 | ValueSetValuePEOFlexValueAttribute4 | FLEX_VALUE_ATTRIBUTE4 | — | — |
| 31 | ValueSetValuePEOFlexValueAttribute5 | FLEX_VALUE_ATTRIBUTE5 | — | — |
| 32 | ValueSetValuePEOFlexValueAttribute6 | FLEX_VALUE_ATTRIBUTE6 | — | — |
| 33 | ValueSetValuePEOFlexValueAttribute7 | FLEX_VALUE_ATTRIBUTE7 | — | — |
| 34 | ValueSetValuePEOFlexValueAttribute8 | FLEX_VALUE_ATTRIBUTE8 | — | — |
| 35 | ValueSetValuePEOFlexValueAttribute9 | FLEX_VALUE_ATTRIBUTE9 | — | — |
| 36 | ValueSetValuePEOIndependentValue | INDEPENDENT_VALUE | — | ✅ |
| 37 | ValueSetValuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | ValueSetValuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | ValueSetValuePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | ValueSetValuePEOSortOrder | SORT_ORDER | — | — |
| 41 | ValueSetValuePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 42 | ValueSetValuePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 43 | ValueSetValuePEOValue | VALUE | — | ✅ |
| 44 | ValueSetValuePEOValueSetId | VALUE_SET_ID | — | — |

### [[fnd_vs_values_tl|FND_VS_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetValuePEODescription | DESCRIPTION | — | ✅ |
| 2 | ValueSetValuePEOTranslatedValue | TRANSLATED_VALUE | — | — |
| 3 | ValueSetValuesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ValueSetValuesTLPEOValueId | VALUE_ID | — | — |

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetPEOCreatedBy | CREATED_BY | — | — |
| 2 | ValueSetPEOCreationDate | CREATION_DATE | — | — |
| 3 | ValueSetPEODataSecurityObjectName | DATA_SECURITY_OBJECT_NAME | — | — |
| 4 | ValueSetPEODescription | DESCRIPTION | — | — |
| 5 | ValueSetPEOIndependentValueSetId | INDEPENDENT_VALUE_SET_ID | — | — |
| 6 | ValueSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ValueSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ValueSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ValueSetPEOMaximumLength | MAXIMUM_LENGTH | — | — |
| 10 | ValueSetPEOMaximumValue | MAXIMUM_VALUE | — | — |
| 11 | ValueSetPEOMinimumValue | MINIMUM_VALUE | — | — |
| 12 | ValueSetPEOModuleId | MODULE_ID | — | — |
| 13 | ValueSetPEOPrecision | PRECISION | — | — |
| 14 | ValueSetPEOScale | SCALE | — | — |
| 15 | ValueSetPEOSecurityEnabledFlag | SECURITY_ENABLED_FLAG | — | — |
| 16 | ValueSetPEOUppercaseOnlyFlag | UPPERCASE_ONLY_FLAG | — | — |
| 17 | ValueSetPEOValidationType | VALIDATION_TYPE | — | ✅ |
| 18 | ValueSetPEOValueDataType | VALUE_DATA_TYPE | — | — |
| 19 | ValueSetPEOValueSetCode | VALUE_SET_CODE | — | — |
| 20 | ValueSetPEOValueSetId | VALUE_SET_ID | — | — |
| 21 | ValueSetPEOValueSubtype | VALUE_SUBTYPE | — | — |
| 22 | ValueSetPEOZeroFillFlag | ZERO_FILL_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
