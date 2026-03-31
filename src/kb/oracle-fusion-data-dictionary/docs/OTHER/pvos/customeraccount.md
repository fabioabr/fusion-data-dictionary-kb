---
id: DOC-OTHER-PVO-CustomerAccount
doc_type: system-doc
title: "CustomerAccount — PVO Cross-Module"
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
  - CustomerAccount
  - customeraccount
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerAccount

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Account. Acessa as tabelas: HZ_CUST_ACCOUNTS.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.CustomerAccount`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 1 | 32 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 32 atributos (1 PKs, 32 BICC)

---

## ⚙️ Atributos

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | ✅ |
| 2 | AccountName | ACCOUNT_NAME | — | ✅ |
| 3 | AccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 4 | AccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | ✅ |
| 5 | ArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | ✅ |
| 6 | AutopayFlag | AUTOPAY_FLAG | — | ✅ |
| 7 | Comments | COMMENTS | — | ✅ |
| 8 | CoterminateDayMonth | COTERMINATE_DAY_MONTH | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 11 | CreationDate | CREATION_DATE | — | ✅ |
| 12 | CustAccountId | CUST_ACCOUNT_ID | 🔑 | ✅ |
| 13 | CustomerClassCode | CUSTOMER_CLASS_CODE | — | ✅ |
| 14 | CustomerType | CUSTOMER_TYPE | — | ✅ |
| 15 | DateTypePreference | DATE_TYPE_PREFERENCE | — | ✅ |
| 16 | DepositRefundMethod | DEPOSIT_REFUND_METHOD | — | ✅ |
| 17 | HeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | ✅ |
| 18 | HoldBillFlag | HOLD_BILL_FLAG | — | ✅ |
| 19 | LastBatchId | LAST_BATCH_ID | — | ✅ |
| 20 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | NpaNumber | NPA_NUMBER | — | ✅ |
| 24 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 25 | PartyId | PARTY_ID | — | ✅ |
| 26 | SellingPartyId | SELLING_PARTY_ID | — | ✅ |
| 27 | SourceCode | SOURCE_CODE | — | ✅ |
| 28 | Status | STATUS | — | ✅ |
| 29 | StatusUpdateDate | STATUS_UPDATE_DATE | — | ✅ |
| 30 | TaxCode | TAX_CODE | — | ✅ |
| 31 | TaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | ✅ |
| 32 | TaxRoundingRule | TAX_ROUNDING_RULE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
