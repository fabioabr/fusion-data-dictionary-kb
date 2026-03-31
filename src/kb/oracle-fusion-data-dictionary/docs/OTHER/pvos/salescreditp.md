---
id: DOC-OTHER-PVO-SalesCreditP
doc_type: system-doc
title: "SalesCreditP — PVO Cross-Module"
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
  - SalesCreditP
  - salescreditp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalesCreditP

## 📌 Visão Geral

View Object para extração BICC de dados de Sales Credit P. Acessa as tabelas: AR_SALES_CREDIT_TYPES, OKC_K_SALES_CREDITS, RA_SALESREPS.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.SalesCreditP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 3 | 2 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_sales_credit_types|AR_SALES_CREDIT_TYPES]] — 5 atributos (5 BICC)
- [[okc_k_sales_credits|OKC_K_SALES_CREDITS]] — 14 atributos (2 PKs, 14 BICC)
- [[ra_salesreps|RA_SALESREPS]] — 8 atributos (8 BICC)

---

## ⚙️ Atributos

### [[ar_sales_credit_types|AR_SALES_CREDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesCreditTypePEODescription | DESCRIPTION | — | ✅ |
| 2 | SalesCreditTypePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 3 | SalesCreditTypePEOName | NAME | — | ✅ |
| 4 | SalesCreditTypePEOQuotaFlag | QUOTA_FLAG | — | ✅ |
| 5 | SalesCreditTypeSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | ✅ |

### [[okc_k_sales_credits|OKC_K_SALES_CREDITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesCreditPEOActiveYn | ACTIVE_YN | — | ✅ |
| 2 | SalesCreditPEOChrId | CHR_ID | — | ✅ |
| 3 | SalesCreditPEOCleId | CLE_ID | — | ✅ |
| 4 | SalesCreditPEODnzChrId | DNZ_CHR_ID | — | ✅ |
| 5 | SalesCreditPEOEndDate | END_DATE | — | ✅ |
| 6 | SalesCreditPEOExternalKey1 | EXTERNAL_KEY1 | — | ✅ |
| 7 | SalesCreditPEOExternalKey2 | EXTERNAL_KEY2 | — | ✅ |
| 8 | SalesCreditPEOId | ID | 🔑 | ✅ |
| 9 | SalesCreditPEOMajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 10 | SalesCreditPEOPercent | PERCENT | — | ✅ |
| 11 | SalesCreditPEOSalesrepId | SALESREP_ID | — | ✅ |
| 12 | SalesCreditPEOStartDate | START_DATE | — | ✅ |
| 13 | SalesCreditPEOVersionType | VERSION_TYPE | — | ✅ |
| 14 | SalesCreditSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | ✅ |

### [[ra_salesreps|RA_SALESREPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesrepRaPEOName | NAME | — | ✅ |
| 2 | SalesrepRaPEOPartyId | PARTY_ID | — | ✅ |
| 3 | SalesrepRaPEOSalesTaxGeocode | SALES_TAX_GEOCODE | — | ✅ |
| 4 | SalesrepRaPEOSalesrepNumber | SALESREP_NUMBER | — | ✅ |
| 5 | SalesrepRaPEOStatus | STATUS | — | ✅ |
| 6 | SalesrepRaResourceSalesrepId | RESOURCE_SALESREP_ID | — | ✅ |
| 7 | SalesrepRaSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | ✅ |
| 8 | SalesrepRaSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
