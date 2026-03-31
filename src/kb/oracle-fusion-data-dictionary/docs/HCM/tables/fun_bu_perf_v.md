---
id: DOC-HCM-150
doc_type: system-doc
title: "FUN_BU_PERF_V — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FUN_BU_PERF_V
  - fun_bu_perf_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_BU_PERF_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_GROUP_ID | — | — | — | — | — | — |
| 2 | BU_ID | — | — | — | — | — | — |
| 3 | BU_NAME | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | DATE_FROM | — | — | — | — | — | — |
| 7 | DATE_TO | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[balanceactivitypvo|BalanceActivityPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBuId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[businessunitextractpvo|BusinessUnitExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | FunBuPerfPEOBusinessUnitId | ✅ |
| BU_NAME | FunBuPerfPEOName | ✅ |
| BUSINESS_GROUP_ID | FunBuPerfPEOEnterpriseId | ✅ |
| CREATED_BY | FunBuPerfPEOCreatedBy | ✅ |
| CREATION_DATE | FunBuPerfPEOCreationDate | ✅ |
| DATE_FROM | FunBuPerfPEODateFrom | ✅ |
| DATE_TO | FunBuPerfPEODateTo | ✅ |
| LAST_UPDATE_DATE | FunBuPerfPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FunBuPerfPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | FunBuPerfPEOLastUpdatedBy | ✅ |
| STATUS | FunBuPerfPEOStatus | ✅ |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[creditmemorequestpvo|CreditMemoRequestPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[disbursementhistoryheaderpvo|DisbursementHistoryHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[externaltransactionspvo|ExternalTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoicepaymentschedulepvo|InvoicePaymentSchedulePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[invoiceselfassessedtaxdistributionpvo|InvoiceSelfAssessedTaxDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[otbistatsbasesummarypvo|OtbiStatsBaseSummaryPVO]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |
| BU_NAME | BUName | — |
| BUSINESS_GROUP_ID | BUEnterpriseId | — |
| CREATED_BY | BUCreatedBy | — |
| CREATION_DATE | BUCreationDate | — |
| DATE_FROM | BUDateFrom | — |
| DATE_TO | BUDateTo | — |
| LAST_UPDATE_DATE | BULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BULastUpdateLogin | — |
| LAST_UPDATED_BY | BULastUpdatedBy | — |
| STATUS | BUStatus | — |

### [[otbistatssummarypvo|OtbiStatsSummaryPVO]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |
| BU_NAME | BUName | — |
| BUSINESS_GROUP_ID | BUEnterpriseId | — |
| CREATED_BY | BUCreatedBy1 | — |
| CREATION_DATE | BUCreationDate1 | — |
| DATE_FROM | BUDateFrom | — |
| DATE_TO | BUDateTo | — |
| LAST_UPDATE_DATE | BULastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | BULastUpdateLogin1 | — |
| LAST_UPDATED_BY | BULastUpdatedBy1 | — |
| STATUS | BUStatus | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | InvoicingBuBusinessUnitId | — |
| BU_NAME | InvoicingBuName | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_ID | InvoicingBuBusinessUnitId | — |
| BU_NAME | InvoicingBuName | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[rateadjustmentpvo|RateAdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_ID | TrxHdrRcptAppliedBusinessUnitId | — |
| BU_NAME | TrxHdrRcptAppliedBusinessUnitName | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_ID | TrxHdrRcptAppliedBusinessUnitId | — |
| BU_NAME | TrxHdrRcptAppliedBusinessUnitName | ✅ |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_ID | TrxHeaderBusinessUnitId | — |
| BU_NAME | TrxHeaderBusinessUnitName | ✅ |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[referenceaccount|ReferenceAccount]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |
| STATUS | BusinessUnitStatus | — |

### [[revenueadjustmentdistributionpvo|RevenueAdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[revenueadjustmentpvo|RevenueAdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |

### [[salesinvoicecustomertrxlinesalescreditpvo|SalesInvoiceCustomerTrxLineSalesCreditPVO]] (AR · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[trialbalancepvo|TrialBalancePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |

### [[withholdingbucketpvo|WithholdingBucketPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
