---
id: DOC-OTHER-PVO-FosTransactionTypeTranslationExtractPVO
doc_type: system-doc
title: "FosTransactionTypeTranslationExtractPVO — PVO Cross-Module"
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
  - FosTransactionTypeTranslationExtractPVO
  - fostransactiontypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTransactionTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Transaction Type Translation Extract. Acessa as tabelas: FOS_TRANSACTION_TYPE_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTransactionTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_transaction_type_tl|FOS_TRANSACTION_TYPE_TL]] — 14 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fos_transaction_type_tl|FOS_TRANSACTION_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TransactionTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TransactionTypeTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | TransactionTypeTLPEOForwardTransactionName | FORWARD_TRANSACTION_NAME | — | ✅ |
| 5 | TransactionTypeTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | TransactionTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TransactionTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TransactionTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TransactionTypeTLPEOReturnTransactionName | RETURN_TRANSACTION_NAME | — | ✅ |
| 11 | TransactionTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | TransactionTypeTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 13 | TransactionTypeTLPEOTransactionName | TRANSACTION_NAME | — | ✅ |
| 14 | TransactionTypeTLPEOTransactionTypeId | TRANSACTION_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
