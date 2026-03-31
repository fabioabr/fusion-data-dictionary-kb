---
id: DOC-OTHER-PVO-PriceAdjustmentExtractPVO
doc_type: system-doc
title: "PriceAdjustmentExtractPVO — PVO Cross-Module"
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
  - PriceAdjustmentExtractPVO
  - priceadjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PriceAdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Price Adjustment Extract. Acessa as tabelas: DOO_PRICE_ADJUSTMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.PriceAdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_price_adjustments|DOO_PRICE_ADJUSTMENTS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[doo_price_adjustments|DOO_PRICE_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceAdjustmentAdjustmentName | ADJUSTMENT_NAME | — | ✅ |
| 2 | PriceAdjustmentAdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 3 | PriceAdjustmentAmount | AMOUNT | — | ✅ |
| 4 | PriceAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 5 | PriceAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 6 | PriceAdjustmentFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 7 | PriceAdjustmentHeaderId | HEADER_ID | — | ✅ |
| 8 | PriceAdjustmentId | PRICE_ADJUSTMENT_ID | 🔑 | ✅ |
| 9 | PriceAdjustmentInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 10 | PriceAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PriceAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PriceAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PriceAdjustmentLineId | LINE_ID | — | ✅ |
| 14 | PriceAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | PriceAdjustmentOrigSysAdjustmentRef | ORIG_SYS_ADJUSTMENT_REF | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
