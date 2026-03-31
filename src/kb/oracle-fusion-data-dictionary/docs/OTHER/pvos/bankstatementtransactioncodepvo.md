---
id: DOC-OTHER-PVO-BankStatementTransactionCodePVO
doc_type: system-doc
title: "BankStatementTransactionCodePVO — PVO Cross-Module"
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
  - BankStatementTransactionCodePVO
  - bankstatementtransactioncodepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankStatementTransactionCodePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Statement Transaction Code. Acessa as tabelas: CE_TRANSACTION_CODES.

**Caminho:** `FscmTopModelAM.FinCeBankStatementsAM.BankStatementTransactionCodePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 3 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[ce_transaction_codes|CE_TRANSACTION_CODES]] — 14 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ce_transaction_codes|CE_TRANSACTION_CODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankTransactionCodesCreatedBy | CREATED_BY | — | — |
| 2 | BankTransactionCodesCreationDate | CREATION_DATE | — | — |
| 3 | BankTransactionCodesDescription | DESCRIPTION | — | ✅ |
| 4 | BankTransactionCodesDomain | DOMAIN | — | — |
| 5 | BankTransactionCodesFamily | FAMILY | — | — |
| 6 | BankTransactionCodesLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | BankTransactionCodesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | BankTransactionCodesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | BankTransactionCodesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | BankTransactionCodesSeededFlag | SEEDED_FLAG | — | — |
| 11 | BankTransactionCodesSubFamily | SUB_FAMILY | — | — |
| 12 | BankTransactionCodesTransactionCodeId | TRANSACTION_CODE_ID | 🔑 | ✅ |
| 13 | BankTransactionCodesTrxCode | TRX_CODE | — | ✅ |
| 14 | BankTransactionCodesTrxType | TRX_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
