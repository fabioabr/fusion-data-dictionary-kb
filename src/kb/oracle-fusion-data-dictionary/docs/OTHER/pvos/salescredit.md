---
id: DOC-OTHER-PVO-SalesCredit
doc_type: system-doc
title: "SalesCredit — PVO Cross-Module"
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
  - SalesCredit
  - salescredit
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalesCredit

## 📌 Visão Geral

View Object para extração BICC de dados de Sales Credit. Acessa as tabelas: DOO_HEADERS_ALL, DOO_SALES_CREDITS, MSC_SALES_CREDIT_TYPES.

**Caminho:** `FscmTopModelAM.DooTopAM.SalesCredit`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 3 | 1 | 12 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 2 atributos
- [[doo_sales_credits|DOO_SALES_CREDITS]] — 14 atributos (1 PKs, 10 BICC)
- [[msc_sales_credit_types|MSC_SALES_CREDIT_TYPES]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderHeaderId | HEADER_ID | — | — |
| 2 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | — |

### [[doo_sales_credits|DOO_SALES_CREDITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesCreditCreatedBy | CREATED_BY | — | ✅ |
| 2 | SalesCreditCreationDate | CREATION_DATE | — | ✅ |
| 3 | SalesCreditFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 4 | SalesCreditHeaderId | HEADER_ID | — | ✅ |
| 5 | SalesCreditId | SALES_CREDIT_ID | 🔑 | ✅ |
| 6 | SalesCreditLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SalesCreditLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SalesCreditLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SalesCreditLineId | LINE_ID | — | ✅ |
| 10 | SalesCreditObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | SalesCreditOrigSysSalesCreditRef | ORIG_SYS_SALES_CREDIT_REF | — | — |
| 12 | SalesCreditPercent | PERCENT | — | ✅ |
| 13 | SalesCreditSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | — |
| 14 | SalesCreditSalespersonId | SALESPERSON_ID | — | ✅ |

### [[msc_sales_credit_types|MSC_SALES_CREDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesCreditTypeDescription | DESCRIPTION | — | ✅ |
| 2 | SalesCreditTypeEnabledFlag | ENABLED_FLAG | — | — |
| 3 | SalesCreditTypeName | NAME | — | ✅ |
| 4 | SalesCreditTypeRefreshNumber | REFRESH_NUMBER | — | — |
| 5 | SalesCreditTypeSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
