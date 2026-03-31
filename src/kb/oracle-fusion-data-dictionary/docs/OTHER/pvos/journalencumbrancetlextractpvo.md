---
id: DOC-OTHER-PVO-JournalEncumbranceTLExtractPVO
doc_type: system-doc
title: "JournalEncumbranceTLExtractPVO — PVO Cross-Module"
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
  - JournalEncumbranceTLExtractPVO
  - journalencumbrancetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalEncumbranceTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Encumbrance TLExtract. Acessa as tabelas: GL_ENCUMBRANCE_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalEncumbranceTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gl_encumbrance_types_tl|GL_ENCUMBRANCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalEncumbranceTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | JournalEncumbranceTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | JournalEncumbranceTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | JournalEncumbranceTLPEOEncumbranceType | ENCUMBRANCE_TYPE | — | ✅ |
| 5 | JournalEncumbranceTLPEOEncumbranceTypeId | ENCUMBRANCE_TYPE_ID | 🔑 | ✅ |
| 6 | JournalEncumbranceTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | JournalEncumbranceTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | JournalEncumbranceTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | JournalEncumbranceTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | JournalEncumbranceTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | JournalEncumbranceTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | JournalEncumbranceTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
