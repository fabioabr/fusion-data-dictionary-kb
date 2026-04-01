---
id: DOC-OTHER-PVO-PerformancePotentialBoxSequencePVO_Viewall
doc_type: system-doc
title: "PerformancePotentialBoxSequencePVO_Viewall — PVO Cross-Module"
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
  - PerformancePotentialBoxSequencePVO_Viewall
  - performancepotentialboxsequencepvo_viewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformancePotentialBoxSequencePVO_Viewall

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Potential Box Sequence_Viewall. Acessa as tabelas: HRR_TMPL_ANALYTIC_TYPES_B, HRT_CONTENT_ITEMS_B, HRT_CONTENT_TYPES_B (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.PerformancePotentialBoxSequencePVO_Viewall`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 5 | 8 | 14 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]] — 8 atributos (1 PKs, 2 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 4 atributos (1 PKs, 2 BICC)
- [[hrt_content_types_b|HRT_CONTENT_TYPES_B]] — 5 atributos (1 PKs, 2 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 14 atributos (3 PKs, 4 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 6 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateAnalyticTypeBPEOAnalyticTypeId | ANALYTIC_TYPE_ID | 🔑 | ✅ |
| 2 | TemplateAnalyticTypeBPEOAnalyticViewMode | ANALYTIC_VIEW_MODE | — | — |
| 3 | TemplateAnalyticTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | TemplateAnalyticTypeBPEOHorizontalAxisCode | HORIZONTAL_AXIS_CODE | — | — |
| 5 | TemplateAnalyticTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TemplateAnalyticTypeBPEOMetricCode | METRIC_CODE | — | — |
| 7 | TemplateAnalyticTypeBPEOSubmitBoxAsgnmntFlag | SUBMIT_BOX_ASGNMNT_FLAG | — | — |
| 8 | TemplateAnalyticTypeBPEOVerticalAxisCode | VERTICAL_AXIS_CODE | — | — |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ContentTypeBPEOContentItemCode | CONTENT_ITEM_CODE | — | — |
| 4 | ContentTypeBPEOContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |

### [[hrt_content_types_b|HRT_CONTENT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentTypeBPEOContentTypeId | CONTENT_TYPE_ID | 🔑 | ✅ |
| 3 | ContentTypeBPEOContextName | CONTEXT_NAME | — | — |
| 4 | ContentTypeBPEOFreeFormFlag | FREE_FORM_FLAG | — | — |
| 5 | ContentTypeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProfileBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 8 | ProfileBPEOOwnerPersonId | OWNER_PERSON_ID | — | — |
| 9 | ProfileBPEOPartyId | PARTY_ID | — | — |
| 10 | ProfileBPEOPersonId | PERSON_ID | 🔑 | ✅ |
| 11 | ProfileBPEOProfileCode | PROFILE_CODE | — | — |
| 12 | ProfileBPEOProfileId | PROFILE_ID | 🔑 | ✅ |
| 13 | ProfileBPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 14 | ProfileBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | — |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | ✅ |
| 2 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | ProfileItemPEOProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 4 | ProfileItemPEOSourceId | SOURCE_ID | — | — |
| 5 | ProfileItemPEOSourceKey1 | SOURCE_KEY1 | 🔑 | ✅ |
| 6 | ProfileItemPEOSourceType | SOURCE_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
