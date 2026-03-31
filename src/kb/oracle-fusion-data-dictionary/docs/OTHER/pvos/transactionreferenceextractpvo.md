---
id: DOC-OTHER-PVO-TransactionReferenceExtractPVO
doc_type: system-doc
title: "TransactionReferenceExtractPVO — PVO Cross-Module"
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
  - TransactionReferenceExtractPVO
  - transactionreferenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionReferenceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Reference Extract. Acessa as tabelas: FA_TRX_REFERENCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.TransactionReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_trx_references|FA_TRX_REFERENCES]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[fa_trx_references|FA_TRX_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionReferenceBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 2 | TransactionReferenceCreatedBy | CREATED_BY | — | ✅ |
| 3 | TransactionReferenceCreationDate | CREATION_DATE | — | ✅ |
| 4 | TransactionReferenceDestAmortizationStartDate | DEST_AMORTIZATION_START_DATE | — | ✅ |
| 5 | TransactionReferenceDestAssetId | DEST_ASSET_ID | — | ✅ |
| 6 | TransactionReferenceDestEofyReserve | DEST_EOFY_RESERVE | — | ✅ |
| 7 | TransactionReferenceDestExpenseAmount | DEST_EXPENSE_AMOUNT | — | ✅ |
| 8 | TransactionReferenceDestTransactionHeaderId | DEST_TRANSACTION_HEADER_ID | — | ✅ |
| 9 | TransactionReferenceDestTransactionSubtype | DEST_TRANSACTION_SUBTYPE | — | ✅ |
| 10 | TransactionReferenceEventId | EVENT_ID | — | ✅ |
| 11 | TransactionReferenceInvoiceTransactionId | INVOICE_TRANSACTION_ID | — | ✅ |
| 12 | TransactionReferenceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | TransactionReferenceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | TransactionReferenceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | TransactionReferenceMemberAssetId | MEMBER_ASSET_ID | — | ✅ |
| 16 | TransactionReferenceMemberTransactionHeaderId | MEMBER_TRANSACTION_HEADER_ID | — | ✅ |
| 17 | TransactionReferenceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | TransactionReferenceReserveTransferAmount | RESERVE_TRANSFER_AMOUNT | — | ✅ |
| 19 | TransactionReferenceSrcAmortizationStartDate | SRC_AMORTIZATION_START_DATE | — | ✅ |
| 20 | TransactionReferenceSrcAssetId | SRC_ASSET_ID | — | ✅ |
| 21 | TransactionReferenceSrcEofyReserve | SRC_EOFY_RESERVE | — | ✅ |
| 22 | TransactionReferenceSrcExpenseAmount | SRC_EXPENSE_AMOUNT | — | ✅ |
| 23 | TransactionReferenceSrcTransactionHeaderId | SRC_TRANSACTION_HEADER_ID | — | ✅ |
| 24 | TransactionReferenceSrcTransactionSubtype | SRC_TRANSACTION_SUBTYPE | — | ✅ |
| 25 | TransactionReferenceTransactionType | TRANSACTION_TYPE | — | ✅ |
| 26 | TransactionReferenceTrxReferenceId | TRX_REFERENCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
