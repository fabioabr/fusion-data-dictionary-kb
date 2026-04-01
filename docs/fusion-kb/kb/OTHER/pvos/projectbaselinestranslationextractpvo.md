---
id: DOC-OTHER-PVO-ProjectBaselinesTranslationExtractPVO
doc_type: system-doc
title: "ProjectBaselinesTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectBaselinesTranslationExtractPVO
  - projectbaselinestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectBaselinesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Baselines Translation Extract. Acessa as tabelas: PJT_BASELINES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectBaselinesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_baselines_tl|PJT_BASELINES_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjt_baselines_tl|PJT_BASELINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtBaselineTranslationEOBaselineDesc | BASELINE_DESC | — | ✅ |
| 2 | PjtBaselineTranslationEOBaselineId | BASELINE_ID | 🔑 | ✅ |
| 3 | PjtBaselineTranslationEOBaselineName | BASELINE_NAME | — | ✅ |
| 4 | PjtBaselineTranslationEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PjtBaselineTranslationEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PjtBaselineTranslationEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | PjtBaselineTranslationEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PjtBaselineTranslationEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PjtBaselineTranslationEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PjtBaselineTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PjtBaselineTranslationEOProjectId | PROJECT_ID | 🔑 | ✅ |
| 12 | PjtBaselineTranslationEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
