---
id: DOC-AR-PVO-ReceiptMethodPVO
doc_type: system-doc
title: "ReceiptMethodPVO — PVO Accounts Receivable"
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
  - ReceiptMethodPVO
  - receiptmethodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceiptMethodPVO

## 📌 Visão Geral

Extrai os métodos de recebimento configurados no sistema (boleto, TED, cartão, cheque, débito automático), com classes e canais de pagamento. Define os meios de cobrança disponíveis e suas regras de processamento.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReceiptMethodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 3 | 1 | 16 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[ar_receipt_classes|AR_RECEIPT_CLASSES]] — 16 atributos (5 BICC)
- [[ar_receipt_methods|AR_RECEIPT_METHODS]] — 27 atributos (1 PKs, 9 BICC)
- [[iby_fndcpt_pmt_chnnls_vl|IBY_FNDCPT_PMT_CHNNLS_VL]] — 9 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ar_receipt_classes|AR_RECEIPT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptClassBillOfExchangeFlag | BILL_OF_EXCHANGE_FLAG | — | — |
| 2 | ReceiptClassClearFlag | CLEAR_FLAG | — | — |
| 3 | ReceiptClassConfirmFlag | CONFIRM_FLAG | — | — |
| 4 | ReceiptClassCreatedBy | CREATED_BY | — | — |
| 5 | ReceiptClassCreationDate | CREATION_DATE | — | — |
| 6 | ReceiptClassCreationMethodCode | CREATION_METHOD_CODE | — | ✅ |
| 7 | ReceiptClassCreationStatus | CREATION_STATUS | — | ✅ |
| 8 | ReceiptClassLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ReceiptClassLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ReceiptClassLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ReceiptClassName | NAME | — | ✅ |
| 12 | ReceiptClassNotesReceivable | NOTES_RECEIVABLE | — | — |
| 13 | ReceiptClassObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ReceiptClassReceiptClassId | RECEIPT_CLASS_ID | — | ✅ |
| 15 | ReceiptClassRemitFlag | REMIT_FLAG | — | — |
| 16 | ReceiptClassRemitMethodCode | REMIT_METHOD_CODE | — | — |

### [[ar_receipt_methods|AR_RECEIPT_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReceiptMethodAutoPrintProgramId | AUTO_PRINT_PROGRAM_ID | — | — |
| 2 | ReceiptMethodAutoTransProgramId | AUTO_TRANS_PROGRAM_ID | — | — |
| 3 | ReceiptMethodBrCustTrxTypeId | BR_CUST_TRX_TYPE_ID | — | — |
| 4 | ReceiptMethodBrInheritInvNumFlag | BR_INHERIT_INV_NUM_FLAG | — | — |
| 5 | ReceiptMethodBrMaxAcctdAmount | BR_MAX_ACCTD_AMOUNT | — | — |
| 6 | ReceiptMethodBrMinAcctdAmount | BR_MIN_ACCTD_AMOUNT | — | — |
| 7 | ReceiptMethodCreatedBy | CREATED_BY | — | ✅ |
| 8 | ReceiptMethodCreationDate | CREATION_DATE | — | ✅ |
| 9 | ReceiptMethodDmInheritReceiptNumFlag | DM_INHERIT_RECEIPT_NUM_FLAG | — | — |
| 10 | ReceiptMethodEndDate | END_DATE | — | ✅ |
| 11 | ReceiptMethodId | RECEIPT_METHOD_ID | 🔑 | ✅ |
| 12 | ReceiptMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ReceiptMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ReceiptMethodLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ReceiptMethodLeadDays | LEAD_DAYS | — | — |
| 16 | ReceiptMethodMaturityDateRuleCode | MATURITY_DATE_RULE_CODE | — | — |
| 17 | ReceiptMethodMerchantId | MERCHANT_ID | — | — |
| 18 | ReceiptMethodMerchantRef | MERCHANT_REF | — | — |
| 19 | ReceiptMethodName | NAME | — | ✅ |
| 20 | ReceiptMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ReceiptMethodPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | — |
| 22 | ReceiptMethodPaymentTypeCode | PAYMENT_TYPE_CODE | — | ✅ |
| 23 | ReceiptMethodPrintedName | PRINTED_NAME | — | ✅ |
| 24 | ReceiptMethodReceiptClassId | RECEIPT_CLASS_ID | — | — |
| 25 | ReceiptMethodReceiptCreationRuleCode | RECEIPT_CREATION_RULE_CODE | — | — |
| 26 | ReceiptMethodReceiptInheritInvNumFlag | RECEIPT_INHERIT_INV_NUM_FLAG | — | — |
| 27 | ReceiptMethodStartDate | START_DATE | — | — |

### [[iby_fndcpt_pmt_chnnls_vl|IBY_FNDCPT_PMT_CHNNLS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IbyFndcptPmtChnnlsDescription | DESCRIPTION | — | — |
| 2 | IbyFndcptPmtChnnlsEndDate | END_DATE | — | — |
| 3 | IbyFndcptPmtChnnlsFormatValue | FORMAT_VALUE | — | — |
| 4 | IbyFndcptPmtChnnlsInactiveDate | INACTIVE_DATE | — | — |
| 5 | IbyFndcptPmtChnnlsInstrumentType | INSTRUMENT_TYPE | — | — |
| 6 | IbyFndcptPmtChnnlsPaymentChannelCode | PAYMENT_CHANNEL_CODE | — | ✅ |
| 7 | IbyFndcptPmtChnnlsPaymentChannelName | PAYMENT_CHANNEL_NAME | — | ✅ |
| 8 | IbyFndcptPmtChnnlsSeededFlag | SEEDED_FLAG | — | — |
| 9 | IbyFndcptPmtChnnlsStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
