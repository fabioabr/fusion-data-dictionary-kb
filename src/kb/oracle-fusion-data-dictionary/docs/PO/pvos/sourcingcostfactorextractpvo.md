---
id: DOC-PO-PVO-SourcingCostFactorExtractPVO
doc_type: system-doc
title: "SourcingCostFactorExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SourcingCostFactorExtractPVO
  - sourcingcostfactorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingCostFactorExtractPVO

## 📌 Visão Geral

Extrai os fatores de custo configurados para processos de sourcing (frete, imposto, seguro, desconto) para carga BICC. Permite padronização de componentes de preço e análise de TCO.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.SourcingCostFactorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 3 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_price_elements|PON_PRICE_ELEMENTS]] — 18 atributos (3 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[pon_price_elements|PON_PRICE_ELEMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DisplayTargetFlag | DISPLAY_TARGET_FLAG | — | ✅ |
| 5 | DisplayToSuppliersFlag | DISPLAY_TO_SUPPLIERS_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PfType | PF_TYPE | — | ✅ |
| 12 | PriceElementTypeId | PRICE_ELEMENT_TYPE_ID | — | ✅ |
| 13 | PricingBasis | PRICING_BASIS | — | ✅ |
| 14 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 15 | ProgramName | PROGRAM_NAME | — | ✅ |
| 16 | RequestId | REQUEST_ID | — | ✅ |
| 17 | SequenceNumber | SEQUENCE_NUMBER | 🔑 | ✅ |
| 18 | Value | VALUE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
