---
id: DOC-OTHER-PVO-TransactionDocumentTranslationExtractPVO
doc_type: system-doc
title: "TransactionDocumentTranslationExtractPVO — PVO Cross-Module"
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
  - TransactionDocumentTranslationExtractPVO
  - transactiondocumenttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionDocumentTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Document Translation Extract. Acessa as tabelas: PJF_TXN_DOCUMENT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.TransactionDocumentTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_txn_document_tl|PJF_TXN_DOCUMENT_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_txn_document_tl|PJF_TXN_DOCUMENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionDocumentTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionDocumentTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TransactionDocumentTLPEODocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 5 | TransactionDocumentTLPEODocumentName | DOCUMENT_NAME | — | ✅ |
| 6 | TransactionDocumentTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | TransactionDocumentTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TransactionDocumentTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | TransactionDocumentTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | TransactionDocumentTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | TransactionDocumentTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
