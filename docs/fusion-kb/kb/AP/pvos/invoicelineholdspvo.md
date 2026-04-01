---
id: DOC-AP-PVO-InvoiceLineHoldsPVO
doc_type: system-doc
title: "InvoiceLineHoldsPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - InvoiceLineHoldsPVO
  - invoicelineholdspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceLineHoldsPVO

## 📌 Visão Geral

Extrai as retenções (holds) aplicadas em nível de linha de fatura, incluindo motivo do bloqueio e referência a pedido/recebimento. Permite análise granular de exceções por item da fatura e resolução direcionada de discrepâncias.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.InvoiceLineHoldsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 93 | 12 | 1 | 13 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[ap_holds_all|AP_HOLDS_ALL]] — 18 atributos (1 PKs, 10 BICC)
- [[ap_invoices_all|AP_INVOICES_ALL]] — 19 atributos
- [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]] — 1 atributos
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos
- [[hz_party_sites|HZ_PARTY_SITES]] — 2 atributos
- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 19 atributos (2 BICC)
- [[per_users|PER_USERS]] — 15 atributos
- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 3 atributos
- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 5 atributos (1 BICC)
- [[rcv_transactions|RCV_TRANSACTIONS]] — 2 atributos

---

## ⚙️ Atributos

### [[ap_holds_all|AP_HOLDS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldId | HOLD_ID | 🔑 | ✅ |
| 2 | InvoiceHoldCreatedBy | CREATED_BY | — | — |
| 3 | InvoiceHoldCreationDate | CREATION_DATE | — | ✅ |
| 4 | InvoiceHoldHeldBy | HELD_BY | — | — |
| 5 | InvoiceHoldHoldDate | HOLD_DATE | — | ✅ |
| 6 | InvoiceHoldHoldDetails | HOLD_DETAILS | — | ✅ |
| 7 | InvoiceHoldHoldLookupCode | HOLD_LOOKUP_CODE | — | ✅ |
| 8 | InvoiceHoldHoldReason | HOLD_REASON | — | ✅ |
| 9 | InvoiceHoldInvoiceId | INVOICE_ID | — | — |
| 10 | InvoiceHoldLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | InvoiceHoldLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | InvoiceHoldLineNumber | LINE_NUMBER | — | — |
| 13 | InvoiceHoldObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | InvoiceHoldOrgId | ORG_ID | — | — |
| 15 | InvoiceHoldReleaseLookupCode | RELEASE_LOOKUP_CODE | — | ✅ |
| 16 | InvoiceHoldReleaseReason | RELEASE_REASON | — | ✅ |
| 17 | InvoiceHoldStatusFlag | STATUS_FLAG | — | — |
| 18 | InvoiceHoldWfStatus | WF_STATUS | — | ✅ |

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderEarliestSettlementDate | EARLIEST_SETTLEMENT_DATE | — | — |
| 2 | InvoiceHeaderExchangeDate | EXCHANGE_DATE | — | — |
| 3 | InvoiceHeaderExchangeRate | EXCHANGE_RATE | — | — |
| 4 | InvoiceHeaderExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 5 | InvoiceHeaderInvoiceAmount | INVOICE_AMOUNT | — | — |
| 6 | InvoiceHeaderInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 7 | InvoiceHeaderInvoiceDate | INVOICE_DATE | — | — |
| 8 | InvoiceHeaderInvoiceId | INVOICE_ID | — | — |
| 9 | InvoiceHeaderInvoiceNum | INVOICE_NUM | — | — |
| 10 | InvoiceHeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 11 | InvoiceHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | InvoiceHeaderOrgId | ORG_ID | — | — |
| 13 | InvoiceHeaderPartyId | PARTY_ID | — | — |
| 14 | InvoiceHeaderPartySiteId | PARTY_SITE_ID | — | — |
| 15 | InvoiceHeaderPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 16 | InvoiceHeaderSetOfBooksId | SET_OF_BOOKS_ID | — | — |
| 17 | InvoiceHeaderSource | SOURCE | — | — |
| 18 | InvoiceHeaderTermsId | TERMS_ID | — | — |
| 19 | InvoiceHeaderVendorSiteId | VENDOR_SITE_ID | — | — |

### [[ap_payment_schedules_all|AP_PAYMENT_SCHEDULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderRemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | PartyPartyId | PARTY_ID | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | PartySitePartySiteId | PARTY_SITE_ID | — | — |

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayDelcodeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | PayDelcodePaymentCode | PAYMENT_CODE | — | — |
| 3 | PayDelcodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |
| 4 | PayReacodeLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | PayReacodePaymentCode | PAYMENT_CODE | — | — |
| 6 | PayReacodePaymentCodeType | PAYMENT_CODE_TYPE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonHoldHeldByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonHoldHeldByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonHoldHeldByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonHoldHeldByPersonId | PERSON_ID | — | — |
| 10 | PersonHoldHeldByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonNameDisplayName | DISPLAY_NAME | — | — |
| 12 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 15 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 16 | PersonUpdatedByEffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 17 | PersonUpdatedByEffectiveStartDate2 | EFFECTIVE_START_DATE | — | — |
| 18 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 19 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserHoldHeldByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserHoldHeldByPersonId | PERSON_ID | — | — |
| 8 | UserHoldHeldByUserGuid | USER_GUID | — | — |
| 9 | UserHoldHeldByUserId | USER_ID | — | — |
| 10 | UserHoldHeldByUsername | USERNAME | — | — |
| 11 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 13 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 14 | UserUpdatedByUserId | USER_ID | — | — |
| 15 | UserUpdatedByUsername | USERNAME | — | — |

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoLineLocLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | PoLineLocLineLocationId | LINE_LOCATION_ID | — | — |
| 3 | PoLineLocObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvShipHeaderInvHoldLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | RcvShipHeaderInvHoldObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | RcvShipHeaderInvHoldRaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | — |
| 4 | RcvShipHeaderInvHoldReceiptNum | RECEIPT_NUM | — | ✅ |
| 5 | RcvShipHeaderInvHoldShipmentHeaderId | SHIPMENT_HEADER_ID | — | — |

### [[rcv_transactions|RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvTransInvHoldLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | RcvTransInvHoldTransactionId | TRANSACTION_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
