---
id: DOC-OTHER-PVO-OrderTotalDiscount
doc_type: system-doc
title: "OrderTotalDiscount — PVO Cross-Module"
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
  - OrderTotalDiscount
  - ordertotaldiscount
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderTotalDiscount

## 📌 Visão Geral

View Object para extração BICC de dados de Order Total Discount. Acessa as tabelas: DOO_HEADERS_ALL, DOO_ORDER_TOTALS, FUN_ALL_BUSINESS_UNITS_V (+1).

**Caminho:** `FscmTopModelAM.DooTopAM.OrderTotalDiscount`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 4 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 46 atributos
- [[doo_order_totals|DOO_ORDER_TOTALS]] — 15 atributos (1 PKs, 3 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 4 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | HeaderAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 3 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | — |
| 4 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 5 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 6 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 7 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 8 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 9 | HeaderCreatedBy | CREATED_BY | — | — |
| 10 | HeaderCreationDate | CREATION_DATE | — | — |
| 11 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 12 | HeaderHeaderId | HEADER_ID | — | — |
| 13 | HeaderIsEditable | IS_EDITABLE | — | — |
| 14 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 18 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | HeaderOnHold | ON_HOLD | — | — |
| 20 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 21 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 22 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 23 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 24 | HeaderOrgId | ORG_ID | — | — |
| 25 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 26 | HeaderOwnerId | OWNER_ID | — | — |
| 27 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 28 | HeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 29 | HeaderPricingDate | PRICING_DATE | — | — |
| 30 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 31 | HeaderSalesChannelCode | SALES_CHANNEL_CODE | — | — |
| 32 | HeaderSalespersonId | SALESPERSON_ID | — | — |
| 33 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 34 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 35 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 36 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 37 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 38 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 39 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 40 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 41 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 42 | HeaderStatusCode | STATUS_CODE | — | — |
| 43 | HeaderSubmittedBy | SUBMITTED_BY | — | — |
| 44 | HeaderSubmittedDate | SUBMITTED_DATE | — | — |
| 45 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | — |
| 46 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_order_totals|DOO_ORDER_TOTALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTotalCreatedBy | CREATED_BY | — | — |
| 2 | OrderTotalCreationDate | CREATION_DATE | — | — |
| 3 | OrderTotalCurrencyCode | CURRENCY_CODE | — | — |
| 4 | OrderTotalDisplayName | DISPLAY_NAME | — | — |
| 5 | OrderTotalEstimatedFlag | ESTIMATED_FLAG | — | — |
| 6 | OrderTotalHeaderId | HEADER_ID | — | — |
| 7 | OrderTotalId | ORDER_TOTAL_ID | 🔑 | ✅ |
| 8 | OrderTotalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | OrderTotalLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | OrderTotalLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | OrderTotalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | OrderTotalPrimaryFlag | PRIMARY_FLAG | — | — |
| 13 | OrderTotalTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 14 | OrderTotalTotalCode | TOTAL_CODE | — | — |
| 15 | OrderTotalTotalGroup | TOTAL_GROUP | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 3 | BUName | BU_NAME | — | — |
| 4 | BUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 2 | LedgerLedgerId | LEDGER_ID | — | — |
| 3 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
