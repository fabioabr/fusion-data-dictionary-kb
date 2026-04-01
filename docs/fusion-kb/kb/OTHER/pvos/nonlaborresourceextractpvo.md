---
id: DOC-OTHER-PVO-NonLaborResourceExtractPVO
doc_type: system-doc
title: "NonLaborResourceExtractPVO — PVO Cross-Module"
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
  - NonLaborResourceExtractPVO
  - nonlaborresourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NonLaborResourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Non Labor Resource Extract. Acessa as tabelas: PJF_NON_LABOR_RES_B, PJF_NON_LABOR_RES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.NonLaborResourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 22 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]] — 27 atributos (1 PKs, 11 BICC)
- [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | NonLaborResourceBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | NonLaborResourceBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | NonLaborResourceBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | NonLaborResourceBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | NonLaborResourceBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | NonLaborResourceBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | NonLaborResourceBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | NonLaborResourceBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | NonLaborResourceBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | NonLaborResourceBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | NonLaborResourceBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | NonLaborResourceBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | NonLaborResourceBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | NonLaborResourceBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | NonLaborResourceBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | NonLaborResourceBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | NonLaborResourceBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | NonLaborResourceBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 20 | NonLaborResourceBasePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | ✅ |
| 21 | NonLaborResourceBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 22 | NonLaborResourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | NonLaborResourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | NonLaborResourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | NonLaborResourceBasePEONonLaborResourceId | NON_LABOR_RESOURCE_ID | 🔑 | ✅ |
| 26 | NonLaborResourceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | NonLaborResourceBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceTranslangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | NonLaborResourceTranslangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | NonLaborResourceTranslangPEODescription | DESCRIPTION | — | ✅ |
| 4 | NonLaborResourceTranslangPEOLanguage | LANGUAGE | — | ✅ |
| 5 | NonLaborResourceTranslangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | NonLaborResourceTranslangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | NonLaborResourceTranslangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | NonLaborResourceTranslangPEONlrName | NLR_NAME | — | ✅ |
| 9 | NonLaborResourceTranslangPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 10 | NonLaborResourceTranslangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | NonLaborResourceTranslangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
