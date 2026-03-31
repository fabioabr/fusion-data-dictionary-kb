---
id: DOC-OTHER-PVO-DeferredDepreciationExtractPVO
doc_type: system-doc
title: "DeferredDepreciationExtractPVO — PVO Cross-Module"
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
  - DeferredDepreciationExtractPVO
  - deferreddepreciationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeferredDepreciationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Deferred Depreciation Extract. Acessa as tabelas: FA_DEFERRED_DEPRN.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.DeferredDepreciationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 4 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_deferred_deprn|FA_DEFERRED_DEPRN]] — 15 atributos (4 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[fa_deferred_deprn|FA_DEFERRED_DEPRN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeferredDepreciationAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | DeferredDepreciationCorpBookTypeCode | CORP_BOOK_TYPE_CODE | — | ✅ |
| 3 | DeferredDepreciationCorpPeriodCounter | CORP_PERIOD_COUNTER | — | ✅ |
| 4 | DeferredDepreciationCreatedBy | CREATED_BY | — | ✅ |
| 5 | DeferredDepreciationCreationDate | CREATION_DATE | — | ✅ |
| 6 | DeferredDepreciationDeferredDeprnExpenseAmount | DEFERRED_DEPRN_EXPENSE_AMOUNT | — | ✅ |
| 7 | DeferredDepreciationDeferredDeprnReserveAmount | DEFERRED_DEPRN_RESERVE_AMOUNT | — | ✅ |
| 8 | DeferredDepreciationDistributionId | DISTRIBUTION_ID | 🔑 | ✅ |
| 9 | DeferredDepreciationEventId | EVENT_ID | — | ✅ |
| 10 | DeferredDepreciationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DeferredDepreciationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | DeferredDepreciationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | DeferredDepreciationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | DeferredDepreciationTaxBookTypeCode | TAX_BOOK_TYPE_CODE | 🔑 | ✅ |
| 15 | DeferredDepreciationTaxPeriodCounter | TAX_PERIOD_COUNTER | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
