---
id: DOC-HCM-880
doc_type: system-doc
title: "ZX_FC_BUSINESS_CATEGORIES_V — (título a preencher)"
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
  - ZX_FC_BUSINESS_CATEGORIES_V
  - zx_fc_business_categories_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_BUSINESS_CATEGORIES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLICATION_ID | — | — | — | — | — | — |
| 2 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 3 | CLASSIFICATION_CODE_LEVEL | — | — | — | — | — | — |
| 4 | CLASSIFICATION_ID | — | — | — | — | — | — |
| 5 | CLASSIFICATION_NAME | — | — | — | — | — | — |
| 6 | CONCAT_CLASSIF_CODE | — | — | — | — | — | — |
| 7 | CONCAT_CLASSIF_NAME | — | — | — | — | — | — |
| 8 | COUNTRY_CODE | — | — | — | — | — | — |
| 9 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 10 | EFFECTIVE_TO | — | — | — | — | — | — |
| 11 | ENTITY_CODE | — | — | — | — | — | — |
| 12 | EVENT_CLASS_CODE | — | — | — | — | — | — |
| 13 | TAX_EVNT_CLS_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | TransactionBizCategoriesApplicationId | — |
| CLASSIFICATION_CODE | TransactionBizCategoriesClassificationCode | — |
| CLASSIFICATION_ID | TransactionBizCategoriesClassificationId | — |
| CLASSIFICATION_NAME | TransactionBizCategoriesClassificationName | ✅ |
| CONCAT_CLASSIF_CODE | TransactionBizCategoriesConcatClassifCode | — |
| ENTITY_CODE | TransactionBizCategoriesEntityCode | — |
| EVENT_CLASS_CODE | TransactionBizCategoriesEventClassCode | — |
| TAX_EVNT_CLS_CODE | TransactionBizCategoriesTaxEvntClsCode | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | TransactionBizCategoriesApplicationId | — |
| CLASSIFICATION_CODE | TransactionBizCategoriesClassificationCode | — |
| CLASSIFICATION_ID | TransactionBizCategoriesClassificationId | — |
| CLASSIFICATION_NAME | TransactionBizCategoriesClassificationName | — |
| CONCAT_CLASSIF_CODE | TransactionBizCategoriesConcatClassifCode | — |
| ENTITY_CODE | TransactionBizCategoriesEntityCode | — |
| EVENT_CLASS_CODE | TransactionBizCategoriesEventClassCode | — |
| TAX_EVNT_CLS_CODE | TransactionBizCategoriesTaxEvntClsCode | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | TransactionBizCategoriesApplicationId | — |
| CLASSIFICATION_CODE | TransactionBizCategoriesClassificationCode | — |
| CLASSIFICATION_ID | TransactionBizCategoriesClassificationId | — |
| CLASSIFICATION_NAME | TransactionBizCategoriesClassificationName | ✅ |
| CONCAT_CLASSIF_CODE | TransactionBizCategoriesConcatClassifCode | — |
| ENTITY_CODE | TransactionBizCategoriesEntityCode | — |
| EVENT_CLASS_CODE | TransactionBizCategoriesEventClassCode | — |
| TAX_EVNT_CLS_CODE | TransactionBizCategoriesTaxEvntClsCode | — |

### [[transactionbizcategoriespvo|TransactionBizCategoriesPVO]] (AR · BICC: 7/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | TrxBizCategoriesApplicationId | ✅ |
| CLASSIFICATION_CODE | TrxBizCategoriesClassificationCode | ✅ |
| CLASSIFICATION_CODE_LEVEL | TrxBizCategoriesClassificationCodeLevel | — |
| CLASSIFICATION_ID | TrxBizCategoriesClassificationId | ✅ |
| CLASSIFICATION_NAME | TrxBizCategoriesClassificationName | ✅ |
| CONCAT_CLASSIF_CODE | TrxBizCategoriesConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | TrxBizCategoriesConcatClassifName | — |
| COUNTRY_CODE | TrxBizCategoriesCountryCode | — |
| EFFECTIVE_FROM | TrxBizCategoriesEffectiveFrom | — |
| EFFECTIVE_TO | TrxBizCategoriesEffectiveTo | — |
| ENTITY_CODE | TrxBizCategoriesEntityCode | ✅ |
| EVENT_CLASS_CODE | TrxBizCategoriesEventClassCode | ✅ |
| TAX_EVNT_CLS_CODE | TrxBizCategoriesTaxEvntClsCode | ✅ |
