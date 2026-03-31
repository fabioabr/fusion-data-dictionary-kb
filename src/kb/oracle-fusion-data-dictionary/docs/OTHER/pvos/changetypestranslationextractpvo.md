---
id: DOC-OTHER-PVO-ChangeTypesTranslationExtractPVO
doc_type: system-doc
title: "ChangeTypesTranslationExtractPVO — PVO Cross-Module"
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
  - ChangeTypesTranslationExtractPVO
  - changetypestranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeTypesTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Types Translation Extract. Acessa as tabelas: EGO_CHANGE_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeTypesTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[ego_change_types_tl|EGO_CHANGE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EgoChangeTypesTLPEOChangeTypeId | CHANGE_TYPE_ID | 🔑 | ✅ |
| 2 | EgoChangeTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EgoChangeTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EgoChangeTypesTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | EgoChangeTypesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | EgoChangeTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | EgoChangeTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | EgoChangeTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | EgoChangeTypesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | EgoChangeTypesTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | EgoChangeTypesTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 12 | EgoChangeTypesTLPEOTypeName | TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
