---
id: DOC-OTHER-PVO-TransactionDocumentEntryTranslation
doc_type: system-doc
title: "TransactionDocumentEntryTranslation — PVO Cross-Module"
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
  - TransactionDocumentEntryTranslation
  - transactiondocumententrytranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDocumentEntryTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Document Entry Translation. Acessa as tabelas: PJF_TXN_DOC_ENTRY_TL.

**Caminho:** `FscmTopModelAM.PjfSetupTransactionsAM.TransactionDocumentEntryTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DocEntryId | DOC_ENTRY_ID | 🔑 | ✅ |
| 5 | DocEntryName | DOC_ENTRY_NAME | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
