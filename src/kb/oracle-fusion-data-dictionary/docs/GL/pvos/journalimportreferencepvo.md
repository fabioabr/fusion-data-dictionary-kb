---
id: DOC-GL-PVO-JournalImportReferencePVO
doc_type: system-doc
title: "JournalImportReferencePVO — PVO General Ledger"
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
  - JournalImportReferencePVO
  - journalimportreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalImportReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Import Reference. Acessa as tabelas: GL_IMPORT_REFERENCES, GL_JE_HEADERS.

**Caminho:** `FscmTopModelAM.FinGlProgramJrnlImportAM.JournalImportReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 4 | 9 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[gl_import_references|GL_IMPORT_REFERENCES]] — 23 atributos (4 PKs, 6 BICC)
- [[gl_je_headers|GL_JE_HEADERS]] — 8 atributos (3 BICC)

---

## ⚙️ Atributos

### [[gl_import_references|GL_IMPORT_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | GlSlLinkId | GL_SL_LINK_ID | 🔑 | ✅ |
| 4 | GlSlLinkTable | GL_SL_LINK_TABLE | 🔑 | ✅ |
| 5 | JeBatchId | JE_BATCH_ID | — | — |
| 6 | JeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 7 | JeLineNum | JE_LINE_NUM | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | Reference1 | REFERENCE_1 | — | — |
| 13 | Reference10 | REFERENCE_10 | — | — |
| 14 | Reference2 | REFERENCE_2 | — | — |
| 15 | Reference3 | REFERENCE_3 | — | — |
| 16 | Reference4 | REFERENCE_4 | — | — |
| 17 | Reference5 | REFERENCE_5 | — | — |
| 18 | Reference6 | REFERENCE_6 | — | — |
| 19 | Reference7 | REFERENCE_7 | — | — |
| 20 | Reference8 | REFERENCE_8 | — | — |
| 21 | Reference9 | REFERENCE_9 | — | — |
| 22 | SubledgerDocSequenceId | SUBLEDGER_DOC_SEQUENCE_ID | — | — |
| 23 | SubledgerDocSequenceValue | SUBLEDGER_DOC_SEQUENCE_VALUE | — | — |

### [[gl_je_headers|GL_JE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GjhLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 2 | GjhLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 3 | JournalCreatedBy | CREATED_BY | — | — |
| 4 | JournalCreationDate | CREATION_DATE | — | — |
| 5 | JrnlHdrJeHeaderId | JE_HEADER_ID | — | — |
| 6 | JrnlHdrObjectVerNum | OBJECT_VERSION_NUMBER | — | — |
| 7 | LedgerId | LEDGER_ID | — | ✅ |
| 8 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
