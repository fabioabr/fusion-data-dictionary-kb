---
id: DOC-OTHER-PVO-InvoiceHeaderExtractPVO
doc_type: system-doc
title: "InvoiceHeaderExtractPVO — PVO Cross-Module"
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
  - InvoiceHeaderExtractPVO
  - invoiceheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Header Extract. Acessa as tabelas: PJB_INVOICE_HEADERS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.InvoiceHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 1 | 1 | 64 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_invoice_headers|PJB_INVOICE_HEADERS]] — 80 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[pjb_invoice_headers|PJB_INVOICE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceHeaderPEOAcctdCurrencyCode | ACCTD_CURRENCY_CODE | — | ✅ |
| 2 | InvoiceHeaderPEOAcctdExchgRate | ACCTD_EXCHG_RATE | — | ✅ |
| 3 | InvoiceHeaderPEOAcctdRateDate | ACCTD_RATE_DATE | — | ✅ |
| 4 | InvoiceHeaderPEOAcctdRateType | ACCTD_RATE_TYPE | — | ✅ |
| 5 | InvoiceHeaderPEOApprovedByPersonId | APPROVED_BY_PERSON_ID | — | ✅ |
| 6 | InvoiceHeaderPEOApprovedDate | APPROVED_DATE | — | ✅ |
| 7 | InvoiceHeaderPEOAttribute1 | ATTRIBUTE1 | — | — |
| 8 | InvoiceHeaderPEOAttribute10 | ATTRIBUTE10 | — | — |
| 9 | InvoiceHeaderPEOAttribute11 | ATTRIBUTE11 | — | — |
| 10 | InvoiceHeaderPEOAttribute12 | ATTRIBUTE12 | — | — |
| 11 | InvoiceHeaderPEOAttribute13 | ATTRIBUTE13 | — | — |
| 12 | InvoiceHeaderPEOAttribute14 | ATTRIBUTE14 | — | — |
| 13 | InvoiceHeaderPEOAttribute15 | ATTRIBUTE15 | — | — |
| 14 | InvoiceHeaderPEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | InvoiceHeaderPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | InvoiceHeaderPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | InvoiceHeaderPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | InvoiceHeaderPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | InvoiceHeaderPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | InvoiceHeaderPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | InvoiceHeaderPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | InvoiceHeaderPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | InvoiceHeaderPEOBillFromDate | BILL_FROM_DATE | — | ✅ |
| 24 | InvoiceHeaderPEOBillSetNum | BILL_SET_NUM | — | ✅ |
| 25 | InvoiceHeaderPEOBillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 26 | InvoiceHeaderPEOBillToCustAcctId | BILL_TO_CUST_ACCT_ID | — | ✅ |
| 27 | InvoiceHeaderPEOBillToDate | BILL_TO_DATE | — | ✅ |
| 28 | InvoiceHeaderPEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 29 | InvoiceHeaderPEOBillingTypeCode | BILLING_TYPE_CODE | — | ✅ |
| 30 | InvoiceHeaderPEOCancelledFlag | CANCELLED_FLAG | — | ✅ |
| 31 | InvoiceHeaderPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 32 | InvoiceHeaderPEOContractId | CONTRACT_ID | — | ✅ |
| 33 | InvoiceHeaderPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 34 | InvoiceHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 35 | InvoiceHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 36 | InvoiceHeaderPEOCreditMemoReasonCode | CREDIT_MEMO_REASON_CODE | — | ✅ |
| 37 | InvoiceHeaderPEOCreditedInvoiceId | CREDITED_INVOICE_ID | — | ✅ |
| 38 | InvoiceHeaderPEODocNumber | DOC_NUMBER | — | ✅ |
| 39 | InvoiceHeaderPEODocumentSubType | DOCUMENT_SUB_TYPE | — | ✅ |
| 40 | InvoiceHeaderPEOExceptionFlag | EXCEPTION_FLAG | — | ✅ |
| 41 | InvoiceHeaderPEOExportProcessId | EXPORT_PROCESS_ID | — | ✅ |
| 42 | InvoiceHeaderPEOGenerationErrorFlag | GENERATION_ERROR_FLAG | — | ✅ |
| 43 | InvoiceHeaderPEOGlDate | GL_DATE | — | ✅ |
| 44 | InvoiceHeaderPEOGlPeriodName | GL_PERIOD_NAME | — | ✅ |
| 45 | InvoiceHeaderPEOInApTransferErrorCode | IN_AP_TRANSFER_ERROR_CODE | — | ✅ |
| 46 | InvoiceHeaderPEOInApTransferStatusCode | IN_AP_TRANSFER_STATUS_CODE | — | ✅ |
| 47 | InvoiceHeaderPEOInvoiceComment | INVOICE_COMMENT | — | ✅ |
| 48 | InvoiceHeaderPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 49 | InvoiceHeaderPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 50 | InvoiceHeaderPEOInvoiceId | INVOICE_ID | 🔑 | ✅ |
| 51 | InvoiceHeaderPEOInvoiceInstructions | INVOICE_INSTRUCTIONS | — | ✅ |
| 52 | InvoiceHeaderPEOInvoiceNum | INVOICE_NUM | — | ✅ |
| 53 | InvoiceHeaderPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 54 | InvoiceHeaderPEOInvoiceTypeCode | INVOICE_TYPE_CODE | — | ✅ |
| 55 | InvoiceHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 56 | InvoiceHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 57 | InvoiceHeaderPEOLang | LANG | — | ✅ |
| 58 | InvoiceHeaderPEOLastCreditRequestId | LAST_CREDIT_REQUEST_ID | — | ✅ |
| 59 | InvoiceHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | InvoiceHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | InvoiceHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | InvoiceHeaderPEOLocNumber | LOC_NUMBER | — | ✅ |
| 63 | InvoiceHeaderPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 64 | InvoiceHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 65 | InvoiceHeaderPEOOrgId | ORG_ID | — | ✅ |
| 66 | InvoiceHeaderPEOPaDate | PA_DATE | — | ✅ |
| 67 | InvoiceHeaderPEOPaPeriodName | PA_PERIOD_NAME | — | ✅ |
| 68 | InvoiceHeaderPEOPjsSummaryId | PJS_SUMMARY_ID | — | ✅ |
| 69 | InvoiceHeaderPEOPurgeFlag | PURGE_FLAG | — | ✅ |
| 70 | InvoiceHeaderPEORaInvoiceNumber | RA_INVOICE_NUMBER | — | ✅ |
| 71 | InvoiceHeaderPEORcvrSetupCode | RCVR_SETUP_CODE | — | ✅ |
| 72 | InvoiceHeaderPEOReleasedByPersonId | RELEASED_BY_PERSON_ID | — | ✅ |
| 73 | InvoiceHeaderPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 74 | InvoiceHeaderPEOReportTypeCode | REPORT_TYPE_CODE | — | ✅ |
| 75 | InvoiceHeaderPEORequestId | REQUEST_ID | — | ✅ |
| 76 | InvoiceHeaderPEOSystemReference | SYSTEM_REFERENCE | — | ✅ |
| 77 | InvoiceHeaderPEOTaxationCountry | TAXATION_COUNTRY | — | ✅ |
| 78 | InvoiceHeaderPEOTransferRejectReasonCode | TRANSFER_REJECT_REASON_CODE | — | ✅ |
| 79 | InvoiceHeaderPEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 80 | InvoiceHeaderPEOTransferredDate | TRANSFERRED_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
