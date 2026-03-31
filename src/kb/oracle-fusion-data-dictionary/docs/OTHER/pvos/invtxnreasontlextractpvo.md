---
id: DOC-OTHER-PVO-InvTxnReasonTLExtractPVO
doc_type: system-doc
title: "InvTxnReasonTLExtractPVO — PVO Cross-Module"
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
  - InvTxnReasonTLExtractPVO
  - invtxnreasontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvTxnReasonTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Txn Reason TLExtract. Acessa as tabelas: INV_TRANSACTION_REASONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvTxnReasonTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transaction_reasons_tl|INV_TRANSACTION_REASONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[inv_transaction_reasons_tl|INV_TRANSACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTxnReasonTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvTxnReasonTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvTxnReasonTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvTxnReasonTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | InvTxnReasonTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvTxnReasonTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | InvTxnReasonTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | InvTxnReasonTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | InvTxnReasonTLPEOReasonId | REASON_ID | 🔑 | ✅ |
| 10 | InvTxnReasonTLPEOReasonName | REASON_NAME | — | ✅ |
| 11 | InvTxnReasonTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
