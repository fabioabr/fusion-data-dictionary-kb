---
id: DOC-GL-PVO-ActionsTranslationPVO
doc_type: system-doc
title: "ActionsTranslationPVO — PVO General Ledger"
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
  - ActionsTranslationPVO
  - actionstranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionsTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Actions Translation. Acessa as tabelas: PER_ACTIONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionsTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 11 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[per_actions_tl|PER_ACTIONS_TL]] — 13 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[per_actions_tl|PER_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ActionTranslationPEOActionName | ACTION_NAME | — | ✅ |
| 3 | ActionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ActionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ActionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | ActionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ActionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ActionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ActionTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | ActionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 13 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
