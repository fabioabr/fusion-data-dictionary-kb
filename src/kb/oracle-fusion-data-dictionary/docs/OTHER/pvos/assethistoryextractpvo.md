---
id: DOC-OTHER-PVO-AssetHistoryExtractPVO
doc_type: system-doc
title: "AssetHistoryExtractPVO — PVO Cross-Module"
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
  - AssetHistoryExtractPVO
  - assethistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetHistoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset History Extract. Acessa as tabelas: FA_ASSET_HISTORY.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AssetHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 1 | 2 | 17 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[fa_asset_history|FA_ASSET_HISTORY]] — 58 atributos (2 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[fa_asset_history|FA_ASSET_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetHistoryAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | AssetHistoryAssetType | ASSET_TYPE | — | ✅ |
| 3 | AssetHistoryAttribute1 | ATTRIBUTE1 | — | — |
| 4 | AssetHistoryAttribute10 | ATTRIBUTE10 | — | — |
| 5 | AssetHistoryAttribute11 | ATTRIBUTE11 | — | — |
| 6 | AssetHistoryAttribute12 | ATTRIBUTE12 | — | — |
| 7 | AssetHistoryAttribute13 | ATTRIBUTE13 | — | — |
| 8 | AssetHistoryAttribute14 | ATTRIBUTE14 | — | — |
| 9 | AssetHistoryAttribute15 | ATTRIBUTE15 | — | — |
| 10 | AssetHistoryAttribute16 | ATTRIBUTE16 | — | — |
| 11 | AssetHistoryAttribute17 | ATTRIBUTE17 | — | — |
| 12 | AssetHistoryAttribute18 | ATTRIBUTE18 | — | — |
| 13 | AssetHistoryAttribute19 | ATTRIBUTE19 | — | — |
| 14 | AssetHistoryAttribute2 | ATTRIBUTE2 | — | — |
| 15 | AssetHistoryAttribute20 | ATTRIBUTE20 | — | — |
| 16 | AssetHistoryAttribute21 | ATTRIBUTE21 | — | — |
| 17 | AssetHistoryAttribute22 | ATTRIBUTE22 | — | — |
| 18 | AssetHistoryAttribute23 | ATTRIBUTE23 | — | — |
| 19 | AssetHistoryAttribute24 | ATTRIBUTE24 | — | — |
| 20 | AssetHistoryAttribute25 | ATTRIBUTE25 | — | — |
| 21 | AssetHistoryAttribute26 | ATTRIBUTE26 | — | — |
| 22 | AssetHistoryAttribute27 | ATTRIBUTE27 | — | — |
| 23 | AssetHistoryAttribute28 | ATTRIBUTE28 | — | — |
| 24 | AssetHistoryAttribute29 | ATTRIBUTE29 | — | — |
| 25 | AssetHistoryAttribute3 | ATTRIBUTE3 | — | — |
| 26 | AssetHistoryAttribute30 | ATTRIBUTE30 | — | — |
| 27 | AssetHistoryAttribute4 | ATTRIBUTE4 | — | — |
| 28 | AssetHistoryAttribute5 | ATTRIBUTE5 | — | — |
| 29 | AssetHistoryAttribute6 | ATTRIBUTE6 | — | — |
| 30 | AssetHistoryAttribute7 | ATTRIBUTE7 | — | — |
| 31 | AssetHistoryAttribute8 | ATTRIBUTE8 | — | — |
| 32 | AssetHistoryAttribute9 | ATTRIBUTE9 | — | — |
| 33 | AssetHistoryAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 34 | AssetHistoryAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | AssetHistoryAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 36 | AssetHistoryAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 37 | AssetHistoryAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 38 | AssetHistoryAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 39 | AssetHistoryAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 40 | AssetHistoryAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 41 | AssetHistoryAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 42 | AssetHistoryAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 43 | AssetHistoryAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 44 | AssetHistoryBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 45 | AssetHistoryCategoryId | CATEGORY_ID | — | ✅ |
| 46 | AssetHistoryContext | CONTEXT | — | ✅ |
| 47 | AssetHistoryCreatedBy | CREATED_BY | — | ✅ |
| 48 | AssetHistoryCreationDate | CREATION_DATE | — | ✅ |
| 49 | AssetHistoryDateEffective | DATE_EFFECTIVE | — | ✅ |
| 50 | AssetHistoryDateIneffective | DATE_INEFFECTIVE | — | ✅ |
| 51 | AssetHistoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | AssetHistoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | AssetHistoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | AssetHistoryLeaseTypeCode | LEASE_TYPE_CODE | — | ✅ |
| 55 | AssetHistoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 56 | AssetHistoryTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | 🔑 | ✅ |
| 57 | AssetHistoryTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 58 | AssetHistoryUnits | UNITS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
