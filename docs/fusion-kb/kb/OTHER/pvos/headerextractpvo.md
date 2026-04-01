---
id: DOC-OTHER-PVO-HeaderExtractPVO
doc_type: system-doc
title: "HeaderExtractPVO — PVO Cross-Module"
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
  - HeaderExtractPVO
  - headerextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Header Extract. Acessa as tabelas: DOO_HEADERS_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.HeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 93 | 1 | 1 | 92 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 93 atributos (1 PKs, 92 BICC)

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderAgreementHeaderId | AGREEMENT_HEADER_ID | — | ✅ |
| 2 | HeaderAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | ✅ |
| 3 | HeaderAllowCurrencyOverrideFlag | ALLOW_CURRENCY_OVERRIDE_FLAG | — | ✅ |
| 4 | HeaderAppliedCurrencyCode | APPLIED_CURRENCY_CODE | — | ✅ |
| 5 | HeaderApprovalSequenceNumber | APPROVAL_SEQUENCE_NUMBER | — | ✅ |
| 6 | HeaderBatchId | BATCH_ID | — | ✅ |
| 7 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 8 | HeaderCanceledFlag | CANCELED_FLAG | — | ✅ |
| 9 | HeaderCarrierId | CARRIER_ID | — | ✅ |
| 10 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | ✅ |
| 11 | HeaderComments | COMMENTS | — | ✅ |
| 12 | HeaderConversionDate | CONVERSION_DATE | — | ✅ |
| 13 | HeaderConversionRate | CONVERSION_RATE | — | ✅ |
| 14 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | ✅ |
| 15 | HeaderCreatedBy | CREATED_BY | — | ✅ |
| 16 | HeaderCreatedInRelease | CREATED_IN_RELEASE | — | ✅ |
| 17 | HeaderCreationDate | CREATION_DATE | — | ✅ |
| 18 | HeaderCreationMode | CREATION_MODE | — | ✅ |
| 19 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 20 | HeaderDemandClassCode | DEMAND_CLASS_CODE | — | ✅ |
| 21 | HeaderEarliestAcceptArrivalDate | EARLIEST_ACCEPT_ARRIVAL_DATE | — | ✅ |
| 22 | HeaderEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 23 | HeaderFobPointCode | FOB_POINT_CODE | — | ✅ |
| 24 | HeaderFreezePriceFlag | FREEZE_PRICE_FLAG | — | ✅ |
| 25 | HeaderFreezeShippingChargeFlag | FREEZE_SHIPPING_CHARGE_FLAG | — | ✅ |
| 26 | HeaderFreezeTaxFlag | FREEZE_TAX_FLAG | — | ✅ |
| 27 | HeaderFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 28 | HeaderFulfillOrgId | FULFILL_ORG_ID | — | ✅ |
| 29 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 30 | HeaderInternalComments | INTERNAL_COMMENTS | — | ✅ |
| 31 | HeaderIsEditable | IS_EDITABLE | — | ✅ |
| 32 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 34 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | HeaderLatestAcceptArrivalDate | LATEST_ACCEPT_ARRIVAL_DATE | — | ✅ |
| 36 | HeaderLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 37 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 38 | HeaderMdoFlag | MDO_FLAG | — | ✅ |
| 39 | HeaderModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 40 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | HeaderOnHold | ON_HOLD | — | ✅ |
| 42 | HeaderOpenFlag | OPEN_FLAG | — | ✅ |
| 43 | HeaderOrderNumber | ORDER_NUMBER | — | ✅ |
| 44 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 45 | HeaderOrderedDate | ORDERED_DATE | — | ✅ |
| 46 | HeaderOrgId | ORG_ID | — | ✅ |
| 47 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 48 | HeaderOwnerId | OWNER_ID | — | ✅ |
| 49 | HeaderPackingInstructions | PACKING_INSTRUCTIONS | — | ✅ |
| 50 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | ✅ |
| 51 | HeaderPaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 52 | HeaderPreCreditCheckedFlag | PRE_CREDIT_CHECKED_FLAG | — | ✅ |
| 53 | HeaderPricedOn | PRICED_ON | — | ✅ |
| 54 | HeaderPricingDate | PRICING_DATE | — | — |
| 55 | HeaderPricingSegmentCode | PRICING_SEGMENT_CODE | — | ✅ |
| 56 | HeaderPricingSegmentExplanation | PRICING_SEGMENT_EXPLANATION | — | ✅ |
| 57 | HeaderPricingStrategyExplanation | PRICING_STRATEGY_EXPLANATION | — | ✅ |
| 58 | HeaderPricingStrategyId | PRICING_STRATEGY_ID | — | ✅ |
| 59 | HeaderReferenceHeaderId | REFERENCE_HEADER_ID | — | ✅ |
| 60 | HeaderRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | ✅ |
| 61 | HeaderRequestCancelDate | REQUEST_CANCEL_DATE | — | ✅ |
| 62 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 63 | HeaderRevisionSourceOrderSystem | REVISION_SOURCE_ORDER_SYSTEM | — | ✅ |
| 64 | HeaderSalesChannelCode | SALES_CHANNEL_CODE | — | ✅ |
| 65 | HeaderSalespersonId | SALESPERSON_ID | — | ✅ |
| 66 | HeaderSegmentExplanationMsgName | SEGMENT_EXPLANATION_MSG_NAME | — | ✅ |
| 67 | HeaderShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 68 | HeaderShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 69 | HeaderShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 70 | HeaderShippingInstructions | SHIPPING_INSTRUCTIONS | — | ✅ |
| 71 | HeaderShipsetFlag | SHIPSET_FLAG | — | ✅ |
| 72 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | ✅ |
| 73 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | ✅ |
| 74 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | ✅ |
| 75 | HeaderSoldToPartyContactPointId | SOLD_TO_PARTY_CONTACT_POINT_ID | — | ✅ |
| 76 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |
| 77 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | ✅ |
| 78 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | ✅ |
| 79 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 80 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 81 | HeaderSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 82 | HeaderSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | ✅ |
| 83 | HeaderStatusCode | STATUS_CODE | — | ✅ |
| 84 | HeaderStrategyExplanationMsgName | STRATEGY_EXPLANATION_MSG_NAME | — | ✅ |
| 85 | HeaderSubinventory | SUBINVENTORY | — | ✅ |
| 86 | HeaderSubmittedBy | SUBMITTED_BY | — | ✅ |
| 87 | HeaderSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 88 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | ✅ |
| 89 | HeaderSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | ✅ |
| 90 | HeaderSupplierId | SUPPLIER_ID | — | ✅ |
| 91 | HeaderSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 92 | HeaderTradeComplianceResultCode | TRADE_COMPLIANCE_RESULT_CODE | — | ✅ |
| 93 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
