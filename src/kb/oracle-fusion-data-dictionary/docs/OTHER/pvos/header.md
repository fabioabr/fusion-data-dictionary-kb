---
id: DOC-OTHER-PVO-Header
doc_type: system-doc
title: "Header — PVO Cross-Module"
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
  - Header
  - header
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Header

## 📌 Visão Geral

View Object para extração BICC de dados de Header. Acessa as tabelas: DOO_HEADERS_ALL, FUN_ALL_BUSINESS_UNITS_V, GL_LEDGERS.

**Caminho:** `FscmTopModelAM.DooTopAM.Header`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 3 | 1 | 24 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 46 atributos (1 PKs, 24 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 3 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CanceledFlag | CANCELED_FLAG | — | ✅ |
| 2 | ChangeVersionNumber | CHANGE_VERSION_NUMBER | — | ✅ |
| 3 | ConversionDate | CONVERSION_DATE | — | — |
| 4 | ConversionRate | CONVERSION_RATE | — | — |
| 5 | ConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 9 | HeaderAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 10 | HeaderAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 11 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 12 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 13 | HeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 14 | HeaderPricingDate | PRICING_DATE | — | — |
| 15 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 16 | HeaderSalesChannelCode | SALES_CHANNEL_CODE | — | ✅ |
| 17 | HeaderSalespersonId | SALESPERSON_ID | — | — |
| 18 | HeaderSubmittedBy | SUBMITTED_BY | — | ✅ |
| 19 | HeaderSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 20 | IsEditable | IS_EDITABLE | — | — |
| 21 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 26 | OnHold | ON_HOLD | — | ✅ |
| 27 | OpenFlag | OPEN_FLAG | — | ✅ |
| 28 | OrderNumber | ORDER_NUMBER | — | ✅ |
| 29 | OrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 30 | OrderedDate | ORDERED_DATE | — | ✅ |
| 31 | OrgId | ORG_ID | — | — |
| 32 | OrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 33 | OwnerId | OWNER_ID | — | — |
| 34 | PartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 35 | SoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 36 | SoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 37 | SoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 38 | SoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 39 | SourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | ✅ |
| 40 | SourceOrderId | SOURCE_ORDER_ID | — | — |
| 41 | SourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 42 | SourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 43 | SourceOrgId | SOURCE_ORG_ID | — | — |
| 44 | StatusCode | STATUS_CODE | — | — |
| 45 | SubmittedFlag | SUBMITTED_FLAG | — | ✅ |
| 46 | TransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 3 | BUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 2 | LedgerLedgerId | LEDGER_ID | — | — |
| 3 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
