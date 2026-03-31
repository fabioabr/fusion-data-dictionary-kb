---
id: DOC-OTHER-PVO-TemplateDefnPVO
doc_type: system-doc
title: "TemplateDefnPVO — PVO Cross-Module"
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
  - TemplateDefnPVO
  - templatedefnpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateDefnPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Defn. Acessa as tabelas: HRA_TMPL_DEFNS_B, HRA_TMPL_DEFNS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.TemplateDefnPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 2 | 4 | 30 | 88% |

---

## 🔗 Tabelas Relacionadas

- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 27 atributos (2 PKs, 23 BICC)
- [[hra_tmpl_defns_tl|HRA_TMPL_DEFNS_TL]] — 7 atributos (2 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | ✅ |
| 9 | TemplateDefnBPEODateFrom | DATE_FROM | — | ✅ |
| 10 | TemplateDefnBPEODateTo | DATE_TO | — | ✅ |
| 11 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 12 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | ✅ |
| 13 | TemplateDefnBPEOKudosRegionFlag | KUDOS_REGION_FLAG | — | ✅ |
| 14 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | ✅ |
| 15 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 16 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 17 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | ✅ |
| 18 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 19 | TemplateDefnBPEOSetRoleMinimumsFlag | SET_ROLE_MINIMUMS_FLAG | — | ✅ |
| 20 | TemplateDefnBPEOShowCheckInRegionFlag | SHOW_CHECK_IN_REGION_FLAG | — | ✅ |
| 21 | TemplateDefnBPEOShowFeedbackReqRegionFlag | SHOW_FEEDBACK_REQ_REGION_FLAG | — | ✅ |
| 22 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | ✅ |
| 23 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | ✅ |
| 24 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | ✅ |
| 25 | TemplateDefnBPEOTotalMinParticipants | TOTAL_MIN_PARTICIPANTS | — | ✅ |
| 26 | TemplateDefnId | TEMPLATE_DEFN_ID | 🔑 | ✅ |
| 27 | TemplateTypeCode | TEMPLATE_TYPE_CODE | — | ✅ |

### [[hra_tmpl_defns_tl|HRA_TMPL_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | SourceLang | SOURCE_LANG | — | ✅ |
| 3 | TemplateDefnTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 4 | TemplateDefnTranslationPEOComments | COMMENTS | — | ✅ |
| 5 | TemplateDefnTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TemplateDefnTranslationPEOName | NAME | — | ✅ |
| 7 | TemplateDefnTranslationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
