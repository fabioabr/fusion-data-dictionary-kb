---
id: DOC-OTHER-PVO-TaxRatesTLExtractPVO
doc_type: system-doc
title: "TaxRatesTLExtractPVO — PVO Cross-Module"
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
  - TaxRatesTLExtractPVO
  - taxratestlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRatesTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Rates TLExtract. Acessa as tabelas: ZX_RATES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxRatesTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_rates_tl|ZX_RATES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[zx_rates_tl|ZX_RATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRatesTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaxRatesTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaxRatesTLDescription | DESCRIPTION | — | ✅ |
| 4 | TaxRatesTLLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | TaxRatesTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaxRatesTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TaxRatesTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TaxRatesTLSourceLang | SOURCE_LANG | — | ✅ |
| 9 | TaxRatesTLTaxRateId | TAX_RATE_ID | 🔑 | ✅ |
| 10 | TaxRatesTLTaxRateName | TAX_RATE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
