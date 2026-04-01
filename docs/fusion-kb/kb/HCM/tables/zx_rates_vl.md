---
id: DOC-HCM-899
doc_type: system-doc
title: "ZX_RATES_VL — (título a preencher)"
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
  - ZX_RATES_VL
  - zx_rates_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_RATES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESCRIPTION | — | — | — | — | — | — |
| 2 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 3 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 4 | TAX_RATE_CODE | — | — | — | — | — | — |
| 5 | TAX_RATE_ID | — | — | — | — | — | — |
| 6 | TAX_RATE_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 5/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | WhtRatesDescription | ✅ |
| LAST_UPDATE_DATE | TaxRateLastUpdateDate | ✅ |
| LAST_UPDATED_BY | TaxRateLastUpdatedBy | — |
| TAX_RATE_CODE | WhtRatesTaxRateCode | ✅ |
| TAX_RATE_ID | TaxRateTaxRateId | — |
| TAX_RATE_ID | WhtRatesTaxRateId | — |
| TAX_RATE_NAME | TaxRateTaxRateName | ✅ |
| TAX_RATE_NAME | WhtRatesTaxRateName | ✅ |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | TaxRateLastUpdateDate | ✅ |
| TAX_RATE_ID | TaxRateTaxRateId | — |
