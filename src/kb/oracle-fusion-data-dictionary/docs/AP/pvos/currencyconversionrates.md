---
id: DOC-AP-PVO-CurrencyConversionRates
doc_type: system-doc
title: "CurrencyConversionRates — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CurrencyConversionRates
  - currencyconversionrates
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CurrencyConversionRates

## 📌 Visão Geral

Extrai as taxas de conversão de moedas utilizadas no módulo de compensação por incentivos (ICM), incluindo moedas de origem/destino, taxas e datas de vigência. Fundamental para cálculos de comissões em operações multimoeda e reconciliação de valores entre diferentes moedas.

**Caminho:** `FscmTopModelAM.ApplicationSetupAM.CurrencyConversionRates`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 1 | 1 | 13 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[cn_conversion_rates|CN_CONVERSION_RATES]] — 35 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cn_conversion_rates|CN_CONVERSION_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | Context | CONTEXT | — | — |
| 18 | ConversionDate | CONVERSION_DATE | — | ✅ |
| 19 | ConversionEndDate | CONVERSION_END_DATE | — | ✅ |
| 20 | ConversionRate | CONVERSION_RATE | — | ✅ |
| 21 | ConversionRateId | CONVERSION_RATE_ID | 🔑 | ✅ |
| 22 | ConversionStartDate | CONVERSION_START_DATE | — | ✅ |
| 23 | ConversionTypeId | CONVERSION_TYPE_ID | — | ✅ |
| 24 | CreatedBy | CREATED_BY | — | — |
| 25 | CreationDate | CREATION_DATE | — | — |
| 26 | FromCurrency | FROM_CURRENCY | — | ✅ |
| 27 | InverseConvRate | INVERSE_CONV_RATE | — | ✅ |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | MonetaryFlag | MONETARY_FLAG | — | ✅ |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | RateSourceCode | RATE_SOURCE_CODE | — | ✅ |
| 34 | StatusCode | STATUS_CODE | — | ✅ |
| 35 | ToCurrency | TO_CURRENCY | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
