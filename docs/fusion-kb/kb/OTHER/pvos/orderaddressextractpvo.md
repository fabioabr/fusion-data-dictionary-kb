---
id: DOC-OTHER-PVO-OrderAddressExtractPVO
doc_type: system-doc
title: "OrderAddressExtractPVO — PVO Cross-Module"
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
  - OrderAddressExtractPVO
  - orderaddressextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderAddressExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Address Extract. Acessa as tabelas: DOO_ORDER_ADDRESSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderAddressExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_addresses|DOO_ORDER_ADDRESSES]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[doo_order_addresses|DOO_ORDER_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderAddressContactId | CONTACT_ID | — | ✅ |
| 2 | OrderAddressCreatedBy | CREATED_BY | — | ✅ |
| 3 | OrderAddressCreationDate | CREATION_DATE | — | ✅ |
| 4 | OrderAddressCustAccountContactId | CUST_ACCOUNT_CONTACT_ID | — | ✅ |
| 5 | OrderAddressCustAcctId | CUST_ACCT_ID | — | ✅ |
| 6 | OrderAddressCustAcctSiteUseId | CUST_ACCT_SITE_USE_ID | — | ✅ |
| 7 | OrderAddressDeltaType | DELTA_TYPE | — | ✅ |
| 8 | OrderAddressFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 9 | OrderAddressHeaderId | HEADER_ID | — | ✅ |
| 10 | OrderAddressId | ADDRESS_ID | 🔑 | ✅ |
| 11 | OrderAddressLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrderAddressLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | OrderAddressLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | OrderAddressModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 15 | OrderAddressObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | OrderAddressPartyId | PARTY_ID | — | ✅ |
| 17 | OrderAddressPartySiteId | PARTY_SITE_ID | — | ✅ |
| 18 | OrderAddressPrefContactPointId | PREF_CONTACT_POINT_ID | — | ✅ |
| 19 | OrderAddressReferenceAddressId | REFERENCE_ADDRESS_ID | — | ✅ |
| 20 | OrderAddressUseType | ADDRESS_USE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
