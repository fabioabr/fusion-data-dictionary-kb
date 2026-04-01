---
id: DOC-OTHER-PVO-EligibilityResultsDetailsPVO
doc_type: system-doc
title: "EligibilityResultsDetailsPVO — PVO Cross-Module"
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
  - EligibilityResultsDetailsPVO
  - eligibilityresultsdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibilityResultsDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eligibility Results Details. Acessa as tabelas: BEN_ELIG_OBJ_F, BEN_ELIG_RSLT_F, HRA_TMPL_DEFNS_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.EligibilityResultsDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 132 | 4 | 11 | 24 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_obj_f|BEN_ELIG_OBJ_F]] — 14 atributos (3 PKs, 5 BICC)
- [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]] — 20 atributos (4 PKs, 13 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 87 atributos (2 PKs, 3 BICC)
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ben_elig_obj_f|BEN_ELIG_OBJ_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EligibilityObjectPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EligibilityObjectPEOColumnName | COLUMN_NAME | — | — |
| 3 | EligibilityObjectPEOColumnValue | COLUMN_VALUE | — | — |
| 4 | EligibilityObjectPEOCreatedBy | CREATED_BY | — | — |
| 5 | EligibilityObjectPEOCreationDate | CREATION_DATE | — | — |
| 6 | EligibilityObjectPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | EligibilityObjectPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | EligibilityObjectPEOEligObjId | ELIG_OBJ_ID | 🔑 | ✅ |
| 9 | EligibilityObjectPEOEligObjType | ELIG_OBJ_TYPE | — | ✅ |
| 10 | EligibilityObjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | EligibilityObjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EligibilityObjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EligibilityObjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | EligibilityObjectPEOTableName | TABLE_NAME | — | — |

### [[ben_elig_rslt_f|BEN_ELIG_RSLT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EligibilityResultPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | EligibilityResultPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | EligibilityResultPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | EligibilityResultPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | EligibilityResultPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EligibilityResultPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EligibilityResultPEOEligFlag | ELIG_FLAG | — | ✅ |
| 8 | EligibilityResultPEOEligObjId | ELIG_OBJ_ID | — | ✅ |
| 9 | EligibilityResultPEOEligRsltId | ELIG_RSLT_ID | 🔑 | ✅ |
| 10 | EligibilityResultPEOInelgRsnCd | INELG_RSN_CD | — | ✅ |
| 11 | EligibilityResultPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | EligibilityResultPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | EligibilityResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EligibilityResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | EligibilityResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | EligibilityResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | EligibilityResultPEOOverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 18 | EligibilityResultPEOOverrideThruDate | OVERRIDE_THRU_DATE | — | — |
| 19 | EligibilityResultPEOPersonId | PERSON_ID | — | — |
| 20 | EligibilityResultPEORequestId | REQUEST_ID | — | — |

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateDefnBPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | TemplateDefnBPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | TemplateDefnBPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | TemplateDefnBPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | TemplateDefnBPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | TemplateDefnBPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | TemplateDefnBPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | TemplateDefnBPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | TemplateDefnBPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | TemplateDefnBPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | TemplateDefnBPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | TemplateDefnBPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | TemplateDefnBPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | TemplateDefnBPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | TemplateDefnBPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | TemplateDefnBPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | TemplateDefnBPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | TemplateDefnBPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | TemplateDefnBPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | TemplateDefnBPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | TemplateDefnBPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | TemplateDefnBPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | TemplateDefnBPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | TemplateDefnBPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | TemplateDefnBPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | TemplateDefnBPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | TemplateDefnBPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | TemplateDefnBPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | TemplateDefnBPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | TemplateDefnBPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | TemplateDefnBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | TemplateDefnBPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | TemplateDefnBPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | TemplateDefnBPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | TemplateDefnBPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | TemplateDefnBPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | TemplateDefnBPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | TemplateDefnBPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | TemplateDefnBPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | TemplateDefnBPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | TemplateDefnBPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | TemplateDefnBPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | TemplateDefnBPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | TemplateDefnBPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | TemplateDefnBPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | TemplateDefnBPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | TemplateDefnBPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | TemplateDefnBPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | TemplateDefnBPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | TemplateDefnBPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | TemplateDefnBPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | TemplateDefnBPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | TemplateDefnBPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | TemplateDefnBPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | TemplateDefnBPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | TemplateDefnBPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | TemplateDefnBPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | TemplateDefnBPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | TemplateDefnBPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | TemplateDefnBPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | TemplateDefnBPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | TemplateDefnBPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | TemplateDefnBPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | TemplateDefnBPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | TemplateDefnBPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | TemplateDefnBPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | TemplateDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 68 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | — |
| 69 | TemplateDefnBPEOCreatedBy | CREATED_BY | — | — |
| 70 | TemplateDefnBPEOCreationDate | CREATION_DATE | — | — |
| 71 | TemplateDefnBPEODateFrom | DATE_FROM | — | — |
| 72 | TemplateDefnBPEODateTo | DATE_TO | — | — |
| 73 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 74 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | — |
| 75 | TemplateDefnBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | TemplateDefnBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 77 | TemplateDefnBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 78 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 79 | TemplateDefnBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 81 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 82 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | — |
| 83 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 84 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | — |
| 85 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 86 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | — |
| 87 | TemplateDefnBPEOTemplateDefnId | TEMPLATE_DEFN_ID | 🔑 | ✅ |

### [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplatePeriodBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | TemplatePeriodBPEOCreatedBy | CREATED_BY | — | — |
| 3 | TemplatePeriodBPEOCreationDate | CREATION_DATE | — | — |
| 4 | TemplatePeriodBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TemplatePeriodBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TemplatePeriodBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TemplatePeriodBPEONominalFromDate | NOMINAL_FROM_DATE | — | — |
| 8 | TemplatePeriodBPEONominalToDate | NOMINAL_TO_DATE | — | — |
| 9 | TemplatePeriodBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TemplatePeriodBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 11 | TemplatePeriodBPEOTmplPeriodId | TMPL_PERIOD_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
