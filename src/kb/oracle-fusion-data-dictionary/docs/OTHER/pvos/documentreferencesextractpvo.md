---
id: DOC-OTHER-PVO-DocumentReferencesExtractPVO
doc_type: system-doc
title: "DocumentReferencesExtractPVO — PVO Cross-Module"
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
  - DocumentReferencesExtractPVO
  - documentreferencesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DocumentReferencesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Document References Extract. Acessa as tabelas: DOO_DOCUMENT_REFERENCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.DocumentReferencesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_document_references|DOO_DOCUMENT_REFERENCES]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_document_references|DOO_DOCUMENT_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentReferencesCreatedBy | CREATED_BY | — | ✅ |
| 2 | DocumentReferencesCreationDate | CREATION_DATE | — | ✅ |
| 3 | DocumentReferencesDocAltUserKey | DOC_ALT_USER_KEY | — | ✅ |
| 4 | DocumentReferencesDocContextId | DOC_CONTEXT_ID | — | ✅ |
| 5 | DocumentReferencesDocId | DOC_ID | — | ✅ |
| 6 | DocumentReferencesDocLineAltUserKey | DOC_LINE_ALT_USER_KEY | — | ✅ |
| 7 | DocumentReferencesDocLineContextId | DOC_LINE_CONTEXT_ID | — | ✅ |
| 8 | DocumentReferencesDocLineId | DOC_LINE_ID | — | ✅ |
| 9 | DocumentReferencesDocLineUserKey | DOC_LINE_USER_KEY | — | ✅ |
| 10 | DocumentReferencesDocRefType | DOC_REF_TYPE | — | ✅ |
| 11 | DocumentReferencesDocSublineAltUserKey | DOC_SUBLINE_ALT_USER_KEY | — | ✅ |
| 12 | DocumentReferencesDocSublineContextId | DOC_SUBLINE_CONTEXT_ID | — | ✅ |
| 13 | DocumentReferencesDocSublineId | DOC_SUBLINE_ID | — | ✅ |
| 14 | DocumentReferencesDocSublineUserKey | DOC_SUBLINE_USER_KEY | — | ✅ |
| 15 | DocumentReferencesDocSystemRefId | DOC_SYSTEM_REF_ID | 🔑 | ✅ |
| 16 | DocumentReferencesDocUserKey | DOC_USER_KEY | — | ✅ |
| 17 | DocumentReferencesFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 18 | DocumentReferencesHeaderId | HEADER_ID | — | ✅ |
| 19 | DocumentReferencesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | DocumentReferencesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | DocumentReferencesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | DocumentReferencesLineId | LINE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
