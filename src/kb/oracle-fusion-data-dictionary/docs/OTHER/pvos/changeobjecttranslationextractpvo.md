---
id: DOC-OTHER-PVO-ChangeObjectTranslationExtractPVO
doc_type: system-doc
title: "ChangeObjectTranslationExtractPVO — PVO Cross-Module"
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
  - ChangeObjectTranslationExtractPVO
  - changeobjecttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeObjectTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Object Translation Extract. Acessa as tabelas: EGO_ENGINEERING_CHANGES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeObjectTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ego_engineering_changes_tl|EGO_ENGINEERING_CHANGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeObjectTLPEOCancellationComments | CANCELLATION_COMMENTS | — | ✅ |
| 2 | ChangeObjectTLPEOChangeId | CHANGE_ID | 🔑 | ✅ |
| 3 | ChangeObjectTLPEOChangeName | CHANGE_NAME | — | ✅ |
| 4 | ChangeObjectTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ChangeObjectTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ChangeObjectTLPEODescription | DESCRIPTION | — | ✅ |
| 7 | ChangeObjectTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | ChangeObjectTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ChangeObjectTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ChangeObjectTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ChangeObjectTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ChangeObjectTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
