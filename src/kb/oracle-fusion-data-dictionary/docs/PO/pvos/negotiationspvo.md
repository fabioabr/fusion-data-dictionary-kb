---
id: DOC-PO-PVO-NegotiationsPVO
doc_type: system-doc
title: "NegotiationsPVO — PVO Purchasing"
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
  - NegotiationsPVO
  - negotiationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationsPVO

## 📌 Visão Geral

Extrai os cabeçalhos de negociações de sourcing (RFQ, RFI, Auction, RFP), incluindo tipo de evento, status, datas, regras de precificação e unidade de negócio. Permite análise de processos competitivos e eficácia das estratégias de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 3 | 1 | 3 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]] — 9 atributos (1 PKs, 3 BICC)
- [[pon_auc_doctypes_vl|PON_AUC_DOCTYPES_VL]] — 2 atributos

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBuId | BU_ID | — | — |
| 2 | BusinessUnitBuName | BU_NAME | — | — |

### [[pon_auction_headers_all|PON_AUCTION_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationHeaderAuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 2 | NegotiationHeaderAuctionStatus | AUCTION_STATUS | — | ✅ |
| 3 | NegotiationHeaderAuctionTitle | AUCTION_TITLE | — | ✅ |
| 4 | NegotiationHeaderAwardStatus | AWARD_STATUS | — | — |
| 5 | NegotiationHeaderDocumentNumber | DOCUMENT_NUMBER | — | — |
| 6 | NegotiationHeaderIsTemplateFlag | IS_TEMPLATE_FLAG | — | — |
| 7 | NegotiationHeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | NegotiationHeaderPrcBuId | PRC_BU_ID | — | — |
| 9 | NegotiationHeaderProjectsEnabledFlag | PROJECTS_ENABLED_FLAG | — | — |

### [[pon_auc_doctypes_vl|PON_AUC_DOCTYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationDocumentTypeDoctypeId | DOCTYPE_ID | — | — |
| 2 | NegotiationDocumentTypeName | NAME | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
