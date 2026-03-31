---
id: DOC-OTHER-PVO-SubledgerJournalTransactionEntityExtractPVO
doc_type: system-doc
title: "SubledgerJournalTransactionEntityExtractPVO — PVO Cross-Module"
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
  - SubledgerJournalTransactionEntityExtractPVO
  - subledgerjournaltransactionentityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerJournalTransactionEntityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Journal Transaction Entity Extract. Acessa as tabelas: XLA_TRANSACTION_ENTITIES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerJournalTransactionEntityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 29 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]] — 30 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[xla_transaction_entities|XLA_TRANSACTION_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionApplicationId | APPLICATION_ID | — | ✅ |
| 2 | TransactionCreatedBy | CREATED_BY | — | ✅ |
| 3 | TransactionCreationDate | CREATION_DATE | — | ✅ |
| 4 | TransactionEntityCode | ENTITY_CODE | — | ✅ |
| 5 | TransactionEntityId | ENTITY_ID | 🔑 | ✅ |
| 6 | TransactionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TransactionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TransactionLedgerId | LEDGER_ID | — | ✅ |
| 10 | TransactionLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 11 | TransactionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | TransactionOriginalTransactionNumber | ORIGINAL_TRANSACTION_NUMBER | — | — |
| 13 | TransactionSecurityIdChar1 | SECURITY_ID_CHAR_1 | — | ✅ |
| 14 | TransactionSecurityIdChar2 | SECURITY_ID_CHAR_2 | — | ✅ |
| 15 | TransactionSecurityIdChar3 | SECURITY_ID_CHAR_3 | — | ✅ |
| 16 | TransactionSecurityIdInt1 | SECURITY_ID_INT_1 | — | ✅ |
| 17 | TransactionSecurityIdInt2 | SECURITY_ID_INT_2 | — | ✅ |
| 18 | TransactionSecurityIdInt3 | SECURITY_ID_INT_3 | — | ✅ |
| 19 | TransactionSourceApplicationId | SOURCE_APPLICATION_ID | — | ✅ |
| 20 | TransactionSourceIdChar1 | SOURCE_ID_CHAR_1 | — | ✅ |
| 21 | TransactionSourceIdChar2 | SOURCE_ID_CHAR_2 | — | ✅ |
| 22 | TransactionSourceIdChar3 | SOURCE_ID_CHAR_3 | — | ✅ |
| 23 | TransactionSourceIdChar4 | SOURCE_ID_CHAR_4 | — | ✅ |
| 24 | TransactionSourceIdInt1 | SOURCE_ID_INT_1 | — | ✅ |
| 25 | TransactionSourceIdInt2 | SOURCE_ID_INT_2 | — | ✅ |
| 26 | TransactionSourceIdInt3 | SOURCE_ID_INT_3 | — | ✅ |
| 27 | TransactionSourceIdInt4 | SOURCE_ID_INT_4 | — | ✅ |
| 28 | TransactionTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 29 | TransactionUpgValidFlag | UPG_VALID_FLAG | — | ✅ |
| 30 | TransactionValuationMethod | VALUATION_METHOD | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
