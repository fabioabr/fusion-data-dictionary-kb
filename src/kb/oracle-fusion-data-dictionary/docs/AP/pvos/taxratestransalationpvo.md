---
id: DOC-AP-PVO-TaxRatesTransalationPVO
doc_type: system-doc
title: "TaxRatesTransalationPVO — PVO Accounts Payable"
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
  - TaxRatesTransalationPVO
  - taxratestransalationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRatesTransalationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes de alíquotas fiscais para diferentes idiomas. Necessário para conformidade tributária em operações multinacionais, garantindo que as alíquotas sejam identificáveis no idioma local.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.TaxRatesTransalationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 4 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[zx_rates_tl|ZX_RATES_TL]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[zx_rates_tl|ZX_RATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | TaxRateId | TAX_RATE_ID | 🔑 | ✅ |
| 3 | TaxRatesTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | TaxRatesTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | TaxRatesTLPEODescription | DESCRIPTION | — | — |
| 6 | TaxRatesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TaxRatesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TaxRatesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TaxRatesTLPEOSourceLang | SOURCE_LANG | — | — |
| 10 | TaxRatesTLPEOTaxRateName | TAX_RATE_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
