---
id: DOC-PO-PVO-DraftPurchasingDocumentHeaderExtractPVO
doc_type: system-doc
title: "DraftPurchasingDocumentHeaderExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DraftPurchasingDocumentHeaderExtractPVO
  - draftpurchasingdocumentheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DraftPurchasingDocumentHeaderExtractPVO

## 📌 Visão Geral

Extrai os cabeçalhos de rascunhos de documentos de compra ainda não submetidos para aprovação. Permite análise de pedidos em elaboração, previsão de demanda e identificação de requisições pendentes de finalização.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.DraftPurchasingDocumentHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 118 | 1 | 1 | 115 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]] — 118 atributos (1 PKs, 115 BICC)

---

## ⚙️ Atributos

### [[po_headers_draft_all|PO_HEADERS_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | ✅ |
| 2 | AcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | ✅ |
| 3 | AcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | ✅ |
| 4 | AdditionalContactEmailAddress | ALT_CONTACT_EMAIL_ADDRESS | — | — |
| 5 | AgentId | AGENT_ID | — | ✅ |
| 6 | AgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 7 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 8 | AmountLimit | AMOUNT_LIMIT | — | ✅ |
| 9 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 10 | BillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | ✅ |
| 11 | BilltoBuId | BILLTO_BU_ID | — | ✅ |
| 12 | BlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 13 | BudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 14 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 15 | CarrierId | CARRIER_ID | — | ✅ |
| 16 | CbcAccountingDate | CBC_ACCOUNTING_DATE | — | ✅ |
| 17 | ChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | ✅ |
| 18 | ChangeRequestedBy | CHANGE_REQUESTED_BY | — | ✅ |
| 19 | ChangeSummary | CHANGE_SUMMARY | — | ✅ |
| 20 | ChecklistId | CHECKLIST_ID | — | — |
| 21 | Comments | COMMENTS | — | ✅ |
| 22 | ConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 23 | ConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 24 | ConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 25 | ContermsArticlesUpdDate | CONTERMS_ARTICLES_UPD_DATE | — | ✅ |
| 26 | ContermsDelivUpdDate | CONTERMS_DELIV_UPD_DATE | — | ✅ |
| 27 | ContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 28 | CpaReference | CPA_REFERENCE | — | ✅ |
| 29 | CreatedBy | CREATED_BY | — | ✅ |
| 30 | CreatedLanguage | CREATED_LANGUAGE | — | ✅ |
| 31 | CreationDate | CREATION_DATE | — | ✅ |
| 32 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 33 | DefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | ✅ |
| 34 | DefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | ✅ |
| 35 | DefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 36 | DocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | ✅ |
| 37 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 38 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 39 | EncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | ✅ |
| 40 | EndDate | END_DATE | — | ✅ |
| 41 | EntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | ✅ |
| 42 | ExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | ✅ |
| 43 | Fax | FAX | — | ✅ |
| 44 | FirmDate | FIRM_DATE | — | ✅ |
| 45 | FirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | ✅ |
| 46 | FirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 47 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 48 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 49 | FromHeaderId | FROM_HEADER_ID | — | ✅ |
| 50 | FromTypeLookupCode | FROM_TYPE_LOOKUP_CODE | — | ✅ |
| 51 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 52 | GenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | ✅ |
| 53 | GovernmentContext | GOVERNMENT_CONTEXT | — | ✅ |
| 54 | GroupRequisitionLines | GROUP_REQUISITION_LINES | — | ✅ |
| 55 | GroupRequisitions | GROUP_REQUISITIONS | — | ✅ |
| 56 | InterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 57 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 58 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 59 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | ManualBccdOverrideFlag | MANUAL_BCCD_OVERRIDE_FLAG | — | ✅ |
| 63 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 64 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 65 | NoteToAuthorizer | NOTE_TO_AUTHORIZER | — | ✅ |
| 66 | NoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 67 | NoteToVendor | NOTE_TO_VENDOR | — | ✅ |
| 68 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 69 | OrchestrationOrderFlag | ORCHESTRATION_ORDER_FLAG | — | ✅ |
| 70 | OverridingApproverId | OVERRIDING_APPROVER_ID | — | ✅ |
| 71 | PayOnCode | PAY_ON_CODE | — | ✅ |
| 72 | PayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 73 | PcardId | PCARD_ID | — | ✅ |
| 74 | PendingSignatureFlag | PENDING_SIGNATURE_FLAG | — | ✅ |
| 75 | PoHeaderId | PO_HEADER_ID | 🔑 | ✅ |
| 76 | PrcBuId | PRC_BU_ID | — | ✅ |
| 77 | PriceUpdateTolerance | PRICE_UPDATE_TOLERANCE | — | ✅ |
| 78 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 79 | ProgramName | PROGRAM_NAME | — | ✅ |
| 80 | Rate | RATE | — | ✅ |
| 81 | RateDate | RATE_DATE | — | ✅ |
| 82 | RateType | RATE_TYPE | — | ✅ |
| 83 | ReferenceNum | REFERENCE_NUM | — | ✅ |
| 84 | ReqBuId | REQ_BU_ID | — | ✅ |
| 85 | RequestId | REQUEST_ID | — | ✅ |
| 86 | RetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | ✅ |
| 87 | RetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | ✅ |
| 88 | RetroPriceInitApprovalFlag | RETRO_PRICE_INIT_APPROVAL_FLAG | — | ✅ |
| 89 | RetroPriceOpenOrderFlag | RETRO_PRICE_OPEN_ORDER_FLAG | — | ✅ |
| 90 | Segment1 | SEGMENT1 | — | ✅ |
| 91 | Segment2 | SEGMENT2 | — | ✅ |
| 92 | Segment3 | SEGMENT3 | — | ✅ |
| 93 | Segment4 | SEGMENT4 | — | ✅ |
| 94 | Segment5 | SEGMENT5 | — | ✅ |
| 95 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 96 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 97 | ShippingControl | SHIPPING_CONTROL | — | ✅ |
| 98 | SignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | ✅ |
| 99 | SoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 100 | SourcingPriority | SOURCING_PRIORITY | — | — |
| 101 | StartDate | START_DATE | — | ✅ |
| 102 | StyleId | STYLE_ID | — | ✅ |
| 103 | SubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | ✅ |
| 104 | SubmitDate | SUBMIT_DATE | — | ✅ |
| 105 | SupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 106 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 107 | TaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | ✅ |
| 108 | TermsId | TERMS_ID | — | ✅ |
| 109 | ThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 110 | TypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 111 | UseNeedByDate | USE_NEED_BY_DATE | — | ✅ |
| 112 | UseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | ✅ |
| 113 | UseShipTo | USE_SHIP_TO | — | ✅ |
| 114 | VendorContactId | VENDOR_CONTACT_ID | — | ✅ |
| 115 | VendorId | VENDOR_ID | — | ✅ |
| 116 | VendorOrderNum | VENDOR_ORDER_NUM | — | ✅ |
| 117 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 118 | XmlFlag | XML_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
