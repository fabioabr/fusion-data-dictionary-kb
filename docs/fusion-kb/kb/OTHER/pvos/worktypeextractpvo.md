---
id: DOC-OTHER-PVO-WorkTypeExtractPVO
doc_type: system-doc
title: "WorkTypeExtractPVO — PVO Cross-Module"
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
  - WorkTypeExtractPVO
  - worktypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Type Extract. Acessa as tabelas: PJF_WORK_TYPES_B, PJF_WORK_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.WorkTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 2 | 1 | 23 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_work_types_b|PJF_WORK_TYPES_B]] — 28 atributos (1 PKs, 12 BICC)
- [[pjf_work_types_tl|PJF_WORK_TYPES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_work_types_b|PJF_WORK_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | WorkTypeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | WorkTypeBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | WorkTypeBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | WorkTypeBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | WorkTypeBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | WorkTypeBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | WorkTypeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | WorkTypeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | WorkTypeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | WorkTypeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | WorkTypeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | WorkTypeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | WorkTypeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | WorkTypeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | WorkTypeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | WorkTypeBasePEOBillableCapitalizableFlag | BILLABLE_CAPITALIZABLE_FLAG | — | ✅ |
| 18 | WorkTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | WorkTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | WorkTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 21 | WorkTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | WorkTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | WorkTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | WorkTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | WorkTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 26 | WorkTypeBasePEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 27 | WorkTypeBasePEOUtilizableFlag | UTILIZABLE_FLAG | — | ✅ |
| 28 | WorkTypeBasePEOWorkTypeId | WORK_TYPE_ID | 🔑 | ✅ |

### [[pjf_work_types_tl|PJF_WORK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypeTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkTypeTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkTypeTransLangPEODescription | DESCRIPTION | — | ✅ |
| 4 | WorkTypeTransLangPEOLanguage | LANGUAGE | — | ✅ |
| 5 | WorkTypeTransLangPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkTypeTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | WorkTypeTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | WorkTypeTransLangPEOName | NAME | — | ✅ |
| 9 | WorkTypeTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | WorkTypeTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | WorkTypeTransLangPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
