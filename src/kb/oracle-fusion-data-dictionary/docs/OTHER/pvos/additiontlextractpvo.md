---
id: DOC-OTHER-PVO-AdditionTLExtractPVO
doc_type: system-doc
title: "AdditionTLExtractPVO — PVO Cross-Module"
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
  - AdditionTLExtractPVO
  - additiontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdditionTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Addition TLExtract. Acessa as tabelas: FA_ADDITIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AdditionTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_tl|FA_ADDITIONS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[fa_additions_tl|FA_ADDITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionTranslationAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | AdditionTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | AdditionTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | AdditionTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | AdditionTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AdditionTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AdditionTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AdditionTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AdditionTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AdditionTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
