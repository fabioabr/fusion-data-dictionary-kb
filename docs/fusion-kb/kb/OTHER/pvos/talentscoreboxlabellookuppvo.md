---
id: DOC-OTHER-PVO-TalentScoreBoxLabelLookupPVO
doc_type: system-doc
title: "TalentScoreBoxLabelLookupPVO — PVO Cross-Module"
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
  - TalentScoreBoxLabelLookupPVO
  - talentscoreboxlabellookuppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TalentScoreBoxLabelLookupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Talent Score Box Label Lookup. Acessa as tabelas: HRR_DASHBOARD_TMPLS_B, HRR_MEETINGS, HRR_TMPL_ANALYTIC_TYPES_B (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibMeetingsAM.TalentScoreBoxLabelLookupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 6 | 8 | 9 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]] — 2 atributos
- [[hrr_meetings|HRR_MEETINGS]] — 2 atributos (2 PKs, 2 BICC)
- [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]] — 6 atributos
- [[hrr_tmpl_anlyt_box_ratings|HRR_TMPL_ANLYT_BOX_RATINGS]] — 5 atributos (3 PKs, 3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 4 atributos
- [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]] — 5 atributos (3 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboard_tmpls_b|HRR_DASHBOARD_TMPLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | DashboardTmplId | DASHBOARD_TMPL_ID | — | — |

### [[hrr_meetings|HRR_MEETINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | MeetingId | MEETING_ID | 🔑 | ✅ |

### [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticTypeCode | ANALYTIC_TYPE_CODE | — | — |
| 2 | AnalyticTypeId | ANALYTIC_TYPE_ID | — | — |
| 3 | AnalyticViewMode | ANALYTIC_VIEW_MODE | — | — |
| 4 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 5 | MetricCode | METRIC_CODE | — | — |
| 6 | SubmitBoxAsgnmntFlag | SUBMIT_BOX_ASGNMNT_FLAG | — | — |

### [[hrr_tmpl_anlyt_box_ratings|HRR_TMPL_ANLYT_BOX_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BoxRatingMappingId | BOX_RATING_MAPPING_ID | 🔑 | ✅ |
| 2 | BoxSequence | BOX_SEQUENCE | 🔑 | ✅ |
| 3 | BusinessGroupId3 | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 4 | MetricRatingModelId | METRIC_RATING_MODEL_ID | — | — |
| 5 | RatingLevelId | RATING_LEVEL_ID | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 2 | NumericRating | NUMERIC_RATING | — | — |
| 3 | RatingLevelCode | RATING_LEVEL_CODE | — | — |
| 4 | RatingLevelId2 | RATING_LEVEL_ID | — | — |

### [[hrt_rating_levels_tl|HRT_RATING_LEVELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId4 | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | Language | LANGUAGE | 🔑 | ✅ |
| 3 | RatingDescription | RATING_DESCRIPTION | — | ✅ |
| 4 | RatingLevelId1 | RATING_LEVEL_ID | 🔑 | ✅ |
| 5 | RatingShortDescr | RATING_SHORT_DESCR | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
