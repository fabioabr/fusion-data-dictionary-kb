---
id: DOC-OTHER-PVO-BankStatementLinesExtractPVO
doc_type: system-doc
title: "BankStatementLinesExtractPVO — PVO Cross-Module"
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
  - BankStatementLinesExtractPVO
  - bankstatementlinesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankStatementLinesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Statement Lines Extract. Acessa as tabelas: CE_STATEMENT_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankStatementLinesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 1 | 1 | 38 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[ce_statement_lines|CE_STATEMENT_LINES]] — 70 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[ce_statement_lines|CE_STATEMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BBankStatementLinesReversalIndFlag | REVERSAL_IND_FLAG | — | ✅ |
| 2 | BankStatementLinesAccntServicerRef | ACCNT_SERVICER_REF | — | ✅ |
| 3 | BankStatementLinesAddendaTxt | ADDENDA_TXT | — | ✅ |
| 4 | BankStatementLinesAmount | AMOUNT | — | ✅ |
| 5 | BankStatementLinesAttribute1 | ATTRIBUTE1 | — | — |
| 6 | BankStatementLinesAttribute10 | ATTRIBUTE10 | — | — |
| 7 | BankStatementLinesAttribute11 | ATTRIBUTE11 | — | — |
| 8 | BankStatementLinesAttribute12 | ATTRIBUTE12 | — | — |
| 9 | BankStatementLinesAttribute13 | ATTRIBUTE13 | — | — |
| 10 | BankStatementLinesAttribute14 | ATTRIBUTE14 | — | — |
| 11 | BankStatementLinesAttribute15 | ATTRIBUTE15 | — | — |
| 12 | BankStatementLinesAttribute2 | ATTRIBUTE2 | — | — |
| 13 | BankStatementLinesAttribute3 | ATTRIBUTE3 | — | — |
| 14 | BankStatementLinesAttribute4 | ATTRIBUTE4 | — | — |
| 15 | BankStatementLinesAttribute5 | ATTRIBUTE5 | — | — |
| 16 | BankStatementLinesAttribute6 | ATTRIBUTE6 | — | — |
| 17 | BankStatementLinesAttribute7 | ATTRIBUTE7 | — | — |
| 18 | BankStatementLinesAttribute8 | ATTRIBUTE8 | — | — |
| 19 | BankStatementLinesAttribute9 | ATTRIBUTE9 | — | — |
| 20 | BankStatementLinesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 21 | BankStatementLinesBookingDate | BOOKING_DATE | — | ✅ |
| 22 | BankStatementLinesCheckNumber | CHECK_NUMBER | — | ✅ |
| 23 | BankStatementLinesClearingSystemRef | CLEARING_SYSTEM_REF | — | ✅ |
| 24 | BankStatementLinesCommWaiverIndFlag | COMM_WAIVER_IND_FLAG | — | ✅ |
| 25 | BankStatementLinesContractIdentification | CONTRACT_IDENTIFICATION | — | ✅ |
| 26 | BankStatementLinesCreatedBy | CREATED_BY | — | ✅ |
| 27 | BankStatementLinesCreationDate | CREATION_DATE | — | ✅ |
| 28 | BankStatementLinesCustomerReference | CUSTOMER_REFERENCE | — | ✅ |
| 29 | BankStatementLinesEndToEndId | END_TO_END_ID | — | ✅ |
| 30 | BankStatementLinesExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 31 | BankStatementLinesExchangeRate | EXCHANGE_RATE | — | ✅ |
| 32 | BankStatementLinesExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 33 | BankStatementLinesExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 34 | BankStatementLinesExternalTransactionId | EXTERNAL_TRANSACTION_ID | — | ✅ |
| 35 | BankStatementLinesFlowIndicator | FLOW_INDICATOR | — | ✅ |
| 36 | BankStatementLinesGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 37 | BankStatementLinesGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 38 | BankStatementLinesGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 39 | BankStatementLinesGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 40 | BankStatementLinesGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 41 | BankStatementLinesGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 42 | BankStatementLinesGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 43 | BankStatementLinesGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 44 | BankStatementLinesGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 45 | BankStatementLinesGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 46 | BankStatementLinesGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 47 | BankStatementLinesGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 48 | BankStatementLinesGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 49 | BankStatementLinesGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 50 | BankStatementLinesGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 51 | BankStatementLinesGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 52 | BankStatementLinesInstructionIdentification | INSTRUCTION_IDENTIFICATION | — | ✅ |
| 53 | BankStatementLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | BankStatementLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 55 | BankStatementLinesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | BankStatementLinesLineNumber | LINE_NUMBER | — | ✅ |
| 57 | BankStatementLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 58 | BankStatementLinesOrigBankAccountId | ORIG_BANK_ACCOUNT_ID | — | ✅ |
| 59 | BankStatementLinesReconHistoryId | RECON_HISTORY_ID | — | ✅ |
| 60 | BankStatementLinesReconReference | RECON_REFERENCE | — | ✅ |
| 61 | BankStatementLinesReconStatus | RECON_STATUS | — | ✅ |
| 62 | BankStatementLinesServicerStatus | SERVICER_STATUS | — | ✅ |
| 63 | BankStatementLinesStatementHeaderId | STATEMENT_HEADER_ID | — | ✅ |
| 64 | BankStatementLinesStatementLineId | STATEMENT_LINE_ID | 🔑 | ✅ |
| 65 | BankStatementLinesTransactionId | TRANSACTION_ID | — | ✅ |
| 66 | BankStatementLinesTrxAmount | TRX_AMOUNT | — | ✅ |
| 67 | BankStatementLinesTrxCodeId | TRX_CODE_ID | — | ✅ |
| 68 | BankStatementLinesTrxCurrCode | TRX_CURR_CODE | — | ✅ |
| 69 | BankStatementLinesTrxType | TRX_TYPE | — | ✅ |
| 70 | BankStatementLinesValueDate | VALUE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
