---
id: DOC-OTHER-PVO-InvTxnReasonExtractPVO
doc_type: system-doc
title: "InvTxnReasonExtractPVO — PVO Cross-Module"
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
  - InvTxnReasonExtractPVO
  - invtxnreasonextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvTxnReasonExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Txn Reason Extract. Acessa as tabelas: INV_TRANSACTION_REASONS_VL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvTxnReasonExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_transaction_reasons_vl|INV_TRANSACTION_REASONS_VL]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[inv_transaction_reasons_vl|INV_TRANSACTION_REASONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisableDate | DISABLE_DATE | — | ✅ |
| 5 | EnableDate | ENABLE_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ReasonContextCode | REASON_CONTEXT_CODE | — | ✅ |
| 11 | ReasonId | REASON_ID | 🔑 | ✅ |
| 12 | ReasonName | REASON_NAME | — | ✅ |
| 13 | ReasonType | REASON_TYPE | — | ✅ |
| 14 | ReasonTypeDisplay | REASON_TYPE_DISPLAY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
