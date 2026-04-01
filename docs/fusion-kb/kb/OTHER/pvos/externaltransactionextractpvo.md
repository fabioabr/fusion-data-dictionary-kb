---
id: DOC-OTHER-PVO-ExternalTransactionExtractPVO
doc_type: system-doc
title: "ExternalTransactionExtractPVO — PVO Cross-Module"
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
  - ExternalTransactionExtractPVO
  - externaltransactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExternalTransactionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de External Transaction Extract. Acessa as tabelas: CE_EXTERNAL_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.ExternalTransactionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 1 | 1 | 26 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[ce_external_transactions|CE_EXTERNAL_TRANSACTIONS]] — 52 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[ce_external_transactions|CE_EXTERNAL_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExternalTransactionsAccountingFlag | ACCOUNTING_FLAG | — | ✅ |
| 2 | ExternalTransactionsAmount | AMOUNT | — | ✅ |
| 3 | ExternalTransactionsAssetCcid | ASSET_CCID | — | ✅ |
| 4 | ExternalTransactionsAttribute1 | ATTRIBUTE1 | — | — |
| 5 | ExternalTransactionsAttribute10 | ATTRIBUTE10 | — | — |
| 6 | ExternalTransactionsAttribute11 | ATTRIBUTE11 | — | — |
| 7 | ExternalTransactionsAttribute12 | ATTRIBUTE12 | — | — |
| 8 | ExternalTransactionsAttribute13 | ATTRIBUTE13 | — | — |
| 9 | ExternalTransactionsAttribute14 | ATTRIBUTE14 | — | — |
| 10 | ExternalTransactionsAttribute15 | ATTRIBUTE15 | — | — |
| 11 | ExternalTransactionsAttribute2 | ATTRIBUTE2 | — | — |
| 12 | ExternalTransactionsAttribute3 | ATTRIBUTE3 | — | — |
| 13 | ExternalTransactionsAttribute4 | ATTRIBUTE4 | — | — |
| 14 | ExternalTransactionsAttribute5 | ATTRIBUTE5 | — | — |
| 15 | ExternalTransactionsAttribute6 | ATTRIBUTE6 | — | — |
| 16 | ExternalTransactionsAttribute7 | ATTRIBUTE7 | — | — |
| 17 | ExternalTransactionsAttribute8 | ATTRIBUTE8 | — | — |
| 18 | ExternalTransactionsAttribute9 | ATTRIBUTE9 | — | — |
| 19 | ExternalTransactionsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | ExternalTransactionsAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 21 | ExternalTransactionsAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 22 | ExternalTransactionsAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 23 | ExternalTransactionsAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 24 | ExternalTransactionsAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 25 | ExternalTransactionsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 26 | ExternalTransactionsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 27 | ExternalTransactionsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 28 | ExternalTransactionsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 29 | ExternalTransactionsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 30 | ExternalTransactionsBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 31 | ExternalTransactionsBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 32 | ExternalTransactionsClearedDate | CLEARED_DATE | — | ✅ |
| 33 | ExternalTransactionsCreatedBy | CREATED_BY | — | ✅ |
| 34 | ExternalTransactionsCreationDate | CREATION_DATE | — | ✅ |
| 35 | ExternalTransactionsCurrencyCode | CURRENCY_CODE | — | ✅ |
| 36 | ExternalTransactionsDescription | DESCRIPTION | — | ✅ |
| 37 | ExternalTransactionsExternalTransactionId | EXTERNAL_TRANSACTION_ID | 🔑 | ✅ |
| 38 | ExternalTransactionsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | ExternalTransactionsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | ExternalTransactionsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | ExternalTransactionsLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 42 | ExternalTransactionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | ExternalTransactionsOffsetCcid | OFFSET_CCID | — | ✅ |
| 44 | ExternalTransactionsReconHistoryId | RECON_HISTORY_ID | — | ✅ |
| 45 | ExternalTransactionsReferenceText | REFERENCE_TEXT | — | ✅ |
| 46 | ExternalTransactionsSource | SOURCE | — | ✅ |
| 47 | ExternalTransactionsStatementLineId | STATEMENT_LINE_ID | — | ✅ |
| 48 | ExternalTransactionsStatus | STATUS | — | ✅ |
| 49 | ExternalTransactionsTransactionDate | TRANSACTION_DATE | — | ✅ |
| 50 | ExternalTransactionsTransactionId | TRANSACTION_ID | — | ✅ |
| 51 | ExternalTransactionsTransactionType | TRANSACTION_TYPE | — | ✅ |
| 52 | ExternalTransactionsValueDate | VALUE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
