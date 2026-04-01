---
id: DOC-OTHER-PVO-CmrPurchaseIntransitAmtsExtractPVO
doc_type: system-doc
title: "CmrPurchaseIntransitAmtsExtractPVO — PVO Cross-Module"
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
  - CmrPurchaseIntransitAmtsExtractPVO
  - cmrpurchaseintransitamtsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CmrPurchaseIntransitAmtsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cmr Purchase Intransit Amts Extract. Acessa as tabelas: CMR_ASN_INTRANSIT_AMTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CmrBiccExtractAM.CmrPurchaseIntransitAmtsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 1 | 1 | 60 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmr_asn_intransit_amts|CMR_ASN_INTRANSIT_AMTS]] — 60 atributos (1 PKs, 60 BICC)

---

## ⚙️ Atributos

### [[cmr_asn_intransit_amts|CMR_ASN_INTRANSIT_AMTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CmrAsnIntransitAmtsPEOAsnIntransitId | ASN_INTRANSIT_ID | 🔑 | ✅ |
| 2 | CmrAsnIntransitAmtsPEOAsnLineNumber | ASN_LINE_NUMBER | — | ✅ |
| 3 | CmrAsnIntransitAmtsPEOAsnStatus | ASN_STATUS | — | ✅ |
| 4 | CmrAsnIntransitAmtsPEOAsnUomCode | ASN_UOM_CODE | — | ✅ |
| 5 | CmrAsnIntransitAmtsPEOBillToBusinessUnitId | BILL_TO_BUSINESS_UNIT_ID | — | ✅ |
| 6 | CmrAsnIntransitAmtsPEOBusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 7 | CmrAsnIntransitAmtsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CmrAsnIntransitAmtsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CmrAsnIntransitAmtsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | CmrAsnIntransitAmtsPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 11 | CmrAsnIntransitAmtsPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 12 | CmrAsnIntransitAmtsPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 13 | CmrAsnIntransitAmtsPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 14 | CmrAsnIntransitAmtsPEOFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 15 | CmrAsnIntransitAmtsPEOFuncCurrencyCode | FUNC_CURRENCY_CODE | — | ✅ |
| 16 | CmrAsnIntransitAmtsPEOIntransitAmount | INTRANSIT_AMOUNT | — | ✅ |
| 17 | CmrAsnIntransitAmtsPEOIntransitAmtFuncCurr | INTRANSIT_AMT_FUNC_CURR | — | ✅ |
| 18 | CmrAsnIntransitAmtsPEOIntransitQuantity | INTRANSIT_QUANTITY | — | ✅ |
| 19 | CmrAsnIntransitAmtsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 20 | CmrAsnIntransitAmtsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 21 | CmrAsnIntransitAmtsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CmrAsnIntransitAmtsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CmrAsnIntransitAmtsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CmrAsnIntransitAmtsPEOLatestReceiptDate | LATEST_RECEIPT_DATE | — | ✅ |
| 25 | CmrAsnIntransitAmtsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 26 | CmrAsnIntransitAmtsPEOLineNumber | LINE_NUMBER | — | ✅ |
| 27 | CmrAsnIntransitAmtsPEONewNrTax | NEW_NR_TAX | — | ✅ |
| 28 | CmrAsnIntransitAmtsPEONewPoPrice | NEW_PO_PRICE | — | ✅ |
| 29 | CmrAsnIntransitAmtsPEONrTax | NR_TAX | — | ✅ |
| 30 | CmrAsnIntransitAmtsPEOOwnershipChange | OWNERSHIP_CHANGE | — | ✅ |
| 31 | CmrAsnIntransitAmtsPEOPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 32 | CmrAsnIntransitAmtsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 33 | CmrAsnIntransitAmtsPEOPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 34 | CmrAsnIntransitAmtsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | ✅ |
| 35 | CmrAsnIntransitAmtsPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 36 | CmrAsnIntransitAmtsPEOPoNumber | PO_NUMBER | — | ✅ |
| 37 | CmrAsnIntransitAmtsPEOPoPrice | PO_PRICE | — | ✅ |
| 38 | CmrAsnIntransitAmtsPEOPoScheduleNumber | PO_SCHEDULE_NUMBER | — | ✅ |
| 39 | CmrAsnIntransitAmtsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 40 | CmrAsnIntransitAmtsPEOPriorIntransitQuantity | PRIOR_INTRANSIT_QUANTITY | — | ✅ |
| 41 | CmrAsnIntransitAmtsPEOReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 42 | CmrAsnIntransitAmtsPEOReceivedQuantity | RECEIVED_QUANTITY | — | ✅ |
| 43 | CmrAsnIntransitAmtsPEORetroPriceFlag | RETRO_PRICE_FLAG | — | ✅ |
| 44 | CmrAsnIntransitAmtsPEOReturnQuantity | RETURN_QUANTITY | — | ✅ |
| 45 | CmrAsnIntransitAmtsPEOReversalQuantity | REVERSAL_QUANTITY | — | ✅ |
| 46 | CmrAsnIntransitAmtsPEORunDate | RUN_DATE | — | ✅ |
| 47 | CmrAsnIntransitAmtsPEORunMode | RUN_MODE | — | ✅ |
| 48 | CmrAsnIntransitAmtsPEOScheduleStatus | SCHEDULE_STATUS | — | ✅ |
| 49 | CmrAsnIntransitAmtsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 50 | CmrAsnIntransitAmtsPEOShipmentDate | SHIPMENT_DATE | — | ✅ |
| 51 | CmrAsnIntransitAmtsPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 52 | CmrAsnIntransitAmtsPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 53 | CmrAsnIntransitAmtsPEOShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 54 | CmrAsnIntransitAmtsPEOShipmentQuantity | SHIPMENT_QUANTITY | — | ✅ |
| 55 | CmrAsnIntransitAmtsPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 56 | CmrAsnIntransitAmtsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 57 | CmrAsnIntransitAmtsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 58 | CmrAsnIntransitAmtsPEOUomConversionFactor | UOM_CONVERSION_FACTOR | — | ✅ |
| 59 | CmrAsnIntransitAmtsPEOVendorId | VENDOR_ID | — | ✅ |
| 60 | CmrAsnIntransitAmtsPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
