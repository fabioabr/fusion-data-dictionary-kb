---
id: DOC-OTHER-PVO-WSHLookupsDeliveryLineStatusPVO
doc_type: system-doc
title: "WSHLookupsDeliveryLineStatusPVO — PVO Cross-Module"
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
  - WSHLookupsDeliveryLineStatusPVO
  - wshlookupsdeliverylinestatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WSHLookupsDeliveryLineStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WSHLookups Delivery Line Status. Acessa as tabelas: WSH_LOOKUPS.

**Caminho:** `FscmTopModelAM.WshCommonAM.WSHLookupsDeliveryLineStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 2 | 3 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[wsh_lookups|WSH_LOOKUPS]] — 7 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[wsh_lookups|WSH_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 2 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 3 | ShippingLookupEODescription | DESCRIPTION | — | — |
| 4 | ShippingLookupEOEnabledFlag | ENABLED_FLAG | — | — |
| 5 | ShippingLookupEOEndDateActive | END_DATE_ACTIVE | — | — |
| 6 | ShippingLookupEOMeaning | MEANING | — | ✅ |
| 7 | ShippingLookupEOStartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
