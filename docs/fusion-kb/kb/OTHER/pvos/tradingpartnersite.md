---
id: DOC-OTHER-PVO-TradingPartnerSite
doc_type: system-doc
title: "TradingPartnerSite — PVO Cross-Module"
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
  - TradingPartnerSite
  - tradingpartnersite
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TradingPartnerSite

## 📌 Visão Geral

View Object para extração BICC de dados de Trading Partner Site. Acessa as tabelas: MSC_TRADING_PARTNER_SITES.

**Caminho:** `FscmTopModelAM.DooTopAM.TradingPartnerSite`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 7 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[msc_trading_partner_sites|MSC_TRADING_PARTNER_SITES]] — 17 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[msc_trading_partner_sites|MSC_TRADING_PARTNER_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | City | CITY | — | ✅ |
| 2 | Country | COUNTRY | — | ✅ |
| 3 | Location | LOCATION | — | — |
| 4 | LocationId | LOCATION_ID | — | — |
| 5 | OperatingUnitName | OPERATING_UNIT_NAME | — | — |
| 6 | PartnerAddress | PARTNER_ADDRESS | — | ✅ |
| 7 | PartnerId | PARTNER_ID | — | — |
| 8 | PartnerName | PARTNER_NAME | — | — |
| 9 | PartnerSiteId | PARTNER_SITE_ID | 🔑 | ✅ |
| 10 | PartnerType | PARTNER_TYPE | — | — |
| 11 | PostalCode | POSTAL_CODE | — | ✅ |
| 12 | ShippingControl | SHIPPING_CONTROL | — | — |
| 13 | SrInstanceId | SR_INSTANCE_ID | — | — |
| 14 | SrTpId | SR_TP_ID | — | — |
| 15 | SrTpSiteId | SR_TP_SITE_ID | — | — |
| 16 | State | STATE | — | ✅ |
| 17 | TpSiteCode | TP_SITE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
