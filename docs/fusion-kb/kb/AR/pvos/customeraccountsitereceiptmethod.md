---
id: DOC-AR-PVO-CustomerAccountSiteReceiptMethod
doc_type: system-doc
title: "CustomerAccountSiteReceiptMethod — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CustomerAccountSiteReceiptMethod
  - customeraccountsitereceiptmethod
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerAccountSiteReceiptMethod

## 📌 Visão Geral

Extrai os métodos de recebimento configurados por site (filial/endereço) de conta de cliente. Permite diferenciar os meios de pagamento aceitos por localidade do cliente, suportando operações multi-site.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.CustomerAccountSiteReceiptMethod`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 3 | 1 | 13 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[ar_receipt_methods|AR_RECEIPT_METHODS]] — 27 atributos (2 BICC)
- [[iby_fndcpt_pmt_chnnls_vl|IBY_FNDCPT_PMT_CHNNLS_VL]] — 2 atributos (2 BICC)
- [[ra_cust_receipt_methods|RA_CUST_RECEIPT_METHODS]] — 17 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[ar_receipt_methods|AR_RECEIPT_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptMethodAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptMethodAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptMethodBrCustTrxTypeId | BR_CUST_TRX_TYPE_ID | — | — |
| 4 | ReceiptMethodBrInheritInvNumFlag | BR_INHERIT_INV_NUM_FLAG | — | — |
| 5 | ReceiptMethodBrMaxAcctdAmount | BR_MAX_ACCTD_AMOUNT | — | — |
| 6 | ReceiptMethodBrMinAcctdAmount | BR_MIN_ACCTD_AMOUNT | — | — |
| 7 | ReceiptMethodCreatedBy | CREATED_BY | — | — |
| 8 | ReceiptMethodCreationDate | CREATION_DATE | — | — |
| 9 | ReceiptMethodDmInheritReceiptNumFlag | DM_INHERIT_RECEIPT_NUM_FLAG | — | — |
| 10 | ReceiptMethodEndDate | END_DATE | — | — |
| 11 | ReceiptMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ReceiptMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ReceiptMethodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ReceiptMethodLeadDays | LEAD_DAYS | — | — |
| 15 | ReceiptMethodMaturityDateRuleCode | MATURITY_DATE_RULE_CODE | — | — |
| 16 | ReceiptMethodMerchantId | MERCHANT_ID | — | — |
| 17 | ReceiptMethodMerchantRef | MERCHANT_REF | — | — |
| 18 | ReceiptMethodName | NAME | — | ✅ |
| 19 | ReceiptMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ReceiptMethodPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 21 | ReceiptMethodPaymentTypeCode | PAYMENT_TYPE_CODE | — | — |
| 22 | ReceiptMethodPrintedName | PRINTED_NAME | — | — |
| 23 | ReceiptMethodReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 24 | ReceiptMethodReceiptCreationRuleCode | RECEIPT_CREATION_RULE_CODE | — | — |
| 25 | ReceiptMethodReceiptInheritInvNumFlag | RECEIPT_INHERIT_INV_NUM_FLAG | — | — |
| 26 | ReceiptMethodReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 27 | ReceiptMethodStartDate | START_DATE | — | — |

### [[iby_fndcpt_pmt_chnnls_vl|IBY_FNDCPT_PMT_CHNNLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FundsCapturePaymentMethodPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | ✅ |
| 2 | FundsCapturePaymentMethodPaymentChannelName | PAYMENT_CHANNEL_NAME | — | ✅ |

### [[ra_cust_receipt_methods|RA_CUST_RECEIPT_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustReceiptMethodCreatedBy | CREATED_BY | — | ✅ |
| 2 | CustReceiptMethodCreationDate | CREATION_DATE | — | ✅ |
| 3 | CustReceiptMethodCustomerId | CUSTOMER_ID | — | — |
| 4 | CustReceiptMethodEndDate | END_DATE | — | ✅ |
| 5 | CustReceiptMethodId | CUST_RECEIPT_METHOD_ID | 🔑 | ✅ |
| 6 | CustReceiptMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CustReceiptMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CustReceiptMethodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CustReceiptMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CustReceiptMethodPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 11 | CustReceiptMethodProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 12 | CustReceiptMethodProgramId | PROGRAM_ID | — | — |
| 13 | CustReceiptMethodProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 14 | CustReceiptMethodReceiptMethodId | RECEIPT_METHOD_ID | — | — |
| 15 | CustReceiptMethodRequestId | REQUEST_ID | — | — |
| 16 | CustReceiptMethodSiteUseId | SITE_USE_ID | — | — |
| 17 | CustReceiptMethodStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
