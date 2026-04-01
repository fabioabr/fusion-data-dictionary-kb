---
id: DOC-OTHER-PVO-SpreadCurveTranslationExtractP1
doc_type: system-doc
title: "SpreadCurveTranslationExtractP1 — PVO Cross-Module"
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
  - SpreadCurveTranslationExtractP1
  - spreadcurvetranslationextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SpreadCurveTranslationExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Spread Curve Translation Extract P1. Acessa as tabelas: PJO_SPREAD_CURVES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.SpreadCurveTranslationExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_spread_curves_tl|PJO_SPREAD_CURVES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjo_spread_curves_tl|PJO_SPREAD_CURVES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SpreadCurveTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SpreadCurveTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SpreadCurveTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | SpreadCurveTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | SpreadCurveTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SpreadCurveTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SpreadCurveTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SpreadCurveTranslationPEOName | NAME | — | ✅ |
| 9 | SpreadCurveTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SpreadCurveTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | SpreadCurveTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | SpreadCurveTranslationPEOSpreadCurveId | SPREAD_CURVE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
