---
id: DOC-OTHER-PVO-BankAccountBalanceExtractPVO
doc_type: system-doc
title: "BankAccountBalanceExtractPVO — PVO Cross-Module"
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
  - BankAccountBalanceExtractPVO
  - bankaccountbalanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankAccountBalanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Account Balance Extract. Acessa as tabelas: CE_STMT_BALANCES.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankAccountBalanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_stmt_balances|CE_STMT_BALANCES]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ce_stmt_balances|CE_STMT_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountBalanceBalanceAmount | BALANCE_AMOUNT | — | ✅ |
| 2 | BankAccountBalanceBalanceCode | BALANCE_CODE | — | ✅ |
| 3 | BankAccountBalanceBalanceCurr | BALANCE_CURR | — | ✅ |
| 4 | BankAccountBalanceBalanceDate | BALANCE_DATE | — | ✅ |
| 5 | BankAccountBalanceBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 6 | BankAccountBalanceCreatedBy | CREATED_BY | — | ✅ |
| 7 | BankAccountBalanceCreationDate | CREATION_DATE | — | ✅ |
| 8 | BankAccountBalanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | BankAccountBalanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | BankAccountBalanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | BankAccountBalanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | BankAccountBalanceStatementHeaderId | STATEMENT_HEADER_ID | — | ✅ |
| 13 | BankAccountBalanceStmtBalanceId | STMT_BALANCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
