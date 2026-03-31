---
id: DOC-OTHER-PVO-InvoiceLineExtractPVO
doc_type: system-doc
title: "InvoiceLineExtractPVO — PVO Cross-Module"
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
  - InvoiceLineExtractPVO
  - invoicelineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Line Extract. Acessa as tabelas: PJB_INVOICE_LINES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.InvoiceLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 1 | 1 | 69 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_invoice_lines|PJB_INVOICE_LINES]] — 85 atributos (1 PKs, 69 BICC)

---

## ⚙️ Atributos

### [[pjb_invoice_lines|PJB_INVOICE_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceLinePEOAcctdCurrencyAmt | ACCTD_CURRENCY_AMT | — | ✅ |
| 2 | InvoiceLinePEOAcctdCurrencyCode | ACCTD_CURRENCY_CODE | — | ✅ |
| 3 | InvoiceLinePEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 4 | InvoiceLinePEOAttribute1 | ATTRIBUTE1 | — | — |
| 5 | InvoiceLinePEOAttribute10 | ATTRIBUTE10 | — | — |
| 6 | InvoiceLinePEOAttribute11 | ATTRIBUTE11 | — | — |
| 7 | InvoiceLinePEOAttribute12 | ATTRIBUTE12 | — | — |
| 8 | InvoiceLinePEOAttribute13 | ATTRIBUTE13 | — | — |
| 9 | InvoiceLinePEOAttribute14 | ATTRIBUTE14 | — | — |
| 10 | InvoiceLinePEOAttribute15 | ATTRIBUTE15 | — | — |
| 11 | InvoiceLinePEOAttribute2 | ATTRIBUTE2 | — | — |
| 12 | InvoiceLinePEOAttribute3 | ATTRIBUTE3 | — | — |
| 13 | InvoiceLinePEOAttribute4 | ATTRIBUTE4 | — | — |
| 14 | InvoiceLinePEOAttribute5 | ATTRIBUTE5 | — | — |
| 15 | InvoiceLinePEOAttribute6 | ATTRIBUTE6 | — | — |
| 16 | InvoiceLinePEOAttribute7 | ATTRIBUTE7 | — | — |
| 17 | InvoiceLinePEOAttribute8 | ATTRIBUTE8 | — | — |
| 18 | InvoiceLinePEOAttribute9 | ATTRIBUTE9 | — | — |
| 19 | InvoiceLinePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | InvoiceLinePEOBillPlanId | BILL_PLAN_ID | — | ✅ |
| 21 | InvoiceLinePEOBillSetNum | BILL_SET_NUM | — | ✅ |
| 22 | InvoiceLinePEOContractCurrCreditAmt | CONTRACT_CURR_CREDIT_AMT | — | ✅ |
| 23 | InvoiceLinePEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 24 | InvoiceLinePEOContractCurrencyInvAmt | CONTRACT_CURRENCY_INV_AMT | — | ✅ |
| 25 | InvoiceLinePEOContractId | CONTRACT_ID | — | ✅ |
| 26 | InvoiceLinePEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 27 | InvoiceLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 28 | InvoiceLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 29 | InvoiceLinePEOCreditProcessedFlag | CREDIT_PROCESSED_FLAG | — | ✅ |
| 30 | InvoiceLinePEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | ✅ |
| 31 | InvoiceLinePEOCreditedInvoiceLineId | CREDITED_INVOICE_LINE_ID | — | ✅ |
| 32 | InvoiceLinePEODocNumber | DOC_NUMBER | — | ✅ |
| 33 | InvoiceLinePEOExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 34 | InvoiceLinePEOExpenditureOrgId | EXPENDITURE_ORG_ID | — | ✅ |
| 35 | InvoiceLinePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 36 | InvoiceLinePEOInApTransferErrorCode | IN_AP_TRANSFER_ERROR_CODE | — | ✅ |
| 37 | InvoiceLinePEOInApTransferStatusCode | IN_AP_TRANSFER_STATUS_CODE | — | ✅ |
| 38 | InvoiceLinePEOIntendedUse | INTENDED_USE | — | ✅ |
| 39 | InvoiceLinePEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 40 | InvoiceLinePEOInvBilledQuantity | INV_BILLED_QUANTITY | — | ✅ |
| 41 | InvoiceLinePEOInvCurrLineAmt | INV_CURR_LINE_AMT | — | ✅ |
| 42 | InvoiceLinePEOInvCurrUnitPrice | INV_CURR_UNIT_PRICE | — | ✅ |
| 43 | InvoiceLinePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 44 | InvoiceLinePEOInvoiceCurrCreditAmt | INVOICE_CURR_CREDIT_AMT | — | ✅ |
| 45 | InvoiceLinePEOInvoiceCurrCreditPct | INVOICE_CURR_CREDIT_PCT | — | ✅ |
| 46 | InvoiceLinePEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 47 | InvoiceLinePEOInvoiceFormatId | INVOICE_FORMAT_ID | — | ✅ |
| 48 | InvoiceLinePEOInvoiceId | INVOICE_ID | — | ✅ |
| 49 | InvoiceLinePEOInvoiceLineDesc | INVOICE_LINE_DESC | — | ✅ |
| 50 | InvoiceLinePEOInvoiceLineId | INVOICE_LINE_ID | 🔑 | ✅ |
| 51 | InvoiceLinePEOInvoiceLineNum | INVOICE_LINE_NUM | — | ✅ |
| 52 | InvoiceLinePEOInvoiceLineType | INVOICE_LINE_TYPE | — | ✅ |
| 53 | InvoiceLinePEOInvoiceNum | INVOICE_NUM | — | ✅ |
| 54 | InvoiceLinePEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 55 | InvoiceLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 56 | InvoiceLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 57 | InvoiceLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 58 | InvoiceLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 59 | InvoiceLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 60 | InvoiceLinePEOLocNumber | LOC_NUMBER | — | ✅ |
| 61 | InvoiceLinePEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 62 | InvoiceLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 63 | InvoiceLinePEOOutputTaxAmt | OUTPUT_TAX_AMT | — | ✅ |
| 64 | InvoiceLinePEOOutputTaxClassCode | OUTPUT_TAX_CLASS_CODE | — | ✅ |
| 65 | InvoiceLinePEOOutputTaxExemptFlag | OUTPUT_TAX_EXEMPT_FLAG | — | ✅ |
| 66 | InvoiceLinePEOOutputTaxExmtCertNumber | OUTPUT_TAX_EXMT_CERT_NUMBER | — | ✅ |
| 67 | InvoiceLinePEOOutputTaxExmtReasonCode | OUTPUT_TAX_EXMT_REASON_CODE | — | ✅ |
| 68 | InvoiceLinePEOPaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 69 | InvoiceLinePEOProdFcCategId | PROD_FC_CATEG_ID | — | ✅ |
| 70 | InvoiceLinePEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 71 | InvoiceLinePEOProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 72 | InvoiceLinePEOProductType | PRODUCT_TYPE | — | ✅ |
| 73 | InvoiceLinePEORateSourceCode | RATE_SOURCE_CODE | — | ✅ |
| 74 | InvoiceLinePEORecalcExtnFlag | RECALC_EXTN_FLAG | — | ✅ |
| 75 | InvoiceLinePEOReceiverProjectId | RECEIVER_PROJECT_ID | — | ✅ |
| 76 | InvoiceLinePEOReceiverTaskId | RECEIVER_TASK_ID | — | ✅ |
| 77 | InvoiceLinePEORequestId | REQUEST_ID | — | ✅ |
| 78 | InvoiceLinePEOShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 79 | InvoiceLinePEOShipToCustAcctId | SHIP_TO_CUST_ACCT_ID | — | ✅ |
| 80 | InvoiceLinePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 81 | InvoiceLinePEOTranslatedText | TRANSLATED_TEXT | — | ✅ |
| 82 | InvoiceLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 83 | InvoiceLinePEOUomCode | UOM_CODE | — | ✅ |
| 84 | InvoiceLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 85 | InvoiceLinePEOWriteOffFlag | WRITE_OFF_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
