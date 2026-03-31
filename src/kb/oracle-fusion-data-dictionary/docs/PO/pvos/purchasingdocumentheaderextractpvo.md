---
id: DOC-PO-PVO-PurchasingDocumentHeaderExtractPVO
doc_type: system-doc
title: "PurchasingDocumentHeaderExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentHeaderExtractPVO
  - purchasingdocumentheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentHeaderExtractPVO

## 📌 Visão Geral

Extrai os cabeçalhos de ordens de compra (Purchase Orders) para carga BICC, incluindo fornecedor, valor total, moeda, status de aprovação, tipo de documento e parâmetros do sistema. Essencial para análise de compras, acompanhamento de contratos e controle de gastos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 154 | 2 | 1 | 148 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[po_headers_all|PO_HEADERS_ALL]] — 116 atributos (1 PKs, 110 BICC)
- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 38 atributos (38 BICC)

---

## ⚙️ Atributos

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceDueDate | ACCEPTANCE_DUE_DATE | — | ✅ |
| 2 | AcceptanceRequiredFlag | ACCEPTANCE_REQUIRED_FLAG | — | ✅ |
| 3 | AcceptanceWithinDays | ACCEPTANCE_WITHIN_DAYS | — | ✅ |
| 4 | AdditionalContactEmailAddress | ALT_CONTACT_EMAIL_ADDRESS | — | — |
| 5 | AgentId | AGENT_ID | — | ✅ |
| 6 | AgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 7 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 8 | AllowMultipleSitesFlag | ALLOW_MULTIPLE_SITES_FLAG | — | ✅ |
| 9 | AmountLimit | AMOUNT_LIMIT | — | ✅ |
| 10 | AmountReleased | AMOUNT_RELEASED | — | ✅ |
| 11 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 12 | ApprovedFlag | APPROVED_FLAG | — | ✅ |
| 13 | BccEmailAddress | BCC_EMAIL_ADDRESS | — | ✅ |
| 14 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 15 | BillingCycleClosingDate | BILLING_CYCLE_CLOSING_DATE | — | ✅ |
| 16 | BilltoBuId | BILLTO_BU_ID | — | ✅ |
| 17 | BlanketTotalAmount | BLANKET_TOTAL_AMOUNT | — | ✅ |
| 18 | BudgetControlEnabledFlag | BUDGET_CONTROL_ENABLED_FLAG | — | ✅ |
| 19 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 20 | CarrierId | CARRIER_ID | — | ✅ |
| 21 | CatAdminAuthEnabledFlag | CAT_ADMIN_AUTH_ENABLED_FLAG | — | ✅ |
| 22 | CcEmailAddress | CC_EMAIL_ADDRESS | — | ✅ |
| 23 | ChangeRequestedBy | CHANGE_REQUESTED_BY | — | ✅ |
| 24 | ChangeSummary | CHANGE_SUMMARY | — | ✅ |
| 25 | ChecklistId | CHECKLIST_ID | — | — |
| 26 | ClosedDate | CLOSED_DATE | — | ✅ |
| 27 | Comments | COMMENTS | — | ✅ |
| 28 | ConfirmingOrderFlag | CONFIRMING_ORDER_FLAG | — | ✅ |
| 29 | ConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 30 | ConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 31 | ContermsExistFlag | CONTERMS_EXIST_FLAG | — | ✅ |
| 32 | CpaReference | CPA_REFERENCE | — | ✅ |
| 33 | CreatedBy | CREATED_BY | — | ✅ |
| 34 | CreatedLanguage | CREATED_LANGUAGE | — | ✅ |
| 35 | CreationDate | CREATION_DATE | — | ✅ |
| 36 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 37 | CurrentVersionId | CURRENT_VERSION_ID | — | — |
| 38 | DefaultConsignmentLineFlag | DEFAULT_CONSIGNMENT_LINE_FLAG | — | ✅ |
| 39 | DefaultPoTradeOrgId | DEFAULT_PO_TRADE_ORG_ID | — | ✅ |
| 40 | DefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 41 | DocumentCreationMethod | DOCUMENT_CREATION_METHOD | — | ✅ |
| 42 | DocumentStatus | DOCUMENT_STATUS | — | ✅ |
| 43 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 44 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 45 | EncumbranceRequiredFlag | ENCUMBRANCE_REQUIRED_FLAG | — | ✅ |
| 46 | EndDate | END_DATE | — | ✅ |
| 47 | Fax | FAX | — | ✅ |
| 48 | FirmDate | FIRM_DATE | — | ✅ |
| 49 | FirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 50 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 51 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 52 | FrozenFlag | FROZEN_FLAG | — | ✅ |
| 53 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 54 | GenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | ✅ |
| 55 | GroupRequisitionLines | GROUP_REQUISITION_LINES | — | ✅ |
| 56 | GroupRequisitions | GROUP_REQUISITIONS | — | ✅ |
| 57 | InterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 58 | LastBilledDate | LAST_BILLED_DATE | — | ✅ |
| 59 | LastReleaseDate | LAST_RELEASE_DATE | — | ✅ |
| 60 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 61 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | MasterContractId | MASTER_CONTRACT_ID | — | ✅ |
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
| 78 | Rate | RATE | — | ✅ |
| 79 | RateDate | RATE_DATE | — | ✅ |
| 80 | RateType | RATE_TYPE | — | ✅ |
| 81 | ReferenceNum | REFERENCE_NUM | — | — |
| 82 | ReleaseMethod | RELEASE_METHOD | — | ✅ |
| 83 | ReqBuId | REQ_BU_ID | — | ✅ |
| 84 | RetroPriceApplyUpdatesFlag | RETRO_PRICE_APPLY_UPDATES_FLAG | — | ✅ |
| 85 | RetroPriceCommUpdatesFlag | RETRO_PRICE_COMM_UPDATES_FLAG | — | ✅ |
| 86 | RetroPriceInitApprovalFlag | RETRO_PRICE_INIT_APPROVAL_FLAG | — | ✅ |
| 87 | RetroPriceOpenOrderFlag | RETRO_PRICE_OPEN_ORDER_FLAG | — | ✅ |
| 88 | RevisedDate | REVISED_DATE | — | ✅ |
| 89 | RevisionNum | REVISION_NUM | — | ✅ |
| 90 | Segment1 | SEGMENT1 | — | ✅ |
| 91 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 92 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 93 | ShippingControl | SHIPPING_CONTROL | — | ✅ |
| 94 | SignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | ✅ |
| 95 | SkipElectronicCommFlag | SKIP_ELECTRONIC_COMM_FLAG | — | ✅ |
| 96 | SoldtoLeId | SOLDTO_LE_ID | — | ✅ |
| 97 | SourcingPriority | SOURCING_PRIORITY | — | — |
| 98 | SpecialHandlingTypeCode | SPECIAL_HANDLING_TYPE_CODE | — | — |
| 99 | StartDate | START_DATE | — | ✅ |
| 100 | StyleId | STYLE_ID | — | ✅ |
| 101 | SubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | ✅ |
| 102 | SubmitDate | SUBMIT_DATE | — | ✅ |
| 103 | SupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 104 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 105 | TaxDocumentSubtype | TAX_DOCUMENT_SUBTYPE | — | ✅ |
| 106 | TermsId | TERMS_ID | — | ✅ |
| 107 | ThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 108 | TypeLookupCode | TYPE_LOOKUP_CODE | — | ✅ |
| 109 | UseNeedByDate | USE_NEED_BY_DATE | — | ✅ |
| 110 | UseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | ✅ |
| 111 | UseShipTo | USE_SHIP_TO | — | ✅ |
| 112 | UseShipToForGroupReqs | USE_SHIP_TO_FOR_GROUP_REQS | — | ✅ |
| 113 | VendorContactId | VENDOR_CONTACT_ID | — | ✅ |
| 114 | VendorId | VENDOR_ID | — | ✅ |
| 115 | VendorOrderNum | VENDOR_ORDER_NUM | — | ✅ |
| 116 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | ✅ |
| 2 | AllowManulPriceUpdateOrder | ALLOW_MANUL_PRICE_UPDATE_ORDER | — | ✅ |
| 3 | AllowRetroPricing | ALLOW_RETRO_PRICING | — | ✅ |
| 4 | AwardApprovalEnabledFlag | AWARD_APPROVAL_ENABLED_FLAG | — | ✅ |
| 5 | BypassApprovalFlag | BYPASS_APPROVAL_FLAG | — | ✅ |
| 6 | CatAdminAuthoringAcceptance | CAT_ADMIN_AUTHORING_ACCEPTANCE | — | ✅ |
| 7 | CurrencyCode1 | CURRENCY_CODE | — | ✅ |
| 8 | DefaultBuyerId | DEFAULT_BUYER_ID | — | ✅ |
| 9 | DefaultPromiseDate | DEFAULT_PROMISE_DATE | — | ✅ |
| 10 | DefaultRateType | DEFAULT_RATE_TYPE | — | ✅ |
| 11 | DoctypeId | DOCTYPE_ID | — | ✅ |
| 12 | EmailAttachmentFilename | EMAIL_ATTACHMENT_FILENAME | — | ✅ |
| 13 | EnforceMinBidPrice | ENFORCE_MIN_BID_PRICE | — | ✅ |
| 14 | EnforceVendorHoldFlag | ENFORCE_VENDOR_HOLD_FLAG | — | ✅ |
| 15 | GenOrderForNegReqsFlag | GEN_ORDER_FOR_NEG_REQS_FLAG | — | ✅ |
| 16 | InventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 17 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 18 | LanguageCode | LANGUAGE_CODE | — | ✅ |
| 19 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 20 | ManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | ✅ |
| 21 | MatchOption | MATCH_OPTION | — | ✅ |
| 22 | MaxAttachmentSize | MAX_ATTACHMENT_SIZE | — | ✅ |
| 23 | ModeOfTransport1 | MODE_OF_TRANSPORT | — | ✅ |
| 24 | NegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
| 25 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | ✅ |
| 26 | PriceChangeAmount | PRICE_CHANGE_AMOUNT | — | ✅ |
| 27 | ProcurementOptionsPrcBuId | PRC_BU_ID | — | ✅ |
| 28 | ReceiveCloseCode | RECEIVE_CLOSE_CODE | — | ✅ |
| 29 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 30 | ReceivingFlag | RECEIVING_FLAG | — | ✅ |
| 31 | ServiceLevel1 | SERVICE_LEVEL | — | ✅ |
| 32 | SourcingSuppEligibilityFlag | SOURCING_SUPP_ELIGIBILITY_FLAG | — | ✅ |
| 33 | StyleId1 | STYLE_ID | — | ✅ |
| 34 | SupplierAuthoringAcceptance | SUPPLIER_AUTHORING_ACCEPTANCE | — | ✅ |
| 35 | TermsId1 | TERMS_ID | — | ✅ |
| 36 | UseShipToForGroupReqs1 | USE_SHIP_TO_FOR_GROUP_REQS | — | ✅ |
| 37 | UserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | ✅ |
| 38 | UserDefinedReqNumCode | USER_DEFINED_REQ_NUM_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
