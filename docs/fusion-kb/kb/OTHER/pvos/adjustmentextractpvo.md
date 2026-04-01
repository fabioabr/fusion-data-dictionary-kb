---
id: DOC-OTHER-PVO-AdjustmentExtractPVO
doc_type: system-doc
title: "AdjustmentExtractPVO — PVO Cross-Module"
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
  - AdjustmentExtractPVO
  - adjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Adjustment Extract. Acessa as tabelas: FA_ADJUSTMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 2 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_adjustments|FA_ADJUSTMENTS]] — 24 atributos (2 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[fa_adjustments|FA_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | AdjustmentAdjustmentLineId | ADJUSTMENT_LINE_ID | 🔑 | ✅ |
| 3 | AdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 4 | AdjustmentAnnualizedAdjustment | ANNUALIZED_ADJUSTMENT | — | ✅ |
| 5 | AdjustmentAssetId | ASSET_ID | — | ✅ |
| 6 | AdjustmentAssetInvoiceId | ASSET_INVOICE_ID | — | ✅ |
| 7 | AdjustmentBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 8 | AdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 9 | AdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 10 | AdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 11 | AdjustmentDebitCreditFlag | DEBIT_CREDIT_FLAG | — | ✅ |
| 12 | AdjustmentDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 13 | AdjustmentDistributionId | DISTRIBUTION_ID | — | ✅ |
| 14 | AdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | AdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | AdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | AdjustmentPeriodCounterAdjusted | PERIOD_COUNTER_ADJUSTED | — | ✅ |
| 19 | AdjustmentPeriodCounterCreated | PERIOD_COUNTER_CREATED | — | ✅ |
| 20 | AdjustmentSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 21 | AdjustmentSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 22 | AdjustmentSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 23 | AdjustmentTrackMemberFlag | TRACK_MEMBER_FLAG | — | ✅ |
| 24 | AdjustmentTransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
