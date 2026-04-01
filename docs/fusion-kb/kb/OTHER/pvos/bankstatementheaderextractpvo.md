---
id: DOC-OTHER-PVO-BankStatementHeaderExtractPVO
doc_type: system-doc
title: "BankStatementHeaderExtractPVO — PVO Cross-Module"
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
  - BankStatementHeaderExtractPVO
  - bankstatementheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankStatementHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Statement Header Extract. Acessa as tabelas: CE_STATEMENT_HEADERS.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankStatementHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 1 | 1 | 23 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[ce_statement_headers|CE_STATEMENT_HEADERS]] — 55 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[ce_statement_headers|CE_STATEMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankStatementHeaderAttribute1 | ATTRIBUTE1 | — | — |
| 2 | BankStatementHeaderAttribute10 | ATTRIBUTE10 | — | — |
| 3 | BankStatementHeaderAttribute11 | ATTRIBUTE11 | — | — |
| 4 | BankStatementHeaderAttribute12 | ATTRIBUTE12 | — | — |
| 5 | BankStatementHeaderAttribute13 | ATTRIBUTE13 | — | — |
| 6 | BankStatementHeaderAttribute14 | ATTRIBUTE14 | — | — |
| 7 | BankStatementHeaderAttribute15 | ATTRIBUTE15 | — | — |
| 8 | BankStatementHeaderAttribute2 | ATTRIBUTE2 | — | — |
| 9 | BankStatementHeaderAttribute3 | ATTRIBUTE3 | — | — |
| 10 | BankStatementHeaderAttribute4 | ATTRIBUTE4 | — | — |
| 11 | BankStatementHeaderAttribute5 | ATTRIBUTE5 | — | — |
| 12 | BankStatementHeaderAttribute6 | ATTRIBUTE6 | — | — |
| 13 | BankStatementHeaderAttribute7 | ATTRIBUTE7 | — | — |
| 14 | BankStatementHeaderAttribute8 | ATTRIBUTE8 | — | — |
| 15 | BankStatementHeaderAttribute9 | ATTRIBUTE9 | — | — |
| 16 | BankStatementHeaderAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | BankStatementHeaderAutorecProcessCode | AUTOREC_PROCESS_CODE | — | ✅ |
| 18 | BankStatementHeaderAutorecProcessId | AUTOREC_PROCESS_ID | — | ✅ |
| 19 | BankStatementHeaderBalanceCheck | BALANCE_CHECK | — | ✅ |
| 20 | BankStatementHeaderBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 21 | BankStatementHeaderCreatedBy | CREATED_BY | — | ✅ |
| 22 | BankStatementHeaderCreationDate | CREATION_DATE | — | ✅ |
| 23 | BankStatementHeaderCurrencyCode | CURRENCY_CODE | — | ✅ |
| 24 | BankStatementHeaderElectronicSeqNum | ELECTRONIC_SEQ_NUM | — | ✅ |
| 25 | BankStatementHeaderGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 26 | BankStatementHeaderGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 27 | BankStatementHeaderGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 28 | BankStatementHeaderGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 29 | BankStatementHeaderGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 30 | BankStatementHeaderGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 31 | BankStatementHeaderGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 32 | BankStatementHeaderGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 33 | BankStatementHeaderGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 34 | BankStatementHeaderGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 35 | BankStatementHeaderGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 36 | BankStatementHeaderGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 37 | BankStatementHeaderGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 38 | BankStatementHeaderGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 39 | BankStatementHeaderGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 40 | BankStatementHeaderGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 41 | BankStatementHeaderInboundFileId | INBOUND_FILE_ID | — | ✅ |
| 42 | BankStatementHeaderIntradayFlag | INTRADAY_FLAG | — | ✅ |
| 43 | BankStatementHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | BankStatementHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | BankStatementHeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | BankStatementHeaderLegalSeqNum | LEGAL_SEQ_NUM | — | ✅ |
| 47 | BankStatementHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 48 | BankStatementHeaderReconStatusCode | RECON_STATUS_CODE | — | ✅ |
| 49 | BankStatementHeaderStatementDate | STATEMENT_DATE | — | ✅ |
| 50 | BankStatementHeaderStatementEntryType | STATEMENT_ENTRY_TYPE | — | ✅ |
| 51 | BankStatementHeaderStatementHeaderId | STATEMENT_HEADER_ID | 🔑 | ✅ |
| 52 | BankStatementHeaderStatementNumber | STATEMENT_NUMBER | — | ✅ |
| 53 | BankStatementHeaderStatementType | STATEMENT_TYPE | — | ✅ |
| 54 | BankStatementHeaderStmtFromDate | STMT_FROM_DATE | — | ✅ |
| 55 | BankStatementHeaderStmtToDate | STMT_TO_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
