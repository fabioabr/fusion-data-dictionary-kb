---
id: DOC-OTHER-PVO-TemplateAnalyticTypePVO
doc_type: system-doc
title: "TemplateAnalyticTypePVO — PVO Cross-Module"
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
  - TemplateAnalyticTypePVO
  - templateanalytictypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateAnalyticTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Analytic Type. Acessa as tabelas: HRR_TMPL_ANALYTIC_TYPES_B, HRR_TMPL_ANALYTIC_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibSetupAM.TemplateAnalyticTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 2 | 21 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]] — 20 atributos (2 PKs, 20 BICC)
- [[hrr_tmpl_analytic_types_tl|HRR_TMPL_ANALYTIC_TYPES_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrr_tmpl_analytic_types_b|HRR_TMPL_ANALYTIC_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticTypeCode | ANALYTIC_TYPE_CODE | — | ✅ |
| 2 | AnalyticTypeId | ANALYTIC_TYPE_ID | 🔑 | ✅ |
| 3 | AnalyticViewMode | ANALYTIC_VIEW_MODE | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 5 | ColorSchemeCode | COLOR_SCHEME_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | DashboardTmplId | DASHBOARD_TMPL_ID | — | ✅ |
| 9 | DefaultViewFlag | DEFAULT_VIEW_FLAG | — | ✅ |
| 10 | HorizontalAxisCode | HORIZONTAL_AXIS_CODE | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | MetricCode | METRIC_CODE | — | ✅ |
| 15 | ModuleId | MODULE_ID | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | SubmitBoxAsgnmntFlag | SUBMIT_BOX_ASGNMNT_FLAG | — | ✅ |
| 18 | VerticalAxisCode | VERTICAL_AXIS_CODE | — | ✅ |
| 19 | ViewColumnCount | VIEW_COLUMN_COUNT | — | ✅ |
| 20 | ViewRowCount | VIEW_ROW_COUNT | — | ✅ |

### [[hrr_tmpl_analytic_types_tl|HRR_TMPL_ANALYTIC_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticViewName | ANALYTIC_VIEW_NAME | — | ✅ |
| 2 | Language | LANGUAGE | — | — |
| 3 | SourceLang | SOURCE_LANG | — | — |
| 4 | TemplateAnalyticTypeTLPEOAnalyticTypeId | ANALYTIC_TYPE_ID | — | — |
| 5 | TemplateAnalyticTypeTLPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | TemplateAnalyticTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 7 | TemplateAnalyticTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 8 | TemplateAnalyticTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | TemplateAnalyticTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | TemplateAnalyticTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | TemplateAnalyticTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
