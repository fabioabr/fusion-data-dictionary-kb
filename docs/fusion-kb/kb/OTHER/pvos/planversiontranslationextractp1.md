---
id: DOC-OTHER-PVO-PlanVersionTranslationExtractP1
doc_type: system-doc
title: "PlanVersionTranslationExtractP1 — PVO Cross-Module"
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
  - PlanVersionTranslationExtractP1
  - planversiontranslationextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanVersionTranslationExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Version Translation Extract P1. Acessa as tabelas: PJO_PLAN_VERSIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanVersionTranslationExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjo_plan_versions_tl|PJO_PLAN_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanVersionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PlanVersionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PlanVersionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PlanVersionTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PlanVersionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanVersionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PlanVersionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PlanVersionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PlanVersionTranslationPEOPlanVersionId | PLAN_VERSION_ID | 🔑 | ✅ |
| 10 | PlanVersionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | PlanVersionTranslationPEOVersionName | VERSION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
