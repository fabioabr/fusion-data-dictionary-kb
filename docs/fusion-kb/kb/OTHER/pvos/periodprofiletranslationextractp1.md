---
id: DOC-OTHER-PVO-PeriodProfileTranslationExtractP1
doc_type: system-doc
title: "PeriodProfileTranslationExtractP1 — PVO Cross-Module"
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
  - PeriodProfileTranslationExtractP1
  - periodprofiletranslationextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodProfileTranslationExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Period Profile Translation Extract P1. Acessa as tabelas: PJO_PERIOD_PROFILES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PeriodProfileTranslationExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_period_profiles_tl|PJO_PERIOD_PROFILES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjo_period_profiles_tl|PJO_PERIOD_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PeriodProfileTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PeriodProfileTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PeriodProfileTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PeriodProfileTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PeriodProfileTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PeriodProfileTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PeriodProfileTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PeriodProfileTranslationPEOName | NAME | — | ✅ |
| 9 | PeriodProfileTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PeriodProfileTranslationPEOPeriodProfileId | PERIOD_PROFILE_ID | 🔑 | ✅ |
| 11 | PeriodProfileTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | PeriodProfileTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
