---
id: DOC-PO-PVO-PurchasingSystemParameterExtractPVO
doc_type: system-doc
title: "PurchasingSystemParameterExtractPVO — PVO Purchasing"
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
  - PurchasingSystemParameterExtractPVO
  - purchasingsystemparameterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingSystemParameterExtractPVO

## 📌 Visão Geral

Extrai os parâmetros de configuração do sistema de compras por unidade de negócio (tolerâncias, matching, aprovação automática) para carga BICC. Essencial para auditoria de configuração e conformidade.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingSystemParameterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 1 | 1 | 75 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]] — 75 atributos (1 PKs, 75 BICC)

---

## ⚙️ Atributos

### [[po_system_parameters_all|PO_SYSTEM_PARAMETERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 2 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 3 | AllowItemDescUpdateFlag | ALLOW_ITEM_DESC_UPDATE_FLAG | — | ✅ |
| 4 | AllowManulPriceUpdateOrder | ALLOW_MANUL_PRICE_UPDATE_ORDER | — | ✅ |
| 5 | AllowRetroPricing | ALLOW_RETRO_PRICING | — | ✅ |
| 6 | AwardApprovalEnabledFlag | AWARD_APPROVAL_ENABLED_FLAG | — | ✅ |
| 7 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 8 | BypassApprovalFlag | BYPASS_APPROVAL_FLAG | — | ✅ |
| 9 | CarrierId | CARRIER_ID | — | ✅ |
| 10 | CatAdminAuthoringAcceptance | CAT_ADMIN_AUTHORING_ACCEPTANCE | — | ✅ |
| 11 | CommunicateCoFlag | COMMUNICATE_CO_FLAG | — | ✅ |
| 12 | CommunicatePaFlag | COMMUNICATE_PA_FLAG | — | ✅ |
| 13 | ConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 14 | ConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 15 | CreatedBy | CREATED_BY | — | ✅ |
| 16 | CreationDate | CREATION_DATE | — | ✅ |
| 17 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 18 | DefaultBuyerId | DEFAULT_BUYER_ID | — | ✅ |
| 19 | DefaultPromiseDate | DEFAULT_PROMISE_DATE | — | ✅ |
| 20 | DefaultRateType | DEFAULT_RATE_TYPE | — | ✅ |
| 21 | DoctypeId | DOCTYPE_ID | — | ✅ |
| 22 | EmailAttachmentFilename | EMAIL_ATTACHMENT_FILENAME | — | ✅ |
| 23 | EnforceMinBidPrice | ENFORCE_MIN_BID_PRICE | — | ✅ |
| 24 | EnforceVendorHoldFlag | ENFORCE_VENDOR_HOLD_FLAG | — | ✅ |
| 25 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 26 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 27 | GenOrderForNegReqsFlag | GEN_ORDER_FOR_NEG_REQS_FLAG | — | ✅ |
| 28 | GenerateOrdersAutomatic | GENERATE_ORDERS_AUTOMATIC | — | ✅ |
| 29 | GroupRequisitionLines | GROUP_REQUISITION_LINES | — | ✅ |
| 30 | GroupRequisitions | GROUP_REQUISITIONS | — | ✅ |
| 31 | InventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 32 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 33 | LanguageCode | LANGUAGE_CODE | — | ✅ |
| 34 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | LineTypeId | LINE_TYPE_ID | — | ✅ |
| 38 | ManualReceiptNumType | MANUAL_RECEIPT_NUM_TYPE | — | ✅ |
| 39 | ManualReqNumType | MANUAL_REQ_NUM_TYPE | — | ✅ |
| 40 | MatchOption | MATCH_OPTION | — | ✅ |
| 41 | MaxAttachmentSize | MAX_ATTACHMENT_SIZE | — | ✅ |
| 42 | MinReleaseAmount | MIN_RELEASE_AMOUNT | — | ✅ |
| 43 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 44 | NegApprovalEnabledFlag | NEG_APPROVAL_ENABLED_FLAG | — | ✅ |
| 45 | NextApproverLookupCode | NEXT_APPROVER_LOOKUP_CODE | — | ✅ |
| 46 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 47 | PrcBuId | PRC_BU_ID | 🔑 | ✅ |
| 48 | PriceBreakLookupCode | PRICE_BREAK_LOOKUP_CODE | — | ✅ |
| 49 | PriceChangeAmount | PRICE_CHANGE_AMOUNT | — | ✅ |
| 50 | ReceiveCloseCode | RECEIVE_CLOSE_CODE | — | ✅ |
| 51 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 52 | ReceivingFlag | RECEIVING_FLAG | — | ✅ |
| 53 | RfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 54 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 55 | SourcingSuppEligibilityFlag | SOURCING_SUPP_ELIGIBILITY_FLAG | — | ✅ |
| 56 | StyleId | STYLE_ID | — | ✅ |
| 57 | SubmitApprovalAutomatic | SUBMIT_APPROVAL_AUTOMATIC | — | ✅ |
| 58 | SupplierAuthoringAcceptance | SUPPLIER_AUTHORING_ACCEPTANCE | — | ✅ |
| 59 | TaxFromItemFlag | TAX_FROM_ITEM_FLAG | — | ✅ |
| 60 | TaxFromShipToLocFlag | TAX_FROM_SHIP_TO_LOC_FLAG | — | ✅ |
| 61 | TaxFromSystemFlag | TAX_FROM_SYSTEM_FLAG | — | ✅ |
| 62 | TaxFromVendorFlag | TAX_FROM_VENDOR_FLAG | — | ✅ |
| 63 | TaxFromVendorSiteFlag | TAX_FROM_VENDOR_SITE_FLAG | — | ✅ |
| 64 | TaxHierItem | TAX_HIER_ITEM | — | ✅ |
| 65 | TaxHierShipToLoc | TAX_HIER_SHIP_TO_LOC | — | ✅ |
| 66 | TaxHierSystem | TAX_HIER_SYSTEM | — | ✅ |
| 67 | TaxHierVendor | TAX_HIER_VENDOR | — | ✅ |
| 68 | TaxHierVendorSite | TAX_HIER_VENDOR_SITE | — | ✅ |
| 69 | TermsId | TERMS_ID | — | ✅ |
| 70 | UseNeedByDate | USE_NEED_BY_DATE | — | ✅ |
| 71 | UseSalesOrderNumberFlag | USE_SALES_ORDER_NUMBER_FLAG | — | ✅ |
| 72 | UseShipTo | USE_SHIP_TO | — | ✅ |
| 73 | UseShipToForGroupReqs | USE_SHIP_TO_FOR_GROUP_REQS | — | ✅ |
| 74 | UserDefinedReceiptNumCode | USER_DEFINED_RECEIPT_NUM_CODE | — | ✅ |
| 75 | UserDefinedReqNumCode | USER_DEFINED_REQ_NUM_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
