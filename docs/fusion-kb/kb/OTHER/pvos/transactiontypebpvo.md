---
id: DOC-OTHER-PVO-TransactionTypeBPVO
doc_type: system-doc
title: "TransactionTypeBPVO — PVO Cross-Module"
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
  - TransactionTypeBPVO
  - transactiontypebpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionTypeBPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Type B. Acessa as tabelas: FUN_TRX_TYPES_B, FUN_TRX_TYPES_TL.

**Caminho:** `FscmTopModelAM.FinFunIntercoTransactionsAM.TransactionTypeBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 12 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[fun_trx_types_b|FUN_TRX_TYPES_B]] — 13 atributos (1 PKs, 8 BICC)
- [[fun_trx_types_tl|FUN_TRX_TYPES_TL]] — 11 atributos (4 BICC)

---

## ⚙️ Atributos

### [[fun_trx_types_b|FUN_TRX_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeAllowInterestAccrualFlag | ALLOW_INTEREST_ACCRUAL_FLAG | — | ✅ |
| 2 | TransactionTypeAllowInvoicingFlag | ALLOW_INVOICING_FLAG | — | ✅ |
| 3 | TransactionTypeCreatedBy | CREATED_BY | — | — |
| 4 | TransactionTypeCreationDate | CREATION_DATE | — | — |
| 5 | TransactionTypeEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | TransactionTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TransactionTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TransactionTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TransactionTypeManualApproveFlag | MANUAL_APPROVE_FLAG | — | ✅ |
| 10 | TransactionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | TransactionTypeTrxTypeCode | TRX_TYPE_CODE | — | ✅ |
| 12 | TransactionTypeVatTaxableFlag | VAT_TAXABLE_FLAG | — | ✅ |
| 13 | TrxTypeId | TRX_TYPE_ID | 🔑 | ✅ |

### [[fun_trx_types_tl|FUN_TRX_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionTypeTranslatedCreatedBy | CREATED_BY | — | — |
| 2 | TransactionTypeTranslatedCreationDate | CREATION_DATE | — | — |
| 3 | TransactionTypeTranslatedDescription | DESCRIPTION | — | ✅ |
| 4 | TransactionTypeTranslatedLanguage | LANGUAGE | — | ✅ |
| 5 | TransactionTypeTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TransactionTypeTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TransactionTypeTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TransactionTypeTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | TransactionTypeTranslatedSourceLang | SOURCE_LANG | — | — |
| 10 | TransactionTypeTranslatedTrxTypeId | TRX_TYPE_ID | — | — |
| 11 | TransactionTypeTranslatedTrxTypeName | TRX_TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
