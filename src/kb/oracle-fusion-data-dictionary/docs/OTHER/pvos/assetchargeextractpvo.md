---
id: DOC-OTHER-PVO-AssetChargeExtractPVO
doc_type: system-doc
title: "AssetChargeExtractPVO — PVO Cross-Module"
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
  - AssetChargeExtractPVO
  - assetchargeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetChargeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Charge Extract. Acessa as tabelas: CSE_ASSET_CHARGES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.AssetChargeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 1 | 1 | 64 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_asset_charges|CSE_ASSET_CHARGES]] — 64 atributos (1 PKs, 64 BICC)

---

## ⚙️ Atributos

### [[cse_asset_charges|CSE_ASSET_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetChargeId | ASSET_CHARGE_ID | 🔑 | ✅ |
| 2 | AssetId | ASSET_ID | — | ✅ |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 5 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 6 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 7 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 8 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 9 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 10 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 11 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 12 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 13 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 14 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 15 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 16 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 17 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 18 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 19 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 20 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 21 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 22 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 23 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 24 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 29 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 30 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 31 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 32 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 33 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 34 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 35 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 36 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 37 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 38 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 39 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 40 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 41 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 42 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 43 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 44 | ChargeComponentsRollupFlag | CHARGE_COMPONENTS_ROLLUP_FLAG | — | ✅ |
| 45 | ChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | ✅ |
| 46 | ChargesRollupFlag | CHARGES_ROLLUP_FLAG | — | ✅ |
| 47 | CreatedBy | CREATED_BY | — | ✅ |
| 48 | CreationDate | CREATION_DATE | — | ✅ |
| 49 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 50 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 51 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 52 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 54 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 55 | LoadRequestId | LOAD_REQUEST_ID | — | ✅ |
| 56 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 57 | PriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 58 | PriceElementUsageCode | PRICE_ELEMENT_USAGE_CODE | — | ✅ |
| 59 | PricePeriodicityCode | PRICE_PERIODICITY_CODE | — | ✅ |
| 60 | PricedQuantityUomCode | PRICED_QUANTITY_UOM_CODE | — | ✅ |
| 61 | PrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 62 | RequestId | REQUEST_ID | — | ✅ |
| 63 | TaxIncludedFlag | TAX_INCLUDED_FLAG | — | ✅ |
| 64 | UnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
