---
id: DOC-OTHER-PVO-ActionTypesTranslationPVO
doc_type: system-doc
title: "ActionTypesTranslationPVO — PVO Cross-Module"
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
  - ActionTypesTranslationPVO
  - actiontypestranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionTypesTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Types Translation. Acessa as tabelas: PER_ACTION_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionTypesTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 3 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_types_tl|PER_ACTION_TYPES_TL]] — 10 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_action_types_tl|PER_ACTION_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTypeId | ACTION_TYPE_ID | 🔑 | ✅ |
| 2 | ActionTypesTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ActionTypesTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ActionTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ActionTypesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ActionTypesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ActionTypesTranslationPEOMeaning | MEANING | — | — |
| 8 | ActionTypesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ActionTypesTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 10 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
