---
id: DOC-OTHER-PVO-JournalImportReferenceExtractPVO
doc_type: system-doc
title: "JournalImportReferenceExtractPVO — PVO Cross-Module"
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
  - JournalImportReferenceExtractPVO
  - journalimportreferenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalImportReferenceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Import Reference Extract. Acessa as tabelas: GL_IMPORT_REFERENCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalImportReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 14 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_import_references|GL_IMPORT_REFERENCES]] — 23 atributos (14 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[gl_import_references|GL_IMPORT_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlImportReferencesCreatedBy | CREATED_BY | — | ✅ |
| 2 | GlImportReferencesCreationDate | CREATION_DATE | — | ✅ |
| 3 | GlImportReferencesGlSlLinkId | GL_SL_LINK_ID | 🔑 | ✅ |
| 4 | GlImportReferencesGlSlLinkTable | GL_SL_LINK_TABLE | 🔑 | ✅ |
| 5 | GlImportReferencesJeBatchId | JE_BATCH_ID | — | ✅ |
| 6 | GlImportReferencesJeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 7 | GlImportReferencesJeLineNum | JE_LINE_NUM | 🔑 | ✅ |
| 8 | GlImportReferencesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GlImportReferencesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | GlImportReferencesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | GlImportReferencesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | GlImportReferencesReference1 | REFERENCE_1 | 🔑 | ✅ |
| 13 | GlImportReferencesReference10 | REFERENCE_10 | 🔑 | ✅ |
| 14 | GlImportReferencesReference2 | REFERENCE_2 | 🔑 | ✅ |
| 15 | GlImportReferencesReference3 | REFERENCE_3 | 🔑 | ✅ |
| 16 | GlImportReferencesReference4 | REFERENCE_4 | 🔑 | ✅ |
| 17 | GlImportReferencesReference5 | REFERENCE_5 | 🔑 | ✅ |
| 18 | GlImportReferencesReference6 | REFERENCE_6 | 🔑 | ✅ |
| 19 | GlImportReferencesReference7 | REFERENCE_7 | 🔑 | ✅ |
| 20 | GlImportReferencesReference8 | REFERENCE_8 | 🔑 | ✅ |
| 21 | GlImportReferencesReference9 | REFERENCE_9 | 🔑 | ✅ |
| 22 | GlImportReferencesSubledgerDocSequenceId | SUBLEDGER_DOC_SEQUENCE_ID | — | ✅ |
| 23 | GlImportReferencesSubledgerDocSequenceValue | SUBLEDGER_DOC_SEQUENCE_VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
