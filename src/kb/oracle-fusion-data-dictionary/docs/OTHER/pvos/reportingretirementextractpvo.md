---
id: DOC-OTHER-PVO-ReportingRetirementExtractPVO
doc_type: system-doc
title: "ReportingRetirementExtractPVO — PVO Cross-Module"
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
  - ReportingRetirementExtractPVO
  - reportingretirementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReportingRetirementExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reporting Retirement Extract. Acessa as tabelas: FA_MC_RETIREMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.ReportingRetirementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 1 | 2 | 41 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[fa_mc_retirements|FA_MC_RETIREMENTS]] — 58 atributos (2 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[fa_mc_retirements|FA_MC_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReportingRetirementAssetId | ASSET_ID | — | ✅ |
| 2 | ReportingRetirementAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ReportingRetirementAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ReportingRetirementAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ReportingRetirementAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ReportingRetirementAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ReportingRetirementAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ReportingRetirementAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ReportingRetirementAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ReportingRetirementAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ReportingRetirementAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ReportingRetirementAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ReportingRetirementAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ReportingRetirementAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ReportingRetirementAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ReportingRetirementAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ReportingRetirementAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 18 | ReportingRetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | ✅ |
| 19 | ReportingRetirementBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 20 | ReportingRetirementConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 21 | ReportingRetirementCostOfRemoval | COST_OF_REMOVAL | — | ✅ |
| 22 | ReportingRetirementCostRetired | COST_RETIRED | — | ✅ |
| 23 | ReportingRetirementCreatedBy | CREATED_BY | — | ✅ |
| 24 | ReportingRetirementCreationDate | CREATION_DATE | — | ✅ |
| 25 | ReportingRetirementDateEffective | DATE_EFFECTIVE | — | ✅ |
| 26 | ReportingRetirementDateRetired | DATE_RETIRED | — | ✅ |
| 27 | ReportingRetirementEofyReserve | EOFY_RESERVE | — | ✅ |
| 28 | ReportingRetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | ✅ |
| 29 | ReportingRetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | ✅ |
| 30 | ReportingRetirementImpairReserveRetired | IMPAIR_RESERVE_RETIRED | — | — |
| 31 | ReportingRetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | ReportingRetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | ReportingRetirementLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | ReportingRetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | ✅ |
| 35 | ReportingRetirementNbvRetired | NBV_RETIRED | — | ✅ |
| 36 | ReportingRetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 37 | ReportingRetirementProceedsOfSale | PROCEEDS_OF_SALE | — | ✅ |
| 38 | ReportingRetirementRecaptureAmount | RECAPTURE_AMOUNT | — | ✅ |
| 39 | ReportingRetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | ✅ |
| 40 | ReportingRetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 41 | ReportingRetirementReductionRate | REDUCTION_RATE | — | ✅ |
| 42 | ReportingRetirementReferenceNum | REFERENCE_NUM | — | ✅ |
| 43 | ReportingRetirementReserveRetired | RESERVE_RETIRED | — | ✅ |
| 44 | ReportingRetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | ✅ |
| 45 | ReportingRetirementRetirementId | RETIREMENT_ID | 🔑 | ✅ |
| 46 | ReportingRetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | ✅ |
| 47 | ReportingRetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | ✅ |
| 48 | ReportingRetirementSetOfBooksId | SET_OF_BOOKS_ID | 🔑 | ✅ |
| 49 | ReportingRetirementSoldTo | SOLD_TO | — | ✅ |
| 50 | ReportingRetirementStatus | STATUS | — | ✅ |
| 51 | ReportingRetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | ✅ |
| 52 | ReportingRetirementStlMethodId | STL_METHOD_ID | — | ✅ |
| 53 | ReportingRetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | ✅ |
| 54 | ReportingRetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | ✅ |
| 55 | ReportingRetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 56 | ReportingRetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 57 | ReportingRetirementUnits | UNITS | — | ✅ |
| 58 | ReportingRetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
