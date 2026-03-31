---
id: DOC-OTHER-PVO-ProgramUtilExtractPVO
doc_type: system-doc
title: "ProgramUtilExtractPVO — PVO Cross-Module"
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
  - ProgramUtilExtractPVO
  - programutilextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramUtilExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Util Extract. Acessa as tabelas: CJM_PROGRAMS_UTILIZED_ALL_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramUtilExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 91 | 1 | 1 | 91 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_programs_utilized_all_b|CJM_PROGRAMS_UTILIZED_ALL_B]] — 91 atributos (1 PKs, 91 BICC)

---

## ⚙️ Atributos

### [[cjm_programs_utilized_all_b|CJM_PROGRAMS_UTILIZED_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualQty | ACCRUAL_QTY | — | ✅ |
| 2 | AccrualQtyInInvUom | ACCRUAL_QTY_IN_INV_UOM | — | ✅ |
| 3 | AccrualQtyInProgLineUom | ACCRUAL_QTY_IN_PROG_LINE_UOM | — | ✅ |
| 4 | AccrualTrxType | ACCRUAL_TRX_TYPE | — | ✅ |
| 5 | AccrualType | ACCRUAL_TYPE | — | ✅ |
| 6 | AccrualUom | ACCRUAL_UOM | — | ✅ |
| 7 | AcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 8 | AcctdAmountRemaining | ACCTD_AMOUNT_REMAINING | — | ✅ |
| 9 | AdjustmentDate | ADJUSTMENT_DATE | — | ✅ |
| 10 | AdjustmentReasonId | ADJUSTMENT_REASON_ID | — | ✅ |
| 11 | AdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 12 | AdjustmentTypeId | ADJUSTMENT_TYPE_ID | — | ✅ |
| 13 | BillOfLadingNumber | BILL_OF_LADING_NUMBER | — | ✅ |
| 14 | BillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 15 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 16 | BuId | BU_ID | — | ✅ |
| 17 | CategoryId | CATEGORY_ID | — | ✅ |
| 18 | ChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | ✅ |
| 19 | CreatedBy | CREATED_BY | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | CustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 22 | DiscountAmount | DISCOUNT_AMOUNT | — | ✅ |
| 23 | DiscountType | DISCOUNT_TYPE | — | ✅ |
| 24 | DistributorId | DISTRIBUTOR_ID | — | ✅ |
| 25 | DistributorSiteId | DISTRIBUTOR_SITE_ID | — | ✅ |
| 26 | DocumentProgramId | DOCUMENT_PROGRAM_ID | — | ✅ |
| 27 | EarnedAccrualsEvent | EARNED_ACCRUALS_EVENT | — | ✅ |
| 28 | ExchangeRate | EXCHANGE_RATE | — | ✅ |
| 29 | ExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 30 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 31 | GlDate | GL_DATE | — | ✅ |
| 32 | GlPostedFlag | GL_POSTED_FLAG | — | ✅ |
| 33 | InvoiceDate | INVOICE_DATE | — | ✅ |
| 34 | InvoiceId | INVOICE_ID | — | ✅ |
| 35 | InvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 36 | InvoiceNumber | INVOICE_NUMBER | — | ✅ |
| 37 | InvoiceSourceApplication | INVOICE_SOURCE_APPLICATION | — | ✅ |
| 38 | InvoiceSourceCode | INVOICE_SOURCE_CODE | — | ✅ |
| 39 | ItemId | ITEM_ID | — | ✅ |
| 40 | ItemLevelCode | ITEM_LEVEL_CODE | — | ✅ |
| 41 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 42 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 43 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 45 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 46 | ManualAdjustmentId | MANUAL_ADJUSTMENT_ID | — | ✅ |
| 47 | MatchOption | MATCH_OPTION | — | ✅ |
| 48 | ObjectId | OBJECT_ID | — | ✅ |
| 49 | ObjectLineId | OBJECT_LINE_ID | — | ✅ |
| 50 | ObjectType | OBJECT_TYPE | — | ✅ |
| 51 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | OrigUtilizationId | ORIG_UTILIZATION_ID | — | ✅ |
| 53 | PeriodName | PERIOD_NAME | — | ✅ |
| 54 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 55 | PoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 56 | PoNumber | PO_NUMBER | — | ✅ |
| 57 | PriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 58 | PricePeriodicityCode | PRICE_PERIODICITY_CODE | — | ✅ |
| 59 | PricingSourceId | PRICING_SOURCE_ID | — | ✅ |
| 60 | PricingSourceTypeCode | PRICING_SOURCE_TYPE_CODE | — | ✅ |
| 61 | ProgramAmount | PROGRAM_AMOUNT | — | ✅ |
| 62 | ProgramAmountRemaining | PROGRAM_AMOUNT_REMAINING | — | ✅ |
| 63 | ProgramCurrencyCode | PROGRAM_CURRENCY_CODE | — | ✅ |
| 64 | ProgramHeaderId | PROGRAM_HEADER_ID | — | ✅ |
| 65 | ProgramLineId | PROGRAM_LINE_ID | — | ✅ |
| 66 | ProgramLineUomCode | PROGRAM_LINE_UOM_CODE | — | ✅ |
| 67 | ReceiptId | RECEIPT_ID | — | ✅ |
| 68 | ReceiptNumber | RECEIPT_NUMBER | — | ✅ |
| 69 | ReferenceId | REFERENCE_ID | — | ✅ |
| 70 | ReferenceType | REFERENCE_TYPE | — | ✅ |
| 71 | RequestId | REQUEST_ID | — | ✅ |
| 72 | RequestedGlDate | REQUESTED_GL_DATE | — | ✅ |
| 73 | SeededProgramTypeCode | SEEDED_PROGRAM_TYPE_CODE | — | ✅ |
| 74 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 75 | ShipmentDate | SHIPMENT_DATE | — | ✅ |
| 76 | ShipmentNumber | SHIPMENT_NUMBER | — | ✅ |
| 77 | SourceTrxAcctdAmount | SOURCE_TRX_ACCTD_AMOUNT | — | ✅ |
| 78 | SourceTrxAmountInPrgCurr | SOURCE_TRX_AMOUNT_IN_PRG_CURR | — | ✅ |
| 79 | SourceTrxAmountInTrxCurr | SOURCE_TRX_AMOUNT_IN_TRX_CURR | — | ✅ |
| 80 | TpItemId | TP_ITEM_ID | — | ✅ |
| 81 | TransactionCurrAmount | TRANSACTION_CURR_AMOUNT | — | ✅ |
| 82 | TransactionCurrAmountRem | TRANSACTION_CURR_AMOUNT_REM | — | ✅ |
| 83 | TransactionCurrencyCode | TRANSACTION_CURRENCY_CODE | — | ✅ |
| 84 | TransactionId | TRANSACTION_ID | — | ✅ |
| 85 | TransactionUnitPrice | TRANSACTION_UNIT_PRICE | — | ✅ |
| 86 | UtilizationId | UTILIZATION_ID | 🔑 | ✅ |
| 87 | UtilizationType | UTILIZATION_TYPE | — | ✅ |
| 88 | VendorId | VENDOR_ID | — | ✅ |
| 89 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 90 | WaybillNumber | WAYBILL_NUMBER | — | ✅ |
| 91 | YearId | YEAR_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
