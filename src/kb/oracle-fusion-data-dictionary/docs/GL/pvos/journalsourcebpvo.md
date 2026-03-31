---
id: DOC-GL-PVO-JournalSourceBPVO
doc_type: system-doc
title: "JournalSourceBPVO — PVO General Ledger"
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
  - JournalSourceBPVO
  - journalsourcebpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalSourceBPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Source B. Acessa as tabelas: GL_JE_SOURCES_B, GL_JE_SOURCES_TL.

**Caminho:** `FscmTopModelAM.FinGlJrnlSetupSrcAM.JournalSourceBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 2 | 2 | 12 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_sources_b|GL_JE_SOURCES_B]] — 13 atributos (1 PKs, 3 BICC)
- [[gl_je_sources_tl|GL_JE_SOURCES_TL]] — 22 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[gl_je_sources_b|GL_JE_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeSourceName | JE_SOURCE_NAME | 🔑 | ✅ |
| 2 | JrnlSrcCreatedBy | CREATED_BY | — | — |
| 3 | JrnlSrcCreationDate | CREATION_DATE | — | — |
| 4 | JrnlSrcEffectiveDateRuleCode | EFFECTIVE_DATE_RULE_CODE | — | — |
| 5 | JrnlSrcImportUsingKeyFlag | IMPORT_USING_KEY_FLAG | — | — |
| 6 | JrnlSrcJeSourceKey | JE_SOURCE_KEY | — | ✅ |
| 7 | JrnlSrcJournalApprovalFlag | JOURNAL_APPROVAL_FLAG | — | — |
| 8 | JrnlSrcJournalReferenceFlag | JOURNAL_REFERENCE_FLAG | — | — |
| 9 | JrnlSrcLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | JrnlSrcLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | JrnlSrcLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | JrnlSrcObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | JrnlSrcOverrideEditsFlag | OVERRIDE_EDITS_FLAG | — | — |

### [[gl_je_sources_tl|GL_JE_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlSrcTransLangCreatedBy | CREATED_BY | — | — |
| 2 | JrnlSrcTransLangCreationDate | CREATION_DATE | — | — |
| 3 | JrnlSrcTransLangDescription | DESCRIPTION | — | — |
| 4 | JrnlSrcTransLangJeSourceName | JE_SOURCE_NAME | — | — |
| 5 | JrnlSrcTransLangLanguage | LANGUAGE | — | — |
| 6 | JrnlSrcTransLangLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | JrnlSrcTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | JrnlSrcTransLangLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | JrnlSrcTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | JrnlSrcTransLangSourceLang | SOURCE_LANG | — | — |
| 11 | JrnlSrcTransLangUserJeSourceName | USER_JE_SOURCE_NAME | — | — |
| 12 | JrnlSrcTranslatedCreatedBy | CREATED_BY | — | ✅ |
| 13 | JrnlSrcTranslatedCreationDate | CREATION_DATE | — | ✅ |
| 14 | JrnlSrcTranslatedDescription | DESCRIPTION | — | ✅ |
| 15 | JrnlSrcTranslatedJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 16 | JrnlSrcTranslatedLanguage | LANGUAGE | 🔑 | ✅ |
| 17 | JrnlSrcTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | JrnlSrcTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | JrnlSrcTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | JrnlSrcTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | JrnlSrcTranslatedSourceLang | SOURCE_LANG | — | ✅ |
| 22 | JrnlSrcTranslatedUserJeSourceName | USER_JE_SOURCE_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
