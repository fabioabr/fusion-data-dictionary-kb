---
id: DOC-OTHER-PVO-CurrencyConversion
doc_type: system-doc
title: "CurrencyConversion — PVO Cross-Module"
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
  - CurrencyConversion
  - currencyconversion
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CurrencyConversion

## 📌 Visão Geral

View Object para extração BICC de dados de Currency Conversion. Acessa as tabelas: MSC_CURRENCY_CONVERSIONS.

**Caminho:** `FscmTopModelAM.DooTopAM.CurrencyConversion`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 5 | 1 | 4 | 4 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[msc_currency_conversions|MSC_CURRENCY_CONVERSIONS]] — 5 atributos (4 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[msc_currency_conversions|MSC_CURRENCY_CONVERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionDate | CONVERSION_DATE | 🔑 | ✅ |
| 2 | ConversionRate | CONVERSION_RATE | — | — |
| 3 | ConversionType | CONVERSION_TYPE | 🔑 | ✅ |
| 4 | FromCurrency | FROM_CURRENCY | 🔑 | ✅ |
| 5 | ToCurrency | TO_CURRENCY | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
