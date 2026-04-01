---
id: DOC-OTHER-PVO-ManufacturerExtractPVO
doc_type: system-doc
title: "ManufacturerExtractPVO — PVO Cross-Module"
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
  - ManufacturerExtractPVO
  - manufacturerextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManufacturerExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manufacturer Extract. Acessa as tabelas: EGP_MANUFACTURER.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ManufacturerExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_manufacturer|EGP_MANUFACTURER]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[egp_manufacturer|EGP_MANUFACTURER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | Brands | BRANDS | — | ✅ |
| 3 | Channels | CHANNELS | — | ✅ |
| 4 | Classifications | CLASSIFICATIONS | — | ✅ |
| 5 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 9 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | FormattedDescription | FORMATTED_DESCRIPTION | — | ✅ |
| 11 | GlobalRevenue | GLOBAL_REVENUE | — | ✅ |
| 12 | HeadcountDetails | HEADCOUNT_DETAILS | — | ✅ |
| 13 | History | HISTORY | — | ✅ |
| 14 | Industry | INDUSTRY | — | ✅ |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | ManufacturerId | PARTY_ID | 🔑 | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | Products | PRODUCTS | — | ✅ |
| 21 | Website | WEBSITE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
