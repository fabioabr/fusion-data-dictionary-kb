---
id: DOC-OTHER-PVO-TransactionDocumentEntryTranslationExtractPVO
doc_type: system-doc
title: "TransactionDocumentEntryTranslationExtractPVO — PVO Cross-Module"
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
  - TransactionDocumentEntryTranslationExtractPVO
  - transactiondocumententrytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDocumentEntryTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Document Entry Translation Extract. Acessa as tabelas: PJF_TXN_DOC_ENTRY_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionDocumentEntryTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_doc_entry_tl|PJF_TXN_DOC_ENTRY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentEntryTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionDocumentEntryTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionDocumentEntryTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionDocumentEntryTLPEODocEntryId | DOC_ENTRY_ID | 🔑 | ✅ |
| 5 | TransactionDocumentEntryTLPEODocEntryName | DOC_ENTRY_NAME | — | ✅ |
| 6 | TransactionDocumentEntryTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | TransactionDocumentEntryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TransactionDocumentEntryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | TransactionDocumentEntryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | TransactionDocumentEntryTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TransactionDocumentEntryTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
