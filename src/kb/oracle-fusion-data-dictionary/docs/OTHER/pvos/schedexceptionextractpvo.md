---
id: DOC-OTHER-PVO-SchedExceptionExtractPVO
doc_type: system-doc
title: "SchedExceptionExtractPVO — PVO Cross-Module"
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
  - SchedExceptionExtractPVO
  - schedexceptionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedExceptionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sched Exception Extract. Acessa as tabelas: ZMM_SR_AVL_EXCEPTIONS_B, ZMM_SR_AVL_EXCEPTIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.SchedExceptionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 2 | 1 | 46 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_avl_exceptions_b|ZMM_SR_AVL_EXCEPTIONS_B]] — 44 atributos (1 PKs, 44 BICC)
- [[zmm_sr_avl_exceptions_tl|ZMM_SR_AVL_EXCEPTIONS_TL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_avl_exceptions_b|ZMM_SR_AVL_EXCEPTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvlExceptionId | AVL_EXCEPTION_ID | 🔑 | ✅ |
| 2 | SchedExceptionPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 3 | SchedExceptionPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 4 | SchedExceptionPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 5 | SchedExceptionPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 6 | SchedExceptionPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 7 | SchedExceptionPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 8 | SchedExceptionPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 9 | SchedExceptionPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 10 | SchedExceptionPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 11 | SchedExceptionPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 12 | SchedExceptionPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 13 | SchedExceptionPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 14 | SchedExceptionPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 15 | SchedExceptionPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 16 | SchedExceptionPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 17 | SchedExceptionPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 18 | SchedExceptionPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 19 | SchedExceptionPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 20 | SchedExceptionPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 21 | SchedExceptionPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 22 | SchedExceptionPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 23 | SchedExceptionPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 24 | SchedExceptionPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 25 | SchedExceptionPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 26 | SchedExceptionPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 27 | SchedExceptionPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 28 | SchedExceptionPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 29 | SchedExceptionPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 30 | SchedExceptionPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 31 | SchedExceptionPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 32 | SchedExceptionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | SchedExceptionPEOAvailabilityCode | AVAILABILITY_CODE | — | ✅ |
| 34 | SchedExceptionPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 35 | SchedExceptionPEOCreatedBy | CREATED_BY | — | ✅ |
| 36 | SchedExceptionPEOCreationDate | CREATION_DATE | — | ✅ |
| 37 | SchedExceptionPEOEndDateTime | END_DATE_TIME | — | ✅ |
| 38 | SchedExceptionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | SchedExceptionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | SchedExceptionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | SchedExceptionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 42 | SchedExceptionPEOShortTxt | SHORT_TXT | — | ✅ |
| 43 | SchedExceptionPEOStartDateTime | START_DATE_TIME | — | ✅ |
| 44 | SchedExceptionPEOWholeDayFlag | WHOLE_DAY_FLAG | — | ✅ |

### [[zmm_sr_avl_exceptions_tl|ZMM_SR_AVL_EXCEPTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedExceptionTranslationPEOAvlExcpDesc | AVL_EXCP_DESC | — | ✅ |
| 2 | SchedExceptionTranslationPEOAvlExcpName | AVL_EXCP_NAME | — | ✅ |
| 3 | SchedExceptionTranslationPEOLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
