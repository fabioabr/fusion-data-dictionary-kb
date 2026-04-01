---
id: DOC-OTHER-PVO-ProjPlanVersionTranslationPVO
doc_type: system-doc
title: "ProjPlanVersionTranslationPVO — PVO Cross-Module"
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
  - ProjPlanVersionTranslationPVO
  - projplanversiontranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjPlanVersionTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Proj Plan Version Translation. Acessa as tabelas: PJO_PLAN_VERSIONS_TL.

**Caminho:** `FscmTopModelAM.PjoBudgetsAndForecastsAnalyticsAM.ProjPlanVersionTranslationPVO`

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
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PlanVersionId | PLAN_VERSION_ID | 🔑 | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |
| 11 | VersionName | VERSION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
