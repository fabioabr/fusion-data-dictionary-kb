---
id: DOC-AR-PVO-TransactionBizCategoriesPVO
doc_type: system-doc
title: "TransactionBizCategoriesPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TransactionBizCategoriesPVO
  - transactionbizcategoriespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionBizCategoriesPVO

## 📌 Visão Geral

Extrai as categorias de negócio fiscal (business categories) aplicáveis às transações de Contas a Receber. Classifica transações para fins de determinação tributária automática e reporte fiscal.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.TransactionBizCategoriesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 6 | 7 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[zx_fc_business_categories_v|ZX_FC_BUSINESS_CATEGORIES_V]] — 13 atributos (6 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[zx_fc_business_categories_v|ZX_FC_BUSINESS_CATEGORIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxBizCategoriesApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | TrxBizCategoriesClassificationCode | CLASSIFICATION_CODE | 🔑 | ✅ |
| 3 | TrxBizCategoriesClassificationCodeLevel | CLASSIFICATION_CODE_LEVEL | — | — |
| 4 | TrxBizCategoriesClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 5 | TrxBizCategoriesClassificationName | CLASSIFICATION_NAME | — | ✅ |
| 6 | TrxBizCategoriesConcatClassifCode | CONCAT_CLASSIF_CODE | — | — |
| 7 | TrxBizCategoriesConcatClassifName | CONCAT_CLASSIF_NAME | — | — |
| 8 | TrxBizCategoriesCountryCode | COUNTRY_CODE | — | — |
| 9 | TrxBizCategoriesEffectiveFrom | EFFECTIVE_FROM | — | — |
| 10 | TrxBizCategoriesEffectiveTo | EFFECTIVE_TO | — | — |
| 11 | TrxBizCategoriesEntityCode | ENTITY_CODE | 🔑 | ✅ |
| 12 | TrxBizCategoriesEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 13 | TrxBizCategoriesTaxEvntClsCode | TAX_EVNT_CLS_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
