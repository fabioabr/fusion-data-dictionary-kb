---
id: DOC-OTHER-PVO-ReportingAdjustmentExtractPVO
doc_type: system-doc
title: "ReportingAdjustmentExtractPVO — PVO Cross-Module"
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
  - ReportingAdjustmentExtractPVO
  - reportingadjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingAdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Adjustment Extract. Acessa as tabelas: fa_mc_adjustments.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingAdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 3 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_adjustments|fa_mc_adjustments]] — 26 atributos (3 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[fa_mc_adjustments|fa_mc_adjustments]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingAdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | ReportingAdjustmentAdjustmentLineId | ADJUSTMENT_LINE_ID | 🔑 | ✅ |
| 3 | ReportingAdjustmentAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 4 | ReportingAdjustmentAnnualizedAdjustment | ANNUALIZED_ADJUSTMENT | — | ✅ |
| 5 | ReportingAdjustmentAssetId | ASSET_ID | — | ✅ |
| 6 | ReportingAdjustmentAssetInvoiceId | ASSET_INVOICE_ID | — | ✅ |
| 7 | ReportingAdjustmentBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 8 | ReportingAdjustmentCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 9 | ReportingAdjustmentConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 10 | ReportingAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 11 | ReportingAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 12 | ReportingAdjustmentDebitCreditFlag | DEBIT_CREDIT_FLAG | — | ✅ |
| 13 | ReportingAdjustmentDeprnOverrideFlag | DEPRN_OVERRIDE_FLAG | — | ✅ |
| 14 | ReportingAdjustmentDistributionId | DISTRIBUTION_ID | — | ✅ |
| 15 | ReportingAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ReportingAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | ReportingAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ReportingAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | ReportingAdjustmentPeriodCounterAdjusted | PERIOD_COUNTER_ADJUSTED | — | ✅ |
| 20 | ReportingAdjustmentPeriodCounterCreated | PERIOD_COUNTER_CREATED | — | ✅ |
| 21 | ReportingAdjustmentSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 22 | ReportingAdjustmentSourceDestCode | SOURCE_DEST_CODE | — | ✅ |
| 23 | ReportingAdjustmentSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 24 | ReportingAdjustmentSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 25 | ReportingAdjustmentTrackMemberFlag | TRACK_MEMBER_FLAG | — | ✅ |
| 26 | ReportingAdjustmentTransactionHeaderId | TRANSACTION_HEADER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
