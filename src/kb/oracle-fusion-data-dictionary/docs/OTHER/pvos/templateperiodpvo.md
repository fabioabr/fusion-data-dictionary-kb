---
id: DOC-OTHER-PVO-TemplatePeriodPVO
doc_type: system-doc
title: "TemplatePeriodPVO — PVO Cross-Module"
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
  - TemplatePeriodPVO
  - templateperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplatePeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Period. Acessa as tabelas: HRA_TMPL_PERIODS_B, HRA_TMPL_PERIODS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.TemplatePeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 3 | 10 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 6 BICC)
- [[hra_tmpl_periods_tl|HRA_TMPL_PERIODS_TL]] — 7 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TemplatePeriodBPEOLockMgrShareForCalibFlag | LOCK_MGR_SHARE_FOR_CALIB_FLAG | — | ✅ |
| 9 | TemplatePeriodBPEONominalFromDate | NOMINAL_FROM_DATE | — | ✅ |
| 10 | TemplatePeriodBPEONominalToDate | NOMINAL_TO_DATE | — | ✅ |
| 11 | TemplatePeriodBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 12 | TmplPeriodId | TMPL_PERIOD_ID | 🔑 | ✅ |

### [[hra_tmpl_periods_tl|HRA_TMPL_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | SourceLang | SOURCE_LANG | — | — |
| 3 | TemplatePeriodTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | TemplatePeriodTranslationPEOCustomaryName | CUSTOMARY_NAME | — | ✅ |
| 5 | TemplatePeriodTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TemplatePeriodTranslationPEOShortName | SHORT_NAME | — | ✅ |
| 7 | TemplatePeriodTranslationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
