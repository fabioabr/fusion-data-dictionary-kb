---
id: DOC-HCM-PVO-CurrencyPVO
doc_type: system-doc
title: "CurrencyPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CurrencyPVO
  - currencypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CurrencyPVO

## 📌 Visão Geral

Disponibiliza moedas para contexto de perfis de talento com descricao. Suporta selecao de moeda em preferencias salariais e compensacao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.CurrencyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 4 | 22% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_currencies_vl|FND_CURRENCIES_VL]] — 18 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_currencies_vl|FND_CURRENCIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrencyPEOContext | CONTEXT | — | — |
| 2 | CurrencyPEOCurrencyCode | CURRENCY_CODE | 🔑 | ✅ |
| 3 | CurrencyPEOCurrencyFlag | CURRENCY_FLAG | — | — |
| 4 | CurrencyPEODeriveEffective | DERIVE_EFFECTIVE | — | — |
| 5 | CurrencyPEODeriveFactor | DERIVE_FACTOR | — | — |
| 6 | CurrencyPEODeriveType | DERIVE_TYPE | — | — |
| 7 | CurrencyPEODescription | DESCRIPTION | — | ✅ |
| 8 | CurrencyPEOEnabledFlag | ENABLED_FLAG | — | — |
| 9 | CurrencyPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 10 | CurrencyPEOExtendedPrecision | EXTENDED_PRECISION | — | — |
| 11 | CurrencyPEOIsoFlag | ISO_FLAG | — | — |
| 12 | CurrencyPEOIssuingTerritoryCode | ISSUING_TERRITORY_CODE | — | — |
| 13 | CurrencyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CurrencyPEOMinimumAccountableUnit | MINIMUM_ACCOUNTABLE_UNIT | — | — |
| 15 | CurrencyPEOName | NAME | — | ✅ |
| 16 | CurrencyPEOPrecision | PRECISION | — | — |
| 17 | CurrencyPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 18 | CurrencyPEOSymbol | SYMBOL | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
