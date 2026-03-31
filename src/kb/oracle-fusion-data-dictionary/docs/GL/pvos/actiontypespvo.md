---
id: DOC-GL-PVO-ActionTypesPVO
doc_type: system-doc
title: "ActionTypesPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ActionTypesPVO
  - actiontypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Types. Acessa as tabelas: PER_ACTION_TYPES_B, PER_ACTION_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 2 | 12 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_types_b|PER_ACTION_TYPES_B]] — 10 atributos (1 PKs, 8 BICC)
- [[per_action_types_tl|PER_ACTION_TYPES_TL]] — 10 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_action_types_b|PER_ACTION_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTypeId | ACTION_TYPE_ID | 🔑 | ✅ |
| 2 | ActionTypesPEOActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 3 | ActionTypesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | ActionTypesPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ActionTypesPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ActionTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ActionTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ActionTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ActionTypesPEOModuleId | MODULE_ID | — | — |
| 10 | ActionTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_action_types_tl|PER_ACTION_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTypesTranslationPEOActionTypeId | ACTION_TYPE_ID | — | — |
| 2 | ActionTypesTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ActionTypesTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ActionTypesTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ActionTypesTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ActionTypesTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ActionTypesTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ActionTypesTranslationPEOMeaning | MEANING | — | ✅ |
| 9 | ActionTypesTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ActionTypesTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
