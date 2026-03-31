---
id: DOC-OTHER-PVO-FosPricingOptionExtractPVO
doc_type: system-doc
title: "FosPricingOptionExtractPVO — PVO Cross-Module"
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
  - FosPricingOptionExtractPVO
  - fospricingoptionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosPricingOptionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Pricing Option Extract. Acessa as tabelas: FOS_PRICING_OPTION_F.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosPricingOptionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_pricing_option_f|FOS_PRICING_OPTION_F]] — 21 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[fos_pricing_option_f|FOS_PRICING_OPTION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingOptionDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PricingOptionDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PricingOptionDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | PricingOptionDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | PricingOptionDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | PricingOptionDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PricingOptionDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PricingOptionDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PricingOptionDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PricingOptionDPEOPricingId | PRICING_ID | 🔑 | ✅ |
| 11 | PricingOptionDPEOPricingOptionDescription | PRICING_OPTION_DESC | — | ✅ |
| 12 | PricingOptionDPEOPricingOptionName | PRICING_OPTION_NAME | — | ✅ |
| 13 | PricingOptionDPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 14 | PricingOptionDPEOTpItemCostBasisFlag | TP_ITEM_COST_BASIS_FLAG | — | ✅ |
| 15 | PricingOptionDPEOTpItemCostMarkupValue | TP_ITEM_COST_MARKUP_VALUE | — | ✅ |
| 16 | PricingOptionDPEOTransferPriceCostBasisMarkupType | TP_COST_MARKUP_TYPE | — | ✅ |
| 17 | PricingOptionDPEOTransferPriceCostBasisMarkupValue | TP_COST_MARKUP_VALUE | — | ✅ |
| 18 | PricingOptionDPEOTransferPriceSourceDocMarkupType | TP_DOC_MARKUP_TYPE | — | ✅ |
| 19 | PricingOptionDPEOTransferPriceSourceDocumentMarkupValue | TP_DOC_MARKUP_VALUE | — | ✅ |
| 20 | PricingOptionDPEOTransferPriceSourceDocumentPriceBasisFlag | TP_DOC_PRICE_BASIS_FLAG | — | ✅ |
| 21 | PricingOptionDPEOTransferPriceTransactionCostBasisFlag | TP_TXN_COST_BASIS_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
