---
id: DOC-OTHER-PVO-JournalEncumbranceExtractPVO
doc_type: system-doc
title: "JournalEncumbranceExtractPVO — PVO Cross-Module"
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
  - JournalEncumbranceExtractPVO
  - journalencumbranceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalEncumbranceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Encumbrance Extract. Acessa as tabelas: GL_ENCUMBRANCE_TYPES_B, GL_ENCUMBRANCE_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalEncumbranceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 20 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[gl_encumbrance_types_b|GL_ENCUMBRANCE_TYPES_B]] — 15 atributos (1 PKs, 9 BICC)
- [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[gl_encumbrance_types_b|GL_ENCUMBRANCE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute2 | ATTRIBUTE2 | — | — |
| 3 | Attribute3 | ATTRIBUTE3 | — | — |
| 4 | Attribute4 | ATTRIBUTE4 | — | — |
| 5 | Attribute5 | ATTRIBUTE5 | — | — |
| 6 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 10 | EncumbranceTypeCode | ENCUMBRANCE_TYPE_CODE | — | ✅ |
| 11 | EncumbranceTypeId | ENCUMBRANCE_TYPE_ID | 🔑 | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

### [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | EncumbranceType | ENCUMBRANCE_TYPE | — | ✅ |
| 3 | JournalEncumbranceTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | JournalEncumbranceTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | JournalEncumbranceTLPEOEncumbTypeId | ENCUMBRANCE_TYPE_ID | — | ✅ |
| 6 | JournalEncumbranceTLPEOLanguage | LANGUAGE | — | ✅ |
| 7 | JournalEncumbranceTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | JournalEncumbranceTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | JournalEncumbranceTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | JournalEncumbranceTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | JournalEncumbranceTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
