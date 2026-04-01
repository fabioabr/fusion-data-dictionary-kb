---
id: DOC-OTHER-PVO-ReportingDeferredDeprnExtractPVO
doc_type: system-doc
title: "ReportingDeferredDeprnExtractPVO — PVO Cross-Module"
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
  - ReportingDeferredDeprnExtractPVO
  - reportingdeferreddeprnextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingDeferredDeprnExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Deferred Deprn Extract. Acessa as tabelas: FA_MC_DEFERRED_DEPRN.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingDeferredDeprnExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 5 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_deferred_deprn|FA_MC_DEFERRED_DEPRN]] — 16 atributos (5 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[fa_mc_deferred_deprn|FA_MC_DEFERRED_DEPRN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingDeferredDeprnAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | ReportingDeferredDeprnCorpBookTypeCode | CORP_BOOK_TYPE_CODE | — | ✅ |
| 3 | ReportingDeferredDeprnCorpPeriodCounter | CORP_PERIOD_COUNTER | — | ✅ |
| 4 | ReportingDeferredDeprnCreatedBy | CREATED_BY | — | ✅ |
| 5 | ReportingDeferredDeprnCreationDate | CREATION_DATE | — | ✅ |
| 6 | ReportingDeferredDeprnDeferredDeprnExpenseAmount | DEFERRED_DEPRN_EXPENSE_AMOUNT | — | ✅ |
| 7 | ReportingDeferredDeprnDeferredDeprnReserveAmount | DEFERRED_DEPRN_RESERVE_AMOUNT | — | ✅ |
| 8 | ReportingDeferredDeprnDistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 9 | ReportingDeferredDeprnEventId | EVENT_ID | — | ✅ |
| 10 | ReportingDeferredDeprnLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ReportingDeferredDeprnLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | ReportingDeferredDeprnLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ReportingDeferredDeprnObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | ReportingDeferredDeprnSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 15 | ReportingDeferredDeprnTaxBookTypeCode | TAX_BOOK_TYPE_CODE | 🔑 | ✅ |
| 16 | ReportingDeferredDeprnTaxPeriodCounter | TAX_PERIOD_COUNTER | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
