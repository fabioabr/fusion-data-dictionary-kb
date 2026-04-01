---
id: DOC-OTHER-PVO-ProgramTypeExtractPVO
doc_type: system-doc
title: "ProgramTypeExtractPVO — PVO Cross-Module"
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
  - ProgramTypeExtractPVO
  - programtypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program Type Extract. Acessa as tabelas: CJM_PROGRAM_TYPES_B.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CjmBiccExtractAM.ProgramTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cjm_program_types_b|CJM_PROGRAM_TYPES_B]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[cjm_program_types_b|CJM_PROGRAM_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualBasisId | ACCRUAL_BASIS_ID | — | ✅ |
| 2 | AccrualDiscountTypeCode | ACCRUAL_DISCOUNT_TYPE_CODE | — | ✅ |
| 3 | ChargeSubtypeCode | CHARGE_SUBTYPE_CODE | — | ✅ |
| 4 | ChargeTypeCode | CHARGE_TYPE_CODE | — | ✅ |
| 5 | CostPriceBasisId | COST_PRICE_BASIS_ID | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | CustomerProgram | CUSTOMER_PROGRAM | — | ✅ |
| 9 | DefaultCalcMethodCode | DEFAULT_CALC_METHOD_CODE | — | ✅ |
| 10 | DefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | ✅ |
| 11 | DefaultProdContextCode | DEFAULT_PROD_CONTEXT_CODE | — | ✅ |
| 12 | DefaultTierTypeCode | DEFAULT_TIER_TYPE_CODE | — | ✅ |
| 13 | DiscountAppliedToCode | DISCOUNT_APPLIED_TO_CODE | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | OverrideProgram | OVERRIDE_PROGRAM | — | ✅ |
| 19 | ParentProgramTypeId | PARENT_PROGRAM_TYPE_ID | — | ✅ |
| 20 | PriceTypeCode | PRICE_TYPE_CODE | — | ✅ |
| 21 | PricingDateTypeCode | PRICING_DATE_TYPE_CODE | — | ✅ |
| 22 | ProgramCodePrefix | PROGRAM_CODE_PREFIX | — | ✅ |
| 23 | ProgramTypeCode | PROGRAM_TYPE_CODE | — | ✅ |
| 24 | ProgramTypeId | PROGRAM_TYPE_ID | 🔑 | ✅ |
| 25 | RequestOnlyFlag | REQUEST_ONLY_FLAG | — | ✅ |
| 26 | SeededFlag | SEEDED_FLAG | — | ✅ |
| 27 | SeededProgramTypeCode | SEEDED_PROGRAM_TYPE_CODE | — | ✅ |
| 28 | SoldBySalesMethodCode | SOLD_BY_SALES_METHOD_CODE | — | ✅ |
| 29 | StatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
