---
id: DOC-OTHER-PVO-CseAssetFailureSetTranslationExtractPVO
doc_type: system-doc
title: "CseAssetFailureSetTranslationExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureSetTranslationExtractPVO
  - cseassetfailuresettranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureSetTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Set Translation Extract. Acessa as tabelas: CSE_FAILURE_SETS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureSetTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_sets_tl|CSE_FAILURE_SETS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_failure_sets_tl|CSE_FAILURE_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | FailureSetDesc | FAILURE_SET_DESC | — | ✅ |
| 4 | FailureSetId | FAILURE_SET_ID | 🔑 | ✅ |
| 5 | FailureSetName | FAILURE_SET_NAME | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
