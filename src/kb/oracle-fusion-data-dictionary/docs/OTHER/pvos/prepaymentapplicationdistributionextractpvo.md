---
id: DOC-OTHER-PVO-PrepaymentApplicationDistributionExtractPVO
doc_type: system-doc
title: "PrepaymentApplicationDistributionExtractPVO — PVO Cross-Module"
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
  - PrepaymentApplicationDistributionExtractPVO
  - prepaymentapplicationdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PrepaymentApplicationDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Prepayment Application Distribution Extract. Acessa as tabelas: AP_PREPAY_APP_DISTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ApBiccExtractAM.PrepaymentApplicationDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 1 | 1 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ap_prepay_app_dists|AP_PREPAY_APP_DISTS]] — 43 atributos (1 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[ap_prepay_app_dists|AP_PREPAY_APP_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApPrepayAppDistsAccountingEventId | ACCOUNTING_EVENT_ID | — | ✅ |
| 2 | ApPrepayAppDistsAmount | AMOUNT | — | ✅ |
| 3 | ApPrepayAppDistsAmountVariance | AMOUNT_VARIANCE | — | ✅ |
| 4 | ApPrepayAppDistsAwtRelatedId | AWT_RELATED_ID | — | ✅ |
| 5 | ApPrepayAppDistsBaseAmount | BASE_AMOUNT | — | ✅ |
| 6 | ApPrepayAppDistsBaseAmtAtPrepayClrXrate | BASE_AMT_AT_PREPAY_CLR_XRATE | — | ✅ |
| 7 | ApPrepayAppDistsBaseAmtAtPrepayPayXrate | BASE_AMT_AT_PREPAY_PAY_XRATE | — | ✅ |
| 8 | ApPrepayAppDistsBaseAmtAtPrepayXrate | BASE_AMT_AT_PREPAY_XRATE | — | ✅ |
| 9 | ApPrepayAppDistsBcEventId | BC_EVENT_ID | — | ✅ |
| 10 | ApPrepayAppDistsCreatedBy | CREATED_BY | — | ✅ |
| 11 | ApPrepayAppDistsCreationDate | CREATION_DATE | — | ✅ |
| 12 | ApPrepayAppDistsInvoiceBaseAmtVariance | INVOICE_BASE_AMT_VARIANCE | — | ✅ |
| 13 | ApPrepayAppDistsInvoiceBaseQtyVariance | INVOICE_BASE_QTY_VARIANCE | — | ✅ |
| 14 | ApPrepayAppDistsInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 15 | ApPrepayAppDistsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ApPrepayAppDistsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | ApPrepayAppDistsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ApPrepayAppDistsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | ApPrepayAppDistsPaAdditionFlag | PA_ADDITION_FLAG | — | ✅ |
| 20 | ApPrepayAppDistsPrepayAppDistId | PREPAY_APP_DIST_ID | 🔑 | ✅ |
| 21 | ApPrepayAppDistsPrepayAppDistributionId | PREPAY_APP_DISTRIBUTION_ID | — | ✅ |
| 22 | ApPrepayAppDistsPrepayClrExchangeDate | PREPAY_CLR_EXCHANGE_DATE | — | ✅ |
| 23 | ApPrepayAppDistsPrepayClrExchangeRate | PREPAY_CLR_EXCHANGE_RATE | — | ✅ |
| 24 | ApPrepayAppDistsPrepayClrExchangeRateType | PREPAY_CLR_EXCHANGE_RATE_TYPE | — | ✅ |
| 25 | ApPrepayAppDistsPrepayDistLookupCode | PREPAY_DIST_LOOKUP_CODE | — | ✅ |
| 26 | ApPrepayAppDistsPrepayExchangeDate | PREPAY_EXCHANGE_DATE | — | ✅ |
| 27 | ApPrepayAppDistsPrepayExchangeRate | PREPAY_EXCHANGE_RATE | — | ✅ |
| 28 | ApPrepayAppDistsPrepayExchangeRateType | PREPAY_EXCHANGE_RATE_TYPE | — | ✅ |
| 29 | ApPrepayAppDistsPrepayHistoryId | PREPAY_HISTORY_ID | — | ✅ |
| 30 | ApPrepayAppDistsPrepayPayExchangeDate | PREPAY_PAY_EXCHANGE_DATE | — | ✅ |
| 31 | ApPrepayAppDistsPrepayPayExchangeRate | PREPAY_PAY_EXCHANGE_RATE | — | ✅ |
| 32 | ApPrepayAppDistsPrepayPayExchangeRateType | PREPAY_PAY_EXCHANGE_RATE_TYPE | — | ✅ |
| 33 | ApPrepayAppDistsProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 34 | ApPrepayAppDistsProgramId | PROGRAM_ID | — | ✅ |
| 35 | ApPrepayAppDistsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 36 | ApPrepayAppDistsQuantityVariance | QUANTITY_VARIANCE | — | ✅ |
| 37 | ApPrepayAppDistsReleaseInvDistDerivedFrom | RELEASE_INV_DIST_DERIVED_FROM | — | ✅ |
| 38 | ApPrepayAppDistsRequestId | REQUEST_ID | — | ✅ |
| 39 | ApPrepayAppDistsReversedPrepayAppDistId | REVERSED_PREPAY_APP_DIST_ID | — | ✅ |
| 40 | ApPrepayAppDistsRoundAmtAtPrepayClrXrate | ROUND_AMT_AT_PREPAY_CLR_XRATE | — | ✅ |
| 41 | ApPrepayAppDistsRoundAmtAtPrepayPayXrate | ROUND_AMT_AT_PREPAY_PAY_XRATE | — | ✅ |
| 42 | ApPrepayAppDistsRoundAmtAtPrepayXrate | ROUND_AMT_AT_PREPAY_XRATE | — | ✅ |
| 43 | ApPrepayAppDistsRoundingAmt | ROUNDING_AMT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
