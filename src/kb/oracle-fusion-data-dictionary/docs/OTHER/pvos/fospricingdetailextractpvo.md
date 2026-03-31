---
id: DOC-OTHER-PVO-FosPricingDetailExtractPVO
doc_type: system-doc
title: "FosPricingDetailExtractPVO — PVO Cross-Module"
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
  - FosPricingDetailExtractPVO
  - fospricingdetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosPricingDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Pricing Detail Extract. Acessa as tabelas: FOS_PRICING_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosPricingDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_pricing_details|FOS_PRICING_DETAILS]] — 25 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[fos_pricing_details|FOS_PRICING_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingDetailPEOAgreementFtrId | AGREEMENT_FTR_ID | — | ✅ |
| 2 | PricingDetailPEOAsOnEffectiveDate | AS_ON_EFFECTIVE_DATE | — | ✅ |
| 3 | PricingDetailPEOBasis | BASIS | — | ✅ |
| 4 | PricingDetailPEOChargeId | CHARGE_ID | — | ✅ |
| 5 | PricingDetailPEOConversionType | CONVERSION_TYPE | — | ✅ |
| 6 | PricingDetailPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PricingDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PricingDetailPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | PricingDetailPEODocumentId | DOCUMENT_ID | — | ✅ |
| 10 | PricingDetailPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 11 | PricingDetailPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 12 | PricingDetailPEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 13 | PricingDetailPEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 14 | PricingDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | PricingDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | PricingDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | PricingDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | PricingDetailPEOPriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 19 | PricingDetailPEOPriceType | PRICE_TYPE | — | ✅ |
| 20 | PricingDetailPEOPricingDetailId | PRICING_DETAIL_ID | 🔑 | ✅ |
| 21 | PricingDetailPEOPricingId | PRICING_ID | — | ✅ |
| 22 | PricingDetailPEOReferenceInformation | REFERENCE_INFORMATION | — | ✅ |
| 23 | PricingDetailPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 24 | PricingDetailPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 25 | PricingDetailPEOUnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
