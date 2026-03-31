---
id: DOC-OTHER-PVO-RetirementExtractPVO
doc_type: system-doc
title: "RetirementExtractPVO — PVO Cross-Module"
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
  - RetirementExtractPVO
  - retirementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RetirementExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Retirement Extract. Acessa as tabelas: FA_RETIREMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.RetirementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 1 | 1 | 42 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[fa_retirements|FA_RETIREMENTS]] — 68 atributos (1 PKs, 42 BICC)

---

## ⚙️ Atributos

### [[fa_retirements|FA_RETIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RetirementAssetId | ASSET_ID | — | ✅ |
| 2 | RetirementAttribute1 | ATTRIBUTE1 | — | — |
| 3 | RetirementAttribute10 | ATTRIBUTE10 | — | — |
| 4 | RetirementAttribute11 | ATTRIBUTE11 | — | — |
| 5 | RetirementAttribute12 | ATTRIBUTE12 | — | — |
| 6 | RetirementAttribute13 | ATTRIBUTE13 | — | — |
| 7 | RetirementAttribute14 | ATTRIBUTE14 | — | — |
| 8 | RetirementAttribute15 | ATTRIBUTE15 | — | — |
| 9 | RetirementAttribute2 | ATTRIBUTE2 | — | — |
| 10 | RetirementAttribute3 | ATTRIBUTE3 | — | — |
| 11 | RetirementAttribute4 | ATTRIBUTE4 | — | — |
| 12 | RetirementAttribute5 | ATTRIBUTE5 | — | — |
| 13 | RetirementAttribute6 | ATTRIBUTE6 | — | — |
| 14 | RetirementAttribute7 | ATTRIBUTE7 | — | — |
| 15 | RetirementAttribute8 | ATTRIBUTE8 | — | — |
| 16 | RetirementAttribute9 | ATTRIBUTE9 | — | — |
| 17 | RetirementAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 18 | RetirementAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 19 | RetirementAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 20 | RetirementAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 21 | RetirementAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 22 | RetirementAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 23 | RetirementAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 24 | RetirementAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 25 | RetirementAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 26 | RetirementAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 27 | RetirementAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 28 | RetirementBonusReserveRetired | BONUS_RESERVE_RETIRED | — | ✅ |
| 29 | RetirementBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 30 | RetirementCostOfRemoval | COST_OF_REMOVAL | — | ✅ |
| 31 | RetirementCostRetired | COST_RETIRED | — | ✅ |
| 32 | RetirementCreatedBy | CREATED_BY | — | ✅ |
| 33 | RetirementCreationDate | CREATION_DATE | — | ✅ |
| 34 | RetirementDateEffective | DATE_EFFECTIVE | — | ✅ |
| 35 | RetirementDateRetired | DATE_RETIRED | — | ✅ |
| 36 | RetirementEofyReserve | EOFY_RESERVE | — | ✅ |
| 37 | RetirementGainLossAmount | GAIN_LOSS_AMOUNT | — | ✅ |
| 38 | RetirementGainLossTypeCode | GAIN_LOSS_TYPE_CODE | — | ✅ |
| 39 | RetirementImpairReserveRetired | IMPAIR_RESERVE_RETIRED | — | ✅ |
| 40 | RetirementItcRecaptureId | ITC_RECAPTURE_ID | — | ✅ |
| 41 | RetirementItcRecaptured | ITC_RECAPTURED | — | ✅ |
| 42 | RetirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | RetirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 44 | RetirementLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 45 | RetirementLimitProceedsFlag | LIMIT_PROCEEDS_FLAG | — | ✅ |
| 46 | RetirementNbvRetired | NBV_RETIRED | — | ✅ |
| 47 | RetirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 48 | RetirementProceedsOfSale | PROCEEDS_OF_SALE | — | ✅ |
| 49 | RetirementRecaptureAmount | RECAPTURE_AMOUNT | — | ✅ |
| 50 | RetirementRecaptureReserveFlag | RECAPTURE_RESERVE_FLAG | — | ✅ |
| 51 | RetirementRecognizeGainLoss | RECOGNIZE_GAIN_LOSS | — | ✅ |
| 52 | RetirementReductionRate | REDUCTION_RATE | — | ✅ |
| 53 | RetirementReferenceNum | REFERENCE_NUM | — | ✅ |
| 54 | RetirementReserveRetired | RESERVE_RETIRED | — | ✅ |
| 55 | RetirementRetirementConventionTypeId | RETIREMENT_CONVENTION_TYPE_ID | — | ✅ |
| 56 | RetirementRetirementId | RETIREMENT_ID | 🔑 | ✅ |
| 57 | RetirementRetirementTypeCode | RETIREMENT_TYPE_CODE | — | ✅ |
| 58 | RetirementRevalReserveRetired | REVAL_RESERVE_RETIRED | — | ✅ |
| 59 | RetirementSoldTo | SOLD_TO | — | ✅ |
| 60 | RetirementStatus | STATUS | — | ✅ |
| 61 | RetirementStlDeprnAmount | STL_DEPRN_AMOUNT | — | ✅ |
| 62 | RetirementStlMethodId | STL_METHOD_ID | — | ✅ |
| 63 | RetirementTerminalGainLoss | TERMINAL_GAIN_LOSS | — | ✅ |
| 64 | RetirementTradeInAssetId | TRADE_IN_ASSET_ID | — | ✅ |
| 65 | RetirementTransactionHeaderIdIn | TRANSACTION_HEADER_ID_IN | — | ✅ |
| 66 | RetirementTransactionHeaderIdOut | TRANSACTION_HEADER_ID_OUT | — | ✅ |
| 67 | RetirementUnits | UNITS | — | ✅ |
| 68 | RetirementUnrevaluedCostRetired | UNREVALUED_COST_RETIRED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
