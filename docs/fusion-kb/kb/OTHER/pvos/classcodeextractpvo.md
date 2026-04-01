---
id: DOC-OTHER-PVO-ClassCodeExtractPVO
doc_type: system-doc
title: "ClassCodeExtractPVO — PVO Cross-Module"
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
  - ClassCodeExtractPVO
  - classcodeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassCodeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Class Code Extract. Acessa as tabelas: PJF_CLASS_CODES_B, PJF_CLASS_CODES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ClassCodeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 2 | 1 | 21 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_class_codes_b|PJF_CLASS_CODES_B]] — 26 atributos (1 PKs, 10 BICC)
- [[pjf_class_codes_tl|PJF_CLASS_CODES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_class_codes_b|PJF_CLASS_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCodeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ClassCodeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ClassCodeBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ClassCodeBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ClassCodeBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ClassCodeBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ClassCodeBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ClassCodeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ClassCodeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ClassCodeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ClassCodeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ClassCodeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ClassCodeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ClassCodeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ClassCodeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ClassCodeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ClassCodeBasePEOClassCategoryId | CLASS_CATEGORY_ID | — | ✅ |
| 18 | ClassCodeBasePEOClassCodeId | CLASS_CODE_ID | 🔑 | ✅ |
| 19 | ClassCodeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 20 | ClassCodeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 21 | ClassCodeBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 22 | ClassCodeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ClassCodeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | ClassCodeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ClassCodeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ClassCodeBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_class_codes_tl|PJF_CLASS_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassCodeTransLangPEOClassCode | CLASS_CODE | — | ✅ |
| 2 | ClassCodeTransLangPEOClassCodeId | CLASS_CODE_ID | — | ✅ |
| 3 | ClassCodeTransLangPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ClassCodeTransLangPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ClassCodeTransLangPEODescription | DESCRIPTION | — | ✅ |
| 6 | ClassCodeTransLangPEOLanguage | LANGUAGE | — | ✅ |
| 7 | ClassCodeTransLangPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | ClassCodeTransLangPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ClassCodeTransLangPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ClassCodeTransLangPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ClassCodeTransLangPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
