---
id: DOC-OTHER-PVO-ChangeActionsTranslationExtractPVO
doc_type: system-doc
title: "ChangeActionsTranslationExtractPVO — PVO Cross-Module"
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
  - ChangeActionsTranslationExtractPVO
  - changeactionstranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeActionsTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Actions Translation Extract. Acessa as tabelas: EGO_CHANGE_ACTIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeActionsTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_actions_tl|EGO_CHANGE_ACTIONS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ego_change_actions_tl|EGO_CHANGE_ACTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeActionsTranslationPEOActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ChangeActionsTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ChangeActionsTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ChangeActionsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ChangeActionsTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ChangeActionsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ChangeActionsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ChangeActionsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ChangeActionsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ChangeActionsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
