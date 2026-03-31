---
id: DOC-OTHER-PVO-HeaderScheduling
doc_type: system-doc
title: "HeaderScheduling — PVO Cross-Module"
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
  - HeaderScheduling
  - headerscheduling
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HeaderScheduling

## 📌 Visão Geral

View Object para extração BICC de dados de Header Scheduling. Acessa as tabelas: DOO_HEADERS_ALL.

**Caminho:** `FscmTopModelAM.DooTopAM.HeaderScheduling`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 20 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 40 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 2 | HeaderCanceledFlag | CANCELED_FLAG | — | ✅ |
| 3 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | ✅ |
| 4 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 5 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 6 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 7 | HeaderCreatedBy | CREATED_BY | — | ✅ |
| 8 | HeaderCreationDate | CREATION_DATE | — | ✅ |
| 9 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 10 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 11 | HeaderIsEditable | IS_EDITABLE | — | — |
| 12 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | HeaderOnHold | ON_HOLD | — | ✅ |
| 18 | HeaderOpenFlag | OPEN_FLAG | — | ✅ |
| 19 | HeaderOrderNumber | ORDER_NUMBER | — | ✅ |
| 20 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 21 | HeaderOrderedDate | ORDERED_DATE | — | ✅ |
| 22 | HeaderOrgId | ORG_ID | — | — |
| 23 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 24 | HeaderOwnerId | OWNER_ID | — | — |
| 25 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 26 | HeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 27 | HeaderPricingDate | PRICING_DATE | — | — |
| 28 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 29 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 30 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 31 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 32 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 33 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | ✅ |
| 34 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 35 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 36 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 37 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 38 | HeaderStatusCode | STATUS_CODE | — | — |
| 39 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | ✅ |
| 40 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
