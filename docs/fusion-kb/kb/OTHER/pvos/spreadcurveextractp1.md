---
id: DOC-OTHER-PVO-SpreadCurveExtractP1
doc_type: system-doc
title: "SpreadCurveExtractP1 — PVO Cross-Module"
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
  - SpreadCurveExtractP1
  - spreadcurveextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SpreadCurveExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Spread Curve Extract P1. Acessa as tabelas: PJO_SPREAD_CURVES_B, PJO_SPREAD_CURVES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.SpreadCurveExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 2 | 1 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_spread_curves_b|PJO_SPREAD_CURVES_B]] — 22 atributos (1 PKs, 22 BICC)
- [[pjo_spread_curves_tl|PJO_SPREAD_CURVES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjo_spread_curves_b|PJO_SPREAD_CURVES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SpreadCurveBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SpreadCurveBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SpreadCurveBasePEOEndDate | END_DATE | — | ✅ |
| 4 | SpreadCurveBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SpreadCurveBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | SpreadCurveBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | SpreadCurveBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SpreadCurveBasePEOPoint1 | POINT1 | — | ✅ |
| 9 | SpreadCurveBasePEOPoint10 | POINT10 | — | ✅ |
| 10 | SpreadCurveBasePEOPoint2 | POINT2 | — | ✅ |
| 11 | SpreadCurveBasePEOPoint3 | POINT3 | — | ✅ |
| 12 | SpreadCurveBasePEOPoint4 | POINT4 | — | ✅ |
| 13 | SpreadCurveBasePEOPoint5 | POINT5 | — | ✅ |
| 14 | SpreadCurveBasePEOPoint6 | POINT6 | — | ✅ |
| 15 | SpreadCurveBasePEOPoint7 | POINT7 | — | ✅ |
| 16 | SpreadCurveBasePEOPoint8 | POINT8 | — | ✅ |
| 17 | SpreadCurveBasePEOPoint9 | POINT9 | — | ✅ |
| 18 | SpreadCurveBasePEORoundingFactorCode | ROUNDING_FACTOR_CODE | — | ✅ |
| 19 | SpreadCurveBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 20 | SpreadCurveBasePEOSpreadCurveCode | SPREAD_CURVE_CODE | — | ✅ |
| 21 | SpreadCurveBasePEOSpreadCurveId | SPREAD_CURVE_ID | 🔑 | ✅ |
| 22 | SpreadCurveBasePEOStartDate | START_DATE | — | ✅ |

### [[pjo_spread_curves_tl|PJO_SPREAD_CURVES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SpreadCurveTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SpreadCurveTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SpreadCurveTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | SpreadCurveTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | SpreadCurveTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SpreadCurveTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SpreadCurveTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SpreadCurveTranslationPEOName | NAME | — | ✅ |
| 9 | SpreadCurveTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SpreadCurveTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | SpreadCurveTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | SpreadCurveTranslationPEOSpreadCurveId | SPREAD_CURVE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
