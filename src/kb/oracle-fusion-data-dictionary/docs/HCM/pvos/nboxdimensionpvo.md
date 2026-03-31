---
id: DOC-HCM-PVO-NBoxDimensionPVO
doc_type: system-doc
title: "NBoxDimensionPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - NBoxDimensionPVO
  - nboxdimensionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NBoxDimensionPVO

## 📌 Visão Geral

Extrai dimensões do N-Box (matriz 9-box) para reuniões de calibração, com tipos analíticos e itens de conteúdo. Fundamental para configuração de eixos de desempenho vs. potencial.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.NBoxDimensionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 435 | 7 | 12 | 30 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_meetings|HRR_MEETINGS]] — 87 atributos (3 BICC)
- [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]] — 20 atributos (2 PKs, 3 BICC)
- [[hrr_tmpl_analytic_types_tl|HRR_TMPL_ANALYTIC_TYPES_TL]] — 11 atributos (3 PKs, 5 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 134 atributos (2 PKs, 3 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 11 atributos (2 PKs, 3 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (1 PKs, 3 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 158 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeetingPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | MeetingPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | MeetingPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | MeetingPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | MeetingPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | MeetingPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | MeetingPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | MeetingPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | MeetingPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | MeetingPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | MeetingPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | MeetingPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | MeetingPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | MeetingPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | MeetingPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | MeetingPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | MeetingPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | MeetingPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | MeetingPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | MeetingPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | MeetingPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | MeetingPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | MeetingPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | MeetingPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | MeetingPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | MeetingPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | MeetingPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | MeetingPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | MeetingPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | MeetingPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | MeetingPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | MeetingPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | MeetingPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | MeetingPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | MeetingPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | MeetingPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | MeetingPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | MeetingPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | MeetingPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | MeetingPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | MeetingPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | MeetingPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | MeetingPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | MeetingPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | MeetingPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | MeetingPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | MeetingPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | MeetingPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | MeetingPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | MeetingPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | MeetingPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | MeetingPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | MeetingPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | MeetingPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | MeetingPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | MeetingPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | MeetingPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | MeetingPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | MeetingPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | MeetingPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | MeetingPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | MeetingPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | MeetingPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | MeetingPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | MeetingPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | MeetingPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | MeetingPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 68 | MeetingPEOCreatedBy | CREATED_BY | — | — |
| 69 | MeetingPEOCreationDate | CREATION_DATE | — | — |
| 70 | MeetingPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 71 | MeetingPEODataSubmitDate | DATA_SUBMIT_DATE | — | — |
| 72 | MeetingPEODataValidityCode | DATA_VALIDITY_CODE | — | — |
| 73 | MeetingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | MeetingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 75 | MeetingPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 76 | MeetingPEOMeetingDate | MEETING_DATE | — | — |
| 77 | MeetingPEOMeetingFacilitatorNotes | MEETING_FACILITATOR_NOTES | — | — |
| 78 | MeetingPEOMeetingId | MEETING_ID | — | ✅ |
| 79 | MeetingPEOMeetingInstructions | MEETING_INSTRUCTIONS | — | — |
| 80 | MeetingPEOMeetingLeaderId | MEETING_LEADER_ID | — | — |
| 81 | MeetingPEOMeetingOrganizationId | MEETING_ORGANIZATION_ID | — | — |
| 82 | MeetingPEOMeetingPurpose | MEETING_PURPOSE | — | — |
| 83 | MeetingPEOMeetingStatusCode | MEETING_STATUS_CODE | — | — |
| 84 | MeetingPEOMeetingSubmitStatusCode | MEETING_SUBMIT_STATUS_CODE | — | — |
| 85 | MeetingPEOMeetingTitle | MEETING_TITLE | — | ✅ |
| 86 | MeetingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 87 | MeetingPEOPrefReviewQualifierId | PREF_REVIEW_QUALIFIER_ID | — | — |

### [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateAnalyticTypeBPEOAnalyticTypeCode | ANALYTIC_TYPE_CODE | — | — |
| 2 | TemplateAnalyticTypeBPEOAnalyticTypeId | ANALYTIC_TYPE_ID | 🔑 | ✅ |
| 3 | TemplateAnalyticTypeBPEOAnalyticViewMode | ANALYTIC_VIEW_MODE | — | — |
| 4 | TemplateAnalyticTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 5 | TemplateAnalyticTypeBPEOColorSchemeCode | COLOR_SCHEME_CODE | — | — |
| 6 | TemplateAnalyticTypeBPEOCreatedBy | CREATED_BY | — | — |
| 7 | TemplateAnalyticTypeBPEOCreationDate | CREATION_DATE | — | — |
| 8 | TemplateAnalyticTypeBPEODashboardTmplId | DASHBOARD_TMPL_ID | — | — |
| 9 | TemplateAnalyticTypeBPEODefaultViewFlag | DEFAULT_VIEW_FLAG | — | — |
| 10 | TemplateAnalyticTypeBPEOHorizontalAxisCode | HORIZONTAL_AXIS_CODE | — | — |
| 11 | TemplateAnalyticTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | TemplateAnalyticTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | TemplateAnalyticTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | TemplateAnalyticTypeBPEOMetricCode | METRIC_CODE | — | — |
| 15 | TemplateAnalyticTypeBPEOModuleId | MODULE_ID | — | — |
| 16 | TemplateAnalyticTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | SUBMIT_BOX_ASGNMNT_FLAG | — | — |
| 18 | TemplateAnalyticTypeBPEOVerticalAxisCode | VERTICAL_AXIS_CODE | — | — |
| 19 | TemplateAnalyticTypeBPEOViewColumnCount | VIEW_COLUMN_COUNT | — | — |
| 20 | TemplateAnalyticTypeBPEOViewRowCount | VIEW_ROW_COUNT | — | — |

### [[hrr_tmpl_analytic_types_tl|HRR_TMPL_ANALYTIC_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticTypeId | ANALYTIC_TYPE_ID | 🔑 | ✅ |
| 2 | AnalyticViewName | ANALYTIC_VIEW_NAME | — | ✅ |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ContentItemBPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ContentItemBPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ContentItemBPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ContentItemBPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ContentItemBPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ContentItemBPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ContentItemBPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ContentItemBPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ContentItemBPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ContentItemBPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ContentItemBPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ContentItemBPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ContentItemBPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | ContentItemBPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | ContentItemBPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | ContentItemBPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | ContentItemBPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | ContentItemBPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | ContentItemBPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | ContentItemBPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | ContentItemBPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | ContentItemBPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | ContentItemBPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | ContentItemBPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | ContentItemBPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | ContentItemBPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | ContentItemBPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | ContentItemBPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | ContentItemBPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | ContentItemBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | ContentItemBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | ContentItemBPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | ContentItemBPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | ContentItemBPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | ContentItemBPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | ContentItemBPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | ContentItemBPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | ContentItemBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | ContentItemBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | ContentItemBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | ContentItemBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | ContentItemBPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | ContentItemBPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | ContentItemBPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | ContentItemBPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | ContentItemBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | ContentItemBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | ContentItemBPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | ContentItemBPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | ContentItemBPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | ContentItemBPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | ContentItemBPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | ContentItemBPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | ContentItemBPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | ContentItemBPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | ContentItemBPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | ContentItemBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | ContentItemBPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | ContentItemBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | ContentItemBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | ContentItemBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | ContentItemBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | ContentItemBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | ContentItemBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | ContentItemBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 68 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 69 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |
| 70 | ContentItemBPEOContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 71 | ContentItemBPEOContentSupplierCode | CONTENT_SUPPLIER_CODE | — | — |
| 72 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 73 | ContentItemBPEOCountryId | COUNTRY_ID | — | — |
| 74 | ContentItemBPEOCreatedBy | CREATED_BY | — | — |
| 75 | ContentItemBPEOCreationDate | CREATION_DATE | — | — |
| 76 | ContentItemBPEODateFrom | DATE_FROM | — | — |
| 77 | ContentItemBPEODateTo | DATE_TO | — | — |
| 78 | ContentItemBPEOItemDate1 | ITEM_DATE_1 | — | — |
| 79 | ContentItemBPEOItemDate10 | ITEM_DATE_10 | — | — |
| 80 | ContentItemBPEOItemDate2 | ITEM_DATE_2 | — | — |
| 81 | ContentItemBPEOItemDate3 | ITEM_DATE_3 | — | — |
| 82 | ContentItemBPEOItemDate4 | ITEM_DATE_4 | — | — |
| 83 | ContentItemBPEOItemDate5 | ITEM_DATE_5 | — | — |
| 84 | ContentItemBPEOItemDate6 | ITEM_DATE_6 | — | — |
| 85 | ContentItemBPEOItemDate7 | ITEM_DATE_7 | — | — |
| 86 | ContentItemBPEOItemDate8 | ITEM_DATE_8 | — | — |
| 87 | ContentItemBPEOItemDate9 | ITEM_DATE_9 | — | — |
| 88 | ContentItemBPEOItemNumber1 | ITEM_NUMBER_1 | — | — |
| 89 | ContentItemBPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 90 | ContentItemBPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 91 | ContentItemBPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 92 | ContentItemBPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 93 | ContentItemBPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 94 | ContentItemBPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 95 | ContentItemBPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 96 | ContentItemBPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 97 | ContentItemBPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 98 | ContentItemBPEOItemText1 | ITEM_TEXT_1 | — | — |
| 99 | ContentItemBPEOItemText10 | ITEM_TEXT_10 | — | — |
| 100 | ContentItemBPEOItemText11 | ITEM_TEXT_11 | — | — |
| 101 | ContentItemBPEOItemText12 | ITEM_TEXT_12 | — | — |
| 102 | ContentItemBPEOItemText13 | ITEM_TEXT_13 | — | — |
| 103 | ContentItemBPEOItemText14 | ITEM_TEXT_14 | — | — |
| 104 | ContentItemBPEOItemText15 | ITEM_TEXT_15 | — | — |
| 105 | ContentItemBPEOItemText16 | ITEM_TEXT_16 | — | — |
| 106 | ContentItemBPEOItemText17 | ITEM_TEXT_17 | — | — |
| 107 | ContentItemBPEOItemText18 | ITEM_TEXT_18 | — | — |
| 108 | ContentItemBPEOItemText19 | ITEM_TEXT_19 | — | — |
| 109 | ContentItemBPEOItemText2 | ITEM_TEXT_2 | — | — |
| 110 | ContentItemBPEOItemText20 | ITEM_TEXT_20 | — | — |
| 111 | ContentItemBPEOItemText21 | ITEM_TEXT_21 | — | — |
| 112 | ContentItemBPEOItemText22 | ITEM_TEXT_22 | — | — |
| 113 | ContentItemBPEOItemText23 | ITEM_TEXT_23 | — | — |
| 114 | ContentItemBPEOItemText24 | ITEM_TEXT_24 | — | — |
| 115 | ContentItemBPEOItemText25 | ITEM_TEXT_25 | — | — |
| 116 | ContentItemBPEOItemText26 | ITEM_TEXT_26 | — | — |
| 117 | ContentItemBPEOItemText27 | ITEM_TEXT_27 | — | — |
| 118 | ContentItemBPEOItemText28 | ITEM_TEXT_28 | — | — |
| 119 | ContentItemBPEOItemText29 | ITEM_TEXT_29 | — | — |
| 120 | ContentItemBPEOItemText3 | ITEM_TEXT_3 | — | — |
| 121 | ContentItemBPEOItemText30 | ITEM_TEXT_30 | — | — |
| 122 | ContentItemBPEOItemText4 | ITEM_TEXT_4 | — | — |
| 123 | ContentItemBPEOItemText5 | ITEM_TEXT_5 | — | — |
| 124 | ContentItemBPEOItemText6 | ITEM_TEXT_6 | — | — |
| 125 | ContentItemBPEOItemText7 | ITEM_TEXT_7 | — | — |
| 126 | ContentItemBPEOItemText8 | ITEM_TEXT_8 | — | — |
| 127 | ContentItemBPEOItemText9 | ITEM_TEXT_9 | — | — |
| 128 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 129 | ContentItemBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 130 | ContentItemBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 131 | ContentItemBPEOModuleId | MODULE_ID | — | — |
| 132 | ContentItemBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 133 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | — |
| 134 | ContentItemBPEOStateProvinceId | STATE_PROVINCE_ID | — | — |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 3 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOCreatedBy | CREATED_BY | — | — |
| 5 | ContentTypeBPEOCreationDate | CREATION_DATE | — | — |
| 6 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 7 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContentTypeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContentTypeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContentTypeBPEOModuleId | MODULE_ID | — | — |
| 11 | ContentTypeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProfileBPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProfileBPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | — | ✅ |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 13 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |
| 14 | ProfileId | PROFILE_ID | 🔑 | ✅ |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ProfileItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ProfileItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ProfileItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ProfileItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ProfileItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ProfileItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ProfileItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ProfileItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ProfileItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ProfileItemPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ProfileItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ProfileItemPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ProfileItemPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | ProfileItemPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | ProfileItemPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | ProfileItemPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | ProfileItemPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | ProfileItemPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | ProfileItemPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | ProfileItemPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | ProfileItemPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | ProfileItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | ProfileItemPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | ProfileItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | ProfileItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | ProfileItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | ProfileItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | ProfileItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | ProfileItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | ProfileItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | ProfileItemPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | ProfileItemPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | ProfileItemPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | ProfileItemPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | ProfileItemPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | ProfileItemPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | ProfileItemPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | ProfileItemPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | ProfileItemPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | ProfileItemPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | ProfileItemPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | ProfileItemPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | ProfileItemPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | ProfileItemPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | ProfileItemPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | ProfileItemPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | ProfileItemPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | ProfileItemPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | ProfileItemPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | ProfileItemPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | ProfileItemPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | ProfileItemPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | ProfileItemPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | ProfileItemPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | ProfileItemPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | ProfileItemPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | ProfileItemPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | ProfileItemPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | ProfileItemPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | ProfileItemPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | ProfileItemPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | ProfileItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | ProfileItemPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | ProfileItemPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | ProfileItemPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | ProfileItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | ProfileItemPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 69 | ProfileItemPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 70 | ProfileItemPEOCountryId | COUNTRY_ID | — | — |
| 71 | ProfileItemPEOCreatedBy | CREATED_BY | — | — |
| 72 | ProfileItemPEOCreationDate | CREATION_DATE | — | — |
| 73 | ProfileItemPEODateFrom | DATE_FROM | — | ✅ |
| 74 | ProfileItemPEODateTo | DATE_TO | — | ✅ |
| 75 | ProfileItemPEOImportance | IMPORTANCE | — | — |
| 76 | ProfileItemPEOInterestLevel | INTEREST_LEVEL | — | — |
| 77 | ProfileItemPEOItemDate1 | ITEM_DATE_1 | — | — |
| 78 | ProfileItemPEOItemDate10 | ITEM_DATE_10 | — | — |
| 79 | ProfileItemPEOItemDate2 | ITEM_DATE_2 | — | — |
| 80 | ProfileItemPEOItemDate3 | ITEM_DATE_3 | — | — |
| 81 | ProfileItemPEOItemDate4 | ITEM_DATE_4 | — | — |
| 82 | ProfileItemPEOItemDate5 | ITEM_DATE_5 | — | — |
| 83 | ProfileItemPEOItemDate6 | ITEM_DATE_6 | — | — |
| 84 | ProfileItemPEOItemDate7 | ITEM_DATE_7 | — | — |
| 85 | ProfileItemPEOItemDate8 | ITEM_DATE_8 | — | — |
| 86 | ProfileItemPEOItemDate9 | ITEM_DATE_9 | — | — |
| 87 | ProfileItemPEOItemDecimal1 | ITEM_DECIMAL_1 | — | — |
| 88 | ProfileItemPEOItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 89 | ProfileItemPEOItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 90 | ProfileItemPEOItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 91 | ProfileItemPEOItemDecimal5 | ITEM_DECIMAL_5 | — | — |
| 92 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 93 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 94 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 95 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 96 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 97 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 98 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 99 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 100 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 101 | ProfileItemPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 102 | ProfileItemPEOItemText20001 | ITEM_TEXT2000_1 | — | — |
| 103 | ProfileItemPEOItemText20002 | ITEM_TEXT2000_2 | — | — |
| 104 | ProfileItemPEOItemText20003 | ITEM_TEXT2000_3 | — | — |
| 105 | ProfileItemPEOItemText20004 | ITEM_TEXT2000_4 | — | — |
| 106 | ProfileItemPEOItemText20005 | ITEM_TEXT2000_5 | — | — |
| 107 | ProfileItemPEOItemText2401 | ITEM_TEXT240_1 | — | — |
| 108 | ProfileItemPEOItemText24010 | ITEM_TEXT240_10 | — | — |
| 109 | ProfileItemPEOItemText24011 | ITEM_TEXT240_11 | — | — |
| 110 | ProfileItemPEOItemText24012 | ITEM_TEXT240_12 | — | — |
| 111 | ProfileItemPEOItemText24013 | ITEM_TEXT240_13 | — | — |
| 112 | ProfileItemPEOItemText24014 | ITEM_TEXT240_14 | — | — |
| 113 | ProfileItemPEOItemText24015 | ITEM_TEXT240_15 | — | — |
| 114 | ProfileItemPEOItemText2402 | ITEM_TEXT240_2 | — | — |
| 115 | ProfileItemPEOItemText2403 | ITEM_TEXT240_3 | — | — |
| 116 | ProfileItemPEOItemText2404 | ITEM_TEXT240_4 | — | — |
| 117 | ProfileItemPEOItemText2405 | ITEM_TEXT240_5 | — | — |
| 118 | ProfileItemPEOItemText2406 | ITEM_TEXT240_6 | — | — |
| 119 | ProfileItemPEOItemText2407 | ITEM_TEXT240_7 | — | — |
| 120 | ProfileItemPEOItemText2408 | ITEM_TEXT240_8 | — | — |
| 121 | ProfileItemPEOItemText2409 | ITEM_TEXT240_9 | — | — |
| 122 | ProfileItemPEOItemText301 | ITEM_TEXT30_1 | — | — |
| 123 | ProfileItemPEOItemText3010 | ITEM_TEXT30_10 | — | — |
| 124 | ProfileItemPEOItemText3011 | ITEM_TEXT30_11 | — | — |
| 125 | ProfileItemPEOItemText3012 | ITEM_TEXT30_12 | — | — |
| 126 | ProfileItemPEOItemText3013 | ITEM_TEXT30_13 | — | — |
| 127 | ProfileItemPEOItemText3014 | ITEM_TEXT30_14 | — | — |
| 128 | ProfileItemPEOItemText3015 | ITEM_TEXT30_15 | — | — |
| 129 | ProfileItemPEOItemText302 | ITEM_TEXT30_2 | — | — |
| 130 | ProfileItemPEOItemText303 | ITEM_TEXT30_3 | — | — |
| 131 | ProfileItemPEOItemText304 | ITEM_TEXT30_4 | — | — |
| 132 | ProfileItemPEOItemText305 | ITEM_TEXT30_5 | — | — |
| 133 | ProfileItemPEOItemText306 | ITEM_TEXT30_6 | — | — |
| 134 | ProfileItemPEOItemText307 | ITEM_TEXT30_7 | — | — |
| 135 | ProfileItemPEOItemText308 | ITEM_TEXT30_8 | — | — |
| 136 | ProfileItemPEOItemText309 | ITEM_TEXT30_9 | — | — |
| 137 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 138 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 139 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 140 | ProfileItemPEOMandatory | MANDATORY | — | — |
| 141 | ProfileItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 142 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 143 | ProfileItemPEOProfileId | PROFILE_ID | — | — |
| 144 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 145 | ProfileItemPEOQualifierId1 | QUALIFIER_ID1 | — | — |
| 146 | ProfileItemPEOQualifierId2 | QUALIFIER_ID2 | — | — |
| 147 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 148 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 149 | ProfileItemPEORatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 150 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 151 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 152 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 153 | ProfileItemPEOSourceId | SOURCE_ID | — | — |
| 154 | ProfileItemPEOSourceKey1 | SOURCE_KEY1 | 🔑 | ✅ |
| 155 | ProfileItemPEOSourceKey2 | SOURCE_KEY2 | — | — |
| 156 | ProfileItemPEOSourceKey3 | SOURCE_KEY3 | — | — |
| 157 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 158 | SourceType | SOURCE_TYPE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
