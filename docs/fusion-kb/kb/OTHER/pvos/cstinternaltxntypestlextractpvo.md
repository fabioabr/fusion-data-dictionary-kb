---
id: DOC-OTHER-PVO-CstInternalTxnTypesTLExtractPVO
doc_type: system-doc
title: "CstInternalTxnTypesTLExtractPVO — PVO Cross-Module"
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
  - CstInternalTxnTypesTLExtractPVO
  - cstinternaltxntypestlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInternalTxnTypesTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Internal Txn Types TLExtract. Acessa as tabelas: CST_INTERNAL_TXN_TYPES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInternalTxnTypesTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 11 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[cst_internal_txn_types_tl|CST_INTERNAL_TXN_TYPES_TL]] — 12 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cst_internal_txn_types_tl|CST_INTERNAL_TXN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstInternalTxnTypesTLPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | 🔑 | ✅ |
| 2 | CstInternalTxnTypesTLPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | 🔑 | ✅ |
| 3 | CstInternalTxnTypesTLPEOBaseTxnTypeName | BASE_TXN_TYPE_NAME | — | ✅ |
| 4 | CstInternalTxnTypesTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstInternalTxnTypesTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstInternalTxnTypesTLPEODescription | DESCRIPTION | — | ✅ |
| 7 | CstInternalTxnTypesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | CstInternalTxnTypesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CstInternalTxnTypesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CstInternalTxnTypesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CstInternalTxnTypesTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | CstInternalTxnTypesTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
