---
id: DOC-OTHER-PVO-JournalSourceExtractPVO
doc_type: system-doc
title: "JournalSourceExtractPVO — PVO Cross-Module"
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
  - JournalSourceExtractPVO
  - journalsourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalSourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Source Extract. Acessa as tabelas: GL_JE_SOURCES_B, GL_JE_SOURCES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalSourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 23 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_sources_b|GL_JE_SOURCES_B]] — 20 atributos (1 PKs, 13 BICC)
- [[gl_je_sources_tl|GL_JE_SOURCES_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[gl_je_sources_b|GL_JE_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalSourceAttribute1 | ATTRIBUTE1 | — | — |
| 2 | JournalSourceAttribute2 | ATTRIBUTE2 | — | — |
| 3 | JournalSourceAttribute3 | ATTRIBUTE3 | — | — |
| 4 | JournalSourceAttribute4 | ATTRIBUTE4 | — | — |
| 5 | JournalSourceAttribute5 | ATTRIBUTE5 | — | — |
| 6 | JournalSourceAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | JournalSourceCreatedBy | CREATED_BY | — | ✅ |
| 8 | JournalSourceCreationDate | CREATION_DATE | — | ✅ |
| 9 | JournalSourceEffDateRuleCode | EFFECTIVE_DATE_RULE_CODE | — | ✅ |
| 10 | JournalSourceImpUsingKeyFlag | IMPORT_USING_KEY_FLAG | — | ✅ |
| 11 | JournalSourceJeSourceKey | JE_SOURCE_KEY | — | ✅ |
| 12 | JournalSourceJeSourceName | JE_SOURCE_NAME | 🔑 | ✅ |
| 13 | JournalSourceJournalApprvlFlag | JOURNAL_APPROVAL_FLAG | — | ✅ |
| 14 | JournalSourceJournalRefFlag | JOURNAL_REFERENCE_FLAG | — | ✅ |
| 15 | JournalSourceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | JournalSourceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | JournalSourceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | JournalSourceObjectVersionNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | JournalSourceOverrideEditsFlag | OVERRIDE_EDITS_FLAG | — | ✅ |
| 20 | JournalSourceXlaApprovalFlag | XLA_APPROVAL_FLAG | — | — |

### [[gl_je_sources_tl|GL_JE_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JrnlSrcTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | JrnlSrcTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | JrnlSrcTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | JrnlSrcTransLangJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 5 | JrnlSrcTransLangLanguage | LANGUAGE | — | ✅ |
| 6 | JrnlSrcTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | JrnlSrcTransLangLastUpdateLog | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | JrnlSrcTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | JrnlSrcTransLangSourceLang | SOURCE_LANG | — | ✅ |
| 10 | JrnlSrcTransLangUserJeSrcName | USER_JE_SOURCE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
