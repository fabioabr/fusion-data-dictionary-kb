---
id: DOC-OTHER-PVO-ExpenditureTypeClassTranslationExtractPVO
doc_type: system-doc
title: "ExpenditureTypeClassTranslationExtractPVO — PVO Cross-Module"
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
  - ExpenditureTypeClassTranslationExtractPVO
  - expendituretypeclasstranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureTypeClassTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Type Class Translation Extract. Acessa as tabelas: PJF_SYSTEM_LINKAGES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ExpenditureTypeClassTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_system_linkages_tl|PJF_SYSTEM_LINKAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeClassTransCreatedBy | CREATED_BY | — | ✅ |
| 2 | ExpenditureTypeClassTransCreationDate | CREATION_DATE | — | ✅ |
| 3 | ExpenditureTypeClassTransDescription | DESCRIPTION | — | ✅ |
| 4 | ExpenditureTypeClassTransFunction1 | FUNCTION | 🔑 | ✅ |
| 5 | ExpenditureTypeClassTransLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ExpenditureTypeClassTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ExpenditureTypeClassTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ExpenditureTypeClassTransLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ExpenditureTypeClassTransMeaning | MEANING | — | ✅ |
| 10 | ExpenditureTypeClassTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ExpenditureTypeClassTransSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
