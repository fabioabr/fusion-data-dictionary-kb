---
id: DOC-OTHER-PVO-WorkType
doc_type: system-doc
title: "WorkType — PVO Cross-Module"
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
  - WorkType
  - worktype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkType

## 📌 Visão Geral

View Object para extração BICC de dados de Work Type. Acessa as tabelas: PJF_WORK_TYPES_B, PJF_WORK_TYPES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupProjectsAM.WorkType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 1 | 13 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_work_types_b|PJF_WORK_TYPES_B]] — 12 atributos (1 PKs, 10 BICC)
- [[pjf_work_types_tl|PJF_WORK_TYPES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[pjf_work_types_b|PJF_WORK_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypeBasePEOBillableCapitalizableFlag | BILLABLE_CAPITALIZABLE_FLAG | — | ✅ |
| 2 | WorkTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | WorkTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WorkTypeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | WorkTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | WorkTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | WorkTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | WorkTypeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 10 | WorkTypeBasePEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 11 | WorkTypeBasePEOUtilizableFlag | UTILIZABLE_FLAG | — | — |
| 12 | WorkTypeId | WORK_TYPE_ID | 🔑 | ✅ |

### [[pjf_work_types_tl|PJF_WORK_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | WorkTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | WorkTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | WorkTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | WorkTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | WorkTypeTranslationPEOName | NAME | — | ✅ |
| 9 | WorkTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | WorkTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 11 | WorkTypeTranslationPEOWorkTypeId | WORK_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
