---
id: DOC-HCM-489
doc_type: system-doc
title: "HZ_CUST_ACCOUNT_ROLES — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - HZ_CUST_ACCOUNT_ROLES
  - hz_cust_account_roles
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_CUST_ACCOUNT_ROLES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTACT_PERSON_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | CUST_ACCOUNT_ID | — | — | — | — | — | — |
| 6 | CUST_ACCOUNT_ROLE_ID | — | — | — | — | — | — |
| 7 | CUST_ACCT_SITE_ID | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | ORIG_SYSTEM_REFERENCE | — | — | — | — | — | — |
| 12 | PRIMARY_FLAG | — | — | — | — | — | — |
| 13 | RELATIONSHIP_ID | — | — | — | — | — | — |
| 14 | ROLE_TYPE | — | — | — | — | — | — |
| 15 | SOURCE_CODE | — | — | — | — | — | — |
| 16 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountcontact|AccountContact]] (AR · BICC: 11/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | CustomerAccountContactContactPersonId | — |
| CREATED_BY | CustomerAccountContactCreatedBy | ✅ |
| CREATED_BY_MODULE | CustomerAccountContactCreatedByModule | ✅ |
| CREATION_DATE | CustomerAccountContactCreationDate | ✅ |
| CUST_ACCOUNT_ID | CustomerAccountContactCustAccountId | — |
| CUST_ACCOUNT_ROLE_ID | CustAccountRoleId | ✅ |
| CUST_ACCT_SITE_ID | CustomerAccountContactCustAcctSiteId | — |
| LAST_UPDATE_DATE | CustomerAccountContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CustomerAccountContactLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CustomerAccountContactLastUpdatedBy | ✅ |
| ORIG_SYSTEM_REFERENCE | CustomerAccountContactOrigSystemReference | ✅ |
| PRIMARY_FLAG | CustomerAccountContactPrimaryFlag | ✅ |
| RELATIONSHIP_ID | CustomerAccountContactRelationshipId | — |
| ROLE_TYPE | CustomerAccountContactRoleType | ✅ |
| SOURCE_CODE | CustomerAccountContactSourceCode | — |
| STATUS | CustomerAccountContactStatus | ✅ |

### [[accountcontactrelationship|AccountContactRelationShip]] (AR · BICC: 11/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | CustomerAccountContactContactPersonId | — |
| CREATED_BY | CustomerAccountContactCreatedBy | ✅ |
| CREATED_BY_MODULE | CustomerAccountContactCreatedByModule | ✅ |
| CREATION_DATE | CustomerAccountContactCreationDate | ✅ |
| CUST_ACCOUNT_ID | CustomerAccountContactCustAccountId | — |
| CUST_ACCOUNT_ROLE_ID | CustAccountRoleId | ✅ |
| CUST_ACCT_SITE_ID | CustomerAccountContactCustAcctSiteId | — |
| LAST_UPDATE_DATE | CustomerAccountContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CustomerAccountContactLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CustomerAccountContactLastUpdatedBy | ✅ |
| ORIG_SYSTEM_REFERENCE | CustomerAccountContactOrigSystemReference | ✅ |
| PRIMARY_FLAG | CustomerAccountContactPrimaryFlag | ✅ |
| RELATIONSHIP_ID | CustomerAccountContactRelationshipId | — |
| ROLE_TYPE | CustomerAccountContactRoleType | ✅ |
| SOURCE_CODE | CustomerAccountContactSourceCode | — |
| STATUS | CustomerAccountContactStatus | ✅ |

### [[billingplan|BillingPlan]] (OTHER · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | BillToContactAccountCustAccountRoleId | ✅ |
| RELATIONSHIP_ID | BillToContactAccountRelationshipId | ✅ |

### [[fulfillline|FulfillLine]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | BillToContactAccountCustAccountRoleId | — |
| RELATIONSHIP_ID | BillToContactAccountRelationshipId | — |

### [[fulfilllineref|FulfillLineRef]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | BillToContactAccountCustAccountRoleId | — |
| RELATIONSHIP_ID | BillToContactAccountRelationshipId | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CONTACT_PERSON_ID | SoldToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | SoldToContactCustAccountRoleId | — |

### [[manualpriceadjustment|ManualPriceAdjustment]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | BillToContactAccountCustAccountRoleId | — |
| RELATIONSHIP_ID | BillToContactAccountRelationshipId | — |

### [[orderaddressbillto|OrderAddressBillTo]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | CustAccountRoleId | — |
| RELATIONSHIP_ID | CustAcctContRelationshipId | — |

### [[orderchargecomponent|OrderChargeComponent]] (OTHER · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_ACCOUNT_ROLE_ID | BillToContactAccountCustAccountRoleId | ✅ |
| RELATIONSHIP_ID | BillToContactAccountRelationshipId | ✅ |

### [[sitecontact|SiteContact]] (AR · BICC: 11/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | CustomerAccountContactContactPersonId | — |
| CREATED_BY | CustomerAccountContactCreatedBy | ✅ |
| CREATED_BY_MODULE | CustomerAccountContactCreatedByModule | ✅ |
| CREATION_DATE | CustomerAccountContactCreationDate | ✅ |
| CUST_ACCOUNT_ID | CustomerAccountContactCustAccountId | — |
| CUST_ACCOUNT_ROLE_ID | CustAccountRoleId | ✅ |
| CUST_ACCT_SITE_ID | CustomerAccountContactCustAcctSiteId | — |
| LAST_UPDATE_DATE | CustomerAccountContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CustomerAccountContactLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CustomerAccountContactLastUpdatedBy | ✅ |
| ORIG_SYSTEM_REFERENCE | CustomerAccountContactOrigSystemReference | ✅ |
| PRIMARY_FLAG | CustomerAccountContactPrimaryFlag | ✅ |
| RELATIONSHIP_ID | CustomerAccountContactRelationshipId | — |
| ROLE_TYPE | CustomerAccountContactRoleType | ✅ |
| SOURCE_CODE | CustomerAccountContactSourceCode | — |
| STATUS | CustomerAccountContactStatus | ✅ |

### [[sitecontactrelationship|SiteContactRelationShip]] (AR · BICC: 10/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | CustomerAccountContactContactPersonId | — |
| CREATED_BY | CustomerAccountContactCreatedBy | ✅ |
| CREATED_BY_MODULE | CustomerAccountContactCreatedByModule | ✅ |
| CREATION_DATE | CustomerAccountContactCreationDate | ✅ |
| CUST_ACCOUNT_ID | CustomerAccountContactCustAccountId | — |
| CUST_ACCOUNT_ROLE_ID | CustAccountRoleId | ✅ |
| CUST_ACCT_SITE_ID | CustomerAccountContactCustAcctSiteId | — |
| LAST_UPDATE_DATE | CustomerAccountContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CustomerAccountContactLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CustomerAccountContactLastUpdatedBy | — |
| ORIG_SYSTEM_REFERENCE | CustomerAccountContactOrigSystemReference | ✅ |
| PRIMARY_FLAG | CustomerAccountContactPrimaryFlag | ✅ |
| RELATIONSHIP_ID | CustomerAccountContactRelationshipId | — |
| ROLE_TYPE | CustomerAccountContactRoleType | ✅ |
| SOURCE_CODE | CustomerAccountContactSourceCode | — |
| STATUS | CustomerAccountContactStatus | ✅ |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CONTACT_PERSON_ID | DraweeToContactContactPersonId | — |
| CONTACT_PERSON_ID | ShipToContactContactPersonId | — |
| CONTACT_PERSON_ID | SoldToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | DraweeToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | ShipToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | SoldToContactCustAccountRoleId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CONTACT_PERSON_ID | DraweeToContactContactPersonId | — |
| CONTACT_PERSON_ID | ShipToContactContactPersonId | — |
| CONTACT_PERSON_ID | SoldToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | DraweeToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | ShipToContactCustAccountRoleId | — |
| CUST_ACCOUNT_ROLE_ID | SoldToContactCustAccountRoleId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_PERSON_ID | BillToContactContactPersonId | — |
| CUST_ACCOUNT_ROLE_ID | BillToContactCustAccountRoleId | — |
