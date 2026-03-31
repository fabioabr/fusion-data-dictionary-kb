---
id: DOC-OTHER-PVO-OrderAddressBillTo
doc_type: system-doc
title: "OrderAddressBillTo — PVO Cross-Module"
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
  - OrderAddressBillTo
  - orderaddressbillto
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderAddressBillTo

## 📌 Visão Geral

View Object para extração BICC de dados de Order Address Bill To. Acessa as tabelas: DOO_ORDER_ADDRESSES, HZ_CUST_ACCOUNT_ROLES.

**Caminho:** `FscmTopModelAM.DooTopAM.OrderAddressBillTo`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 4 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_addresses|DOO_ORDER_ADDRESSES]] — 20 atributos (1 PKs, 4 BICC)
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos

---

## ⚙️ Atributos

### [[doo_order_addresses|DOO_ORDER_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressId | ADDRESS_ID | 🔑 | ✅ |
| 2 | AddressUseType | ADDRESS_USE_TYPE | — | ✅ |
| 3 | ContactId | CONTACT_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | CustAccountContactId | CUST_ACCOUNT_CONTACT_ID | — | — |
| 7 | CustAcctId | CUST_ACCT_ID | — | — |
| 8 | CustAcctSiteUseId | CUST_ACCT_SITE_USE_ID | — | ✅ |
| 9 | DeltaType | DELTA_TYPE | — | — |
| 10 | FulfillLineId | FULFILL_LINE_ID | — | — |
| 11 | HeaderId | HEADER_ID | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ModifiedFlag | MODIFIED_FLAG | — | — |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PartyId | PARTY_ID | — | — |
| 18 | PartySiteId | PARTY_SITE_ID | — | — |
| 19 | PrefContactPointId | PREF_CONTACT_POINT_ID | — | — |
| 20 | ReferenceAddressId | REFERENCE_ADDRESS_ID | — | — |

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |
| 2 | CustAcctContRelationshipId | RELATIONSHIP_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
