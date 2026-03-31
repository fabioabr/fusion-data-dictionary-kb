---
id: DOC-OTHER-PVO-CmrTransactionTypesTLExtractPVO
doc_type: system-doc
title: "CmrTransactionTypesTLExtractPVO — PVO Cross-Module"
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
  - CmrTransactionTypesTLExtractPVO
  - cmrtransactiontypestlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrTransactionTypesTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Transaction Types TLExtract. Acessa as tabelas: CMR_TRANSACTION_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrTransactionTypesTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_transaction_types_tl|CMR_TRANSACTION_TYPES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cmr_transaction_types_tl|CMR_TRANSACTION_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrTransactionTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CmrTransactionTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CmrTransactionTypesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | CmrTransactionTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CmrTransactionTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | CmrTransactionTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | CmrTransactionTypesTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 8 | CmrTransactionTypesTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | CmrTransactionTypesTLPEOTransactionTypeDescription | TRANSACTION_TYPE_DESCRIPTION | — | ✅ |
| 10 | CmrTransactionTypesTLPEOTransactionTypeId | TRANSACTION_TYPE_ID | 🔑 | ✅ |
| 11 | CmrTransactionTypesTLPEOTransactionTypeName | TRANSACTION_TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
