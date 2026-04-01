---
id: DOC-OTHER-PVO-JournalSourceTLExtractPVO
doc_type: system-doc
title: "JournalSourceTLExtractPVO — PVO Cross-Module"
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
  - JournalSourceTLExtractPVO
  - journalsourcetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalSourceTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Source TLExtract. Acessa as tabelas: GL_JE_SOURCES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalSourceTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_sources_tl|GL_JE_SOURCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gl_je_sources_tl|GL_JE_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlSrcTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | JrnlSrcTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | JrnlSrcTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | JrnlSrcTranslationJeSourceName | JE_SOURCE_NAME | 🔑 | ✅ |
| 5 | JrnlSrcTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | JrnlSrcTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JrnlSrcTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | JrnlSrcTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | JrnlSrcTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | JrnlSrcTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 11 | JrnlSrcTranslationUserJeSourceName | USER_JE_SOURCE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
