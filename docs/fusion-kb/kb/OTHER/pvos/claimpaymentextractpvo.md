---
id: DOC-OTHER-PVO-ClaimPaymentExtractPVO
doc_type: system-doc
title: "ClaimPaymentExtractPVO — PVO Cross-Module"
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
  - ClaimPaymentExtractPVO
  - claimpaymentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClaimPaymentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Claim Payment Extract. Acessa as tabelas: CJM_CLAIM_PAYMENTS_ALL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ClaimPaymentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_claim_payments_all|CJM_CLAIM_PAYMENTS_ALL]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[cjm_claim_payments_all|CJM_CLAIM_PAYMENTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuId | BU_ID | — | ✅ |
| 2 | ClaimId | CLAIM_ID | — | ✅ |
| 3 | ClaimPaymentId | CLAIM_PAYMENT_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PaymentAmount | PAYMENT_AMOUNT | — | ✅ |
| 11 | PaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 12 | PaymentEffectiveDate | PAYMENT_EFFECTIVE_DATE | — | ✅ |
| 13 | PaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 14 | PaymentReferenceDate | PAYMENT_REFERENCE_DATE | — | ✅ |
| 15 | PaymentReferenceId | PAYMENT_REFERENCE_ID | — | ✅ |
| 16 | PaymentReferenceNumber | PAYMENT_REFERENCE_NUMBER | — | ✅ |
| 17 | PaymentStatusCode | PAYMENT_STATUS_CODE | — | ✅ |
| 18 | RaCustTrxTypeSeqId | RA_CUST_TRX_TYPE_SEQ_ID | — | ✅ |
| 19 | ReceivablesReasonCode | RECEIVABLES_REASON_CODE | — | ✅ |
| 20 | WoReceivablesTrxId | WO_RECEIVABLES_TRX_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
