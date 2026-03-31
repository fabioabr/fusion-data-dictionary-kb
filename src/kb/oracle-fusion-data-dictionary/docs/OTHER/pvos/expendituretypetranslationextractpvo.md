---
id: DOC-OTHER-PVO-ExpenditureTypeTranslationExtractPVO
doc_type: system-doc
title: "ExpenditureTypeTranslationExtractPVO — PVO Cross-Module"
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
  - ExpenditureTypeTranslationExtractPVO
  - expendituretypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Translation Extract. Acessa as tabelas: PJF_EXP_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_exp_types_tl|PJF_EXP_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeTranslationPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | 🔑 | ✅ |
| 5 | ExpenditureTypeTranslationPEOExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | ExpenditureTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ExpenditureTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ExpenditureTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ExpenditureTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ExpenditureTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
