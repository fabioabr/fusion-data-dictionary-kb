---
id: DOC-OTHER-PVO-FaAssetHistoryPVO
doc_type: system-doc
title: "FaAssetHistoryPVO — PVO Cross-Module"
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
  - FaAssetHistoryPVO
  - faassethistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FaAssetHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fa Asset History. Acessa as tabelas: FA_ASSET_HISTORY, FA_BOOKS, FA_BOOK_CONTROLS.

**Caminho:** `FscmTopModelAM.FinFaSharedUtilAM.FaAssetHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 3 | 2 | 4 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[fa_asset_history|FA_ASSET_HISTORY]] — 14 atributos (2 PKs, 4 BICC)
- [[fa_books|FA_BOOKS]] — 3 atributos
- [[fa_book_controls|FA_BOOK_CONTROLS]] — 3 atributos

---

## ⚙️ Atributos

### [[fa_asset_history|FA_ASSET_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetHistoryAssetType | ASSET_TYPE | — | — |
| 2 | AssetHistoryCategoryId | CATEGORY_ID | — | — |
| 3 | AssetHistoryCreatedBy | CREATED_BY | — | — |
| 4 | AssetHistoryCreationDate | CREATION_DATE | — | — |
| 5 | AssetHistoryDateEffective | DATE_EFFECTIVE | — | — |
| 6 | AssetHistoryDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 7 | AssetHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AssetHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AssetHistoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AssetHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AssetHistoryTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | — |
| 12 | AssetHistoryUnits | UNITS | — | — |
| 13 | AssetId | ASSET_ID | 🔑 | ✅ |
| 14 | TransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |

### [[fa_books|FA_BOOKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookAssetId | ASSET_ID | — | — |
| 2 | BookBookTypeCode | BOOK_TYPE_CODE | — | — |
| 3 | BookTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | — |

### [[fa_book_controls|FA_BOOK_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BookControlBookClass | BOOK_CLASS | — | — |
| 2 | BookControlBookTypeCode1 | BOOK_TYPE_CODE | — | — |
| 3 | BookControlBookTypeName | BOOK_TYPE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
