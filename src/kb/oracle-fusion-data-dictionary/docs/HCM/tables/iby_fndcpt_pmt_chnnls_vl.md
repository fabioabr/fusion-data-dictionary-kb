---
id: DOC-HCM-515
doc_type: system-doc
title: "IBY_FNDCPT_PMT_CHNNLS_VL — (título a preencher)"
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
  - IBY_FNDCPT_PMT_CHNNLS_VL
  - iby_fndcpt_pmt_chnnls_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_FNDCPT_PMT_CHNNLS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESCRIPTION | — | — | — | — | — | — |
| 2 | END_DATE | — | — | — | — | — | — |
| 3 | FORMAT_VALUE | — | — | — | — | — | — |
| 4 | INACTIVE_DATE | — | — | — | — | — | — |
| 5 | INSTRUMENT_TYPE | — | — | — | — | — | — |
| 6 | PAYMENT_CHANNEL_CODE | — | — | — | — | — | — |
| 7 | PAYMENT_CHANNEL_NAME | — | — | — | — | — | — |
| 8 | SEEDED_FLAG | — | — | — | — | — | — |
| 9 | START_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[customeraccountreceiptmethod|CustomerAccountReceiptMethod]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PAYMENT_CHANNEL_CODE | FundsCapturePaymentMethodPaymentChannelCode | — |
| PAYMENT_CHANNEL_NAME | FundsCapturePaymentMethodPaymentChannelName | — |

### [[customeraccountsitereceiptmethod|CustomerAccountSiteReceiptMethod]] (AR · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PAYMENT_CHANNEL_CODE | FundsCapturePaymentMethodPaymentChannelCode | ✅ |
| PAYMENT_CHANNEL_NAME | FundsCapturePaymentMethodPaymentChannelName | ✅ |

### [[receiptmethodpvo|ReceiptMethodPVO]] (AR · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | IbyFndcptPmtChnnlsDescription | — |
| END_DATE | IbyFndcptPmtChnnlsEndDate | — |
| FORMAT_VALUE | IbyFndcptPmtChnnlsFormatValue | — |
| INACTIVE_DATE | IbyFndcptPmtChnnlsInactiveDate | — |
| INSTRUMENT_TYPE | IbyFndcptPmtChnnlsInstrumentType | — |
| PAYMENT_CHANNEL_CODE | IbyFndcptPmtChnnlsPaymentChannelCode | ✅ |
| PAYMENT_CHANNEL_NAME | IbyFndcptPmtChnnlsPaymentChannelName | ✅ |
| SEEDED_FLAG | IbyFndcptPmtChnnlsSeededFlag | — |
| START_DATE | IbyFndcptPmtChnnlsStartDate | — |
