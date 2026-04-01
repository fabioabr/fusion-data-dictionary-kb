---
id: DOC-OTHER-PVO-AdditionExtractPVO
doc_type: system-doc
title: "AdditionExtractPVO — PVO Cross-Module"
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
  - AdditionExtractPVO
  - additionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AdditionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Addition Extract. Acessa as tabelas: FA_ADDITIONS_B, FA_ADDITIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AdditionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 121 | 2 | 1 | 39 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[fa_additions_b|FA_ADDITIONS_B]] — 111 atributos (1 PKs, 29 BICC)
- [[fa_additions_tl|FA_ADDITIONS_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[fa_additions_b|FA_ADDITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionAssetCategoryId | ASSET_CATEGORY_ID | — | ✅ |
| 2 | AdditionAssetId | ASSET_ID | 🔑 | ✅ |
| 3 | AdditionAssetKeyCcid | ASSET_KEY_CCID | — | ✅ |
| 4 | AdditionAssetNumber | ASSET_NUMBER | — | ✅ |
| 5 | AdditionAssetType | ASSET_TYPE | — | ✅ |
| 6 | AdditionAttribute1 | ATTRIBUTE1 | — | — |
| 7 | AdditionAttribute10 | ATTRIBUTE10 | — | — |
| 8 | AdditionAttribute11 | ATTRIBUTE11 | — | — |
| 9 | AdditionAttribute12 | ATTRIBUTE12 | — | — |
| 10 | AdditionAttribute13 | ATTRIBUTE13 | — | — |
| 11 | AdditionAttribute14 | ATTRIBUTE14 | — | — |
| 12 | AdditionAttribute15 | ATTRIBUTE15 | — | — |
| 13 | AdditionAttribute16 | ATTRIBUTE16 | — | — |
| 14 | AdditionAttribute17 | ATTRIBUTE17 | — | — |
| 15 | AdditionAttribute18 | ATTRIBUTE18 | — | — |
| 16 | AdditionAttribute19 | ATTRIBUTE19 | — | — |
| 17 | AdditionAttribute2 | ATTRIBUTE2 | — | — |
| 18 | AdditionAttribute20 | ATTRIBUTE20 | — | — |
| 19 | AdditionAttribute21 | ATTRIBUTE21 | — | — |
| 20 | AdditionAttribute22 | ATTRIBUTE22 | — | — |
| 21 | AdditionAttribute23 | ATTRIBUTE23 | — | — |
| 22 | AdditionAttribute24 | ATTRIBUTE24 | — | — |
| 23 | AdditionAttribute25 | ATTRIBUTE25 | — | — |
| 24 | AdditionAttribute26 | ATTRIBUTE26 | — | — |
| 25 | AdditionAttribute27 | ATTRIBUTE27 | — | — |
| 26 | AdditionAttribute28 | ATTRIBUTE28 | — | — |
| 27 | AdditionAttribute29 | ATTRIBUTE29 | — | — |
| 28 | AdditionAttribute3 | ATTRIBUTE3 | — | — |
| 29 | AdditionAttribute30 | ATTRIBUTE30 | — | — |
| 30 | AdditionAttribute4 | ATTRIBUTE4 | — | — |
| 31 | AdditionAttribute5 | ATTRIBUTE5 | — | — |
| 32 | AdditionAttribute6 | ATTRIBUTE6 | — | — |
| 33 | AdditionAttribute7 | ATTRIBUTE7 | — | — |
| 34 | AdditionAttribute8 | ATTRIBUTE8 | — | — |
| 35 | AdditionAttribute9 | ATTRIBUTE9 | — | — |
| 36 | AdditionAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 37 | AdditionAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | AdditionAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | AdditionAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | AdditionAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | AdditionAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | AdditionAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 43 | AdditionAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 44 | AdditionAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 45 | AdditionAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 46 | AdditionAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 47 | AdditionCommitment | COMMITMENT | — | ✅ |
| 48 | AdditionContext | CONTEXT | — | ✅ |
| 49 | AdditionCreatedBy | CREATED_BY | — | ✅ |
| 50 | AdditionCreationDate | CREATION_DATE | — | ✅ |
| 51 | AdditionCurrentUnits | CURRENT_UNITS | — | ✅ |
| 52 | AdditionDistributionSourceBook | DISTRIBUTION_SOURCE_BOOK | — | ✅ |
| 53 | AdditionGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 54 | AdditionGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 55 | AdditionGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 56 | AdditionGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 57 | AdditionGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 58 | AdditionGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 59 | AdditionGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 60 | AdditionGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 61 | AdditionGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 62 | AdditionGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 63 | AdditionGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 64 | AdditionGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 65 | AdditionGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 66 | AdditionGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 67 | AdditionGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 68 | AdditionGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 69 | AdditionGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 70 | AdditionGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 71 | AdditionGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 72 | AdditionGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 73 | AdditionGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 74 | AdditionGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 75 | AdditionGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | — |
| 76 | AdditionGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 77 | AdditionGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 78 | AdditionGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 79 | AdditionGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 80 | AdditionGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | — |
| 81 | AdditionGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | — |
| 82 | AdditionGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | — |
| 83 | AdditionGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | — |
| 84 | AdditionGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 85 | AdditionGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 86 | AdditionGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 87 | AdditionGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 88 | AdditionGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 89 | AdditionGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 90 | AdditionGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 91 | AdditionGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 92 | AdditionGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 93 | AdditionGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 94 | AdditionInUseFlag | IN_USE_FLAG | — | ✅ |
| 95 | AdditionIntangibleAssetFlag | INTANGIBLE_ASSET_FLAG | — | ✅ |
| 96 | AdditionInventorial | INVENTORIAL | — | ✅ |
| 97 | AdditionInvestmentLaw | INVESTMENT_LAW | — | ✅ |
| 98 | AdditionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 99 | AdditionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 100 | AdditionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 101 | AdditionLeaseId | LEASE_ID | — | ✅ |
| 102 | AdditionManufacturerName | MANUFACTURER_NAME | — | ✅ |
| 103 | AdditionModelNumber | MODEL_NUMBER | — | ✅ |
| 104 | AdditionNewUsed | NEW_USED | — | ✅ |
| 105 | AdditionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 106 | AdditionOwnedLeased | OWNED_LEASED | — | ✅ |
| 107 | AdditionParentAssetId | PARENT_ASSET_ID | — | ✅ |
| 108 | AdditionProperty12451250Code | PROPERTY_1245_1250_CODE | — | ✅ |
| 109 | AdditionPropertyTypeCode | PROPERTY_TYPE_CODE | — | ✅ |
| 110 | AdditionSerialNumber | SERIAL_NUMBER | — | ✅ |
| 111 | AdditionTagNumber | TAG_NUMBER | — | ✅ |

### [[fa_additions_tl|FA_ADDITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionDescription | DESCRIPTION | — | ✅ |
| 2 | AdditionTranslationLangAssetId | ASSET_ID | — | ✅ |
| 3 | AdditionTranslationLangCreatedBy | CREATED_BY | — | ✅ |
| 4 | AdditionTranslationLangCreationDate | CREATION_DATE | — | ✅ |
| 5 | AdditionTranslationLangLanguage | LANGUAGE | — | ✅ |
| 6 | AdditionTranslationLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AdditionTranslationLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AdditionTranslationLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AdditionTranslationLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AdditionTranslationLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
