---
id: DOC-OTHER-PVO-PlanTypeTranslationExtractP1
doc_type: system-doc
title: "PlanTypeTranslationExtractP1 — PVO Cross-Module"
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
  - PlanTypeTranslationExtractP1
  - plantypetranslationextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanTypeTranslationExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Type Translation Extract P1. Acessa as tabelas: PJO_PLAN_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanTypeTranslationExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PlanTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PlanTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PlanTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PlanTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PlanTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PlanTypeTranslationPEOName | NAME | — | ✅ |
| 9 | PlanTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PlanTypeTranslationPEOPlanTypeId | PLAN_TYPE_ID | 🔑 | ✅ |
| 11 | PlanTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
