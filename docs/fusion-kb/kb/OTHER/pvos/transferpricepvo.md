---
id: DOC-OTHER-PVO-TransferPricePVO
doc_type: system-doc
title: "TransferPricePVO — PVO Cross-Module"
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
  - TransferPricePVO
  - transferpricepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransferPricePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transfer Price. Acessa as tabelas: FOS_TRANSFER_PRICE_V.

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.TransferPricePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 1 | 1 | 34 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[fos_transfer_price_v|FOS_TRANSFER_PRICE_V]] — 39 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[fos_transfer_price_v|FOS_TRANSFER_PRICE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TpItemCostBasisFlag | TP_ITEM_COST_BASIS_FLAG | — | — |
| 2 | TpItemCostMarkupValue | TP_ITEM_COST_MARKUP_VALUE | — | — |
| 3 | TransferPricePEOAgreementFtrId | AGREEMENT_FTR_ID | — | ✅ |
| 4 | TransferPricePEOAsOnEffectiveDate | AS_ON_EFFECTIVE_DATE | — | — |
| 5 | TransferPricePEOBasis | BASIS | — | ✅ |
| 6 | TransferPricePEOChargeId | CHARGE_ID | — | ✅ |
| 7 | TransferPricePEOConversionType | CONVERSION_TYPE | — | ✅ |
| 8 | TransferPricePEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | TransferPricePEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | TransferPricePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | TransferPricePEODocumentId | DOCUMENT_ID | — | ✅ |
| 12 | TransferPricePEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 13 | TransferPricePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 14 | TransferPricePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | TransferPricePEOEventDataId | EVENT_DATA_ID | — | — |
| 16 | TransferPricePEOEventDefinitionId | EVENT_DEFINITION_ID | — | — |
| 17 | TransferPricePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | TransferPricePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | TransferPricePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | TransferPricePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | TransferPricePEOPriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 22 | TransferPricePEOPriceType | PRICE_TYPE | — | ✅ |
| 23 | TransferPricePEOPricingDetailId | PRICING_DETAIL_ID | 🔑 | ✅ |
| 24 | TransferPricePEOPricingId | PRICING_ID | — | ✅ |
| 25 | TransferPricePEOPricingOptionDesc | PRICING_OPTION_DESC | — | ✅ |
| 26 | TransferPricePEOPricingOptionName | PRICING_OPTION_NAME | — | ✅ |
| 27 | TransferPricePEOReferenceInformation | REFERENCE_INFORMATION | — | ✅ |
| 28 | TransferPricePEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 29 | TransferPricePEOTpCostMarkupType | TP_COST_MARKUP_TYPE | — | ✅ |
| 30 | TransferPricePEOTpCostMarkupValue | TP_COST_MARKUP_VALUE | — | ✅ |
| 31 | TransferPricePEOTpDocMarkupType | TP_DOC_MARKUP_TYPE | — | ✅ |
| 32 | TransferPricePEOTpDocMarkupValue | TP_DOC_MARKUP_VALUE | — | ✅ |
| 33 | TransferPricePEOTpDocPriceBasisFlag | TP_DOC_PRICE_BASIS_FLAG | — | ✅ |
| 34 | TransferPricePEOTpOptionsCriteria | TP_OPTIONS_CRITERIA | — | ✅ |
| 35 | TransferPricePEOTpPricingBasisFlag | TP_PRICING_BASIS_FLAG | — | ✅ |
| 36 | TransferPricePEOTpTxnCostBasisFlag | TP_TXN_COST_BASIS_FLAG | — | ✅ |
| 37 | TransferPricePEOTpUseSopriceFlag | TP_USE_SOPRICE_FLAG | — | ✅ |
| 38 | TransferPricePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 39 | TransferPricePEOUnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
