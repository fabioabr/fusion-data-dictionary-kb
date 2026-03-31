---
id: DOC-OTHER-PVO-SourcesAllTranslationPVO
doc_type: system-doc
title: "SourcesAllTranslationPVO — PVO Cross-Module"
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
  - SourcesAllTranslationPVO
  - sourcesalltranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcesAllTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sources All Translation. Acessa as tabelas: HRT_SOURCES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileContentLibraryAM.SourcesAllTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_sources_tl|HRT_SOURCES_TL]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hrt_sources_tl|HRT_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SourceDescription | SOURCE_DESCRIPTION | — | ✅ |
| 10 | SourceId | SOURCE_ID | 🔑 | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
