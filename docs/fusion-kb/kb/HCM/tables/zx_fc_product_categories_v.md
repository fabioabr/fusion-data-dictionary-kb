---
id: DOC-HCM-885
doc_type: system-doc
title: "ZX_FC_PRODUCT_CATEGORIES_V — (título a preencher)"
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
  - ZX_FC_PRODUCT_CATEGORIES_V
  - zx_fc_product_categories_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_PRODUCT_CATEGORIES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 2 | CLASSIFICATION_ID | — | — | — | — | — | — |
| 3 | CLASSIFICATION_NAME | — | — | — | — | — | — |
| 4 | CONCAT_LEAF_CODE | — | — | — | — | — | — |
| 5 | CONCAT_LEAF_NAME | — | — | — | — | — | — |
| 6 | COUNTRY_CODE | — | — | — | — | — | — |
| 7 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 8 | EFFECTIVE_TO | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fdinterfaceexceptionsp1|FDInterfaceExceptionsP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName | — |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode1 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo1 | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode1 | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName1 | ✅ |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode2 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom2 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo2 | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode1 | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName1 | — |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode3 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom2 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo2 | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode1 | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName1 | ✅ |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode2 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom2 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo2 | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode1 | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName1 | ✅ |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode3 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom2 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo2 | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode1 | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName1 | ✅ |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode3 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom2 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo2 | — |

### [[interfacefiscaldocumentp1|InterfaceFiscalDocumentP1]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId1 | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName | ✅ |
| CONCAT_LEAF_CODE | ProductCategoriesPEOConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProductCategoriesPEOConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesPEOCountryCode1 | — |
| EFFECTIVE_FROM | ProductCategoriesPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | ProductCategoriesPEOEffectiveTo1 | — |

### [[invoicedistributionpvo|InvoiceDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesPEOClassificationCode | — |
| CLASSIFICATION_ID | ProductCategoriesPEOClassificationId | — |
| CLASSIFICATION_NAME | ProductCategoriesPEOClassificationName | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | ✅ |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |

### [[memolinepvo|MemoLinePVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesClassificationCode | — |
| CLASSIFICATION_ID | ProductCategoriesClassificationId | — |
| CLASSIFICATION_NAME | ProductCategoriesClassificationName | ✅ |
| CONCAT_LEAF_NAME | ProductCategoriesConcatLeafName | — |
| COUNTRY_CODE | ProductCategoriesCountryCode | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesClassificationCode | — |
| CLASSIFICATION_NAME | ProductCategoriesClassificationName | ✅ |
| CONCAT_LEAF_NAME | ProductCategoriesConcatLeafName | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesClassificationCode | — |
| CLASSIFICATION_NAME | ProductCategoriesClassificationName | — |
| CONCAT_LEAF_NAME | ProductCategoriesConcatLeafName | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductCategoriesClassificationCode | — |
| CLASSIFICATION_NAME | ProductCategoriesClassificationName | ✅ |
| CONCAT_LEAF_NAME | ProductCategoriesConcatLeafName | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | — |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | — |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | — |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | ✅ |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdCatClassificationCode | — |
| CLASSIFICATION_ID | ProdCatClassificationId | — |
| CLASSIFICATION_NAME | ProdCatClassificationName | ✅ |
| CONCAT_LEAF_CODE | ProdCatConcatLeafCode | — |
| CONCAT_LEAF_NAME | ProdCatConcatLeafName | — |
| COUNTRY_CODE | ProdCatCountryCode | — |
