---
id: DOC-OTHER-PVO-ExpenditureTypeTranslation
doc_type: system-doc
title: "ExpenditureTypeTranslation — PVO Cross-Module"
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
  - ExpenditureTypeTranslation
  - expendituretypetranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Translation. Acessa as tabelas: PJF_EXP_TYPES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.ExpenditureTypeTranslation`

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
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeId | EXPENDITURE_TYPE_ID | 🔑 | ✅ |
| 5 | ExpenditureTypeName | EXPENDITURE_TYPE_NAME | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
