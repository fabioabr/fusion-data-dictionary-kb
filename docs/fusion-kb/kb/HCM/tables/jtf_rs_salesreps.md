---
id: DOC-HCM-654
doc_type: system-doc
title: "JTF_RS_SALESREPS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - JTF_RS_SALESREPS
  - jtf_rs_salesreps
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# JTF_RS_SALESREPS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 4 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 5 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 6 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 7 | RESOURCE_ID | — | — | — | — | — | — |
| 8 | RESOURCE_SALESREP_ID | — | — | — | — | — | — |
| 9 | SALESREP_NUMBER | — | — | — | — | — | — |
| 10 | SALES_CREDIT_TYPE_ID | — | — | — | — | — | — |
| 11 | SALES_TAX_GEOCODE | — | — | — | — | — | — |
| 12 | SALES_TAX_INSIDE_CITY_LIMITS | — | — | — | — | — | — |
| 13 | SET_ID | — | — | — | — | — | — |
| 14 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 15 | STATUS | — | — | — | — | — | — |
| 16 | WH_UPDATE_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[referenceaccount|ReferenceAccount]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RESOURCE_ID | ResourceSalesrepResourceId | — |
| RESOURCE_SALESREP_ID | ResourceSalesrepResourceSalesrepId | — |
| STATUS | ResourceSalesrepStatus | — |

### [[salesrep|SalesRep]] (OTHER · BICC: 8/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ResourceSalesrepPEOCreatedBy | — |
| CREATION_DATE | ResourceSalesrepPEOCreationDate | — |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | ResourceSalesrepPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResourceSalesrepPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResourceSalesrepPEOLastUpdatedBy | — |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_SALESREP_ID | ResourceSalesrepId | ✅ |
| SALES_CREDIT_TYPE_ID | SalesCreditTypeId | ✅ |
| SALES_TAX_GEOCODE | SalesTaxGeocode | — |
| SALES_TAX_INSIDE_CITY_LIMITS | SalesTaxInsideCityLimits | — |
| SALESREP_NUMBER | SalesrepNumber | ✅ |
| SET_ID | SetId | — |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| STATUS | ResourceSalesrepPEOStatus | ✅ |
| WH_UPDATE_DATE | WhUpdateDate | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RESOURCE_ID | ResourceSalesrepResourceId | — |
| RESOURCE_SALESREP_ID | ResourceSalesrepResourceSalesrepId | — |
