---
id: DOC-OTHER-PVO-VcsDocumentDefinitionTranslationsExtractPVO
doc_type: system-doc
title: "VcsDocumentDefinitionTranslationsExtractPVO — PVO Cross-Module"
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
  - VcsDocumentDefinitionTranslationsExtractPVO
  - vcsdocumentdefinitiontranslationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VcsDocumentDefinitionTranslationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vcs Document Definition Translations Extract. Acessa as tabelas: VCS_DOCUMENT_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.VcsDemandBiccExtractAM.VcsDocumentDefinitionTranslationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[vcs_document_definitions_tl|VCS_DOCUMENT_DEFINITIONS_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[vcs_document_definitions_tl|VCS_DOCUMENT_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DCDocumentDefinitionTranslationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DCDocumentDefinitionTranslationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DCDocumentDefinitionTranslationsPEODocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 4 | DCDocumentDefinitionTranslationsPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | DCDocumentDefinitionTranslationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DCDocumentDefinitionTranslationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DCDocumentDefinitionTranslationsPEOName | NAME | — | ✅ |
| 8 | DCDocumentDefinitionTranslationsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | DCDocumentDefinitionTranslationsPEOSourceLanguage | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
