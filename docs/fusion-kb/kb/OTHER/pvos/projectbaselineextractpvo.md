---
id: DOC-OTHER-PVO-ProjectBaselineExtractPVO
doc_type: system-doc
title: "ProjectBaselineExtractPVO — PVO Cross-Module"
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
  - ProjectBaselineExtractPVO
  - projectbaselineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectBaselineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Baseline Extract. Acessa as tabelas: PJT_BASELINES_B, PJT_BASELINES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectBaselineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 1 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_baselines_b|PJT_BASELINES_B]] — 11 atributos (1 PKs, 11 BICC)
- [[pjt_baselines_tl|PJT_BASELINES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjt_baselines_b|PJT_BASELINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtBaselineBasePEOBaselineDatetime | BASELINE_DATETIME | — | ✅ |
| 2 | PjtBaselineBasePEOBaselineId | BASELINE_ID | 🔑 | ✅ |
| 3 | PjtBaselineBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PjtBaselineBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PjtBaselineBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PjtBaselineBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PjtBaselineBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PjtBaselineBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PjtBaselineBasePEOPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 10 | PjtBaselineBasePEOProjectId | PROJECT_ID | — | ✅ |
| 11 | PjtBaselineTranslationEOPrimaryBaselineFlag | PRIMARY_BASELINE_FLAG | — | ✅ |

### [[pjt_baselines_tl|PJT_BASELINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtBaselineTranslationEOBaselineDesc | BASELINE_DESC | — | ✅ |
| 2 | PjtBaselineTranslationEOBaselineId | BASELINE_ID | — | ✅ |
| 3 | PjtBaselineTranslationEOBaselineName | BASELINE_NAME | — | ✅ |
| 4 | PjtBaselineTranslationEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PjtBaselineTranslationEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PjtBaselineTranslationEOLanguage | LANGUAGE | — | ✅ |
| 7 | PjtBaselineTranslationEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PjtBaselineTranslationEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PjtBaselineTranslationEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PjtBaselineTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PjtBaselineTranslationEOProjectId | PROJECT_ID | — | ✅ |
| 12 | PjtBaselineTranslationEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
