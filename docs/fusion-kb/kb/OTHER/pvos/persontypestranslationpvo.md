---
id: DOC-OTHER-PVO-PersonTypesTranslationPVO
doc_type: system-doc
title: "PersonTypesTranslationPVO — PVO Cross-Module"
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
  - PersonTypesTranslationPVO
  - persontypestranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonTypesTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Types Translation. Acessa as tabelas: PER_PERSON_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonTypesTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 8 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_types_tl|PER_PERSON_TYPES_TL]] — 10 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[per_person_types_tl|PER_PERSON_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | PersonTypeId | PERSON_TYPE_ID | 🔑 | ✅ |
| 3 | PersonTypesTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PersonTypesTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PersonTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PersonTypesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PersonTypesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PersonTypesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | PersonTypesTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | PersonTypesTranslationPEOUserPersonType | USER_PERSON_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
