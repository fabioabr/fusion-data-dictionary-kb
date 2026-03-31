---
id: DOC-OTHER-PVO-CustomerAccountRelationship
doc_type: system-doc
title: "CustomerAccountRelationship — PVO Cross-Module"
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
  - CustomerAccountRelationship
  - customeraccountrelationship
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerAccountRelationship

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Account Relationship. Acessa as tabelas: HZ_CUST_ACCOUNTS, HZ_CUST_ACCT_RELATE_ALL, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.CustomerAccountRelationship`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 3 | 1 | 15 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 32 atributos (7 BICC)
- [[hz_cust_acct_relate_all|HZ_CUST_ACCT_RELATE_ALL]] — 13 atributos (1 PKs, 7 BICC)
- [[hz_parties|HZ_PARTIES]] — 5 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | CustomerAccountAccountName | ACCOUNT_NAME | — | ✅ |
| 3 | CustomerAccountAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 4 | CustomerAccountAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | — |
| 5 | CustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 6 | CustomerAccountAutopayFlag | AUTOPAY_FLAG | — | — |
| 7 | CustomerAccountComments | COMMENTS | — | — |
| 8 | CustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 9 | CustomerAccountCreatedBy | CREATED_BY | — | ✅ |
| 10 | CustomerAccountCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 11 | CustomerAccountCreationDate | CREATION_DATE | — | ✅ |
| 12 | CustomerAccountCustAccountId | CUST_ACCOUNT_ID | — | ✅ |
| 13 | CustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 14 | CustomerAccountCustomerType | CUSTOMER_TYPE | — | — |
| 15 | CustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 16 | CustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 17 | CustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 18 | CustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 19 | CustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 20 | CustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | CustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | CustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 24 | CustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 25 | CustomerAccountPartyId | PARTY_ID | — | — |
| 26 | CustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 27 | CustomerAccountSourceCode | SOURCE_CODE | — | — |
| 28 | CustomerAccountStatus | STATUS | — | — |
| 29 | CustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 30 | CustomerAccountTaxCode | TAX_CODE | — | — |
| 31 | CustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 32 | CustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[hz_cust_acct_relate_all|HZ_CUST_ACCT_RELATE_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAcctRelateId | CUST_ACCT_RELATE_ID | 🔑 | ✅ |
| 2 | CustomerAccountRelationshipBillToFlag | BILL_TO_FLAG | — | ✅ |
| 3 | CustomerAccountRelationshipComments | COMMENTS | — | — |
| 4 | CustomerAccountRelationshipCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 5 | CustomerAccountRelationshipCustAccountId | CUST_ACCOUNT_ID | — | — |
| 6 | CustomerAccountRelationshipCustomerReciprocalFlag | CUSTOMER_RECIPROCAL_FLAG | — | ✅ |
| 7 | CustomerAccountRelationshipEndDate | END_DATE | — | ✅ |
| 8 | CustomerAccountRelationshipRelatedCustAccountId | RELATED_CUST_ACCOUNT_ID | — | — |
| 9 | CustomerAccountRelationshipRelationshipType | RELATIONSHIP_TYPE | — | — |
| 10 | CustomerAccountRelationshipSetId | SET_ID | — | — |
| 11 | CustomerAccountRelationshipShipToFlag | SHIP_TO_FLAG | — | ✅ |
| 12 | CustomerAccountRelationshipStartDate | START_DATE | — | ✅ |
| 13 | CustomerAccountRelationshipStatus | STATUS | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedPartyPartyId | PARTY_ID | — | — |
| 2 | RelatedPartyPartyName | PARTY_NAME | — | ✅ |
| 3 | RelatedPartyPartyNumber | PARTY_NUMBER | — | — |
| 4 | RelatedPartyPartyType | PARTY_TYPE | — | — |
| 5 | RelatedPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
